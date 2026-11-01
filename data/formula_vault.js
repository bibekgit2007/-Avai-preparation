/**
 * AVAI Preparation Platform - High-Yield Formula & Concept Cheatsheet Vault
 * Contains KaTeX mathematical & chemical formulas, dimensional analysis,
 * competitive exam traps, and flashcard derivations.
 */

(function(window) {
    'use strict';

    const FORMULA_VAULT_DATA = [
        // ==========================================
        // 1. PHYSICS - MECHANICS & KINEMATICS
        // ==========================================
        {
            id: 'PHY_FORM_01',
            subject: 'Physics',
            chapter: 'Kinematics',
            chapterId: 'PHY_CH_02',
            title: 'Equations of Motion (Constant Acceleration)',
            formulaLatex: 'v = u + at \\quad;\\quad s = ut + \\frac{1}{2}at^2 \\quad;\\quad v^2 = u^2 + 2as \\quad;\\quad s_n = u + \\frac{a}{2}(2n - 1)',
            variables: 'u: \\text{initial velocity}, v: \\text{final velocity}, a: \\text{uniform acceleration}, s: \\text{displacement}, t: \\text{time}, s_n: \\text{displacement in } n\\text{-th sec}',
            units: 'v, u: \\text{m/s} \\quad;\\quad a: \\text{m/s}^2 \\quad;\\quad s: \\text{m}',
            trap: 'Applicable ONLY when acceleration is strictly uniform. If $a = f(t)$ or $f(x)$, use calculus: $v = \\int a\\,dt$ and $v\\,dv = a\\,dx$.',
            derivation: 'Integrate $a = \\frac{dv}{dt} \\implies v - u = at$. Integrate $v = \\frac{ds}{dt} = u + at \\implies s = ut + \\frac{1}{2}at^2$.',
            highYieldExam: 'NEET, JEE Main, WBJEE, NDA'
        },
        {
            id: 'PHY_FORM_02',
            subject: 'Physics',
            chapter: 'Kinematics',
            chapterId: 'PHY_CH_02',
            title: 'Projectile Motion on Flat Ground',
            formulaLatex: 'H_{\\max} = \\frac{u^2 \\sin^2\\theta}{2g} \\quad;\\quad T = \\frac{2u \\sin\\theta}{g} \\quad;\\quad R = \\frac{u^2 \\sin 2\\theta}{g}',
            variables: 'u: \\text{launch speed}, \\theta: \\text{angle of projection}, g: \\text{acceleration due to gravity}',
            units: 'H, R: \\text{m} \\quad;\\quad T: \\text{s}',
            trap: 'Max range occurs at $\\theta = 45^\\circ$ where $R_{\\max} = \\frac{u^2}{g} = 4 H_{\\max}$. Angle pairs $\\theta$ and $(90^\\circ - \\theta)$ give identical horizontal ranges!',
            derivation: 'Vertical component: $u_y = u\\sin\\theta$, $a_y = -g$. Time of flight found by setting $y = 0 \\implies t(u\\sin\\theta - \\frac{1}{2}gt) = 0$.',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },
        {
            id: 'PHY_FORM_03',
            subject: 'Physics',
            chapter: 'Laws of Motion',
            chapterId: 'PHY_CH_03',
            title: 'Friction Force & Angle of Banking',
            formulaLatex: 'f_{\\max} = \\mu_s N \\quad;\\quad f_k = \\mu_k N \\quad;\\quad v_{\\text{safe}} = \\sqrt{rg \\left(\\frac{\\mu + \\tan\\theta}{1 - \\mu\\tan\\theta}\\right)}',
            variables: '\\mu_s, \\mu_k: \\text{coefficients of static/kinetic friction}, N: \\text{normal reaction}, \\theta: \\text{banking angle}, r: \\text{radius}',
            units: '\\mu: \\text{dimensionless} \\quad;\\quad N: \\text{N}',
            trap: 'Static friction is a self-adjusting force: $0 \\le f_s \\le \\mu_s N$. Friction does NOT always oppose motion; it opposes RELATIVE motion between surfaces.',
            derivation: 'Balancing vertical components $N\\cos\\theta - f\\sin\\theta = mg$ and horizontal centripetal requirement $N\\sin\\theta + f\\cos\\theta = \\frac{mv^2}{r}$.',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },
        {
            id: 'PHY_FORM_04',
            subject: 'Physics',
            chapter: 'Work, Energy, and Power',
            chapterId: 'PHY_CH_04',
            title: 'Work-Energy Theorem & Power',
            formulaLatex: 'W_{\\text{net}} = \\Delta K = \\frac{1}{2}m v_f^2 - \\frac{1}{2}m v_i^2 \\quad;\\quad P = \\vec{F} \\cdot \\vec{v} = \\frac{dW}{dt}',
            variables: 'W_{\\text{net}}: \\text{work done by all forces (conservative + non-conservative + external)}, K: \\text{kinetic energy}',
            units: 'W: \\text{J (Joule)} \\quad;\\quad P: \\text{W (Watt)}',
            trap: 'Work-Energy Theorem holds true in all inertial frames and for all types of forces, whether conservative or non-conservative.',
            derivation: '$W = \\int F\\,dx = \\int m\\frac{dv}{dt}dx = \\int m v\\,dv = \\frac{1}{2}m v_f^2 - \\frac{1}{2}m v_i^2$.',
            highYieldExam: 'NEET, JEE Main, WBJEE, NDA'
        },
        {
            id: 'PHY_FORM_05',
            subject: 'Physics',
            chapter: 'Rotational Motion',
            chapterId: 'PHY_CH_05',
            title: 'Moment of Inertia & Rolling Kinetic Energy',
            formulaLatex: 'I = \\sum m_i r_i^2 = \\int r^2 dm \\quad;\\quad K_{\\text{roll}} = \\frac{1}{2}M v_{\\text{cm}}^2 \\left(1 + \\frac{k^2}{R^2}\\right)',
            variables: 'I: \\text{moment of inertia}, k: \\text{radius of gyration}, v_{\\text{cm}}: \\text{center of mass speed}',
            units: 'I: \\text{kg}\\cdot\\text{m}^2 \\quad;\\quad k: \\text{m}',
            trap: 'Parallel Axis Theorem $I = I_{\\text{cm}} + M d^2$ ONLY applies when one axis passes through the CENTER OF MASS. Perpendicular Axis Theorem is strictly for planar 2D laminar bodies!',
            derivation: '$K_{\\text{total}} = K_{\\text{trans}} + K_{\\text{rot}} = \\frac{1}{2}M v^2 + \\frac{1}{2}I\\omega^2$. Substitute $\\omega = v/R$ and $I = M k^2$.',
            highYieldExam: 'NEET, JEE Main, JEE Adv'
        },
        {
            id: 'PHY_FORM_06',
            subject: 'Physics',
            chapter: 'Gravitation',
            chapterId: 'PHY_CH_06',
            title: 'Gravitational Potential, Escape & Orbital Velocity',
            formulaLatex: 'v_e = \\sqrt{\\frac{2GM}{R}} = \\sqrt{2gR} \\quad;\\quad v_o = \\sqrt{\\frac{GM}{R}} = \\frac{v_e}{\\sqrt{2}} \\quad;\\quad T^2 = \\frac{4\\pi^2}{GM} r^3',
            variables: 'G = 6.674 \\times 10^{-11}\\,\\text{N}\\cdot\\text{m}^2/\\text{kg}^2, M: \\text{mass of planet}, R: \\text{radius of planet}',
            units: 'v_e, v_o: \\text{m/s} \\quad;\\quad T: \\text{s}',
            trap: 'Escape velocity is INDEPENDENT of the mass and angle of projection of the launched projectile (provided $\\theta \\ne 90^\\circ$ towards the ground).',
            derivation: 'Conservation of mechanical energy: $-\\frac{GMm}{R} + \\frac{1}{2}m v_e^2 = 0 \\implies v_e = \\sqrt{2GM/R}$.',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },

        // ==========================================
        // 2. PHYSICS - FLUIDS & THERMODYNAMICS
        // ==========================================
        {
            id: 'PHY_FORM_07',
            subject: 'Physics',
            chapter: 'Properties of Solids and Liquids',
            chapterId: 'PHY_CH_07',
            title: 'Bernoulli Equation & Continuity Equation',
            formulaLatex: 'A_1 v_1 = A_2 v_2 \\quad;\\quad P + \\frac{1}{2}\\rho v^2 + \\rho g h = \\text{constant}',
            variables: 'A: \\text{cross-sectional area}, v: \\text{fluid speed}, P: \\text{static pressure}, \\rho: \\text{fluid density}',
            units: 'P: \\text{Pa (N/m}^2) \\quad;\\quad \\rho: \\text{kg/m}^3',
            trap: 'Valid ONLY for streamline, steady, incompressible, and non-viscous (ideal) fluids. At narrow constrictions, speed $v$ increases and static pressure $P$ DECREASES!',
            derivation: 'Work done by pressure energy = change in kinetic energy + change in gravitational potential energy across a tube element.',
            highYieldExam: 'NEET, JEE Main'
        },
        {
            id: 'PHY_FORM_08',
            subject: 'Physics',
            chapter: 'Thermodynamics',
            chapterId: 'PHY_CH_09',
            title: 'First Law of Thermodynamics & Carnot Engine',
            formulaLatex: '\\Delta Q = \\Delta U + W \\quad;\\quad W = \\int P\\,dV \\quad;\\quad \\eta_{\\text{Carnot}} = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}',
            variables: '\\Delta Q: \\text{heat absorbed}, \\Delta U = n C_v \\Delta T: \\text{internal energy change}, \\eta: \\text{efficiency}, T_C, T_H: \\text{sink & source temp (Kelvin)}',
            units: 'Q, W, U: \\text{J} \\quad;\\quad T: \\text{Kelvin (MUST use K, not }^\\circ\\text{C)}',
            trap: 'CRITICAL: In Carnot efficiency $\\eta = 1 - \\frac{T_C}{T_H}$, temperatures MUST BE IN ABSOLUTE KELVIN! Cyclic process has $\\Delta U = 0 \\implies Q = W$.',
            derivation: 'For ideal gas, internal energy $U = \\frac{f}{2}n R T$, where $f$ is degrees of freedom (mono=3, dia=5).',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },

        // ==========================================
        // 3. PHYSICS - ELECTRODYNAMICS & MAGNETISM
        // ==========================================
        {
            id: 'PHY_FORM_09',
            subject: 'Physics',
            chapter: 'Electrostatics',
            chapterId: 'PHY_CH_11',
            title: 'Coulomb Law & Electric Field',
            formulaLatex: 'F = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q_1 q_2}{r^2} \\quad;\\quad \\vec{E} = \\frac{\\vec{F}}{q} \\quad;\\quad V = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q}{r}',
            variables: '\\frac{1}{4\\pi\\varepsilon_0} = 8.99 \\times 10^9\\,\\text{N}\\cdot\\text{m}^2/\\text{C}^2, q: \\text{charge}, r: \\text{separation}',
            units: 'F: \\text{N} \\quad;\\quad E: \\text{V/m or N/C} \\quad;\\quad V: \\text{Volt}',
            trap: 'Potential $V$ is a SCALAR (include algebraic charge signs $\\pm$), while Electric Field $\\vec{E}$ is a VECTOR (use superposition vector addition). Inside a conducting shell, $E = 0$ while $V = \\text{constant}$!',
            derivation: 'Gauss Law: $\\oint \\vec{E} \\cdot d\\vec{A} = \\frac{q_{\\text{enclosed}}}{\\varepsilon_0}$. For spherical symmetry: $E(4\\pi r^2) = \\frac{q}{\\varepsilon_0}$.',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },
        {
            id: 'PHY_FORM_10',
            subject: 'Physics',
            chapter: 'Current Electricity',
            chapterId: 'PHY_CH_12',
            title: 'Drift Velocity, Ohm Law & Resistance Drift',
            formulaLatex: 'I = n e A v_d \\quad;\\quad v_d = \\frac{e E \\tau}{m} \\quad;\\quad R = \\rho \\frac{l}{A} \\quad;\\quad R_T = R_0 (1 + \\alpha \\Delta T)',
            variables: 'n: \\text{charge carrier density}, e = 1.6 \\times 10^{-19}\\,\\text{C}, A: \\text{area}, v_d: \\text{drift speed}, \\tau: \\text{relaxation time}, \\rho: \\text{resistivity}',
            units: 'v_d: \\text{m/s} \\quad;\\quad R: \\Omega \\quad;\\quad \\rho: \\Omega\\cdot\\text{m}',
            trap: 'When a wire is stretched to $n$ times its length ($l\' = n l$), volume remains constant so area becomes $A\' = A/n$. Therefore, resistance becomes $R\' = n^2 R$!',
            derivation: 'Acceleration of electron $a = \\frac{e E}{m}$. Average drift speed over relaxation time $\\tau$ is $v_d = a \\tau = \\frac{e E \\tau}{m}$.',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },
        {
            id: 'PHY_FORM_11',
            subject: 'Physics',
            chapter: 'Electromagnetic Induction',
            chapterId: 'PHY_CH_14',
            title: 'Faraday Law, Lenz Law & LCR Resonance',
            formulaLatex: '\\varepsilon = -\\frac{d\\Phi_B}{dt} = -L \\frac{dI}{dt} \\quad;\\quad \\omega_0 = \\frac{1}{\\sqrt{LC}} \\quad;\\quad Z = \\sqrt{R^2 + (X_L - X_C)^2}',
            variables: '\\Phi_B: \\text{magnetic flux}, L: \\text{self-inductance}, Z: \\text{impedance}, X_L = \\omega L, X_C = \\frac{1}{\\omega C}',
            units: '\\varepsilon: \\text{V} \\quad;\\quad L: \\text{Henry (H)} \\quad;\\quad Z: \\Omega',
            trap: 'At electrical resonance, $X_L = X_C$, impedance is minimum $Z = R$, current is maximum $I = V/R$, and power factor $\\cos\\phi = 1$ (purely resistive)!',
            derivation: 'Setting $X_L = X_C \\implies \\omega L = \\frac{1}{\\omega C} \\implies \\omega_0^2 = \\frac{1}{LC} \\implies f_0 = \\frac{1}{2\\pi\\sqrt{LC}}$.',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },

        // ==========================================
        // 4. PHYSICS - OPTICS & MODERN PHYSICS
        // ==========================================
        {
            id: 'PHY_FORM_12',
            subject: 'Physics',
            chapter: 'Optics',
            chapterId: 'PHY_CH_16',
            title: 'Lens Maker Formula & Young Double Slit (YDSE)',
            formulaLatex: '\\frac{1}{f} = (\\mu - 1)\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right) \\quad;\\quad \\beta = \\frac{\\lambda D}{d} \\quad;\\quad y_n = n \\frac{\\lambda D}{d}',
            variables: 'f: \\text{focal length}, \\mu: \\text{refractive index}, R_1, R_2: \\text{radii of curvature}, \\beta: \\text{fringe width}, \\lambda: \\text{wavelength}',
            units: 'f, \\beta, y_n, D, d: \\text{m}',
            trap: 'When lens is immersed in a liquid of refractive index $\\mu_l$, replace $(\\mu - 1)$ by $\\left(\\frac{\\mu_g}{\\mu_l} - 1\\right)$. If immersed in water, focal length increases by ~4x!',
            derivation: 'Path difference in YDSE: $\\Delta x = d \\sin\\theta \\approx \\frac{yd}{D}$. For constructive maxima: $\\Delta x = n\\lambda \\implies y_n = \\frac{n\\lambda D}{d}$.',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },
        {
            id: 'PHY_FORM_13',
            subject: 'Physics',
            chapter: 'Dual Nature of Matter and Radiation',
            chapterId: 'PHY_CH_17',
            title: 'Einstein Photoelectric Equation & De Broglie Wavelength',
            formulaLatex: 'E = h\\nu = \\phi_0 + K_{\\max} \\quad;\\quad K_{\\max} = e V_0 \\quad;\\quad \\lambda = \\frac{h}{p} = \\frac{h}{\\sqrt{2m q V}} = \\frac{12.27}{\\sqrt{V}}\\,\\text{\\AA (for } e^-)',
            variables: 'h = 6.626 \\times 10^{-34}\\,\\text{J}\\cdot\\text{s}, \\phi_0: \\text{work function}, V_0: \\text{stopping potential}, V: \\text{accelerating voltage}',
            units: 'E, \\phi_0: \\text{eV or J} \\quad;\\quad V_0: \\text{Volt} \\quad;\\quad \\lambda: \\text{\\AA or m}',
            trap: 'Stopping potential $V_0$ depends strictly on the FREQUENCY of incident light, NOT its intensity! Intensity only affects saturation photoelectric current.',
            derivation: 'Kinetic energy $K = q V$. Momentum $p = \\sqrt{2m K} = \\sqrt{2m q V}$. De Broglie relation $\\lambda = \\frac{h}{p} = \\frac{h}{\\sqrt{2m q V}}$.',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },

        // ==========================================
        // 5. CHEMISTRY - PHYSICAL CHEMISTRY
        // ==========================================
        {
            id: 'CHEM_FORM_01',
            subject: 'Chemistry',
            chapter: 'Chemical Thermodynamics',
            chapterId: 'CHEM_CH_04',
            title: 'Gibbs Free Energy & Spontaneity Criterion',
            formulaLatex: '\\Delta G = \\Delta H - T \\Delta S \\quad;\\quad \\Delta G^\\circ = -RT \\ln K = -2.303 RT \\log_{10} K \\quad;\\quad \\Delta G^\\circ = -n F E^\\circ_{\\text{cell}}',
            variables: '\\Delta G: \\text{Gibbs energy change}, \\Delta H: \\text{enthalpy change}, \\Delta S: \\text{entropy change}, K: \\text{equilibrium constant}, F = 96500\\,\\text{C/mol}',
            units: '\\Delta G, \\Delta H: \\text{kJ/mol} \\quad;\\quad \\Delta S: \\text{J/mol}\\cdot\\text{K}',
            trap: 'Spontaneous reaction REQUIRES $\\Delta G < 0$. If $\\Delta H > 0$ and $\\Delta S > 0$, reaction is spontaneous ONLY at HIGH temperature ($T > \\Delta H / \\Delta S$).',
            derivation: 'Combined First and Second Laws of Thermodynamics: $dG = V dP - S dT$. At constant $T$ and $P$, $dG = -T dS_{\\text{total}} \\le 0$.',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },
        {
            id: 'CHEM_FORM_02',
            subject: 'Chemistry',
            chapter: 'Electrochemistry',
            chapterId: 'CHEM_CH_07',
            title: 'Nernst Equation for Electrode & Cell Potential',
            formulaLatex: 'E_{\\text{cell}} = E^\\circ_{\\text{cell}} - \\frac{2.303 RT}{n F} \\log_{10} Q \\approx E^\\circ_{\\text{cell}} - \\frac{0.0591}{n} \\log_{10} Q \\quad (\\text{at } 298\\,\\text{K})',
            variables: 'E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}}, n: \\text{number of moles of electrons transferred}, Q: \\text{reaction quotient}',
            units: 'E: \\text{Volt (V)}',
            trap: 'Pure solids and pure liquids have activity = 1 and are EXCLUDED from reaction quotient $Q$. At equilibrium, $E_{\\text{cell}} = 0$ (battery dead) and $Q = K_{\\text{eq}}$!',
            derivation: 'From $\\Delta G = \\Delta G^\\circ + RT\\ln Q$. Substitute $\\Delta G = -nFE$ and $\\Delta G^\\circ = -nFE^\\circ$ and divide by $-nF$.',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },
        {
            id: 'CHEM_FORM_03',
            subject: 'Chemistry',
            chapter: 'Chemical Kinetics',
            chapterId: 'CHEM_CH_08',
            title: 'First Order Kinetics & Arrhenius Equation',
            formulaLatex: 'k = \\frac{2.303}{t}\\log_{10}\\left(\\frac{[A]_0}{[A]_t}\\right) \\quad;\\quad t_{1/2} = \\frac{0.693}{k} \\quad;\\quad \\log_{10}\\left(\\frac{k_2}{k_1}\\right) = \\frac{E_a}{2.303 R}\\left(\\frac{1}{T_1} - \\frac{1}{T_2}\\right)',
            variables: 'k: \\text{rate constant}, [A]_0: \\text{initial concentration}, t_{1/2}: \\text{half-life}, E_a: \\text{activation energy}',
            units: 'k: \\text{s}^{-1} \\text{ (for 1st order)} \\quad;\\quad E_a: \\text{J/mol}',
            trap: 'For a 1st order reaction, $t_{1/2}$ is completely INDEPENDENT of initial concentration $[A]_0$. Time to complete 75% reaction is exactly $2 \\times t_{1/2}$!',
            derivation: 'Rate equation: $-\\frac{d[A]}{dt} = k[A] \\implies \\int_{[A]_0}^{[A]} \\frac{d[A]}{[A]} = -k \\int_0^t dt \\implies \\ln\\frac{[A]_0}{[A]} = kt$.',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },
        {
            id: 'CHEM_FORM_04',
            subject: 'Chemistry',
            chapter: 'Solutions',
            chapterId: 'CHEM_CH_06',
            title: 'Colligative Properties & Van \'t Hoff Factor',
            formulaLatex: '\\frac{P^\\circ - P}{P^\\circ} = i X_B \\quad;\\quad \\Delta T_b = i K_b m \\quad;\\quad \\Delta T_f = i K_f m \\quad;\\quad \\pi = i C R T',
            variables: 'i: \\text{Van \'t Hoff factor } (i = 1 + (n-1)\\alpha), K_b: \\text{ebullioscopic const}, K_f: \\text{cryoscopic const}, m: \\text{molality}, \\pi: \\text{osmotic pressure}',
            units: '\\Delta T: \\text{K or }^\\circ\\text{C} \\quad;\\quad \\pi: \\text{atm or Pa}',
            trap: 'For association (e.g. benzoic acid in benzene dimers), $i = 1 - \\frac{\\alpha}{2} < 1$. For complete dissociation of $\\text{NaCl}$, $i = 2$; for $\\text{CaCl}_2$, $i = 3$!',
            derivation: 'Colligative properties depend solely on number of solute particles per unit solvent volume, modified by ionization factor $i$.',
            highYieldExam: 'NEET, JEE Main, WBJEE'
        },

        // ==========================================
        // 6. MATHEMATICS - CORE CALCULUS & ALGEBRA
        // ==========================================
        {
            id: 'MATH_FORM_01',
            subject: 'Mathematics',
            chapter: 'Calculus',
            chapterId: 'MATH_CH_05',
            title: 'Standard Differentiation & Product/Quotient Rules',
            formulaLatex: '\\frac{d}{dx}(uv) = u\'v + uv\' \\quad;\\quad \\frac{d}{dx}\\left(\\frac{u}{v}\\right) = \\frac{u\'v - uv\'}{v^2} \\quad;\\quad \\frac{d}{dx}[\\sin x] = \\cos x \\quad;\\quad \\frac{d}{dx}[e^x] = e^x',
            variables: 'u(x), v(x): \\text{differentiable functions of } x',
            units: '\\text{Dimensionless}',
            trap: 'In quotient rule, the numerator is $(u\'v - uv\')$, NOT $(uv\' - u\'v)$. Watch the minus sign order carefully!',
            derivation: 'Product rule from first principles definition: $\\lim_{h \\to 0} \\frac{u(x+h)v(x+h) - u(x)v(x)}{h}$.',
            highYieldExam: 'JEE Main, JEE Adv, WBJEE, NDA'
        },
        {
            id: 'MATH_FORM_02',
            subject: 'Mathematics',
            chapter: 'Integral Calculus',
            chapterId: 'MATH_CH_06',
            title: 'Integration by Parts & King Property of Definite Integrals',
            formulaLatex: '\\int u\\,v\\,dx = u\\int v\\,dx - \\int\\left(u\' \\int v\\,dx\\right)dx \\quad;\\quad \\int_a^b f(x)\\,dx = \\int_a^b f(a + b - x)\\,dx',
            variables: 'u, v: \\text{chosen via ILATE rule (Inverse, Logarithmic, Algebraic, Trigonometric, Exponential)}',
            units: '\\text{Dimensionless}',
            trap: 'King property $\\int_0^a f(x)\\,dx = \\int_0^a f(a - x)\\,dx$ solves 90% of tricky definite integrals involving $\\sin, \\cos, \\ln(1+\\tan x)$ without actual anti-differentiation!',
            derivation: 'Substitute $t = a + b - x \\implies dt = -dx$. As $x: a \\to b$, $t: b \\to a$. Reversing limits absorbs the negative sign.',
            highYieldExam: 'JEE Main, JEE Adv, WBJEE, NDA'
        },
        {
            id: 'MATH_FORM_03',
            subject: 'Mathematics',
            chapter: 'Vectors & 3D Geometry',
            chapterId: 'MATH_CH_08',
            title: 'Vector Products & Shortest Distance between Skew Lines',
            formulaLatex: '\\vec{a} \\cdot \\vec{b} = |a||b|\\cos\\theta \\quad;\\quad \\vec{a} \\times \\vec{b} = |a||b|\\sin\\theta\\,\\hat{n} \\quad;\\quad d = \\frac{|(\\vec{a}_2 - \\vec{a}_1) \\cdot (\\vec{b}_1 \\times \\vec{b}_2)|}{|\\vec{b}_1 \\times \\vec{b}_2|}',
            variables: '\\vec{r} = \\vec{a}_1 + \\lambda \\vec{b}_1, \\vec{r} = \\vec{a}_2 + \\mu \\vec{b}_2: \\text{lines in 3D space}',
            units: 'd: \\text{units of length}',
            trap: 'If lines are parallel ($\\vec{b}_1 = \\vec{b}_2 = \\vec{b}$), shortest distance is $d = \\frac{|(\\vec{a}_2 - \\vec{a}_1) \\times \\vec{b}|}{|\\vec{b}|}$, NOT the scalar triple product formula!',
            derivation: 'Projection of displacement vector $(\\vec{a}_2 - \\vec{a}_1)$ onto the common normal vector $\\hat{n} = \\frac{\\vec{b}_1 \\times \\vec{b}_2}{|\\vec{b}_1 \\times \\vec{b}_2|}$.',
            highYieldExam: 'JEE Main, JEE Adv, WBJEE'
        }
    ];

    // Helper utilities for Formula Vault API
    window.AVAI_FORMULA_VAULT = {
        data: FORMULA_VAULT_DATA,

        getAll: function() {
            return FORMULA_VAULT_DATA;
        },

        getBySubject: function(subject) {
            if (!subject || subject === 'ALL') return FORMULA_VAULT_DATA;
            return FORMULA_VAULT_DATA.filter(f => f.subject.toLowerCase() === subject.toLowerCase());
        },

        getByChapter: function(chapterName) {
            if (!chapterName) return [];
            const q = chapterName.toLowerCase();
            return FORMULA_VAULT_DATA.filter(f => 
                f.chapter.toLowerCase().includes(q) || 
                (f.chapterId && f.chapterId.toLowerCase() === q)
            );
        },

        search: function(query) {
            if (!query || !query.trim()) return FORMULA_VAULT_DATA;
            const q = query.toLowerCase().trim();
            return FORMULA_VAULT_DATA.filter(f => 
                f.title.toLowerCase().includes(q) ||
                f.chapter.toLowerCase().includes(q) ||
                f.subject.toLowerCase().includes(q) ||
                f.formulaLatex.toLowerCase().includes(q) ||
                f.trap.toLowerCase().includes(q)
            );
        }
    };

})(window);
