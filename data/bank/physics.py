# =============================================================================
# PHYSICS QUESTION BANK (80 Authentic High-Yield Questions)
# =============================================================================

SVG_SCREW_GAUGE = """<svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <defs>
    <linearGradient id="metalGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="50%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="thimbleGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="50%" stop-color="#475569"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect x="30" y="45" width="220" height="90" rx="6" fill="url(#metalGrad)" stroke="#0f172a" stroke-width="2"/>
  <line x1="30" y1="90" x2="250" y2="90" stroke="#f8fafc" stroke-width="2.5"/>
  <line x1="60" y1="90" x2="60" y2="70" stroke="#f8fafc" stroke-width="2"/><text x="56" y="65" fill="#f8fafc" font-size="12" font-family="system-ui" font-weight="bold">0</text>
  <line x1="90" y1="90" x2="90" y2="72" stroke="#f8fafc" stroke-width="1.8"/><text x="86" y="65" fill="#f8fafc" font-size="12" font-family="system-ui" font-weight="bold">1</text>
  <line x1="120" y1="90" x2="120" y2="72" stroke="#f8fafc" stroke-width="1.8"/><text x="116" y="65" fill="#f8fafc" font-size="12" font-family="system-ui" font-weight="bold">2</text>
  <line x1="150" y1="90" x2="150" y2="72" stroke="#f8fafc" stroke-width="1.8"/><text x="146" y="65" fill="#38bdf8" font-size="13" font-family="system-ui" font-weight="bold">3</text>
  <line x1="75" y1="90" x2="75" y2="104" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="105" y1="90" x2="105" y2="104" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="135" y1="90" x2="135" y2="104" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 250 30 L 460 30 L 460 150 L 250 150 Z" fill="url(#thimbleGrad)" stroke="#0f172a" stroke-width="2"/>
  <line x1="250" y1="30" x2="250" y2="150" stroke="#38bdf8" stroke-width="3"/>
  <line x1="250" y1="50" x2="275" y2="50" stroke="#f8fafc" stroke-width="1.5"/><text x="282" y="54" fill="#f8fafc" font-size="11" font-family="monospace">40</text>
  <line x1="250" y1="70" x2="275" y2="70" stroke="#f8fafc" stroke-width="1.5"/><text x="282" y="74" fill="#f8fafc" font-size="11" font-family="monospace">35</text>
  <line x1="250" y1="82" x2="285" y2="82" stroke="#38bdf8" stroke-width="2.5"/><text x="292" y="86" fill="#38bdf8" font-size="13" font-family="monospace" font-weight="bold">32 (Coincides)</text>
  <line x1="250" y1="90" x2="275" y2="90" stroke="#f8fafc" stroke-width="1.5"/><text x="282" y="94" fill="#f8fafc" font-size="11" font-family="monospace">30</text>
  <line x1="250" y1="110" x2="275" y2="110" stroke="#f8fafc" stroke-width="1.5"/><text x="282" y="114" fill="#f8fafc" font-size="11" font-family="monospace">25</text>
  <text x="75" y="165" fill="#0f172a" font-size="12" font-family="system-ui" font-weight="bold">Main Scale (mm)</text>
  <text x="280" y="165" fill="#0369a1" font-size="12" font-family="system-ui" font-weight="bold">Circular Scale (Pitch = 0.5 mm, 50 div)</text>
</svg>"""

SVG_LCR_CIRCUIT = """<svg viewBox="0 0 560 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <rect x="40" y="50" width="480" height="120" rx="12" fill="none" stroke="#334155" stroke-width="3"/>
  <!-- Inductor L -->
  <rect x="75" y="47" width="150" height="6" fill="#ffffff"/>
  <path d="M 80 50 C 90 25, 105 25, 115 50 C 125 25, 140 25, 150 50 C 160 25, 175 25, 185 50 C 195 25, 210 25, 220 50" fill="none" stroke="#2563eb" stroke-width="3.5"/>
  <text x="150" y="80" fill="#1e40af" font-size="13" font-family="system-ui" font-weight="bold" text-anchor="middle">Inductor L</text>
  <circle cx="150" cy="18" r="14" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="150" y="23" fill="#1e40af" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">V<tspan font-size="8">L</tspan></text>
  <line x1="80" y1="50" x2="136" y2="18" stroke="#2563eb" stroke-dasharray="2 2"/>
  <line x1="220" y1="50" x2="164" y2="18" stroke="#2563eb" stroke-dasharray="2 2"/>
  
  <!-- Capacitor C -->
  <rect x="250" y="46" width="60" height="8" fill="#ffffff"/>
  <line x1="270" y1="35" x2="270" y2="65" stroke="#0891b2" stroke-width="4"/>
  <line x1="285" y1="35" x2="285" y2="65" stroke="#0891b2" stroke-width="4"/>
  <text x="277" y="80" fill="#0e7490" font-size="13" font-family="system-ui" font-weight="bold" text-anchor="middle">Capacitor C</text>
  <circle cx="277" cy="18" r="14" fill="#ecfeff" stroke="#0891b2" stroke-width="2"/>
  <text x="277" y="23" fill="#0e7490" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">V<tspan font-size="8">C</tspan></text>
  <line x1="250" y1="50" x2="263" y2="18" stroke="#0891b2" stroke-dasharray="2 2"/>
  <line x1="310" y1="50" x2="291" y2="18" stroke="#0891b2" stroke-dasharray="2 2"/>

  <!-- Resistor R -->
  <rect x="345" y="46" width="130" height="8" fill="#ffffff"/>
  <path d="M 350 50 L 360 40 L 375 60 L 390 40 L 405 60 L 420 40 L 435 60 L 445 50" fill="none" stroke="#d97706" stroke-width="3.5"/>
  <text x="398" y="80" fill="#b45309" font-size="13" font-family="system-ui" font-weight="bold" text-anchor="middle">R = 4 Ω</text>
  <circle cx="398" cy="18" r="14" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
  <text x="398" y="23" fill="#b45309" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">V<tspan font-size="8">R</tspan></text>
  <line x1="350" y1="50" x2="384" y2="18" stroke="#d97706" stroke-dasharray="2 2"/>
  <line x1="445" y1="50" x2="412" y2="18" stroke="#d97706" stroke-dasharray="2 2"/>

  <!-- AC Source Bottom -->
  <rect x="250" y="165" width="60" height="10" fill="#ffffff"/>
  <circle cx="280" cy="170" r="18" fill="#f8fafc" stroke="#475569" stroke-width="2.5"/>
  <path d="M 270 170 Q 275 163 280 170 T 290 170" fill="none" stroke="#475569" stroke-width="2.5"/>
  <text x="280" y="202" fill="#334155" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">V = V₀ sin(100πt + π/6)</text>
</svg>"""

SVG_MECHANICAL_EQUILIBRIUM = """<svg viewBox="0 0 460 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <rect x="30" y="100" width="220" height="20" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
  <line x1="30" y1="120" x2="30" y2="190" stroke="#475569" stroke-width="4"/>
  <line x1="250" y1="100" x2="250" y2="190" stroke="#475569" stroke-width="4"/>
  <rect x="350" y="20" width="80" height="14" fill="#94a3b8" stroke="#475569" stroke-width="1.5"/>
  <rect x="90" y="55" width="75" height="45" rx="4" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
  <text x="127" y="83" fill="#ffffff" font-size="16" font-family="system-ui" font-weight="black" text-anchor="middle">B (W)</text>
  <line x1="165" y1="78" x2="320" y2="78" stroke="#0f172a" stroke-width="3"/>
  <circle cx="320" cy="78" r="6" fill="#ef4444" stroke="#991b1b" stroke-width="1.5"/>
  <text x="320" y="68" fill="#991b1b" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">Knot</text>
  <line x1="320" y1="78" x2="390" y2="20" stroke="#0f172a" stroke-width="3"/>
  <path d="M 375 20 A 20 20 0 0 1 365 40" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text x="365" y="32" fill="#1d4ed8" font-size="12" font-family="system-ui" font-weight="bold">θ</text>
  <line x1="320" y1="78" x2="320" y2="135" stroke="#0f172a" stroke-width="3"/>
  <rect x="295" y="135" width="50" height="45" rx="4" fill="#10b981" stroke="#047857" stroke-width="2"/>
  <text x="320" y="163" fill="#ffffff" font-size="15" font-family="system-ui" font-weight="black" text-anchor="middle">A</text>
  <text x="127" y="115" fill="#475569" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Friction coeff: μ</text>
</svg>"""

SVG_SPHERE_CAVITY = """<svg viewBox="0 0 380 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <circle cx="170" cy="100" r="80" fill="#f1f5f9" stroke="#334155" stroke-width="2.5"/>
  <circle cx="210" cy="100" r="40" fill="#e2e8f0" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="4 3"/>
  <circle cx="170" cy="100" r="3.5" fill="#334155"/>
  <text x="162" y="118" fill="#334155" font-size="13" font-family="system-ui" font-weight="bold">O</text>
  <circle cx="210" cy="100" r="3.5" fill="#dc2626"/>
  <text x="214" y="118" fill="#dc2626" font-size="13" font-family="system-ui" font-weight="bold">P (Center of Cavity)</text>
  <line x1="170" y1="100" x2="170" y2="20" stroke="#64748b" stroke-width="1.5" stroke-dasharray="2 2"/>
  <text x="155" y="60" fill="#475569" font-size="12" font-family="system-ui" font-weight="bold">R</text>
  <line x1="210" y1="100" x2="210" y2="60" stroke="#dc2626" stroke-width="1.5"/>
  <text x="215" y="78" fill="#dc2626" font-size="11" font-family="system-ui" font-weight="bold">R/2</text>
</svg>"""

SVG_PRISM_TIR = """<svg viewBox="0 0 440 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <polygon points="100,180 320,180 100,40" fill="#f0fdf4" stroke="#16a34a" stroke-width="3"/>
  <text x="85" y="195" fill="#15803d" font-size="14" font-family="system-ui" font-weight="bold">A (90°)</text>
  <text x="330" y="190" fill="#15803d" font-size="14" font-family="system-ui" font-weight="bold">B (45°)</text>
  <text x="85" y="35" fill="#15803d" font-size="14" font-family="system-ui" font-weight="bold">C (45°)</text>
  <!-- Incident Ray -->
  <line x1="20" y1="110" x2="100" y2="110" stroke="#2563eb" stroke-width="3.5"/>
  <line x1="100" y1="110" x2="210" y2="110" stroke="#2563eb" stroke-width="3.5"/>
  <!-- Normal at hypotenuse -->
  <line x1="180" y1="80" x2="240" y2="140" stroke="#94a3b8" stroke-width="2" stroke-dasharray="3 3"/>
  <circle cx="210" cy="110" r="4" fill="#dc2626"/>
  <!-- Reflected Ray inside -->
  <line x1="210" y1="110" x2="210" y2="180" stroke="#dc2626" stroke-width="3.5"/>
  <!-- Emergent Ray -->
  <line x1="210" y1="180" x2="210" y2="215" stroke="#dc2626" stroke-width="3.5"/>
  <text x="220" y="150" fill="#dc2626" font-size="13" font-family="system-ui" font-weight="bold">TIR (i = 45° > C)</text>
  <text x="220" y="210" fill="#dc2626" font-size="12" font-family="system-ui" font-weight="bold">δ = 90°</text>
</svg>"""

SVG_WHEATSTONE_BRIDGE = """<svg viewBox="0 0 480 230" width="100%" height="230" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Diamond Shape -->
  <polygon points="240,30 380,115 240,200 100,115" fill="#f8fafc" stroke="#334155" stroke-width="3"/>
  <!-- Resistor P (Top-Left) -->
  <rect x="140" y="55" width="55" height="24" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="167" y="72" fill="#1e40af" font-size="13" font-family="system-ui" font-weight="bold" text-anchor="middle">P = 10 Ω</text>
  <!-- Resistor Q (Top-Right) -->
  <rect x="285" y="55" width="55" height="24" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="312" y="72" fill="#1e40af" font-size="13" font-family="system-ui" font-weight="bold" text-anchor="middle">Q = 20 Ω</text>
  <!-- Resistor R (Bottom-Left) -->
  <rect x="140" y="150" width="55" height="24" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="167" y="167" fill="#b45309" font-size="13" font-family="system-ui" font-weight="bold" text-anchor="middle">R = 15 Ω</text>
  <!-- Resistor S (Bottom-Right) -->
  <rect x="285" y="150" width="55" height="24" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="312" y="167" fill="#b45309" font-size="13" font-family="system-ui" font-weight="bold" text-anchor="middle">S = ? Ω</text>
  <!-- Galvanometer Branch -->
  <line x1="240" y1="30" x2="240" y2="85" stroke="#475569" stroke-width="2.5"/>
  <circle cx="240" cy="115" r="22" fill="#ffffff" stroke="#16a34a" stroke-width="2.5"/>
  <text x="240" y="121" fill="#15803d" font-size="15" font-family="system-ui" font-weight="black" text-anchor="middle">G (0)</text>
  <line x1="240" y1="145" x2="240" y2="200" stroke="#475569" stroke-width="2.5"/>
  <!-- Nodes -->
  <circle cx="100" cy="115" r="5" fill="#0f172a"/><text x="80" y="120" fill="#0f172a" font-size="14" font-family="system-ui" font-weight="bold">A</text>
  <circle cx="380" cy="115" r="5" fill="#0f172a"/><text x="390" y="120" fill="#0f172a" font-size="14" font-family="system-ui" font-weight="bold">C</text>
  <circle cx="240" cy="30" r="5" fill="#0f172a"/><text x="240" y="20" fill="#0f172a" font-size="14" font-family="system-ui" font-weight="bold" text-anchor="middle">B</text>
  <circle cx="240" cy="200" r="5" fill="#0f172a"/><text x="240" y="222" fill="#0f172a" font-size="14" font-family="system-ui" font-weight="bold" text-anchor="middle">D</text>
</svg>"""

SVG_CARNOT_CYCLE = """<svg viewBox="0 0 460 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Axes -->
  <line x1="60" y1="190" x2="420" y2="190" stroke="#475569" stroke-width="2.5"/>
  <line x1="60" y1="190" x2="60" y2="20" stroke="#475569" stroke-width="2.5"/>
  <text x="415" y="180" fill="#475569" font-size="13" font-family="system-ui" font-weight="bold">Volume (V)</text>
  <text x="70" y="30" fill="#475569" font-size="13" font-family="system-ui" font-weight="bold">Pressure (P)</text>
  
  <!-- Carnot Loop Path -->
  <path d="M 120 50 Q 180 65 240 90 Q 280 130 320 160 Q 250 155 180 145 Q 150 100 120 50 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="3"/>
  
  <!-- Vertices -->
  <circle cx="120" cy="50" r="4.5" fill="#dc2626"/><text x="105" y="45" fill="#dc2626" font-size="13" font-family="system-ui" font-weight="bold">1 (P₁,V₁,T₁)</text>
  <circle cx="240" cy="90" r="4.5" fill="#dc2626"/><text x="250" y="85" fill="#dc2626" font-size="13" font-family="system-ui" font-weight="bold">2 (P₂,V₂,T₁)</text>
  <circle cx="320" cy="160" r="4.5" fill="#2563eb"/><text x="330" y="165" fill="#2563eb" font-size="13" font-family="system-ui" font-weight="bold">3 (P₃,V₃,T₂)</text>
  <circle cx="180" cy="145" r="4.5" fill="#2563eb"/><text x="145" y="165" fill="#2563eb" font-size="13" font-family="system-ui" font-weight="bold">4 (P₄,V₄,T₂)</text>
  
  <!-- Process Labels -->
  <text x="180" y="55" fill="#b91c1c" font-size="11" font-family="system-ui" font-weight="bold">Isothermal (Q_in at T₁)</text>
  <text x="295" y="120" fill="#475569" font-size="11" font-family="system-ui" font-weight="bold">Adiabatic</text>
  <text x="210" y="175" fill="#1d4ed8" font-size="11" font-family="system-ui" font-weight="bold">Isothermal (Q_out at T₂)</text>
  <text x="105" y="110" fill="#475569" font-size="11" font-family="system-ui" font-weight="bold">Adiabatic</text>
</svg>"""

SVG_TWO_CONDUCTORS_SERIES = """<svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <defs>
    <linearGradient id="cond1Grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="50%" stop-color="#60a5fa"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="cond2Grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="50%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect x="70" y="55" width="170" height="60" rx="6" fill="url(#cond1Grad)" stroke="#1e3a8a" stroke-width="2"/>
  <ellipse cx="70" cy="85" rx="14" ry="30" fill="#2563eb" stroke="#1e3a8a" stroke-width="2"/>
  <text x="155" y="82" fill="#ffffff" font-size="14" font-family="system-ui" font-weight="bold" text-anchor="middle">Metal 1 (σ₁)</text>
  <text x="155" y="100" fill="#eff6ff" font-size="11" font-family="system-ui" text-anchor="middle">Length = L, Area = A</text>
  <rect x="240" y="55" width="170" height="60" rx="6" fill="url(#cond2Grad)" stroke="#b45309" stroke-width="2"/>
  <ellipse cx="240" cy="85" rx="14" ry="30" fill="#d97706" stroke="#b45309" stroke-width="2"/>
  <ellipse cx="410" cy="85" rx="14" ry="30" fill="#f59e0b" stroke="#b45309" stroke-width="2"/>
  <text x="325" y="82" fill="#ffffff" font-size="14" font-family="system-ui" font-weight="bold" text-anchor="middle">Metal 2 (σ₂)</text>
  <text x="325" y="100" fill="#fffbeb" font-size="11" font-family="system-ui" text-anchor="middle">Length = L, Area = A</text>
  <line x1="20" y1="85" x2="60" y2="85" stroke="#0f172a" stroke-width="3"/>
  <polygon points="65,85 55,80 55,90" fill="#0f172a"/>
  <text x="35" y="75" fill="#0f172a" font-size="13" font-family="system-ui" font-weight="bold">I</text>
  <line x1="420" y1="85" x2="480" y2="85" stroke="#0f172a" stroke-width="3"/>
  <polygon points="485,85 475,80 475,90" fill="#0f172a"/>
  <text x="450" y="75" fill="#0f172a" font-size="13" font-family="system-ui" font-weight="bold">I</text>
  <line x1="70" y1="135" x2="410" y2="135" stroke="#64748b" stroke-width="1.5"/>
  <line x1="70" y1="128" x2="70" y2="142" stroke="#64748b" stroke-width="1.5"/>
  <line x1="240" y1="128" x2="240" y2="142" stroke="#64748b" stroke-width="1.5"/>
  <line x1="410" y1="128" x2="410" y2="142" stroke="#64748b" stroke-width="1.5"/>
  <text x="155" y="152" fill="#475569" font-size="12" font-family="system-ui" text-anchor="middle">L</text>
  <text x="325" y="152" fill="#475569" font-size="12" font-family="system-ui" text-anchor="middle">L</text>
  <text x="240" y="172" fill="#0369a1" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">Equivalent Conductivity: σ_eq = 2σ₁σ₂ / (σ₁ + σ₂)</text>
</svg>"""

SVG_COIL_MAGNETIC_MOMENT = """<svg viewBox="0 0 460 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <line x1="40" y1="100" x2="420" y2="100" stroke="#94a3b8" stroke-dasharray="4 3" stroke-width="1.5"/>
  <ellipse cx="200" cy="100" rx="35" ry="75" fill="none" stroke="#2563eb" stroke-width="4"/>
  <line x1="200" y1="100" x2="200" y2="25" stroke="#dc2626" stroke-width="2"/>
  <text x="185" y="65" fill="#dc2626" font-size="12" font-family="system-ui" font-weight="bold">R = 5 cm</text>
  <circle cx="200" cy="100" r="4" fill="#0f172a"/>
  <text x="205" y="115" fill="#0f172a" font-size="12" font-family="system-ui" font-weight="bold">O (Centre)</text>
  <polygon points="166,95 163,108 171,105" fill="#2563eb"/>
  <polygon points="234,105 237,92 229,95" fill="#2563eb"/>
  <text x="140" y="105" fill="#2563eb" font-size="12" font-family="system-ui" font-weight="bold">I</text>
  <line x1="200" y1="100" x2="360" y2="100" stroke="#16a34a" stroke-width="3.5"/>
  <polygon points="368,100 355,94 355,106" fill="#16a34a"/>
  <text x="270" y="85" fill="#16a34a" font-size="13" font-family="system-ui" font-weight="bold">B_centre = μ₀NI / 2R</text>
  <text x="270" y="125" fill="#0f766e" font-size="13" font-family="system-ui" font-weight="bold">M = NI(πR²)</text>
  <text x="200" y="190" fill="#334155" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">N = 100 turns, B = 3.14 × 10⁻³ T → I = 2.5 A, M ≈ 2 A·m²</text>
</svg>"""

physics_questions = [
    {
        "id": 'PHY-001',
        "exam": 'NEET, JEE, WBJEE, CUET, VITEEE, MHT-CET, KCET, CBSE',
        "subject": 'Physics',
        "topic": 'Units and Measurement',
        "difficulty": 'Easy',
        "en": 'In a Vernier callipers, 20 Vernier Scale Divisions (VSD) coincide with 16 Main Scale Divisions (MSD). If each MSD is 1 mm, the least count of the Vernier callipers is:',
        "bn": 'একটি ভার্নিয়ার ক্যালিপার্সে, ২০টি ভার্নিয়ার স্কেল ঘর (VSD) ১৬টি মূল স্কেল ঘরের (MSD) সাথে মিলে যায়। মূল স্কেলের প্রতিটি ঘর ১ মিমি হলে ভার্নিয়ার ধ্রুবক (Least Count) কত?',
        "opts": {'en': ['0.02 cm', '0.01 cm', '0.2 mm', '0.02 mm'], 'bn': ['0.02 cm', '0.01 cm', '0.2 mm', '0.02 mm']},
        "correct": 0,
        "expl_en": '1 VSD = (16/20) MSD = 0.8 mm. Least Count LC = 1 MSD - 1 VSD = 1 mm - 0.8 mm = 0.2 mm = 0.02 cm.',
        "expl_bn": '১ VSD = (১৬/২০) MSD = ০.৮ মিমি। ভার্নিয়ার ধ্রুবক LC = ১ MSD - ১ VSD = ১ - ০.৮ = ০.২ মিমি = ০.০২ সেমি।',
    },
    {
        "id": 'PHY-002',
        "exam": 'JEE, WBJEE, BITSAT, NDA, MHT-CET, VITEEE, KCET',
        "subject": 'Physics',
        "topic": 'Kinematics',
        "difficulty": 'Medium',
        "en": 'A projectile is thrown with an initial velocity of u = (6i + 8j) m/s. The horizontal range of the projectile is (take g = 10 m/s²):',
        "bn": 'একটি প্রক্ষেপ্যকে (6i + 8j) m/s প্রারম্ভিক বেগে নিক্ষেপ করা হলো। প্রক্ষেপ্যটির অনুভূমিক সীমা (Range) কত? (g = 10 m/s²):',
        "opts": {'en': ['9.6 m', '4.8 m', '12.8 m', '19.2 m'], 'bn': ['9.6 m', '4.8 m', '12.8 m', '19.2 m']},
        "correct": 0,
        "expl_en": 'u<sub>x</sub> = 6 m/s, u<sub>y</sub> = 8 m/s. Time of flight T = 2 u<sub>y</sub> / g = 2(8)/10 = 1.6 s. Horizontal Range R = u<sub>x</sub> × T = 6 × 1.6 = 9.6 m.',
        "expl_bn": 'u<sub>x</sub> = ৬ m/s, u<sub>y</sub> = ৮ m/s। উড্ডয়ন কাল T = ১.৬ সেকেন্ড। অনুভূমিক সীমা R = ৬ × ১.৬ = ৯.৬ মিটার।',
    },
    {
        "id": 'PHY-003',
        "exam": 'WBJEE, JEE, NEET, CUET, VITEEE, MHT-CET, KCET, COMEDK',
        "subject": 'Physics',
        "topic": 'Current Electricity',
        "difficulty": 'Medium',
        "en": 'A wire of resistance R is stretched uniformly such that its length increases by 10%. The percentage increase in its resistance is approximately:',
        "bn": 'R রোধের একটি পরিবাহী তারকে সুষমভাবে টেনে দৈর্ঘ্য ১০% বৃদ্ধি করা হলো। তারটির রোধের শতকরা বৃদ্ধি কত হবে?',
        "opts": {'en': ['21%', '10%', '20%', '11%'], 'bn': ['21%', '10%', '20%', '11%']},
        "correct": 0,
        "expl_en": "Since volume V = A × L remains constant during stretching, R ∝ L². If L' = 1.1 L, then R' = (1.1)² R = 1.21 R. Percentage increase = (1.21 - 1) × 100% = 21%.",
        "expl_bn": "আয়তন ধ্রুবক থাকায় R ∝ L²। L' = ১.১ L হলে R' = ১.২১ R। রোধের শতকরা বৃদ্ধি = ২১%।",
    },
    {
        "id": 'PHY-004',
        "exam": 'NEET, CUET, WBJEE, NDA, CBSE, AIIMS, AFMC',
        "subject": 'Physics',
        "topic": 'Ray Optics',
        "difficulty": 'Easy',
        "en": 'A convex lens of focal length 20 cm in air is immersed in water of refractive index 4/3. If refractive index of glass is 3/2, its new focal length in water is:',
        "bn": 'বায়ুতে ২০ সেমি ফোকাস দূরত্বের একটি উত্তল লেন্সকে ৪/৩ প্রতিসরাঙ্কের পানিতে নিমজ্জিত করা হলো। কাঁচের প্রতিসরাঙ্ক ৩/২ হলে পানিতে লেন্সটির নতুন ফোকাস দূরত্ব কত?',
        "opts": {'en': ['80 cm', '40 cm', '20 cm', '60 cm'], 'bn': ['80 cm', '40 cm', '20 cm', '60 cm']},
        "correct": 0,
        "expl_en": "By Lens Maker's Formula: 1/f<sub>air</sub> = (1.5 - 1)(1/R1 - 1/R2) = 0.5 K => K = 1/10. In water: 1/f<sub>water</sub> = [(1.5 / 1.333) - 1] K = (1/8)(1/10) = 1/80 => f<sub>water</sub> = 80 cm.",
        "expl_bn": 'লেন্স মেকার সূত্রানুসারে: f<sub>water</sub> = 4 × f<sub>air</sub> = ৪ × ২০ = ৮০ সেমি।',
    },
    {
        "id": 'PHY-005',
        "exam": 'JEE, WBJEE, IAT, NEET, BITSAT, OLYMPIAD, IIT-JAM',
        "subject": 'Physics',
        "topic": 'Modern Physics & Dual Nature',
        "difficulty": 'Medium',
        "en": 'The de Broglie wavelength of an electron accelerated through a potential difference of 100 V is approximately:',
        "bn": '১০০ ভোল্ট বিভব পার্থক্যের মধ্য দিয়ে ত্বরান্বিত একটি ইলেকট্রনের দ্য ব্রগলি তরঙ্গদৈর্ঘ্য কত?',
        "opts": {'en': ['1.227 Å', '0.123 Å', '12.27 Å', '0.613 Å'], 'bn': ['1.227 Å', '0.123 Å', '12.27 Å', '0.613 Å']},
        "correct": 0,
        "expl_en": 'For an electron accelerated by V volts: λ = 12.27 / √V Å = 12.27 / √100 Å = 12.27 / 10 = 1.227 Å (or 0.1227 nm).',
        "expl_bn": 'ইলেকট্রনের জন্য λ = ১২.২৭ / √V Å = ১২.২৭ / ১০ = ১.২২৭ Å।',
    },
    {
        "id": 'PHY-006',
        "exam": 'JEE, WBJEE, NEET, BITSAT, IAT, NEST, KCET, COMEDK',
        "subject": 'Physics',
        "topic": 'Experimental Physics & Instruments',
        "difficulty": 'Hard',
        "diagram": SVG_SCREW_GAUGE,
        "en": 'A screw gauge has a pitch of 0.5 mm and 50 divisions on its circular scale. When measuring a wire, the linear scale reads 3 mm and the 32nd division coincides with the reference line. If the screw gauge has a negative zero error of -0.02 mm, the true diameter of the wire is:',
        "bn": 'একটি স্ক্রু গেজের পিচ ০.৫ মিমি এবং বৃত্তাকার স্কেলে ৫০টি ভাগ রয়েছে। একটি তারের ব্যাস পরিমাপে রৈখিক স্কেলের পাঠ ৩ মিমি এবং বৃত্তাকার স্কেলের ৩২তম দাগ নির্দেশক রেখার সাথে মিলে যায়। যন্ত্রটিতে যদি -০.০২ মিমি ঋণাত্মক শূন্য ত্রুটি থাকে, তবে তারটির প্রকৃত ব্যাস কত?',
        "opts": {'en': ['3.34 mm', '3.30 mm', '3.32 mm', '3.36 mm'], 'bn': ['3.34 mm', '3.30 mm', '3.32 mm', '3.36 mm']},
        "correct": 0,
        "expl_en": 'Least Count LC = Pitch / Total Circular Divisions = 0.5 mm / 50 = 0.01 mm. Measured Reading = MSR + (CSR × LC) = 3 mm + (32 × 0.01 mm) = 3.32 mm. True Reading = Measured Reading - (Zero Error) = 3.32 mm - (-0.02 mm) = 3.34 mm.',
        "expl_bn": 'লঘিষ্ঠ ধ্রুবক LC = ০.৫ / ৫০ = ০.০১ মিমি। পরিমাপকৃত মান = ৩ + (৩২ × ০.০১) = ৩.৩২ মিমি। প্রকৃত মান = ৩.৩২ - (-০.০২) = ৩.৩৪ মিমি।',
    },
    {
        "id": 'PHY-007',
        "exam": 'JEE, WBJEE, IAT, BITSAT, VITEEE, MHT-CET, GATE',
        "subject": 'Physics',
        "topic": 'Alternating Current',
        "difficulty": 'Hard',
        "diagram": SVG_LCR_CIRCUIT,
        "en": 'In the given series LCR circuit connected to an AC source V = V₀ sin(100πt + π/6), the voltmeters read V<sub>L</sub> = 40 V, V<sub>R</sub> = 40 V, and the circuit parameters are Z = 5 Ω, R = 4 Ω. The capacitive reactance X<sub>C</sub> and the peak voltage V₀ of the AC source are respectively:',
        "bn": 'চিত্রে প্রদর্শিত শ্রেণী LCR বর্তনীতে V = V₀ sin(100πt + π/6) পরিবর্তী উৎসের সাথে যুক্ত থাকলে ভোল্টমিটারের পাঠ V<sub>L</sub> = 40 V, V<sub>R</sub> = 40 V এবং বর্তনীর প্রতিবন্ধকতা Z = 5 Ω, রোধ R = 4 Ω। ধারকীয় প্রতিঘাত X<sub>C</sub> এবং উৎসের শীর্ষ ভোল্টেজ V₀ যথাক্রমে কত?',
        "opts": {'en': ['1 Ω and 50√2 V', '7 Ω and 50 V', '1 Ω and 50 V', '3 Ω and 40√2 V'], 'bn': ['1 Ω এবং 50√2 V', '7 Ω and 50 V', '1 Ω and 50 V', '3 Ω and 40√2 V']},
        "correct": 0,
        "expl_en": 'Current I<sub>rms</sub> = V<sub>R</sub> / R = 40/4 = 10 A. Peak current I<sub>0</sub> = 10√2 A. Effective voltage V<sub>rms</sub> = I<sub>rms</sub> × Z = 10 × 5 = 50 V => V<sub>0</sub> = 50√2 V. Reactance X<sub>L</sub> = V<sub>L</sub> / I<sub>rms</sub> = 40/10 = 4 Ω. Since Z² = R² + (X<sub>L</sub> - X<sub>C</sub>)², 25 = 16 + (4 - X<sub>C</sub>)² => (4 - X<sub>C</sub>)² = 9 => 4 - X<sub>C</sub> = 3 => X<sub>C</sub> = 1 Ω.',
        "expl_bn": 'তড়িৎপ্রবাহ I<sub>rms</sub> = ৪০/৪ = ১০ A। কার্যকর ভোল্টেজ V<sub>rms</sub> = ১০ × ৫ = ৫০ V, শীর্ষ ভোল্টেজ V₀ = ৫০√২ V। প্রতিঘাত X<sub>L</sub> = ৪০/১০ = ৪ Ω। Z² = R² + (X<sub>L</sub> - X<sub>C</sub>)² থেকে X<sub>C</sub> = ১ Ω।',
    },
    {
        "id": 'PHY-008',
        "exam": 'JEE, WBJEE, NDA, NEET, CDS, AFCAT, MHT-CET',
        "subject": 'Physics',
        "topic": 'Laws of Motion & Equilibrium',
        "difficulty": 'Medium',
        "diagram": SVG_MECHANICAL_EQUILIBRIUM,
        "en": 'Block B of weight W lies on a rough horizontal table with coefficient of static friction μ. The cord between block B and the knot is horizontal, while the cord to the wall makes an angle θ with the ceiling. The maximum weight of hanging block A for which the system remains in stationary equilibrium is:',
        "bn": 'W ওজনের একটি ব্লক B একটি খসখসে অনুভূমিক টেবিলের ওপর রাখা আছে যার স্থৈতিক ঘর্ষণ গুণাঙ্ক μ। B এবং নটের (knot) মধ্যবর্তী দড়িটি অনুভূমিক এবং ছাদের সাথে যুক্ত দড়িটি ছাদের সাথে θ কোণ উৎপন্ন করে। ঝুলন্ত ব্লক A-এর সর্বোচ্চ কত ওজনের জন্য সংস্থাটি সাম্যাবস্থায় স্থির থাকবে?',
        "opts": {'en': ['μ W tan θ', 'W tan θ / μ', 'μ W sin θ', 'μ W √(1 + tan² θ)'], 'bn': ['μ W tan θ', 'W tan θ / μ', 'μ W sin θ', 'μ W √(1 + tan² θ)']},
        "correct": 0,
        "expl_en": 'At the knot: let slanted tension be T. Horizontal equilibrium: T cos θ = T<sub>horiz</sub> = f<sub>s</sub> ≤ μ W. Vertical equilibrium: T sin θ = W<sub>A</sub>. Dividing the two equations: W<sub>A</sub> / (μ W) = tan θ => W<sub>A</sub> = μ W tan θ.',
        "expl_bn": 'নট বিন্দুতে সাম্যাবস্থা বিবেচনা করে: অনুভূমিক উপাংশ T cos θ = μ W এবং উল্লম্ব উপাংশ T sin θ = W<sub>A</sub>। ভাগ করে পাওয়া যায় W<sub>A</sub> = μ W tan θ।',
    },
    {
        "id": 'PHY-009',
        "exam": 'JEE, JEE-ADV, IAT, WBJEE, NEST, OLYMPIAD, IIT-JAM',
        "subject": 'Physics',
        "topic": 'Gravitation',
        "difficulty": 'Hard',
        "diagram": SVG_SPHERE_CAVITY,
        "en": 'From a uniform solid sphere of mass M and radius R, a spherical cavity of radius R/2 is removed such that its surface touches the boundary of the sphere. Taking gravitational potential V = 0 at r = ∞, the gravitational potential at the center P of the cavity thus formed is:',
        "bn": 'M ভর ও R ব্যাসার্ধের একটি সুষম নিরেট গোলক থেকে R/2 ব্যাসার্ধের একটি গোলকীয় গহ্বর অপসারণ করা হলো যা মূল গোলকের পৃষ্ঠ স্পর্শ করে। r = ∞ তে মহাকর্ষীয় বিভব V = 0 ধরে, উৎপন্ন গহ্বরের কেন্দ্রবিন্দু P-তে মহাকর্ষীয় বিভব কত?',
        "opts": {'en': ['-GM / R', '-2GM / 3R', '-GM / 2R', '-2GM / R'], 'bn': ['-GM / R', '-2GM / 3R', '-GM / 2R', '-2GM / R']},
        "correct": 0,
        "expl_en": "By superposition principle: V<sub>P</sub> = V<sub>entire</sub>(at r = R/2) - V<sub>removed</sub>(at its own center). For complete sphere: V<sub>entire</sub>(R/2) = -(GM / 2R³)[3R² - (R/2)²] = -11GM / (8R). The removed cavity has mass M' = M( (R/2)³ / R³ ) = M/8 and radius R' = R/2. Potential at its center V<sub>removed</sub>(0) = -3G M' / (2R') = -3G(M/8) / [2(R/2)] = -3GM / (8R). Therefore, V<sub>P</sub> = -11GM/(8R) - [-3GM/(8R)] = -8GM/(8R) = -GM/R.",
        "expl_bn": 'উপরিলেপন নীতি অনুযায়ী: V<sub>P</sub> = V<sub>সম্পূর্ণ</sub>(R/2) - V<sub>অপসারিত</sub>(0)। সম্পূর্ণ গোলকের জন্য বিভব = -১১GM/(৮R) এবং অপসারিত অংশের কেন্দ্রে নিজস্ব বিভব = -৩GM/(৮R)। অতএব V<sub>P</sub> = -GM/R।',
    },
    {
        "id": 'PHY-010',
        "exam": 'NEET, JEE, WBJEE, NDA, CUET, AIIMS, AFMC, KCET',
        "subject": 'Physics',
        "topic": 'Ray Optics & Optical Instruments',
        "difficulty": 'Medium',
        "diagram": SVG_PRISM_TIR,
        "en": 'A light ray is incident normally on face AB of a right-angled isosceles prism (A = 90°, B = 45°, C = 45°). If the refractive index of the prism material is μ = 1.50, the angle of deviation experienced by the ray upon emerging is:',
        "bn": 'একটি সমকোণী সমদ্বিবাহু প্রিজমের (A = ৯০°, B = ৪৫°, C = ৪৫°) AB তলে একটি আলোক রশ্মি লম্বভাবে আপতিত হলো। প্রিজমের উপাদানের প্রতিসরাঙ্ক μ = ১.৫০ হলে নির্গমনকালে রশ্মিটির চ্যুতি কোণ (Angle of Deviation) কত হবে?',
        "opts": {'en': ['90°', '45°', '0°', '180°'], 'bn': ['90°', '45°', '0°', '180°']},
        "correct": 0,
        "expl_en": 'Critical angle C<sub>c</sub> = sin⁻¹(1/μ) = sin⁻¹(1/1.5) = 41.8°. Inside the prism, the ray strikes the hypotenuse BC at an angle of incidence i = 45°. Since i > C<sub>c</sub>, Total Internal Reflection (TIR) occurs at BC and the ray exits perpendicular to face AC. Net deviation δ = 90°.',
        "expl_bn": 'সংকট কোণ C<sub>c</sub> = sin⁻¹(১/১.৫) = ৪১.৮°। প্রিজমের অভ্যন্তরে অতিভুজ পৃষ্ঠে আপতন কোণ i = ৪৫° যা সংকট কোণের চেয়ে বড়। ফলে পূর্ণ অভ্যন্তরীণ প্রতিফলন ঘটে এবং রশ্মিটি ৯০° কোণে বিচ্যুত হয়।',
    },
    {
        "id": 'PHY-011',
        "exam": 'JEE, WBJEE, BITSAT, NEET, CUET, NDA, MHT-CET',
        "subject": 'Physics',
        "topic": 'Current Electricity & Bridge Circuits',
        "difficulty": 'Easy',
        "diagram": SVG_WHEATSTONE_BRIDGE,
        "en": 'In the balanced Wheatstone bridge circuit shown in the diagram, the values of the three known resistors are P = 10 Ω, Q = 20 Ω, and R = 15 Ω. For zero deflection in the galvanometer, the unknown resistance S must be:',
        "bn": 'চিত্রে প্রদর্শিত নিস্পন্দ বা সাম্যাবস্থায় থাকা হুইটস্টোন ব্রিজ বর্তনীতে তিনটি জানা রোধের মান P = ১০ Ω, Q = ২০ Ω এবং R = ১৫ Ω। গ্যালভানোমিটারে শূন্য বিক্ষেপের জন্য অজানা রোধ S-এর মান কত হতে হবে?',
        "opts": {'en': ['30 Ω', '7.5 Ω', '25 Ω', '15 Ω'], 'bn': ['30 Ω', '7.5 Ω', '25 Ω', '15 Ω']},
        "correct": 0,
        "expl_en": 'For a balanced Wheatstone bridge with zero galvanometer deflection: P/Q = R/S => S = R × (Q/P) = 15 × (20/10) = 15 × 2 = 30 Ω.',
        "expl_bn": 'হুইটস্টোন ব্রিজের সাম্যাবস্থার শর্তানুসারে: P/Q = R/S => S = ১৫ × (২০/১০) = ৩০ Ω।',
    },
    {
        "id": 'PHY-012',
        "exam": 'JEE, JEE-ADV, WBJEE, IAT, NEET, IIT-JAM, GATE',
        "subject": 'Physics',
        "topic": 'Thermodynamics & Carnot Engine',
        "difficulty": 'Medium',
        "diagram": SVG_CARNOT_CYCLE,
        "en": 'A Carnot heat engine operates between source temperature T₁ = 500 K and sink temperature T₂ = 300 K. If it absorbs 600 J of heat from the high-temperature source per cycle, the work done by the engine per cycle is:',
        "bn": 'একটি কার্নো ইঞ্জিন T₁ = ৫০০ K তাপমাত্রার উৎস এবং T₂ = ৩০০ K তাপমাত্রার গ্রাহকের মধ্যে কার্যকর। ইঞ্জিনটি প্রতি চক্রে উৎস থেকে ৬০০ J তাপ শোষণ করলে প্রতি চক্রে কৃতকার্যের পরিমাণ কত?',
        "opts": {'en': ['240 J', '360 J', '300 J', '400 J'], 'bn': ['240 J', '360 J', '300 J', '400 J']},
        "correct": 0,
        "expl_en": 'Carnot efficiency η = 1 - T₂/T₁ = 1 - 300/500 = 1 - 0.6 = 0.4 (40%). Work done W = η × Q<sub>in</sub> = 0.4 × 600 J = 240 J.',
        "expl_bn": 'কার্নো ইঞ্জিনের কর্মদক্ষতা η = ১ - ৩০০/৫০০ = ০.৪ (৪০%)। প্রতি চক্রে কৃতকার্য W = ০.৪ × ৬০০ = ২৪০ জুল।',
    },
    {
        "id": 'PHY-013',
        "exam": 'NEET, JEE, WBJEE, CUET, BITSAT, VITEEE',
        "subject": 'Physics',
        "topic": 'Magnetic Effects of Current & Dipole Moment',
        "difficulty": 'Medium',
        "diagram": SVG_COIL_MAGNETIC_MOMENT,
        "en": 'A 100-turn closely wound circular coil of radius 5 cm carries a steady current such that the magnetic field at its centre is 3.14 × 10⁻³ T. Taking μ₀ = 4π × 10⁻⁷ T·m/A, the electric current flowing through the coil and the magnitude of the magnetic dipole moment of the coil are respectively:',
        "bn": '৫ সেমি ব্যাসার্ধের একটি ১০০ পাকের নিবিড়ভাবে জড়ানো বৃত্তাকার কুণ্ডলীর কেন্দ্রে চৌম্বক ক্ষেত্র ৩.১৪ × ১০⁻³ T। μ₀ = ৪π × ১০⁻⁷ T·m/A ধরে, কুণ্ডলীর মধ্য দিয়ে প্রবাহিত তড়িৎপ্রবাহ এবং কুণ্ডলীটির চৌম্বক দ্বিমেরু ভ্রামকের মান যথাক্রমে কত?',
        "opts": {'en': ['2.5 A and 2.0 A·m²', '2.5 A and 20.0 A·m²', '2.0 A and 4.0 A·m²', '2.0 A and 10.0 A·m²'], 'bn': ['2.5 A এবং 2.0 A·m²', '2.5 A এবং 20.0 A·m²', '2.0 A এবং 4.0 A·m²', '2.0 A এবং 10.0 A·m²']},
        "correct": 0,
        "expl_en": 'Magnetic field at centre: B = (μ₀ N I)/(2R) => I = (2 R B)/(μ₀ N) = (2 × 0.05 × 3.14 × 10⁻³)/(4π × 10⁻⁷ × 100) = 2.5 A. Magnetic moment: M = N I (π R²) = 100 × 2.5 × π × (0.05)² ≈ 1.963 A·m² ≈ 2.0 A·m².',
        "expl_bn": 'কুণ্ডলীর কেন্দ্রে চৌম্বক ক্ষেত্র: B = (μ₀ N I)/(2R) => I = (২ × ০.০৫ × ৩.১৪ × ১০⁻³)/(৪π × ১০⁻⁷ × ১০০) = ২.৫ A। চৌম্বক ভ্রামক: M = N I (π R²) = ১০০ × ২.৫ × π × (০.০৫)² ≈ ১.৯৬৩ A·m² ≈ ২.০ A·m²।',
    },
    {
        "id": 'PHY-014',
        "exam": 'JEE, WBJEE, NEET, CUET, MHT-CET, KCET, BITSAT',
        "subject": 'Physics',
        "topic": 'Current Electricity & Conductivity',
        "difficulty": 'Medium',
        "diagram": SVG_TWO_CONDUCTORS_SERIES,
        "en": 'Two metal rods of identical length L and cross-sectional area A have electrical conductivities σ₁ and σ₂ respectively. When they are joined end-to-end in series, the effective electrical conductivity (σ<sub>eq</sub>) of the combination is:',
        "bn": 'সমান দৈর্ঘ্য L এবং সমান প্রস্থচ্ছেদ A বিশিষ্ট দুটি ধাতব দণ্ডের তড়িৎ পরিবাহিতা যথাক্রমে σ₁ এবং σ₂। এদের শ্রেণি সমবায়ে যুক্ত করা হলে সমবায়টির কার্যকর তড়িৎ পরিবাহিতা (σ<sub>eq</sub>) কত হবে?',
        "opts": {'en': ['(2σ₁σ₂) / (σ₁ + σ₂)', '(σ₁ + σ₂) / 2', '√(σ₁σ₂)', '(σ₁σ₂) / (2(σ₁ + σ₂))'], 'bn': ['(2σ₁σ₂) / (σ₁ + σ₂)', '(σ₁ + σ₂) / 2', '√(σ₁σ₂)', '(σ₁σ₂) / (2(σ₁ + σ₂))']},
        "correct": 0,
        "expl_en": 'Total length = 2L, area = A. In series, equivalent resistance R<sub>eq</sub> = R₁ + R₂. Using R = L / (σ A): (2L)/(σ<sub>eq</sub> A) = L/(σ₁ A) + L/(σ₂ A) => 2/σ<sub>eq</sub> = (σ₁ + σ₂)/(σ₁σ₂) => σ<sub>eq</sub> = (2σ₁σ₂) / (σ₁ + σ₂).',
        "expl_bn": 'মোট দৈর্ঘ্য = 2L এবং ক্ষেত্রফল = A। শ্রেণি সমবায়ে তুল্য রোধ R<sub>eq</sub> = R₁ + R₂। R = L / (σ A) থেকে: 2/σ<sub>eq</sub> = 1/σ₁ + 1/σ₂ => σ<sub>eq</sub> = (2σ₁σ₂) / (σ₁ + σ₂), যা পরিবাহিতা দুটির হারমোনিক গড়।',
    },
    {
        "id": 'PHY-015',
        "exam": 'NEET, JEE, WBJEE, CUET, BITSAT, NDA',
        "subject": 'Physics',
        "topic": 'Alternating Current & Resonance',
        "difficulty": 'Medium',
        "en": 'An AC circuit consists of a pure resistance of 1 kΩ, a capacitor of capacitance 0.1 μF, and an inductor of inductance 1 mH connected in series. The approximate resonant frequency (f<sub>r</sub>) of the circuit and the effect on f<sub>r</sub> if the resistance is doubled are respectively:',
        "bn": 'একটি পরিবর্তী প্রবাহ (AC) বর্তনীতে ১ kΩ রোধ, ০.১ μF ধারকত্ব এবং ১ mH আবেশাঙ্ক শ্রেণি সমবায়ে যুক্ত রয়েছে। বর্তনীটির আনুমানিক অনুনাদী কম্পাঙ্ক (f<sub>r</sub>) এবং রোধ দ্বিগুণ করা হলে f<sub>r</sub>-এর ওপর প্রভাব যথাক্রমে:',
        "opts": {'en': ['15.9 kHz, unchanged', '10.1 kHz, halved', '15.9 kHz, doubled', '20.7 kHz, unchanged'], 'bn': ['15.9 kHz, অপরিবর্তিত থাকবে', '10.1 kHz, অর্ধেক হবে', '15.9 kHz, দ্বিগুণ হবে', '20.7 kHz, অপরিবর্তিত থাকবে']},
        "correct": 0,
        "expl_en": 'Series resonant frequency: f<sub>r</sub> = 1 / (2π√(LC)). With L = 10⁻³ H and C = 10⁻⁷ F, √(LC) = 10⁻⁵ s => f<sub>r</sub> = 10⁵ / (2π) ≈ 15.9 kHz. Because resonance depends solely on L and C and is independent of resistance R, doubling R leaves f<sub>r</sub> unchanged.',
        "expl_bn": 'অনুনাদী কম্পাঙ্ক: f<sub>r</sub> = ১ / (২π√(LC))। L = ১০⁻³ H এবং C = ১০⁻⁷ F হলে √(LC) = ১০⁻⁵ s => f<sub>r</sub> = ১০⁵ / (২π) ≈ ১৫.৯ kHz। অনুনাদী কম্পাঙ্ক রোধ R-এর ওপর নির্ভর করে না, তাই রোধ দ্বিগুণ করলেও তা অপরিবর্তিত থাকে।',
    },
    {
        "id": 'PHY-016',
        "exam": 'JEE, WBJEE, NEET, CUET, NDA, BITSAT',
        "subject": 'Physics',
        "topic": 'Current Electricity & Bridge Instruments',
        "difficulty": 'Medium',
        "en": 'In a balanced Metre Bridge experiment, the positions of the galvanometer and the battery cell are interchanged. Which of the following observations will be correct regarding the balance point?',
        "bn": 'একটি ভারসাম্যাবস্থায় থাকা মিটার ব্রিজ পরীক্ষায় গ্যালভানোমিটার এবং ব্যাটারি কোষের অবস্থান পরস্পর বিনিময় করা হলো। ভারসাম্যাবস্থার বিন্দুর ক্ষেত্রে নিচের কোন পর্যবেক্ষণটি সঠিক হবে?',
        "opts": {'en': ['The balance condition remains unaffected and the galvanometer still shows null deflection', 'The balance point shifts to the extreme right end', 'The balance point shifts to the extreme left end', 'The bridge becomes inoperable and permanent deflection occurs'], 'bn': ['ভারসাম্যের শর্ত অপরিবর্তিত থাকবে এবং গ্যালভানোমিটারে বিক্ষেপ শূন্যই থাকবে', 'ভারসাম্য বিন্দু চরম ডান প্রান্তে সরে যাবে', 'ভারসাম্য বিন্দু চরম বাম প্রান্তে সরে যাবে', 'ব্রিজটি অকার্যকর হয়ে যাবে এবং স্থায়ী বিক্ষেপ দেখাবে']},
        "correct": 0,
        "expl_en": 'By the conjugate arms property of a Wheatstone bridge, the battery arm and galvanometer arm are mutually conjugate. Interchanging the galvanometer and battery does not alter the balance condition (P/Q = R/S), so the galvanometer continues to show null deflection at the exact same point.',
        "expl_bn": 'হুইটস্টোন ব্রিজের অনুবন্ধী বাহু (Conjugate Arms) নীতি অনুসারে ব্যাটারি এবং গ্যালভানোমিটারের বাহু পরস্পর অনুবন্ধী। এদের অবস্থান বিনিময় করলেও ভারসাম্যের মূল শর্ত অপরিবর্তিত থাকে এবং গ্যালভানোমিটার শূন্য বিক্ষেপই প্রদর্শন করে।',
    },
    {
        "id": 'PHY-017',
        "exam": 'NEET, JEE, WBJEE, CUET, NDA',
        "subject": 'Physics',
        "topic": 'Kinematics & Motion in 1D',
        "difficulty": 'Easy',
        "en": 'A car accelerates uniformly from rest to a speed of 72 km/h in 10 seconds. The total distance covered by the car in this time interval is:',
        "bn": 'একটি গাড়ি স্থির অবস্থা থেকে সুষম ত্বরণে ১০ সেকেন্ডে ৭২ কিমি/ঘণ্টা বেগ অর্জন করে। এই সময় ব্যবধানে গাড়িটির অতিক্রান্ত মোট দূরত্ব কত?',
        "opts": {'en': ['100 m', '200 m', '50 m', '150 m'], 'bn': ['100 m', '200 m', '50 m', '150 m']},
        "correct": 0,
        "expl_en": 'Final velocity v = 72 km/h = 72 × (5/18) = 20 m/s. Acceleration a = (v - u)/t = (20 - 0)/10 = 2 m/s². Distance s = ut + 0.5 a t² = 0 + 0.5(2)(10)² = 100 m.',
        "expl_bn": 'অন্তিম বেগ v = ৭২ × (৫/১৮) = ২০ m/s। ত্বরণ a = ২০/১০ = ২ m/s²। অতিক্রান্ত দূরত্ব s = ut + 1/2 at² = ০ + ১/২(২)(১০)² = ১০০ মিটার।',
    },
    {
        "id": 'PHY-018',
        "exam": 'JEE, WBJEE, BITSAT, NEET',
        "subject": 'Physics',
        "topic": 'Relative Motion & River Boat Problems',
        "difficulty": 'Medium',
        "en": 'A boat can travel at 5 km/h in still water. If the river flows at 3 km/h and the river is 1 km wide, the minimum time required to cross the river along the shortest path is:',
        "bn": 'একটি নৌকা স্থির জলে ৫ কিমি/ঘণ্টা বেগে চলতে পারে। নদী ৩ কিমি/ঘণ্টা বেগে প্রবাহিত হলে এবং নদীর বিস্তার ১ কিমি হলে, ক্ষুদ্রতম পথে নদী পার হতে ন্যূনতম কত সময় লাগবে?',
        "opts": {'en': ['15 minutes', '12 minutes', '20 minutes', '10 minutes'], 'bn': ['১৫ মিনিট', '১২ মিনিট', '২০ মিনিট', '১০ মিনিট']},
        "correct": 0,
        "expl_en": 'For shortest path (perpendicular crossing), resultant velocity v<sub>net</sub> = √(v<sub>b</sub>² - v<sub>r</sub>²) = √(5² - 3²) = √16 = 4 km/h. Time t = d / v<sub>net</sub> = 1 km / (4 km/h) = 0.25 h = 15 minutes.',
        "expl_bn": 'ক্ষুদ্রতম পথে (সরাসরি নদীর বিপরীত পাড়ে) পারাপারের জন্য লব্ধি বেগ v<sub>net</sub> = √(৫² - ৩²) = ৪ কিমি/ঘণ্টা। প্রয়োজনীয় সময় t = ১/৪ ঘণ্টা = ১৫ মিনিট।',
    },
    {
        "id": 'PHY-019',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Laws of Motion & Friction',
        "difficulty": 'Medium',
        "en": 'A block of mass 2 kg is placed on a rough horizontal surface with coefficient of static friction μ<sub>s</sub> = 0.4. If a horizontal force of 6 N is applied to the block, the frictional force exerted by the surface on the block is (take g = 10 m/s²):',
        "bn": '২ কেজি ভরের একটি ব্লক অমসৃণ অনুভূমিক তলে রাখা আছে যার স্থির ঘর্ষণ গুণাঙ্ক μ<sub>s</sub> = ০.৪। ব্লকের ওপর ৬ N অনুভূমিক বল প্রয়োগ করা হলে তল কর্তৃক ব্লকের ওপর প্রযুক্ত ঘর্ষণ বল কত? (g = 10 m/s²):',
        "opts": {'en': ['6 N', '8 N', '4 N', '0 N'], 'bn': ['6 N', '8 N', '4 N', '0 N']},
        "correct": 0,
        "expl_en": 'Maximum static limiting friction f<sub>max</sub> = μ<sub>s</sub> × N = μ<sub>s</sub> × m g = 0.4 × 2 × 10 = 8 N. Since applied force F = 6 N < f<sub>max</sub>, the block does not move. Static friction is self-adjusting, so f = F<sub>applied</sub> = 6 N.',
        "expl_bn": 'সীমাস্ত ঘর্ষণ বল f<sub>max</sub> = μ<sub>s</sub> × mg = ০.৪ × ২ × ১০ = ৮ N। যেহেতু প্রযুক্ত বল ৬ N সীমাস্ত মানের চেয়ে কম, তাই ব্লকটি গতিশীল হবে না। স্ব-নিয়ন্ত্রক স্থির ঘর্ষণ বল প্রযুক্ত বলের সমান হবে, অর্থাৎ f = ৬ N।',
    },
    {
        "id": 'PHY-020',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Work, Energy and Power',
        "difficulty": 'Medium',
        "en": 'A variable force F = (3x² + 2x) N acts on a particle of mass 1 kg moving along the x-axis. The work done by this force in displacing the particle from x = 1 m to x = 3 m is:',
        "bn": 'x-অক্ষ বরাবর গতিশীল ১ কেজি ভরের একটি কণার ওপর পরিবর্তনশীল বল F = (3x² + 2x) N ক্রিয়া করে। কণাটিকে x = ১ মি থেকে x = ৩ মি অবস্থানে সরাতে কৃতকার্য কত?',
        "opts": {'en': ['34 J', '26 J', '30 J', '40 J'], 'bn': ['34 J', '26 J', '30 J', '40 J']},
        "correct": 0,
        "expl_en": 'Work done W = ∫ F dx = ∫₁³ (3x² + 2x) dx = [x³ + x²]₁³ = (3³ + 3²) - (1³ + 1²) = (27 + 9) - (1 + 1) = 36 - 2 = 34 J.',
        "expl_bn": 'কৃতকার্য W = ∫₁³ (3x² + 2x) dx = [x³ + x²]₁³ = (২৭ + ৯) - (১ + ১) = ৩৬ - ২ = ৩৪ জুল।',
    },
    {
        "id": 'PHY-021',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Work, Energy and Power & Collisions',
        "difficulty": 'Medium',
        "en": 'A ball of mass m moving with speed v collides head-on elastically with another stationary ball of identical mass m. After the collision, the velocities of the two balls are respectively:',
        "bn": 'v দ্রুতিতে গতিশীল m ভরের একটি বল অপর একটি স্থির সমভরের (m) বলের সাথে পূর্ণ স্থিতিস্থাপক মুখোমুখি সংঘর্ষে লিপ্ত হয়। সংঘর্ষের পর বল দুটির বেগ যথাক্রমে কত হবে?',
        "opts": {'en': ['0 and v', 'v/2 and v/2', 'v and 0', '-v/2 and v/2'], 'bn': ['0 এবং v', 'v/2 এবং v/2', 'v এবং 0', '-v/2 এবং v/2']},
        "correct": 0,
        "expl_en": 'In a 1D head-on elastic collision between two bodies of equal mass, the velocities are completely interchanged. Thus the incoming ball comes to rest (v₁ = 0) and the stationary target moves with velocity v₂ = v.',
        "expl_bn": 'সমান ভরের দুটি বস্তুর একমাত্রিক পূর্ণ স্থিতিস্থাপক সংঘর্ষে বেগদ্বয় পরস্পর বিনিময় হয়। ফলে প্রথম বলটি থেমে যায় (v₁ = ০) এবং দ্বিতীয় বলটি v বেগে চলতে শুরু করে।',
    },
    {
        "id": 'PHY-022',
        "exam": 'JEE, WBJEE, BITSAT, NEET',
        "subject": 'Physics',
        "topic": 'Rotational Motion & Moment of Inertia',
        "difficulty": 'Hard',
        "en": 'A solid cylinder and a hollow cylinder of identical mass M and outer radius R roll down an inclined plane without slipping from the same height. The ratio of their linear accelerations (a<sub>solid</sub> / a<sub>hollow</sub>) down the incline is:',
        "bn": 'সমান ভর M এবং ব্যাসার্ধ R বিশিষ্ট একটি নিরেট চোঙ এবং একটি ফাঁপা চোঙ একই উচ্চতা থেকে একটি নততল বেয়ে না পিছলে গড়িয়ে নিচে নামে। তাদের রৈখিক ত্বরণের অনুপাত (a<sub>solid</sub> / a<sub>hollow</sub>) কত?',
        "opts": {'en': ['4 / 3', '3 / 2', '2 / 1', '5 / 4'], 'bn': ['4 / 3', '3 / 2', '2 / 1', '5 / 4']},
        "correct": 0,
        "expl_en": 'Pure rolling acceleration on an incline: a = (g sin θ) / (1 + I / (M R²)). For a solid cylinder, I = 0.5 M R² => a<sub>s</sub> = (g sin θ)/(1 + 0.5) = (2/3) g sin θ. For a hollow cylinder, I = M R² => a<sub>h</sub> = (g sin θ)/(1 + 1) = (1/2) g sin θ. Ratio = (2/3) / (1/2) = 4/3.',
        "expl_bn": 'নততলে ঘূর্ণনের ক্ষেত্রে ত্বরণ a = (g sin θ) / (১ + I/(MR²))। নিরেট চোঙের জন্য I = ০.৫ MR² => a<sub>s</sub> = (২/৩) g sin θ। ফাঁপা চোঙের জন্য I = MR² => a<sub>h</sub> = (১/২) g sin θ। ত্বরণের অনুপাত = (২/৩) / (১/২) = ৪/৩।',
    },
    {
        "id": 'PHY-023',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Gravitation & Escape Velocity',
        "difficulty": 'Easy',
        "en": 'If the mass of the Earth remains constant but its radius shrinks by 1%, the acceleration due to gravity (g) on the surface of the Earth will:',
        "bn": 'পৃথিবীর ভর অপরিবর্তিত রেখে যদি এর ব্যাসার্ধ ১% সংকুচিত হয়, তবে ভূপৃষ্ঠে অভিকর্ষজ ত্বরণের (g) মান:',
        "opts": {'en': ['Increase by 2%', 'Decrease by 2%', 'Increase by 1%', 'Remain unchanged'], 'bn': ['২% বৃদ্ধি পাবে', '২% হ্রাস পাবে', '১% বৃদ্ধি পাবে', 'অপরিবর্তিত থাকবে']},
        "correct": 0,
        "expl_en": 'Since g = G M / R², for small fractional changes: Δg/g = -2 (ΔR/R). If radius shrinks by 1% (ΔR/R = -1%), Δg/g = -2(-1%) = +2%. Thus g increases by 2%.',
        "expl_bn": 'g = GM/R² সমীকরণ থেকে পাই: Δg/g = -২(ΔR/R)। ব্যাসার্ধ ১% কমলে (ΔR/R = -১%), অভিকর্ষজ ত্বরণ Δg/g = -২(-১%) = +২% বৃদ্ধি পাবে।',
    },
    {
        "id": 'PHY-024',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": "Gravitation & Kepler's Laws",
        "difficulty": 'Medium',
        "en": "A geostationary satellite orbits Earth at a height of approximately 6R above Earth's surface (orbital radius = 7R). The orbital period of a spy satellite orbiting at a height of 2.5R above Earth's surface (orbital radius = 3.5R) will be:",
        "bn": 'একটি ভূ-সমলয় উপগ্রহ ভূপৃষ্ঠ থেকে প্রায় 6R উচ্চতায় (কক্ষপথীয় ব্যাসার্ধ = 7R) পৃথিবীকে আবর্তন করে। ভূপৃষ্ঠ থেকে 2.5R উচ্চতায় (কক্ষপথীয় ব্যাসার্ধ = 3.5R) প্রদক্ষিণকারী একটি নজরদারি উপগ্রহের পর্যায়কাল কত হবে?',
        "opts": {'en': ['6√2 hours (≈ 8.48 h)', '12 hours', '6 hours', '3√2 hours'], 'bn': ['6√2 ঘণ্টা (≈ 8.48 ঘণ্টা)', '১২ ঘণ্টা', '৬ ঘণ্টা', '3√2 ঘণ্টা']},
        "correct": 0,
        "expl_en": "By Kepler's Third Law, T² ∝ r³. T<sub>geo</sub> = 24 h at r₁ = 7R. For r₂ = 3.5R = r₁/2: T₂ / T₁ = (r₂ / r₁)<sup>3/2</sup> = (1/2)<sup>3/2</sup> = 1 / (2√2). T₂ = 24 / (2√2) = 12 / √2 = 6√2 hours ≈ 8.48 h.",
        "expl_bn": 'কেপলারের ৩য় সূত্রানুসারে T² ∝ r³। ভূ-সমলয় উপগ্রহের T₁ = ২৪ ঘণ্টা, r₁ = 7R। r₂ = 3.5R = r₁/২ হলে: T₂ = ২৪ × (১/২)<sup>৩/২</sup> = ২৪ / (২√২) = ৬√২ ঘণ্টা ≈ ৮.৪৮ ঘণ্টা।',
    },
    {
        "id": 'PHY-025',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": "Mechanical Properties of Solids & Young's Modulus",
        "difficulty": 'Easy',
        "en": "A steel wire of length 2 m and cross-sectional area 2 mm² is stretched by a force of 400 N. If Young's modulus of steel is 2 × 10¹¹ N/m², the elongation produced in the wire is:",
        "bn": '২ মিটার দৈর্ঘ্য এবং ২ মিমি² প্রস্থচ্ছেদবিশিষ্ট একটি ইস্পাতের তারকে ৪০০ N বল দ্বারা টানা হলো। ইস্পাতের ইয়ং গুণাঙ্ক ২ × ১০¹¹ N/m² হলে তারটির দৈর্ঘ্য বৃদ্ধি কত?',
        "opts": {'en': ['2.0 mm', '1.0 mm', '0.5 mm', '4.0 mm'], 'bn': ['2.0 mm', '1.0 mm', '0.5 mm', '4.0 mm']},
        "correct": 0,
        "expl_en": 'Elongation ΔL = (F L) / (A Y). Here F = 400 N, L = 2 m, A = 2 mm² = 2 × 10⁻⁶ m², Y = 2 × 10¹¹ N/m². ΔL = (400 × 2) / (2 × 10⁻⁶ × 2 × 10¹¹) = 800 / (4 × 10⁵) = 2 × 10⁻³ m = 2.0 mm.',
        "expl_bn": 'দৈর্ঘ্য প্রসারণ ΔL = (FL) / (AY) = (৪০০ × ২) / (২ × ১০⁻⁶ × ২ × ১০¹¹) = ৮০০ / (৪ × ১০⁵) = ২ × ১০⁻³ মিটার = ২.০ মিমি।',
    },
    {
        "id": 'PHY-026',
        "exam": 'JEE, WBJEE, NEET, CUET',
        "subject": 'Physics',
        "topic": "Fluid Mechanics & Bernoulli's Theorem",
        "difficulty": 'Medium',
        "en": 'Water flows through a horizontal pipe of varying cross section. At a point where the cross-sectional area is 20 cm², the flow speed is 1 m/s and gauge pressure is 2000 Pa. At another point where the cross-sectional area is 10 cm², the speed and gauge pressure are (density = 1000 kg/m³):',
        "bn": 'পরিবর্তনশীল প্রস্থচ্ছেদের একটি অনুভূমিক নলের মধ্য দিয়ে জল প্রবাহিত হচ্ছে। ২০ সেমি² ক্ষেত্রফলযুক্ত স্থানে বেগ ১ m/s এবং গেজ চাপ ২০০০ Pa। ১০ সেমি² ক্ষেত্রফলযুক্ত অপর স্থানে প্রবাহের বেগ এবং গেজ চাপ কত? (ঘনত্ব = ১০০০ kg/m³):',
        "opts": {'en': ['2 m/s and 500 Pa', '2 m/s and 1000 Pa', '0.5 m/s and 2500 Pa', '4 m/s and 0 Pa'], 'bn': ['2 m/s এবং 500 Pa', '2 m/s এবং 1000 Pa', '0.5 m/s এবং 2500 Pa', '4 m/s এবং 0 Pa']},
        "correct": 0,
        "expl_en": "By equation of continuity: A₁ v₁ = A₂ v₂ => v₂ = (20/10) × 1 = 2 m/s. By Bernoulli's equation for horizontal flow: P₁ + 0.5 ρ v₁² = P₂ + 0.5 ρ v₂² => P₂ = P₁ + 0.5 ρ (v₁² - v₂²) = 2000 + 0.5(1000)(1 - 4) = 2000 - 1500 = 500 Pa.",
        "expl_bn": 'ধারাবাহিকতা সমীকরণ অনুসারে A₁v₁ = A₂v₂ => v₂ = ২ m/s। বার্নোলির সমীকরণ থেকে: P₂ = ২০০০ + ০.৫ × ১০০০ × (১² - ২²) = ২০০০ - ১৫০০ = ৫০০ Pa।',
    },
    {
        "id": 'PHY-027',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Thermal Properties & Heat Transfer',
        "difficulty": 'Medium',
        "en": 'A black body radiates heat at a temperature of 227 °C at a rate of 20 W. When its temperature is raised to 727 °C, the rate of heat radiation will become:',
        "bn": '২২৭ °C তাপমাত্রায় একটি কৃষ্ণবস্তু প্রতি সেকেন্ডে ২০ জুল হারে (২০ W) তাপ বিকিরণ করে। এর তাপমাত্রা বৃদ্ধি করে ৭২৭ °C করা হলে বিকিরণ হার কত হবে?',
        "opts": {'en': ['320 W', '160 W', '80 W', '640 W'], 'bn': ['320 W', '160 W', '80 W', '640 W']},
        "correct": 0,
        "expl_en": 'By Stefan-Boltzmann law, E ∝ T⁴. T₁ = 227 + 273 = 500 K. T₂ = 727 + 273 = 1000 K. E₂ / E₁ = (T₂ / T₁)⁴ = (1000 / 500)⁴ = 2⁴ = 16. E₂ = 16 × 20 W = 320 W.',
        "expl_bn": 'স্টিফানের সূত্রানুসারে বিকিরণ হার E ∝ T⁴। T₁ = ৫০০ K, T₂ = ১০০০ K। E₂/E₁ = (১০০০/৫০০)⁴ = ১৬। সুতরাং E₂ = ১৬ × ২০ W = ৩২০ W।',
    },
    {
        "id": 'PHY-028',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Thermodynamics & First Law',
        "difficulty": 'Hard',
        "en": 'In an adiabatic expansion of an ideal monoatomic gas (γ = 5/3), the volume increases by a factor of 8. The temperature of the gas changes by a factor of:',
        "bn": 'একটি আদর্শ এক-পরমাণুক গ্যাসের (γ = ৫/৩) রুদ্ধতাপীয় প্রসারণে আয়তন ৮ গুণ বৃদ্ধি পায়। গ্যাসের তাপমাত্রা পূর্বের তাপমাত্রার কত গুণ হবে?',
        "opts": {'en': ['1 / 4', '1 / 2', '1 / 8', '1 / 16'], 'bn': ['1 / 4', '1 / 2', '1 / 8', '1 / 16']},
        "correct": 0,
        "expl_en": 'For an adiabatic process: T V<sup>γ - 1</sup> = constant. T₂ / T₁ = (V₁ / V₂)<sup>γ - 1</sup> = (1 / 8)<sup>5/3 - 1</sup> = (1 / 8)<sup>2/3</sup> = ((1/8)<sup>1/3</sup>)² = (1/2)² = 1/4.',
        "expl_bn": 'রুদ্ধতাপ প্রক্রিয়ায় T V<sup>γ - 1</sup> = ধ্রুবক। T₂/T₁ = (১/৮)<sup>৫/৩ - ১</sup> = (১/৮)<sup>২/৩</sup> = (১/২)² = ১/৪।',
    },
    {
        "id": 'PHY-029',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Kinetic Theory of Gases',
        "difficulty": 'Easy',
        "en": 'The ratio of the root-mean-square (rms) speed of helium gas atoms (He, M = 4) to oxygen gas molecules (O₂, M = 32) at the same absolute temperature is:',
        "bn": 'একই পরম তাপমাত্রায় হিলিয়াম পরমাণুর (He, M = 4) এবং অক্সিজেন অণুর (O₂, M = 32) গড় বর্গবেগের বর্গমূলের (rms speed) অনুপাত কত?',
        "opts": {'en': ['2√2 : 1', '4 : 1', '8 : 1', '2 : 1'], 'bn': ['2√2 : 1', '4 : 1', '8 : 1', '2 : 1']},
        "correct": 0,
        "expl_en": 'v<sub>rms</sub> = √(3 R T / M) => v<sub>rms</sub> ∝ 1 / √M. v<sub>He</sub> / v<sub>O2</sub> = √(M<sub>O2</sub> / M<sub>He</sub>) = √(32 / 4) = √8 = 2√2.',
        "expl_bn": 'গ্যাসের rms বেগ v<sub>rms</sub> = √(3RT/M) ∝ ১/√M। v<sub>He</sub> / v<sub>O2</sub> = √(৩২/৪) = √৮ = ২√২ : ১।',
    },
    {
        "id": 'PHY-030',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Oscillations & Simple Harmonic Motion',
        "difficulty": 'Medium',
        "en": 'A particle executes simple harmonic motion with an amplitude A. At what displacement from the mean position does its kinetic energy equal its potential energy?',
        "bn": 'A বিস্তার নিয়ে একটি কণা সরল দোলগতি সম্পাদন করছে। সাম্যাবস্থা থেকে কত দূরত্বে কণাটির গতিশক্তি ও স্থিতিশক্তি পরস্পর সমান হবে?',
        "opts": {'en': ['A / √2', 'A / 2', 'A / 4', 'A √3 / 2'], 'bn': ['A / √2', 'A / 2', 'A / 4', 'A √3 / 2']},
        "correct": 0,
        "expl_en": 'KE = 0.5 m ω² (A² - x²) and PE = 0.5 m ω² x². Setting KE = PE: A² - x² = x² => 2 x² = A² => x = A / √2.',
        "expl_bn": 'গতিশক্তি KE = ১/২ m ω² (A² - x²) এবং স্থিতিশক্তি PE = ১/২ m ω² x²। KE = PE হলে: A² - x² = x² => x = A / √২।',
    },
    {
        "id": 'PHY-031',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Waves & Sound & Doppler Effect',
        "difficulty": 'Medium',
        "en": 'A train blowing a whistle of frequency 300 Hz approaches a stationary listener at a speed of 33 m/s. Taking the speed of sound in air as 330 m/s, the frequency heard by the listener is:',
        "bn": '৩০০ Hz কম্পাঙ্কের বাঁশি বাজিয়ে একটি ট্রেন ৩৩ m/s বেগে একজন স্থির শ্রোতার দিকে এগিয়ে আসছে। বায়ুতে শব্দের বেগ ৩৩০ m/s হলে শ্রোতা কর্তৃক শ্রুত আপাত কম্পাঙ্ক কত?',
        "opts": {'en': ['333.3 Hz', '300 Hz', '272.7 Hz', '360 Hz'], 'bn': ['333.3 Hz', '300 Hz', '272.7 Hz', '360 Hz']},
        "correct": 0,
        "expl_en": "By Doppler's effect for moving source approaching stationary observer: f' = f × v / (v - v<sub>s</sub>) = 300 × 330 / (330 - 33) = 300 × 330 / 297 = 300 × (10/9) = 333.3 Hz.",
        "expl_bn": "ডপলার ক্রিয়া অনুসারে f' = f × v / (v - v<sub>s</sub>) = ৩০০ × ৩৩০ / (৩৩০ - ৩৩) = ৩০০ × (১০/৯) = ৩৩৩.৩ Hz।",
    },
    {
        "id": 'PHY-032',
        "exam": 'JEE, WBJEE, NEET, CUET',
        "subject": 'Physics',
        "topic": "Electrostatics & Coulomb's Law",
        "difficulty": 'Easy',
        "en": 'Two point charges +q and +4q are separated by a distance d. A third charge Q is placed on the line joining them so that the entire system is in electrostatic equilibrium. The position and magnitude of Q are:',
        "bn": '+q এবং +4q আধানদ্বয় d দূরত্বে অবস্থিত। এদের সংযোগকারী সরলরেখায় একটি তৃতীয় আধান Q স্থাপন করা হলো যাতে সমগ্র সংস্থাটি ভারসাম্যে থাকে। Q এর অবস্থান ও মান কত?',
        "opts": {'en': ['At distance d/3 from +q, Q = -4q/9', 'At distance d/2 from +q, Q = -q/4', 'At distance d/3 from +q, Q = +4q/9', 'At distance 2d/3 from +q, Q = -q'], 'bn': ['+q থেকে d/3 দূরত্বে, Q = -4q/9', '+q থেকে d/2 দূরত্বে, Q = -q/4', '+q থেকে d/3 দূরত্বে, Q = +4q/9', '+q থেকে 2d/3 দূরত্বে, Q = -q']},
        "correct": 0,
        "expl_en": 'For net force on Q to be zero: q/x² = 4q/(d - x)² => 1/x = 2/(d - x) => d - x = 2x => x = d/3 from +q. For net force on +q to be zero: k(q)(4q)/d² + k(q)(Q)/(d/3)² = 0 => 4q/d² + 9Q/d² = 0 => Q = -4q/9.',
        "expl_bn": 'Q এর ওপর বল শূন্য হতে হলে: q/x² = 4q/(d-x)² => x = d/৩। +q এর ওপর লব্ধি বল শূন্য হতে হলে: 4q/d² + 9Q/d² = 0 => Q = -৪q/৯।',
    },
    {
        "id": 'PHY-033',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": "Electrostatics & Gauss's Law",
        "difficulty": 'Easy',
        "en": 'A point charge q is placed at the center of a cube of side a. The electric flux passing through each of the six faces of the cube is:',
        "bn": 'a বাহুবিশিষ্ট একটি ঘনকের কেন্দ্রে একটি বিন্দু আধান q অবস্থিত। ঘনকের প্রতিটি তলের মধ্য দিয়ে অতিক্রান্ত তড়িৎ ফ্লাক্স কত?',
        "opts": {'en': ['q / (6 ε₀)', 'q / ε₀', 'q / (8 ε₀)', 'q / (24 ε₀)'], 'bn': ['q / (6 ε₀)', 'q / ε₀', 'q / (8 ε₀)', 'q / (24 ε₀)']},
        "correct": 0,
        "expl_en": "By Gauss's law, total flux through the enclosed cube is Φ<sub>total</sub> = q / ε₀. By symmetry, the flux is distributed equally across all 6 faces, so flux through each face = q / (6 ε₀).",
        "expl_bn": 'গাউসের সূত্রানুসারে ঘনকের মধ্য দিয়ে মোট ফ্লাক্স Φ = q / ε₀। প্রতিসাম্যের কারণে ৬টি তলের প্রতিটির মধ্য দিয়ে ফ্লাক্স = q / (৬ ε₀)।',
    },
    {
        "id": 'PHY-034',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Capacitance & Dielectrics',
        "difficulty": 'Medium',
        "en": 'A parallel plate capacitor with air between the plates has a capacitance C₀. When a dielectric slab of dielectric constant K = 4 and thickness t = 0.5 d (where d is plate separation) is inserted between the plates, the new capacitance becomes:',
        "bn": 'বায়ু মাধ্যমযুক্ত একটি সমান্তরাল পাত ধারকের ধারকত্ব C₀। পাতদ্বয়ের মধ্যবর্তী দূরত্ব d হলে, K = ৪ পরাবৈদ্যুতিক ধ্রুবক এবং t = ০.৫ d পুরুত্বের একটি স্ল্যাব প্রবেশ করালে নতুন ধারকত্ব কত হবে?',
        "opts": {'en': ['1.6 C₀', '2.0 C₀', '1.25 C₀', '2.5 C₀'], 'bn': ['1.6 C₀', '2.0 C₀', '1.25 C₀', '2.5 C₀']},
        "correct": 0,
        "expl_en": 'Capacitance with partial dielectric: C = (ε₀ A) / (d - t + t/K). Substituting t = d/2 and K = 4: C = (ε₀ A) / (d - d/2 + d/8) = (ε₀ A) / (5d/8) = (8/5) (ε₀ A / d) = 1.6 C₀.',
        "expl_bn": 'আংশিক পরাবৈদ্যুতিক স্ল্যাবের ক্ষেত্রে C = (ε₀ A) / (d - t + t/K)। মান বসিয়ে: C = (ε₀ A) / (d - d/২ + d/৮) = (৮/৫) C₀ = ১.৬ C₀।',
    },
    {
        "id": 'PHY-035',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Current Electricity & Potentiometer',
        "difficulty": 'Medium',
        "en": 'In a potentiometer experiment, a cell of EMF 1.5 V gives a balance length of 30 cm. Another cell of unknown EMF gives a balance length of 40 cm on the same wire. The EMF of the second cell is:',
        "bn": 'একটি পোটেনশিওমিটার পরীক্ষায় ১.৫ V তড়িচ্চালক বলের একটি কোষ ৩০ সেমি তারে নিস্পন্দ বিন্দু দেয়। একই তারে একটি অজ্ঞাত কোষ ৪০ সেমি দৈর্ঘ্যে নিস্পন্দ বিন্দু দিলে অজ্ঞাত কোষটির তড়িচ্চালক বল কত?',
        "opts": {'en': ['2.0 V', '1.8 V', '2.5 V', '1.2 V'], 'bn': ['2.0 V', '1.8 V', '2.5 V', '1.2 V']},
        "correct": 0,
        "expl_en": 'In a potentiometer, E ∝ L. Thus E₂ / E₁ = L₂ / L₁ => E₂ = E₁ × (L₂ / L₁) = 1.5 × (40 / 30) = 1.5 × (4/3) = 2.0 V.',
        "expl_bn": 'পোটেনশিওমিটারে E ∝ L। সুতরাং E₂ = E₁ × (L₂/L₁) = ১.৫ × (৪০/৩০) = ২.০ V।',
    },
    {
        "id": 'PHY-036',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Magnetic Effects & Biot-Savart Law',
        "difficulty": 'Medium',
        "en": 'An electron moves with velocity v = 2 × 10⁶ m/s along the +x axis into a uniform magnetic field B = 0.5 T directed along the +y axis. The magnitude and direction of the magnetic Lorentz force on the electron are:',
        "bn": 'একটি ইলেকট্রন v = ২ × ১০⁶ m/s বেগে +x অক্ষ বরাবর গতিশীল হয়ে +y অক্ষ বরাবর ক্রিয়াশীল B = ০.৫ T সুষম চৌম্বক ক্ষেত্রে প্রবেশ করে। ইলেকট্রনটির ওপর ক্রিয়াশীল চৌম্বক বলের মান ও দিক কী?',
        "opts": {'en': ['1.6 × 10⁻¹³ N along -z axis', '1.6 × 10⁻¹³ N along +z axis', '3.2 × 10⁻¹³ N along -z axis', '0 N'], 'bn': ['1.6 × 10⁻¹³ N, -z অক্ষ বরাবর', '1.6 × 10⁻¹³ N, +z অক্ষ বরাবর', '3.2 × 10⁻¹³ N, -z অক্ষ বরাবর', '0 N']},
        "correct": 0,
        "expl_en": 'F = q (v × B). Magnitude F = e v B = (1.6 × 10⁻¹⁹ C)(2 × 10⁶ m/s)(0.5 T) = 1.6 × 10⁻¹³ N. Direction: v is +i, B is +j => i × j = +k. Since electron has negative charge, F is along -k (-z axis).',
        "expl_bn": 'লরেঞ্জ বল F = q (v × B)। মান F = (১.৬ × ১০⁻¹৯)(২ × ১০⁶)(০.৫) = ১.৬ × ১০⁻¹³ N। দিক: i × j = +k, কিন্তু ইলেকট্রন ঋণাত্মক আধানযুক্ত হওয়ায় বলের দিক হবে -k অর্থাৎ -z অক্ষ বরাবর।',
    },
    {
        "id": 'PHY-037',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Magnetism and Matter',
        "difficulty": 'Easy',
        "en": 'Which of the following substances has a negative magnetic susceptibility (χ < 0) and is weakly repelled by a magnetic field?',
        "bn": 'নিচের কোন পদার্থটির চৌম্বক গ্রাহিতা ঋণাত্মক (χ < 0) এবং চৌম্বক ক্ষেত্র দ্বারা মৃদুভাবে বিকর্ষিত হয়?',
        "opts": {'en': ['Copper (Diamagnetic)', 'Aluminum (Paramagnetic)', 'Iron (Ferromagnetic)', 'Nickel (Ferromagnetic)'], 'bn': ['তামা (তিরশ্চৌম্বক)', 'অ্যালুমিনিয়াম (পরাচৌম্বক)', 'লোহা (অয়শ্চৌম্বক)', 'নিকেল (অয়শ্চৌম্বক)']},
        "correct": 0,
        "expl_en": 'Diamagnetic materials such as copper, bismuth, and water have negative magnetic susceptibility (χ < 0) and are weakly repelled by magnetic fields.',
        "expl_bn": 'কপার (তামা), বিসমাথ প্রভৃতি তিরশ্চৌম্বক (ডায়াম্যাগনেটিক) পদার্থের চৌম্বক গ্রাহিতা ঋণাত্মক হয় এবং এরা চৌম্বক ক্ষেত্র দ্বারা সামান্য বিকর্ষিত হয়।',
    },
    {
        "id": 'PHY-038',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": "Electromagnetic Induction & Faraday's Law",
        "difficulty": 'Medium',
        "en": 'The magnetic flux through a stationary loop of resistance 10 Ω varies with time as Φ = (5t² - 4t + 1) Wb. The magnitude of the induced current at t = 2 s is:',
        "bn": '১০ Ω রোধের একটি স্থির লুপের মধ্য দিয়ে অতিক্রান্ত চৌম্বক ফ্লাক্স সময়ের সাথে Φ = (5t² - 4t + 1) Wb অনুসারে পরিবর্তিত হয়। t = ২ সেকেন্ড সময়ে আবিষ্ট তড়িৎপ্রবাহের মান কত?',
        "opts": {'en': ['1.6 A', '2.0 A', '0.8 A', '3.2 A'], 'bn': ['1.6 A', '2.0 A', '0.8 A', '3.2 A']},
        "correct": 0,
        "expl_en": 'Induced EMF e = |dΦ/dt| = |d/dt (5t² - 4t + 1)| = |10t - 4|. At t = 2 s: e = 10(2) - 4 = 16 V. Induced current I = e / R = 16 V / 10 Ω = 1.6 A.',
        "expl_bn": 'আবিষ্ট তড়িচ্চালক বল e = |dΦ/dt| = ১০t - ৪। t = ২ সেকেন্ডে e = ২০ - ৪ = ১৬ V। আবিষ্ট প্রবাহ I = ১৬/১০ = ১.৬ A।',
    },
    {
        "id": 'PHY-039',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Electromagnetic Waves',
        "difficulty": 'Easy',
        "en": 'In a plane electromagnetic wave propagating in vacuum, the electric field amplitude is E₀ = 60 V/m. The amplitude of the oscillating magnetic field B₀ is:',
        "bn": 'শূন্য মাধ্যমে সঞ্চালিত একটি সমতল তড়িৎচৌম্বক তরঙ্গে তড়িৎক্ষেত্রের বিস্তার E₀ = 60 V/m হলে কম্পমান চৌম্বক ক্ষেত্রের বিস্তার B₀ কত?',
        "opts": {'en': ['2.0 × 10⁻⁷ T', '1.8 × 10¹⁰ T', '5.0 × 10⁻⁷ T', '6.0 × 10⁻⁸ T'], 'bn': ['2.0 × 10⁻⁷ T', '1.8 × 10¹⁰ T', '5.0 × 10⁻⁷ T', '6.0 × 10⁻⁸ T']},
        "correct": 0,
        "expl_en": 'For an electromagnetic wave in vacuum: c = E₀ / B₀ => B₀ = E₀ / c = 60 / (3 × 10⁸ m/s) = 2.0 × 10⁻⁷ T.',
        "expl_bn": 'তড়িৎচৌম্বক তরঙ্গের ক্ষেত্রে B₀ = E₀ / c = ৬০ / (৩ × ১০⁸) = ২.০ × ১০⁻⁷ T।',
    },
    {
        "id": 'PHY-040',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": "Ray Optics & Lens Maker's Formula",
        "difficulty": 'Medium',
        "en": 'A convex lens of focal length 20 cm in air (refractive index μ<sub>glass</sub> = 1.5) is immersed in water (μ<sub>water</sub> = 4/3). Its focal length in water becomes:',
        "bn": 'বায়ুতে ২০ সেমি ফোকাস দৈর্ঘ্যের একটি উত্তল কাচ লেন্সকে (μ<sub>glass</sub> = ১.৫) জলে (μ<sub>water</sub> = ৪/৩) নিমজ্জিত করা হলো। জলে লেন্সটির ফোকাস দৈর্ঘ্য কত হবে?',
        "opts": {'en': ['80 cm', '40 cm', '60 cm', '100 cm'], 'bn': ['80 cm', '40 cm', '60 cm', '100 cm']},
        "correct": 0,
        "expl_en": "Lens maker's formula: 1/f = (μ<sub>rel</sub> - 1)(1/R₁ - 1/R₂). In air: 1/20 = (1.5 - 1) K = 0.5 K => K = 0.1. In water: 1/f<sub>w</sub> = (1.5 / (4/3) - 1) K = (9/8 - 1) K = (1/8)(0.1) = 1/80 => f<sub>w</sub> = 80 cm.",
        "expl_bn": 'লেন্স নির্মাতার সূত্রানুসারে f<sub>w</sub> / f<sub>a</sub> = (μ<sub>g</sub> - ১) / (μ<sub>g</sub>/μ<sub>w</sub> - ১) = (০.৫) / (৯/৮ - ১) = ০.৫ / (১/৮) = ৪। f<sub>w</sub> = ৪ × ২০ = ৮০ সেমি।',
    },
    {
        "id": 'PHY-041',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": "Wave Optics & Young's Double Slit Experiment",
        "difficulty": 'Easy',
        "en": "In Young's double slit experiment, if the distance between the two slits is halved and the distance between the slit screen is doubled, the fringe width will:",
        "bn": 'ইয়াং-এর দ্বি-রেখাছিদ্র পরীক্ষায় রেখাছিদ্রদ্বয়ের মধ্যবর্তী দূরত্ব অর্ধেক এবং পর্দা থেকে দূরত্ব দ্বিগুণ করা হলে ঝালর প্রস্থের কী পরিবর্তন ঘটবে?',
        "opts": {'en': ['Increase by a factor of 4', 'Increase by a factor of 2', 'Remain unchanged', 'Decrease by a factor of 2'], 'bn': ['৪ গুণ বৃদ্ধি পাবে', '২ গুণ বৃদ্ধি পাবে', 'অপরিবর্তিত থাকবে', 'অর্ধেক হয়ে যাবে']},
        "correct": 0,
        "expl_en": "Fringe width β = λ D / d. When D' = 2D and d' = d/2: β' = λ (2D) / (d/2) = 4 (λ D / d) = 4β. Fringe width quadruples.",
        "expl_bn": "ঝালর প্রস্থ β = λ D / d। D' = ২D এবং d' = d/২ হলে β' = ৪β। ঝালর প্রস্থ ৪ গুণ হবে।",
    },
    {
        "id": 'PHY-042',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Dual Nature of Matter & Photoelectric Effect',
        "difficulty": 'Medium',
        "en": 'The threshold wavelength for photoelectric emission in a metal is 500 nm. When light of wavelength 250 nm is incident on the metal, the maximum kinetic energy of the emitted photoelectrons is (take hc = 1240 eV·nm):',
        "bn": 'একটি ধাতুর আলোক-তড়িৎ নিঃসরণের প্রারম্ভ তরঙ্গদৈর্ঘ্য ৫০০ nm। ধাতুপাতে ২৫০ nm তরঙ্গদৈর্ঘ্যের আলো আপতিত হলে নির্গত ইলেকট্রনের সর্বোচ্চ গতিশক্তি কত? (hc = 1240 eV·nm):',
        "opts": {'en': ['2.48 eV', '4.96 eV', '1.24 eV', '3.72 eV'], 'bn': ['2.48 eV', '4.96 eV', '1.24 eV', '3.72 eV']},
        "correct": 0,
        "expl_en": 'Work function Φ = hc / λ₀ = 1240 / 500 = 2.48 eV. Incident photon energy E = hc / λ = 1240 / 250 = 4.96 eV. Maximum kinetic energy K<sub>max</sub> = E - Φ = 4.96 - 2.48 = 2.48 eV.',
        "expl_bn": 'কার্য-অপেক্ষক Φ = ১২৪০/৫০০ = ২.৪৮ eV। আপতিত ফোটন শক্তি E = ১২৪০/২৫০ = ৪.৯৬ eV। সর্বোচ্চ গতিশক্তি K<sub>max</sub> = ৪.৯৬ - ২.৪৮ = ২.৪৮ eV।',
    },
    {
        "id": 'PHY-043',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Atoms & Bohr Model',
        "difficulty": 'Easy',
        "en": 'In a hydrogen atom, the ratio of the radius of the third Bohr orbit (n = 3) to the radius of the first Bohr orbit (n = 1) is:',
        "bn": 'হাইড্রোজেন পরমাণুর ক্ষেত্রে তৃতীয় বোর কক্ষপথের (n = 3) ব্যাসার্ধ ও প্রথম কক্ষপথের (n = 1) ব্যাসার্ধের অনুপাত কত?',
        "opts": {'en': ['9 : 1', '3 : 1', '27 : 1', '1 : 9'], 'bn': ['9 : 1', '3 : 1', '27 : 1', '1 : 9']},
        "correct": 0,
        "expl_en": "According to Bohr's model, the radius of the nth orbit is r<sub>n</sub> = r₀ × n² / Z. For hydrogen Z = 1, so r₃ / r₁ = 3² / 1² = 9/1 = 9 : 1.",
        "expl_bn": 'বোর তত্ত্ব অনুসারে r<sub>n</sub> ∝ n²। তাই তৃতীয় ও প্রথম কক্ষপথের ব্যাসার্ধের অনুপাত = ৩² / ১² = ৯ : ১।',
    },
    {
        "id": 'PHY-044',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Nuclei & Radioactive Decay',
        "difficulty": 'Medium',
        "en": 'The half-life of a radioactive isotope is 20 days. If the initial activity of the sample is 8000 disintegrations per second, its activity after 60 days will be:',
        "bn": 'একটি তেজস্ক্রিয় আইসোটোপের অর্ধায়ু ২০ দিন। প্রাথমিক তেজস্ক্রিয় সক্রিয়তা ৮০০০ disintegration/s হলে ৬০ দিন পর সক্রিয়তা কত হবে?',
        "opts": {'en': ['1000 dps', '2000 dps', '500 dps', '250 dps'], 'bn': ['1000 dps', '2000 dps', '500 dps', '250 dps']},
        "correct": 0,
        "expl_en": 'Number of half-lives n = t / T<sub>half</sub> = 60 / 20 = 3. Activity A = A₀ (1/2)<sup>n</sup> = 8000 × (1/2)³ = 8000 / 8 = 1000 dps.',
        "expl_bn": 'অর্ধায়ুর সংখ্যা n = ৬০/২০ = ৩। সক্রিয়তা A = A₀ × (১/২)³ = ৮০০০ / ৮ = ১০০০ dps।',
    },
    {
        "id": 'PHY-045',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Semiconductor Electronics & Logic Gates',
        "difficulty": 'Easy',
        "en": 'Which of the following logic gates produces an output of logic 0 ONLY when both of its inputs are logic 1?',
        "bn": 'নিচের কোন লজিক গেটের ক্ষেত্রে কেবল তখনই আউটপুট ০ হয় যখন এর দুটি ইনপুটই ১ হয়?',
        "opts": {'en': ['NAND gate', 'NOR gate', 'AND gate', 'XOR gate'], 'bn': ['NAND গেট', 'NOR গেট', 'AND গেট', 'XOR গেট']},
        "correct": 0,
        "expl_en": 'A NAND gate is the negation of an AND gate. When both inputs A = 1 and B = 1, A·B = 1, so the output Y = NOT(A·B) = 0. For any other combination, the output is 1.',
        "expl_bn": 'NAND গেট হলো AND গেটের বিপরীত। দুটি ইনপুট ১ হলে AND গেটের আউটপুট ১ হয়, ফলে NAND গেট ০ আউটপুট প্রদান করে।',
    },
    {
        "id": 'PHY-046',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Circular Motion & Banking of Roads',
        "difficulty": 'Medium',
        "en": 'A curved road of radius 100 m is banked for an optimum design speed of 72 km/h. The optimum angle of banking θ of the road is (take g = 10 m/s²):',
        "bn": '১০০ মিটার ব্যাসার্ধের একটি বাঁকানো সড়ককে ৭২ কিমি/ঘণ্টা সর্বোচ্চ নিরাপদ দ্রুতির জন্য ঢালু (banked) করা হয়েছে। সড়কের ব্যাংকিং কোণ θ কত? (g = 10 m/s²):',
        "opts": {'en': ['tan⁻¹(0.4)', 'tan⁻¹(0.2)', 'tan⁻¹(0.5)', 'tan⁻¹(0.8)'], 'bn': ['tan⁻¹(0.4)', 'tan⁻¹(0.2)', 'tan⁻¹(0.5)', 'tan⁻¹(0.8)']},
        "correct": 0,
        "expl_en": 'Optimum speed on a banked road: v = √(r g tan θ). v = 72 km/h = 20 m/s. tan θ = v² / (r g) = (20)² / (100 × 10) = 400 / 1000 = 0.4 => θ = tan⁻¹(0.4).',
        "expl_bn": 'ব্যাংকিং কোণের সূত্র: tan θ = v² / (rg)। বেগ v = ২০ m/s হলে: tan θ = ৪০০ / (১০০ × ১০) = ০.৪ => θ = tan⁻¹(০.৪)।',
    },
    {
        "id": 'PHY-047',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'System of Particles & Center of Mass',
        "difficulty": 'Medium',
        "en": 'Two particles of masses 1 kg and 3 kg are located at positions (2, 4) and (6, 8) respectively. The coordinates of the center of mass of the two-particle system are:',
        "bn": '১ কেজি ও ৩ কেজি ভরের দুটি কণা যথাক্রমে (২, ৪) এবং (৬, ৮) স্থানাঙ্কে অবস্থিত। কণা দুটির ভরকেন্দ্রের স্থানাঙ্ক কত?',
        "opts": {'en': ['(5, 7)', '(4, 6)', '(3, 5)', '(4.5, 6.5)'], 'bn': ['(5, 7)', '(4, 6)', '(3, 5)', '(4.5, 6.5)']},
        "correct": 0,
        "expl_en": 'x<sub>cm</sub> = (m₁ x₁ + m₂ x₂) / (m₁ + m₂) = (1×2 + 3×6)/(1 + 3) = (2 + 18)/4 = 20/4 = 5. y<sub>cm</sub> = (1×4 + 3×8)/4 = (4 + 24)/4 = 28/4 = 7. Center of mass = (5, 7).',
        "expl_bn": 'ভরকেন্দ্রের স্থানাঙ্ক x<sub>cm</sub> = (১×২ + ৩×৬) / ৪ = ৫। y<sub>cm</sub> = (১×৪ + ৩×৮) / ৪ = ৭। সুতরাং ভরকেন্দ্র = (৫, ৭)।',
    },
    {
        "id": 'PHY-048',
        "exam": 'JEE, WBJEE, BITSAT, NEET',
        "subject": 'Physics',
        "topic": 'Rotational Motion & Angular Momentum',
        "difficulty": 'Medium',
        "en": 'A horizontal circular disc of mass M and radius R rotates about its vertical central axis with angular velocity ω₀. A point mass m is gently placed on the rim of the disc. The new angular velocity of the system is:',
        "bn": 'M ভর এবং R ব্যাসার্ধের একটি অনুভূমিক বৃত্তাকার চাকতি তার উল্লম্ব কেন্দ্রীয় অক্ষের সাপেক্ষে ω₀ কৌণিক বেগে ঘুরছে। চাকতির কিনারায় আলতো করে m ভরের একটি কণা রাখা হলো। সংস্থাটির নতুন কৌণিক বেগ কত?',
        "opts": {'en': ['(M / (M + 2m)) ω₀', '(M / (M + m)) ω₀', '(2M / (M + 2m)) ω₀', '(M / 2m) ω₀'], 'bn': ['(M / (M + 2m)) ω₀', '(M / (M + m)) ω₀', '(2M / (M + 2m)) ω₀', '(M / 2m) ω₀']},
        "correct": 0,
        "expl_en": 'By conservation of angular momentum: I₁ ω₀ = I₂ ω. I₁ = 0.5 M R². I₂ = 0.5 M R² + m R² = (0.5 M + m) R². (0.5 M R²) ω₀ = (0.5 M + m) R² ω => ω = (0.5 M / (0.5 M + m)) ω₀ = (M / (M + 2m)) ω₀.',
        "expl_bn": 'কৌণিক ভরবেগ সংরক্ষণ নীতি অনুসারে: I₁ ω₀ = I₂ ω। চাকতির জড়তার ভ্রামক I₁ = ১/২ MR²। কণা বসানোর পর I₂ = ১/২ MR² + mR²। সুতরাং ω = (M / (M + 2m)) ω₀।',
    },
    {
        "id": 'PHY-049',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Gravitation & Potential Energy',
        "difficulty": 'Medium',
        "en": "The work done in lifting a body of mass m from the Earth's surface to a height equal to the radius of the Earth (h = R) is (where g is acceleration on Earth's surface):",
        "bn": 'm ভরের একটি বস্তুকে ভূপৃষ্ঠ থেকে পৃথিবীর ব্যাসার্ধের সমান উচ্চতায় (h = R) তুলতে কৃতকার্য কত? (g হলো ভূপৃষ্ঠে অভিকর্ষজ ত্বরণ):',
        "opts": {'en': ['0.5 m g R', 'm g R', '2 m g R', '0.25 m g R'], 'bn': ['0.5 m g R', 'm g R', '2 m g R', '0.25 m g R']},
        "correct": 0,
        "expl_en": 'Work done W = ΔU = U<sub>final</sub> - U<sub>initial</sub> = -GMm/(R + h) - (-GMm/R). For h = R: W = -GMm/2R + GMm/R = GMm / 2R = 0.5 (GM/R²) m R = 0.5 m g R.',
        "expl_bn": 'কৃতকার্য W = ΔU = -GMm/2R - (-GMm/R) = GMm/2R = ১/২ mgR।',
    },
    {
        "id": 'PHY-050',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Mechanical Properties of Fluids & Terminal Velocity',
        "difficulty": 'Easy',
        "en": 'A small spherical lead ball of radius r falls through a viscous liquid with terminal velocity v. Another lead ball of radius 2r falling through the same liquid will achieve a terminal velocity of:',
        "bn": 'সান্দ্র তরলের মধ্য দিয়ে অবাধে পতনশীল r ব্যাসার্ধের একটি গোলকের প্রান্তিক বেগ v। একই তরলে 2r ব্যাসার্ধের অপর একটি গোলকের প্রান্তিক বেগ কত হবে?',
        "opts": {'en': ['4v', '2v', '8v', '16v'], 'bn': ['4v', '2v', '8v', '16v']},
        "correct": 0,
        "expl_en": "Terminal velocity by Stokes' law: v<sub>t</sub> = (2/9) r² (ρ - σ) g / η => v<sub>t</sub> ∝ r². If radius is doubled (r' = 2r), terminal velocity increases by 2² = 4 times (4v).",
        "expl_bn": 'স্টোকসের সূত্রানুসারে প্রান্তিক বেগ v<sub>t</sub> ∝ r²। ব্যাসার্ধ দ্বিগুণ হলে প্রান্তিক বেগ ২² = ৪ গুণ (4v) হবে।',
    },
    {
        "id": 'PHY-051',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Surface Tension & Capillary Action',
        "difficulty": 'Medium',
        "en": 'A capillary tube of radius r is immersed in water and water rises to a height h. If the tube is replaced by another capillary tube of radius r/2, the height to which water will rise is:',
        "bn": 'r ব্যাসার্ধের একটি কৈশিক নলকে জলে নিমজ্জিত করলে জল h উচ্চতায় ওঠে। নলটিকে r/২ ব্যাসার্ধের অপর একটি নল দ্বারা প্রতিস্থাপিত করলে জলের আরোহণ উচ্চতা কত হবে?',
        "opts": {'en': ['2h', 'h/2', '4h', 'h'], 'bn': ['2h', 'h/2', '4h', 'h']},
        "correct": 0,
        "expl_en": "By Jurin's Law: h = (2 T cos θ) / (r ρ g) => h ∝ 1/r. If radius is halved (r' = r/2), height doubles to 2h.",
        "expl_bn": 'জুরিনের সূত্রানুসারে h ∝ ১/r। ব্যাসার্ধ অর্ধেক করা হলে জলের উচ্চতা দ্বিগুণ (2h) হবে।',
    },
    {
        "id": 'PHY-052',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Thermal Expansion & Bimetallic Strips',
        "difficulty": 'Easy',
        "en": 'A bimetallic strip consists of brass (α<sub>brass</sub> = 19 × 10⁻⁶ K⁻¹) and iron (α<sub>iron</sub> = 12 × 10⁻⁶ K⁻¹) welded together. When the temperature of the strip is increased, it bends such that:',
        "bn": 'পিতল (α<sub>brass</sub> = 19 × 10⁻⁶ K⁻¹) এবং লোহা (α<sub>iron</sub> = 12 × 10⁻⁶ K⁻¹) দ্বারা নির্মিত একটি দ্বিধাতব পাত উত্তপ্ত করা হলে পাতটি এমনভাবে বাঁকবে যাতে:',
        "opts": {'en': ['Brass is on the convex (outer) side and iron is on the concave (inner) side', 'Iron is on the convex side and brass is on the concave side', 'The strip expands linearly without bending', 'The strip twists in a spiral'], 'bn': ['পিতল উত্তল (বাইরের) পৃষ্ঠে এবং লোহা অবতল (ভেতরের) পৃষ্ঠে থাকবে', 'লোহা উত্তল পৃষ্ঠে এবং পিতল অবতল পৃষ্ঠে থাকবে', 'পাতটি না বেঁকে রৈখিকভাবে প্রসারিত হবে', 'পাতটি সর্পিল আকারে মোচড় খাবে']},
        "correct": 0,
        "expl_en": 'Since brass has a higher coefficient of linear expansion (α<sub>brass</sub> > α<sub>iron</sub>), it expands more upon heating. To accommodate greater length, brass forms the outer convex curve, while iron forms the inner concave curve.',
        "expl_bn": 'পিতলের দৈর্ঘ্য প্রসারণ গুণাঙ্ক লোহার চেয়ে বেশি হওয়ায় উত্তাপে পিতল বেশি প্রসারিত হয় এবং বাইরের উত্তল পৃষ্ঠে অবস্থান নেয়।',
    },
    {
        "id": 'PHY-053',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Thermodynamics & Heat Engines',
        "difficulty": 'Medium',
        "en": 'A Carnot engine has an efficiency of 40% when its sink is at 27 °C. To increase its efficiency to 50%, the temperature of the heat source must be increased by:',
        "bn": 'একটি কার্নো ইঞ্জিনের গ্রাহকের তাপমাত্রা ২৭ °C হলে এর কর্মদক্ষতা ৪০%। কর্মদক্ষতা ৫০% এ উন্নীত করতে উৎসের তাপমাত্রা কত বৃদ্ধি করতে হবে?',
        "opts": {'en': ['100 K', '50 K', '80 K', '120 K'], 'bn': ['100 K', '50 K', '80 K', '120 K']},
        "correct": 0,
        "expl_en": 'T<sub>sink</sub> = 27 + 273 = 300 K. η = 1 - T<sub>sink</sub> / T<sub>source</sub>. For 40%: 0.40 = 1 - 300/T₁ => 300/T₁ = 0.60 => T₁ = 500 K. For 50%: 0.50 = 1 - 300/T₂ => 300/T₂ = 0.50 => T₂ = 600 K. Increase in source temperature ΔT = 600 - 500 = 100 K.',
        "expl_bn": 'গ্রাহকের তাপমাত্রা T<sub>sink</sub> = ৩০০ K। η = ১ - T<sub>sink</sub>/T<sub>source</sub>। ৪০% দক্ষতার জন্য: T₁ = ৩০০/০.৬ = ৫০০ K। ৫০% দক্ষতার জন্য: T₂ = ৩০০/০.৫ = ৬০০ K। তাপমাত্রা বৃদ্ধি = ৬০০ - ৫০০ = ১০০ K।',
    },
    {
        "id": 'PHY-054',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Waves & Organ Pipes',
        "difficulty": 'Medium',
        "en": 'An organ pipe closed at one end has fundamental frequency 250 Hz. The frequency of its second overtone (fifth harmonic) is:',
        "bn": 'একমুখ বন্ধ একটি অর্গান নলের মূল সুরের কম্পাঙ্ক ২৫০ Hz। এর দ্বিতীয় উপসূরের (পঞ্চম সমমেল) কম্পাঙ্ক কত?',
        "opts": {'en': ['1250 Hz', '750 Hz', '500 Hz', '1000 Hz'], 'bn': ['1250 Hz', '750 Hz', '500 Hz', '1000 Hz']},
        "correct": 0,
        "expl_en": 'In a closed organ pipe, only odd harmonics exist: f<sub>n</sub> = (2n + 1) f₁, where n = 0 is fundamental, n = 1 is 1st overtone (3f₁), and n = 2 is 2nd overtone (5f₁). Frequency = 5 × 250 = 1250 Hz.',
        "expl_bn": 'একমুখ বন্ধ নলে কেবল বিজোড় সমমেল উপস্থিত থাকে। দ্বিতীয় উপসূর (পঞ্চম সমমেল) = ৫ × মূল কম্পাঙ্ক = ৫ × ২৫০ = ১২৫০ Hz।',
    },
    {
        "id": 'PHY-055',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Electrostatics & Electric Dipole',
        "difficulty": 'Medium',
        "en": 'An electric dipole of dipole moment p is placed in a uniform electric field E at an angle θ. The torque acting on the dipole and the potential energy stored in it are respectively:',
        "bn": 'p ভ্রামকের একটি তড়িৎ দ্বিমেরু E সুষম তড়িৎক্ষেত্রে θ কোণে অবস্থিত। দ্বিমেরুটির ওপর ক্রিয়াশীল টর্ক এবং সঞ্চিত স্থিতিশক্তি যথাক্রমে:',
        "opts": {'en': ['p E sin θ and -p E cos θ', 'p E cos θ and -p E sin θ', 'p E sin θ and +p E cos θ', '0 and -p E cos θ'], 'bn': ['p E sin θ এবং -p E cos θ', 'p E cos θ এবং -p E sin θ', 'p E sin θ এবং +p E cos θ', '0 এবং -p E cos θ']},
        "correct": 0,
        "expl_en": 'Torque on dipole: τ = p × E => magnitude = p E sin θ. Electrostatic potential energy: U = -p · E = -p E cos θ.',
        "expl_bn": 'দ্বিমেরুর ওপর টর্ক τ = p E sin θ এবং স্থিতিশক্তি U = -p E cos θ।',
    },
    {
        "id": 'PHY-056',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Current Electricity & Temperature Dependence',
        "difficulty": 'Easy',
        "en": 'The resistance of a platinum wire is 5.0 Ω at 0 °C and 6.0 Ω at 50 °C. The temperature coefficient of resistance (α) of platinum is:',
        "bn": '০ °C তাপমাত্রায় একটি প্ল্যাটিনাম তারের রোধ ৫.০ Ω এবং ৫০ °C তাপমাত্রায় রোধ ৬.০ Ω। প্ল্যাটিনামের রোধের উষ্ণতা গুণাঙ্ক (α) কত?',
        "opts": {'en': ['0.004 °C⁻¹', '0.002 °C⁻¹', '0.005 °C⁻¹', '0.008 °C⁻¹'], 'bn': ['0.004 °C⁻¹', '0.002 °C⁻¹', '0.005 °C⁻¹', '0.008 °C⁻¹']},
        "correct": 0,
        "expl_en": 'R<sub>t</sub> = R₀ (1 + α ΔT) => α = (R<sub>t</sub> - R₀) / (R₀ ΔT) = (6.0 - 5.0) / (5.0 × 50) = 1.0 / 250 = 0.004 °C⁻¹.',
        "expl_bn": 'রোধের উষ্ণতা গুণাঙ্ক α = (R<sub>t</sub> - R₀) / (R₀ ΔT) = (৬ - ৫) / (৫ × ৫০) = ১ / ২৫০ = ০.০০৪ °C⁻¹।',
    },
    {
        "id": 'PHY-057',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Current Electricity & Galvanometer Conversion',
        "difficulty": 'Medium',
        "en": 'A galvanometer of resistance 50 Ω gives full-scale deflection for a current of 2 mA. To convert it into a voltmeter of range 0 to 10 V, the required series resistance is:',
        "bn": '৫০ Ω রোধের একটি গ্যালভানোমিটার ২ mA প্রবাহে পূর্ণ স্কেল বিক্ষেপ দেয়। এটিকে ০ থেকে ১০ V পাল্লার ভোল্টমিটারে রূপান্তরিত করতে শ্রেণি সমবায়ে কত রোধ যুক্ত করতে হবে?',
        "opts": {'en': ['4950 Ω', '5000 Ω', '4500 Ω', '5050 Ω'], 'bn': ['4950 Ω', '5000 Ω', '4500 Ω', '5050 Ω']},
        "correct": 0,
        "expl_en": 'V = I<sub>g</sub> (G + R<sub>s</sub>) => R<sub>s</sub> = V / I<sub>g</sub> - G = 10 / (2 × 10⁻³) - 50 = 5000 - 50 = 4950 Ω.',
        "expl_bn": 'শ্রেণি রোধ R<sub>s</sub> = V / I<sub>g</sub> - G = ১০ / (২ × ১০⁻³) - ৫০ = ৫০০০ - ৫০ = ৪৯৫০ Ω।',
    },
    {
        "id": 'PHY-058',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Magnetic Field of a Solenoid',
        "difficulty": 'Easy',
        "en": 'A long solenoid of length 1 m has 1000 turns of wire and carries a current of 2 A. The magnetic field at its interior center is (μ₀ = 4π × 10⁻⁷ T·m/A):',
        "bn": '১ মিটার দীর্ঘ একটি সলিনয়েডে ১০০০ পাকের তার আছে এবং এতে ২ A প্রবাহ চলছে। এর অভ্যন্তরে কেন্দ্রে চৌম্বক ক্ষেত্র কত? (μ₀ = ৪π × ১০⁻⁷ T·m/A):',
        "opts": {'en': ['2.51 × 10⁻³ T (8π × 10⁻⁴ T)', '1.26 × 10⁻³ T', '5.02 × 10⁻³ T', '6.28 × 10⁻⁴ T'], 'bn': ['2.51 × 10⁻³ T (8π × 10⁻⁴ T)', '1.26 × 10⁻³ T', '5.02 × 10⁻³ T', '6.28 × 10⁻⁴ T']},
        "correct": 0,
        "expl_en": 'B = μ₀ n I = μ₀ (N / L) I = (4π × 10⁻⁷)(1000 / 1)(2) = 8π × 10⁻⁴ T ≈ 2.51 × 10⁻³ T.',
        "expl_bn": 'সলিনয়েডের চৌম্বক ক্ষেত্র B = μ₀ n I = (৪π × ১০⁻⁷)(১০০০)(২) = ৮π × ১০⁻⁴ T ≈ ২.৫১ × ১০⁻³ T।',
    },
    {
        "id": 'PHY-059',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Cyclotron & Charged Particle in Magnetic Field',
        "difficulty": 'Medium',
        "en": 'A proton (mass m, charge +e) enters perpendicularly into a uniform magnetic field B with kinetic energy K. The radius of its circular orbit in the field is:',
        "bn": 'm ভর এবং +e আধানের একটি প্রোটন K গতিশক্তি নিয়ে B সুষম চৌম্বক ক্ষেত্রে লম্বভাবে প্রবেশ করে। চৌম্বক ক্ষেত্রে প্রোটনটির বৃত্তাকার কক্ষপথের ব্যাসার্ধ কত?',
        "opts": {'en': ['√(2 m K) / (e B)', '2 m K / (e B)', '√(m K) / (2 e B)', 'm K / (e B)'], 'bn': ['√(2 m K) / (e B)', '2 m K / (e B)', '√(m K) / (2 e B)', 'm K / (e B)']},
        "correct": 0,
        "expl_en": 'Magnetic force provides centripetal force: q v B = m v² / r => r = m v / (q B) = p / (q B). Since momentum p = √(2 m K) and q = e: r = √(2 m K) / (e B).',
        "expl_bn": 'কক্ষপথের ব্যাসার্ধ r = p / (q B)। ভরবেগ p = √(2 m K) এবং q = e হলে r = √(2 m K) / (e B)।',
    },
    {
        "id": 'PHY-060',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Electromagnetic Induction & Self-Inductance',
        "difficulty": 'Easy',
        "en": 'An inductor of self-inductance L = 2 H carries a steady current of 3 A. The magnetic potential energy stored in the inductor is:',
        "bn": '২ H স্বাবেশাঙ্কের একটি আবেশকে ৩ A স্থির প্রবাহ চলছে। আবেশকে সঞ্চিত চৌম্বক স্থিতিশক্তি কত?',
        "opts": {'en': ['9 J', '6 J', '18 J', '3 J'], 'bn': ['9 J', '6 J', '18 J', '3 J']},
        "correct": 0,
        "expl_en": 'Magnetic energy stored in an inductor: U = 0.5 L I² = 0.5 × 2 × 3² = 9 J.',
        "expl_bn": 'আবেশকে সঞ্চিত চৌম্বক শক্তি U = ১/২ L I² = ১/২ × ২ × ৩² = ৯ জুল।',
    },
    {
        "id": 'PHY-061',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Alternating Current & Power Factor',
        "difficulty": 'Medium',
        "en": 'In a series AC circuit containing resistance R = 30 Ω and inductive reactance X<sub>L</sub> = 40 Ω, the power factor (cos φ) of the circuit is:',
        "bn": 'একটি শ্রেণি AC বর্তনীতে রোধ R = ৩০ Ω এবং আবেশীয় প্রতিঘাত X<sub>L</sub> = ৪০ Ω হলে বর্তনীটির ক্ষমতা গুণক (Power Factor) কত?',
        "opts": {'en': ['0.6', '0.8', '0.75', '1.0'], 'bn': ['0.6', '0.8', '0.75', '1.0']},
        "correct": 0,
        "expl_en": 'Impedance Z = √(R² + X<sub>L</sub>²) = √(30² + 40²) = √2500 = 50 Ω. Power factor cos φ = R / Z = 30 / 50 = 0.6.',
        "expl_bn": 'প্রতিবন্ধকতা Z = √(৩০² + ৪০²) = ৫০ Ω। ক্ষমতা গুণক cos φ = R / Z = ৩০ / ৫০ = ০.৬।',
    },
    {
        "id": 'PHY-062',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Electromagnetic Waves & Displacement Current',
        "difficulty": 'Easy',
        "en": "According to Maxwell's correction to Ampere's circuital law, the displacement current I<sub>d</sub> between the plates of a charging capacitor is equal to:",
        "bn": 'অ্যাম্পিয়ারের বর্তনী সূত্রে ম্যাক্সওয়েলের সংশোধনের পর, একটি আহিত ধারকের পাতদ্বয়ের মধ্যবর্তী সরণ প্রবাহ (Displacement current) I<sub>d</sub> এর মান কত?',
        "opts": {'en': ['ε₀ (dΦ<sub>E</sub> / dt)', 'μ₀ (dΦ<sub>E</sub> / dt)', '(1/ε₀) (dΦ<sub>E</sub> / dt)', 'ε₀ μ₀ (dΦ<sub>E</sub> / dt)'], 'bn': ['ε₀ (dΦ<sub>E</sub> / dt)', 'μ₀ (dΦ<sub>E</sub> / dt)', '(1/ε₀) (dΦ<sub>E</sub> / dt)', 'ε₀ μ₀ (dΦ<sub>E</sub> / dt)']},
        "correct": 0,
        "expl_en": 'Maxwell defined displacement current as I<sub>d</sub> = ε₀ (dΦ<sub>E</sub> / dt), where Φ<sub>E</sub> is the electric flux between the plates.',
        "expl_bn": 'ম্যাক্সওয়েলের তত্ত্বানুসারে সরণ প্রবাহ I<sub>d</sub> = ε₀ (dΦ<sub>E</sub> / dt), যেখানে Φ<sub>E</sub> হলো তড়িৎ ফ্লাক্স।',
    },
    {
        "id": 'PHY-063',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Ray Optics & Total Internal Reflection',
        "difficulty": 'Easy',
        "en": 'A ray of light traveling in glass (refractive index μ = 1.5) is incident on a glass-air boundary. The critical angle θ<sub>c</sub> for total internal reflection is:',
        "bn": 'কাচের (প্রতিসরাঙ্ক μ = ১.৫) মধ্য দিয়ে চলমান একটি আলোক রশ্মি কাচ-বায়ু তলে আপতিত হয়। অভ্যন্তরীণ পূর্ণ প্রতিফলনের সংকট কোণ θ<sub>c</sub> কত?',
        "opts": {'en': ['sin⁻¹(2/3) (≈ 41.8°)', 'sin⁻¹(1/3)', 'sin⁻¹(3/4)', '45°'], 'bn': ['sin⁻¹(2/3) (≈ 41.8°)', 'sin⁻¹(1/3)', 'sin⁻¹(3/4)', '45°']},
        "correct": 0,
        "expl_en": 'Critical angle θ<sub>c</sub> = sin⁻¹(1 / μ) = sin⁻¹(1 / 1.5) = sin⁻¹(2/3) ≈ 41.8°.',
        "expl_bn": 'সংকট কোণ θ<sub>c</sub> = sin⁻¹(১/μ) = sin⁻¹(১/১.৫) = sin⁻¹(২/৩) ≈ ৪১.৮°।',
    },
    {
        "id": 'PHY-064',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Optical Instruments & Compound Microscope',
        "difficulty": 'Medium',
        "en": 'In a compound microscope, the focal lengths of the objective and eyepiece are 1.0 cm and 5.0 cm respectively. If an object is placed 1.2 cm in front of the objective and the final image is formed at near point (D = 25 cm), the magnifying power is:',
        "bn": 'একটি যৌগিক অণুবীক্ষণ যন্ত্রে অভিনেত্র ও অভিলক্ষ্যের ফোকাস দৈর্ঘ্য যথাক্রমে ৫.০ সেমি এবং ১.০ সেমি। অভিলক্ষ্য থেকে ১.২ সেমি দূরে বস্তু রাখলে এবং স্পষ্ট দর্শনের ন্যূনতম দূরত্বে (D = ২৫ সেমি) চূড়ান্ত প্রতিবিম্ব গঠিত হলে বিবর্ধন ক্ষমতা কত?',
        "opts": {'en': ['30', '25', '36', '20'], 'bn': ['30', '25', '36', '20']},
        "correct": 0,
        "expl_en": 'For objective: 1/v<sub>o</sub> - 1/u<sub>o</sub> = 1/f<sub>o</sub> => 1/v<sub>o</sub> - 1/(-1.2) = 1/1.0 => 1/v<sub>o</sub> = 1 - 5/6 = 1/6 => v<sub>o</sub> = 6 cm. Linear magnification of objective m<sub>o</sub> = |v<sub>o</sub> / u<sub>o</sub>| = 6 / 1.2 = 5. Eyepiece magnification m<sub>e</sub> = 1 + D/f<sub>e</sub> = 1 + 25/5 = 6. Total magnifying power M = m<sub>o</sub> × m<sub>e</sub> = 5 × 6 = 30.',
        "expl_bn": 'অভিলক্ষ্যের বিবর্ধন m<sub>o</sub> = v<sub>o</sub> / u<sub>o</sub> = ৬/১.২ = ৫। অভিনেত্রের বিবর্ধন m<sub>e</sub> = ১ + D/f<sub>e</sub> = ১ + ২৫/৫ = ৬। মোট বিবর্ধন M = ৫ × ৬ = ৩০।',
    },
    {
        "id": 'PHY-065',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": "Wave Optics & Brewster's Law",
        "difficulty": 'Easy',
        "en": "When unpolarized light is incident on a transparent plate at Brewster's polarizing angle i<sub>p</sub> = 60°, the reflected ray is completely plane-polarized. The refractive index of the plate is:",
        "bn": 'ব্রুস্টারের কোণ i<sub>p</sub> = ৬০° তে একটি স্বচ্ছ মাধ্যমে অসমাবর্তিত আলো আপতিত হলে প্রতিফলিত রশ্মি সম্পূর্ণ সমাবর্তিত হয়। মাধ্যমটির প্রতিসরাঙ্ক কত?',
        "opts": {'en': ['√3 (≈ 1.732)', '1 / √3', '1.5', '1.33'], 'bn': ['√3 (≈ 1.732)', '1 / √3', '1.5', '1.33']},
        "correct": 0,
        "expl_en": "By Brewster's law: μ = tan(i<sub>p</sub>) = tan(60°) = √3 ≈ 1.732.",
        "expl_bn": 'ব্রুস্টারের সূত্রানুসারে প্রতিসরাঙ্ক μ = tan(i<sub>p</sub>) = tan(৬০°) = √৩ ≈ ১.৭৩২।',
    },
    {
        "id": 'PHY-066',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": "Wave Optics & Malus's Law",
        "difficulty": 'Medium',
        "en": 'Two polaroids are placed with their transmission axes aligned at an angle of 60° to each other. An unpolarized light beam of intensity I₀ is incident on the first polaroid. The intensity of light transmitted by the second polaroid is:',
        "bn": 'দুটি পোলারয়েড এমনভাবে রাখা আছে যাতে তাদের অক্ষদ্বয়ের মধ্যবর্তী কোণ ৬০°। I₀ তীব্রতার অসমাবর্তিত আলো প্রথম পোলারয়েডে আপতিত হলে দ্বিতীয় পোলারয়েড থেকে নির্গত আলোর তীব্রতা কত হবে?',
        "opts": {'en': ['I₀ / 8', 'I₀ / 4', 'I₀ / 2', '3 I₀ / 8'], 'bn': ['I₀ / 8', 'I₀ / 4', 'I₀ / 2', '3 I₀ / 8']},
        "correct": 0,
        "expl_en": "After first polaroid, unpolarized light intensity becomes I₁ = I₀ / 2. By Malus's law, after second polaroid: I₂ = I₁ cos²(60°) = (I₀ / 2) × (1/2)² = (I₀ / 2) × (1/4) = I₀ / 8.",
        "expl_bn": 'প্রথম পোলারয়েড পার হওয়ার পর তীব্রতা I₁ = I₀ / ২। মালুসের সূত্রানুসারে দ্বিতীয় পোলারয়েডের পর: I₂ = (I₀ / ২) cos²(৬০°) = I₀ / ৮।',
    },
    {
        "id": 'PHY-067',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Dual Nature & de Broglie Wavelength',
        "difficulty": 'Easy',
        "en": 'An electron is accelerated from rest through an electric potential difference of 100 V. The de Broglie wavelength associated with the electron is approximately:',
        "bn": '১০০ V বিভব পার্থক্যের মধ্য দিয়ে স্থির অবস্থা থেকে একটি ইলেকট্রনকে ত্বরান্বিত করা হলো। ইলেকট্রনের দ্য ব্রয় তরঙ্গদৈর্ঘ্য আনুমানিক কত?',
        "opts": {'en': ['0.123 nm (1.23 Å)', '0.245 nm', '0.061 nm', '1.23 nm'], 'bn': ['0.123 nm (1.23 Å)', '0.245 nm', '0.061 nm', '1.23 nm']},
        "correct": 0,
        "expl_en": 'de Broglie wavelength of an accelerated electron: λ = 1.227 / √V nm = 1.227 / √100 = 1.227 / 10 = 0.1227 nm ≈ 0.123 nm = 1.23 Å.',
        "expl_bn": 'ইলেকট্রনের দ্য ব্রয় তরঙ্গদৈর্ঘ্য λ = ১.২২৭ / √V nm = ১.২২৭ / ১০ ≈ ০.১২৩ nm = ১.২৩ Å।',
    },
    {
        "id": 'PHY-068',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Atoms & Hydrogen Spectral Series',
        "difficulty": 'Medium',
        "en": 'The ratio of the longest wavelength in the Lyman series to the longest wavelength in the Balmer series of hydrogen atom spectrum is:',
        "bn": 'হাইড্রোজেন পরমাণুর বর্ণালিতে লাইম্যান শ্রেণির দীর্ঘতম তরঙ্গদৈর্ঘ্য এবং বামার শ্রেণির দীর্ঘতম তরঙ্গদৈর্ঘ্যের অনুপাত কত?',
        "opts": {'en': ['5 / 27', '27 / 5', '3 / 4', '4 / 9'], 'bn': ['5 / 27', '27 / 5', '3 / 4', '4 / 9']},
        "correct": 0,
        "expl_en": '1/λ = R (1/n₁² - 1/n₂²). For Lyman longest: n₁=1, n₂=2 => 1/λ<sub>L</sub> = R(1 - 1/4) = 3R/4 => λ<sub>L</sub> = 4/(3R). For Balmer longest: n₁=2, n₂=3 => 1/λ<sub>B</sub> = R(1/4 - 1/9) = 5R/36 => λ<sub>B</sub> = 36/(5R). Ratio λ<sub>L</sub> / λ<sub>B</sub> = (4/3R) / (36/5R) = (4/3) × (5/36) = 20 / 108 = 5 / 27.',
        "expl_bn": 'লাইম্যানের দীর্ঘতম তরঙ্গদৈর্ঘ্য λ<sub>L</sub> = ৪/(৩R)। বামারের দীর্ঘতম তরঙ্গদৈর্ঘ্য λ<sub>B</sub> = ৩৬/(৫R)। অনুপাত = (৪/৩) × (৫/৩৬) = ৫/২৭।',
    },
    {
        "id": 'PHY-069',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Nuclei & Mass Defect & Binding Energy',
        "difficulty": 'Medium',
        "en": 'If the mass defect in a nuclear reaction is Δm = 0.02 amu, the energy released in the reaction is approximately (1 amu = 931.5 MeV):',
        "bn": 'একটি নিউক্লীয় বিক্রিয়ায় ভর ত্রুটি Δm = ০.০২ amu হলে বিক্রিয়ায় নির্গত শক্তি প্রায় কত? (১ amu = ৯৩১.৫ MeV):',
        "opts": {'en': ['18.63 MeV', '9.31 MeV', '37.26 MeV', '4.65 MeV'], 'bn': ['18.63 MeV', '9.31 MeV', '37.26 MeV', '4.65 MeV']},
        "correct": 0,
        "expl_en": 'Energy released Q = Δm × 931.5 MeV = 0.02 × 931.5 = 18.63 MeV.',
        "expl_bn": 'নিউক্লীয় বিক্রিয়ায় নির্গত শক্তি Q = ০.০২ × ৯৩১.৫ MeV = ১৮.৬৩ MeV।',
    },
    {
        "id": 'PHY-070',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Semiconductor Devices & Zener Diode',
        "difficulty": 'Easy',
        "en": 'A Zener diode is heavily doped and primarily used in electronic circuits as a:',
        "bn": 'উচ্চ ডোপিংযুক্ত জেনার ডায়োড ইলেকট্রনিক বর্তনীতে প্রধানত কী হিসেবে ব্যবহৃত হয়?',
        "opts": {'en': ['Voltage regulator operated in reverse breakdown region', 'Current amplifier in forward bias', 'Oscillator generating RF frequencies', 'Full-wave rectifier'], 'bn': ['বিপরীত বায়াসে ভোল্টেজ নিয়ন্ত্রক (Voltage regulator)', 'সম্মুখ বায়াসে প্রবাহ বিবর্ধক', 'উচ্চ কম্পাঙ্কের স্পন্দক (Oscillator)', 'পূর্ণ তরঙ্গ একমুখীকারী']},
        "correct": 0,
        "expl_en": 'A Zener diode is specifically designed to operate safely in its reverse breakdown region, maintaining an essentially constant voltage across its terminals despite fluctuations in supply voltage or load current, making it an ideal voltage regulator.',
        "expl_bn": 'জেনার ডায়োড বিপরীত বায়াসে ব্রেকডাউন অঞ্চলে ভোল্টেজ স্থির রাখতে সক্ষম, তাই একে ভোল্টেজ নিয়ন্ত্রক (Voltage Regulator) হিসেবে ব্যবহার করা হয়।',
    },
    {
        "id": 'PHY-071',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Semiconductors & p-n Junction Diode',
        "difficulty": 'Medium',
        "en": 'In a full-wave rectifier circuit supplied by an AC mains frequency of 50 Hz, the fundamental frequency of the output ripple is:',
        "bn": '৫০ Hz কম্পাঙ্কের পরিবর্তী বিদ্যুৎ দ্বারা চালিত একটি পূর্ণ তরঙ্গ একমুখীকারী (full-wave rectifier) বর্তনীর আউটপুট রিপলের মূল কম্পাঙ্ক কত?',
        "opts": {'en': ['100 Hz', '50 Hz', '25 Hz', '200 Hz'], 'bn': ['100 Hz', '50 Hz', '25 Hz', '200 Hz']},
        "correct": 0,
        "expl_en": 'In a full-wave rectifier, both half cycles of the AC input are rectified, doubling the output pulse rate. Therefore, ripple frequency = 2 × f<sub>in</sub> = 2 × 50 Hz = 100 Hz.',
        "expl_bn": 'পূর্ণ তরঙ্গ একমুখীকারী বর্তনীতে ইনপুটের প্রতি চক্রে দুটি আউটপুট স্পন্দন পাওয়া যায়। তাই রিপল কম্পাঙ্ক = ২ × ৫০ = ১০০ Hz।',
    },
    {
        "id": 'PHY-072',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Units and Measurement & Dimensional Analysis',
        "difficulty": 'Easy',
        "en": 'Which of the following physical quantities has the dimensional formula [M¹ L⁻¹ T⁻²]?',
        "bn": 'নিচের কোন ভৌত রাশিটির মাত্রীয় সংকেত [M¹ L⁻¹ T⁻²]?',
        "opts": {'en': ['Pressure and Stress', 'Force and Torque', 'Energy and Work', 'Power and Momentum'], 'bn': ['চাপ এবং পীড়ন', 'বল এবং টর্ক', 'শক্তি এবং কার্য', 'ক্ষমতা এবং ভরবেগ']},
        "correct": 0,
        "expl_en": 'Pressure = Force / Area = [M L T⁻²] / [L²] = [M L⁻¹ T⁻²]. Stress also has dimensions of Force / Area = [M L⁻¹ T⁻²].',
        "expl_bn": 'চাপ = বল / ক্ষেত্রফল = [M L T⁻²] / [L²] = [M L⁻¹ T⁻²]। পীড়নের মাত্রাও একই।',
    },
    {
        "id": 'PHY-073',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Kinematics & Projectile Motion from Height',
        "difficulty": 'Medium',
        "en": 'A stone is projected horizontally with speed 20 m/s from the top of a cliff of height 80 m. The speed of the stone when it strikes the ground is (take g = 10 m/s²):',
        "bn": '৮০ মিটার উঁচু একটি খাড়া পাহাড়ের শীর্ষ থেকে একটি পাথরকে ২০ m/s অনুভূমিক বেগে নিক্ষেপ করা হলো। ভূমিতে আঘাত করার মুহূর্তে পাথরটির দ্রুতি কত? (g = 10 m/s²):',
        "opts": {'en': ['20√5 m/s (≈ 44.7 m/s)', '40 m/s', '30 m/s', '50 m/s'], 'bn': ['20√5 m/s (≈ 44.7 m/s)', '40 m/s', '30 m/s', '50 m/s']},
        "correct": 0,
        "expl_en": 'Horizontal velocity remains constant: v<sub>x</sub> = 20 m/s. Vertical velocity upon hitting ground: v<sub>y</sub>² = 2 g h = 2 × 10 × 80 = 1600 => v<sub>y</sub> = 40 m/s. Net speed v = √(v<sub>x</sub>² + v<sub>y</sub>²) = √(20² + 40²) = √(400 + 1600) = √2000 = 20√5 m/s ≈ 44.7 m/s.',
        "expl_bn": 'অনুভূমিক বেগ v<sub>x</sub> = ২০ m/s স্থির। উলম্ব বেগ v<sub>y</sub> = √(২gh) = √(২ × ১০ × ৮০) = ৪০ m/s। লব্ধি দ্রুতি v = √(২০² + ৪০²) = ২০√৫ m/s।',
    },
    {
        "id": 'PHY-074',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Laws of Motion & Connected Bodies',
        "difficulty": 'Easy',
        "en": 'Two blocks of masses 4 kg and 6 kg connected by a light inextensible string are placed on a smooth horizontal table. A horizontal force of 20 N pulls the 6 kg block. The tension in the string connecting the blocks is:',
        "bn": 'একটি মসৃণ অনুভূমিক টেবিলে হালকা অপ্রসার্য সুতো দ্বারা যুক্ত ৪ কেজি ও ৬ কেজি ভরের দুটি ব্লক রাখা আছে। ৬ কেজি ব্লকের ওপর ২০ N বল প্রয়োগ করে টানা হলে তাদের সংযোগকারী সুতোর টান কত?',
        "opts": {'en': ['8 N', '12 N', '10 N', '16 N'], 'bn': ['8 N', '12 N', '10 N', '16 N']},
        "correct": 0,
        "expl_en": 'Common acceleration a = F / (m₁ + m₂) = 20 / (4 + 6) = 2 m/s². The string accelerates only the 4 kg block: Tension T = m₁ a = 4 × 2 = 8 N.',
        "expl_bn": 'সাধারণ ত্বরণ a = ২০ / (৪ + ৬) = ২ m/s²। সুতোটি ৪ কেজি ভরকে টানে, সুতরাং টান T = ৪ × ২ = ৮ N।',
    },
    {
        "id": 'PHY-075',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Rotational Motion & Rolling Energy',
        "difficulty": 'Medium',
        "en": 'A uniform solid sphere of mass M and radius R rolls without slipping on a horizontal surface with linear velocity v. The fraction of its total kinetic energy that is associated with rotational kinetic energy is:',
        "bn": 'M ভর ও R ব্যাসার্ধের একটি নিরেট গোলক অনুভূমিক তলে v রৈখিক বেগে না পিছলে গড়িয়ে চলছে। এর মোট গতিশক্তির কত ভগ্নাংশ ঘূর্ণন গতিশক্তি হিসেবে থাকে?',
        "opts": {'en': ['2 / 7', '5 / 7', '1 / 2', '2 / 5'], 'bn': ['2 / 7', '5 / 7', '1 / 2', '2 / 5']},
        "correct": 0,
        "expl_en": 'Translational KE = 0.5 M v². Rotational KE = 0.5 I ω² = 0.5 (2/5 M R²) (v/R)² = (1/5) M v². Total KE = 0.5 M v² + 0.2 M v² = (7/10) M v². Fraction rotational = (1/5) / (7/10) = 2/7.',
        "expl_bn": 'ঘূর্ণন গতিশক্তি K<sub>rot</sub> = ১/৫ M v²। মোট গতিশক্তি K<sub>total</sub> = ৭/১০ M v²। ঘূর্ণন গতিশক্তির ভগ্নাংশ = (১/৫) / (৭/১০) = ২/৭।',
    },
    {
        "id": 'PHY-076',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Oscillations & Spring-Mass System',
        "difficulty": 'Easy',
        "en": 'A spring of spring constant k is cut into two equal halves. The spring constant of each half is:',
        "bn": 'k বল ধ্রুবকবিশিষ্ট একটি স্প্রিংকে কেটে সমান দুটি অংশে বিভক্ত করা হলো। প্রতিটি অর্ধাংশের স্প্রিং ধ্রুবক কত হবে?',
        "opts": {'en': ['2k', 'k / 2', 'k', '4k'], 'bn': ['2k', 'k / 2', 'k', '4k']},
        "correct": 0,
        "expl_en": "Spring constant is inversely proportional to its length (k × L = constant). When the length is halved (L' = L/2), the spring constant doubles to 2k.",
        "expl_bn": 'স্প্রিং ধ্রুবক দৈর্ঘ্যের ব্যস্তানুপাতিক (k ∝ ১/L)। দৈর্ঘ্য অর্ধেক হলে স্প্রিং ধ্রুবক দ্বিগুণ (2k) হয়।',
    },
    {
        "id": 'PHY-077',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Current Electricity & Wheatstone Bridge',
        "difficulty": 'Easy',
        "en": 'In a Wheatstone bridge, the four arms have resistances P = 10 Ω, Q = 20 Ω, R = 15 Ω, and S = 30 Ω. The bridge is:',
        "bn": 'একটি হুইটস্টোন ব্রিজের চারটি বাহুর রোধ P = ১০ Ω, Q = ২০ Ω, R = ১৫ Ω এবং S = ৩০ Ω। ব্রিজটি:',
        "opts": {'en': ['Balanced, and no current flows through the galvanometer', 'Unbalanced, and current flows from B to D', 'Unbalanced, and current flows from D to B', 'Short-circuited'], 'bn': ['ভারসাম্যাবস্থায় আছে, এবং গ্যালভানোমিটারে কোনো প্রবাহ যাবে না', 'ভারসাম্যহীন, এবং B থেকে D তে প্রবাহ যাবে', 'ভারসাম্যহীন, এবং D থেকে B তে প্রবাহ যাবে', 'শর্ট-সার্কিটযুক্ত']},
        "correct": 0,
        "expl_en": 'Check balance condition: P / Q = 10 / 20 = 1/2. R / S = 15 / 30 = 1/2. Since P / Q = R / S, the bridge is balanced and the galvanometer current is zero.',
        "expl_bn": 'P/Q = ১০/২০ = ১/২ এবং R/S = ১৫/৩০ = ১/২। যেহেতু P/Q = R/S, ব্রিজটি ভারসাম্যাবস্থায় আছে এবং গ্যালভানোমিটার দিয়ে কোনো তড়িৎ প্রবাহিত হবে না।',
    },
    {
        "id": 'PHY-078',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Magnetism & Tangent Galvanometer',
        "difficulty": 'Easy',
        "en": "At a certain place, the horizontal component of Earth's magnetic field is B<sub>H</sub> and the vertical component is B<sub>V</sub>. If the angle of dip (magnetic inclination) is 45°, then:",
        "bn": 'কোনো স্থানে পৃথিবীর চৌম্বক ক্ষেত্রের অনুভূমিক উপাংশ B<sub>H</sub> এবং উলম্ব উপাংশ B<sub>V</sub>। বিনতি কোণ ৪৫° হলে:',
        "opts": {'en': ['B<sub>V</sub> = B<sub>H</sub>', 'B<sub>V</sub> = √3 B<sub>H</sub>', 'B<sub>V</sub> = B<sub>H</sub> / √3', 'B<sub>V</sub> = 0'], 'bn': ['B<sub>V</sub> = B<sub>H</sub>', 'B<sub>V</sub> = √3 B<sub>H</sub>', 'B<sub>V</sub> = B<sub>H</sub> / √3', 'B<sub>V</sub> = 0']},
        "correct": 0,
        "expl_en": 'Angle of dip δ is given by tan δ = B<sub>V</sub> / B<sub>H</sub>. For δ = 45°: tan(45°) = 1 => B<sub>V</sub> / B<sub>H</sub> = 1 => B<sub>V</sub> = B<sub>H</sub>.',
        "expl_bn": 'বিনতি কোণ tan δ = B<sub>V</sub> / B<sub>H</sub>। δ = ৪৫° হলে tan(৪৫°) = ১ => B<sub>V</sub> = B<sub>H</sub>।',
    },
    {
        "id": 'PHY-079',
        "exam": 'JEE, WBJEE, NEET, BITSAT',
        "subject": 'Physics',
        "topic": 'Electromagnetic Induction & Transformer',
        "difficulty": 'Easy',
        "en": 'An ideal step-down transformer transforms 2200 V to 220 V. If the primary coil has 5000 turns, the number of turns in the secondary coil is:',
        "bn": 'একটি আদর্শ স্টেপ-ডাউন ট্রান্সফরমার ২২০০ V কে ২২০ V এ রূপান্তরিত করে। মুখ্য কুণ্ডলীর পাকসংখ্যা ৫০০০ হলে গৌণ কুণ্ডলীর পাকসংখ্যা কত?',
        "opts": {'en': ['500 turns', '50 turns', '1000 turns', '250 turns'], 'bn': ['৫০০ পাক', '৫০ পাক', '১০০০ পাক', '২৫০ পাক']},
        "correct": 0,
        "expl_en": 'Transformation ratio: V<sub>s</sub> / V<sub>p</sub> = N<sub>s</sub> / N<sub>p</sub> => N<sub>s</sub> = N<sub>p</sub> × (V<sub>s</sub> / V<sub>p</sub>) = 5000 × (220 / 2200) = 5000 × (1/10) = 500 turns.',
        "expl_bn": 'ট্রান্সফরমারের সূত্রানুসারে N<sub>s</sub> = N<sub>p</sub> × (V<sub>s</sub> / V<sub>p</sub>) = ৫০০০ × (২২০ / ২২০০) = ৫০০ পাক।',
    },
    {
        "id": 'PHY-080',
        "exam": 'NEET, JEE, WBJEE, CUET',
        "subject": 'Physics',
        "topic": 'Dual Nature & Photoelectric Stopping Potential',
        "difficulty": 'Medium',
        "en": 'When radiation of frequency 2ν₀ (where ν₀ is the threshold frequency) is incident on a metal plate, the maximum velocity of photoelectrons is v₁. When radiation of frequency 5ν₀ is incident on the same plate, the maximum velocity is v₂. The ratio v₁ / v₂ is:',
        "bn": 'কোনো ধাতুর ওপর ২ν₀ (যেখানে ν₀ হলো সূচনা কম্পাঙ্ক) কম্পাঙ্কের আলো আপতিত হলে নির্গত ইলেকট্রনের সর্বোচ্চ বেগ হয় v₁। একই ধাতুতে ৫ν₀ কম্পাঙ্কের আলো আপতিত হলে সর্বোচ্চ বেগ হয় v₂। v₁ / v₂ এর অনুপাত কত?',
        "opts": {'en': ['1 / 2', '1 / 4', '1 / √2', '2 / 5'], 'bn': ['1 / 2', '1 / 4', '1 / √2', '2 / 5']},
        "correct": 0,
        "expl_en": "By Einstein's photoelectric equation: K<sub>max</sub> = 0.5 m v² = hν - hν₀. For ν = 2ν₀: 0.5 m v₁² = 2hν₀ - hν₀ = hν₀. For ν = 5ν₀: 0.5 m v₂² = 5hν₀ - hν₀ = 4hν₀. Dividing the two equations: v₁² / v₂² = hν₀ / 4hν₀ = 1/4 => v₁ / v₂ = 1/2.",
        "expl_bn": 'আইনস্টাইনের সমীকরণ: ১/২ m v² = h(ν - ν₀)। প্রথম ক্ষেত্রে ১/২ m v₁² = hν₀, দ্বিতীয় ক্ষেত্রে ১/২ m v₂² = ৪hν₀। v₁²/v₂² = ১/৪ => v₁/v₂ = ১/২।',
    },
]
