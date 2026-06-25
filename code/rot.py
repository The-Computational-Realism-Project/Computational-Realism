import taichi as ti
import numpy as np

# Enable GPU acceleration
ti.init(arch=ti.gpu)

N = 256  # 3D grid size
center = N // 2

#Psi has 4 real degrees of freedom
p_prev = ti.Vector.field(4, dtype=ti.f32, shape=(N, N, N))
p_curr = ti.Vector.field(4, dtype=ti.f32, shape=(N, N, N))
p_next = ti.Vector.field(4, dtype=ti.f32, shape=(N, N, N))

# 2D pixel field for rendering
pixels = ti.Vector.field(3, dtype=ti.f32, shape=(N, N))

# Constant definitions
kappa = 0.367879  # Grid intrinsic coupling constant 1/e
rho_th = 5.0    # Grid capacity th

@ti.func
def left_M(a, v):
    # Implementation of left-multiplication algebra for generator M_a = gamma_a * I_3
    res = ti.Vector([0.0, 0.0, 0.0, 0.0])
    if a == 2:    # z-axis
        res = ti.Vector([-v[3], v[2], -v[1], v[0]])
    elif a == 1:  # y-axis
        res = ti.Vector([v[2], v[3], -v[0], -v[1]])
    elif a == 0:  # x-axis
        res = ti.Vector([-v[1], v[0], v[3], -v[2]])
    return res

@ti.func
def right_M(a, v):
    # Implementation of right-multiplication algebra for generator M_a = gamma_a * I_3
    res = ti.Vector([0.0, 0.0, 0.0, 0.0])
    if a == 2:    # z-axis
        res = ti.Vector([-v[3], -v[2], v[1], v[0]])
    elif a == 1:  # y-axis
        res = ti.Vector([v[2], -v[3], -v[0], v[1]])
    elif a == 0:  # x-axis
        res = ti.Vector([-v[1], v[0], -v[3], v[2]])
    return res

@ti.func
def apply_rotor_adjoint(a, v, phi):
    # Implementation of adjoint transformation R * Psi * R^-1
    c = ti.cos(phi)
    s = ti.sin(phi)
    
    term1 = c * c * v
    
    # M_a * Psi * M_a
    m_psi = left_M(a, v)
    m_psi_m = right_M(a, m_psi)
    term2 = - s * s * m_psi_m
    
    # M_a * Psi - Psi * M_a
    psi_m = right_M(a, v)
    term3 = s * c * (m_psi - psi_m)
    
    return term1 + term2 + term3

@ti.kernel
def step_wave_spinor(enable_nonlinear: ti.i32):
    # Implementation of multi-dimensional spinor transport dynamics equations
    # Psi(t+1) = 1/3 * sum_a [ R(a) Psi_prev(x - h a) R^-1(a) + R(-a) Psi_prev(x + h a) R^-1(-a) ] - Psi(t-1)
    for i, j, k in p_curr:
        if 0 < i < N-1 and 0 < j < N-1 and 0 < k < N-1:
            
            # Isotropic neighborhood summation
            sum_val = ti.Vector([0.0, 0.0, 0.0, 0.0])
            
            # Traverse three spatial axes: x, y, z
            for axis in ti.static(range(3)):
                # Retrieve neighbor spinor values in positive and negative directions
                v_minus = ti.Vector([0.0, 0.0, 0.0, 0.0])
                v_plus = ti.Vector([0.0, 0.0, 0.0, 0.0])
                
                if axis == 0:
                    v_minus = p_curr[i-1, j, k]
                    v_plus = p_curr[i+1, j, k]
                elif axis == 1:
                    v_minus = p_curr[i, j-1, k]
                    v_plus = p_curr[i, j+1, k]
                elif axis == 2:
                    v_minus = p_curr[i, j, k-1]
                    v_plus = p_curr[i, j, k+1]
                
                phi_minus = 0.0
                phi_plus = 0.0
                
                if enable_nonlinear == 1:
                    # Calculate phase shift angle phi based on local info saturation using optimized single logarithm
                    rho_m = (v_minus[0]**2 + v_minus[1]**2 + v_minus[2]**2 + v_minus[3]**2) / rho_th
                    rho_p = (v_plus[0]**2 + v_plus[1]**2 + v_plus[2]**2 + v_plus[3]**2) / rho_th
                    
                    #Fixed chirality
                    phi_minus = ti.sqrt(1.0 / 8.0 * kappa * ti.log(1.0 + rho_m))
                    phi_plus = ti.sqrt(1.0 / 8.0 * kappa * ti.log(1.0 + rho_p))
                
                # Apply adjoint transformations for both directions and accumulate
                sum_val += apply_rotor_adjoint(axis, v_minus, phi_minus)
                sum_val += apply_rotor_adjoint(axis, v_plus, -phi_plus) # R(-h a) corresponds to negative phase shift
                
            p_next[i, j, k] = (sum_val / 3.0) - p_prev[i, j, k]

@ti.kernel
def apply_smoothing_spinor(epsilon: ti.f32):
    # Non-local smoothing operator exp(a^2 Laplace) for 4-component spinor field
    for i, j, k in p_curr:
        if 1 < i < N-2 and 1 < j < N-2 and 1 < k < N-2:
            laplacian = (p_next[i-1, j, k] + p_next[i+1, j, k] +
                         p_next[i, j-1, k] + p_next[i, j+1, k] +
                         p_next[i, j, k-1] + p_next[i, j, k+1] - 6.0 * p_next[i, j, k])
            p_next[i, j, k] += epsilon * laplacian

@ti.kernel
def update_buffers():
    for i, j, k in p_curr:
        p_prev[i, j, k] = p_curr[i, j, k]
        p_curr[i, j, k] = p_next[i, j, k]



@ti.kernel
def set_spinor_source(t: ti.f32, omega: ti.f32):    
    # Inject a phase-rotating circularly polarized spinor source
    val_sin = ti.sin(omega * t) * 15.0
    val_cos = ti.cos(omega * t) * 15.0
    p_curr[center, center, center] = ti.Vector([val_cos, -val_cos, val_sin, val_sin])
    #p_curr[center+20, center, center] = ti.Vector([val_cos, -val_cos, val_sin, val_sin])


@ti.kernel
def render_slice_spinor():
    display_mode1 = True
    # Slice at Z = N // 2 to visualize the 4-component spinor field as a color image
    for i, j in pixels:
        v = p_curr[i, j, center]
        if display_mode1:
            length = v.norm()
            brightness = ti.math.clamp(length *4, 0.0, 1.0)
            xyz = ti.Vector([v[1], v[2], v[3]])
            xyz_len = xyz.norm()            
            base_rgb = ti.Vector([0.5, 0.5, 0.5])
            if xyz_len > 1e-12:
                base_rgb = (xyz / xyz_len) * 0.5 + 0.5
            pixels[i, j]= base_rgb * brightness
        else:
            r_val = ti.abs(v[0]) * 4.0
            g_val = ti.abs(v[3]) * 4.0
            b_val = ti.sqrt(v[0]**2 + v[1]**2 + v[2]**2 + v[3]**2) * 4.0        
            pixels[i, j] = ti.Vector([r_val, g_val, b_val])

def main():
    gui = ti.GUI("3D Spinor Grid Wave", res=(N, N))
    
    time_step = 0
    omega_low = 0.01
    omega_high = 0.2
    
    current_omega = omega_high
    apply_filter = True
    enable_nonlinear = True
    generator = True

    print("Instructions:")
    print("[L] Key: Low-frequency source")
    print("[H] Key: High-frequency source")
    print("[S] Key: Toggle theoretical non-local smoothing operator")
    print("[N] Key: Toggle logarithmic nonlinear locking")
    print("[R] Key: Reset field")

    while gui.running:
        for e in gui.get_events(ti.GUI.PRESS):
            if e.key in ['l', 'L']:
                current_omega = omega_low
                print("Current state: Low frequency")
            elif e.key in ['h', 'H']:
                current_omega = omega_high
                print("Current state: High frequency")
            elif e.key in ['s', 'S']:
                apply_filter = not apply_filter
                print(f"Non-local smoothing operator: {'ON' if apply_filter else 'OFF'}")
            elif e.key in ['n', 'N']:
                enable_nonlinear = not enable_nonlinear
                print(f"Logarithmic nonlinear phase-lock: {'ON' if enable_nonlinear else 'OFF'}")
            elif e.key in ['g', 'G']:
                generator = not generator
                print(f"Generator : {'ON' if generator else 'OFF'}")
            elif e.key in ['r', 'R']:
                p_prev.fill(0)
                p_curr.fill(0)
                p_next.fill(0)
                time_step = 0
                print("System reset")
        
        for _ in range(2):
            step_wave_spinor(1 if enable_nonlinear else 0)
            if apply_filter:
                apply_smoothing_spinor(0.05)
            update_buffers()
            if generator:
                set_spinor_source(time_step, current_omega)
            time_step += 1
            
        render_slice_spinor()
        gui.set_image(pixels)
        
        status_text = f"Freq: {'High' if current_omega == omega_high else 'Low'} | Non-linear: {'ON' if enable_nonlinear else 'OFF'} | Filter: {'ON' if apply_filter else 'OFF'}"
        gui.text(content=status_text, pos=(0.02, 0.95), color=0xFFFFFF, font_size=10)
        gui.show()

if __name__ == "__main__":
    main()
