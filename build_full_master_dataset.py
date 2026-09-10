import json
import csv
import os

# =============================================================================
# INLINE RESPONSIVE SVG SCHEMATICS (CIRCUITS, OPTICS, MECHANICS, REACTIONS, BIO)
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

SVG_CHEM_REACTION_FLOW = """<svg viewBox="0 0 540 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Box A -->
  <rect x="20" y="30" width="130" height="60" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="85" y="55" fill="#1e40af" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">PbO₂ + H₂SO₄</text>
  <text x="85" y="75" fill="#64748b" font-size="11" font-family="system-ui" text-anchor="middle">(Warm, Δ)</text>
  <!-- Arrow 1 -->
  <line x1="150" y1="60" x2="210" y2="60" stroke="#2563eb" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="180" y="50" fill="#2563eb" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">O₂ ↑</text>
  <!-- Box B -->
  <rect x="210" y="30" width="130" height="60" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
  <text x="275" y="55" fill="#15803d" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">PbSO₄ + H₂O</text>
  <text x="275" y="75" fill="#16a34a" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">White ppt</text>
  
  <!-- Row 2 -->
  <rect x="20" y="125" width="130" height="60" rx="8" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
  <text x="85" y="150" fill="#b45309" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">Na₂S₂O₃ + Cl₂</text>
  <text x="85" y="170" fill="#64748b" font-size="11" font-family="system-ui" text-anchor="middle">+ H₂O</text>
  <!-- Arrow 2 -->
  <line x1="150" y1="155" x2="210" y2="155" stroke="#d97706" stroke-width="2.5"/>
  <!-- Box C -->
  <rect x="210" y="125" width="130" height="60" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
  <text x="275" y="150" fill="#b91c1c" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">NaHSO₄ + S ↓</text>
  <text x="275" y="170" fill="#dc2626" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Colloidal Sulfur</text>

  <!-- Legend -->
  <rect x="360" y="30" width="160" height="155" rx="8" fill="#f8fafc" stroke="#475569" stroke-width="1.5"/>
  <text x="440" y="55" fill="#0f172a" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">Reagent Key</text>
  <text x="370" y="85" fill="#334155" font-size="11" font-family="system-ui">• (A) Δ (Heat)</text>
  <text x="370" y="110" fill="#334155" font-size="11" font-family="system-ui">• (B) Chlorine (Cl₂)</text>
  <text x="370" y="135" fill="#334155" font-size="11" font-family="system-ui">• (C) Iodine (I₂)</text>
  <text x="370" y="160" fill="#334155" font-size="11" font-family="system-ui">• (D) Nitric Oxide (NO)</text>
</svg>"""

SVG_CFT_SPLITTING = """<svg viewBox="0 0 460 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Free ion d-orbitals -->
  <rect x="30" y="90" width="110" height="30" rx="4" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>
  <text x="85" y="110" fill="#1e293b" font-size="13" font-family="system-ui" font-weight="bold" text-anchor="middle">Free ion (5 d)</text>
  <!-- Barycenter line -->
  <line x1="140" y1="105" x2="430" y2="105" stroke="#94a3b8" stroke-dasharray="3 3" stroke-width="1.5"/>
  <text x="420" y="120" fill="#64748b" font-size="10" font-family="system-ui">Barycenter</text>
  <!-- Octahedral splitting -->
  <!-- eg level (up) -->
  <line x1="200" y1="105" x2="270" y2="45" stroke="#3b82f6" stroke-width="1.5"/>
  <rect x="270" y="30" width="80" height="30" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="310" y="50" fill="#1e40af" font-size="13" font-family="system-ui" font-weight="bold" text-anchor="middle">e<tspan font-size="10">g</tspan> (+0.6 Δₒ)</text>
  <!-- t2g level (down) -->
  <line x1="200" y1="105" x2="270" y2="155" stroke="#3b82f6" stroke-width="1.5"/>
  <rect x="270" y="140" width="90" height="30" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="315" y="160" fill="#1e40af" font-size="13" font-family="system-ui" font-weight="bold" text-anchor="middle">t<tspan font-size="10">2g</tspan> (-0.4 Δₒ)</text>
  <!-- Arrow delta_o -->
  <line x1="380" y1="45" x2="380" y2="155" stroke="#dc2626" stroke-width="2"/>
  <text x="395" y="105" fill="#dc2626" font-size="15" font-family="system-ui" font-weight="black">Δₒ</text>
</svg>"""

SVG_IMMUNE_RESPONSE = """<svg viewBox="0 0 520 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Axes -->
  <line x1="50" y1="175" x2="480" y2="175" stroke="#334155" stroke-width="2"/>
  <line x1="50" y1="175" x2="50" y2="25" stroke="#334155" stroke-width="2"/>
  <text x="440" y="195" fill="#334155" font-size="11" font-family="system-ui" font-weight="bold">Time (Days)</text>
  <text x="55" y="20" fill="#334155" font-size="11" font-family="system-ui" font-weight="bold">Antibody Titer in Serum (log scale)</text>
  
  <!-- Primary Response Curve -->
  <path d="M 70 175 Q 110 175 140 105 Q 170 115 210 160" fill="none" stroke="#2563eb" stroke-width="3"/>
  <text x="140" y="90" fill="#1d4ed8" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">Primary Response (IgM)</text>
  
  <!-- Secondary Exposure Point -->
  <line x1="250" y1="175" x2="250" y2="130" stroke="#dc2626" stroke-dasharray="2 2" stroke-width="1.5"/>
  <text x="250" y="125" fill="#dc2626" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">2nd Exposure</text>
  
  <!-- Secondary Response Curve (Much higher & faster) -->
  <path d="M 250 160 Q 280 40 330 35 Q 400 45 470 95" fill="none" stroke="#dc2626" stroke-width="3.5"/>
  <text x="350" y="28" fill="#b91c1c" font-size="13" font-family="system-ui" font-weight="black" text-anchor="middle">Secondary Response (High IgG)</text>
</svg>"""

SVG_ANTIBODY_STRUCTURE = """<svg viewBox="0 0 420 230" width="100%" height="230" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Heavy Chains (Blue) -->
  <path d="M 120 40 L 190 110 L 190 200" fill="none" stroke="#2563eb" stroke-width="8" stroke-linecap="round"/>
  <path d="M 300 40 L 230 110 L 230 200" fill="none" stroke="#2563eb" stroke-width="8" stroke-linecap="round"/>
  <!-- Light Chains (Cyan) -->
  <path d="M 80 65 L 145 125" fill="none" stroke="#06b6d4" stroke-width="7" stroke-linecap="round"/>
  <path d="M 340 65 L 275 125" fill="none" stroke="#06b6d4" stroke-width="7" stroke-linecap="round"/>
  <!-- Disulfide bonds -->
  <line x1="190" y1="135" x2="230" y2="135" stroke="#eab308" stroke-width="3"/>
  <line x1="190" y1="150" x2="230" y2="150" stroke="#eab308" stroke-width="3"/>
  <line x1="125" y1="105" x2="140" y2="120" stroke="#eab308" stroke-width="3"/>
  <line x1="295" y1="105" x2="280" y2="120" stroke="#eab308" stroke-width="3"/>
  <text x="70" y="30" fill="#0e7490" font-size="12" font-family="system-ui" font-weight="bold">Antigen-Binding Site (Fab)</text>
  <text x="350" y="30" fill="#0e7490" font-size="12" font-family="system-ui" font-weight="bold">Antigen-Binding Site (Fab)</text>
  <text x="210" y="215" fill="#1e3a8a" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">Fc Region (Constant)</text>
  <text x="50" y="100" fill="#0891b2" font-size="11" font-family="system-ui">Light Chain (L)</text>
  <text x="250" y="170" fill="#1d4ed8" font-size="11" font-family="system-ui">Heavy Chain (H₂L₂)</text>
</svg>"""

SVG_LAC_OPERON = """<svg viewBox="0 0 540 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- DNA Strip -->
  <rect x="20" y="60" width="500" height="40" rx="6" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>
  <!-- Genes -->
  <rect x="30" y="65" width="60" height="30" rx="4" fill="#cbd5e1"/><text x="60" y="85" fill="#0f172a" font-size="12" font-family="monospace" font-weight="bold" text-anchor="middle">p(i)</text>
  <rect x="95" y="65" width="70" height="30" rx="4" fill="#fed7aa"/><text x="130" y="85" fill="#9a3412" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">i (rep)</text>
  <rect x="170" y="65" width="60" height="30" rx="4" fill="#cbd5e1"/><text x="200" y="85" fill="#0f172a" font-size="12" font-family="monospace" font-weight="bold" text-anchor="middle">P</text>
  <rect x="235" y="65" width="55" height="30" rx="4" fill="#bbf7d0"/><text x="262" y="85" fill="#166534" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">O</text>
  <rect x="295" y="65" width="75" height="30" rx="4" fill="#bfdbfe"/><text x="332" y="85" fill="#1e40af" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">z (β-gal)</text>
  <rect x="375" y="65" width="70" height="30" rx="4" fill="#ddd6fe"/><text x="410" y="85" fill="#5b21b6" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">y (perm)</text>
  <rect x="450" y="65" width="65" height="30" rx="4" fill="#fbcfe8"/><text x="482" y="85" fill="#9d174d" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">a (trans)</text>
  <text x="270" y="140" fill="#0f172a" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">Lac Operon Regulatory Unit in E. coli</text>
</svg>"""

SVG_PARABOLAS_AREA = """<svg viewBox="0 0 420 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <line x1="60" y1="190" x2="380" y2="190" stroke="#475569" stroke-width="2"/>
  <line x1="90" y1="210" x2="90" y2="20" stroke="#475569" stroke-width="2"/>
  <text x="375" y="180" fill="#475569" font-size="12" font-family="system-ui" font-weight="bold">x</text>
  <text x="100" y="30" fill="#475569" font-size="12" font-family="system-ui" font-weight="bold">y</text>
  <path d="M 90 190 Q 180 190 270 70 Q 180 30 90 190 Z" fill="#93c5fd" fill-opacity="0.45" stroke="#2563eb" stroke-width="1.5"/>
  <path d="M 40 190 Q 90 190 290 30" fill="none" stroke="#2563eb" stroke-width="3"/>
  <text x="300" y="45" fill="#1d4ed8" font-size="12" font-family="system-ui" font-weight="bold">y = x²</text>
  <path d="M 50 190 Q 180 10 310 190" fill="none" stroke="#dc2626" stroke-width="3"/>
  <text x="220" y="25" fill="#b91c1c" font-size="12" font-family="system-ui" font-weight="bold">y = 2x - x²</text>
  <circle cx="90" cy="190" r="4" fill="#0f172a"/>
  <text x="75" y="205" fill="#0f172a" font-size="11" font-family="monospace">(0,0)</text>
  <circle cx="270" cy="70" r="4" fill="#0f172a"/>
  <text x="275" y="75" fill="#0f172a" font-size="11" font-family="monospace">(1,1)</text>
</svg>"""

SVG_SKEW_LINES = """<svg viewBox="0 0 460 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Line 1 -->
  <line x1="60" y1="60" x2="380" y2="40" stroke="#2563eb" stroke-width="3"/>
  <text x="390" y="45" fill="#1d4ed8" font-size="13" font-family="system-ui" font-weight="bold">L₁: r⃗ = a⃗₁ + λb⃗₁</text>
  <!-- Line 2 -->
  <line x1="80" y1="160" x2="400" y2="130" stroke="#dc2626" stroke-width="3"/>
  <text x="410" y="135" fill="#b91c1c" font-size="13" font-family="system-ui" font-weight="bold">L₂: r⃗ = a⃗₂ + μb⃗₂</text>
  <!-- Common Perpendicular Shortest Distance -->
  <line x1="220" y1="50" x2="250" y2="145" stroke="#0f172a" stroke-width="2.5" stroke-dasharray="4 3"/>
  <circle cx="220" cy="50" r="4" fill="#0f172a"/>
  <circle cx="250" cy="145" r="4" fill="#0f172a"/>
  <text x="245" y="100" fill="#0f172a" font-size="13" font-family="system-ui" font-weight="black">d (Shortest Distance)</text>
</svg>"""

SVG_ICJ_EMBLEM = """<svg viewBox="0 0 440 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047"/>
      <stop offset="100%" stop-color="#ca8a04"/>
    </linearGradient>
  </defs>
  <polygon points="220,25 100,60 340,60" fill="url(#goldGrad)" opacity="0.9"/>
  <rect x="110" y="60" width="220" height="8" rx="2" fill="#93c5fd"/>
  <rect x="130" y="68" width="14" height="60" rx="3" fill="#cbd5e1"/>
  <rect x="170" y="68" width="14" height="60" rx="3" fill="#cbd5e1"/>
  <rect x="213" y="68" width="14" height="60" rx="3" fill="#cbd5e1"/>
  <rect x="256" y="68" width="14" height="60" rx="3" fill="#cbd5e1"/>
  <rect x="296" y="68" width="14" height="60" rx="3" fill="#cbd5e1"/>
  <rect x="100" y="128" width="240" height="12" rx="3" fill="url(#goldGrad)"/>
  <circle cx="220" cy="48" r="7" fill="#1e1b4b" stroke="#fde047" stroke-width="1.5"/>
  <line x1="210" y1="48" x2="230" y2="48" stroke="#fde047" stroke-width="2"/>
  <text x="220" y="156" fill="#0f172a" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">PEACE PALACE • THE HAGUE (NETHERLANDS)</text>
  <text x="220" y="172" fill="#2563eb" font-size="9" font-family="system-ui" font-weight="bold" text-anchor="middle">International Court of Justice (ICJ) • Principal UN Judicial Organ</text>
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

SVG_ARRHENIUS_PLOT = """<svg viewBox="0 0 460 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <line x1="60" y1="170" x2="420" y2="170" stroke="#334155" stroke-width="2.5"/>
  <line x1="60" y1="170" x2="60" y2="20" stroke="#334155" stroke-width="2.5"/>
  <text x="415" y="160" fill="#334155" font-size="12" font-family="system-ui" font-weight="bold">1 / T (K⁻¹)</text>
  <text x="70" y="30" fill="#334155" font-size="12" font-family="system-ui" font-weight="bold">ln(k)</text>
  <circle cx="60" cy="45" r="4" fill="#2563eb"/>
  <text x="68" y="45" fill="#2563eb" font-size="11" font-family="system-ui" font-weight="bold">ln(A) (Intercept)</text>
  <line x1="60" y1="45" x2="380" y2="155" stroke="#dc2626" stroke-width="3"/>
  <line x1="200" y1="93" x2="280" y2="93" stroke="#64748b" stroke-dasharray="3 2" stroke-width="1.5"/>
  <line x1="280" y1="93" x2="280" y2="121" stroke="#64748b" stroke-dasharray="3 2" stroke-width="1.5"/>
  <text x="290" y="112" fill="#dc2626" font-size="12" font-family="system-ui" font-weight="bold">Slope = −Eₐ / R</text>
  <rect x="180" y="25" width="220" height="35" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="290" y="47" fill="#0f172a" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">ln(k) = ln(A) − (Eₐ / R)(1 / T)</text>
</svg>"""

SVG_CANNIZZARO_FLOW = """<svg viewBox="0 0 540 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <rect x="20" y="45" width="150" height="70" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="95" y="72" fill="#1e40af" font-size="12" font-family="monospace" font-weight="bold" text-anchor="middle">C₆H₅CHO + HCHO</text>
  <text x="95" y="95" fill="#3b82f6" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">(No α-H atoms)</text>
  <line x1="170" y1="80" x2="260" y2="80" stroke="#0f172a" stroke-width="2.5"/>
  <polygon points="268,80 256,75 256,85" fill="#0f172a"/>
  <text x="215" y="65" fill="#b91c1c" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">50% conc. NaOH</text>
  <text x="215" y="98" fill="#475569" font-size="10" font-family="system-ui" text-anchor="middle">Δ (Heat)</text>
  <rect x="270" y="25" width="240" height="50" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
  <text x="390" y="48" fill="#15803d" font-size="12" font-family="monospace" font-weight="bold" text-anchor="middle">C₆H₅CH₂OH (Benzyl alcohol)</text>
  <text x="390" y="64" fill="#16a34a" font-size="10" font-family="system-ui" text-anchor="middle">[Reduction Product]</text>
  <rect x="270" y="85" width="240" height="50" rx="6" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
  <text x="390" y="108" fill="#b45309" font-size="12" font-family="monospace" font-weight="bold" text-anchor="middle">HCOO⁻Na⁺ (Sodium formate)</text>
  <text x="390" y="124" fill="#d97706" font-size="10" font-family="system-ui" text-anchor="middle">[Oxidation Product: HCHO is more reactive]</text>
  <text x="270" y="170" fill="#475569" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Crossed Cannizzaro Reaction: Formaldehyde oxidized, Benzaldehyde reduced</text>
</svg>"""

SVG_KRANZ_ANATOMY = """<svg viewBox="0 0 520 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <circle cx="260" cy="105" r="30" fill="#fed7aa" stroke="#c2410c" stroke-width="2"/>
  <text x="260" y="103" fill="#9a3412" font-size="10" font-family="system-ui" font-weight="bold" text-anchor="middle">Vascular</text>
  <text x="260" y="117" fill="#9a3412" font-size="10" font-family="system-ui" font-weight="bold" text-anchor="middle">Bundle</text>
  <circle cx="260" cy="105" r="58" fill="none" stroke="#16a34a" stroke-width="22" stroke-opacity="0.25"/>
  <circle cx="208" cy="105" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>
  <circle cx="312" cy="105" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>
  <circle cx="260" cy="53" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>
  <circle cx="260" cy="157" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>
  <circle cx="223" cy="68" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>
  <circle cx="297" cy="68" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>
  <circle cx="223" cy="142" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>
  <circle cx="297" cy="142" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>
  <rect x="60" y="30" width="100" height="40" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="110" y="48" fill="#166534" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Mesophyll Cell</text>
  <text x="110" y="62" fill="#15803d" font-size="9" font-family="system-ui" text-anchor="middle">PEPcase (C₄ Acid)</text>
  <line x1="160" y1="50" x2="220" y2="70" stroke="#16a34a" stroke-width="1.5"/>
  <rect x="360" y="30" width="130" height="40" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="425" y="48" fill="#92400e" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Bundle Sheath Cell</text>
  <text x="425" y="62" fill="#b45309" font-size="9" font-family="system-ui" text-anchor="middle">RuBisCO (Calvin Cycle)</text>
  <line x1="360" y1="50" x2="300" y2="70" stroke="#d97706" stroke-width="1.5"/>
  <text x="260" y="195" fill="#0f172a" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">Kranz Anatomy in C₄ Plants (Maize, Sugarcane) • Zero Photorespiration</text>
</svg>"""

SVG_SARCOMERE_STRUCTURE = """<svg viewBox="0 0 540 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <line x1="60" y1="20" x2="60" y2="160" stroke="#1e3a8a" stroke-width="3"/>
  <text x="60" y="175" fill="#1e3a8a" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Z-line</text>
  <line x1="480" y1="20" x2="480" y2="160" stroke="#1e3a8a" stroke-width="3"/>
  <text x="480" y="175" fill="#1e3a8a" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Z-line</text>
  <line x1="270" y1="20" x2="270" y2="160" stroke="#dc2626" stroke-dasharray="3 2" stroke-width="2"/>
  <text x="270" y="175" fill="#dc2626" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">M-line</text>
  <rect x="150" y="55" width="240" height="12" rx="3" fill="#dc2626"/>
  <rect x="150" y="85" width="240" height="12" rx="3" fill="#dc2626"/>
  <rect x="150" y="115" width="240" height="12" rx="3" fill="#dc2626"/>
  <line x1="60" y1="45" x2="220" y2="45" stroke="#2563eb" stroke-width="3"/>
  <line x1="60" y1="75" x2="220" y2="75" stroke="#2563eb" stroke-width="3"/>
  <line x1="60" y1="105" x2="220" y2="105" stroke="#2563eb" stroke-width="3"/>
  <line x1="60" y1="135" x2="220" y2="135" stroke="#2563eb" stroke-width="3"/>
  <line x1="480" y1="45" x2="320" y2="45" stroke="#2563eb" stroke-width="3"/>
  <line x1="480" y1="75" x2="320" y2="75" stroke="#2563eb" stroke-width="3"/>
  <line x1="480" y1="105" x2="320" y2="105" stroke="#2563eb" stroke-width="3"/>
  <line x1="480" y1="135" x2="320" y2="135" stroke="#2563eb" stroke-width="3"/>
  <line x1="150" y1="30" x2="390" y2="30" stroke="#991b1b" stroke-width="1.5"/>
  <text x="270" y="24" fill="#991b1b" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">A-Band (Constant Length)</text>
  <line x1="220" y1="150" x2="320" y2="150" stroke="#ea580c" stroke-width="1.5"/>
  <text x="270" y="145" fill="#ea580c" font-size="10" font-family="system-ui" font-weight="bold" text-anchor="middle">H-Zone</text>
  <text x="270" y="195" fill="#0f172a" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">1 Sarcomere (Between two Z-discs) • Contraction reduces H-zone &amp; I-band</text>
</svg>"""

SVG_GEL_ELECTROPHORESIS = """<svg viewBox="0 0 500 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <rect x="50" y="30" width="400" height="150" rx="8" fill="#f8fafc" stroke="#475569" stroke-width="2"/>
  <rect x="50" y="15" width="400" height="12" rx="3" fill="#3b82f6"/>
  <text x="250" y="25" fill="#ffffff" font-size="10" font-family="system-ui" font-weight="bold" text-anchor="middle">Cathode (−)</text>
  <rect x="50" y="183" width="400" height="12" rx="3" fill="#ef4444"/>
  <text x="250" y="193" fill="#ffffff" font-size="10" font-family="system-ui" font-weight="bold" text-anchor="middle">Anode (+)</text>
  <rect x="90" y="40" width="30" height="10" rx="2" fill="#334155"/>
  <rect x="160" y="40" width="30" height="10" rx="2" fill="#334155"/>
  <rect x="230" y="40" width="30" height="10" rx="2" fill="#334155"/>
  <rect x="300" y="40" width="30" height="10" rx="2" fill="#334155"/>
  <rect x="370" y="40" width="30" height="10" rx="2" fill="#334155"/>
  <rect x="93" y="65" width="24" height="4" fill="#f97316"/>
  <rect x="93" y="90" width="24" height="4" fill="#f97316"/>
  <rect x="93" y="115" width="24" height="4" fill="#f97316"/>
  <rect x="93" y="140" width="24" height="4" fill="#f97316"/>
  <rect x="93" y="165" width="24" height="4" fill="#f97316"/>
  <text x="105" y="58" fill="#64748b" font-size="9" font-family="system-ui" text-anchor="middle">Ladder</text>
  <rect x="163" y="80" width="24" height="5" fill="#f97316"/>
  <rect x="163" y="145" width="24" height="5" fill="#f97316"/>
  <rect x="233" y="165" width="24" height="5" fill="#f97316"/>
  <text x="245" y="155" fill="#ea580c" font-size="9" font-family="system-ui" font-weight="bold" text-anchor="middle">Smallest DNA</text>
  <line x1="420" y1="50" x2="420" y2="160" stroke="#dc2626" stroke-width="2"/>
  <polygon points="420,165 415,155 425,155" fill="#dc2626"/>
  <text x="430" y="105" fill="#dc2626" font-size="10" font-family="system-ui" font-weight="bold" transform="rotate(90,430,105)" text-anchor="middle">Migration Direction</text>
</svg>"""

SVG_HORMONAL_CYCLE = """<svg viewBox="0 0 520 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <line x1="45" y1="160" x2="480" y2="160" stroke="#334155" stroke-width="2"/>
  <line x1="45" y1="160" x2="45" y2="20" stroke="#334155" stroke-width="2"/>
  <text x="45" y="180" fill="#334155" font-size="10" font-family="system-ui" font-weight="bold">Day 1</text>
  <text x="240" y="180" fill="#dc2626" font-size="11" font-family="system-ui" font-weight="bold">Day 14 (Ovulation)</text>
  <text x="460" y="180" fill="#334155" font-size="10" font-family="system-ui" font-weight="bold">Day 28</text>
  <line x1="250" y1="160" x2="250" y2="25" stroke="#dc2626" stroke-dasharray="3 2" stroke-width="1.5"/>
  <path d="M 50 145 Q 180 140 230 110 Q 250 25 270 120 Q 350 145 475 145" fill="none" stroke="#dc2626" stroke-width="3"/>
  <text x="260" y="40" fill="#dc2626" font-size="11" font-family="system-ui" font-weight="bold">LH Surge</text>
  <path d="M 50 150 Q 150 145 220 70 Q 250 110 320 100 Q 400 135 475 150" fill="none" stroke="#2563eb" stroke-width="2.5"/>
  <text x="200" y="60" fill="#2563eb" font-size="10" font-family="system-ui" font-weight="bold">Estrogen</text>
  <path d="M 50 155 L 250 155 Q 350 65 420 80 Q 460 130 475 155" fill="none" stroke="#16a34a" stroke-width="2.5"/>
  <text x="375" y="75" fill="#16a34a" font-size="10" font-family="system-ui" font-weight="bold">Progesterone</text>
  <text x="260" y="198" fill="#475569" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">LH Surge triggers rupture of Graafian Follicle and Ovulation at Day 14</text>
</svg>"""

SVG_CONIC_COMMON_TANGENT = """<svg viewBox="0 0 460 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <line x1="30" y1="105" x2="430" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="180" y1="20" x2="180" y2="190" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="420" y="98" fill="#64748b" font-size="11" font-family="system-ui">x</text>
  <text x="185" y="25" fill="#64748b" font-size="11" font-family="system-ui">y</text>
  <circle cx="180" cy="105" r="50" fill="none" stroke="#2563eb" stroke-width="2.5"/>
  <text x="135" y="70" fill="#2563eb" font-size="11" font-family="system-ui" font-weight="bold">x² + y² = 2a²</text>
  <path d="M 330 35 Q 180 105 330 175" fill="none" stroke="#16a34a" stroke-width="2.5"/>
  <text x="320" y="30" fill="#16a34a" font-size="11" font-family="system-ui" font-weight="bold">y² = 8ax</text>
  <line x1="80" y1="180" x2="340" y2="40" stroke="#dc2626" stroke-width="2.5"/>
  <text x="240" y="65" fill="#dc2626" font-size="12" font-family="system-ui" font-weight="bold">Common Tangent: y = ±(x + 2a)</text>
  <circle cx="145" cy="142" r="3.5" fill="#dc2626"/>
  <circle cx="280" cy="72" r="3.5" fill="#dc2626"/>
</svg>"""

# =============================================================================
# MASTER MULTI-SUBJECT & MULTI-EXAM COMPATIBLE QUESTION REPOSITORY
# =============================================================================

all_questions = [
    # =========================================================================
    # 1. PHYSICS (High-Yield Authentic Questions & Circuit / Optics / Mechanics)
    # =========================================================================
    {
        "id": "PHY-001",
        "exam": "NEET, JEE, WBJEE, CUET, VITEEE, MHT-CET, KCET, CBSE",
        "subject": "Physics",
        "topic": "Units and Measurement",
        "difficulty": "Easy",
        "en": "In a Vernier callipers, 20 Vernier Scale Divisions (VSD) coincide with 16 Main Scale Divisions (MSD). If each MSD is 1 mm, the least count of the Vernier callipers is:",
        "bn": "একটি ভার্নিয়ার ক্যালিপার্সে, ২০টি ভার্নিয়ার স্কেল ঘর (VSD) ১৬টি মূল স্কেল ঘরের (MSD) সাথে মিলে যায়। মূল স্কেলের প্রতিটি ঘর ১ মিমি হলে ভার্নিয়ার ধ্রুবক (Least Count) কত?",
        "opts": {
            "en": ["0.02 cm", "0.01 cm", "0.2 mm", "0.02 mm"],
            "bn": ["0.02 cm", "0.01 cm", "0.2 mm", "0.02 mm"]
        },
        "correct": 0,
        "expl_en": "1 VSD = (16/20) MSD = 0.8 mm. Least Count LC = 1 MSD - 1 VSD = 1 mm - 0.8 mm = 0.2 mm = 0.02 cm.",
        "expl_bn": "১ VSD = (১৬/২০) MSD = ০.৮ মিমি। ভার্নিয়ার ধ্রুবক LC = ১ MSD - ১ VSD = ১ - ০.৮ = ০.২ মিমি = ০.০২ সেমি।"
    },
    {
        "id": "PHY-002",
        "exam": "JEE, WBJEE, BITSAT, NDA, MHT-CET, VITEEE, KCET",
        "subject": "Physics",
        "topic": "Kinematics",
        "difficulty": "Medium",
        "en": "A projectile is thrown with an initial velocity of u = (6i + 8j) m/s. The horizontal range of the projectile is (take g = 10 m/s²):",
        "bn": "একটি প্রক্ষেপ্যকে (6i + 8j) m/s প্রারম্ভিক বেগে নিক্ষেপ করা হলো। প্রক্ষেপ্যটির অনুভূমিক সীমা (Range) কত? (g = 10 m/s²):",
        "opts": {
            "en": ["9.6 m", "4.8 m", "12.8 m", "19.2 m"],
            "bn": ["9.6 m", "4.8 m", "12.8 m", "19.2 m"]
        },
        "correct": 0,
        "expl_en": "u_x = 6 m/s, u_y = 8 m/s. Time of flight T = 2 u_y / g = 2(8)/10 = 1.6 s. Horizontal Range R = u_x × T = 6 × 1.6 = 9.6 m.",
        "expl_bn": "u_x = ৬ m/s, u_y = ৮ m/s। উড্ডয়ন কাল T = ১.৬ সেকেন্ড। অনুভূমিক সীমা R = ৬ × ১.৬ = ৯.৬ মিটার।"
    },
    {
        "id": "PHY-003",
        "exam": "WBJEE, JEE, NEET, CUET, VITEEE, MHT-CET, KCET, COMEDK",
        "subject": "Physics",
        "topic": "Current Electricity",
        "difficulty": "Medium",
        "en": "A wire of resistance R is stretched uniformly such that its length increases by 10%. The percentage increase in its resistance is approximately:",
        "bn": "R রোধের একটি পরিবাহী তারকে সুষমভাবে টেনে দৈর্ঘ্য ১০% বৃদ্ধি করা হলো। তারটির রোধের শতকরা বৃদ্ধি কত হবে?",
        "opts": {
            "en": ["21%", "10%", "20%", "11%"],
            "bn": ["21%", "10%", "20%", "11%"]
        },
        "correct": 0,
        "expl_en": "Since volume V = A × L remains constant during stretching, R ∝ L². If L' = 1.1 L, then R' = (1.1)² R = 1.21 R. Percentage increase = (1.21 - 1) × 100% = 21%.",
        "expl_bn": "আয়তন ধ্রুবক থাকায় R ∝ L²। L' = ১.১ L হলে R' = ১.২১ R। রোধের শতকরা বৃদ্ধি = ২১%।"
    },
    {
        "id": "PHY-004",
        "exam": "NEET, CUET, WBJEE, NDA, CBSE, AIIMS, AFMC",
        "subject": "Physics",
        "topic": "Ray Optics",
        "difficulty": "Easy",
        "en": "A convex lens of focal length 20 cm in air is immersed in water of refractive index 4/3. If refractive index of glass is 3/2, its new focal length in water is:",
        "bn": "বায়ুতে ২০ সেমি ফোকাস দূরত্বের একটি উত্তল লেন্সকে ৪/৩ প্রতিসরাঙ্কের পানিতে নিমজ্জিত করা হলো। কাঁচের প্রতিসরাঙ্ক ৩/২ হলে পানিতে লেন্সটির নতুন ফোকাস দূরত্ব কত?",
        "opts": {
            "en": ["80 cm", "40 cm", "20 cm", "60 cm"],
            "bn": ["80 cm", "40 cm", "20 cm", "60 cm"]
        },
        "correct": 0,
        "expl_en": "By Lens Maker's Formula: 1/f_air = (1.5 - 1)(1/R1 - 1/R2) = 0.5 K => K = 1/10. In water: 1/f_water = [(1.5 / 1.333) - 1] K = (1/8)(1/10) = 1/80 => f_water = 80 cm.",
        "expl_bn": "লেন্স মেকার সূত্রানুসারে: f_water = 4 × f_air = ৪ × ২০ = ৮০ সেমি।"
    },
    {
        "id": "PHY-005",
        "exam": "JEE, WBJEE, IAT, NEET, BITSAT, OLYMPIAD, IIT-JAM",
        "subject": "Physics",
        "topic": "Modern Physics & Dual Nature",
        "difficulty": "Medium",
        "en": "The de Broglie wavelength of an electron accelerated through a potential difference of 100 V is approximately:",
        "bn": "১০০ ভোল্ট বিভব পার্থক্যের মধ্য দিয়ে ত্বরান্বিত একটি ইলেকট্রনের দ্য ব্রগলি তরঙ্গদৈর্ঘ্য কত?",
        "opts": {
            "en": ["1.227 Å", "0.123 Å", "12.27 Å", "0.613 Å"],
            "bn": ["1.227 Å", "0.123 Å", "12.27 Å", "0.613 Å"]
        },
        "correct": 0,
        "expl_en": "For an electron accelerated by V volts: λ = 12.27 / √V Å = 12.27 / √100 Å = 12.27 / 10 = 1.227 Å (or 0.1227 nm).",
        "expl_bn": "ইলেকট্রনের জন্য λ = ১২.২৭ / √V Å = ১২.২৭ / ১০ = ১.২২৭ Å।"
    },
    {
        "id": "PHY-006",
        "exam": "JEE, WBJEE, NEET, BITSAT, IAT, NEST, KCET, COMEDK",
        "subject": "Physics",
        "topic": "Experimental Physics & Instruments",
        "difficulty": "Hard",
        "diagram": SVG_SCREW_GAUGE,
        "en": "A screw gauge has a pitch of 0.5 mm and 50 divisions on its circular scale. When measuring a wire, the linear scale reads 3 mm and the 32nd division coincides with the reference line. If the screw gauge has a negative zero error of -0.02 mm, the true diameter of the wire is:",
        "bn": "একটি স্ক্রু গেজের পিচ ০.৫ মিমি এবং বৃত্তাকার স্কেলে ৫০টি ভাগ রয়েছে। একটি তারের ব্যাস পরিমাপে রৈখিক স্কেলের পাঠ ৩ মিমি এবং বৃত্তাকার স্কেলের ৩২তম দাগ নির্দেশক রেখার সাথে মিলে যায়। যন্ত্রটিতে যদি -০.০২ মিমি ঋণাত্মক শূন্য ত্রুটি থাকে, তবে তারটির প্রকৃত ব্যাস কত?",
        "opts": {
            "en": ["3.34 mm", "3.30 mm", "3.32 mm", "3.36 mm"],
            "bn": ["3.34 mm", "3.30 mm", "3.32 mm", "3.36 mm"]
        },
        "correct": 0,
        "expl_en": "Least Count LC = Pitch / Total Circular Divisions = 0.5 mm / 50 = 0.01 mm. Measured Reading = MSR + (CSR × LC) = 3 mm + (32 × 0.01 mm) = 3.32 mm. True Reading = Measured Reading - (Zero Error) = 3.32 mm - (-0.02 mm) = 3.34 mm.",
        "expl_bn": "লঘিষ্ঠ ধ্রুবক LC = ০.৫ / ৫০ = ০.০১ মিমি। পরিমাপকৃত মান = ৩ + (৩২ × ০.০১) = ৩.৩২ মিমি। প্রকৃত মান = ৩.৩২ - (-০.০২) = ৩.৩৪ মিমি।"
    },
    {
        "id": "PHY-007",
        "exam": "JEE, WBJEE, IAT, BITSAT, VITEEE, MHT-CET, GATE",
        "subject": "Physics",
        "topic": "Alternating Current",
        "difficulty": "Hard",
        "diagram": SVG_LCR_CIRCUIT,
        "en": "In the given series LCR circuit connected to an AC source V = V₀ sin(100πt + π/6), the voltmeters read V_L = 40 V, V_R = 40 V, and the circuit parameters are Z = 5 Ω, R = 4 Ω. The capacitive reactance X_C and the peak voltage V₀ of the AC source are respectively:",
        "bn": "চিত্রে প্রদর্শিত শ্রেণী LCR বর্তনীতে V = V₀ sin(100πt + π/6) পরিবর্তী উৎসের সাথে যুক্ত থাকলে ভোল্টমিটারের পাঠ V_L = 40 V, V_R = 40 V এবং বর্তনীর প্রতিবন্ধকতা Z = 5 Ω, রোধ R = 4 Ω। ধারকীয় প্রতিঘাত X_C এবং উৎসের শীর্ষ ভোল্টেজ V₀ যথাক্রমে কত?",
        "opts": {
            "en": ["1 Ω and 50√2 V", "7 Ω and 50 V", "1 Ω and 50 V", "3 Ω and 40√2 V"],
            "bn": ["1 Ω এবং 50√2 V", "7 Ω and 50 V", "1 Ω and 50 V", "3 Ω and 40√2 V"]
        },
        "correct": 0,
        "expl_en": "Current I_rms = V_R / R = 40/4 = 10 A. Peak current I_0 = 10√2 A. Effective voltage V_rms = I_rms × Z = 10 × 5 = 50 V => V_0 = 50√2 V. Reactance X_L = V_L / I_rms = 40/10 = 4 Ω. Since Z² = R² + (X_L - X_C)², 25 = 16 + (4 - X_C)² => (4 - X_C)² = 9 => 4 - X_C = 3 => X_C = 1 Ω.",
        "expl_bn": "তড়িৎপ্রবাহ I_rms = ৪০/৪ = ১০ A। কার্যকর ভোল্টেজ V_rms = ১০ × ৫ = ৫০ V, শীর্ষ ভোল্টেজ V₀ = ৫০√২ V। প্রতিঘাত X_L = ৪০/১০ = ৪ Ω। Z² = R² + (X_L - X_C)² থেকে X_C = ১ Ω।"
    },
    {
        "id": "PHY-008",
        "exam": "JEE, WBJEE, NDA, NEET, CDS, AFCAT, MHT-CET",
        "subject": "Physics",
        "topic": "Laws of Motion & Equilibrium",
        "difficulty": "Medium",
        "diagram": SVG_MECHANICAL_EQUILIBRIUM,
        "en": "Block B of weight W lies on a rough horizontal table with coefficient of static friction μ. The cord between block B and the knot is horizontal, while the cord to the wall makes an angle θ with the ceiling. The maximum weight of hanging block A for which the system remains in stationary equilibrium is:",
        "bn": "W ওজনের একটি ব্লক B একটি খসখসে অনুভূমিক টেবিলের ওপর রাখা আছে যার স্থৈতিক ঘর্ষণ গুণাঙ্ক μ। B এবং নটের (knot) মধ্যবর্তী দড়িটি অনুভূমিক এবং ছাদের সাথে যুক্ত দড়িটি ছাদের সাথে θ কোণ উৎপন্ন করে। ঝুলন্ত ব্লক A-এর সর্বোচ্চ কত ওজনের জন্য সংস্থাটি সাম্যাবস্থায় স্থির থাকবে?",
        "opts": {
            "en": ["μ W tan θ", "W tan θ / μ", "μ W sin θ", "μ W √(1 + tan² θ)"],
            "bn": ["μ W tan θ", "W tan θ / μ", "μ W sin θ", "μ W √(1 + tan² θ)"]
        },
        "correct": 0,
        "expl_en": "At the knot: let slanted tension be T. Horizontal equilibrium: T cos θ = T_horiz = f_s ≤ μ W. Vertical equilibrium: T sin θ = W_A. Dividing the two equations: W_A / (μ W) = tan θ => W_A = μ W tan θ.",
        "expl_bn": "নট বিন্দুতে সাম্যাবস্থা বিবেচনা করে: অনুভূমিক উপাংশ T cos θ = μ W এবং উল্লম্ব উপাংশ T sin θ = W_A। ভাগ করে পাওয়া যায় W_A = μ W tan θ।"
    },
    {
        "id": "PHY-009",
        "exam": "JEE, JEE-ADV, IAT, WBJEE, NEST, OLYMPIAD, IIT-JAM",
        "subject": "Physics",
        "topic": "Gravitation",
        "difficulty": "Hard",
        "diagram": SVG_SPHERE_CAVITY,
        "en": "From a uniform solid sphere of mass M and radius R, a spherical cavity of radius R/2 is removed such that its surface touches the boundary of the sphere. Taking gravitational potential V = 0 at r = ∞, the gravitational potential at the center P of the cavity thus formed is:",
        "bn": "M ভর ও R ব্যাসার্ধের একটি সুষম নিরেট গোলক থেকে R/2 ব্যাসার্ধের একটি গোলকীয় গহ্বর অপসারণ করা হলো যা মূল গোলকের পৃষ্ঠ স্পর্শ করে। r = ∞ তে মহাকর্ষীয় বিভব V = 0 ধরে, উৎপন্ন গহ্বরের কেন্দ্রবিন্দু P-তে মহাকর্ষীয় বিভব কত?",
        "opts": {
            "en": ["-GM / R", "-2GM / 3R", "-GM / 2R", "-2GM / R"],
            "bn": ["-GM / R", "-2GM / 3R", "-GM / 2R", "-2GM / R"]
        },
        "correct": 0,
        "expl_en": "By superposition principle: V_P = V_entire(at r = R/2) - V_removed(at its own center). For complete sphere: V_entire(R/2) = -(GM / 2R³)[3R² - (R/2)²] = -11GM / (8R). The removed cavity has mass M' = M( (R/2)³ / R³ ) = M/8 and radius R' = R/2. Potential at its center V_removed(0) = -3G M' / (2R') = -3G(M/8) / [2(R/2)] = -3GM / (8R). Therefore, V_P = -11GM/(8R) - [-3GM/(8R)] = -8GM/(8R) = -GM/R.",
        "expl_bn": "উপরিলেপন নীতি অনুযায়ী: V_P = V_সম্পূর্ণ(R/2) - V_অপসারিত(0)। সম্পূর্ণ গোলকের জন্য বিভব = -১১GM/(৮R) এবং অপসারিত অংশের কেন্দ্রে নিজস্ব বিভব = -৩GM/(৮R)। অতএব V_P = -GM/R।"
    },
    {
        "id": "PHY-010",
        "exam": "NEET, JEE, WBJEE, NDA, CUET, AIIMS, AFMC, KCET",
        "subject": "Physics",
        "topic": "Ray Optics & Optical Instruments",
        "difficulty": "Medium",
        "diagram": SVG_PRISM_TIR,
        "en": "A light ray is incident normally on face AB of a right-angled isosceles prism (A = 90°, B = 45°, C = 45°). If the refractive index of the prism material is μ = 1.50, the angle of deviation experienced by the ray upon emerging is:",
        "bn": "একটি সমকোণী সমদ্বিবাহু প্রিজমের (A = ৯০°, B = ৪৫°, C = ৪৫°) AB তলে একটি আলোক রশ্মি লম্বভাবে আপতিত হলো। প্রিজমের উপাদানের প্রতিসরাঙ্ক μ = ১.৫০ হলে নির্গমনকালে রশ্মিটির চ্যুতি কোণ (Angle of Deviation) কত হবে?",
        "opts": {
            "en": ["90°", "45°", "0°", "180°"],
            "bn": ["90°", "45°", "0°", "180°"]
        },
        "correct": 0,
        "expl_en": "Critical angle C_c = sin⁻¹(1/μ) = sin⁻¹(1/1.5) = 41.8°. Inside the prism, the ray strikes the hypotenuse BC at an angle of incidence i = 45°. Since i > C_c, Total Internal Reflection (TIR) occurs at BC and the ray exits perpendicular to face AC. Net deviation δ = 90°.",
        "expl_bn": "সংকট কোণ C_c = sin⁻¹(১/১.৫) = ৪১.৮°। প্রিজমের অভ্যন্তরে অতিভুজ পৃষ্ঠে আপতন কোণ i = ৪৫° যা সংকট কোণের চেয়ে বড়। ফলে পূর্ণ অভ্যন্তরীণ প্রতিফলন ঘটে এবং রশ্মিটি ৯০° কোণে বিচ্যুত হয়।"
    },
    {
        "id": "PHY-011",
        "exam": "JEE, WBJEE, BITSAT, NEET, CUET, NDA, MHT-CET",
        "subject": "Physics",
        "topic": "Current Electricity & Bridge Circuits",
        "difficulty": "Easy",
        "diagram": SVG_WHEATSTONE_BRIDGE,
        "en": "In the balanced Wheatstone bridge circuit shown in the diagram, the values of the three known resistors are P = 10 Ω, Q = 20 Ω, and R = 15 Ω. For zero deflection in the galvanometer, the unknown resistance S must be:",
        "bn": "চিত্রে প্রদর্শিত নিস্পন্দ বা সাম্যাবস্থায় থাকা হুইটস্টোন ব্রিজ বর্তনীতে তিনটি জানা রোধের মান P = ১০ Ω, Q = ২০ Ω এবং R = ১৫ Ω। গ্যালভানোমিটারে শূন্য বিক্ষেপের জন্য অজানা রোধ S-এর মান কত হতে হবে?",
        "opts": {
            "en": ["30 Ω", "7.5 Ω", "25 Ω", "15 Ω"],
            "bn": ["30 Ω", "7.5 Ω", "25 Ω", "15 Ω"]
        },
        "correct": 0,
        "expl_en": "For a balanced Wheatstone bridge with zero galvanometer deflection: P/Q = R/S => S = R × (Q/P) = 15 × (20/10) = 15 × 2 = 30 Ω.",
        "expl_bn": "হুইটস্টোন ব্রিজের সাম্যাবস্থার শর্তানুসারে: P/Q = R/S => S = ১৫ × (২০/১০) = ৩০ Ω।"
    },
    {
        "id": "PHY-012",
        "exam": "JEE, JEE-ADV, WBJEE, IAT, NEET, IIT-JAM, GATE",
        "subject": "Physics",
        "topic": "Thermodynamics & Carnot Engine",
        "difficulty": "Medium",
        "diagram": SVG_CARNOT_CYCLE,
        "en": "A Carnot heat engine operates between source temperature T₁ = 500 K and sink temperature T₂ = 300 K. If it absorbs 600 J of heat from the high-temperature source per cycle, the work done by the engine per cycle is:",
        "bn": "একটি কার্নো ইঞ্জিন T₁ = ৫০০ K তাপমাত্রার উৎস এবং T₂ = ৩০০ K তাপমাত্রার গ্রাহকের মধ্যে কার্যকর। ইঞ্জিনটি প্রতি চক্রে উৎস থেকে ৬০০ J তাপ শোষণ করলে প্রতি চক্রে কৃতকার্যের পরিমাণ কত?",
        "opts": {
            "en": ["240 J", "360 J", "300 J", "400 J"],
            "bn": ["240 J", "360 J", "300 J", "400 J"]
        },
        "correct": 0,
        "expl_en": "Carnot efficiency η = 1 - T₂/T₁ = 1 - 300/500 = 1 - 0.6 = 0.4 (40%). Work done W = η × Q_in = 0.4 × 600 J = 240 J.",
        "expl_bn": "কার্নো ইঞ্জিনের কর্মদক্ষতা η = ১ - ৩০০/৫০০ = ০.৪ (৪০%)। প্রতি চক্রে কৃতকার্য W = ০.৪ × ৬০০ = ২৪০ জুল।"
    },

    # =========================================================================
    # 2. CHEMISTRY (High-Yield Practice Sets & Reaction Pathways)
    # =========================================================================
    {
        "id": "CHEM-001",
        "exam": "JEE, NEET, WBJEE, CUET, AIIMS, AFMC, ICAR, MHT-CET",
        "subject": "Chemistry",
        "topic": "Ionic Equilibrium",
        "difficulty": "Medium",
        "en": "During the titration of a weak acid (HA) with a strong base (NaOH), the pH of the solution at the half-equivalence point is equal to:",
        "bn": "একটি মৃদু অ্যাসিড (HA) ও তীব্র ক্ষারের (NaOH) টাইট্রেশনে অর্ধ-প্রশমন বিন্দুতে (half-equivalence point) দ্রবণের pH কত হবে?",
        "opts": {
            "en": ["pKa", "pKb", "7.0", "pKa + 1"],
            "bn": ["pKa", "pKb", "7.0", "pKa + 1"]
        },
        "correct": 0,
        "expl_en": "By Henderson-Hasselbalch equation: pH = pKa + log([A⁻]/[HA]). At the half-equivalence point, exactly half the weak acid is converted to its conjugate base, so [A⁻] = [HA], which gives log(1) = 0, hence pH = pKa.",
        "expl_bn": "হেন্ডারসন সমীকরণ অনুসারে: pH = pKa + log([A⁻]/[HA])। অর্ধ-প্রশমন বিন্দুতে [A⁻] = [HA], তাই pH = pKa।"
    },
    {
        "id": "CHEM-002",
        "exam": "JEE, JEE-ADV, WBJEE, BITSAT, IAT, NEST, IIT-JAM",
        "subject": "Chemistry",
        "topic": "Stereochemistry",
        "difficulty": "Hard",
        "en": "The total number of optical isomers possible for 1-bromo-2-methylcyclobutane is:",
        "bn": "1-bromo-2-methylcyclobutane যৌগটির জন্য সম্ভাব্য মোট আলোকীয় সমাবয়বের (optical isomers) সংখ্যা কত?",
        "opts": {
            "en": ["4", "2", "3", "6"],
            "bn": ["4", "2", "3", "6"]
        },
        "correct": 0,
        "expl_en": "1-bromo-2-methylcyclobutane has 2 asymmetric chiral carbons (C1 and C2) and lacks any plane or centre of symmetry. The number of d- and l- enantiomeric forms is 2² = 4 with 0 meso forms. Hence total optical isomers = 4.",
        "expl_bn": "যৌগটিতে ২টি কাইরাল কার্বন (C1 ও C2) রয়েছে এবং কোনো প্রতিসাম্য উপাদান নেই। তাই মোট আলোক সক্রিয় সমাবয়ব = ২² = ৪টি।"
    },
    {
        "id": "CHEM-003",
        "exam": "JEE, NEET, WBJEE, CUET, AIIMS, KCET, MHT-CET",
        "subject": "Chemistry",
        "topic": "p-Block Elements",
        "difficulty": "Medium",
        "en": "Which of the following hydride sequences correctly represents the decreasing order of boiling points?",
        "bn": "নিচের কোন ক্রমটি হাইড্রাইডসমূহের স্ফুটনাঙ্কের সঠিক অধঃক্রম প্রকাশ করে?",
        "opts": {
            "en": ["H₂O > SbH₃ > NH₃ > AsH₃ > PH₃", "H₂O > NH₃ > SbH₃ > AsH₃ > PH₃", "SbH₃ > H₂O > NH₃ > AsH₃ > PH₃", "H₂O > SbH₃ > AsH₃ > PH₃ > NH₃"],
            "bn": ["H₂O > SbH₃ > NH₃ > AsH₃ > PH₃", "H₂O > NH₃ > SbH₃ > AsH₃ > PH₃", "SbH₃ > H₂O > NH₃ > AsH₃ > PH₃", "H₂O > SbH₃ > AsH₃ > PH₃ > NH₃"]
        },
        "correct": 0,
        "expl_en": "H₂O has the highest boiling point due to extensive intermolecular hydrogen bonding. NH₃ also forms H-bonds, making its boiling point higher than PH₃ and AsH₃, while SbH₃ has higher van der Waals forces due to large molecular size. Hence: H₂O > SbH₃ > NH₃ > AsH₃ > PH₃.",
        "expl_bn": "আন্তঃআণবিক হাইড্রোজেন বন্ধনের কারণে পানির স্ফুটনাঙ্ক সর্বাধিক। সঠিক ক্রম: H₂O > SbH₃ > NH₃ > AsH₃ > PH₃।"
    },
    {
        "id": "CHEM-004",
        "exam": "JEE, NEET, WBJEE, BITSAT, VITEEE, CUET, CBSE",
        "subject": "Chemistry",
        "topic": "Carbonyl Compounds",
        "difficulty": "Easy",
        "en": "Which of the following carbonyl compounds does NOT undergo aldol condensation?",
        "bn": "নিচের কোন কার্বনিল যৌগটি অ্যালডল ঘনীভবন (Aldol Condensation) বিক্রিয়া দেয় না?",
        "opts": {
            "en": ["Chloral (CCl₃CHO)", "Acetaldehyde (CH₃CHO)", "Propanal (CH₃CH₂CHO)", "Acetone (CH₃COCH₃)"],
            "bn": ["ক্লোরাল (CCl₃CHO)", "অ্যাসিটালডিহাইড (CH₃CHO)", "প্রোপান্যাল (CH₃CH₂CHO)", "অ্যাসিটোন (CH₃COCH₃)"]
        },
        "correct": 0,
        "expl_en": "Aldol condensation requires at least one α-hydrogen atom attached to the α-carbon. Chloral (CCl₃CHO) possesses three chlorine atoms on the α-carbon and zero α-hydrogens, thus it cannot undergo aldol condensation.",
        "expl_bn": "অ্যালডল ঘনীভবনের জন্য আলফা-হাইড্রোজেনের উপস্থিতি বাধ্যতামূলক। ক্লোরালে (CCl₃CHO) কোনো আলফা হাইড্রোজেন নেই।"
    },
    {
        "id": "CHEM-005",
        "exam": "JEE, WBJEE, IAT, NEET, BITSAT, IIT-JAM",
        "subject": "Chemistry",
        "topic": "Inorganic Reaction Pathways",
        "difficulty": "Hard",
        "diagram": SVG_CHEM_REACTION_FLOW,
        "en": "Match the inorganic chemical conversions given in List I with the appropriate reagent/condition in List II:\n(A) PbO₂ + H₂SO₄ → PbSO₄ + O₂\n(B) Na₂S₂O₃ + H₂O → NaHSO₄ + S\n(C) N₂H₄ → N₂\n(D) XeF₂ → Xe",
        "bn": "তালিকা-I এর অজৈব বিক্রিয়া রূপান্তরগুলোর সাথে তালিকা-II এর সঠিক বিকারক/শর্ত মিলিয়ে সঠিক বিকল্প নির্বাচন করো:\n(A) PbO₂ + H₂SO₄ → PbSO₄ + O₂\n(B) Na₂S₂O₃ + H₂O → NaHSO₄ + S\n(C) N₂H₄ → N₂\n(D) XeF₂ → Xe",
        "opts": {
            "en": [
                "A → Warm (Δ), B → Cl₂, C → I₂, D → NO",
                "A → Cl₂, B → Warm (Δ), C → NO, D → I₂",
                "A → NO, B → I₂, C → Cl₂, D → Warm (Δ)",
                "A → Warm (Δ), B → NO, C → Cl₂, D → I₂"
            ],
            "bn": [
                "A → উত্তাপ (Δ), B → Cl₂, C → I₂, D → NO",
                "A → Cl₂, B → উত্তাপ (Δ), C → NO, D → I₂",
                "A → NO, B → I₂, C → Cl₂, D → উত্তাপ (Δ)",
                "A → উত্তাপ (Δ), B → NO, C → Cl₂, D → I₂"
            ]
        },
        "correct": 0,
        "expl_en": "(A) PbO₂ reacts with hot H₂SO₄ releasing O₂. (B) Chlorine oxidizes sodium thiosulfate to sulfate with sulfur precipitate. (C) Hydrazine reduces Iodine (I₂) to HI with liberation of N₂. (D) XeF₂ reacts with Nitric Oxide (NO) forming Xe and nitrosyl fluoride (NOF).",
        "expl_bn": "(A) PbO₂ উত্তপ্ত H₂SO₄ এর সাথে বিক্রিয়ায় O₂ গ্যাস মুক্ত করে। (B) থায়োসালফেটের দ্রবণে ক্লোরিন চালনা করলে সালফারের অধঃক্ষেপ পড়ে। (C) হাইড্রাজিন আয়োডিনকে বিজারিত করে N₂ মুক্ত করে। (D) XeF₂ এবং NO বিক্রিয়া করে Xe ও NOF গঠন করে।"
    },
    {
        "id": "CHEM-006",
        "exam": "JEE, NEET, WBJEE, CUET, AIIMS, KCET, MHT-CET",
        "subject": "Chemistry",
        "topic": "Coordination Compounds",
        "difficulty": "Medium",
        "en": "The spin-only magnetic moment (in B.M.) for high-spin tetrahedral [MnBr₄]²⁻ complex ion (Atomic number of Mn = 25) is:",
        "bn": "উচ্চ-স্পিন চতুস্তলকীয় [MnBr₄]²⁻ জটিল আয়নের (Mn এর পারমাণবিক সংখ্যা = ২৫) শুধুমাত্র স্পিন-ভিত্তিক চৌম্বক ভ্রামক (Spin-only Magnetic Moment) কত?",
        "opts": {
            "en": ["5.92 B.M.", "4.90 B.M.", "3.87 B.M.", "1.73 B.M."],
            "bn": ["5.92 B.M.", "4.90 B.M.", "3.87 B.M.", "1.73 B.M."]
        },
        "correct": 0,
        "expl_en": "Mn²⁺ has 3d⁵ electronic configuration. Since Br⁻ is a weak field ligand, it forms a high-spin tetrahedral complex with n = 5 unpaired electrons. μ = √(n(n+2)) = √(5(7)) = √35 = 5.92 B.M.",
        "expl_bn": "Mn²⁺ এর ৩d⁵ ইলেকট্রন বিন্যাস রয়েছে। Br⁻ দুর্বল লিগ্যান্ড হওয়ায় অযুগ্ম ইলেকট্রন সংখ্যা n = ৫। চৌম্বক ভ্রামক μ = √৩৫ = ৫.৯২ B.M.।"
    },
    {
        "id": "CHEM-007",
        "exam": "JEE, JEE-ADV, IAT, NEET, NEST, OLYMPIAD, IIT-JAM, CSIR-NET",
        "subject": "Chemistry",
        "topic": "Coordination Compounds & CFT",
        "difficulty": "Hard",
        "diagram": SVG_CFT_SPLITTING,
        "en": "In an octahedral crystal field, what is the Crystal Field Stabilization Energy (CFSE) in terms of Δ_o for a high-spin d⁴ transition metal ion?",
        "bn": "একটি অষ্টতলকীয় কেলাস ক্ষেত্রে (Octahedral Crystal Field), উচ্চ-স্পিন d⁴ অবস্থান্তর ধাতু আয়নের জন্য কেলাস ক্ষেত্র স্থায়িত্বায়ন শক্তি (CFSE) Δ_o-এর এককে কত হবে?",
        "opts": {
            "en": ["-0.6 Δ_o", "-1.6 Δ_o", "-0.4 Δ_o", "-1.2 Δ_o + P"],
            "bn": ["-0.6 Δ_o", "-1.6 Δ_o", "-0.4 Δ_o", "-1.2 Δ_o + P"]
        },
        "correct": 0,
        "expl_en": "In an octahedral field, the d-orbitals split into lower t₂g (-0.4 Δ_o) and higher e_g (+0.6 Δ_o). High-spin d⁴ occupies configuration t₂g³ e_g¹. CFSE = [3(-0.4) + 1(+0.6)] Δ_o = (-1.2 + 0.6) Δ_o = -0.6 Δ_o.",
        "expl_bn": "অষ্টতলকীয় ক্ষেত্রে d-অরবিটাল t₂g (-০.৪ Δ_o) এবং e_g (+০.৬ Δ_o) স্তরে বিভক্ত হয়। উচ্চ-স্পিন d⁴ এর বিন্যাস t₂g³ e_g¹। CFSE = [৩(-০.৪) + ১(+০.৬)] Δ_o = -০.৬ Δ_o।"
    },

    # =========================================================================
    # 3. BIOLOGY (NEET, AIIMS, AFMC, CUET, IAT & OLYMPIAD Practice Questions)
    # =========================================================================
    {
        "id": "BIO-001",
        "exam": "NEET, AIIMS, AFMC, CUET, IAT, OLYMPIAD, ICAR",
        "subject": "Biology",
        "topic": "Cell Biology",
        "difficulty": "Easy",
        "en": "Which of the following cell organelles is responsible for the synthesis of ribosomal RNA (rRNA)?",
        "bn": "কোষের কোন অঙ্গাণুটি রাইবোজোমাল আরএনএ (rRNA) সংশ্লেষণের জন্য দায়ী?",
        "opts": {
            "en": ["Nucleolus", "Golgi apparatus", "Lysosome", "Endoplasmic reticulum"],
            "bn": ["নিউক্লিওলাস", "গলগি বডি", "লাইসোজোম", "এন্ডোপ্লাজমিক রেটিকুলাম"]
        },
        "correct": 0,
        "expl_en": "The nucleolus is the distinct, non-membrane bound sub-nuclear structure dedicated to the transcription and processing of ribosomal RNA (rRNA) and ribosome assembly.",
        "expl_bn": "নিউক্লিওলাস হলো নিউক্লিয়াসের অভ্যন্তরে অবস্থিত প্রধান কেন্দ্র যেখানে rRNA সংশ্লেষিত হয়।"
    },
    {
        "id": "BIO-002",
        "exam": "NEET, AIIMS, AFMC, CUET, IAT, OLYMPIAD, ICAR, CSIR-NET",
        "subject": "Biology",
        "topic": "Genetics & Molecular Basis",
        "difficulty": "Medium",
        "en": "In a DNA molecule, if cytosine accounts for 18% of the total nitrogenous bases, the percentage of adenine present in that DNA is:",
        "bn": "একটি ডিএনএ অণুতে যদি সাইটোসিন ১৮% থাকে, তবে ওই ডিএনএ-তে অ্যাডেনিনের শতকরা পরিমাণ কত?",
        "opts": {
            "en": ["32%", "18%", "36%", "64%"],
            "bn": ["32%", "18%", "36%", "64%"]
        },
        "correct": 0,
        "expl_en": "According to Chargaff's rules: %G = %C = 18%. Total (G + C) = 36%. Therefore, %A + %T = 100% - 36% = 64%. Since %A = %T, %Adenine = 64% / 2 = 32%.",
        "expl_bn": "শারগাফের নিয়ম অনুসারে: %G = %C = ১৮%। অতএব %A + %T = ১০০ - ৩৬ = ৬৪%। সুতরাং %অ্যাডেনিন = ৬৪/২ = ৩২%।"
    },
    {
        "id": "BIO-003",
        "exam": "NEET, AIIMS, AFMC, CUET, IAT",
        "subject": "Biology",
        "topic": "Human Physiology",
        "difficulty": "Medium",
        "en": "Which hormone is directly responsible for stimulating the reabsorption of water from the distal convoluted tubules and collecting ducts of the nephron?",
        "bn": "নেফ্রনের দূরবর্তী সংবর্তন নালিকা ও সংগ্রাহী নালিকা থেকে পানি পুনর্শোষণ উদ্দীপিত করার জন্য কোন হরমোনটি প্রত্যক্ষভাবে দায়ী?",
        "opts": {
            "en": ["Antidiuretic Hormone (ADH / Vasopressin)", "Oxytocin", "Aldosterone", "Glucagon"],
            "bn": ["অ্যান্টিডাইইউরেটিক হরমোন (ADH / ভেসোপ্রেসিন)", "অক্সিটোসিন", "অ্যালডোস্টেরন", "গ্লুকাগন"]
        },
        "correct": 0,
        "expl_en": "Antidiuretic hormone (ADH / Vasopressin), released from the posterior pituitary, increases aquaporin channel insertion into collecting ducts to conserve body water.",
        "expl_bn": "পশ্চাৎ পিটুইটারি থেকে ক্ষরিত ADH বা ভেসোপ্রেসিন বৃক্কে পানির পুনঃশোষণ বৃদ্ধি করে।"
    },
    {
        "id": "BIO-004",
        "exam": "NEET, AIIMS, AFMC, CUET, IAT, OLYMPIAD, CSIR-NET",
        "subject": "Biology",
        "topic": "Human Health and Disease",
        "difficulty": "Hard",
        "diagram": SVG_IMMUNE_RESPONSE,
        "en": "The accompanying graph depicts antibody titer in blood serum following primary and secondary antigen exposures. Which immunoglobulin class is predominantly responsible for the rapid, high-magnitude peak observed in the secondary immune response?",
        "bn": "সংযুক্ত লেখচিত্রটিতে প্রাথমিক ও গৌণ অ্যান্টিজেন সংস্পর্শের পর সিরামে অ্যান্টিবডির মাত্রা দেখানো হয়েছে। গৌণ অনাক্রম্য সাড়ায় (Secondary response) দ্রুত ও উচ্চ মাত্রার অ্যান্টিবডি নিঃসরণের জন্য প্রধানত কোন ইমিউনোগ্লোবুলিন দায়ী?",
        "opts": {
            "en": ["IgG", "IgM", "IgE", "IgA"],
            "bn": ["IgG", "IgM", "IgE", "IgA"]
        },
        "correct": 0,
        "expl_en": "The primary immune response predominantly produces IgM with lower affinity and a lag phase. Memory B-cells generated during the primary response facilitate class switching to produce massive titers of high-affinity IgG during the secondary immune response.",
        "expl_bn": "প্রাথমিক অনাক্রম্যতায় প্রধানত IgM উৎপন্ন হয়, কিন্তু মেমরি বি-কোষের উপস্থিতির কারণে গৌণ অনাক্রম্যতায় অত্যন্ত দ্রুত ও বিপুল পরিমাণে IgG অ্যান্টিবডি ক্ষরিত হয়।"
    },
    {
        "id": "BIO-005",
        "exam": "NEET, AIIMS, AFMC, CUET, IAT, ICAR",
        "subject": "Biology",
        "topic": "Human Health and Disease",
        "difficulty": "Medium",
        "diagram": SVG_ANTIBODY_STRUCTURE,
        "en": "In the standard Y-shaped immunoglobulin monomer (H₂L₂), how many inter-chain and intra-chain disulfide bonds typically connect the heavy (H) and light (L) polypeptide chains?",
        "bn": "একটি আদর্শ Y-আকৃতির ইমিউনোগ্লোবুলিন মনোমারে (H₂L₂) ভারী (H) এবং হালকা (L) পলিপেপটাইড শৃঙ্খলগুলো প্রধানত কোন রাসায়নিক বন্ধন দ্বারা পরস্পরের সাথে আবদ্ধ থাকে?",
        "opts": {
            "en": ["Disulfide bridges (—S—S—)", "Glycosidic linkages", "Phosphodiester bonds", "Ester bonds"],
            "bn": ["ডাইসালফাইড বন্ধন (—S—S—)", "গ্লাইকোসাইডিক বন্ধন", "ফসফোডাইএস্টার বন্ধন", "এস্টার বন্ধন"]
        },
        "correct": 0,
        "expl_en": "Antibody molecules are glycoproteins composed of 2 heavy and 2 light polypeptide chains held firmly together by inter-chain covalent disulfide bridges (—S—S— bonds).",
        "expl_bn": "অ্যান্টিবডি অণুতে ২টি ভারী এবং ২টি হালকা শৃঙ্খল পরস্পরের সাথে সমযোজী ডাইসালফাইড বন্ধন (—S—S—) দ্বারা দৃঢ়ভাবে যুক্ত থাকে।"
    },
    {
        "id": "BIO-006",
        "exam": "NEET, AIIMS, AFMC, CUET, IAT, OLYMPIAD, CSIR-NET",
        "subject": "Biology",
        "topic": "Molecular Basis of Inheritance",
        "difficulty": "Medium",
        "diagram": SVG_LAC_OPERON,
        "en": "In the Lac operon of Escherichia coli, which structural gene specifically codes for the enzyme β-galactosidase that catalyzes the hydrolysis of lactose into galactose and glucose?",
        "bn": "Escherichia coli-এর ল্যাক ওপেরনে (Lac Operon), কোন গাঠনিক জিনটি সরাসরি β-গ্যালাক্টোসিডেজ উৎসেচক সংশ্লেষণ করে যা ল্যাকটোজকে গ্লুকোজ ও গ্যালাক্টোজে আর্দ্রবিশ্লেষিত করে?",
        "opts": {
            "en": ["z gene", "y gene", "a gene", "i gene"],
            "bn": ["z জিন", "y জিন", "a জিন", "i জিন"]
        },
        "correct": 0,
        "expl_en": "In the lac operon: gene 'z' codes for β-galactosidase, gene 'y' codes for β-galactoside permease, gene 'a' codes for β-galactoside transacetylase, and gene 'i' codes for the repressor protein.",
        "expl_bn": "ল্যাক ওপেরনে: 'z' জিন β-গ্যালাক্টোসিডেজ সংশ্লেষ করে, 'y' জিন পারমিয়েজ এনজাইম এবং 'a' জিন ট্রান্সঅ্যাসিটাইলেজ সংশ্লেষ করে। 'i' জিন রিপ্রেসার প্রোটিন তৈরি করে।"
    },

    # =========================================================================
    # 4. MATHEMATICS (JEE Main, Advanced, WBJEE, BITSAT, NDA & GATE Practice)
    # =========================================================================
    {
        "id": "MATH-001",
        "exam": "JEE, JEE-ADV, WBJEE, BITSAT, NDA, IAT, IIT-JAM",
        "subject": "Mathematics",
        "topic": "Combinatorics & Number Theory",
        "difficulty": "Hard",
        "en": "Let n = 2³ × 3⁴ × 5². The number of divisors of n which are of the form 4k + 2 (k ≥ 0) is:",
        "bn": "ধরি n = 2³ × 3⁴ × 5²। n-এর এমন উৎপাদকের (divisors) সংখ্যা নির্ণয় করো যা 4k + 2 (k ≥ 0) আকারের:",
        "opts": {
            "en": ["15", "18", "12", "9"],
            "bn": ["15", "18", "12", "9"]
        },
        "correct": 0,
        "expl_en": "Any divisor of the form 4k + 2 = 2(2k + 1) is an even number containing exactly one factor of 2 (i.e., 2¹) and an odd part formed by the factors of 3⁴ × 5². Number of odd factors = (4 + 1)(2 + 1) = 5 × 3 = 15. Hence, there are 15 divisors of the form 4k + 2.",
        "expl_bn": "4k + 2 = 2(2k + 1) আকারের উৎপাদক হলো বিজোড় সংখ্যাকে ২ দ্বারা গুণফল (অর্থাৎ ২-এর ঘাত ঠিক ১ হবে)। 3⁴ × 5²-এর মোট উৎপাদক সংখ্যা = (৪ + ১)(২ + ১) = ৫ × ৩ = ১৫।"
    },
    {
        "id": "MATH-002",
        "exam": "JEE, JEE-ADV, WBJEE, IAT, NEST, OLYMPIAD, IIT-JAM",
        "subject": "Mathematics",
        "topic": "Limits & Infinite Products",
        "difficulty": "Hard",
        "en": "The value of lim (n -> ∞) ∏_{r=1}^{n} (1 + 1/(r(r+2))) is equal to:",
        "bn": "lim (n -> ∞) ∏_{r=1}^{n} (1 + 1/(r(r+2))) -এর মান কত?",
        "opts": {
            "en": ["2", "3", "3/2", "4/3"],
            "bn": ["2", "3", "3/2", "4/3"]
        },
        "correct": 0,
        "expl_en": "1 + 1/(r(r+2)) = (r² + 2r + 1)/(r(r+2)) = (r+1)² / [r(r+2)] = [(r+1)/r] × [(r+1)/(r+2)]. Expanding the telescoping product from r=1 to n: P_n = (2/1 × 3/2 × ... × (n+1)/n) × (2/3 × 3/4 × ... × (n+1)/(n+2)) = (n+1) × [2/(n+2)] = 2(n+1)/(n+2). As n -> ∞, the limit is 2.",
        "expl_bn": "১ + ১/(r(r+২)) = (r+১)² / [r(r+২)] = [(r+১)/r] × [(r+১)/(r+২)]। টেলিস্কোপিং গুণফল নিলে পাওয়া যায় ২(n+১)/(n+২)। n -> ∞ হলে সীমা = ২।"
    },
    {
        "id": "MATH-003",
        "exam": "JEE, JEE-ADV, WBJEE, BITSAT, IAT, IIT-JAM",
        "subject": "Mathematics",
        "topic": "Functional Equations",
        "difficulty": "Hard",
        "en": "If f(x) is a continuous function satisfying f(x + y) = f(x) + f(y) + 3xy(x + y) for all x, y ∈ ℝ, and lim (x -> 0) f(x)/x = 2, then f(3) is equal to:",
        "bn": "যদি f(x) একটি অবিচ্ছিন্ন অপেক্ষক হয় যা f(x + y) = f(x) + f(y) + 3xy(x + y) সিদ্ধ করে এবং lim (x -> 0) f(x)/x = 2 হয়, তবে f(3) এর মান:",
        "opts": {
            "en": ["33", "27", "35", "30"],
            "bn": ["33", "27", "35", "30"]
        },
        "correct": 0,
        "expl_en": "Let g(x) = f(x) - x³. Then g(x+y) = f(x+y) - (x+y)³ = [f(x) + f(y) + 3xy(x+y)] - [x³ + y³ + 3xy(x+y)] = (f(x) - x³) + (f(y) - y³) = g(x) + g(y). Thus g(x) = kx. Given lim(x->0) f(x)/x = 2 => lim(x->0) [g(x) + x³]/x = k = 2. Hence f(x) = x³ + 2x. Therefore, f(3) = 3³ + 2(3) = 27 + 6 = 33.",
        "expl_bn": "g(x) = f(x) - x³ ধরলে g(x+y) = g(x) + g(y) পাওয়া যায়, অর্থাৎ g(x) = 2x। সুতরাং f(x) = x³ + 2x। অতএব f(3) = ৩³ + ২(৩) = ২৭ + ৬ = ৩৩।"
    },
    {
        "id": "MATH-004",
        "exam": "JEE, WBJEE, BITSAT, NDA, VITEEE, MHT-CET, KCET",
        "subject": "Mathematics",
        "topic": "Integral Calculus & Bounded Area",
        "difficulty": "Hard",
        "diagram": SVG_PARABOLAS_AREA,
        "en": "The area of the region bounded by the intersecting parabolas y = x² and y = 2x - x² is equal to:",
        "bn": "y = x² এবং y = 2x - x² পরাবৃত্ত দুটি দ্বারা সীমাবদ্ধ অঞ্চলের ক্ষেত্রফল কত?",
        "opts": {
            "en": ["1/3 sq units", "2/3 sq units", "1/6 sq units", "4/3 sq units"],
            "bn": ["1/3 বর্গ একক", "2/3 বর্গ একক", "1/6 বর্গ একক", "4/3 বর্গ একক"]
        },
        "correct": 0,
        "expl_en": "Intersection points: x² = 2x - x² => 2x² - 2x = 0 => 2x(x - 1) = 0 => x = 0 and x = 1. Area A = ∫₀¹ [(2x - x²) - x²] dx = ∫₀¹ (2x - 2x²) dx = [x² - (2/3)x³]₀¹ = 1 - 2/3 = 1/3 sq units.",
        "expl_bn": "ছেদবিন্দু: x = ০ এবং x = ১। সীমাবদ্ধ ক্ষেত্রফল A = ∫₀¹ (2x - 2x²) dx = [x² - (২/৩)x³]₀¹ = ১ - ২/৩ = ১/৩ বর্গ একক।"
    },
    {
        "id": "MATH-005",
        "exam": "JEE, WBJEE, NDA, CUET, VITEEE, MHT-CET, KCET, CBSE",
        "subject": "Mathematics",
        "topic": "Matrices & Determinants",
        "difficulty": "Medium",
        "en": "If A is a 3 × 3 non-singular matrix such that A² = 3A - 2I, then A⁻¹ is equal to:",
        "bn": "যদি A একটি ৩ × ৩ বর্গ ম্যাট্রিক্স হয় যাতে A² = 3A - 2I, তবে A⁻¹ সমান:",
        "opts": {
            "en": ["(3I - A)/2", "(A - 3I)/2", "3I + A", "2I - A"],
            "bn": ["(3I - A)/2", "(A - 3I)/2", "3I + A", "2I - A"]
        },
        "correct": 0,
        "expl_en": "Rearranging A² - 3A = -2I => 2I = 3A - A² = A(3I - A). Multiplying both sides by A⁻¹ gives 2 A⁻¹ = 3I - A => A⁻¹ = (3I - A)/2.",
        "expl_bn": "2I = 3A - A² = A(3I - A)। উভয়পক্ষে A⁻¹ গুণ করে পাওয়া যায় A⁻¹ = (3I - A)/2।"
    },
    {
        "id": "MATH-006",
        "exam": "JEE, JEE-ADV, WBJEE, BITSAT, NDA, IAT, GATE",
        "subject": "Mathematics",
        "topic": "3D Geometry & Vectors",
        "difficulty": "Hard",
        "diagram": SVG_SKEW_LINES,
        "en": "Find the shortest distance between the two skew lines given by vector equations:\nL₁: r⃗ = (i + 2j + 3k) + λ(2i + 3j + 4k)\nL₂: r⃗ = (2i + 4j + 5k) + μ(3i + 4j + 5k):",
        "bn": "ভেক্টর সমীকরণ দ্বারা প্রকাশিত দুটি বিষমতলীয় সরলরেখার (Skew lines) মধ্যবর্তী ক্ষুদ্রতম দূরত্ব নির্ণয় করো:\nL₁: r⃗ = (i + 2j + 3k) + λ(2i + 3j + 4k)\nL₂: r⃗ = (2i + 4j + 5k) + μ(3i + 4j + 5k):",
        "opts": {
            "en": ["1 / √6", "2 / √6", "1 / √3", "3 / √6"],
            "bn": ["1 / √6", "2 / √6", "1 / √3", "3 / √6"]
        },
        "correct": 0,
        "expl_en": "a⃗₂ - a⃗₁ = (2-1)i + (4-2)j + (5-3)k = i + 2j + 2k. b⃗₁ × b⃗₂ = |i j k; 2 3 4; 3 4 5| = i(15-16) - j(10-12) + k(8-9) = -i + 2j - k. Magnitude |b⃗₁ × b⃗₂| = √((-1)² + 2² + (-1)²) = √6. Dot product (a⃗₂ - a⃗₁) · (b⃗₁ × b⃗₂) = (1)(-1) + (2)(2) + (2)(-1) = -1 + 4 - 2 = 1. Shortest distance d = |(a⃗₂ - a⃗₁) · (b⃗₁ × b⃗₂)| / |b⃗₁ × b⃗₂| = 1 / √6.",
        "expl_bn": "a⃗₂ - a⃗₁ = i + 2j + 2k এবং b⃗₁ × b⃗₂ = -i + 2j - k। ডট গুণফল = ১। অতএব ক্ষুদ্রতম দূরত্ব d = ১ / √৬।"
    },

    # =========================================================================
    # =========================================================================
    # 5. GENERAL SCIENCE (UPSC, SSC, RRB, PSC, NDA, CDS)
    # =========================================================================
    {
        "id": "SCI-001",
        "exam": "UPSC, SSC, RRB, NDA, CDS, STATE-PSC, BANKING",
        "subject": "General Science",
        "topic": "Physics in Daily Life & Atmospheric Optics",
        "difficulty": "Easy",
        "en": "Why does the clear daytime sky appear predominantly blue to an observer on Earth?",
        "bn": "দিনের বেলায় পরিষ্কার আকাশ কেন প্রধানত নীল দেখায়?",
        "opts": {
            "en": [
                "Rayleigh scattering of shorter wavelengths (blue light) by atmospheric molecules",
                "Total internal reflection of solar radiation in water droplets",
                "Selective absorption of red light by nitrogen gas",
                "Diffraction of light by cloud particles"
            ],
            "bn": [
                "বায়ুমণ্ডলের গ্যাসীয় অণু দ্বারা নীল আলোর রেলি বিক্ষেপণ (Rayleigh Scattering)",
                "মেঘের মধ্যে আলোর পূর্ণ অভ্যন্তরীণ প্রতিফলন",
                "নাইট্রোজেন গ্যাস দ্বারা লাল আলোর শোষণ",
                "ধূলিকণা দ্বারা আলোর অপবর্তন"
            ]
        },
        "correct": 0,
        "expl_en": "According to Rayleigh scattering law, the intensity of scattered light is inversely proportional to the fourth power of wavelength (I ∝ 1/λ⁴). Shorter blue wavelengths are scattered roughly 10 times more effectively than longer red wavelengths.",
        "expl_bn": "রেলির বিক্ষেপণ নীতি অনুযায়ী বিক্ষেপণের তীব্রতা I ∝ ১/λ⁴। ক্ষুদ্র তরঙ্গদৈর্ঘ্যের নীল আলো বায়ুমণ্ডলের অণুসমূহ দ্বারা লাল আলোর চেয়ে প্রায় ১০ গুণ বেশি বিক্ষিপ্ত হয়।"
    },
    {
        "id": "SCI-002",
        "exam": "UPSC, SSC, RRB, NDA, CDS, STATE-PSC, BANKING",
        "subject": "General Science",
        "topic": "Chemical Substances in Daily Life",
        "difficulty": "Easy",
        "en": "Which chemical compound is commonly used in food preservation to prevent microbial spoilage in acidic foods like tomato ketchup, pickles, and fruit juices?",
        "bn": "টমেটো সস, আচার এবং ফলের রসের মতো অম্লীয় খাদ্যে জীবাণু সংক্রমণ রোধ করতে প্রিজারভেটিভ হিসেবে সাধারণত কোন রাসায়নিক যৌগটি ব্যবহৃত হয়?",
        "opts": {
            "en": ["Sodium benzoate", "Sodium chloride", "Calcium carbide", "Potassium chlorate"],
            "bn": ["সোডিয়াম বেনজোয়েট", "সোডিয়াম ক্লোরাইড", "ক্যালসিয়াম কার্বাইড", "পটাশিয়াম ক্লোরেট"]
        },
        "correct": 0,
        "expl_en": "Sodium benzoate (C₆H₅COONa) is widely utilized as a food preservative (E211). In acidic media (pH < 4.5), it converts to undissociated benzoic acid which inhibits mold and yeast growth.",
        "expl_bn": "সোডিয়াম বেনজোয়েট হলো বহুল ব্যবহৃত একটি খাদ্য সংরক্ষক যা অম্লীয় মাধ্যমে বেনজোয়িক অ্যাসিডে রূপান্তরিত হয়ে অণুজীবের বৃদ্ধি প্রতিরোধ করে।"
    },
    {
        "id": "SCI-003",
        "exam": "UPSC, SSC, RRB, NDA, CDS, STATE-PSC, AFCAT, CAPF",
        "subject": "General Science",
        "topic": "Space Technology & ISRO",
        "difficulty": "Medium",
        "en": "Which launch vehicle was utilized by the Indian Space Research Organisation (ISRO) to successfully inject Chandrayaan-3 into its intended translunar trajectory?",
        "bn": "ভারতীয় মহাকাশ গবেষণা সংস্থা (ISRO) কোন উৎক্ষেপণ যানের (Launch Vehicle) সাহায্যে চন্দ্রযান-৩ কে সফলভাবে চাঁদের কক্ষপথের অভিমুখে প্রেরণ করেছিল?",
        "opts": {
            "en": ["LVM3 (GSLV Mk-III)", "PSLV-C56", "SSLV-D2", "GSLV-F12"],
            "bn": ["LVM3 (GSLV Mk-III)", "PSLV-C56", "SSLV-D2", "GSLV-F12"]
        },
        "correct": 0,
        "expl_en": "ISRO launched Chandrayaan-3 using the Launch Vehicle Mark-3 (LVM3-M4) heavy-lift rocket from Satish Dhawan Space Centre, Sriharikota.",
        "expl_bn": "চন্দ্রযান-৩ মিশনটি ISRO-এর ভারী উৎক্ষেপণ যান LVM3 (GSLV Mk-III)-এর সাহায্যে শ্রীহরিকোটা থেকে সফলভাবে উৎক্ষেপিত হয়েছিল।"
    },
    {
        "id": "SCI-004",
        "exam": "UPSC, SSC, CDS, STATE-PSC, CUET, NDA, CAPF",
        "subject": "General Science",
        "topic": "Environmental Science & Ecology",
        "difficulty": "Easy",
        "en": "The landmark international environmental treaty known as the Montreal Protocol (1987) was established to regulate and phase out substances that cause:",
        "bn": "ঐতিহাসিক আন্তর্জাতিক পরিবেশ চুক্তি 'মন্ট্রিল প্রোটোকল' (১৯৮৭) কোন ক্ষতিকর প্রক্রিয়া নিয়ন্ত্রণের উদ্দেশ্যে সাক্ষরিত হয়েছিল?",
        "opts": {
            "en": ["Depletion of the stratospheric ozone layer", "Global ocean acidification", "Eutrophication of freshwaters", "Radioactive nuclear fallout"],
            "bn": ["স্ট্র্যাটোস্ফিয়ারের ওজোন স্তরের ক্ষয়রোধ", "মহাসাগরের অম্লতাকরণ", "জলাশয়ের ইউট্রোফিকেশন", "তেজস্ক্রিয় নিউক্লীয় বর্জ্য"]
        },
        "correct": 0,
        "expl_en": "The Montreal Protocol on Substances that Deplete the Ozone Layer is an international environmental treaty designed to phase out the production of ozone-depleting substances (ODSs) such as Chlorofluorocarbons (CFCs).",
        "expl_bn": "মন্ট্রিল প্রোটোকল হলো বায়ুমণ্ডলের স্ট্র্যাটোস্ফিয়ারে ওজোন স্তরের ক্ষয় সৃষ্টিকারী ক্লোরোফ্লুরোকার্বন (CFC) ও অন্যান্য পদার্থ নিষিদ্ধ করার লক্ষ্যে সাক্ষরিত একটি বৈশ্বিক চুক্তি।"
    },

    # =========================================================================
    # 6. ENGLISH LANGUAGE & VERBAL ABILITY
    # =========================================================================
    {
        "id": "ENG-001",
        "exam": "BITSAT, VITEEE, CUET, NDA, CDS, AFCAT, SSC, BANKING, STATE-PSC, AFMC",
        "subject": "English",
        "topic": "Grammar & Error Spotting",
        "difficulty": "Medium",
        "en": "Identify the grammatically correct sentence among the following options:",
        "bn": "নিচের বিকল্পগুলোর মধ্যে ব্যাকরণগতভাবে সঠিক বাক্যটি নির্বাচন করো:",
        "opts": {
            "en": [
                "Neither the teacher nor the students were present in the laboratory.",
                "Neither the teacher nor the students was present in the laboratory.",
                "Neither the teacher or the students were present in the laboratory.",
                "Neither the teacher nor the students is present in the laboratory."
            ],
            "bn": [
                "Neither the teacher nor the students were present in the laboratory.",
                "Neither the teacher nor the students was present in the laboratory.",
                "Neither the teacher or the students were present in the laboratory.",
                "Neither the teacher nor the students is present in the laboratory."
            ]
        },
        "correct": 0,
        "expl_en": "When subjects are joined by 'neither... nor', the verb agrees with the subject closest to it (proximity rule). Since 'students' is plural and in the past tense, the plural verb 'were' is correct.",
        "expl_bn": "'Neither... nor' দ্বারা একাধিক কর্তা যুক্ত হলে নিকটবর্তী কর্তা অনুসারে ক্রিয়া নির্ধারিত হয়। এখানে নিকটবর্তী কর্তা 'students' বহুবচন হওয়ায় 'were' সঠিক।"
    },
    {
        "id": "ENG-002",
        "exam": "BITSAT, VITEEE, CUET, NDA, CDS, SSC, BANKING, UPSC, STATE-PSC",
        "subject": "English",
        "topic": "Vocabulary & Antonyms",
        "difficulty": "Easy",
        "en": "Choose the word that is most nearly OPPOSITE in meaning to the word 'TRANSIENT':",
        "bn": "'TRANSIENT' (ক্ষণস্থায়ী) শব্দটির সবচেয়ে নিকটবর্তী বিপরীতার্থক (Opposite) শব্দটি নির্বাচন করো:",
        "opts": {
            "en": ["Permanent", "Ephemeral", "Fleeting", "Temporal"],
            "bn": ["Permanent (স্থায়ী)", "Ephemeral (ক্ষণস্থায়ী)", "Fleeting (দ্রুত পলায়নপর)", "Temporal (লৌকিক/ক্ষণস্থায়ী)"]
        },
        "correct": 0,
        "expl_en": "'Transient' means lasting only for a short time (impermanent). Its direct antonym is 'Permanent' (lasting or intended to last indefinitely).",
        "expl_bn": "'Transient' শব্দের অর্থ ক্ষণস্থায়ী। এর সঠিক বিপরীতার্থক শব্দ হলো 'Permanent' (চিরস্থায়ী বা দীর্ঘস্থায়ী)।"
    },
    {
        "id": "ENG-003",
        "exam": "BITSAT, VITEEE, CUET, NDA, CDS, AFCAT, SSC, BANKING, STATE-PSC",
        "subject": "English",
        "topic": "Idioms & Phrasal Usage",
        "difficulty": "Medium",
        "en": "What is the accurate meaning of the idiomatic phrase 'To read between the lines'?",
        "bn": "'To read between the lines' প্রবাদবাক্যটির প্রকৃত অর্থ কী?",
        "opts": {
            "en": [
                "To discover an underlying or hidden meaning not explicitly stated",
                "To read very fast skipping alternating lines",
                "To criticize the grammatical style of an author",
                "To re-read a book after a long gap"
            ],
            "bn": [
                "To discover an underlying or hidden meaning not explicitly stated",
                "To read very fast skipping alternating lines",
                "To criticize the grammatical style of an author",
                "To re-read a book after a long gap"
            ]
        },
        "correct": 0,
        "expl_en": "'To read between the lines' means to perceive or detect an unexpressed, subtle, or hidden meaning behind explicit words.",
        "expl_bn": "'To read between the lines' কথাটির অর্থ হলো কোনো লেখার স্পষ্ট বা প্রত্যক্ষ অর্থের আড়ালে থাকা অন্তর্নিহিত বা গোপন ভাবার্থ উপলব্ধি করা।"
    },

    # =========================================================================
    # 7. LOGICAL REASONING & GENERAL MENTAL ABILITY
    # =========================================================================
    {
        "id": "REA-001",
        "exam": "BITSAT, VITEEE, CUET, AFCAT, SSC, RRB, BANKING, UPSC, STATE-PSC, FOUNDATION",
        "subject": "Reasoning",
        "topic": "Syllogism & Deductive Logic",
        "difficulty": "Medium",
        "en": "Analyze the statements and conclusions:\nStatements:\n1. All scientists are researchers.\n2. Some researchers are teachers.\nConclusions:\nI. Some researchers are scientists.\nII. Some teachers are researchers.\nWhich of the following holds true?",
        "bn": "বিবৃতি ও উপসংহার বিশ্লেষণ করো:\nবিবৃতি:\n১. সকল বিজ্ঞানী হলেন গবেষক।\n২. কিছু গবেষক হলেন শিক্ষক।\nউপসংহার:\nI. কিছু গবেষক হলেন বিজ্ঞানী।\nII. কিছু শিক্ষক হলেন গবেষক।\nনিচের কোন বিকল্পটি সত্য?",
        "opts": {
            "en": [
                "Both conclusions I and II follow",
                "Only conclusion I follows",
                "Only conclusion II follows",
                "Neither conclusion follows"
            ],
            "bn": [
                "উভয় উপসংহার I এবং II সঠিক",
                "কেবলমাত্র উপসংহার I সঠিক",
                "কেবলমাত্র উপসংহার II সঠিক",
                "কোনো উপসংহারই সঠিক নয়"
            ]
        },
        "correct": 0,
        "expl_en": "Statement 1: 'All scientists are researchers' logically converts to 'Some researchers are scientists' (Conclusion I is valid). Statement 2: 'Some researchers are teachers' directly converts to 'Some teachers are researchers' (Conclusion II is valid). Hence, both follow.",
        "expl_bn": "বিবৃতি ১ রূপান্তর করলে পাওয়া যায় 'কিছু গবেষক হলেন বিজ্ঞানী' (উপসংহার I সঠিক)। বিবৃতি ২ রূপান্তর করলে পাওয়া যায় 'কিছু শিক্ষক হলেন গবেষক' (উপসংহার II সঠিক)। অতএব উভয় উপসংহারই প্রযোজ্য।"
    },
    {
        "id": "REA-002",
        "exam": "BITSAT, VITEEE, CUET, AFCAT, SSC, RRB, BANKING, UPSC, STATE-PSC, FOUNDATION",
        "subject": "Reasoning",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "en": "In a certain code language, if 'SYSTEM' is coded as 'SYSMET' and 'NEARER' is coded as 'AENRER', how will 'FRACTION' be coded in that same language?",
        "bn": "একটি সাংকেতিক ভাষায় যদি 'SYSTEM' কে লেখা হয় 'SYSMET' এবং 'NEARER' কে লেখা হয় 'AENRER', তবে একই নিয়মে 'FRACTION' কে কীভাবে লেখা হবে?",
        "opts": {
            "en": ["CARFNOIT", "ARFCNOIT", "CARFTION", "CRAFNOIT"],
            "bn": ["CARFNOIT", "ARFCNOIT", "CARFTION", "CRAFNOIT"]
        },
        "correct": 0,
        "expl_en": "The 8-letter word is split into two halves of 4 letters: 'FRAC' and 'TION'. Reversing each 4-letter block gives 'CARF' and 'NOIT'. Combining them yields 'CARFNOIT'.",
        "expl_bn": "শব্দটিকে দুটি সমান অংশে (প্রতিটিতে ৪টি বর্ণ) ভাগ করা হয়েছে: 'FRAC' এবং 'TION'। প্রতিটি অংশকে উল্টো করে লিখলে পাওয়া যায় 'CARF' এবং 'NOIT', যার সমন্বয়ে গঠিত হয় 'CARFNOIT'।"
    },
    {
        "id": "REA-003",
        "exam": "BITSAT, VITEEE, CUET, NDA, CDS, AFCAT, SSC, RRB, BANKING, UPSC, STATE-PSC, FOUNDATION",
        "subject": "Reasoning",
        "topic": "Direction & Distance Sense",
        "difficulty": "Easy",
        "en": "A student walks 12 km towards North, then turns right and walks 5 km. What is the shortest displacement and direction of the student relative to the starting point?",
        "bn": "একজন শিক্ষার্থী উত্তর দিকে ১২ কিমি হেঁটে গিয়ে ডানদিকে মোড় নিয়ে ৫ কিমি হাঁটলেন। প্রারম্ভিক বিন্দুর সাপেক্ষে শিক্ষার্থীর ন্যূনতম সরণ এবং অভিমুখ কী?",
        "opts": {
            "en": ["13 km, North-East", "17 km, North", "13 km, North-West", "7 km, East"],
            "bn": ["13 km, উত্তর-পূর্ব", "17 km, উত্তর", "13 km, উত্তর-পশ্চিম", "7 km, পূর্ব"]
        },
        "correct": 0,
        "expl_en": "By Pythagoras theorem: Shortest displacement d = √(12² + 5²) = √(144 + 25) = √169 = 13 km. The direction from the origin (0,0) to (+5, +12) is North-East.",
        "expl_bn": "পিথাগোরাসের উপপাদ্য অনুসারে: ন্যূনতম সরণ d = √(১২² + ৫²) = √১৬৯ = ১৩ কিমি। প্রারম্ভিক বিন্দুর সাপেক্ষে অভিমুখ হলো উত্তর-পূর্ব।"
    },

    # =========================================================================
    # 8. HISTORY (Indian National Movement, Ancient & Medieval)
    # =========================================================================
    {
        "id": "HIST-001",
        "exam": "UPSC, STATE-PSC, SSC, CDS, NDA, CUET, RRB",
        "subject": "History",
        "topic": "Indian National Movement",
        "difficulty": "Medium",
        "en": "In which historic session of the Indian National Congress was the resolution for 'Poorna Swaraj' (Complete Independence) officially adopted under the presidency of Jawaharlal Nehru?",
        "bn": "জওহরলাল নেহরুর সভাপতিত্বে ভারতীয় জাতীয় কংগ্রেসের কোন ঐতিহাসিক অধিবেশনে 'পূর্ণ স্বরাজ' (সম্পূর্ণ স্বাধীনতা)-এর প্রস্তাব আনুষ্ঠানিকভাবে গৃহীত হয়েছিল?",
        "opts": {
            "en": [
                "Lahore Session (1929)",
                "Belgaum Session (1924)",
                "Karachi Session (1931)",
                "Tripuri Session (1939)"
            ],
            "bn": [
                "লাহোর অধিবেশন (১৯২৯)",
                "বেলগাঁও অধিবেশন (১৯২৪)",
                "করাচি অধিবেশন (১৯৩১)",
                "ত্রিপুরী অধিবেশন (১৯৩৯)"
            ]
        },
        "correct": 0,
        "expl_en": "At the Lahore Session of the Indian National Congress in December 1929, under the presidency of Jawaharlal Nehru, the historic 'Poorna Swaraj' resolution was adopted, declaring 26 January 1930 as the first Independence Day.",
        "expl_bn": "১৯২৯ সালের ডিসেম্বরে লাহোর অধিবেশনে জওহরলাল নেহরুর সভাপতিত্বে পূর্ণ স্বরাজ প্রস্তাব গৃহীত হয় এবং ২৬ জানুয়ারি ১৯৩০ কে প্রথম স্বাধীনতা দিবস হিসেবে উদযাপনের ঘোষণা দেওয়া হয়।"
    },
    {
        "id": "HIST-002",
        "exam": "UPSC, STATE-PSC, SSC, CDS, NDA, CUET, RRB",
        "subject": "History",
        "topic": "Ancient India & Harappan Civilization",
        "difficulty": "Easy",
        "en": "At which of the following Harappan archaeological sites was a prominent tidal dockyard (naval port basin) discovered by archaeologists?",
        "bn": "হরপ্পা সভ্যতার নিচের কোন প্রত্নতাত্ত্বিক নিদর্শনস্থলে একটি কৃত্রিম পোতাশ্রয় বা ডকইয়ার্ড আবিষ্কৃত হয়েছিল?",
        "opts": {
            "en": ["Lothal", "Kalibangan", "Rakhigarhi", "Banawali"],
            "bn": ["লোথাল", "কালিবঙ্গান", "রাখিগড়ি", "বনওয়ালি"]
        },
        "correct": 0,
        "expl_en": "Lothal in Gujarat (excavated by S.R. Rao) featured a massive brick-built tidal dockyard connected to the Gulf of Khambhat via the Bhogavo river, serving as an ancient maritime trading hub.",
        "expl_bn": "গুজরাটের লোথালে সিন্ধু সভ্যতার বিখ্যাত সামুদ্রিক পোতাশ্রয় (ডকইয়ার্ড) আবিষ্কৃত হয় যা প্রাচীনকালে মেসোপটেমিয়ার সাথে বাণিজ্যের প্রধান বন্দর ছিল।"
    },

    # =========================================================================
    # 9. GEOGRAPHY (Physical, Climate & Indian Geography)
    # =========================================================================
    {
        "id": "GEOG-001",
        "exam": "UPSC, STATE-PSC, SSC, CDS, NDA, CUET, RRB",
        "subject": "Geography",
        "topic": "Drainage System of India",
        "difficulty": "Medium",
        "en": "Which of the following major Indian rivers flows westwards through a tectonic rift valley between the Vindhya and Satpura mountain ranges into the Arabian Sea?",
        "bn": "নিচের কোন প্রধান ভারতীয় নদীটি বিন্ধ্য ও সাতপুরা পর্বতমালার মধ্যবর্তী গ্রস্ত উপত্যকার (Rift Valley) মধ্য দিয়ে পশ্চিমবাহিনী হয়ে আরব সাগরে পতিত হয়েছে?",
        "opts": {
            "en": ["Narmada", "Godavari", "Mahanadi", "Krishna"],
            "bn": ["নর্মদা", "গোদাবরী", "মহানদী", "কৃষ্ণা"]
        },
        "correct": 0,
        "expl_en": "The Narmada river originates at Amarkantak and flows westward through a tectonic rift valley bounded by the Vindhyas to the north and Satpuras to the south before emptying into the Arabian Sea.",
        "expl_bn": "নর্মদা নদী বিন্ধ্য ও সাতপুরা পর্বতের মধ্যবর্তী চ্যুতি বা গ্রস্ত উপত্যকা দিয়ে প্রবাহিত হয়ে পশ্চিমবাহিনী হয়ে আরব সাগরে পতিত হয়েছে।"
    },
    {
        "id": "GEOG-002",
        "exam": "UPSC, STATE-PSC, SSC, CDS, NDA, CUET, RRB",
        "subject": "Geography",
        "topic": "Atmosphere & Climatology",
        "difficulty": "Easy",
        "en": "In which atmospheric layer does almost all operational weather phenomena (clouds, rainfall, fog, and convection) take place on Earth?",
        "bn": "পৃথিবীর বায়ুমণ্ডলের কোন স্তরে মেঘ, বৃষ্টিপাত, কুয়াশা এবং পরিচলন সহ বায়ুমণ্ডলীয় আবহাওয়া সংক্রান্ত প্রায় সকল প্রধান ঘটনা সংঘটিত হয়?",
        "opts": {
            "en": ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"],
            "bn": ["ট্রপোস্ফিয়ার", "স্ট্র্যাটোস্ফিয়ার", "মেসোস্ফিয়ার", "থার্মোস্ফিয়ার"]
        },
        "correct": 0,
        "expl_en": "The troposphere is the lowest atmospheric layer containing ~75% of atmospheric mass and 99% of total water vapor. All active weather phenomena occur exclusively here.",
        "expl_bn": "বায়ুমণ্ডলের সর্বনিম্ন স্তর ট্রপোস্ফিয়ারে জলীয় বাষ্প ও বায়ুর ঘনত্বের আধিক্যের কারণে মেঘ, বৃষ্টি, ঝড় ইত্যাদি যাবতীয় আবহাওয়া সংক্রান্ত পরিবর্তন ঘটে।"
    },

    # =========================================================================
    # 10. POLITICAL SCIENCE & INDIAN POLITY
    # =========================================================================
    {
        "id": "POL-001",
        "exam": "UPSC, STATE-PSC, SSC, CDS, NDA, CUET, RRB",
        "subject": "Political Science",
        "topic": "Fundamental Rights & Judicial Remedies",
        "difficulty": "Medium",
        "en": "Which Article of the Constitution of India empowers the Supreme Court to issue writs (including Habeas Corpus, Mandamus, Prohibition, Quo-Warranto, and Certiorari) for the enforcement of Fundamental Rights?",
        "bn": "ভারতের সংবিধানের কোন অনুচ্ছেদ অনুযায়ী নাগরিকদের মৌলিক অধিকার বলবৎ করার জন্য সুপ্রিম কোর্ট লেখ বা রিট (Habeas Corpus, Mandamus ইত্যাদি) জারি করতে পারে?",
        "opts": {
            "en": ["Article 32", "Article 226", "Article 14", "Article 21"],
            "bn": ["অনুচ্ছেদ ৩২", "অনুচ্ছেদ ২২৬", "অনুচ্ছেদ ১৪", "অনুচ্ছেদ ২১"]
        },
        "correct": 0,
        "expl_en": "Article 32 provides the Right to Constitutional Remedies and empowers the Supreme Court to issue prerogative writs. Dr. B.R. Ambedkar famously called Article 32 the 'Heart and Soul of the Indian Constitution'.",
        "expl_bn": "ভারতের সংবিধানের ৩২ নম্বর অনুচ্ছেদ মৌলিক অধিকার সুরক্ষায় সুপ্রিম কোর্টকে রিট জারির ক্ষমতা প্রদান করে। ড. বি. আর. আম্বেদকর একে সংবিধানের 'হৃদয় ও আত্মা' আখ্যা দিয়েছিলেন।"
    },
    {
        "id": "POL-002",
        "exam": "UPSC, STATE-PSC, SSC, CDS, NDA, CUET, RRB",
        "subject": "Political Science",
        "topic": "Preamble & Amendments",
        "difficulty": "Easy",
        "en": "By which Constitutional Amendment Act were the words 'SOCIALIST', 'SECULAR', and 'INTEGRITY' inserted into the Preamble of the Constitution of India?",
        "bn": "কোন সংবিধান সংশোধন আইনের মাধ্যমে ভারতের সংবিধানের প্রস্তাবনায় (Preamble) 'সমাজতান্ত্রিক' (Socialist), 'ধর্মনিরপেক্ষ' (Secular) এবং 'সংহতি' (Integrity) শব্দগুলো যুক্ত করা হয়েছিল?",
        "opts": {
            "en": [
                "42nd Constitutional Amendment Act (1976)",
                "44th Constitutional Amendment Act (1978)",
                "73rd Constitutional Amendment Act (1992)",
                "86th Constitutional Amendment Act (2002)"
            ],
            "bn": [
                "৪২তম সংবিধান সংশোধনী আইন (১৯৭৬)",
                "৪৪তম সংবিধান সংশোধনী আইন (১৯৭৮)",
                "৭৩তম সংবিধান সংশোধনী আইন (১৯৯২)",
                "৮৬তম সংবিধান সংশোধনী আইন (২০০২)"
            ]
        },
        "correct": 0,
        "expl_en": "The 42nd Constitutional Amendment Act of 1976 amended the Preamble for the first and only time, introducing the terms 'Socialist', 'Secular', and 'Integrity'.",
        "expl_bn": "১৯৭৬ সালের ৪২তম সংবিধান সংশোধনী আইনের মাধ্যমে ভারতের সংবিধানের প্রস্তাবনায় প্রথম ও একমাত্র বার সংশোধন এনে 'সমাজতান্ত্রিক', 'ধর্মনিরপেক্ষ' এবং 'সংহতি' শব্দগুলো সংযোজন করা হয়।"
    },

    # =========================================================================
    # 11. GENERAL KNOWLEDGE & STATIC AWARENESS
    # =========================================================================
    {
        "id": "GK-001",
        "exam": "UPSC, SSC, CDS, NDA, CUET, BANKING, RRB, STATE-PSC",
        "subject": "General Knowledge",
        "topic": "International Organizations & Headquarters",
        "difficulty": "Easy",
        "diagram": SVG_ICJ_EMBLEM,
        "en": "The International Court of Justice (ICJ), the principal judicial organ of the United Nations, has its permanent seat located at:",
        "bn": "সম্মিলিত রাষ্ট্রপুঞ্জের (UN) প্রধান বিচার বিভাগীয় অঙ্গ আন্তর্জাতিক বিচারালয় (ICJ)-এর স্থায়ী সদর দপ্তর কোথায় অবস্থিত?",
        "opts": {
            "en": [
                "The Hague (Peace Palace), Netherlands",
                "Geneva, Switzerland",
                "New York, USA",
                "Vienna, Austria"
            ],
            "bn": [
                "দ্য হেগ (পিস প্যালেস), নেদারল্যান্ডস",
                "জেনেভা, সুইজারল্যান্ড",
                "নিউ ইয়র্ক, মার্কিন যুক্তরাষ্ট্র",
                "ভিয়েনা, অস্ট্রিয়া"
            ]
        },
        "correct": 0,
        "expl_en": "The International Court of Justice (ICJ) was established in 1945 by the UN Charter and is situated at the Peace Palace in The Hague, Netherlands. It is the only one of the six principal UN organs not located in New York City.",
        "expl_bn": "আন্তর্জাতিক বিচারালয় (ICJ) ১৯৪৫ সালে প্রতিষ্ঠিত হয় এবং এটি নেদারল্যান্ডসের দ্য হেগ শহরের পিস প্যালেসে অবস্থিত। এটি রাষ্ট্রপুঞ্জের একমাত্র প্রধান অঙ্গ যা নিউ ইয়র্কে অবস্থিত নয়।"
    },
    {
        "id": "GK-002",
        "exam": "UPSC, SSC, CDS, NDA, CUET, RRB, STATE-PSC",
        "subject": "General Knowledge",
        "topic": "Science & Space Milestones of India",
        "difficulty": "Medium",
        "en": "India became the first Asian nation to successfully reach Martian orbit in its maiden attempt. Which launch vehicle carried ISRO's Mars Orbiter Mission (Mangalyaan) into Earth parking orbit on 5th November 2013?",
        "bn": "ভারত প্রথম এশীয় দেশ হিসেবে প্রথম প্রচেষ্টাতেই সফলভাবে মঙ্গল গ্রহের কক্ষপথে পৌঁছায়। ২০১৩ সালের ৫ই নভেম্বর কোন উৎক্ষেপণ যানের মাধ্যমে ইসরোর মার্স অরবিটার মিশন (মঙ্গলযান) উৎক্ষেপণ করা হয়েছিল?",
        "opts": {
            "en": [
                "PSLV-C25 (XL Variant)",
                "GSLV Mk III (LVM3)",
                "PSLV-C11",
                "GSLV-D5"
            ],
            "bn": [
                "PSLV-C25 (XL ভ্যারিয়েন্ট)",
                "GSLV Mk III (LVM3)",
                "PSLV-C11",
                "GSLV-D5"
            ]
        },
        "correct": 0,
        "expl_en": "ISRO's Mars Orbiter Mission (Mangalyaan) was launched aboard the Polar Satellite Launch Vehicle (PSLV-C25) in its 'XL' configuration on 5 November 2013 from the Satish Dhawan Space Centre (SDSC) SHAR, Sriharikota.",
        "expl_bn": "ইসরোর মার্স অরবিটার মিশন (মঙ্গলযান) ২০১৩ সালের ৫ই নভেম্বর অন্ধ্রপ্রদেশের শ্রীহরিকোটার সতীশ ধাওয়ান মহাকাশ কেন্দ্র থেকে PSLV-C25 (XL) রকেটের মাধ্যমে সফলভাবে উৎক্ষেপণ করা হয়।"
    }    ,
    # =========================================================================
    # PHYSICS (Newly Sorted High-Yield Questions)
    # =========================================================================
    {
        "id": "PHY-013",
        "exam": "NEET, JEE, WBJEE, CUET, BITSAT, VITEEE",
        "subject": "Physics",
        "topic": "Magnetic Effects of Current & Dipole Moment",
        "difficulty": "Medium",
        "diagram": SVG_COIL_MAGNETIC_MOMENT,
        "en": "A 100-turn closely wound circular coil of radius 5 cm carries a steady current such that the magnetic field at its centre is 3.14 × 10⁻³ T. Taking μ₀ = 4π × 10⁻⁷ T·m/A, the electric current flowing through the coil and the magnitude of the magnetic dipole moment of the coil are respectively:",
        "bn": "৫ সেমি ব্যাসার্ধের একটি ১০০ পাকের নিবিড়ভাবে জড়ানো বৃত্তাকার কুণ্ডলীর কেন্দ্রে চৌম্বক ক্ষেত্র ৩.১৪ × ১০⁻³ T। μ₀ = ৪π × ১০⁻⁷ T·m/A ধরে, কুণ্ডলীর মধ্য দিয়ে প্রবাহিত তড়িৎপ্রবাহ এবং কুণ্ডলীটির চৌম্বক দ্বিমেরু ভ্রামকের মান যথাক্রমে কত?",
        "opts": {
            "en": ["2.5 A and 2.0 A·m²", "2.5 A and 20.0 A·m²", "2.0 A and 4.0 A·m²", "2.0 A and 10.0 A·m²"],
            "bn": ["2.5 A এবং 2.0 A·m²", "2.5 A এবং 20.0 A·m²", "2.0 A এবং 4.0 A·m²", "2.0 A এবং 10.0 A·m²"]
        },
        "correct": 0,
        "expl_en": "Magnetic field at centre: B = (μ₀ N I)/(2R) => I = (2 R B)/(μ₀ N) = (2 × 0.05 × 3.14 × 10⁻³)/(4π × 10⁻⁷ × 100) = 2.5 A. Magnetic moment: M = N I (π R²) = 100 × 2.5 × π × (0.05)² ≈ 1.963 A·m² ≈ 2.0 A·m².",
        "expl_bn": "কুণ্ডলীর কেন্দ্রে চৌম্বক ক্ষেত্র: B = (μ₀ N I)/(2R) => I = (২ × ০.০৫ × ৩.১৪ × ১০⁻³)/(৪π × ১০⁻⁷ × ১০০) = ২.৫ A। চৌম্বক ভ্রামক: M = N I (π R²) = ১০০ × ২.৫ × π × (০.০৫)² ≈ ১.৯৬৩ A·m² ≈ ২.০ A·m²।"
    },
    {
        "id": "PHY-014",
        "exam": "JEE, WBJEE, NEET, CUET, MHT-CET, KCET, BITSAT",
        "subject": "Physics",
        "topic": "Current Electricity & Conductivity",
        "difficulty": "Medium",
        "diagram": SVG_TWO_CONDUCTORS_SERIES,
        "en": "Two metal rods of identical length L and cross-sectional area A have electrical conductivities σ₁ and σ₂ respectively. When they are joined end-to-end in series, the effective electrical conductivity (σ_eq) of the combination is:",
        "bn": "সমান দৈর্ঘ্য L এবং সমান প্রস্থচ্ছেদ A বিশিষ্ট দুটি ধাতব দণ্ডের তড়িৎ পরিবাহিতা যথাক্রমে σ₁ এবং σ₂। এদের শ্রেণি সমবায়ে যুক্ত করা হলে সমবায়টির কার্যকর তড়িৎ পরিবাহিতা (σ_eq) কত হবে?",
        "opts": {
            "en": ["(2σ₁σ₂) / (σ₁ + σ₂)", "(σ₁ + σ₂) / 2", "√(σ₁σ₂)", "(σ₁σ₂) / (2(σ₁ + σ₂))"],
            "bn": ["(2σ₁σ₂) / (σ₁ + σ₂)", "(σ₁ + σ₂) / 2", "√(σ₁σ₂)", "(σ₁σ₂) / (2(σ₁ + σ₂))"]
        },
        "correct": 0,
        "expl_en": "Total length = 2L, area = A. In series, equivalent resistance R_eq = R₁ + R₂. Using R = L / (σ A): (2L)/(σ_eq A) = L/(σ₁ A) + L/(σ₂ A) => 2/σ_eq = (σ₁ + σ₂)/(σ₁σ₂) => σ_eq = (2σ₁σ₂) / (σ₁ + σ₂).",
        "expl_bn": "মোট দৈর্ঘ্য = 2L এবং ক্ষেত্রফল = A। শ্রেণি সমবায়ে তুল্য রোধ R_eq = R₁ + R₂। R = L / (σ A) থেকে: 2/σ_eq = 1/σ₁ + 1/σ₂ => σ_eq = (2σ₁σ₂) / (σ₁ + σ₂), যা পরিবাহিতা দুটির হারমোনিক গড়।"
    },
    {
        "id": "PHY-015",
        "exam": "NEET, JEE, WBJEE, CUET, BITSAT, NDA",
        "subject": "Physics",
        "topic": "Alternating Current & Resonance",
        "difficulty": "Medium",
        "en": "An AC circuit consists of a pure resistance of 1 kΩ, a capacitor of capacitance 0.1 μF, and an inductor of inductance 1 mH connected in series. The approximate resonant frequency (f_r) of the circuit and the effect on f_r if the resistance is doubled are respectively:",
        "bn": "একটি পরিবর্তী প্রবাহ (AC) বর্তনীতে ১ kΩ রোধ, ০.১ μF ধারকত্ব এবং ১ mH আবেশাঙ্ক শ্রেণি সমবায়ে যুক্ত রয়েছে। বর্তনীটির আনুমানিক অনুনাদী কম্পাঙ্ক (f_r) এবং রোধ দ্বিগুণ করা হলে f_r-এর ওপর প্রভাব যথাক্রমে:",
        "opts": {
            "en": ["15.9 kHz, unchanged", "10.1 kHz, halved", "15.9 kHz, doubled", "20.7 kHz, unchanged"],
            "bn": ["15.9 kHz, অপরিবর্তিত থাকবে", "10.1 kHz, অর্ধেক হবে", "15.9 kHz, দ্বিগুণ হবে", "20.7 kHz, অপরিবর্তিত থাকবে"]
        },
        "correct": 0,
        "expl_en": "Series resonant frequency: f_r = 1 / (2π√(LC)). With L = 10⁻³ H and C = 10⁻⁷ F, √(LC) = 10⁻⁵ s => f_r = 10⁵ / (2π) ≈ 15.9 kHz. Because resonance depends solely on L and C and is independent of resistance R, doubling R leaves f_r unchanged.",
        "expl_bn": "অনুনাদী কম্পাঙ্ক: f_r = ১ / (২π√(LC))। L = ১০⁻³ H এবং C = ১০⁻⁷ F হলে √(LC) = ১০⁻⁵ s => f_r = ১০⁵ / (২π) ≈ ১৫.৯ kHz। অনুনাদী কম্পাঙ্ক রোধ R-এর ওপর নির্ভর করে না, তাই রোধ দ্বিগুণ করলেও তা অপরিবর্তিত থাকে।"
    },
    {
        "id": "PHY-016",
        "exam": "JEE, WBJEE, NEET, CUET, NDA, BITSAT",
        "subject": "Physics",
        "topic": "Current Electricity & Bridge Instruments",
        "difficulty": "Medium",
        "en": "In a balanced Metre Bridge experiment, the positions of the galvanometer and the battery cell are interchanged. Which of the following observations will be correct regarding the balance point?",
        "bn": "একটি ভারসাম্যাবস্থায় থাকা মিটার ব্রিজ পরীক্ষায় গ্যালভানোমিটার এবং ব্যাটারি কোষের অবস্থান পরস্পর বিনিময় করা হলো। ভারসাম্যাবস্থার বিন্দুর ক্ষেত্রে নিচের কোন পর্যবেক্ষণটি সঠিক হবে?",
        "opts": {
            "en": [
                "The balance condition remains unaffected and the galvanometer still shows null deflection",
                "The balance point shifts to the extreme right end",
                "The balance point shifts to the extreme left end",
                "The bridge becomes inoperable and permanent deflection occurs"
            ],
            "bn": [
                "ভারসাম্যের শর্ত অপরিবর্তিত থাকবে এবং গ্যালভানোমিটারে বিক্ষেপ শূন্যই থাকবে",
                "ভারসাম্য বিন্দু চরম ডান প্রান্তে সরে যাবে",
                "ভারসাম্য বিন্দু চরম বাম প্রান্তে সরে যাবে",
                "ব্রিজটি অকার্যকর হয়ে যাবে এবং স্থায়ী বিক্ষেপ দেখাবে"
            ]
        },
        "correct": 0,
        "expl_en": "By the conjugate arms property of a Wheatstone bridge, the battery arm and galvanometer arm are mutually conjugate. Interchanging the galvanometer and battery does not alter the balance condition (P/Q = R/S), so the galvanometer continues to show null deflection at the exact same point.",
        "expl_bn": "হুইটস্টোন ব্রিজের অনুবন্ধী বাহু (Conjugate Arms) নীতি অনুসারে ব্যাটারি এবং গ্যালভানোমিটারের বাহু পরস্পর অনুবন্ধী। এদের অবস্থান বিনিময় করলেও ভারসাম্যের মূল শর্ত অপরিবর্তিত থাকে এবং গ্যালভানোমিটার শূন্য বিক্ষেপই প্রদর্শন করে।"
    },
    # =========================================================================
    # CHEMISTRY (Newly Sorted High-Yield Questions)
    # =========================================================================
    {
        "id": "CHEM-008",
        "exam": "JEE, NEET, WBJEE, BITSAT, CUET, IIT-JAM",
        "subject": "Chemistry",
        "topic": "Chemical Kinetics & Arrhenius Theory",
        "difficulty": "Hard",
        "diagram": SVG_ARRHENIUS_PLOT,
        "en": "According to the Arrhenius equation, a plot of ln(k) against 1/T for a first-order chemical reaction yields a straight line with a slope of -6000 K. Taking the universal gas constant R = 8.314 J·K⁻¹·mol⁻¹, the activation energy (E_a) of the reaction is approximately:",
        "bn": "আরহেনিয়াসের সমীকরণ অনুসারে, একটি প্রথম ক্রম বিক্রিয়ার ক্ষেত্রে 1/T এর বিপরীতে ln(k) এর লেখচিত্র অঙ্কন করলে -৬০০০ K নতি (slope) বিশিষ্ট একটি সরলরেখা পাওয়া যায়। সার্বজনীন গ্যাস ধ্রুবক R = ৮.৩১৪ J·K⁻¹·mol⁻¹ হলে বিক্রিয়াটির সক্রিয়করণ শক্তি (E_a) প্রায় কত?",
        "opts": {
            "en": ["49.88 kJ/mol", "24.94 kJ/mol", "99.76 kJ/mol", "12.47 kJ/mol"],
            "bn": ["49.88 kJ/mol", "24.94 kJ/mol", "99.76 kJ/mol", "12.47 kJ/mol"]
        },
        "correct": 0,
        "expl_en": "Arrhenius equation: ln(k) = ln(A) - (E_a / R)(1/T). Comparing with y = mx + c: Slope m = -E_a / R = -6000 K => E_a = 6000 × 8.314 J/mol = 49,884 J/mol ≈ 49.88 kJ/mol.",
        "expl_bn": "আরহেনিয়াসের সমীকরণ: ln(k) = ln(A) - (E_a / R)(১/T)। লেখচিত্রের নতি m = -E_a / R = -৬০০০ K => E_a = ৬০০০ × ৮.৩১৪ J/mol = ৪৯,৮৮৪ J/mol ≈ ৪৯.৮৮ kJ/mol।"
    },
    {
        "id": "CHEM-009",
        "exam": "JEE, NEET, WBJEE, BITSAT, AIIMS, CUET",
        "subject": "Chemistry",
        "topic": "Carbonyl Compounds & Reaction Mechanisms",
        "difficulty": "Hard",
        "diagram": SVG_CANNIZZARO_FLOW,
        "en": "When an equimolar mixture of benzaldehyde (C₆H₅CHO) and formaldehyde (HCHO) is heated with 50% concentrated aqueous NaOH solution (Crossed Cannizzaro reaction), the major organic products formed are:",
        "bn": "বেনজালডিহাইড (C₆H₅CHO) এবং ফর্মালডিহাইডের (HCHO) সমমোলার মিশ্রণকে ৫০% গাঢ় জলীয় NaOH দ্রবণের সাথে উত্তপ্ত করলে (ক্রসড ক্যানিজারো বিক্রিয়া) প্রধান জৈব উৎপাদসমূহ কী কী গঠিত হয়?",
        "opts": {
            "en": [
                "Benzyl alcohol and Sodium formate",
                "Sodium benzoate and Methanol",
                "Benzyl alcohol and Methanol",
                "Sodium benzoate and Sodium formate"
            ],
            "bn": [
                "বেনজাইল অ্যালকোহল এবং সোডিয়াম ফরমেট",
                "সোডিয়াম বেনজোয়েট এবং মিথানল",
                "বেনজাইল অ্যালকোহল এবং মিথানল",
                "সোডিয়াম বেনজোয়েট এবং সোডিয়াম ফরমেট"
            ]
        },
        "correct": 0,
        "expl_en": "In crossed Cannizzaro, OH⁻ attacks the sterically unhindered and more electrophilic formaldehyde. The formed intermediate transfers a hydride ion (H⁻) to benzaldehyde. Thus, formaldehyde is oxidized to sodium formate (HCOONa) while benzaldehyde is reduced to benzyl alcohol (C₆H₅CH₂OH).",
        "expl_bn": "ক্রসড ক্যানিজারো বিক্রিয়ায় OH⁻ দ্রুত ফর্মালডিহাইডে আক্রমণ করে কারণ এটি অধিক ইলেকট্রোফিলিক। এরপর হাইড্রাইড আয়ন বেনজালডিহাইডে স্থানান্তরিত হওয়ায় ফর্মালডিহাইড জারিত হয়ে সোডিয়াম ফরমেট এবং বেনজালডিহাইড বিজারিত হয়ে বেনজাইল অ্যালকোহল গঠন করে।"
    },
    {
        "id": "CHEM-010",
        "exam": "NEET, JEE, WBJEE, CUET, BITSAT, AIIMS",
        "subject": "Chemistry",
        "topic": "Electrochemistry & Nernst Equation",
        "difficulty": "Medium",
        "en": "For the Daniell cell represented as Zn(s) | Zn²⁺(0.01 M) || Cu²⁺(0.1 M) | Cu(s) at 298 K, the standard cell potential is E°_cell = 1.10 V. Given (2.303 RT/F) = 0.0591 V, the electromotive force (EMF) of this galvanic cell is:",
        "bn": "২৯৮ K তাপমাত্রায় Zn(s) | Zn²⁺(0.01 M) || Cu²⁺(0.1 M) | Cu(s) ড্যানিয়েল কোষের প্রমাণ বিভব E°_cell = 1.10 V। (2.303 RT/F) = 0.0591 V হলে এই গ্যালভানীয় কোষটির তড়িচ্চালক বল (EMF) কত?",
        "opts": {
            "en": ["1.130 V", "1.070 V", "1.159 V", "1.041 V"],
            "bn": ["1.130 V", "1.070 V", "1.159 V", "1.041 V"]
        },
        "correct": 0,
        "expl_en": "Cell reaction: Zn + Cu²⁺ -> Zn²⁺ + Cu (n = 2). Nernst equation: E_cell = E°_cell - (0.0591/2) log([Zn²⁺]/[Cu²⁺]) = 1.10 - 0.02955 log(0.01/0.1) = 1.10 - 0.02955(-1) = 1.10 + 0.02955 ≈ 1.130 V.",
        "expl_bn": "কোষ বিক্রিয়া: Zn + Cu²⁺ -> Zn²⁺ + Cu (n = ২)। নার্নস্ট সমীকরণ: E_cell = ১.১০ - (০.০৫৯১/২) log(০.০১/০.১) = ১.১০ - ০.০২৯৫৫(-১) ≈ ১.১৩০ V।"
    },
    {
        "id": "CHEM-011",
        "exam": "JEE, NEET, WBJEE, CUET, AIIMS, NEST, IIT-JAM",
        "subject": "Chemistry",
        "topic": "Coordination Chemistry & Crystal Field Theory",
        "difficulty": "Hard",
        "en": "Consider the two octahedral iron(III) complexes [Fe(CN)₆]³⁻ and [Fe(H₂O)₆]³⁺. The hybridization of the central metal ion and the spin-only magnetic moment (μ_s) of [Fe(CN)₆]³⁻ are respectively:",
        "bn": "দুটি অষ্টতলকীয় আয়রন(III) জটিল যৌগ [Fe(CN)₆]³⁻ এবং [Fe(H₂O)₆]³⁺ বিবেচনা করো। [Fe(CN)₆]³⁻ যৌগে কেন্দ্রীয় ধাতব আয়নের সংকরায়ন (hybridization) এবং কেবল ঘূর্ণনজনিত চৌম্বক ভ্রামক (μ_s) যথাক্রমে কত?",
        "opts": {
            "en": ["d²sp³ and 1.73 BM", "sp³d² and 5.92 BM", "d²sp³ and 3.87 BM", "sp³d² and 1.73 BM"],
            "bn": ["d²sp³ এবং 1.73 BM", "sp³d² এবং 5.92 BM", "d²sp³ এবং 3.87 BM", "sp³d² এবং 1.73 BM"]
        },
        "correct": 0,
        "expl_en": "Fe³⁺ has 3d⁵ configuration. Strong-field ligand CN⁻ forces electron pairing (t_2g⁵ e_g⁰), giving 1 unpaired electron (n = 1) and vacant inner 3d orbitals for d²sp³ hybridization. Spin-only magnetic moment: μ_s = √(1(3)) ≈ 1.73 BM (low spin complex).",
        "expl_bn": "Fe³⁺ এর ইলেকট্রন বিন্যাস 3d⁵। শক্তিশালী লিগ্যান্ড CN⁻ ইলেকট্রন জোড় বাঁধায় (t_2g⁵ e_g⁰), ফলে ১টি অযুগ্ম ইলেকট্রন থাকে এবং অভ্যন্তরীণ d²sp³ সংকরায়ন ঘটে। ঘূর্ণন চৌম্বক ভ্রামক μ_s = √৩ ≈ ১.৭৩ BM।"
    },
    {
        "id": "CHEM-012",
        "exam": "JEE, NEET, WBJEE, BITSAT, CUET",
        "subject": "Chemistry",
        "topic": "Solutions & Colligative Properties",
        "difficulty": "Medium",
        "en": "When benzoic acid (C₆H₅COOH) is dissolved in benzene, it undergoes partial dimerisation: 2 C₆H₅COOH ⇌ (C₆H₅COOH)₂. If the degree of association (α) of benzoic acid in the solution is 80%, the van 't Hoff factor (i) is:",
        "bn": "বেনজয়িক অ্যাসিডকে (C₆H₅COOH) বেনজিনে দ্রবীভূত করলে এটি আংশিক ডাইমারাইজেশন সম্পন্ন করে: 2 C₆H₅COOH ⇌ (C₆H₅COOH)₂। দ্রবণে বেনজয়িক অ্যাসিডের সংযোজন মাত্রা (α) ৮০% হলে ভ্যান্ট হফ গুণক (i) কত হবে?",
        "opts": {
            "en": ["0.60", "0.80", "1.20", "0.40"],
            "bn": ["0.60", "0.80", "1.20", "0.40"]
        },
        "correct": 0,
        "expl_en": "For association into an n-mer: i = 1 - α(1 - 1/n). For dimerisation n = 2 and α = 0.80: i = 1 - 0.80(1 - 1/2) = 1 - 0.40 = 0.60.",
        "expl_bn": "অণুর সংযোজনের ক্ষেত্রে: i = ১ - α(১ - ১/n)। ডাইমার গঠনের ক্ষেত্রে n = ২ এবং α = ০.৮০ বসালে: i = ১ - ০.৮০(০.৫) = ১ - ০.৪০ = ০.৬০।"
    },
    # =========================================================================
    # BIOLOGY (Newly Sorted High-Yield Questions)
    # =========================================================================
    {
        "id": "BIO-007",
        "exam": "NEET, AIIMS, AFMC, CUET, IAT, ICAR",
        "subject": "Biology",
        "topic": "Plant Physiology & Photosynthesis",
        "difficulty": "Medium",
        "diagram": SVG_KRANZ_ANATOMY,
        "en": "In C₄ plants such as maize and sugarcane, carbon dioxide fixation occurs through the Hatch and Slack pathway. The primary CO₂ acceptor molecule and the initial carboxylating enzyme present in the mesophyll cells are respectively:",
        "bn": "ভুট্টা এবং আখের মতো C₄ উদ্ভিদে হ্যাচ ও স্ল্যাক চক্রের মাধ্যমে কার্বন ডাইঅক্সাইড সংবন্ধন ঘটে। মেসোফিল কোষে প্রাথমিক CO₂ গ্রাহক অণু এবং প্রাথমিক কার্বক্সিলেটিং উৎসেচক যথাক্রমে কোনটি?",
        "opts": {
            "en": [
                "Phosphoenolpyruvate (PEP) and PEP carboxylase",
                "Ribulose-1,5-bisphosphate (RuBP) and RuBisCO",
                "Oxaloacetic acid (OAA) and Malic dehydrogenase",
                "Phosphoglyceric acid (PGA) and RuBisCO"
            ],
            "bn": [
                "ফসফোএনলপাইরুভেট (PEP) এবং PEP কার্বক্সিলেজ",
                "রিবুলোজ-১,৫-বিসফসফেট (RuBP) এবং RuBisCO",
                "অক্সালোঅ্যাসিটিক অ্যাসিড (OAA) এবং ম্যালিক ডিহাইড্রোজিনেজ",
                "ফসফোগ্লিসারিক অ্যাসিড (PGA) এবং RuBisCO"
            ]
        },
        "correct": 0,
        "expl_en": "In C₄ plants showing Kranz anatomy, the primary CO₂ acceptor in the mesophyll cytoplasm is the 3-carbon phosphoenolpyruvate (PEP), catalyzed by PEP carboxylase (PEPcase) to form 4-carbon oxaloacetic acid (OAA). RuBisCO is absent in mesophyll cells and restricted to bundle sheath cells.",
        "expl_bn": "ক্র্যাঞ্জ শারীরস্থান বিশিষ্ট C₄ উদ্ভিদের মেসোফিল কোষে প্রাথমিক CO₂ গ্রাহক হলো ফসফোএনলপাইরুভেট (PEP), যা PEP কার্বক্সিলেজ দ্বারা অনুঘটক হয়ে অক্সালোঅ্যাসিটিক অ্যাসিড (OAA) তৈরি করে। মেসোফিল কোষে RuBisCO থাকে না, এটি বান্ডিল সিথ কোষে থাকে।"
    },
    {
        "id": "BIO-008",
        "exam": "NEET, AIIMS, AFMC, CUET, IAT",
        "subject": "Biology",
        "topic": "Human Physiology & Locomotion",
        "difficulty": "Medium",
        "diagram": SVG_SARCOMERE_STRUCTURE,
        "en": "According to the sliding filament mechanism of skeletal muscle contraction, when calcium ions (Ca²⁺) bind to troponin C on actin filaments, which of the following structural changes occurs in the sarcomere?",
        "bn": "কঙ্কাল পেশি সংকোচনের স্লাইডিং ফিলামেন্ট তত্ত্ব অনুসারে, যখন ক্যালসিয়াম আয়ন (Ca²⁺) অ্যাক্টিন ফিলামেন্টের ট্রপোনিন C-এর সাথে যুক্ত হয়, তখন সারকোমিয়ারে নিচের কোন গাঠনিক পরিবর্তনটি ঘটে?",
        "opts": {
            "en": [
                "The H-zone and I-band narrow while the length of the A-band remains constant",
                "The A-band shortens while the I-band and Z-lines remain stationary",
                "Both the A-band and I-band lengthen as myosin filaments stretch",
                "The Z-lines move apart and the H-zone widens"
            ],
            "bn": [
                "H-অঞ্চল এবং I-ব্যান্ড সংকীর্ণ হয় কিন্তু A-ব্যান্ডের দৈর্ঘ্য অপরিবর্তিত থাকে",
                "A-ব্যান্ড ছোট হয় কিন্তু I-ব্যান্ড এবং Z-রেখা স্থির থাকে",
                "মায়োসিন প্রসারিত হওয়ায় A-ব্যান্ড এবং I-ব্যান্ড উভয়ই দীর্ঘায়িত হয়",
                "Z-রেখা দুটি দূরে সরে যায় এবং H-অঞ্চল প্রসারিত হয়"
            ]
        },
        "correct": 0,
        "expl_en": "During contraction, actin filaments slide over myosin filaments toward the M-line. Consequently, the I-bands shorten, the central H-zone narrows/disappears, while the length of the dark A-band (representing thick myosin filaments) remains strictly constant.",
        "expl_bn": "পেশি সংকোচনের সময় অ্যাক্টিন ফিলামেন্ট মায়োসিনের ওপর দিয়ে কেন্দ্রের দিকে সরে যায়। ফলে I-ব্যান্ড এবং H-অঞ্চল সংকুচিত হয়, কিন্তু মায়োসিন ফিলামেন্টের দৈর্ঘ্য নির্দেশক A-ব্যান্ডের দৈর্ঘ্য সর্বদা স্থির থাকে।"
    },
    {
        "id": "BIO-009",
        "exam": "NEET, AIIMS, AFMC, CUET, IAT, CSIR-NET",
        "subject": "Biology",
        "topic": "Biotechnology & Molecular Techniques",
        "difficulty": "Medium",
        "diagram": SVG_GEL_ELECTROPHORESIS,
        "en": "In agarose gel electrophoresis of DNA fragments, which of the following statements correctly describes the migration behavior and visualization of the separated fragments?",
        "bn": "DNA খণ্ডকের অ্যাগারোজ জেল ইলেক্ট্রোফোরেসিসের ক্ষেত্রে, পৃথকীকৃত খণ্ডকগুলির চলন এবং দৃশ্যমানতার বিষয়ে নিচের কোন বক্তব্যটি সঠিক?",
        "opts": {
            "en": [
                "Negatively charged DNA fragments migrate toward the positive anode, with smaller fragments moving faster; bands appear bright orange under UV light after ethidium bromide staining",
                "Positively charged DNA fragments migrate toward the negative cathode, with larger fragments moving faster; bands are directly visible under white light",
                "DNA fragments migrate toward the anode with velocities independent of their base-pair sizes",
                "Ethidium bromide stains DNA blue under infrared illumination"
            ],
            "bn": [
                "ঋণাত্মক আধানযুক্ত DNA খণ্ডকগুলি ধনাত্মক অ্যানোডের দিকে ধাবিত হয়, ছোট খণ্ডকগুলি দ্রুত চলে; ইথিডিয়াম ব্রোমাইড রঞ্জনের পর UV আলোতে উজ্জ্বল কমলা রঙের ব্যান্ড দৃশ্যমান হয়",
                "ধনাত্মক আধানযুক্ত DNA খণ্ডকগুলি ঋণাত্মক ক্যাথোডের দিকে ধাবিত হয়, বড় খণ্ডকগুলি দ্রুত চলে; সাদা আলোতে সরাসরি দৃশ্যমান হয়",
                "DNA খণ্ডকগুলির অ্যানোডের দিকে চলন তাদের ক্ষার-জোড় (base pair) আকারের ওপর নির্ভর করে না",
                "ইথিডিয়াম ব্রোমাইড অবলোহিত আলোতে DNA-কে নীল রঙে রঞ্জিত করে"
            ]
        },
        "correct": 0,
        "expl_en": "DNA's negative phosphate backbone drives migration toward the positive anode. Agarose acts as a sieve where smaller fragments move faster and farther. Staining with ethidium bromide (EtBr) followed by ultraviolet (UV) transillumination reveals bright orange fluorescent DNA bands.",
        "expl_bn": "ফসফেট গ্রুপের ঋণাত্মক আধানের কারণে DNA অ্যানোডের দিকে অগ্রসর হয় এবং জেলের মধ্যে ছোট খণ্ডকগুলি দ্রুত চলে। ইথিডিয়াম ব্রোমাইড (EtBr) রঞ্জক যোগ করার পর অতিবেগুনি (UV) আলোয় দেখলে উজ্জ্বল কমলা রঙের ব্যান্ড প্রতীয়মান হয়।"
    },
    {
        "id": "BIO-010",
        "exam": "NEET, AIIMS, CUET, ICAR, UPSC, STATE-PSC",
        "subject": "Biology",
        "topic": "Ecosystem Dynamics & Energy Flow",
        "difficulty": "Easy",
        "en": "According to Lindeman's 10 percent law of energy transfer in an ecosystem, if the primary producers (green plants) synthesize 20,000 J of energy through photosynthesis, how much energy will be available to the tertiary consumer (e.g., eagle or apex predator)?",
        "bn": "বাস্তুতন্ত্রে শক্তি প্রবাহের লিন্ডেম্যানের ১০ শতাংশ সূত্র অনুসারে, প্রাথমিক উৎপাদকরা (সবুজ উদ্ভিদ) সালোকসংশ্লেষের মাধ্যমে ২০,০০০ J শক্তি উৎপাদন করলে, তৃতীয় স্তরের খাদক (যেমন ঈগল বা শীর্ষ শিকারী) কতটুকু শক্তি লাভ করবে?",
        "opts": {
            "en": ["20 J", "200 J", "2 J", "2,000 J"],
            "bn": ["20 J", "200 J", "2 J", "2,000 J"]
        },
        "correct": 0,
        "expl_en": "Applying Lindeman's 10% law: Producers (T₁) = 20,000 J -> Herbivores (T₂) = 2,000 J -> Primary Carnivores (T₃) = 200 J -> Tertiary Consumers (T₄) = 20 J.",
        "expl_bn": "লিন্ডেম্যানের ১০% সূত্রানুসারে: উৎপাদক (T₁) = ২০,০০০ J -> প্রাথমিক খাদক (T₂) = ২,০০০ J -> গৌণ খাদক (T₃) = ২০০ J -> তৃতীয় স্তরের খাদক (T₄) = ২০ J।"
    },
    {
        "id": "BIO-011",
        "exam": "NEET, AIIMS, AFMC, CUET, IAT, CSIR-NET",
        "subject": "Biology",
        "topic": "Genetics & Morgan's Linkage Experiments",
        "difficulty": "Hard",
        "en": "In his seminal dihybrid crosses on Drosophila melanogaster, Thomas Hunt Morgan observed that genes located on the same chromosome did not assort independently. When crossing yellow-bodied, white-eyed females with wild-type brown-bodied, red-eyed males, the proportion of parental phenotypes versus recombinant types in the F₂ generation was:",
        "bn": "ড্রোসোফিলা মেলানোগাস্টারের ওপর দ্বি-সংকরায়ন পরীক্ষায় থমাস হান্ট মর্গান লক্ষ্য করেন যে একই ক্রোমোজোমে অবস্থিত জিনগুলি স্বাধীনভাবে সঞ্চারিত হয় না। হলুদ দেহ ও সাদা চোখের স্ত্রী মাছির সাথে বুনো বাদামী দেহ ও লাল চোখের পুরুষ মাছির সংকরায়নে F₂ জনুতে অপত্যদের মধ্যে জনিতৃ বৈশিষ্ট্য এবং পুনর্বিন্যস্ত (রিকম্বিন্যান্ট) বৈশিষ্ট্যের অনুপাত কত ছিল?",
        "opts": {
            "en": [
                "98.7% Parental types and 1.3% Recombinant types",
                "62.8% Parental types and 37.2% Recombinant types",
                "50.0% Parental types and 50.0% Recombinant types",
                "75.0% Parental types and 25.0% Recombinant types"
            ],
            "bn": [
                "৯৮.৭% জনিতৃ বৈশিষ্ট্য এবং ১.৩% রিকম্বিন্যান্ট বৈশিষ্ট্য",
                "৬২.৮% জনিতৃ বৈশিষ্ট্য এবং ৩৭.২% রিকম্বিন্যান্ট বৈশিষ্ট্য",
                "৫০.০% জনিতৃ বৈশিষ্ট্য এবং ৫০.০% রিকম্বিন্যান্ট বৈশিষ্ট্য",
                "৭৫.০% জনিতৃ বৈশিষ্ট্য এবং ২৫.০% রিকম্বিন্যান্ট বৈশিষ্ট্য"
            ]
        },
        "correct": 0,
        "expl_en": "Morgan attributed the deviation from 9:3:3:1 to X-chromosome physical linkage. The genes for body colour (yellow) and eye colour (white) are very tightly linked, showing 98.7% parental combinations and only 1.3% crossing-over recombinants.",
        "expl_bn": "মেন্ডেলীয় অনুপাত থেকে বিচ্যুতির কারণ হিসেবে মর্গান X-ক্রোমোজোমে জিনের সহসংযোজন বা লিংকেজ নির্দেশ করেন। হলুদ দেহ ও সাদা চোখের জিন দুটি দৃঢ়ভাবে সংলগ্ন থাকায় ৯৮.৭% জনিতৃ বৈশিষ্ট্য এবং মাত্র ১.৩% রিকম্বিন্যান্ট অপত্য তৈরি হয়েছিল।"
    },
    {
        "id": "BIO-012",
        "exam": "NEET, AIIMS, AFMC, CUET, IAT",
        "subject": "Biology",
        "topic": "Human Reproduction & Menstrual Cycle",
        "difficulty": "Medium",
        "diagram": SVG_HORMONAL_CYCLE,
        "en": "In the human female menstrual cycle of 28 days, ovulation (release of secondary oocyte from the mature Graafian follicle) is directly triggered by which endocrine event around day 14?",
        "bn": "মানব স্ত্রীদেহে ২৮ দিনের রজঃচক্রের ক্ষেত্রে, ১৪তম দিনের কাছাকাছি পরিপক্ক গ্রাফিয়ান ফলিকল বিদীর্ণ হয়ে ডিম্বাণু নির্গমন (ওভিউলেশন) সরাসরি কোন হরমোনজনিত ঘটনার দ্বারা ঘটে?",
        "opts": {
            "en": [
                "A rapid surge in Luteinizing Hormone (LH surge) secreted by the anterior pituitary",
                "A sharp drop in estrogen levels produced by the corpus luteum",
                "Peak secretion of progesterone by developing primary follicles",
                "A sudden drop in Follicle Stimulating Hormone (FSH) to baseline levels"
            ],
            "bn": [
                "অগ্র পিটুইটারি থেকে নিঃসৃত লিউটিনাইজিং হরমোনের তীব্র বৃদ্ধি (LH সার্জ)",
                "কর্পাস লিউটিয়াম দ্বারা উৎপাদিত ইস্ট্রোজেনের মাত্রায় আকস্মিক হ্রাস",
                "বিকাশমান প্রাথমিক ফলিকল দ্বারা প্রোজেস্টেরনের সর্বোচ্চ ক্ষরণ",
                "ফলিকল স্টিমুলেটিং হরমোনের (FSH) আকস্মিক পতন"
            ]
        },
        "correct": 0,
        "expl_en": "Around the 14th day of the cycle, rapid secretion of LH induces maximum mid-cycle concentration ('LH surge'), which causes rupture of the mature Graafian follicle and release of the ovum (ovulation).",
        "expl_bn": "চক্রের মধ্যভাগে (১৪তম দিনে) অগ্র পিটুইটারি থেকে লিউটিনাইজিং হরমোনের (LH) ক্ষরণ সর্বোচ্চ মাত্রায় পৌঁছায় ('LH সার্জ'), যা গ্রাফিয়ান ফলিকলকে বিদীর্ণ করে ডিম্বাণু নির্গমন বা ওভিউলেশন ঘটায়।"
    },
    # =========================================================================
    # MATHEMATICS (Newly Sorted High-Yield Questions)
    # =========================================================================
    {
        "id": "MATH-007",
        "exam": "JEE, WBJEE, BITSAT, NDA, IAT",
        "subject": "Mathematics",
        "topic": "Differential Calculus & Mean Value Theorems",
        "difficulty": "Hard",
        "en": "Let f(x) = x(x - 1)(x - 2) on the closed interval [0, 1/2]. According to Lagrange's Mean Value Theorem, there exists a value c ∈ (0, 1/2) such that f'(c) = (f(1/2) - f(0)) / (1/2 - 0). The value of c is:",
        "bn": "ধরি [0, 1/2] বদ্ধ বিস্তারে f(x) = x(x - 1)(x - 2)। ল্যাগ্রাঞ্জের গড় মান উপপাদ্য (LMVT) অনুসারে (0, 1/2) মুক্ত বিস্তারে এমন একটি বিন্দু c অবস্থান করে যার জন্য f'(c) = (f(1/2) - f(0)) / (1/2 - 0)। c এর মান কত?",
        "opts": {
            "en": ["(6 - √21) / 6", "(6 + √21) / 6", "1 / √6", "(3 - √5) / 4"],
            "bn": ["(6 - √21) / 6", "(6 + √21) / 6", "1 / √6", "(3 - √5) / 4"]
        },
        "correct": 0,
        "expl_en": "f(x) = x³ - 3x² + 2x. f(0) = 0 and f(1/2) = 3/8 => slope = (3/8)/(1/2) = 3/4. Setting f'(c) = 3c² - 6c + 2 = 3/4 => 12c² - 24c + 5 = 0. Solving: c = (6 ± √21)/6. Because (6 - √21)/6 ≈ 0.236 lies in (0, 1/2), c = (6 - √21)/6.",
        "expl_bn": "f(x) = x³ - 3x² + 2x। f(০) = ০ এবং f(১/২) = ৩/৮ => গড় ঢাল = ৩/৪। f'(c) = 3c² - 6c + 2 = ৩/৪ => 12c² - 24c + 5 = 0। সমাধান করলে c = (৬ ± √২১)/৬। যেহেতু ০.২৩৬ মানটি (০, ১/২) বিস্তারে অবস্থিত, তাই c = (৬ - √২১)/৬।"
    },
    {
        "id": "MATH-008",
        "exam": "JEE, JEE-ADV, WBJEE, BITSAT, IAT, IIT-JAM",
        "subject": "Mathematics",
        "topic": "Integral Calculus & Definite Integrals",
        "difficulty": "Hard",
        "en": "The value of the definite integral I = ∫₀^π (x sin(x)) / (1 + cos²(x)) dx is:",
        "bn": "নির্দিষ্ট সমাকল I = ∫₀^π (x sin(x)) / (1 + cos²(x)) dx এর মান কত?",
        "opts": {
            "en": ["π² / 4", "π² / 2", "π / 4", "π² / 8"],
            "bn": ["π² / 4", "π² / 2", "π / 4", "π² / 8"]
        },
        "correct": 0,
        "expl_en": "By King's property: 2I = π ∫₀^π sin(x)/(1 + cos²(x)) dx. Substituting u = cos(x), du = -sin(x)dx gives 2I = π ∫₋₁¹ du/(1 + u²) = π [tan⁻¹(1) - tan⁻¹(-1)] = π²/2 => I = π²/4.",
        "expl_bn": "কিং-এর ধর্ম প্রয়োগ করে: 2I = π ∫₀^π sin(x)/(1 + cos²(x)) dx। u = cos(x) বসালে: 2I = π ∫₋₁¹ du/(1 + u²) = π²/2 => I = π²/4।"
    },
    {
        "id": "MATH-009",
        "exam": "JEE, WBJEE, BITSAT, NDA",
        "subject": "Mathematics",
        "topic": "Coordinate Geometry & Conic Sections",
        "difficulty": "Hard",
        "diagram": SVG_CONIC_COMMON_TANGENT,
        "en": "The equation of a common tangent to the parabola y² = 8ax and the circle x² + y² = 2a² is:",
        "bn": "অধিবৃত্ত y² = 8ax এবং বৃত্ত x² + y² = 2a² এর একটি সাধারণ স্পর্শকের সমীকরণ কোনটি?",
        "opts": {
            "en": ["y = x + 2a", "y = 2x + a", "y = x + a√2", "y = √3 x + a"],
            "bn": ["y = x + 2a", "y = 2x + a", "y = x + a√2", "y = √3 x + a"]
        },
        "correct": 0,
        "expl_en": "For parabola y² = 8ax (4A = 8a => A = 2a), tangent with slope m is y = mx + 2a/m. Perpendicular distance from circle centre (0,0) to mx - y + 2a/m = 0 must equal circle radius a√2: |2a/m| / √(m² + 1) = a√2. Putting m = 1 gives |2a|/√2 = a√2, which satisfies the condition. Thus, y = x + 2a is a common tangent.",
        "expl_bn": "y² = 8ax অধিবৃত্তের m নতিযুক্ত স্পর্শক হলো y = mx + 2a/m। বৃত্তের কেন্দ্র (0,0) থেকে এর দূরত্ব ব্যাসার্ধ a√2 এর সমান হলে: |2a/m| / √(m² + 1) = a√2। m = ১ বসালে সমীকরণটি সিদ্ধ হয়, সুতরাং সাধারণ স্পর্শকটি হলো y = x + 2a।"
    },
    {
        "id": "MATH-010",
        "exam": "JEE, WBJEE, BITSAT, NDA, CUET",
        "subject": "Mathematics",
        "topic": "Complex Numbers & Cube Roots of Unity",
        "difficulty": "Medium",
        "en": "If ω is a complex cube root of unity (ω ≠ 1), the value of the algebraic expression (1 - ω + ω²)⁵ + (1 + ω - ω²)⁵ is:",
        "bn": "যদি ω এককের একটি জটিল ঘনমূল হয় (ω ≠ 1), তবে (1 - ω + ω²)⁵ + (1 + ω - ω²)⁵ রাশিটির মান কত?",
        "opts": {
            "en": ["32", "-32", "64", "0"],
            "bn": ["32", "-32", "64", "0"]
        },
        "correct": 0,
        "expl_en": "Since 1 + ω + ω² = 0, 1 + ω² = -ω and 1 + ω = -ω². Then (-2ω)⁵ + (-2ω²)⁵ = -32ω⁵ - 32ω¹⁰ = -32ω² - 32ω = -32(ω² + ω) = -32(-1) = 32.",
        "expl_bn": "১ + ω + ω² = ০ থেকে পাই ১ + ω² = -ω এবং ১ + ω = -ω²। মান বসিয়ে: (-২ω)⁵ + (-২ω²)⁵ = -৩২(ω² + ω) = -৩২(-১) = ৩২।"
    },
    {
        "id": "MATH-011",
        "exam": "JEE, WBJEE, BITSAT, NDA, CUET, BANKING",
        "subject": "Mathematics",
        "topic": "Probability & Bayes' Theorem",
        "difficulty": "Hard",
        "en": "In a precision factory, Machine A produces 60% of total daily output with a 2% defective rate, while Machine B produces the remaining 40% with a 4% defective rate. An item is selected at random and found to be defective. The posterior probability that this defective item was manufactured by Machine A is:",
        "bn": "একটি কারখানায় যন্ত্র A মোট উৎপাদনের ৬০% তৈরি করে যার ২% ত্রুটিযুক্ত, এবং যন্ত্র B অবশিষ্ট ৪০% তৈরি করে যার ৪% ত্রুটিযুক্ত। দৈবচয়ন পদ্ধতিতে নির্বাচিত একটি পণ্য ত্রুটিযুক্ত পাওয়া গেল। পণ্যটি যন্ত্র A দ্বারা তৈরি হওয়ার উত্তর সম্ভাবনা (posterior probability) কত?",
        "opts": {
            "en": ["3/7", "4/7", "3/10", "1/2"],
            "bn": ["3/7", "4/7", "3/10", "1/2"]
        },
        "correct": 0,
        "expl_en": "P(A) = 0.60, P(B) = 0.40. Defectives: P(D|A) = 0.02, P(D|B) = 0.04. Total defective probability P(D) = 0.60(0.02) + 0.40(0.04) = 0.012 + 0.016 = 0.028. By Bayes' theorem: P(A|D) = 0.012 / 0.028 = 12/28 = 3/7.",
        "expl_bn": "P(A) = ০.৬০, P(B) = ০.৪০। ত্রুটি P(D|A) = ০.০২, P(D|B) = ০.০৪। মোট ত্রুটি P(D) = ০.০২৮। বেইজের সূত্রানুসারে: P(A|D) = ০.০১২ / ০.০২৮ = ৩/৭।"
    },
    {
        "id": "MATH-012",
        "exam": "JEE, WBJEE, BITSAT, NDA, CUET, IIT-JAM",
        "subject": "Mathematics",
        "topic": "Differential Equations & Integrating Factor",
        "difficulty": "Medium",
        "en": "The particular solution of the linear differential equation dy/dx + y cot(x) = 2 cos(x) satisfying the initial boundary condition y(π/2) = 1 is:",
        "bn": "dy/dx + y cot(x) = 2 cos(x) রৈখিক অবকল সমীকরণের বিশেষ সমাধান কোনটি যা y(π/2) = 1 শর্তটিকে সিদ্ধ করে?",
        "opts": {
            "en": ["y = sin(x)", "y = cos(x)", "y = sin²(x)", "y = 2 sin(x) - 1"],
            "bn": ["y = sin(x)", "y = cos(x)", "y = sin²(x)", "y = 2 sin(x) - 1"]
        },
        "correct": 0,
        "expl_en": "Integrating Factor IF = e^{∫ cot(x) dx} = sin(x). Solution: y sin(x) = ∫ 2 sin(x) cos(x) dx = -cos(2x)/2 + C. Using y(π/2) = 1: 1 = 1/2 + C => C = 1/2. Thus y sin(x) = (1 - cos(2x))/2 = sin²(x) => y = sin(x).",
        "expl_bn": "সমাকলন গুণক IF = sin(x)। সমাকল করে: y sin(x) = -cos(2x)/২ + C। y(π/২) = ১ বসালে C = ১/২। সুতরাং y sin(x) = sin²(x) => y = sin(x)।"
    }

]

def export_all():
    os.makedirs("data", exist_ok=True)
    
    # 1. Export data/physics_questions.js
    js_content = "window.PHYSICS_QUESTIONS_DATA = " + json.dumps(all_questions, indent=4, ensure_ascii=False) + ";\n"
    with open("data/physics_questions.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"[OK] Exported {len(all_questions)} questions to data/physics_questions.js")

    # 2. Export data/physics_for_you_master_questions.csv
    csv_headers = [
        "Question_ID", "Exam", "Subject", "Topic", "Difficulty",
        "Question_EN", "Question_BN",
        "Opt1_EN", "Opt2_EN", "Opt3_EN", "Opt4_EN",
        "Opt1_BN", "Opt2_BN", "Opt3_BN", "Opt4_BN",
        "Correct_Answer", "Explanation_EN", "Explanation_BN"
    ]
    with open("data/physics_for_you_master_questions.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)
        for q in all_questions:
            writer.writerow([
                q["id"],
                q["exam"],
                q["subject"],
                q["topic"],
                q["difficulty"],
                q["en"],
                q["bn"],
                q["opts"]["en"][0], q["opts"]["en"][1], q["opts"]["en"][2], q["opts"]["en"][3],
                q["opts"]["bn"][0], q["opts"]["bn"][1], q["opts"]["bn"][2], q["opts"]["bn"][3],
                q["correct"] + 1,
                q["expl_en"],
                q["expl_bn"]
            ])
    print(f"[OK] Exported {len(all_questions)} questions to data/physics_for_you_master_questions.csv")

    # 3. Export data/master_questions_copy_paste.tsv
    with open("data/master_questions_copy_paste.tsv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(csv_headers)
        for q in all_questions:
            writer.writerow([
                q["id"],
                q["exam"],
                q["subject"],
                q["topic"],
                q["difficulty"],
                q["en"],
                q["bn"],
                q["opts"]["en"][0], q["opts"]["en"][1], q["opts"]["en"][2], q["opts"]["en"][3],
                q["opts"]["bn"][0], q["opts"]["bn"][1], q["opts"]["bn"][2], q["opts"]["bn"][3],
                q["correct"] + 1,
                q["expl_en"],
                q["expl_bn"]
            ])
    print(f"[OK] Exported {len(all_questions)} questions to data/master_questions_copy_paste.tsv")

if __name__ == "__main__":
    export_all()
