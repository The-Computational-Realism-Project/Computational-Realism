# Computational Realism

**An Attempt to Reconstruct Fundamental Physics Based on Nonlinear Soliton Dynamics and Grid Phase Emergence**

### **Introduction**

Modern physics has achieved remarkable success. However, many abstract mathematical postulates in quantum mechanics and relativity—such as complex probability amplitudes, intrinsic spin, point-charge singularities, and wave function collapse—still leave substantial room for ontological exploration.

Inspired by the concepts of discrete spacetime and quantum determinism proposed by scholars such as Stephen Wolfram and Gerard 't Hooft, this project, **Computational Realism**, explores a potential alternative path: treating the vacuum as a discrete computing medium with finite information propagation rates and capacity limits, while attempting to deconstruct all elementary particles and their interactions as **nonlinear topological solitons** that spontaneously emerge from this medium at macroscopic scales.

This repository contains the theoretical manuscripts and mathematical proofs of the framework. We attempt to demonstrate, through a bottom-up "emergence chain," how photons, electrons, and protons can be derived step-by-step from the underlying discrete grid, and explore their algebraic correspondences with classical electromagnetic forces, quantum mechanics, and strong/weak interactions.

* * *

### **Core Hypothesis: Bilayer Grid and Non-local Field Equations**

We hypothesize that the underlying foundation of the vacuum is a bilayer bit-computing grid. Due to the finite information capacity of the discrete grid, high energy densities generate "information congestion" (i.e., saturated nonlinear effects), which gives rise to mass.

The underlying information exchange rules are equivalent to the D'Alembert operator. When these discrete rules are pushed to the macroscopic continuous limit, infinite recursive interactions mathematically emerge as a non-local smoothing operator based on the D'Alembertian ( $\exp(a^2\Box)$ ). Its operation yields a screening mechanism for the self-energy divergence of point charges in classical electromagnetism, while the capacity saturation of the grid emerges as a logarithmic nonlinear feedback term in the field equations:

$$
\exp(a^2\Box) A^\mu = \left[ 1 + \kappa \ln\left(1 + \frac{u_{\text{inv}}}{u_{\text{th}}}\right) \right] A^\mu
$$

This constitutes the fundamental continuous, nonlinear field equation used to study particle evolution.

* * *

### **From Grid to Wave Packet: The Emergence Chain of Physical Reality**

Along the evolution of the aforementioned fundamental field equation, we can establish a bottom-up emergence chain of macroscopic reality:

1.  **The Stable Self-Focusing Solution of the Photon (The Photon Soliton)**  
    In the vacuum grid, transverse wave packet diffraction (the diffusion term) and the intrinsic logarithmic nonlinear attraction of the equation (the self-focusing term) reach a dynamic balance, forming a localized wave packet with zero rest mass in three-dimensional space. This mechanism is highly analogous to the **"spatial self-trapping soliton (Spatial Soliton)"** in nonlinear optics. Due to the logarithmic correction of the grid saturation effect, the transverse radius $R$ of high-energy photons (such as gamma rays) exhibits a logarithmic deviation from linear scaling: $R = \frac{\lambda}{2\pi \sqrt{4\kappa \ln \omega}}$ .

    Under this model, the photon is viewed as an adaptively adjusted, dynamic three-dimensional topological soliton.
    
3.  **The Self-Trapping and Standing Wave Entity of the Electron (The Electron Soliton)**  
    The electron is conceptualized as a composite photon. When two counter-propagating, polarization-locked photons meet, they carve a static refractive index grating (self-induced Bragg grating) in the vacuum under extremely high energy densities. The photon flow undergoes continuous coherent reflection within this grating, trapped in a closed circular orbit, and forms a stable, localized, self-trapped standing wave. In algebraic form, this presents a physical picture consistent with **"Bragg Gap Solitons"** in nonlinear periodic media.
    
    - **Correspondence of Rest Mass**: The energy residence and obstruction of the photon flow within the self-induced gap grating macroscopically manifest as fluid inertia resisting acceleration by external forces, which corresponds to rest mass.
    - **Potential Correspondence of Interactions**: Positive and negative charges correspond to different replicated temporal sequences of the bilayer grid. Attraction and repulsion between charges manifest as "phase neutralization" when overlapping out-of-phase (the system releases vacuum tension, redshifts, and tends to attract) or "parallel saturation pressure" when overlapping in-phase (the system energy blueshifts and tends to repel).
4.  **Composite Topology of the Proton and Gluon Phase Compensation (Strong Interaction & Proton Structure)**  
    We treat the **proton** as three spatially separated but spatiotemporally phase-locked fractional charge sub-wave packets (i.e., three valence quarks $u_1, u_2, d$).  
    According to the fractional charge-to-phase mapping rule $\delta_q = \frac{1+q}{2}\pi$, the phase-locking angles of the quark wave packets are:
    
    - Up quarks ($q = +2/3$) $\implies \delta_1 = \delta_2 = \frac{5\pi}{6}$
    - Down quark ($q = -1/3$) $\implies \delta_3 = \frac{\pi}{3}$
    
    Although the sum of their phases satisfies a $2\pi$ topological closure, the complex phase sum is not algebraically closed ($\sum e^{i\delta_j} \neq -3$), indicating that a pure quark system would have residual coherent interference (i.e., phase leakage and dissipation).  
    In an attempt to eliminate this residual phase difference in the interference to maintain topological stability, the grid must excite an auxiliary phase-stretching and compensation field. This model attempts to provide a classical nonlinear wave mapping for the regulatory mechanism of the **Gluon Field**. Through analytic continuation and multipole expansion, this microscopic quark-gluon composite emerges in the far-field as a trefoil ($3\theta'$) modulated envelope, spatially corresponding to tensor nuclear force characteristics.
    

* * *

### **Mathematical Isomorphism with Quantum Mechanics and Inspiring Physical Perspectives**

By applying the **Slowly Varying Envelope Approximation (SVEA)** and spatial projection to the nonlinear soliton equations, this project establishes a set of correspondences highly aligned with modern quantum mechanics (QM) and high-energy physics, offering the following academically inspiring perspectives:

#### **1\. The Physical Essence of Dirac Bi-spinors and Forward/Backward Wave Packets**

Under the first-order decomposition of spacetime, the quantum Dirac bi-spinor is no longer treated as a completely abstract mathematical construct, but can be mapped to components with explicit wave physics correspondences:

- **Forward Envelope $F$** and **Backward Envelope $B$**: Analogous to the coupling of counter-propagating modes in distributed feedback (DFB) lasers, they represent polarization modes propagating along the $+z$ and $-z$ directions (the spin direction) within the self-induced vacuum Bragg grating.
- **Large Component ($\phi \propto F+B$)**: Can be mapped to the **in-phase superposition (sum)** of the forward and backward waves, representing the bulk of the stationary standing wave energy.
- **Small Component ($\chi \propto F-B$)**: Can be mapped to the **out-of-phase residual (difference)** of the forward and backward waves, representing the asymmetric flow component introduced when the standing wave as a whole translates, providing an algebraic correspondence for why the small component's magnitude is proportional to momentum $p$.
- **Algebraic Symmetry**: Both $F$ and $B$ manifest as physical waves with positive energy characteristics. The electron state is characterized by **in-phase self-locking ($F=B$)**, while the positron state is characterized by **out-of-phase self-locking ($F=-B$)** induced by time reversal, exhibiting algebraic correspondence.

#### **2\. Discussion on the Physical Mechanism of Zitterbewegung**

In the Dirac equation, a free electron at rest still exhibits extremely high-frequency "jitter" (at a frequency of $\omega_{ZB} = 2mc^2/\hbar$). From the perspective of nonlinear waves, this phenomenon can be mapped to a more physically intuitive correspondence:  
**Zitterbewegung algebraically corresponds to a "mode beat frequency" or "Rabi Oscillation" phenomenon, where the trapped photon flow undergoes high-frequency, back-and-forth reflections within the self-induced Bragg grating, resulting in rapid exchanges between forward and backward momentum.** This is mathematically isomorphic to the artificial "Optical Zitterbewegung Analogs" demonstrated by researchers in periodic optical lattices or coupled waveguide arrays. Its characteristic exchange length $L = \hbar/mc$ matches the electron's reduced Compton wavelength.

#### **3\. Fluid Topological Deconstruction of Intrinsic Spin-1/2 and $4\pi$ Symmetry**

As a topological soliton in three-dimensional space, the electron's motion involves a dual self-locking of transverse spatial vortices and longitudinal wave packet oscillations. This model explores a geometric phenomenological correspondence under low-dimensional fluid topological constraints:  
A spatial rotation of $2\pi$ introduces a geometric phase factor of $e^{-i\pi} = -1$ onto the internal spatiotemporal manifold. Due to the entanglement of the internal polarization clock and macroscopic rotation, the system must undergo a $720^\circ$ ($4\pi$) rotation in physical space to untangle the topological connection between the envelope and the carrier wave, restoring all components of the system simultaneously. This provides a wave-geometric mechanism referencing the half-integer spin of fermions.

#### **4\. Wave Function Collapse and Spatial Quantization: Nonlinear Bistable Attractors**

In the Stern-Gerlach (S-G) experiment, when electrons with a continuous initial polarization angle $\alpha$ enter a strong gradient magnetic field $\nabla B_z$, an asymmetric differential phase shift is generated across the two sides of the electron standing wave cavity due to the Aharonov-Bohm (A-B) effect, causing a resonance mismatch in the grating. The resulting escape rate of energy-momentum flow, $\Gamma_{\text{escape}}$, caused by this mismatch is strictly proportional to $\sin^2 \alpha$.  
To maintain interference closure in this imbalanced environment, the electron's nonlinear self-feedback mechanism is activated, driving the evolution of its principal spin axis to follow a bifurcation equation similar to **"Optical Bistability"** in nonlinear optics:

$$
\frac{d\alpha}{dt} = -\lambda \sin(2\alpha)
$$

In this nonlinear phase space, the intermediate tilt angle $\alpha = \pi/2$ is an unstable saddle point. Due to this instability, the spin axis undergoes rapid evolution and ultimately settles into one of two **stable attractors ($\alpha = 0$ or $\alpha = \pi$)**. This explores a deterministic, nonlinear topological evolution path for **"wave function collapse" and "spatial quantization," wherein underlying continuous wave solitons, under extreme external constraints, spontaneously transition toward phase-space stable attractors to preserve interference stability**.

#### **5\. Planck's Constant $E=h\nu$ and the "Area Theorem" of Vacuum Restoration**

This framework discusses the characteristics of photon energy being proportional to frequency and independent of the wave train length $L$ from the perspective of nonlinear wave dynamics:

- **Dispersion Balance of Finite Wave Packets**: A wave packet of finite length $L$ disrupts the D'Alembertian cancellation, introducing logarithmic dispersion at the boundaries. To counter this, the vacuum's logarithmic self-focusing mechanism strictly requires the local energy density $u \propto 1/L$, which algebraically cancels the influence of $L$ on the total energy $E = \int u \, dV$.
    
- **Soliton Area Theorem and Vacuum State Restoration**: The prerequisite for dissipation-free propagation of a photon in a vacuum is that the medium's state must restore to the ground state after the photon passes. This is wave-geometrically highly analogous to the famous **"Soliton Area Theorem"** in nonlinear optics (such as the $2\pi$ pulse in Self-Induced Transparency). When the pulse action integral reaches the topological closure threshold constant $S_0$ of the vacuum grid (which emerges as Planck's constant $\hbar$), perfect vacuum state restoration is achieved without leaving a wake:
    
$$
    S_{\text{total}} = \int \frac{u}{\omega} \, dV = S_0 \equiv \hbar \implies E = \hbar\omega = h\nu
$$
    

#### **6\. High-Order Geometric Origins of the Fine-Structure Constant and Anomalous Magnetic Moment**

- **Strain Nature of the Fine-Structure Constant $\alpha$**: When the electron standing wave undergoes adaptive redshift in the inhomogeneous nuclear potential field to maintain global coherence, the spatial gradient of its macroscopically slowly varying envelope relative to the spatial frequency of the microscopic Compton carrier wave defines a dimensionless **"envelope strain parameter"** $\eta \equiv |\nabla F| / (k_c |F|) = {\bar{\lambda}}_c / a_0$. Algebraic calculation reveals that this deformation curvature is numerically and dimensionally equivalent to the fine-structure constant $\alpha \approx 1/137$, providing high-precision validation for the slowly varying envelope approximation (SVEA).
    
- **High-Order Corrections and Nonlinear Perturbative Cascade Expansion**: When we substitute self-energy into the logarithmic feedback term $\ln(1+x)$ of the field equation and perform a Taylor expansion, we obtain an algebraic series in powers of $\alpha$. This indicates that **the complex "multi-loop perturbative Feynman diagrams" in QED manifest algebraically as high-order cascade corrections of the nonlinear medium response function under perturbative expansion**. The first-order linear regime corresponds to the Schwinger correction ($\alpha/2\pi$), while high-order multi-loop diagrams correspond to nested spatial convolutions of high-order curvatures and non-local grid Green's functions.
    
- **Spontaneous Emergence of Transcendental Numbers**: In second-order perturbation, nested spatial convolutions geometrically degenerate into nested integrals of logarithmic functions, naturally deriving Apéry's constant $\zeta(3)$ and $\pi^2 \ln 2$ at the boundary:
    
$$
    \int_{0}^{1} \frac{\ln(x) \ln(1-x)}{x} \, dx = \sum_{n=1}^{\infty} \frac{1}{n^3} \equiv \zeta(3)
$$
    
This demonstrates that the occurrence of these transcendental numbers can be understood as the geometric evolutionary consequence of high-order cascade convolutions of classical wave equations projected onto the boundaries.
    

#### **7\. Fluid Geometric Interpretation of Parity Non-Conservation and CP Symmetry**

During weak interaction transitions (corresponding to the tearing and re-weaving of soliton structures), the neutrino ($q=0$) plays a critical role. As a composite of positive and negative photons, the phase derived from the charge-neutral condition is $\delta_\nu = \pi/2$.  
This implies that the neutrino carries a purely imaginary phase-lock. To prevent far-field radiation from leaving open topological defects (i.e., not exciting unclosed imaginary phases), the vacuum grid exhibits a blocking effect on purely imaginary wave packets. This static topological constraint forces the system, when propagating in a specific direction, to lock into a specific spin chirality (negative helicity), thereby providing a collisionless fluid flow explanation corresponding to **"parity non-conservation" and "CP symmetry."**

* * *

### **Project Vision**

This theoretical framework has no intention of refuting the established systems of quantum mechanics and quantum field theory. On the contrary, we are committed to exploring an emergent path—**investigating the feasibility of reducing physical reality to highly coherent, self-locked classical wave packets within a bilayer grid medium**—to provide a valuable algebraic and intuitive wave-physics reference perspective for long-unresolved philosophical enigmas in fundamental physics.
