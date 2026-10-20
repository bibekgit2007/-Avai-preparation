# =============================================================================
# BIOLOGY QUESTION BANK (585 Authentic High-Yield NCERT Line-by-Line Questions)
# Mapped to NEET, CUET, AIIMS, and Olympiad
# Includes:
#   - BIO-001 to BIO-080: Comprehensive Biology Core Bank (80 Questions)
#   - BIO-LW-001 to BIO-LW-100: Unit 1 Ch 1 The Living World (100 Questions)
#   - BIO-BC-001 to BIO-BC-135: Unit 1 Ch 2 Biological Classification (135 Questions)
#   - BIO-PK-001 to BIO-PK-135: Unit 1 Ch 3 Plant Kingdom (135 Questions)
#   - BIO-AK-001 to BIO-AK-135: Unit 1 Ch 4 Animal Kingdom (135 Questions)
# Structure: Graded Question Pyramid (MTG NCERT at your Fingertips Pattern)
# 100% Dual-Language Parity (English & Bengali) with Pure Inline Vector SVGs
# =============================================================================

# -----------------------------------------------------------------------------
# VECTOR SVG DIAGRAM DEFINITIONS (Pure Vector, Zero Raster Bloat)
# -----------------------------------------------------------------------------

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

SVG_TAXONOMIC_HIERARCHY = """<svg viewBox="0 0 500 240" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <polygon points="250,20 220,50 280,50" fill="#f43f5e" stroke="#be123c" stroke-width="1.5"/>
  <text x="250" y="42" fill="#ffffff" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Species (Maximum Specificity)</text>
  <polygon points="220,52 280,52 300,82 200,82" fill="#fb7185" stroke="#be123c" stroke-width="1.5"/>
  <text x="250" y="72" fill="#881337" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Genus</text>
  <polygon points="200,84 300,84 320,114 180,114" fill="#fda4af" stroke="#be123c" stroke-width="1.5"/>
  <text x="250" y="104" fill="#881337" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Family (-aceae / -idae)</text>
  <polygon points="180,116 320,116 340,146 160,146" fill="#fecdd3" stroke="#be123c" stroke-width="1.5"/>
  <text x="250" y="136" fill="#9f1239" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Order (-ales)</text>
  <polygon points="160,148 340,148 360,178 140,178" fill="#ffe4e6" stroke="#be123c" stroke-width="1.5"/>
  <text x="250" y="168" fill="#9f1239" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Class</text>
  <polygon points="140,180 360,180 380,210 120,210" fill="#fff1f2" stroke="#be123c" stroke-width="1.5"/>
  <text x="250" y="200" fill="#9f1239" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Phylum / Division (-phyta)</text>
  <polygon points="120,212 380,212 400,238 100,238" fill="#fda4af" stroke="#be123c" stroke-width="1.5"/>
  <text x="250" y="230" fill="#881337" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Kingdom (Highest Generality)</text>
  <line x1="60" y1="230" x2="60" y2="30" stroke="#0284c7" stroke-width="2.5"/>
  <text x="50" y="130" fill="#0369a1" font-size="10" font-family="system-ui" font-weight="bold" transform="rotate(-90,50,130)" text-anchor="middle">Increasing Common Characteristics →</text>
  <line x1="440" y1="30" x2="440" y2="230" stroke="#059669" stroke-width="2.5"/>
  <text x="455" y="130" fill="#047857" font-size="10" font-family="system-ui" font-weight="bold" transform="rotate(90,455,130)" text-anchor="middle">Increasing Diversity &amp; Generalisation →</text>
</svg>"""

SVG_HERBARIUM_SHEET = """<svg viewBox="0 0 340 240" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <rect x="20" y="10" width="300" height="220" rx="4" fill="#fffbeb" stroke="#78350f" stroke-width="2"/>
  <text x="170" y="28" fill="#92400e" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">Standard Herbarium Sheet (41 cm × 29 cm / 16.5" × 11.5")</text>
  <path d="M 120 180 Q 130 110 160 50" fill="none" stroke="#15803d" stroke-width="3"/>
  <path d="M 135 140 Q 105 130 95 140 Q 115 155 135 140" fill="#86efac" stroke="#16a34a" stroke-width="1.5"/>
  <path d="M 145 105 Q 185 95 195 105 Q 175 120 145 105" fill="#86efac" stroke="#16a34a" stroke-width="1.5"/>
  <path d="M 155 75 Q 125 65 115 75 Q 135 90 155 75" fill="#86efac" stroke="#16a34a" stroke-width="1.5"/>
  <circle cx="160" cy="50" r="7" fill="#facc15" stroke="#ca8a04" stroke-width="1.5"/>
  <rect x="180" y="150" width="130" height="70" rx="3" fill="#ffffff" stroke="#b45309" stroke-width="1.5"/>
  <text x="185" y="165" fill="#78350f" font-size="8" font-family="system-ui" font-weight="bold">HERBARIUM LABEL</text>
  <text x="185" y="177" fill="#451a03" font-size="7" font-family="system-ui">• Date &amp; Place of Collection</text>
  <text x="185" y="187" fill="#451a03" font-size="7" font-family="system-ui">• English, Local &amp; Botanical Name</text>
  <text x="185" y="197" fill="#451a03" font-size="7" font-family="system-ui">• Family</text>
  <text x="185" y="207" fill="#451a03" font-size="7" font-family="system-ui">• Collector's Name (NO HEIGHT!)</text>
</svg>"""

SVG_NOSTOC_FILAMENT = """<svg viewBox="0 0 500 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Mucilaginous Sheath outline -->
  <path d="M 30 80 Q 80 50 140 50 T 250 50 T 360 50 T 460 80 Q 400 110 320 110 T 180 110 T 30 80 Z" fill="#dcfce7" stroke="#16a34a" stroke-dasharray="4,3" opacity="0.6"/>
  <!-- Vegetative cells -->
  <circle cx="60" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>
  <circle cx="95" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>
  <circle cx="130" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>
  <circle cx="165" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>
  <!-- Heterocyst (Larger, thick-walled, labeled A) -->
  <circle cx="215" cy="80" r="22" fill="#fed7aa" stroke="#c2410c" stroke-width="3"/>
  <circle cx="215" cy="80" r="16" fill="#ffedd5" stroke="#ea580c" stroke-width="1.5" stroke-dasharray="2,2"/>
  <text x="215" y="85" fill="#9a3412" font-size="14" font-weight="bold" font-family="system-ui" text-anchor="middle">A</text>
  <!-- More vegetative cells (labeled B) -->
  <circle cx="265" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>
  <text x="265" y="85" fill="#14532d" font-size="12" font-weight="bold" font-family="system-ui" text-anchor="middle">B</text>
  <circle cx="300" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>
  <circle cx="335" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>
  <circle cx="370" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>
  <circle cx="405" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>
  <circle cx="440" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>
  <!-- Mucilage label C -->
  <line x1="100" y1="35" x2="100" y2="55" stroke="#047857" stroke-width="1.5"/>
  <text x="100" y="28" fill="#047857" font-size="12" font-weight="bold" font-family="system-ui" text-anchor="middle">C (Mucilaginous Sheath)</text>
  <line x1="215" y1="115" x2="215" y2="135" stroke="#c2410c" stroke-width="1.5"/>
  <text x="215" y="148" fill="#c2410c" font-size="12" font-weight="bold" font-family="system-ui" text-anchor="middle">Part A</text>
  <line x1="335" y1="115" x2="335" y2="135" stroke="#15803d" stroke-width="1.5"/>
  <text x="335" y="148" fill="#15803d" font-size="12" font-weight="bold" font-family="system-ui" text-anchor="middle">Part B (Vegetative Cell)</text>
</svg>"""

SVG_BACTERIOPHAGE = """<svg viewBox="0 0 320 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Head (Icosahedral Capsid, labeled A) -->
  <polygon points="160,20 200,45 200,90 160,115 120,90 120,45" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>
  <path d="M 140,55 Q 160,40 180,60 T 150,85 T 175,100" fill="none" stroke="#e11d48" stroke-width="2"/>
  <text x="160" y="65" fill="#0369a1" font-size="13" font-weight="bold" font-family="system-ui" text-anchor="middle">A (Head)</text>
  <!-- Collar labeled B -->
  <rect x="145" y="115" width="30" height="10" rx="2" fill="#fde047" stroke="#ca8a04" stroke-width="1.5"/>
  <text x="195" y="124" fill="#a16207" font-size="10" font-weight="bold" font-family="system-ui">B (Collar)</text>
  <!-- Sheath labeled C -->
  <rect x="148" y="125" width="24" height="60" fill="#cbd5e1" stroke="#475569" stroke-width="1.5"/>
  <!-- Helical ridges on sheath -->
  <line x1="148" y1="135" x2="172" y2="135" stroke="#64748b" stroke-width="1.5"/>
  <line x1="148" y1="145" x2="172" y2="145" stroke="#64748b" stroke-width="1.5"/>
  <line x1="148" y1="155" x2="172" y2="155" stroke="#64748b" stroke-width="1.5"/>
  <line x1="148" y1="165" x2="172" y2="165" stroke="#64748b" stroke-width="1.5"/>
  <line x1="148" y1="175" x2="172" y2="175" stroke="#64748b" stroke-width="1.5"/>
  <text x="195" y="158" fill="#334155" font-size="10" font-weight="bold" font-family="system-ui">C (Sheath)</text>
  <!-- Baseplate labeled D -->
  <polygon points="135,185 185,185 190,195 130,195" fill="#f43f5e" stroke="#be123c" stroke-width="1.5"/>
  <text x="200" y="193" fill="#be123c" font-size="10" font-weight="bold" font-family="system-ui">Base plate</text>
  <!-- Tail Fibres labeled E -->
  <path d="M 135 195 L 95 235 L 75 245" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 145 195 L 125 240 L 115 250" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 175 195 L 195 240 L 205 250" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 185 195 L 225 235 L 245 245" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>
  <text x="50" y="240" fill="#0f172a" font-size="10" font-weight="bold" font-family="system-ui">D (Tail fibres)</text>
</svg>"""

SVG_TMV = """<svg viewBox="0 0 340 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Cylindrical viral capsid of TMV -->
  <rect x="40" y="30" width="260" height="110" rx="20" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/>
  <!-- Capsomeres arrangement -->
  <g fill="#93c5fd" stroke="#2563eb" stroke-width="1">
    <ellipse cx="80" cy="55" rx="8" ry="12"/>
    <ellipse cx="105" cy="55" rx="8" ry="12"/>
    <ellipse cx="130" cy="55" rx="8" ry="12"/>
    <ellipse cx="155" cy="55" rx="8" ry="12"/>
    <ellipse cx="180" cy="55" rx="8" ry="12"/>
    <ellipse cx="205" cy="55" rx="8" ry="12"/>
    <ellipse cx="230" cy="55" rx="8" ry="12"/>
    <ellipse cx="255" cy="55" rx="8" ry="12"/>
    <ellipse cx="80" cy="115" rx="8" ry="12"/>
    <ellipse cx="105" cy="115" rx="8" ry="12"/>
    <ellipse cx="130" cy="115" rx="8" ry="12"/>
    <ellipse cx="155" cy="115" rx="8" ry="12"/>
    <ellipse cx="180" cy="115" rx="8" ry="12"/>
    <ellipse cx="205" cy="115" rx="8" ry="12"/>
    <ellipse cx="230" cy="115" rx="8" ry="12"/>
    <ellipse cx="255" cy="115" rx="8" ry="12"/>
  </g>
  <!-- ssRNA central helix -->
  <path d="M 60 85 Q 90 70 120 85 T 180 85 T 240 85 T 280 85" fill="none" stroke="#ef4444" stroke-width="4"/>
  <text x="170" y="89" fill="#991b1b" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">ssRNA genetic material</text>
  <text x="170" y="160" fill="#1e40af" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Protein coat made of Capsomeres (2130 units)</text>
</svg>"""

SVG_ASCO_VS_BASIDIO = """<svg viewBox="0 0 460 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Ascus (Ascomycetes): Sac with 8 endogenous spores -->
  <g transform="translate(40, 20)">
    <rect x="20" y="10" width="60" height="150" rx="30" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
    <text x="50" y="180" fill="#92400e" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Ascus (Sac-fungi)</text>
    <text x="50" y="195" fill="#78350f" font-size="9" font-family="system-ui" text-anchor="middle">8 Endogenous Ascospores</text>
    <!-- 8 spores inside -->
    <circle cx="50" cy="30" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
    <circle cx="50" cy="48" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
    <circle cx="50" cy="66" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
    <circle cx="50" cy="84" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
    <circle cx="50" cy="102" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
    <circle cx="50" cy="120" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
    <circle cx="50" cy="138" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
    <circle cx="50" cy="154" r="6" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
  </g>
  <!-- Basidium (Basidiomycetes): Club with 4 exogenous spores -->
  <g transform="translate(260, 20)">
    <!-- Club shaped basidium -->
    <path d="M 50 160 L 50 80 C 30 70 30 40 50 40 C 70 40 70 70 50 80 Z" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>
    <!-- 4 Sterigmata & 4 Exogenous Basidiospores on top -->
    <line x1="38" y1="42" x2="30" y2="28" stroke="#4338ca" stroke-width="2"/>
    <circle cx="28" cy="24" r="7" fill="#818cf8" stroke="#3730a3" stroke-width="1.5"/>
    <line x1="46" y1="40" x2="42" y2="22" stroke="#4338ca" stroke-width="2"/>
    <circle cx="42" cy="16" r="7" fill="#818cf8" stroke="#3730a3" stroke-width="1.5"/>
    <line x1="54" y1="40" x2="58" y2="22" stroke="#4338ca" stroke-width="2"/>
    <circle cx="58" cy="16" r="7" fill="#818cf8" stroke="#3730a3" stroke-width="1.5"/>
    <line x1="62" y1="42" x2="70" y2="28" stroke="#4338ca" stroke-width="2"/>
    <circle cx="72" cy="24" r="7" fill="#818cf8" stroke="#3730a3" stroke-width="1.5"/>
    <text x="50" y="180" fill="#3730a3" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Basidium (Club-fungi)</text>
    <text x="50" y="195" fill="#312e81" font-size="9" font-family="system-ui" text-anchor="middle">4 Exogenous Basidiospores</text>
  </g>
</svg>"""

SVG_MARCHANTIA_THALLI = """<svg viewBox="0 0 520 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Female Thallus (Archegoniophore with finger-like rays) -->
  <g transform="translate(30, 20)">
    <!-- Thallus -->
    <path d="M 40 180 Q 20 150 50 130 Q 70 110 110 130 Q 150 110 170 140 Q 190 170 150 190 Q 90 200 40 180 Z" fill="#86efac" stroke="#15803d" stroke-width="2"/>
    <!-- Midrib -->
    <path d="M 50 180 Q 100 150 140 140" fill="none" stroke="#166534" stroke-width="2" stroke-dasharray="3,2"/>
    <!-- Gemma Cup (A) -->
    <ellipse cx="100" cy="145" rx="14" ry="8" fill="#4ade80" stroke="#14532d" stroke-width="1.5"/>
    <text x="100" y="148" fill="#052e16" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">A</text>
    <!-- Archegoniophore stalk and umbrella head (B) -->
    <path d="M 110 130 L 110 60" fill="none" stroke="#15803d" stroke-width="3"/>
    <!-- Umbrella with rays -->
    <path d="M 80 60 Q 110 40 140 60 L 145 75 L 135 65 L 125 75 L 115 65 L 105 75 L 95 65 L 85 75 Z" fill="#22c55e" stroke="#14532d" stroke-width="1.5"/>
    <text x="110" y="35" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">B (Archegoniophore)</text>
    <!-- Rhizoids -->
    <path d="M 60 190 L 50 210 M 80 195 L 75 215 M 120 195 L 125 215" stroke="#a16207" stroke-width="1.5"/>
    <text x="110" y="210" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Female Thallus</text>
  </g>

  <!-- Male Thallus (Antheridiophore with scalloped disc) -->
  <g transform="translate(290, 20)">
    <!-- Thallus -->
    <path d="M 40 180 Q 20 150 50 130 Q 70 110 110 130 Q 150 110 170 140 Q 190 170 150 190 Q 90 200 40 180 Z" fill="#86efac" stroke="#15803d" stroke-width="2"/>
    <!-- Midrib -->
    <path d="M 50 180 Q 100 150 140 140" fill="none" stroke="#166534" stroke-width="2" stroke-dasharray="3,2"/>
    <!-- Gemma Cup -->
    <ellipse cx="100" cy="145" rx="14" ry="8" fill="#4ade80" stroke="#14532d" stroke-width="1.5"/>
    <!-- Antheridiophore stalk and peltate disc (C) -->
    <path d="M 110 130 L 110 60" fill="none" stroke="#15803d" stroke-width="3"/>
    <!-- Scalloped disc -->
    <ellipse cx="110" cy="60" rx="28" ry="10" fill="#16a34a" stroke="#14532d" stroke-width="1.5"/>
    <text x="110" y="35" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">C (Antheridiophore)</text>
    <!-- Rhizoids -->
    <path d="M 60 190 L 50 210 M 80 195 L 75 215 M 120 195 L 125 215" stroke="#a16207" stroke-width="1.5"/>
    <text x="110" y="210" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Male Thallus</text>
  </g>
</svg>"""

SVG_PLANT_LIFE_CYCLES = """<svg viewBox="0 0 540 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Cycle A: Haplontic -->
  <g transform="translate(10, 10)">
    <rect x="10" y="10" width="150" height="150" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
    <text x="85" y="30" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Haplontic (A)</text>
    <path d="M 40 90 A 45 45 0 1 1 130 90" fill="none" stroke="#16a34a" stroke-width="4"/>
    <path d="M 130 90 A 45 45 0 0 1 40 90" fill="none" stroke="#dc2626" stroke-width="4"/>
    <text x="85" y="70" fill="#15803d" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">Gametophyte (n)</text>
    <text x="85" y="125" fill="#b91c1c" font-size="9" font-family="system-ui" text-anchor="middle">Zygote (2n) only</text>
    <text x="85" y="150" fill="#047857" font-size="9" font-family="system-ui" text-anchor="middle">Volvox, Spirogyra</text>
  </g>

  <!-- Cycle B: Diplontic -->
  <g transform="translate(185, 10)">
    <rect x="10" y="10" width="150" height="150" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
    <text x="85" y="30" fill="#b91c1c" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Diplontic (B)</text>
    <path d="M 40 90 A 45 45 0 1 1 130 90" fill="none" stroke="#dc2626" stroke-width="4"/>
    <path d="M 130 90 A 45 45 0 0 1 40 90" fill="none" stroke="#16a34a" stroke-width="4"/>
    <text x="85" y="70" fill="#b91c1c" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">Sporophyte (2n)</text>
    <text x="85" y="125" fill="#15803d" font-size="9" font-family="system-ui" text-anchor="middle">Gametes (n) only</text>
    <text x="85" y="150" fill="#991b1b" font-size="9" font-family="system-ui" text-anchor="middle">Gymno, Angio, Fucus</text>
  </g>

  <!-- Cycle C: Haplodiplontic -->
  <g transform="translate(360, 10)">
    <rect x="10" y="10" width="165" height="150" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="92" y="30" fill="#1d4ed8" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Haplodiplontic (C)</text>
    <path d="M 47 90 A 45 45 0 1 1 137 90" fill="none" stroke="#16a34a" stroke-width="4"/>
    <path d="M 137 90 A 45 45 0 0 1 47 90" fill="none" stroke="#dc2626" stroke-width="4"/>
    <text x="92" y="65" fill="#15803d" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Gametophyte (n)</text>
    <text x="92" y="125" fill="#b91c1c" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Sporophyte (2n)</text>
    <text x="92" y="150" fill="#1e40af" font-size="8.5" font-family="system-ui" text-anchor="middle">Bryo, Pterido, Kelps</text>
  </g>
</svg>"""

SVG_FERN_PROTHALLUS = """<svg viewBox="0 0 320 230" width="100%" height="230" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Heart-shaped prothallus -->
  <path d="M 160 50 C 130 10 70 20 60 70 C 50 120 110 180 160 210 C 210 180 270 120 260 70 C 250 20 190 10 160 50 Z" fill="#bbf7d0" stroke="#16a34a" stroke-width="2.5"/>
  <!-- Apical notch (A) -->
  <circle cx="160" cy="50" r="4" fill="#15803d"/>
  <line x1="160" y1="50" x2="160" y2="20" stroke="#15803d" stroke-width="1.5"/>
  <text x="160" y="15" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">A (Apical Notch)</text>
  <!-- Archegonia near notch (B) -->
  <g fill="#ec4899" stroke="#be185d" stroke-width="1">
    <circle cx="150" cy="80" r="4"/>
    <circle cx="160" cy="75" r="4"/>
    <circle cx="170" cy="80" r="4"/>
    <circle cx="155" cy="92" r="4"/>
    <circle cx="165" cy="92" r="4"/>
  </g>
  <line x1="170" y1="80" x2="225" y2="80" stroke="#be185d" stroke-width="1.5"/>
  <text x="230" y="84" fill="#9d174d" font-size="10" font-weight="bold" font-family="system-ui">B (Archegonia)</text>
  <!-- Antheridia among rhizoids (C) -->
  <g fill="#0284c7" stroke="#0369a1" stroke-width="1">
    <circle cx="140" cy="140" r="3.5"/>
    <circle cx="175" cy="145" r="3.5"/>
    <circle cx="150" cy="160" r="3.5"/>
    <circle cx="168" cy="165" r="3.5"/>
  </g>
  <line x1="135" y1="140" x2="80" y2="140" stroke="#0369a1" stroke-width="1.5"/>
  <text x="75" y="144" fill="#0369a1" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="end">C (Antheridia)</text>
  <!-- Rhizoids at base (D) -->
  <path d="M 155 180 L 140 215 M 160 190 L 160 225 M 165 185 L 180 220 M 150 170 L 130 200" stroke="#a16207" stroke-width="1.5"/>
  <text x="160" y="225" fill="#78350f" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">D (Rhizoids)</text>
</svg>"""

SVG_COELOM_TYPES = """<svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- (A) Eucoelomate (Coelomate) -->
  <g transform="translate(10, 10)">
    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
    <!-- Mesoderm lining body wall and gut with true cavity -->
    <circle cx="80" cy="80" r="60" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>
    <!-- Coelom cavity (white) -->
    <circle cx="80" cy="80" r="48" fill="#ffffff" stroke="#ef4444" stroke-width="1"/>
    <!-- Gut with mesoderm lining -->
    <circle cx="80" cy="80" r="28" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>
    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Gut</text>
    <text x="80" y="48" fill="#b91c1c" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Coelom</text>
    <text x="80" y="168" fill="#991b1b" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">A: Coelomate</text>
  </g>

  <!-- (B) Pseudocoelomate -->
  <g transform="translate(180, 10)">
    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
    <!-- Pseudocoelom cavity space -->
    <circle cx="80" cy="80" r="60" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
    <!-- Scattered mesodermal pouches -->
    <circle cx="50" cy="60" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>
    <circle cx="110" cy="60" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>
    <circle cx="50" cy="100" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>
    <circle cx="110" cy="100" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>
    <!-- Endodermal gut -->
    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Gut</text>
    <text x="80" y="168" fill="#0369a1" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">B: Pseudocoelomate</text>
  </g>

  <!-- (C) Acoelomate -->
  <g transform="translate(350, 10)">
    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
    <!-- Solid mesoderm (parenchyma) without any cavity -->
    <circle cx="80" cy="80" r="60" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>
    <!-- Endodermal gut -->
    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Gut</text>
    <text x="80" y="45" fill="#991b1b" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Parenchyma</text>
    <text x="80" y="168" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">C: Acoelomate</text>
  </g>
</svg>"""

SVG_CHORDATE_BODY_PLAN = """<svg viewBox="0 0 520 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- General chordate fish-like body outline -->
  <path d="M 40 100 Q 150 20 400 30 Q 480 70 500 100 Q 480 130 400 170 Q 150 180 40 100 Z" fill="#f0f9ff" stroke="#0284c7" stroke-width="2.5"/>
  
  <!-- 1. Nerve cord (Dorsal hollow nerve cord, green, labeled A) -->
  <path d="M 90 55 Q 250 40 450 65" fill="none" stroke="#16a34a" stroke-width="4"/>
  <text x="250" y="45" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">A (Dorsal Hollow Nerve Cord)</text>
  
  <!-- 2. Notochord (Blue solid rod under nerve cord, labeled B) -->
  <path d="M 70 75 Q 250 60 465 85" fill="none" stroke="#2563eb" stroke-width="6" stroke-linecap="round"/>
  <text x="250" y="80" fill="#1d4ed8" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">B (Notochord)</text>
  
  <!-- Gut tube -->
  <path d="M 40 100 Q 160 110 360 140" fill="none" stroke="#ca8a04" stroke-width="3"/>
  <circle cx="360" cy="140" r="4" fill="#a16207"/>
  <text x="360" y="158" fill="#a16207" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">Anus</text>
  
  <!-- 3. Pharyngeal Gill Slits (labeled C) -->
  <g stroke="#dc2626" stroke-width="3" stroke-linecap="round">
    <line x1="120" y1="95" x2="120" y2="120"/>
    <line x1="135" y1="95" x2="135" y2="120"/>
    <line x1="150" y1="95" x2="150" y2="120"/>
    <line x1="165" y1="95" x2="165" y2="120"/>
  </g>
  <text x="142" y="145" fill="#b91c1c" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">C (Pharyngeal Gill Slits)</text>
  
  <!-- 4. Post-anal tail (labeled D) -->
  <path d="M 360 140 Q 420 160 500 100" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-dasharray="3,2"/>
  <text x="440" y="160" fill="#6d28d9" font-size="10" font-weight="bold" font-family="system-ui">D (Post-anal tail)</text>
</svg>"""

SVG_CNIDARIAN_BODY_FORMS = """<svg viewBox="0 0 460 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">
  <!-- Polyp Form (Hydra / Adamsia) -->
  <g transform="translate(40, 20)">
    <!-- Cylindrical stalk attached at base -->
    <path d="M 40 160 L 40 60 Q 60 70 80 60 L 80 160 Z" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
    <!-- Tentacles directed upwards -->
    <path d="M 45 60 Q 30 20 20 10 M 55 63 Q 50 15 60 5 M 65 63 Q 70 15 65 5 M 75 60 Q 90 20 100 10" fill="none" stroke="#1d4ed8" stroke-width="2.5" stroke-linecap="round"/>
    <!-- Mouth on hypostome -->
    <circle cx="60" cy="60" r="4" fill="#ef4444"/>
    <text x="60" y="75" fill="#dc2626" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Mouth</text>
    <text x="60" y="180" fill="#1e40af" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Polyp (A)</text>
    <text x="60" y="195" fill="#3b82f6" font-size="9" font-family="system-ui" text-anchor="middle">Sessile &amp; Cylindrical</text>
  </g>

  <!-- Medusa Form (Aurelia / Jelly fish) -->
  <g transform="translate(260, 20)">
    <!-- Umbrella shaped bell -->
    <path d="M 20 80 Q 80 15 140 80 Q 80 90 20 80 Z" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
    <!-- Mouth directed downwards on manubrium -->
    <rect x="70" y="85" width="20" height="30" fill="#fca5a5" stroke="#b91c1c" stroke-width="1.5"/>
    <circle cx="80" cy="115" r="4" fill="#7f1d1d"/>
    <text x="80" y="130" fill="#991b1b" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Mouth</text>
    <!-- Marginal tentacles hanging down -->
    <path d="M 25 82 Q 20 130 15 160 M 45 86 Q 40 130 45 165 M 115 86 Q 120 130 115 165 M 135 82 Q 140 130 145 160" fill="none" stroke="#e11d48" stroke-width="2" stroke-linecap="round"/>
    <text x="80" y="180" fill="#991b1b" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Medusa (B)</text>
    <text x="80" y="195" fill="#e11d48" font-size="9" font-family="system-ui" text-anchor="middle">Free-swimming &amp; Umbrella</text>
  </g>
</svg>"""


# -----------------------------------------------------------------------------
# ALL 585 BIOLOGY QUESTIONS (Direct List)
# -----------------------------------------------------------------------------

biology_questions = [
    {
        "id": 'BIO-001',
        "exam": 'NEET, AIIMS, AFMC, CUET, IAT, OLYMPIAD, ICAR',
        "subject": 'Biology',
        "topic": 'Cell Biology',
        "difficulty": 'Easy',
        "en": 'Which of the following cell organelles is responsible for the synthesis of ribosomal RNA (rRNA)?',
        "bn": 'কোষের কোন অঙ্গাণুটি রাইবোজোমাল আরএনএ (rRNA) সংশ্লেষণের জন্য দায়ী?',
        "opts": {
            "en": ['Nucleolus', 'Golgi apparatus', 'Lysosome', 'Endoplasmic reticulum'],
            "bn": ['নিউক্লিওলাস', 'গলগি বডি', 'লাইসোজোম', 'এন্ডোপ্লাজমিক রেটিকুলাম']
        },
        "correct": 0,
        "expl_en": 'The nucleolus is the distinct, non-membrane bound sub-nuclear structure dedicated to the transcription and processing of ribosomal RNA (rRNA) and ribosome assembly.',
        "expl_bn": 'নিউক্লিওলাস হলো নিউক্লিয়াসের অভ্যন্তরে অবস্থিত প্রধান কেন্দ্র যেখানে rRNA সংশ্লেষিত হয়।',
    },
    {
        "id": 'BIO-002',
        "exam": 'NEET, AIIMS, AFMC, CUET, IAT, OLYMPIAD, ICAR, CSIR-NET',
        "subject": 'Biology',
        "topic": 'Genetics & Molecular Basis',
        "difficulty": 'Medium',
        "en": 'In a DNA molecule, if cytosine accounts for 18% of the total nitrogenous bases, the percentage of adenine present in that DNA is:',
        "bn": 'একটি ডিএনএ অণুতে যদি সাইটোসিন ১৮% থাকে, তবে ওই ডিএনএ-তে অ্যাডেনিনের শতকরা পরিমাণ কত?',
        "opts": {
            "en": ['32%', '18%', '36%', '64%'],
            "bn": ['32%', '18%', '36%', '64%']
        },
        "correct": 0,
        "expl_en": "According to Chargaff's rules: %G = %C = 18%. Total (G + C) = 36%. Therefore, %A + %T = 100% - 36% = 64%. Since %A = %T, %Adenine = 64% / 2 = 32%.",
        "expl_bn": 'শারগাফের নিয়ম অনুসারে: %G = %C = ১৮%। অতএব %A + %T = ১০০ - ৩৬ = ৬৪%। সুতরাং %অ্যাডেনিন = ৬৪/২ = ৩২%।',
    },
    {
        "id": 'BIO-003',
        "exam": 'NEET, AIIMS, AFMC, CUET, IAT',
        "subject": 'Biology',
        "topic": 'Human Physiology',
        "difficulty": 'Medium',
        "en": 'Which hormone is directly responsible for stimulating the reabsorption of water from the distal convoluted tubules and collecting ducts of the nephron?',
        "bn": 'নেফ্রনের দূরবর্তী সংবর্তন নালিকা ও সংগ্রাহী নালিকা থেকে পানি পুনর্শোষণ উদ্দীপিত করার জন্য কোন হরমোনটি প্রত্যক্ষভাবে দায়ী?',
        "opts": {
            "en": ['Antidiuretic Hormone (ADH / Vasopressin)', 'Oxytocin', 'Aldosterone', 'Glucagon'],
            "bn": ['অ্যান্টিডাইইউরেটিক হরমোন (ADH / ভেসোপ্রেসিন)', 'অক্সিটোসিন', 'অ্যালডোস্টেরন', 'গ্লুকাগন']
        },
        "correct": 0,
        "expl_en": 'Antidiuretic hormone (ADH / Vasopressin), released from the posterior pituitary, increases aquaporin channel insertion into collecting ducts to conserve body water.',
        "expl_bn": 'পশ্চাৎ পিটুইটারি থেকে ক্ষরিত ADH বা ভেসোপ্রেসিন বৃক্কে পানির পুনঃশোষণ বৃদ্ধি করে।',
    },
    {
        "id": 'BIO-004',
        "exam": 'NEET, AIIMS, AFMC, CUET, IAT, OLYMPIAD, CSIR-NET',
        "subject": 'Biology',
        "topic": 'Human Health and Disease',
        "difficulty": 'Hard',
        "en": 'The accompanying graph depicts antibody titer in blood serum following primary and secondary antigen exposures. Which immunoglobulin class is predominantly responsible for the rapid, high-magnitude peak observed in the secondary immune response?',
        "bn": 'সংযুক্ত লেখচিত্রটিতে প্রাথমিক ও গৌণ অ্যান্টিজেন সংস্পর্শের পর সিরামে অ্যান্টিবডির মাত্রা দেখানো হয়েছে। গৌণ অনাক্রম্য সাড়ায় (Secondary response) দ্রুত ও উচ্চ মাত্রার অ্যান্টিবডি নিঃসরণের জন্য প্রধানত কোন ইমিউনোগ্লোবুলিন দায়ী?',
        "opts": {
            "en": ['IgG', 'IgM', 'IgE', 'IgA'],
            "bn": ['IgG', 'IgM', 'IgE', 'IgA']
        },
        "correct": 0,
        "expl_en": 'The primary immune response predominantly produces IgM with lower affinity and a lag phase. Memory B-cells generated during the primary response facilitate class switching to produce massive titers of high-affinity IgG during the secondary immune response.',
        "expl_bn": 'প্রাথমিক অনাক্রম্যতায় প্রধানত IgM উৎপন্ন হয়, কিন্তু মেমরি বি-কোষের উপস্থিতির কারণে গৌণ অনাক্রম্যতায় অত্যন্ত দ্রুত ও বিপুল পরিমাণে IgG অ্যান্টিবডি ক্ষরিত হয়।',
        "diagram": '<svg viewBox="0 0 520 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Axes -->\n  <line x1="50" y1="175" x2="480" y2="175" stroke="#334155" stroke-width="2"/>\n  <line x1="50" y1="175" x2="50" y2="25" stroke="#334155" stroke-width="2"/>\n  <text x="440" y="195" fill="#334155" font-size="11" font-family="system-ui" font-weight="bold">Time (Days)</text>\n  <text x="55" y="20" fill="#334155" font-size="11" font-family="system-ui" font-weight="bold">Antibody Titer in Serum (log scale)</text>\n  \n  <!-- Primary Response Curve -->\n  <path d="M 70 175 Q 110 175 140 105 Q 170 115 210 160" fill="none" stroke="#2563eb" stroke-width="3"/>\n  <text x="140" y="90" fill="#1d4ed8" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">Primary Response (IgM)</text>\n  \n  <!-- Secondary Exposure Point -->\n  <line x1="250" y1="175" x2="250" y2="130" stroke="#dc2626" stroke-dasharray="2 2" stroke-width="1.5"/>\n  <text x="250" y="125" fill="#dc2626" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">2nd Exposure</text>\n  \n  <!-- Secondary Response Curve (Much higher & faster) -->\n  <path d="M 250 160 Q 280 40 330 35 Q 400 45 470 95" fill="none" stroke="#dc2626" stroke-width="3.5"/>\n  <text x="350" y="28" fill="#b91c1c" font-size="13" font-family="system-ui" font-weight="black" text-anchor="middle">Secondary Response (High IgG)</text>\n</svg>',
    },
    {
        "id": 'BIO-005',
        "exam": 'NEET, AIIMS, AFMC, CUET, IAT, ICAR',
        "subject": 'Biology',
        "topic": 'Human Health and Disease',
        "difficulty": 'Medium',
        "en": 'In the standard Y-shaped immunoglobulin monomer (H₂L₂), how many inter-chain and intra-chain disulfide bonds typically connect the heavy (H) and light (L) polypeptide chains?',
        "bn": 'একটি আদর্শ Y-আকৃতির ইমিউনোগ্লোবুলিন মনোমারে (H₂L₂) ভারী (H) এবং হালকা (L) পলিপেপটাইড শৃঙ্খলগুলো প্রধানত কোন রাসায়নিক বন্ধন দ্বারা পরস্পরের সাথে আবদ্ধ থাকে?',
        "opts": {
            "en": ['Disulfide bridges (—S—S—)', 'Glycosidic linkages', 'Phosphodiester bonds', 'Ester bonds'],
            "bn": ['ডাইসালফাইড বন্ধন (—S—S—)', 'গ্লাইকোসাইডিক বন্ধন', 'ফসফোডাইএস্টার বন্ধন', 'এস্টার বন্ধন']
        },
        "correct": 0,
        "expl_en": 'Antibody molecules are glycoproteins composed of 2 heavy and 2 light polypeptide chains held firmly together by inter-chain covalent disulfide bridges (—S—S— bonds).',
        "expl_bn": 'অ্যান্টিবডি অণুতে ২টি ভারী এবং ২টি হালকা শৃঙ্খল পরস্পরের সাথে সমযোজী ডাইসালফাইড বন্ধন (—S—S—) দ্বারা দৃঢ়ভাবে যুক্ত থাকে।',
        "diagram": '<svg viewBox="0 0 420 230" width="100%" height="230" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Heavy Chains (Blue) -->\n  <path d="M 120 40 L 190 110 L 190 200" fill="none" stroke="#2563eb" stroke-width="8" stroke-linecap="round"/>\n  <path d="M 300 40 L 230 110 L 230 200" fill="none" stroke="#2563eb" stroke-width="8" stroke-linecap="round"/>\n  <!-- Light Chains (Cyan) -->\n  <path d="M 80 65 L 145 125" fill="none" stroke="#06b6d4" stroke-width="7" stroke-linecap="round"/>\n  <path d="M 340 65 L 275 125" fill="none" stroke="#06b6d4" stroke-width="7" stroke-linecap="round"/>\n  <!-- Disulfide bonds -->\n  <line x1="190" y1="135" x2="230" y2="135" stroke="#eab308" stroke-width="3"/>\n  <line x1="190" y1="150" x2="230" y2="150" stroke="#eab308" stroke-width="3"/>\n  <line x1="125" y1="105" x2="140" y2="120" stroke="#eab308" stroke-width="3"/>\n  <line x1="295" y1="105" x2="280" y2="120" stroke="#eab308" stroke-width="3"/>\n  <text x="70" y="30" fill="#0e7490" font-size="12" font-family="system-ui" font-weight="bold">Antigen-Binding Site (Fab)</text>\n  <text x="350" y="30" fill="#0e7490" font-size="12" font-family="system-ui" font-weight="bold">Antigen-Binding Site (Fab)</text>\n  <text x="210" y="215" fill="#1e3a8a" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">Fc Region (Constant)</text>\n  <text x="50" y="100" fill="#0891b2" font-size="11" font-family="system-ui">Light Chain (L)</text>\n  <text x="250" y="170" fill="#1d4ed8" font-size="11" font-family="system-ui">Heavy Chain (H₂L₂)</text>\n</svg>',
    },
    {
        "id": 'BIO-006',
        "exam": 'NEET, AIIMS, AFMC, CUET, IAT, OLYMPIAD, CSIR-NET',
        "subject": 'Biology',
        "topic": 'Molecular Basis of Inheritance',
        "difficulty": 'Medium',
        "en": 'In the Lac operon of Escherichia coli, which structural gene specifically codes for the enzyme β-galactosidase that catalyzes the hydrolysis of lactose into galactose and glucose?',
        "bn": 'Escherichia coli-এর ল্যাক ওপেরনে (Lac Operon), কোন গাঠনিক জিনটি সরাসরি β-গ্যালাক্টোসিডেজ উৎসেচক সংশ্লেষণ করে যা ল্যাকটোজকে গ্লুকোজ ও গ্যালাক্টোজে আর্দ্রবিশ্লেষিত করে?',
        "opts": {
            "en": ['z gene', 'y gene', 'a gene', 'i gene'],
            "bn": ['z জিন', 'y জিন', 'a জিন', 'i জিন']
        },
        "correct": 0,
        "expl_en": "In the lac operon: gene 'z' codes for β-galactosidase, gene 'y' codes for β-galactoside permease, gene 'a' codes for β-galactoside transacetylase, and gene 'i' codes for the repressor protein.",
        "expl_bn": "ল্যাক ওপেরনে: 'z' জিন β-গ্যালাক্টোসিডেজ সংশ্লেষ করে, 'y' জিন পারমিয়েজ এনজাইম এবং 'a' জিন ট্রান্সঅ্যাসিটাইলেজ সংশ্লেষ করে। 'i' জিন রিপ্রেসার প্রোটিন তৈরি করে।",
        "diagram": '<svg viewBox="0 0 540 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- DNA Strip -->\n  <rect x="20" y="60" width="500" height="40" rx="6" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n  <!-- Genes -->\n  <rect x="30" y="65" width="60" height="30" rx="4" fill="#cbd5e1"/><text x="60" y="85" fill="#0f172a" font-size="12" font-family="monospace" font-weight="bold" text-anchor="middle">p(i)</text>\n  <rect x="95" y="65" width="70" height="30" rx="4" fill="#fed7aa"/><text x="130" y="85" fill="#9a3412" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">i (rep)</text>\n  <rect x="170" y="65" width="60" height="30" rx="4" fill="#cbd5e1"/><text x="200" y="85" fill="#0f172a" font-size="12" font-family="monospace" font-weight="bold" text-anchor="middle">P</text>\n  <rect x="235" y="65" width="55" height="30" rx="4" fill="#bbf7d0"/><text x="262" y="85" fill="#166534" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">O</text>\n  <rect x="295" y="65" width="75" height="30" rx="4" fill="#bfdbfe"/><text x="332" y="85" fill="#1e40af" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">z (β-gal)</text>\n  <rect x="375" y="65" width="70" height="30" rx="4" fill="#ddd6fe"/><text x="410" y="85" fill="#5b21b6" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">y (perm)</text>\n  <rect x="450" y="65" width="65" height="30" rx="4" fill="#fbcfe8"/><text x="482" y="85" fill="#9d174d" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">a (trans)</text>\n  <text x="270" y="140" fill="#0f172a" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">Lac Operon Regulatory Unit in E. coli</text>\n</svg>',
    },
    {
        "id": 'BIO-007',
        "exam": 'NEET, AIIMS, AFMC, CUET, IAT, ICAR',
        "subject": 'Biology',
        "topic": 'Plant Physiology & Photosynthesis',
        "difficulty": 'Medium',
        "en": 'In C₄ plants such as maize and sugarcane, carbon dioxide fixation occurs through the Hatch and Slack pathway. The primary CO₂ acceptor molecule and the initial carboxylating enzyme present in the mesophyll cells are respectively:',
        "bn": 'ভুট্টা এবং আখের মতো C₄ উদ্ভিদে হ্যাচ ও স্ল্যাক চক্রের মাধ্যমে কার্বন ডাইঅক্সাইড সংবন্ধন ঘটে। মেসোফিল কোষে প্রাথমিক CO₂ গ্রাহক অণু এবং প্রাথমিক কার্বক্সিলেটিং উৎসেচক যথাক্রমে কোনটি?',
        "opts": {
            "en": ['Phosphoenolpyruvate (PEP) and PEP carboxylase', 'Ribulose-1,5-bisphosphate (RuBP) and RuBisCO', 'Oxaloacetic acid (OAA) and Malic dehydrogenase', 'Phosphoglyceric acid (PGA) and RuBisCO'],
            "bn": ['ফসফোএনলপাইরুভেট (PEP) এবং PEP কার্বক্সিলেজ', 'রিবুলোজ-১,৫-বিসফসফেট (RuBP) এবং RuBisCO', 'অক্সালোঅ্যাসিটিক অ্যাসিড (OAA) এবং ম্যালিক ডিহাইড্রোজিনেজ', 'ফসফোগ্লিসারিক অ্যাসিড (PGA) এবং RuBisCO']
        },
        "correct": 0,
        "expl_en": 'In C₄ plants showing Kranz anatomy, the primary CO₂ acceptor in the mesophyll cytoplasm is the 3-carbon phosphoenolpyruvate (PEP), catalyzed by PEP carboxylase (PEPcase) to form 4-carbon oxaloacetic acid (OAA). RuBisCO is absent in mesophyll cells and restricted to bundle sheath cells.',
        "expl_bn": 'ক্র্যাঞ্জ শারীরস্থান বিশিষ্ট C₄ উদ্ভিদের মেসোফিল কোষে প্রাথমিক CO₂ গ্রাহক হলো ফসফোএনলপাইরুভেট (PEP), যা PEP কার্বক্সিলেজ দ্বারা অনুঘটক হয়ে অক্সালোঅ্যাসিটিক অ্যাসিড (OAA) তৈরি করে। মেসোফিল কোষে RuBisCO থাকে না, এটি বান্ডিল সিথ কোষে থাকে।',
        "diagram": '<svg viewBox="0 0 520 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <circle cx="260" cy="105" r="30" fill="#fed7aa" stroke="#c2410c" stroke-width="2"/>\n  <text x="260" y="103" fill="#9a3412" font-size="10" font-family="system-ui" font-weight="bold" text-anchor="middle">Vascular</text>\n  <text x="260" y="117" fill="#9a3412" font-size="10" font-family="system-ui" font-weight="bold" text-anchor="middle">Bundle</text>\n  <circle cx="260" cy="105" r="58" fill="none" stroke="#16a34a" stroke-width="22" stroke-opacity="0.25"/>\n  <circle cx="208" cy="105" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>\n  <circle cx="312" cy="105" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>\n  <circle cx="260" cy="53" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>\n  <circle cx="260" cy="157" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>\n  <circle cx="223" cy="68" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>\n  <circle cx="297" cy="68" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>\n  <circle cx="223" cy="142" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>\n  <circle cx="297" cy="142" r="11" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>\n  <rect x="60" y="30" width="100" height="40" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>\n  <text x="110" y="48" fill="#166534" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Mesophyll Cell</text>\n  <text x="110" y="62" fill="#15803d" font-size="9" font-family="system-ui" text-anchor="middle">PEPcase (C₄ Acid)</text>\n  <line x1="160" y1="50" x2="220" y2="70" stroke="#16a34a" stroke-width="1.5"/>\n  <rect x="360" y="30" width="130" height="40" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>\n  <text x="425" y="48" fill="#92400e" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Bundle Sheath Cell</text>\n  <text x="425" y="62" fill="#b45309" font-size="9" font-family="system-ui" text-anchor="middle">RuBisCO (Calvin Cycle)</text>\n  <line x1="360" y1="50" x2="300" y2="70" stroke="#d97706" stroke-width="1.5"/>\n  <text x="260" y="195" fill="#0f172a" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">Kranz Anatomy in C₄ Plants (Maize, Sugarcane) • Zero Photorespiration</text>\n</svg>',
    },
    {
        "id": 'BIO-008',
        "exam": 'NEET, AIIMS, AFMC, CUET, IAT',
        "subject": 'Biology',
        "topic": 'Human Physiology & Locomotion',
        "difficulty": 'Medium',
        "en": 'According to the sliding filament mechanism of skeletal muscle contraction, when calcium ions (Ca²⁺) bind to troponin C on actin filaments, which of the following structural changes occurs in the sarcomere?',
        "bn": 'কঙ্কাল পেশি সংকোচনের স্লাইডিং ফিলামেন্ট তত্ত্ব অনুসারে, যখন ক্যালসিয়াম আয়ন (Ca²⁺) অ্যাক্টিন ফিলামেন্টের ট্রপোনিন C-এর সাথে যুক্ত হয়, তখন সারকোমিয়ারে নিচের কোন গাঠনিক পরিবর্তনটি ঘটে?',
        "opts": {
            "en": ['The H-zone and I-band narrow while the length of the A-band remains constant', 'The A-band shortens while the I-band and Z-lines remain stationary', 'Both the A-band and I-band lengthen as myosin filaments stretch', 'The Z-lines move apart and the H-zone widens'],
            "bn": ['H-অঞ্চল এবং I-ব্যান্ড সংকীর্ণ হয় কিন্তু A-ব্যান্ডের দৈর্ঘ্য অপরিবর্তিত থাকে', 'A-ব্যান্ড ছোট হয় কিন্তু I-ব্যান্ড এবং Z-রেখা স্থির থাকে', 'মায়োসিন প্রসারিত হওয়ায় A-ব্যান্ড এবং I-ব্যান্ড উভয়ই দীর্ঘায়িত হয়', 'Z-রেখা দুটি দূরে সরে যায় এবং H-অঞ্চল প্রসারিত হয়']
        },
        "correct": 0,
        "expl_en": 'During contraction, actin filaments slide over myosin filaments toward the M-line. Consequently, the I-bands shorten, the central H-zone narrows/disappears, while the length of the dark A-band (representing thick myosin filaments) remains strictly constant.',
        "expl_bn": 'পেশি সংকোচনের সময় অ্যাক্টিন ফিলামেন্ট মায়োসিনের ওপর দিয়ে কেন্দ্রের দিকে সরে যায়। ফলে I-ব্যান্ড এবং H-অঞ্চল সংকুচিত হয়, কিন্তু মায়োসিন ফিলামেন্টের দৈর্ঘ্য নির্দেশক A-ব্যান্ডের দৈর্ঘ্য সর্বদা স্থির থাকে।',
        "diagram": '<svg viewBox="0 0 540 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <line x1="60" y1="20" x2="60" y2="160" stroke="#1e3a8a" stroke-width="3"/>\n  <text x="60" y="175" fill="#1e3a8a" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Z-line</text>\n  <line x1="480" y1="20" x2="480" y2="160" stroke="#1e3a8a" stroke-width="3"/>\n  <text x="480" y="175" fill="#1e3a8a" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Z-line</text>\n  <line x1="270" y1="20" x2="270" y2="160" stroke="#dc2626" stroke-dasharray="3 2" stroke-width="2"/>\n  <text x="270" y="175" fill="#dc2626" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">M-line</text>\n  <rect x="150" y="55" width="240" height="12" rx="3" fill="#dc2626"/>\n  <rect x="150" y="85" width="240" height="12" rx="3" fill="#dc2626"/>\n  <rect x="150" y="115" width="240" height="12" rx="3" fill="#dc2626"/>\n  <line x1="60" y1="45" x2="220" y2="45" stroke="#2563eb" stroke-width="3"/>\n  <line x1="60" y1="75" x2="220" y2="75" stroke="#2563eb" stroke-width="3"/>\n  <line x1="60" y1="105" x2="220" y2="105" stroke="#2563eb" stroke-width="3"/>\n  <line x1="60" y1="135" x2="220" y2="135" stroke="#2563eb" stroke-width="3"/>\n  <line x1="480" y1="45" x2="320" y2="45" stroke="#2563eb" stroke-width="3"/>\n  <line x1="480" y1="75" x2="320" y2="75" stroke="#2563eb" stroke-width="3"/>\n  <line x1="480" y1="105" x2="320" y2="105" stroke="#2563eb" stroke-width="3"/>\n  <line x1="480" y1="135" x2="320" y2="135" stroke="#2563eb" stroke-width="3"/>\n  <line x1="150" y1="30" x2="390" y2="30" stroke="#991b1b" stroke-width="1.5"/>\n  <text x="270" y="24" fill="#991b1b" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">A-Band (Constant Length)</text>\n  <line x1="220" y1="150" x2="320" y2="150" stroke="#ea580c" stroke-width="1.5"/>\n  <text x="270" y="145" fill="#ea580c" font-size="10" font-family="system-ui" font-weight="bold" text-anchor="middle">H-Zone</text>\n  <text x="270" y="195" fill="#0f172a" font-size="12" font-family="system-ui" font-weight="bold" text-anchor="middle">1 Sarcomere (Between two Z-discs) • Contraction reduces H-zone &amp; I-band</text>\n</svg>',
    },
    {
        "id": 'BIO-009',
        "exam": 'NEET, AIIMS, AFMC, CUET, IAT, CSIR-NET',
        "subject": 'Biology',
        "topic": 'Biotechnology & Molecular Techniques',
        "difficulty": 'Medium',
        "en": 'In agarose gel electrophoresis of DNA fragments, which of the following statements correctly describes the migration behavior and visualization of the separated fragments?',
        "bn": 'DNA খণ্ডকের অ্যাগারোজ জেল ইলেক্ট্রোফোরেসিসের ক্ষেত্রে, পৃথকীকৃত খণ্ডকগুলির চলন এবং দৃশ্যমানতার বিষয়ে নিচের কোন বক্তব্যটি সঠিক?',
        "opts": {
            "en": ['Negatively charged DNA fragments migrate toward the positive anode, with smaller fragments moving faster; bands appear bright orange under UV light after ethidium bromide staining', 'Positively charged DNA fragments migrate toward the negative cathode, with larger fragments moving faster; bands are directly visible under white light', 'DNA fragments migrate toward the anode with velocities independent of their base-pair sizes', 'Ethidium bromide stains DNA blue under infrared illumination'],
            "bn": ['ঋণাত্মক আধানযুক্ত DNA খণ্ডকগুলি ধনাত্মক অ্যানোডের দিকে ধাবিত হয়, ছোট খণ্ডকগুলি দ্রুত চলে; ইথিডিয়াম ব্রোমাইড রঞ্জনের পর UV আলোতে উজ্জ্বল কমলা রঙের ব্যান্ড দৃশ্যমান হয়', 'ধনাত্মক আধানযুক্ত DNA খণ্ডকগুলি ঋণাত্মক ক্যাথোডের দিকে ধাবিত হয়, বড় খণ্ডকগুলি দ্রুত চলে; সাদা আলোতে সরাসরি দৃশ্যমান হয়', 'DNA খণ্ডকগুলির অ্যানোডের দিকে চলন তাদের ক্ষার-জোড় (base pair) আকারের ওপর নির্ভর করে না', 'ইথিডিয়াম ব্রোমাইড অবলোহিত আলোতে DNA-কে নীল রঙে রঞ্জিত করে']
        },
        "correct": 0,
        "expl_en": "DNA's negative phosphate backbone drives migration toward the positive anode. Agarose acts as a sieve where smaller fragments move faster and farther. Staining with ethidium bromide (EtBr) followed by ultraviolet (UV) transillumination reveals bright orange fluorescent DNA bands.",
        "expl_bn": 'ফসফেট গ্রুপের ঋণাত্মক আধানের কারণে DNA অ্যানোডের দিকে অগ্রসর হয় এবং জেলের মধ্যে ছোট খণ্ডকগুলি দ্রুত চলে। ইথিডিয়াম ব্রোমাইড (EtBr) রঞ্জক যোগ করার পর অতিবেগুনি (UV) আলোয় দেখলে উজ্জ্বল কমলা রঙের ব্যান্ড প্রতীয়মান হয়।',
        "diagram": '<svg viewBox="0 0 500 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <rect x="50" y="30" width="400" height="150" rx="8" fill="#f8fafc" stroke="#475569" stroke-width="2"/>\n  <rect x="50" y="15" width="400" height="12" rx="3" fill="#3b82f6"/>\n  <text x="250" y="25" fill="#ffffff" font-size="10" font-family="system-ui" font-weight="bold" text-anchor="middle">Cathode (−)</text>\n  <rect x="50" y="183" width="400" height="12" rx="3" fill="#ef4444"/>\n  <text x="250" y="193" fill="#ffffff" font-size="10" font-family="system-ui" font-weight="bold" text-anchor="middle">Anode (+)</text>\n  <rect x="90" y="40" width="30" height="10" rx="2" fill="#334155"/>\n  <rect x="160" y="40" width="30" height="10" rx="2" fill="#334155"/>\n  <rect x="230" y="40" width="30" height="10" rx="2" fill="#334155"/>\n  <rect x="300" y="40" width="30" height="10" rx="2" fill="#334155"/>\n  <rect x="370" y="40" width="30" height="10" rx="2" fill="#334155"/>\n  <rect x="93" y="65" width="24" height="4" fill="#f97316"/>\n  <rect x="93" y="90" width="24" height="4" fill="#f97316"/>\n  <rect x="93" y="115" width="24" height="4" fill="#f97316"/>\n  <rect x="93" y="140" width="24" height="4" fill="#f97316"/>\n  <rect x="93" y="165" width="24" height="4" fill="#f97316"/>\n  <text x="105" y="58" fill="#64748b" font-size="9" font-family="system-ui" text-anchor="middle">Ladder</text>\n  <rect x="163" y="80" width="24" height="5" fill="#f97316"/>\n  <rect x="163" y="145" width="24" height="5" fill="#f97316"/>\n  <rect x="233" y="165" width="24" height="5" fill="#f97316"/>\n  <text x="245" y="155" fill="#ea580c" font-size="9" font-family="system-ui" font-weight="bold" text-anchor="middle">Smallest DNA</text>\n  <line x1="420" y1="50" x2="420" y2="160" stroke="#dc2626" stroke-width="2"/>\n  <polygon points="420,165 415,155 425,155" fill="#dc2626"/>\n  <text x="430" y="105" fill="#dc2626" font-size="10" font-family="system-ui" font-weight="bold" transform="rotate(90,430,105)" text-anchor="middle">Migration Direction</text>\n</svg>',
    },
    {
        "id": 'BIO-010',
        "exam": 'NEET, AIIMS, CUET, ICAR, UPSC, STATE-PSC',
        "subject": 'Biology',
        "topic": 'Ecosystem Dynamics & Energy Flow',
        "difficulty": 'Easy',
        "en": "According to Lindeman's 10 percent law of energy transfer in an ecosystem, if the primary producers (green plants) synthesize 20,000 J of energy through photosynthesis, how much energy will be available to the tertiary consumer (e.g., eagle or apex predator)?",
        "bn": 'বাস্তুতন্ত্রে শক্তি প্রবাহের লিন্ডেম্যানের ১০ শতাংশ সূত্র অনুসারে, প্রাথমিক উৎপাদকরা (সবুজ উদ্ভিদ) সালোকসংশ্লেষের মাধ্যমে ২০,০০০ J শক্তি উৎপাদন করলে, তৃতীয় স্তরের খাদক (যেমন ঈগল বা শীর্ষ শিকারী) কতটুকু শক্তি লাভ করবে?',
        "opts": {
            "en": ['20 J', '200 J', '2 J', '2,000 J'],
            "bn": ['20 J', '200 J', '2 J', '2,000 J']
        },
        "correct": 0,
        "expl_en": "Applying Lindeman's 10% law: Producers (T₁) = 20,000 J → Herbivores (T₂) = 2,000 J → Primary Carnivores (T₃) = 200 J → Tertiary Consumers (T₄) = 20 J.",
        "expl_bn": 'লিন্ডেম্যানের ১০% সূত্রানুসারে: উৎপাদক (T₁) = ২০,০০০ J → প্রাথমিক খাদক (T₂) = ২,০০০ J → গৌণ খাদক (T₃) = ২০০ J → তৃতীয় স্তরের খাদক (T₄) = ২০ J।',
    },
    {
        "id": 'BIO-011',
        "exam": 'NEET, AIIMS, AFMC, CUET, IAT, CSIR-NET',
        "subject": 'Biology',
        "topic": "Genetics & Morgan's Linkage Experiments",
        "difficulty": 'Hard',
        "en": 'In his seminal dihybrid crosses on Drosophila melanogaster, Thomas Hunt Morgan observed that genes located on the same chromosome did not assort independently. When crossing yellow-bodied, white-eyed females with wild-type brown-bodied, red-eyed males, the proportion of parental phenotypes versus recombinant types in the F₂ generation was:',
        "bn": 'ড্রোসোফিলা মেলানোগাস্টারের ওপর দ্বি-সংকরায়ন পরীক্ষায় থমাস হান্ট মর্গান লক্ষ্য করেন যে একই ক্রোমোজোমে অবস্থিত জিনগুলি স্বাধীনভাবে সঞ্চারিত হয় না। হলুদ দেহ ও সাদা চোখের স্ত্রী মাছির সাথে বুনো বাদামী দেহ ও লাল চোখের পুরুষ মাছির সংকরায়নে F₂ জনুতে অপত্যদের মধ্যে জনিতৃ বৈশিষ্ট্য এবং পুনর্বিন্যস্ত (রিকম্বিন্যান্ট) বৈশিষ্ট্যের অনুপাত কত ছিল?',
        "opts": {
            "en": ['98.7% Parental types and 1.3% Recombinant types', '62.8% Parental types and 37.2% Recombinant types', '50.0% Parental types and 50.0% Recombinant types', '75.0% Parental types and 25.0% Recombinant types'],
            "bn": ['৯৮.৭% জনিতৃ বৈশিষ্ট্য এবং ১.৩% রিকম্বিন্যান্ট বৈশিষ্ট্য', '৬২.৮% জনিতৃ বৈশিষ্ট্য এবং ৩৭.২% রিকম্বিন্যান্ট বৈশিষ্ট্য', '৫০.০% জনিতৃ বৈশিষ্ট্য এবং ৫০.০% রিকম্বিন্যান্ট বৈশিষ্ট্য', '৭৫.০% জনিতৃ বৈশিষ্ট্য এবং ২৫.০% রিকম্বিন্যান্ট বৈশিষ্ট্য']
        },
        "correct": 0,
        "expl_en": 'Morgan attributed the deviation from 9:3:3:1 to X-chromosome physical linkage. The genes for body colour (yellow) and eye colour (white) are very tightly linked, showing 98.7% parental combinations and only 1.3% crossing-over recombinants.',
        "expl_bn": 'মেন্ডেলীয় অনুপাত থেকে বিচ্যুতির কারণ হিসেবে মর্গান X-ক্রোমোজোমে জিনের সহসংযোজন বা লিংকেজ নির্দেশ করেন। হলুদ দেহ ও সাদা চোখের জিন দুটি দৃঢ়ভাবে সংলগ্ন থাকায় ৯৮.৭% জনিতৃ বৈশিষ্ট্য এবং মাত্র ১.৩% রিকম্বিন্যান্ট অপত্য তৈরি হয়েছিল।',
    },
    {
        "id": 'BIO-012',
        "exam": 'NEET, AIIMS, AFMC, CUET, IAT',
        "subject": 'Biology',
        "topic": 'Human Reproduction & Menstrual Cycle',
        "difficulty": 'Medium',
        "en": 'In the human female menstrual cycle of 28 days, ovulation (release of secondary oocyte from the mature Graafian follicle) is directly triggered by which endocrine event around day 14?',
        "bn": 'মানব স্ত্রীদেহে ২৮ দিনের রজঃচক্রের ক্ষেত্রে, ১৪তম দিনের কাছাকাছি পরিপক্ক গ্রাফিয়ান ফলিকল বিদীর্ণ হয়ে ডিম্বাণু নির্গমন (ওভিউলেশন) সরাসরি কোন হরমোনজনিত ঘটনার দ্বারা ঘটে?',
        "opts": {
            "en": ['A rapid surge in Luteinizing Hormone (LH surge) secreted by the anterior pituitary', 'A sharp drop in estrogen levels produced by the corpus luteum', 'Peak secretion of progesterone by developing primary follicles', 'A sudden drop in Follicle Stimulating Hormone (FSH) to baseline levels'],
            "bn": ['অগ্র পিটুইটারি থেকে নিঃসৃত লিউটিনাইজিং হরমোনের তীব্র বৃদ্ধি (LH সার্জ)', 'কর্পাস লিউটিয়াম দ্বারা উৎপাদিত ইস্ট্রোজেনের মাত্রায় আকস্মিক হ্রাস', 'বিকাশমান প্রাথমিক ফলিকল দ্বারা প্রোজেস্টেরনের সর্বোচ্চ ক্ষরণ', 'ফলিকল স্টিমুলেটিং হরমোনের (FSH) আকস্মিক পতন']
        },
        "correct": 0,
        "expl_en": "Around the 14th day of the cycle, rapid secretion of LH induces maximum mid-cycle concentration ('LH surge'), which causes rupture of the mature Graafian follicle and release of the ovum (ovulation).",
        "expl_bn": "চক্রের মধ্যভাগে (১৪তম দিনে) অগ্র পিটুইটারি থেকে লিউটিনাইজিং হরমোনের (LH) ক্ষরণ সর্বোচ্চ মাত্রায় পৌঁছায় ('LH সার্জ'), যা গ্রাফিয়ান ফলিকলকে বিদীর্ণ করে ডিম্বাণু নির্গমন বা ওভিউলেশন ঘটায়।",
        "diagram": '<svg viewBox="0 0 520 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <line x1="45" y1="160" x2="480" y2="160" stroke="#334155" stroke-width="2"/>\n  <line x1="45" y1="160" x2="45" y2="20" stroke="#334155" stroke-width="2"/>\n  <text x="45" y="180" fill="#334155" font-size="10" font-family="system-ui" font-weight="bold">Day 1</text>\n  <text x="240" y="180" fill="#dc2626" font-size="11" font-family="system-ui" font-weight="bold">Day 14 (Ovulation)</text>\n  <text x="460" y="180" fill="#334155" font-size="10" font-family="system-ui" font-weight="bold">Day 28</text>\n  <line x1="250" y1="160" x2="250" y2="25" stroke="#dc2626" stroke-dasharray="3 2" stroke-width="1.5"/>\n  <path d="M 50 145 Q 180 140 230 110 Q 250 25 270 120 Q 350 145 475 145" fill="none" stroke="#dc2626" stroke-width="3"/>\n  <text x="260" y="40" fill="#dc2626" font-size="11" font-family="system-ui" font-weight="bold">LH Surge</text>\n  <path d="M 50 150 Q 150 145 220 70 Q 250 110 320 100 Q 400 135 475 150" fill="none" stroke="#2563eb" stroke-width="2.5"/>\n  <text x="200" y="60" fill="#2563eb" font-size="10" font-family="system-ui" font-weight="bold">Estrogen</text>\n  <path d="M 50 155 L 250 155 Q 350 65 420 80 Q 460 130 475 155" fill="none" stroke="#16a34a" stroke-width="2.5"/>\n  <text x="375" y="75" fill="#16a34a" font-size="10" font-family="system-ui" font-weight="bold">Progesterone</text>\n  <text x="260" y="198" fill="#475569" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">LH Surge triggers rupture of Graafian Follicle and Ovulation at Day 14</text>\n</svg>',
    },
    {
        "id": 'BIO-013',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'The Living World & Taxonomic Hierarchy',
        "difficulty": 'Easy',
        "en": 'According to the taxonomic hierarchy, which of the following categories includes all the others?',
        "bn": 'শ্রেণিবিন্যাসীয় ক্রমপরম্পরা (taxonomic hierarchy) অনুসারে নিচের কোন ক্যাটাগরিটি বাকি সকলকে অন্তর্ভুক্ত করে?',
        "opts": {
            "en": ['Order', 'Family', 'Genus', 'Species'],
            "bn": ['বর্গ (Order)', 'গোত্র (Family)', 'গণ (Genus)', 'প্রজাতি (Species)']
        },
        "correct": 0,
        "expl_en": "The ascending order of taxonomic hierarchy is: Species → Genus → Family → Order → Class → Phylum/Division → Kingdom. Thus, 'Order' is higher than Family, Genus, and Species, and includes all of them.",
        "expl_bn": "ট্যাক্সোনমিক ক্রম হলো: প্রজাতি → গণ → গোত্র → বর্গ → শ্রেণী → পর্ব → রাজ্য। অতএব 'বর্গ' (Order) গোত্র, গণ ও প্রজাতিকে অন্তর্ভুক্ত করে।",
    },
    {
        "id": 'BIO-014',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification & Monera',
        "difficulty": 'Easy',
        "en": 'Methanogens belong to which of the following groups and are responsible for the production of biogas from the dung of ruminants?',
        "bn": 'মিথেনোজেন কোন গোষ্ঠীর অন্তর্ভুক্ত এবং রোমন্থক প্রাণীদের গোবর থেকে বায়োগ্যাস উৎপাদনে ভূমিকা রাখে?',
        "opts": {
            "en": ['Archaebacteria', 'Eubacteria', 'Dinoflagellates', 'Slime moulds'],
            "bn": ['আর্কিব্যাকটেরিয়া', 'ইউব্যাকটেরিয়া', 'ডাইনোফ্ল্যাজেলেট', 'স্লাইম মোল্ড']
        },
        "correct": 0,
        "expl_en": 'Methanogens are Archaebacteria that live in marshy areas and in the gut of several ruminant animals (cows, buffaloes). They produce methane (biogas) from animal dung.',
        "expl_bn": 'মিথেনোজেন হলো আর্কিওব্যাকটেরিয়া যারা অবাত পরিবেশে এবং রোমন্থক প্রাণীর পরিপাকতন্ত্রে বাস করে এবং গোবর থেকে মিথেন (বায়োগ্যাস) তৈরি করে।',
    },
    {
        "id": 'BIO-015',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification & Fungi',
        "difficulty": 'Medium',
        "en": 'Dikaryophase (n + n stage) is a characteristic feature seen during sexual reproduction in which classes of fungi?',
        "bn": 'যৌন জননের সময় ডাইক্যারিওদশা (n + n অবস্থা) কোন শ্রেণীর ছত্রাকগুলিতে প্রধান বৈশিষ্ট্য হিসেবে দেখা যায়?',
        "opts": {
            "en": ['Ascomycetes and Basidiomycetes', 'Phycomycetes and Ascomycetes', 'Phycomycetes and Zygomycetes', 'Deuteromycetes and Basidiomycetes'],
            "bn": ['অ্যাসকোমাইসিটিস এবং ব্যাসিডিওমাইসিটিস', 'ফাইকোমাইসিটিস এবং অ্যাসকোমাইসিটিস', 'ফাইকোমাইসিটিস এবং জাইগোমাইসিটিস', 'ডিউটেরোমাইসিটিস এবং ব্যাসিডিওমাইসিটিস']
        },
        "correct": 0,
        "expl_en": 'In Ascomycetes and Basidiomycetes, plasmogamy is not immediately followed by karyogamy; an intervening dikaryotic stage (n + n, two nuclei per cell) occurs called dikaryophase.',
        "expl_bn": 'অ্যাসকোমাইসিটিস এবং ব্যাসিডিওমাইসিটিসে প্লাজমোগ্যামির পর অবিলম্বে ক্যারিয়োগ্যামি ঘটে না, ফলে একটি মধ্যবর্তী দ্বিকেন্দ্রিক বা ডাইক্যারিওদশা (n + n) দেখা যায়।',
    },
    {
        "id": 'BIO-016',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Kingdom & Algae',
        "difficulty": 'Easy',
        "en": 'Floridean starch, which has a structural similarity to amylopectin and glycogen, is the stored food in:',
        "bn": 'ফ্লোরিডিয়ান শ্বেতসার, যা অ্যামাইলোপেকটিন এবং গ্লাইকোজেনের সাথে গঠনগত সাদৃশ্যযুক্ত, কোন শ্যাওলায় সঞ্চিত খাদ্য?',
        "opts": {
            "en": ['Rhodophyceae (Red algae)', 'Phaeophyceae (Brown algae)', 'Chlorophyceae (Green algae)', 'Cyanophyceae (Blue-green algae)'],
            "bn": ['রোডোফাইসি (লোহিত শৈবাল)', 'ফিওফাইসি (বাদামী শৈবাল)', 'ক্লোরোফাইসি (সবুজ শৈবাল)', 'সায়ানোফাইসি (নীলাভ-সবুজ শৈবাল)']
        },
        "correct": 0,
        "expl_en": 'In Rhodophyceae (red algae), food is stored as floridean starch, which is structurally very similar to amylopectin and glycogen in its branching pattern.',
        "expl_bn": 'রোডোফাইসিতে (লাল শৈবাল) খাদ্য ফ্লোরিডিয়ান স্টার্চ হিসেবে সঞ্চিত থাকে, যার গঠন অ্যামাইলোপেকটিন ও গ্লাইকোজেনের অনুরূপ শাখান্বিত।',
    },
    {
        "id": 'BIO-017',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Kingdom & Bryophytes',
        "difficulty": 'Easy',
        "en": "Bryophytes are called the 'amphibians of the plant kingdom' because:",
        "bn": "ব্রায়োফাইটকে 'উদ্ভিদ রাজ্যের উভচর' বলা হয় কারণ:",
        "opts": {
            "en": ['They live in soil but depend on water for sexual reproduction', 'They can float on water and live on land alternately', 'They possess gills in their gametophyte stage', 'Their sporophyte is free-living in water'],
            "bn": ['তারা মাটিতে জন্মায় কিন্তু যৌন জননের জন্য জলের উপর নির্ভরশীল', 'তারা জলে ভেসে এবং ডাঙায় পর্যায়ক্রমে বাস করতে পারে', 'তাদের গ্যামেটোফাইটে ফুলকা থাকে', 'তাদের স্পোরোফাইট জলে স্বাধীনজীবী']
        },
        "correct": 0,
        "expl_en": 'Bryophytes are called amphibians of the plant kingdom because these plants live in soil but are dependent on water for sexual reproduction (transfer of antherozoids to archegonium).',
        "expl_bn": 'ব্রায়োফাইটস স্থলজ মাটিতে জন্মায় কিন্তু শুক্রাণু (অ্যান্থেরোজয়েড) স্ত্রীজননাঙ্গে পৌঁছে নিষেক সম্পন্ন করার জন্য জলের অপরিহার্য প্রয়োজন হয়।',
    },
    {
        "id": 'BIO-018',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Kingdom & Gymnosperms',
        "difficulty": 'Medium',
        "en": 'Coralloid roots of Cycas show symbiotic association with which nitrogen-fixing organisms?',
        "bn": 'সাইকাসের কোরালয়েড মূলে কোন নাইট্রোজেন সংবন্ধনকারী জীবের মিথোজীবী সহাবস্থান দেখা যায়?',
        "opts": {
            "en": ['Cyanobacteria (Nostoc and Anabaena)', 'Rhizobium', 'Mycorrhizal fungi', 'Frankia'],
            "bn": ['সায়ানোব্যাকটেরিয়া (নস্টক এবং অ্যানাবেনা)', 'রাইজোবিয়াম', 'মাইকোরাইজাল ছত্রাক', 'ফ্রাঙ্কিয়া']
        },
        "correct": 0,
        "expl_en": 'Cycas has specialized roots called coralloid roots which harbor cyanobacteria (Nostoc, Anabaena) that fix atmospheric nitrogen symbiotically.',
        "expl_bn": 'সাইকাসের বিশেষায়িত কোরালয়েড মূলে নীলাভ-সবুজ শৈবাল বা সায়ানোব্যাকটেরিয়া (নস্টক ও অ্যানাবেনা) বসবাস করে বায়ুমণ্ডলীয় নাইট্রোজেন সংবন্ধন করে।',
    },
    {
        "id": 'BIO-019',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Animal Kingdom & Symmetry & Coelom',
        "difficulty": 'Easy',
        "en": 'Which phylum exhibits bilateral symmetry in larvae but secondary radial (pentamerous) symmetry in adults?',
        "bn": 'কোন পর্বের প্রাণীদের লার্ভা দশায় দ্বিপার্শ্বীয় প্রতিসাম্য কিন্তু পূর্ণাঙ্গ অবস্থায় পঞ্চ-অরীয় প্রতিসাম্য দেখা যায়?',
        "opts": {
            "en": ['Echinodermata', 'Mollusca', 'Arthropoda', 'Annelida'],
            "bn": ['একাইনোডার্মাটা (Echinodermata)', 'মলাস্কা (Mollusca)', 'আর্থ্রোপোডা (Arthropoda)', 'অ্যানেলিডা (Annelida)']
        },
        "correct": 0,
        "expl_en": 'Adult echinoderms (e.g., starfish) are radially symmetrical (pentamerous), but their free-swimming ciliated larvae are bilaterally symmetrical.',
        "expl_bn": 'একাইনোডার্মাটা পর্বের পূর্ণাঙ্গ প্রাণীরা অরীয় প্রতিসম কিন্তু তাদের মুক্ত সন্তরণশীল লার্ভাগুলি দ্বিপার্শ্বীয় প্রতিসম।',
    },
    {
        "id": 'BIO-020',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Animal Kingdom & Arthropoda',
        "difficulty": 'Easy',
        "en": 'Excretion in honeybees and grasshoppers (insects) is primarily carried out by:',
        "bn": 'মৌমাছি এবং ঘাসফড়িং (পতঙ্গ)-এর প্রধান রেচন অঙ্গ কোনটি?',
        "opts": {
            "en": ['Malpighian tubules', 'Nephridia', 'Flame cells (Protonephridia)', 'Antennal glands (Green glands)'],
            "bn": ['ম্যালপিজিয়ান নালিকা', 'নেফ্রিডিয়া', 'শিখা কোষ', 'অ্যান্টেনাল গ্রন্থি (সবুজ গ্রন্থি)']
        },
        "correct": 0,
        "expl_en": 'In insects (phylum Arthropoda), excretion and osmoregulation are performed by thin filamentous Malpighian tubules that empty uric acid into the hindgut.',
        "expl_bn": 'পতঙ্গ শ্রেণির সন্ধিপদীদের প্রধান রেচন অঙ্গ হলো ম্যালপিজিয়ান নালিকা, যা হিমোলিম্ফ থেকে ইউরিক অ্যাসিড নিষ্কাশন করে পৌষ্টিকনালীতে পাঠায়।',
    },
    {
        "id": 'BIO-021',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Morphology of Flowering Plants & Roots',
        "difficulty": 'Easy',
        "en": 'Pneumatophores are specialized respiratory roots found in plants growing in swampy areas, such as:',
        "bn": 'নিউমেটাফোর বা শ্বাসমূল হলো বিশেষ ধরনের মূল যা লবণাক্ত জলাভূমিতে বসবাসকারী কোন উদ্ভিদে দেখা যায়?',
        "opts": {
            "en": ['Rhizophora', 'Banyan tree (Ficus)', 'Maize (Zea mays)', 'Opuntia'],
            "bn": ['রাইজোফোরা (সুন্দরী/গরান)', 'বট গাছ', 'ভুট্টা', 'ফণীমনসা']
        },
        "correct": 0,
        "expl_en": 'In mangrove plants like Rhizophora growing in swampy/marshy saline areas, negative geotropic roots called pneumatophores grow vertically upwards to obtain oxygen for respiration.',
        "expl_bn": 'ম্যানগ্রোভ উদ্ভিদ যেমন রাইজোফোরায় মূলগুলি প্রতিকূল অভিকর্ষবর্তী হয়ে মাটি ভেদ করে উপরে ওঠে এবং শ্বাসছিদ্রের সাহায্যে বাতাস থেকে অক্সিজেন গ্রহণ করে।',
    },
    {
        "id": 'BIO-022',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Morphology of Flowering Plants & Placentation',
        "difficulty": 'Medium',
        "en": 'In unilocular ovary, when ovules are borne on a central column without any dividing septa, the placentation is called:',
        "bn": 'এক-প্রকোষ্ঠযুক্ত ডিম্বাশয়ে যখন ডিম্বকগুলি কোনো পার্টিশন বা সেপ্টাম ছাড়া কেন্দ্রীয় অক্ষে বিন্যস্ত থাকে, তখন তাকে কোন অমরাবিন্যাস বলা হয়?',
        "opts": {
            "en": ['Free-central (e.g., Dianthus, Primrose)', 'Axile (e.g., Tomato, Lemon)', 'Parietal (e.g., Mustard, Argemone)', 'Basal (e.g., Sunflower, Marigold)'],
            "bn": ['মুক্ত-কেন্দ্রীয় (Free-central, যেমন ডায়ান্থাস)', 'অক্ষীয় (Axile, যেমন টমেটো, লেবু)', 'প্রান্তীয় (Parietal, যেমন সর্ষে)', 'ভূমিজ (Basal, যেমন সূর্যমুখী)']
        },
        "correct": 0,
        "expl_en": 'When the ovules are borne on central axis and septa are absent, as in Dianthus and Primula, the placentation is known as free-central placentation.',
        "expl_bn": 'ডায়ান্থাস এবং প্রিমরোজে ডিম্বকগুলি কেন্দ্রীয় অক্ষে বিন্যস্ত থাকে এবং কোনো প্রস্থপ্রাচীর বা সেপ্টা থাকে না; একে মুক্ত-কেন্দ্রীয় অমরাবিন্যাস বলে।',
    },
    {
        "id": 'BIO-023',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Anatomy of Flowering Plants & Tissues',
        "difficulty": 'Easy',
        "en": 'Casparian strips containing suberin deposition are characteristically present in which layer of dicot roots?',
        "bn": 'সুবেরিনযুক্ত ক্যাসপারিয়ান পট্টি (Casparian strips) দ্বিবীজপত্রী উদ্ভিদের মূলের কোন স্তরে স্পষ্টভাবে উপস্থিত থাকে?',
        "opts": {
            "en": ['Endodermis', 'Pericycle', 'Epidermis', 'Cortex'],
            "bn": ['অন্তস্ত্বক্ (Endodermis)', 'পেরিসাইকেল', 'বহিস্ত্বক্ (Epidermis)', 'কর্টেক্স']
        },
        "correct": 0,
        "expl_en": 'The tangential as well as radial walls of the endodermal cells in roots have a deposition of water-impermeable, waxy material suberin in the form of Casparian strips.',
        "expl_bn": 'মূলের অন্তস্ত্বকের (এন্ডোডার্মিস) কোষগুলির স্পর্শকীয় ও অরীয় প্রাচীরে জল-অভেদ্য মোমজাতীয় সুবেরিন জমা হয়ে ক্যাসপারিয়ান পট্টি গঠন করে।',
    },
    {
        "id": 'BIO-024',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Anatomy of Flowering Plants & Secondary Growth',
        "difficulty": 'Medium',
        "en": 'Heartwood (duramen) differs from sapwood (alburnum) because heartwood is:',
        "bn": 'সারকাঠ (Heartwood) রসকাঠ (Sapwood) থেকে পৃথক কারণ সারকাঠ হলো:',
        "opts": {
            "en": ['Non-functional in conduction, dark-colored, and resistant to microbes due to tannins and resins', 'Actively involved in water and mineral transport', 'Composed only of living parenchymatous cells', 'Light colored and located at the outer periphery'],
            "bn": ['জল সংবহনে নিষ্ক্রিয়, গাঢ় রঙের এবং ট্যানিন-রজন জমার কারণে জীবাণু প্রতিরোধী', 'সক্রিয়ভাবে জল ও খনিজ পরিবহনে অংশ নেয়', 'কেবলমাত্র জীবিত প্যারেনকাইমা কোষ দ্বারা গঠিত', 'হালকা রঙের এবং কান্ডের পরিধির দিকে অবস্থিত']
        },
        "correct": 0,
        "expl_en": 'Heartwood is the non-functional, inner dark-colored secondary xylem plugged with tyloses, tannins, and resins. It provides mechanical support but does not conduct water, whereas sapwood conducts water.',
        "expl_bn": 'সারকাঠ হলো কান্ডের কেন্দ্রীয় অংশের পুরানো জাইলেম যা ট্যানিন, রেজিন ও টাইলোসিস দ্বারা রুদ্ধ হয়ে জল সংবহন বন্ধ করে কিন্তু চরম যান্ত্রিক দৃঢ়তা প্রদান করে।',
    },
    {
        "id": 'BIO-025',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Cell: The Unit of Life & Organelles',
        "difficulty": 'Easy',
        "en": 'Which of the following semi-autonomous cell organelles contains 70S ribosomes and circular double-stranded DNA?',
        "bn": 'নিচের কোন আধা-স্বয়ংক্রিয় (semi-autonomous) কোষ অঙ্গাণুতে ৭০S রাইবোজোম এবং বৃত্তাকার দ্বি-তন্ত্রী DNA থাকে?',
        "opts": {
            "en": ['Mitochondria and Chloroplasts', 'Golgi apparatus and Lysosomes', 'Endoplasmic reticulum and Peroxisomes', 'Nucleolus and Ribosomes'],
            "bn": ['মাইটোকন্ড্রিয়া এবং ক্লোরোপ্লাস্ট', 'গলগি বস্তু এবং লাইসোজোম', 'এন্ডোপ্লাজমিক রেটিকুলাম ও পারঅক্সিজোম', 'নিউক্লিওলাস এবং রাইবোজোম']
        },
        "correct": 0,
        "expl_en": 'Both mitochondria and chloroplasts possess their own circular double-stranded DNA molecules, RNA, and 70S prokaryotic-type ribosomes, making them semi-autonomous organelles.',
        "expl_bn": 'মাইটোকন্ড্রিয়া এবং ক্লোরোপ্লাস্ট উভয়েরই নিজস্ব বৃত্তাকার dsDNA এবং 70S রাইবোজোম থাকে, যার ফলে এরা আধা-স্বয়ংক্রিয় অঙ্গাণু হিসেবে পরিচিত।',
    },
    {
        "id": 'BIO-026',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Cell: The Unit of Life & Endomembrane System',
        "difficulty": 'Easy',
        "en": 'The endomembrane system of eukaryotic cells includes all of the following EXCEPT:',
        "bn": 'ইউক্যারিওটিক কোষের অন্তঃপর্দা ব্যবস্থার (endomembrane system) মধ্যে নিচের কোনটি অন্তর্ভুক্ত নয়?',
        "opts": {
            "en": ['Peroxisomes and Mitochondria', 'Endoplasmic Reticulum', 'Golgi apparatus', 'Lysosomes and Vacuoles'],
            "bn": ['পারঅক্সিজোম এবং মাইটোকন্ড্রিয়া', 'এন্ডোপ্লাজমিক রেটিকুলাম', 'গলগি বডি', 'লাইসোজোম এবং ভ্যাকুওল']
        },
        "correct": 0,
        "expl_en": 'According to NCERT, the endomembrane system consists of ER, Golgi complex, lysosomes, and vacuoles whose functions are coordinated. Mitochondria, chloroplasts, and peroxisomes are not part of it.',
        "expl_bn": 'NCERT অনুসারে এন্ডোপ্লাজমিক রেটিকুলাম, গলগি বডি, লাইসোজোম এবং ভ্যাকুওল মিলিতভাবে এন্ডোমেমব্রেন তন্ত্র গঠন করে। মাইটোকন্ড্রিয়া, ক্লোরোপ্লাস্ট ও পারঅক্সিজোম এর অন্তর্ভুক্ত নয়।',
    },
    {
        "id": 'BIO-027',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Cell Cycle and Cell Division & Meiosis',
        "difficulty": 'Medium',
        "en": 'Crossing over between non-sister chromatids of homologous chromosomes is catalyzed by the enzyme recombinase during which stage of Prophase I?',
        "bn": 'প্রথম প্রফেজের কোন উপদশায় রিকম্বিনেজ এনজাইমের সাহায্যে হোমোলোগাস ক্রোমোজোমের নন-সিস্টার ক্রোমাটিডের মধ্যে ক্রসিং ওভার ঘটে?',
        "opts": {
            "en": ['Pachytene', 'Zygotene', 'Diplotene', 'Leptotene'],
            "bn": ['প্যাকাইটিন (Pachytene)', 'জাইগোটিন (Zygotene)', 'ডিপ্লোটিন (Diplotene)', 'লেপ্টোটিন (Leptotene)']
        },
        "correct": 0,
        "expl_en": 'Crossing over occurs during pachytene of prophase I. It is an enzyme-mediated process involving recombinase, leading to genetic recombination between non-sister chromatids.',
        "expl_bn": 'মিয়োসিসের প্রফেজ-১ এর প্যাকাইটিন উপদশায় রিকম্বিনেজ উৎসেচকের সহায়তায় নন-সিস্টার ক্রোমাটিডদ্বয়ের খণ্ডবিনিময় বা ক্রসিং ওভার সম্পন্ন হয়।',
    },
    {
        "id": 'BIO-028',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Cell Cycle and Cell Division & Mitosis',
        "difficulty": 'Easy',
        "en": 'During which phase of the cell cycle does DNA replication and duplication of centrioles occur?',
        "bn": 'কোষ চক্রের কোন দশায় নিউক্লিয়াসে DNA প্রতিলিপিকরণ এবং সাইটোপ্লাজমে সেন্ট্রিওলের অনুলিপন ঘটে?',
        "opts": {
            "en": ['S phase (Synthesis phase)', 'G₁ phase', 'G₂ phase', 'M phase'],
            "bn": ['S দশা (সংশ্লেষ দশা)', 'G₁ দশা', 'G₂ দশা', 'M দশা']
        },
        "correct": 0,
        "expl_en": 'During S phase (Synthesis phase) of interphase, DNA replication takes place in the nucleus (amount doubles from 2C to 4C) and centriole duplicates in the cytoplasm of animal cells.',
        "expl_bn": 'ইন্টারফেজের S দশায় DNA রেপ্লিকেশন ঘটে যার ফলে DNA-এর পরিমাণ দ্বিগুণ (2C থেকে 4C) হয় এবং প্রাণী কোষে সেন্ট্রিওল দ্বিগুণ হয়।',
    },
    {
        "id": 'BIO-029',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biomolecules & Enzyme Kinetics',
        "difficulty": 'Medium',
        "en": 'In competitive inhibition of an enzyme, how do the Michaelis constant (Km) and maximum velocity (Vmax) change?',
        "bn": 'উৎসেচকের প্রতিযোগিতামূলক প্রতিরোধে (competitive inhibition) মাইকেলিস ধ্রুবক (Km) এবং সর্বোচ্চ বেগ (Vmax) কীভাবে পরিবর্তিত হয়?',
        "opts": {
            "en": ['Km increases, while Vmax remains unchanged', 'Km decreases, while Vmax decreases', 'Km remains unchanged, while Vmax decreases', 'Both Km and Vmax increase'],
            "bn": ['Km বৃদ্ধি পায়, কিন্তু Vmax অপরিবর্তিত থাকে', 'Km হ্রাস পায় এবং Vmax হ্রাস পায়', 'Km অপরিবর্তিত থাকে কিন্তু Vmax হ্রাস পায়', 'Km এবং Vmax উভয়ই বৃদ্ধি পায়']
        },
        "correct": 0,
        "expl_en": 'A competitive inhibitor competes with substrate for the active site. Increasing substrate concentration overcomes the inhibitor, so Vmax is unchanged, but apparent affinity decreases (Km increases).',
        "expl_bn": 'প্রতিযোগিতামূলক ইনহিবিটরের ক্ষেত্রে পর্যাপ্ত সাবস্ট্রেট যোগ করলে প্রভাব দূর করা যায়, ফলে Vmax একই থাকে কিন্তু এনজাইমের সাবস্ট্রেট আকর্ষণ কমে যাওয়ায় Km বৃদ্ধি পায়।',
    },
    {
        "id": 'BIO-030',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Physiology & Water Potential',
        "difficulty": 'Medium',
        "en": 'Water potential (Ψw) of pure water at atmospheric pressure and room temperature is defined as:',
        "bn": 'প্রমাণ বায়ুমণ্ডলীয় চাপে এবং সাধারণ তাপমাত্রায় বিশুদ্ধ জলের জল বিভব (Ψw) কত ধরা হয়?',
        "opts": {
            "en": ['Zero', '100 bars', 'Negative 10', 'Positive 1'],
            "bn": ['শূন্য (Zero)', '১০০ বার', 'ঋণাত্মক ১০', 'ধনাত্মক ১']
        },
        "correct": 0,
        "expl_en": 'By convention, pure water has the maximum water potential, which is taken to be zero at standard temperature and atmospheric pressure. Adding solutes makes Ψw negative.',
        "expl_bn": 'প্রচলিত রীতি অনুযায়ী সাধারণ চাপ ও তাপমাত্রায় বিশুদ্ধ জলের মুক্ত শক্তি বা জল বিভব (Water potential) সর্বাধিক এবং এর মান শূন্য ধার্য করা হয়।',
    },
    {
        "id": 'BIO-031',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Physiology & Mineral Nutrition',
        "difficulty": 'Easy',
        "en": 'Which essential micronutrient is required for the photolysis of water during the light reaction of photosynthesis?',
        "bn": 'সালোকসংশ্লেষের আলোক দশায় জলের আলোক-বিশ্লেষণ বা ফটোলাইসিসের জন্য কোন অপরিহার্য অনুখাদ্যটি (মাইক্রোনিউট্রিয়েন্ট) প্রয়োজন?',
        "opts": {
            "en": ['Manganese (Mn) and Chlorine (Cl)', 'Iron (Fe) and Magnesium (Mg)', 'Zinc (Zn) and Copper (Cu)', 'Molybdenum (Mo) and Boron (B)'],
            "bn": ['ম্যাঙ্গানিজ (Mn) এবং ক্লোরিন (Cl)', 'আয়রন (Fe) এবং ম্যাগনেসিয়াম (Mg)', 'জিংক (Zn) এবং তামা (Cu)', 'মলিবডেনাম (Mo) এবং বোরন (B)']
        },
        "correct": 0,
        "expl_en": 'Manganese (Mn²⁺) and Chlorine (Cl⁻) are essential cofactors of the oxygen-evolving complex (OEC) associated with Photosystem II for the photolytic splitting of water (2H₂O → 4H⁺ + 4e⁻ + O₂).',
        "expl_bn": 'ফটোসিস্টেম-২ এর সাথে যুক্ত অক্সিজেন নির্গমনকারী কমপ্লেক্সে ম্যাঙ্গানিজ ও ক্লোরাইড আয়ন জলের ফটোলাইসিস ও O₂ মুক্তিকরণে অপরিহার্য।',
    },
    {
        "id": 'BIO-032',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Physiology & Photosynthesis',
        "difficulty": 'Medium',
        "en": 'The primary CO₂ acceptor in C₄ plants is phosphoenolpyruvate (PEP), and the reaction is catalyzed by PEP carboxylase located in the:',
        "bn": 'C₄ উদ্ভিদে প্রাথমিক CO₂ গ্রাহক হলো ফসফোএনলপাইরুভেট (PEP), এবং এই বিক্রিয়াটি কোন কোষে অবস্থিত PEP কার্বক্সিলেজ দ্বারা অনুঘটিত হয়?',
        "opts": {
            "en": ['Mesophyll cells', 'Bundle sheath cells', 'Epidermal cells', 'Guard cells'],
            "bn": ['মেসোফিল কোষে', 'বান্ডিল সিথ কোষে', 'বহিস্ত্বকের কোষে', 'রক্ষীকোষে']
        },
        "correct": 0,
        "expl_en": 'In C₄ plants, initial CO₂ fixation occurs in mesophyll cells where PEP carboxylase fixes CO₂ into oxaloacetate (4C acid). RuBisCO is confined exclusively to bundle sheath cells.',
        "expl_bn": 'C₄ উদ্ভিদে মেসোফিল কোষে PEP কার্বক্সিলেজ উৎসেচক বায়ুমণ্ডলীয় CO₂ গ্রহণ করে অক্সালোঅ্যাসিটিক অ্যাসিড তৈরি করে। বান্ডিল সিথে কেবল রুবিসকো উপস্থিত থাকে।',
    },
    {
        "id": 'BIO-033',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Physiology & Respiration in Plants',
        "difficulty": 'Easy',
        "en": 'In aerobic cellular respiration, which enzyme complex of the mitochondrial electron transport chain oxidizes succinate to fumarate?',
        "bn": 'মাইটোকন্ড্রিয়ার ইলেকট্রন পরিবহন শৃঙ্খলের (ETC) কোন কমপ্লেক্স সাকসিনেটকে ফিউমারেটে জারিত করে?',
        "opts": {
            "en": ['Complex II (Succinate dehydrogenase)', 'Complex I (NADH dehydrogenase)', 'Complex III (Cytochrome bc₁ complex)', 'Complex IV (Cytochrome c oxidase)'],
            "bn": ['কমপ্লেক্স II (সাকসিনেট ডিহাইড্রোজিনেজ)', 'কমপ্লেক্স I (NADH ডিহাইড্রোজিনেজ)', 'কমপ্লেক্স III (সাইটোক্রোম bc₁)', 'কমপ্লেক্স IV (সাইটোক্রোম c অক্সিডেজ)']
        },
        "correct": 0,
        "expl_en": 'Complex II is Succinate dehydrogenase / Succinate-CoQ reductase. It oxidizes succinate to fumarate in the Krebs cycle, transferring electrons via FADH₂ to ubiquinone.',
        "expl_bn": 'কমপ্লেক্স-II হলো সাকসিনেট ডিহাইড্রোজিনেজ যা ক্রেবস চক্রে সাকসিনেটকে ফিউমারেটে জারিত করে FADH₂ এর মাধ্যমে ইলেকট্রন ইউবিকুইননে স্থানান্তর করে।',
    },
    {
        "id": 'BIO-034',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Physiology & Plant Growth Regulators',
        "difficulty": 'Easy',
        "en": "Which phytohormone is commonly known as the 'stress hormone' because it stimulates stomatal closure during water deficit?",
        "bn": "জলকষ্টের সময় পত্ররন্ধ্র বন্ধ করে বাষ্পমোচন রোধ করায় কোন উদ্ভিদ হরমোনটিকে 'স্ট্রেস হরমোন' (Stress hormone) বলা হয়?",
        "opts": {
            "en": ['Abscisic acid (ABA)', 'Indole-3-acetic acid (IAA)', 'Gibberellic acid (GA₃)', 'Zeatin (Cytokinin)'],
            "bn": ['অ্যাবসিসিক অ্যাসিড (ABA)', 'ইনডোল-৩-অ্যাসিটিক অ্যাসিড (অক্সিন)', 'জিব্বেরেলিক অ্যাসিড (GA₃)', 'জায়াটিন (সাইটোকাইনিন)']
        },
        "correct": 0,
        "expl_en": 'Abscisic acid (ABA) stimulates the closure of stomata in the epidermis and increases the tolerance of plants to various kinds of stresses; therefore, it is called the stress hormone.',
        "expl_bn": 'অ্যাবসিসিক অ্যাসিড (ABA) জলের ঘাটতিতে রক্ষীকোষের পটাসিয়াম নির্গমন ঘটিয়ে পত্ররন্ধ্র বন্ধ করে দেয়, তাই একে স্ট্রেস হরমোন বলা হয়।',
    },
    {
        "id": 'BIO-035',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Physiology & Digestion and Absorption',
        "difficulty": 'Easy',
        "en": 'Parietal (oxyntic) cells of the human gastric mucosa secrete which of the following substances essential for vitamin B₁₂ absorption?',
        "bn": 'মানুষের গ্যাস্ট্রিক মিউকোসার প্যারাইটাল (অক্সিন্টিক) কোষ থেকে নিঃসৃত কোন উপাদানটি ভিটামিন B₁₂ শোষণের জন্য অপরিহার্য?',
        "opts": {
            "en": ["Castle's intrinsic factor and HCl", 'Pepsinogen and Gastrin', 'Mucus and Bicarbonate', 'Trypsinogen and Enterokinase'],
            "bn": ['ক্যাসেলের ইন্ট্রিনসিক ফ্যাক্টর এবং HCl', 'পেপসিনোজেন এবং গ্যাস্ট্রিন', 'মিউকাস এবং বাইকার্বোনেট', 'ট্রিপসিনোজেন এবং এন্টেরোকাইনেজ']
        },
        "correct": 0,
        "expl_en": "Parietal (oxyntic) cells secrete hydrochloric acid (HCl) and Castle's intrinsic factor (factor essential for absorption of vitamin B₁₂ in the ileum). Deficiency causes pernicious anaemia.",
        "expl_bn": 'পাকস্থলীর প্যারাইটাল কোষ হাইড্রোক্লোরিক অ্যাসিড (HCl) এবং ক্যাসেলের ইন্ট্রিনসিক ফ্যাক্টর ক্ষরণ করে, যা ইলিয়ামে ভিটামিন B₁₂ শোষণে অপরিহার্য।',
    },
    {
        "id": 'BIO-036',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Physiology & Breathing and Exchange of Gases',
        "difficulty": 'Medium',
        "en": 'What is the primary form in which carbon dioxide is transported by blood from tissues to the lungs?',
        "bn": 'কলাকোষ থেকে ফুসফুসে রক্ত দ্বারা কার্বন ডাই-অক্সাইড প্রধানত কোন রূপে পরিবাহিত হয়?',
        "opts": {
            "en": ['As bicarbonate ions (HCO₃⁻) in plasma (~70%)', 'As carbamino-haemoglobin in RBCs (~85%)', 'Dissolved in physical solution in plasma (~70%)', 'As carbonic acid crystals (~50%)'],
            "bn": ['প্লাজমায় বাইকার্বোনেট আয়ন (HCO₃⁻) রূপে (~৭০%)', 'লোহিত কণিকায় কার্বামিনো-হিমোগ্লোবিন রূপে (~৮৫%)', 'প্লাজমায় ভৌত দ্রবণ রূপে (~৭০%)', 'কার্বনিক অ্যাসিড স্ফটিক রূপে (~৫০%)']
        },
        "correct": 0,
        "expl_en": 'Nearly 70% of CO₂ is transported as bicarbonate ions (HCO₃⁻) formed inside RBCs by carbonic anhydrase and exchanged with Cl⁻ (chloride shift). About 20-25% is carbamino-haemoglobin and 7% dissolved in plasma.',
        "expl_bn": 'প্রায় ৭০% কার্বন ডাই-অক্সাইড লোহিত রক্তকণিকায় কার্বনিক অ্যানহাইড্রেজ উৎসেচকের ক্রিয়ায় প্লাজমায় বাইকার্বোনেট আয়ন (HCO₃⁻) রূপে পরিবাহিত হয়।',
    },
    {
        "id": 'BIO-037',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Physiology & Body Fluids and Circulation',
        "difficulty": 'Easy',
        "en": 'The pace-maker of the human heart that generates action potentials at the highest frequency (~70–75 beats/min) is the:',
        "bn": 'মানব হৃৎপিণ্ডের প্রাকৃতিক পেসমেকার যা সর্বাধিক হারে (~৭০-৭৫ বার/মিনিট) অ্যাকশন পটেনশিয়াল তৈরি করে সেটি হলো:',
        "opts": {
            "en": ['Sino-atrial node (SAN)', 'Atrio-ventricular node (AVN)', 'Bundle of His', 'Purkinje fibres'],
            "bn": ['সাইনো-অ্যাট্রিয়াল নোড (SAN)', 'অ্যাট্রিও-ভেন্ট্রিকুলার নোড (AVN)', 'হিজের বান্ডিল', 'পারকিঞ্জি তন্তু']
        },
        "correct": 0,
        "expl_en": 'The Sino-atrial node (SAN) in the right atrium is the pacemaker of the heart because it generates the highest rate of action potentials (70-75/min) and initiates rhythmic contraction.',
        "expl_bn": 'ডান অলিন্দের প্রাচীরে অবস্থিত সাইনো-অ্যাট্রিয়াল নোড (SAN) সর্বাধিক হারে স্বয়ংক্রিয় স্পন্দন তৈরি করায় একে হৃৎপিণ্ডের পেসমেকার বলা হয়।',
    },
    {
        "id": 'BIO-038',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Physiology & Excretory Products',
        "difficulty": 'Medium',
        "en": "The Henle's loop and vasa recta operate via a counter-current mechanism to maintain an osmolarity gradient in the medullary interstitium from:",
        "bn": 'হেনলির লুপ এবং ভাসা রেক্টা কাউন্টার-কারেন্ট পদ্ধতির মাধ্যমে বৃক্কীয় মেডুলায় কত থেকে কত অভিস্রাবণীয় নতিমাত্রা (osmolarity gradient) বজায় রাখে?',
        "opts": {
            "en": ['300 mOsmol/L in cortex to 1200 mOsmol/L in inner medulla', '1200 mOsmol/L in cortex to 300 mOsmol/L in medulla', '100 mOsmol/L in cortex to 600 mOsmol/L in medulla', 'Osmolarity remains constant at 300 mOsmol/L throughout'],
            "bn": ['কর্টেক্সে ৩০০ mOsmol/L থেকে অভ্যন্তরীণ মেডুলায় ১২০০ mOsmol/L', 'কর্টেক্সে ১২০০ mOsmol/L থেকে মেডুলায় ৩০০ mOsmol/L', 'কর্টেক্সে ১০০ mOsmol/L থেকে মেডুলায় ৬০০ mOsmol/L', 'সমগ্র বৃক্কে অভিস্রাব্যতা ৩০০ mOsmol/L ধ্রুব থাকে']
        },
        "correct": 0,
        "expl_en": "The counter-current mechanism between the descending/ascending limbs of Henle's loop and vasa recta creates an increasing osmolar gradient from 300 mOsmol/L in the renal cortex to 1200 mOsmol/L in the deep renal medulla.",
        "expl_bn": 'কাউন্টার-কারেন্ট মেকানিজমের সাহায্যে হেনলির লুপ এবং ভাসা রেক্টা বৃক্কীয় কর্টেক্সে ৩০০ mOsmol/L থেকে মেডুলার গভীরে ১২০০ mOsmol/L অভিস্রাব্যতা বৃদ্ধি বজায় রাখে।',
    },
    {
        "id": 'BIO-039',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Physiology & Locomotion and Movement',
        "difficulty": 'Easy',
        "en": 'During skeletal muscle contraction according to the sliding filament theory, which zone/band shortens and disappears?',
        "bn": 'স্লাইডিং ফিলামেন্ট তত্ত্ব অনুসারে কঙ্কাল পেশির সংকোচনের সময় কোন অঞ্চল বা ব্যান্ডটি সংকুচিত হয়ে অদৃশ্য হয়ে যায়?',
        "opts": {
            "en": ['H zone and I band', 'A band only', 'M line and A band', 'Z disc only'],
            "bn": ['H অঞ্চল এবং I ব্যান্ড', 'শুধুমাত্র A ব্যান্ড', 'M লাইন এবং A ব্যান্ড', 'শুধুমাত্র Z ডিস্ক']
        },
        "correct": 0,
        "expl_en": 'During muscle contraction, thin actin filaments slide over thick myosin filaments towards the centre. The I band gets reduced, and the H zone (central myosin region free of actin) shortens and disappears, while the A band retains its length.',
        "expl_bn": 'পেশি সংকোচনের সময় অ্যাকটিন তন্তুগুলি মায়োসিনের উপর দিয়ে কেন্দ্রের দিকে সরে আসে; ফলে I ব্যান্ড ছোট হয় এবং H অঞ্চলটি বিলুপ্ত হয়, কিন্তু A ব্যান্ডের দৈর্ঘ্য স্থির থাকে।',
    },
    {
        "id": 'BIO-040',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Physiology & Neural Control and Coordination',
        "difficulty": 'Medium',
        "en": 'The resting membrane potential (-70 mV) of an axon is primarily maintained by the active transport of:',
        "bn": 'একটি অ্যাক্সনের বিশ্রামকালীন পর্দা বিভব (-৭০ mV) প্রধানত কোনটির সক্রিয় পরিবহনের মাধ্যমে বজায় থাকে?',
        "opts": {
            "en": ['3 Na⁺ pumped out for every 2 K⁺ pumped in by the Na⁺/K⁺ ATPase pump', '3 K⁺ pumped out for every 2 Na⁺ pumped in', '2 Na⁺ pumped out for every 3 Ca²⁺ pumped in', 'Direct passive diffusion of Cl⁻ ions into the axoplasm'],
            "bn": ['Na⁺/K⁺ পাম্প দ্বারা প্রতি ৩টি Na⁺ বাইরে এবং ২টি K⁺ ভিতরে প্রেরণের মাধ্যমে', 'প্রতি ৩টি K⁺ বাইরে এবং ২টি Na⁺ ভিতরে প্রেরণের মাধ্যমে', 'প্রতি ২টি Na⁺ বাইরে এবং ৩টি Ca²⁺ ভিতরে প্রেরণের মাধ্যমে', 'অ্যাক্সোপ্লাজমে Cl⁻ আয়নের নিষ্ক্রিয় ব্যাপন দ্বারা']
        },
        "correct": 0,
        "expl_en": 'The resting potential (-70 mV) is maintained by the electrogenic Na⁺/K⁺ pump that actively transports 3 Na⁺ outwards for every 2 K⁺ into the cell per ATP hydrolyzed.',
        "expl_bn": 'সোডিয়াম-পটাসিয়াম এটিপেজ পাম্প ৩টি Na⁺ আয়ন কোষের বাইরে বের করে এবং ২টি K⁺ আয়ন কোষের ভেতরে আনে, যা ভেতরের ঋণাত্মক বিশ্রাম বিভব বজায় রাখে।',
    },
    {
        "id": 'BIO-041',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Physiology & Chemical Coordination and Integration',
        "difficulty": 'Easy',
        "en": 'Thyrocalcitonin (TCT) secreted by the parafollicular cells of the thyroid gland acts to:',
        "bn": 'থাইরয়েড গ্রন্থির প্যারাফলিকুলার কোষ থেকে নিঃসৃত থাইরোক্যালসিটোনিন (TCT) হরমোনের প্রধান কাজ কী?',
        "opts": {
            "en": ['Lower blood calcium levels (hypocalcemic)', 'Increase blood calcium levels (hypercalcemic)', 'Stimulate bone resorption by osteoclasts', 'Inhibit calcification of teeth'],
            "bn": ['রক্তে ক্যালসিয়ামের মাত্রা হ্রাস করা (hypocalcemic)', 'রক্তে ক্যালসিয়ামের মাত্রা বৃদ্ধি করা (hypercalcemic)', 'অস্থি ক্ষয় ত্বরান্বিত করা', 'দাঁতের খনিজায়ন বাধাগ্রস্ত করা']
        },
        "correct": 0,
        "expl_en": 'Thyrocalcitonin (TCT) is a hypocalcemic hormone that decreases blood Ca²⁺ levels by promoting calcium deposition in bones, acting antagonistically to parathyroid hormone (PTH).',
        "expl_bn": 'থাইরোক্যালসিটোনিন (TCT) অস্থিতে ক্যালসিয়াম সঞ্চয় বাড়িয়ে রক্তে ক্যালসিয়ামের মাত্রা কমায়, অর্থাৎ এটি প্যারাথরমোনের (PTH) বিপরীতধর্মী।',
    },
    {
        "id": 'BIO-042',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Physiology & Endocrine System',
        "difficulty": 'Easy',
        "en": "Which of the following endocrine glands is called the 'emergency gland' because it secretes adrenaline (epinephrine) and noradrenaline?",
        "bn": "নিচের কোন অন্তঃক্ষরা গ্রন্থিকে 'জরুরীকালীন গ্রন্থি' বলা হয় কারণ এটি অ্যাড্রেনালিন এবং নর-অ্যাড্রেনালিন ক্ষরণ করে?",
        "opts": {
            "en": ['Adrenal medulla', 'Adrenal cortex', 'Pineal gland', 'Thymus gland'],
            "bn": ['অ্যাড্রেনাল মেডুলা', 'অ্যাড্রেনাল কর্টেক্স', 'পিনিয়াল গ্রন্থি', 'থাইমাস গ্রন্থি']
        },
        "correct": 0,
        "expl_en": "The adrenal medulla secretes catecholamines (adrenaline/epinephrine and noradrenaline) in response to stress or emergency situations, mediating the 'fight or flight' response.",
        "expl_bn": 'অ্যাড্রেনাল মেডুলা জরুরী অবস্থায় বা বিপদে ক্যাটেকোলামাইন (অ্যাড্রেনালিন ও নর-অ্যাড্রেনালিন) ক্ষরণ করে আপৎকালীন মোকাবিলায় শরীরকে প্রস্তুত করে।',
    },
    {
        "id": 'BIO-043',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Structural Organisation in Animals & Epithelial Tissue',
        "difficulty": 'Easy',
        "en": 'Ciliated columnar epithelium is typically found lining the luminal surface of:',
        "bn": 'সিলিয়াযুক্ত স্তম্ভাকার আবরণী কলা (Ciliated columnar epithelium) সাধারণত কোন অঙ্গের অভ্যন্তরীণ স্তরে পাওয়া যায়?',
        "opts": {
            "en": ['Fallopian tubes (oviducts) and bronchioles', 'Stomach and small intestine', 'PCT of nephron', 'Blood capillaries and alveoli'],
            "bn": ['ফ্যালোপিয়ান নালী (ডিম্বনালী) এবং ব্রঙ্কিওল', 'পাকস্থলী এবং ক্ষুদ্রান্ত্র', 'নেফ্রনের প্রক্সিমাল প্যাঁচানো নালিকা', 'রক্তজালক এবং ফুসফুসের অ্যালভিওলাই']
        },
        "correct": 0,
        "expl_en": 'Ciliated epithelium functions to move particles or mucus in a specific direction over the surface. It is found on the inner surfaces of hollow organs like fallopian tubes and bronchioles.',
        "expl_bn": 'সিলিয়াযুক্ত আবরণী কলা কণা বা মিউকাসকে নির্দিষ্ট দিকে চালনা করে এবং এটি ফ্যালোপিয়ান নালী ও ব্রঙ্কিওলে উপস্থিত থাকে।',
    },
    {
        "id": 'BIO-044',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Structural Organisation in Animals & Cockroach Morphology',
        "difficulty": 'Medium',
        "en": 'In male cockroaches, a pair of short, thread-like anal styles (which are absent in females) arise from which abdominal segment?',
        "bn": 'পুরুষ আরশোলায় একজোড়া ছোট সুতোর মতো অ্যানাল স্টাইল (যা স্ত্রী আরশোলায় থাকে না) কততম উদর খণ্ডক থেকে সৃষ্টি হয়?',
        "opts": {
            "en": ['9th sternum', '10th tergum', '8th sternum', '7th sternum'],
            "bn": ['৯ম স্টার্নাম', '১০ম টারগাম', '৮ম স্টার্নাম', '৭ম স্টার্নাম']
        },
        "correct": 0,
        "expl_en": 'In males, the 9th abdominal sternum bears a pair of short, thread-like unjointed anal styles which are absent in females, distinguishing male cockroaches from females.',
        "expl_bn": 'পুরুষ আরশোলার ৯ম উদরীয় স্টার্নামে একজোড়া অ্যানাল স্টাইল থাকে যা স্ত্রী আরশোলায় সম্পূর্ণ অনুপস্থিত এবং যৌন দ্বিরূপতা নির্দেশ করে।',
    },
    {
        "id": 'BIO-045',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Cell Biology & Nuclear Pore Complex',
        "difficulty": 'Medium',
        "en": 'The outer membrane of the eukaryotic nuclear envelope remains continuous with the membrane of which organelle and also bears ribosomes on it?',
        "bn": 'ইউক্যারিওটিক কোষের নিউক্লীয় পর্দার বহিঃস্তরটি কোন কোষীয় অঙ্গাণুর পর্দার সাথে অবিচ্ছিন্ন থাকে এবং এর গায়ে রাইবোজোম সংলগ্ন থাকে?',
        "opts": {
            "en": ['Rough Endoplasmic Reticulum (RER)', 'Golgi apparatus', 'Mitochondria', 'Lysosome'],
            "bn": ['অমসৃণ এন্ডোপ্লাজমিক রেটিকুলাম (RER)', 'গলগি বস্তু', 'মাইটোকন্ড্রিয়া', 'লাইসোজোম']
        },
        "correct": 0,
        "expl_en": 'The outer nuclear membrane usually remains continuous with the endoplasmic reticulum (specifically rough ER) and also bears ribosomes on its outer surface.',
        "expl_bn": 'নিউক্লিয়াসের বহিস্থ পর্দাটি সাধারণত অমসৃণ এন্ডোপ্লাজমিক রেটিকুলামের পর্দার সাথে যুক্ত থাকে এবং এর গায়ে রাইবোজোম দানা যুক্ত থাকে।',
    },
    {
        "id": 'BIO-046',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": "Biomolecules & Nucleic Acids & Chargaff's Rules",
        "difficulty": 'Medium',
        "en": "A double-stranded DNA molecule contains 30% adenine. According to Chargaff's rule, what is the percentage of cytosine in this DNA molecule?",
        "bn": 'একটি দ্বি-তন্ত্রী DNA অণুতে ৩০% অ্যাডেনিন রয়েছে। চারগাফের নিয়ম অনুসারে, এই DNA অণুতে সাইটোসিনের শতকরা পরিমাণ কত?',
        "opts": {
            "en": ['20%', '30%', '40%', '70%'],
            "bn": ['২০%', '৩০%', '৪০%', '৭০%']
        },
        "correct": 0,
        "expl_en": "According to Chargaff's rule, A = T and G = C. If A = 30%, then T = 30%, totaling 60% (A + T). The remaining 40% consists of G + C. Since G = C, Cytosine = 40% / 2 = 20%.",
        "expl_bn": 'চারগাফের নিয়ম অনুযায়ী A = T এবং G = C। সুতরাং A = ৩০% হলে T = ৩০%, অর্থাৎ (A + T) = ৬০%। বাকি ৪০% হলো (G + C)। অতএব সাইটোসিন (C) = ৪০/২ = ২০%।',
    },
    {
        "id": 'BIO-047',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Sexual Reproduction in Flowering Plants & Pollen',
        "difficulty": 'Easy',
        "en": 'The hard outer layer of pollen grains (exine) is composed of one of the most resistant organic materials known, which is:',
        "bn": 'পরাগরেণুর শক্ত বহিস্থ প্রাচীর (এক্সাইন) অত্যন্ত প্রতিরোধী কোন জৈব উপাদান দ্বারা গঠিত যা উচ্চ তাপমাত্রা এবং শক্তিশালী অ্যাসিড-ক্ষার প্রতিরোধ করতে পারে?',
        "opts": {
            "en": ['Sporopollenin', 'Cellulose and Pectin', 'Callose', 'Lignin'],
            "bn": ['স্পোরোপোলেনিন (Sporopollenin)', 'সেলুলোজ এবং পেকটিন', 'ক্যাল্লোজ', 'লিগনিন']
        },
        "correct": 0,
        "expl_en": 'The hard exine layer of pollen grains is made of sporopollenin, one of the most resistant organic materials known. It can withstand high temperatures and strong acids and alkali; no enzyme that degrades sporopollenin is known.',
        "expl_bn": 'পরাগরেণুর বহিস্থ প্রাচীর স্পোরোপোলেনিন দ্বারা নির্মিত যা চরম তাপ, শক্তিশালী অ্যাসিড এবং কোনো উৎসেচক দ্বারা ক্ষয়প্রাপ্ত হয় না।',
    },
    {
        "id": 'BIO-048',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Sexual Reproduction in Flowering Plants & Female Gametophyte',
        "difficulty": 'Easy',
        "en": 'A typical mature angiosperm embryo sac (female gametophyte) at the time of fertilization is:',
        "bn": 'নিষেককালে একটি আদর্শ সপুষ্পক উদ্ভিদের পরিণত ভ্রূণস্থলী (স্ত্রী-লিঙ্গধর) কত কোষযুক্ত ও কত নিউক্লিয়াসযুক্ত হয়?',
        "opts": {
            "en": ['7-celled and 8-nucleate', '8-celled and 8-nucleate', '7-celled and 7-nucleate', '8-celled and 7-nucleate'],
            "bn": ['৭-কোষীয় এবং ৮-নিউক্লিয়াসযুক্ত', '৮-কোষীয় এবং ৮-নিউক্লিয়াসযুক্ত', '৭-কোষীয় এবং ৭-নিউক্লিয়াসযুক্ত', '৮-কোষীয় এবং ৭-নিউক্লিয়াসযুক্ত']
        },
        "correct": 0,
        "expl_en": 'A typical angiosperm embryo sac at maturity consists of 7 cells: 3 antipodal cells at chalazal end, 1 large central cell with 2 polar nuclei, and 1 egg apparatus (1 egg cell + 2 synergids) at micropylar end, totaling 8 nuclei.',
        "expl_bn": 'একটি আদর্শ পরিণত ভ্রূণস্থলীতে ৩টি প্রতিপাদ কোষ, ২টি সহকারী কোষ, ১টি ডিম্বাণু এবং ২টি পোলার নিউক্লিয়াসযুক্ত ১টি কেন্দ্রীয় কোষ থাকে—অর্থাৎ ৭টি কোষ ও ৮টি নিউক্লিয়াস।',
    },
    {
        "id": 'BIO-049',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Sexual Reproduction in Flowering Plants & Double Fertilization',
        "difficulty": 'Medium',
        "en": 'In angiosperms, double fertilization involves which of the following two fusion events?',
        "bn": 'গুপ্তবীজী উদ্ভিদের দ্বিনিষেক (double fertilization) প্রক্রিয়ায় কোন দুটি সংযুক্তি ঘটে?',
        "opts": {
            "en": ['Syngamy (egg + sperm) and Triple Fusion (central cell + sperm)', 'Syngamy and Parthenogenesis', 'Two sperms fusing with the egg cell simultaneously', 'Triple fusion only'],
            "bn": ['সিনগ্যামি (ডিম্বাণু + পুংজননকোষ) এবং ত্রিসংযোজন (কেন্দ্রীয় কোষ + পুংজননকোষ)', 'সিনগ্যামি এবং পার্থেনোজেনেসিস', 'দুটি পুংজননকোষ একই সাথে ডিম্বাণুর সাথে যুক্ত হয়', 'শুধুমাত্র ত্রিসংযোজন']
        },
        "correct": 0,
        "expl_en": 'Double fertilization involves: 1) Syngamy (one male gamete + egg cell → diploid zygote, 2n); 2) Triple fusion (second male gamete + 2 polar nuclei of central cell → triploid primary endosperm nucleus, PEN, 3n).',
        "expl_bn": 'দ্বিনিষেকে একটি পুংজননকোষ ডিম্বাণুকে নিষিক্ত করে ডিপ্লয়েড জাইগোট (2n) গঠন করে (সিনগ্যামি), এবং অপর পুংজননকোষটি নির্ণীত নিউক্লিয়াসের সাথে যুক্ত হয়ে ট্রিপ্লয়েড শস্য (3n) তৈরি করে (ত্রিসংযোজন)।',
    },
    {
        "id": 'BIO-050',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Reproduction & Spermatogenesis',
        "difficulty": 'Easy',
        "en": 'Leydig cells (interstitial cells) located in the connective tissue spaces between seminiferous tubules synthesize and secrete:',
        "bn": 'শুক্রাশয়ের সেমিনিফেরাস নালিকার অন্তর্বর্তী স্থানে অবস্থিত লেডিগের আন্তরকোষীয় কোষগুলি কী সংশ্লেষ ও ক্ষরণ করে?',
        "opts": {
            "en": ['Androgens (principally Testosterone)', 'Estrogen and Progesterone', 'Inhibin and ABP', 'Luteinizing Hormone (LH)'],
            "bn": ['অ্যান্ড্রোজেন (প্রধানত টেস্টোস্টেরন)', 'ইস্ট্রোজেন এবং প্রোজেস্টেরন', 'ইনহিবিন এবং ABP', 'লিউটিনাইজিং হরমোন (LH)']
        },
        "correct": 0,
        "expl_en": 'Leydig cells (interstitial cells) present in the interstitial spaces between seminiferous tubules produce testicular hormones called androgens, primarily testosterone, under the stimulation of LH.',
        "expl_bn": 'লেডিগের আন্তরকোষ পিটুইটারির LH হরমোনের প্রভাবে পুরুষ জনন হরমোন অ্যান্ড্রোজেন (প্রধানত টেস্টোস্টেরন) সংশ্লেষ ও ক্ষরণ করে।',
    },
    {
        "id": 'BIO-051',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Reproduction & Oogenesis',
        "difficulty": 'Medium',
        "en": 'In human females, primary oocytes remain arrested at which stage of cell division from fetal life until puberty?',
        "bn": 'মানব স্ত্রীদেহে প্রাইমারি ওওসাইট ভ্রূণাবস্থা থেকে বয়ঃসন্ধিকাল পর্যন্ত কোষ বিভাজনের কোন দশায় স্থগিত (arrested) থাকে?',
        "opts": {
            "en": ['Diplotene stage of Prophase I', 'Metaphase II', 'Anaphase I', 'Telophase II'],
            "bn": ['প্রথম প্রফেজের ডিপ্লোটিন উপদশা', 'মেটাফেজ II', 'অ্যানাফেজ I', 'টেলোফেজ II']
        },
        "correct": 0,
        "expl_en": 'Primary oocytes begin meiotic division before birth but remain arrested at the diplotene stage of prophase I of meiosis I until puberty, when follicular development resumes under gonadotropic stimulation.',
        "expl_bn": 'ভ্রূণাবস্থায় গঠিত প্রাইমারি ওওসাইটগুলি মিয়োসিস-১ এর প্রফেজ-১ এর ডিপ্লোটিন উপদশায় স্থগিত অবস্থায় থাকে এবং বয়ঃসন্ধির পর পুনরায় বিভাজন শুরু করে।',
    },
    {
        "id": 'BIO-052',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Reproduction & Menstrual Cycle',
        "difficulty": 'Easy',
        "en": 'Ovulation (release of the secondary oocyte from the Graafian follicle) is triggered by a sudden surge in which hormone?',
        "bn": 'গ্রাফিয়ান ফলিকল থেকে ওভিউলেশন বা ডিম্বাণু নিঃসরণ কোন হরমোনের আকস্মিক বৃদ্ধির (Surge) কারণে ঘটে?',
        "opts": {
            "en": ['Luteinizing Hormone (LH)', 'Progesterone', 'Oxytocin', 'Prolactin'],
            "bn": ['লিউটিনাইজিং হরমোন (LH)', 'প্রোজেস্টেরন', 'অক্সিটোসিন', 'প্রোল্যাক্টিন']
        },
        "correct": 0,
        "expl_en": 'Rapid secretion of LH leading to its maximum level during the mid-cycle (around 14th day) called LH surge induces rupture of the Graafian follicle and thereby the release of an ovum (ovulation).',
        "expl_bn": 'ঋতুচক্রের মধ্যবর্তী সময়ে (১৪তম দিনে) পিটুইটারি থেকে LH হরমোনের আকস্মিক তীব্র নিঃসরণকে LH সার্জ বলে, যা গ্রাফিয়ান ফলিকল বিদীর্ণ করে ওভিউলেশন ঘটায়।',
    },
    {
        "id": 'BIO-053',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Reproductive Health & Contraception',
        "difficulty": 'Easy',
        "en": 'Copper-releasing intra-uterine devices (e.g., CuT, Cu7, Multiload 375) prevent pregnancy primarily by:',
        "bn": 'কপার নির্গমনকারী আইইউডি (IUDs, যেমন CuT, Multiload 375) প্রধানত কীভাবে গর্ভধারণ প্রতিরোধ করে?',
        "opts": {
            "en": ['Suppressing sperm motility and fertilizing capacity', 'Blocking the entry of sperm into the cervix physically', 'Preventing ovulation and menstruation entirely', 'Inhibiting implantation through progesterone release'],
            "bn": ['শুক্রাণুর চলনক্ষমতা এবং নিষেক ক্ষমতা হ্রাস করে', 'ভৌতভাবে জরায়ুমুখে শুক্রাণু প্রবেশ আটকায়', 'ওভিউলেশন ও ঋতুস্রাব সম্পূর্ণরূপে বন্ধ করে', 'প্রোজেস্টেরন ক্ষরণের মাধ্যমে রোপণ প্রতিহত করে']
        },
        "correct": 0,
        "expl_en": 'Cu ions released by copper-bearing IUDs suppress sperm motility and the fertilizing capacity of sperms, while increasing phagocytosis of sperms within the uterus.',
        "expl_bn": 'CuT থেকে নির্গত কপার আয়ন শুক্রাণুর চলনক্ষমতা এবং ডিম্বাণুকে নিষিক্ত করার ক্ষমতা নষ্ট করে এবং জরায়ুতে শুক্রাণুর ফ্যাগোসাইটোসিস বাড়ায়।',
    },
    {
        "id": 'BIO-054',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Reproductive Health & Assisted Reproductive Technology',
        "difficulty": 'Easy',
        "en": 'In Assisted Reproductive Technologies (ART), the transfer of an embryo with up to 8 blastomeres into the fallopian tube is termed:',
        "bn": 'সহায়ক জনন প্রযুক্তিতে (ART) ৮টি ব্লাস্টোমেয়ার পর্যন্ত ভ্রূণকে সরাসরি ফ্যালোপিয়ান নালীতে স্থানান্তর করার পদ্ধতিকে কী বলা হয়?',
        "opts": {
            "en": ['ZIFT (Zygote Intra-Fallopian Transfer)', 'IUT (Intra-Uterine Transfer)', 'GIFT (Gamete Intra-Fallopian Transfer)', 'ICSI (Intra-Cytoplasmic Sperm Injection)'],
            "bn": ['ZIFT (জাইগোট ইন্ট্রা-ফ্যালোপিয়ান ট্রান্সফার)', 'IUT (ইন্ট্রা-ইউটেরাইন ট্রান্সফার)', 'GIFT (গ্যামেট ইন্ট্রা-ফ্যালোপিয়ান ট্রান্সফার)', 'ICSI (ইন্ট্রা-সাইটোপ্লাজমিক স্পার্ম ইনজেকশন)']
        },
        "correct": 0,
        "expl_en": 'The zygote or early embryo (with up to 8 blastomeres) transferred into the fallopian tube is called ZIFT (Zygote Intra-Fallopian Transfer). Embryos with more than 8 blastomeres are transferred into the uterus (IUT).',
        "expl_bn": 'ইন-ভিট্রো নিষেকের পর জাইগোট বা ৮টি পর্যন্ত ব্লাস্টোমেয়ারযুক্ত প্রাথমিক ভ্রূণকে ফ্যালোপিয়ান নালীতে প্রতিস্থাপন করাকে ZIFT বলা হয়।',
    },
    {
        "id": 'BIO-055',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Principles of Inheritance & Incomplete Dominance',
        "difficulty": 'Easy',
        "en": 'In snapdragon (Antirrhinum majus), crossing a homozygous red-flowered plant (RR) with a homozygous white-flowered plant (rr) produces pink-flowered offspring (Rr) due to:',
        "bn": 'স্ন্যাপড্রাগন (Antirrhinum majus) উদ্ভিদে বিশুদ্ধ লাল ফুল (RR) ও সাদা ফুলের (rr) ক্রসের ফলে F₁ জনুতে গোলাপী ফুল (Rr) ফোটার কারণ কী?',
        "opts": {
            "en": ['Incomplete dominance', 'Co-dominance', 'Epistasis', 'Pleiotropy'],
            "bn": ['অসম্পূর্ণ প্রকটতা (Incomplete dominance)', 'সহ-প্রকটতা (Co-dominance)', 'এপিস্ট্যাসিস', 'প্লিওট্রপি']
        },
        "correct": 0,
        "expl_en": 'In snapdragon, the allele for red color (R) is not completely dominant over the allele for white color (r). The heterozygous condition (Rr) results in an intermediate pink color due to incomplete dominance (1:2:1 phenotypic and genotypic ratio).',
        "expl_bn": 'লাল অ্যালিল (R) সাদা অ্যালিলের (r) উপর সম্পূর্ণ প্রকট না হওয়ায় হেটেরোজাইগাস অবস্থায় অন্তর্বর্তী গোলাপী ফিনোটাইপ প্রকাশ পায়, একে অসম্পূর্ণ প্রকটতা বলে।',
    },
    {
        "id": 'BIO-056',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Principles of Inheritance & Chromosomal Disorders',
        "difficulty": 'Easy',
        "en": "Klinefelter's syndrome in humans is caused by the presence of an additional X chromosome resulting in a karyotype of:",
        "bn": 'মানুষের ক্ষেত্রে ক্লাইনফেল্টার সিন্ড্রোম একটি অতিরিক্ত X ক্রোমোজোমের উপস্থিতির ফলে ঘটে, যার ক্যারিওটাইপ হলো:',
        "opts": {
            "en": ['47, XXY', '45, XO', '47, XYY', '47, XXX'],
            "bn": ['47, XXY', '45, XO', '47, XYY', '47, XXX']
        },
        "correct": 0,
        "expl_en": "Klinefelter's syndrome is caused due to the presence of an additional copy of an X-chromosome resulting in a karyotype of 47, XXY. Such individuals have overall masculine development with feminine features (e.g., gynaecomastia) and are sterile.",
        "expl_bn": 'একটি অতিরিক্ত X ক্রোমোজোমের উপস্থিতিতে ৪৭, XXY ক্যারিওটাইপ গঠিত হয়। ব্যক্তিটি সাধারণত পুরুষ হয় কিন্তু এদের মধ্যে স্ত্রীসুলভ বৈশিষ্ট্য (যেমন গাইনোকোমাস্টিয়া) দেখা যায় এবং এরা বন্ধ্যা হয়।',
    },
    {
        "id": 'BIO-057',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Principles of Inheritance & Sickle-Cell Anaemia',
        "difficulty": 'Medium',
        "en": 'Sickle-cell anaemia is caused by a point mutation in the gene coding for the beta-globin chain, resulting in the substitution of:',
        "bn": 'সিকেল-সেল অ্যানিমিয়া বা কাস্তে-কোষ রক্তাল্পতা জিনগত পয়েন্ট মিউটেশনের ফলে ঘটে, যাতে বিটা-গ্লোবিন শৃঙ্খলের ৬ নম্বর স্থানে কোন অ্যামিনো অ্যাসিডের পরিবর্তন ঘটে?',
        "opts": {
            "en": ['Glutamic acid by Valine at position 6 (GAG to GUG)', 'Valine by Glutamic acid at position 6', 'Glutamic acid by Glycine at position 6', 'Lysine by Valine at position 3'],
            "bn": ['৬ নম্বর স্থানে গ্লুটামিক অ্যাসিডের পরিবর্তে ভ্যালিন (GAG থেকে GUG)', '৬ নম্বর স্থানে ভ্যালিনের পরিবর্তে গ্লুটামিক অ্যাসিড', '৬ নম্বর স্থানে গ্লুটামিক অ্যাসিডের পরিবর্তে গ্লাইসিন', '৩ নম্বর স্থানে লাইসিনের পরিবর্তে ভ্যালিন']
        },
        "correct": 0,
        "expl_en": 'Sickle-cell anemia results from a transversion point mutation where the 6th codon of the β-globin gene changes from GAG to GUG, causing substitution of glutamic acid (polar) with valine (non-polar).',
        "expl_bn": 'β-গ্লোবিন জিনের ৬ষ্ঠ কোডনে একটি বেস পরিবর্তনের কারণে (GAG → GUG) স্বাভাবিক গ্লুটামিক অ্যাসিডের স্থলে হাইড্রোফোবিক ভ্যালিন যুক্ত হয়ে পলিমারাইজেশন ঘটায়।',
    },
    {
        "id": 'BIO-058',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Molecular Basis of Inheritance & Griffith Experiment',
        "difficulty": 'Easy',
        "en": "Frederick Griffith (1928) discovered the 'Transforming Principle' using which organism?",
        "bn": 'ফ্রেডেরিক গ্রিফিথ (১৯২৮) কোন ব্যাকটেরিয়ার ওপর গবেষণা করে রূপান্তর নীতি (Transforming Principle) আবিষ্কার করেছিলেন?',
        "opts": {
            "en": ['Streptococcus pneumoniae', 'Escherichia coli', 'Bacillus thuringiensis', 'Salmonella typhimurium'],
            "bn": ['স্ট্রেপ্টোকক্কাস নিউমোনি (Streptococcus pneumoniae)', 'এসচেরিচিয়া কোলাই (E. coli)', 'ব্যাসিলাস থুরিনজিয়েনসিস', 'সালমোনেলা টাইফিমুরিয়াম']
        },
        "correct": 0,
        "expl_en": 'Griffith worked with Streptococcus pneumoniae (pneumococcus), showing that heat-killed virulent Smooth (S) strain transformed living non-virulent Rough (R) strain into virulent S strain in mice.',
        "expl_bn": 'গ্রিফিথ নিউমোনিয়া সৃষ্টিকারী ব্যাকটেরিয়া স্ট্রেপ্টোকক্কাস নিউমোনির মসৃণ (S) এবং অমসৃণ (R) স্ট্রেন ব্যবহার করে জেনেটিক রূপান্তরণ প্রদর্শন করেন।',
    },
    {
        "id": 'BIO-059',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Molecular Basis of Inheritance & Genetic Code',
        "difficulty": 'Easy',
        "en": 'The codon AUG functions as both the initiation codon for translation and codes for which amino acid?',
        "bn": 'AUG কোডনটি প্রোটিন সংশ্লেষে সূচনা কোডন হিসেবে কাজ করার পাশাপাশি কোন অ্যামিনো অ্যাসিডকে সংকেতায়িত করে?',
        "opts": {
            "en": ['Methionine', 'Tryptophan', 'Phenylalanine', 'Valine'],
            "bn": ['মেথিওনিন (Methionine)', 'ট্রিপটোফ্যান', 'ফিনাইলঅ্যালানিন', 'ভ্যালিন']
        },
        "correct": 0,
        "expl_en": 'AUG has dual functions: it codes for the amino acid Methionine (Met), and it also acts as the initiator codon for polypeptide chain synthesis during translation.',
        "expl_bn": 'AUG কোডনের দ্বৈত কাজ রয়েছে: এটি সূচনা কোডন হিসেবে ট্রান্সলেশন শুরু করে এবং মেথিওনিন অ্যামিনো অ্যাসিডের সংকেত বহন করে।',
    },
    {
        "id": 'BIO-060',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Molecular Basis of Inheritance & Operon Model',
        "difficulty": 'Medium',
        "en": 'In the lac operon of E. coli, what is the specific role of allolactose?',
        "bn": 'ই. কোলাই-এর ল্যাক অপারনে অ্যালোল্যাকটোজ কী হিসেবে কাজ করে?',
        "opts": {
            "en": ['Inducer that binds to the repressor protein and inactivates it', 'Co-repressor that activates the repressor protein', 'Promoter activator that directly stimulates RNA polymerase', 'Enzyme that cleaves glucose into galactose'],
            "bn": ['ইনডিউসার (Inducer) যা রিপ্রেসর প্রোটিনের সাথে যুক্ত হয়ে সেটিকে নিষ্ক্রিয় করে', 'সহ-রিপ্রেসর যা রিপ্রেসরকে সক্রিয় করে', 'প্রোমোটার সক্রিয়ক যা সরাসরি RNA পলিমারেজকে চালায়', 'উৎসেচক যা গ্লুকোজকে গ্যালাক্টোজে ভাঙে']
        },
        "correct": 0,
        "expl_en": 'In the lac operon, allolactose (derived from lactose by β-galactosidase) acts as the inducer. It binds to the lac repressor protein, altering its conformation so it cannot bind to the operator, allowing transcription.',
        "expl_bn": 'অ্যালোল্যাকটোজ ইনডিউসার হিসেবে ল্যাক রিপ্রেসর প্রোটিনের সাথে যুক্ত হয় এবং এর গঠন পরিবর্তন করে একে অপারেটর থেকে বিচ্ছিন্ন করে ট্রান্সক্রিপশন সচল করে।',
    },
    {
        "id": 'BIO-061',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Evolution & Origin of Life',
        "difficulty": 'Easy',
        "en": 'In their classic 1953 experiment simulating primitive Earth conditions, S.L. Miller and H.C. Urey created electric discharges in a gas mixture consisting of:',
        "bn": 'আদিম পৃথিবীর পরিবেশ কৃত্রিমভাবে সৃষ্টি করতে এস.এল. মিলার এবং এইচ.সি. ইউরে (১৯৫৩) কোন কোন গ্যাসের মিশ্রণে তড়িৎক্ষরণ ঘটিয়েছিলেন?',
        "opts": {
            "en": ['CH₄, H₂, NH₃, and water vapour at 800°C', 'CH₄, O₂, NH₃, and CO₂ at 100°C', 'CO₂, N₂, H₂O, and O₂ at 800°C', 'CH₄, NH₃, SO₂, and H₂ at 500°C'],
            "bn": ['৮০০°C তাপমাত্রায় CH₄, H₂, NH₃ এবং জলীয় বাষ্প', '১০০°C তাপমাত্রায় CH₄, O₂, NH₃ এবং CO₂', '৮০০°C তাপমাত্রায় CO₂, N₂, H₂O এবং O₂', '৫০০°C তাপমাত্রায় CH₄, NH₃, SO₂ এবং H₂']
        },
        "correct": 0,
        "expl_en": 'Miller created electric discharge in a closed flask containing CH₄, H₂, NH₃, and water vapour at 800°C to simulate the reducing atmosphere of primitive Earth, observing the synthesis of amino acids.',
        "expl_bn": 'মিলার ও ইউরে আদিম বিজারক বায়ুমণ্ডলের প্রতিরূপ তৈরি করতে মিথেন, হাইড্রোজেন, অ্যামোনিয়া এবং জলীয় বাষ্প নিয়ে ৮০০°C তাপমাত্রায় স্পার্ক ডিসচার্জ ঘটান এবং অ্যামিনো অ্যাসিড তৈরি হতে দেখেন।',
    },
    {
        "id": 'BIO-062',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Evolution & Homology and Analogy',
        "difficulty": 'Easy',
        "en": 'The thorns of Bougainvillea and the tendrils of Passiflora or Cucurbita represent:',
        "bn": 'বোগেনভিলিয়ার কাঁটা এবং ঝুমকালতা বা কুমড়োর আকর্ষ কিসের চমৎকার উদাহরণ?',
        "opts": {
            "en": ['Homologous organs (divergent evolution)', 'Analogous organs (convergent evolution)', 'Vestigial organs', 'Atavistic structures'],
            "bn": ['সমসংস্থ অঙ্গ (অপসারী অভিব্যক্তি)', 'সমবৃত্তীয় অঙ্গ (অভিসারী অভিব্যক্তি)', 'নিষ্ক্রিয় অঙ্গ', 'অ্যাটাভিজম']
        },
        "correct": 0,
        "expl_en": 'Both thorns of Bougainvillea and tendrils of Cucurbita arise from the axillary bud (common embryonic origin and anatomical structure), but perform different functions (defense vs climbing), indicating homology and divergent evolution.',
        "expl_bn": 'বোগেনভিলিয়ার কাঁটা এবং কুমড়োর আকর্ষ উভয়েই কাক্ষিক মুকুলের রূপান্তর (অভিন্ন উৎপত্তি ও গঠন) কিন্তু কাজ আলাদা, তাই এরা সমসংস্থ অঙ্গ (Divergent evolution)।',
    },
    {
        "id": 'BIO-063',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Evolution & Hardy-Weinberg Principle',
        "difficulty": 'Medium',
        "en": 'In a population in Hardy-Weinberg equilibrium, the frequency of a recessive allele (q) is 0.4. What is the expected percentage of heterozygous individuals (2pq)?',
        "bn": 'হার্ডি-ওয়াইনবার্গ সাম্যাবস্থায় থাকা একটি পপুলেশনে প্রচ্ছন্ন অ্যালিলের কম্পাঙ্ক (q) হলো ০.৪। তবে সেখানে হেটেরোজাইগাস জীবের শতকরা অনুপাত (2pq) কত হবে?',
        "opts": {
            "en": ['48%', '16%', '36%', '24%'],
            "bn": ['৪৮%', '১৬%', '৩৬%', '২৪%']
        },
        "correct": 0,
        "expl_en": 'Given q = 0.4. Since p + q = 1, p = 1 - 0.4 = 0.6. The frequency of heterozygotes is 2pq = 2 × 0.6 × 0.4 = 0.48, which corresponds to 48%.',
        "expl_bn": 'দেওয়া আছে q = ০.৪। যেহেতু p + q = ১, তাই p = ১ - ০.৪ = ০.৬। হেটেরোজাইগাসের অনুপাত 2pq = ২ × ০.৬ × ০.৪ = ০.৪৮ বা ৪৮%।',
    },
    {
        "id": 'BIO-064',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Health and Disease & Malaria Parasite',
        "difficulty": 'Easy',
        "en": 'The infective stage of Plasmodium that enters the human body through the bite of an infected female Anopheles mosquito is:',
        "bn": 'স্ত্রী অ্যানোফিলিস মশার কামড়ে ম্যালেরিয়ার সংক্রামক কোন দশাটি মানুষের দেহে প্রবেশ করে?',
        "opts": {
            "en": ['Sporozoite', 'Trophozoite', 'Merozoite', 'Gametocyte'],
            "bn": ['স্পোরোজয়েট (Sporozoite)', 'ট্রফোজয়েট', 'মেরোজয়েট', 'গ্যামেটোসাইট']
        },
        "correct": 0,
        "expl_en": 'Plasmodium enters the human body as infectious sporozoites through the bite of infected female Anopheles mosquitoes. Sporozoites migrate to the liver first to multiply asexually.',
        "expl_bn": 'স্ত্রী অ্যানোফিলিস মশার লালাগ্রন্থি থেকে সংক্রামক স্পোরোজয়েট দশাটি মানুষের রক্তে প্রবেশ করে এবং সরাসরি যকৃতে গিয়ে সংখ্যাবৃদ্ধি করে।',
    },
    {
        "id": 'BIO-065',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Human Health and Disease & Immunity',
        "difficulty": 'Easy',
        "en": 'Colostrum secreted by the mother during initial days of lactation contains abundant amounts of which antibody to protect the newborn?',
        "bn": 'নবজাতককে নিষ্ক্রিয় অনাক্রম্যতা প্রদানের জন্য মায়ের প্রথম ক্ষরিত শালদুধ বা কলোস্ট্রামে কোন অ্যান্টিবডি প্রচুর পরিমাণে থাকে?',
        "opts": {
            "en": ['Secretory IgA', 'IgG', 'IgE', 'IgM'],
            "bn": ['নিঃস্রাবী IgA', 'IgG', 'IgE', 'IgM']
        },
        "correct": 0,
        "expl_en": 'The yellowish fluid colostrum secreted by mother during the initial days of lactation has abundant IgA antibodies that protect the infant from mucosal infections (passive natural immunity).',
        "expl_bn": 'শালদুধ বা কলোস্ট্রামে প্রচুর পরিমাণে ডিমারিক IgA অ্যান্টিবডি থাকে যা নবজাতকের পরিপাক ও শ্বাসতন্ত্রে প্রতিরক্ষা প্রদান করে।',
    },
    {
        "id": 'BIO-066',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Microbes in Human Welfare & Industrial Products',
        "difficulty": 'Easy',
        "en": 'Statins, widely prescribed blood cholesterol lowering agents, are commercially produced by the yeast:',
        "bn": 'রক্তে কোলেস্টেরল হ্রাসকারী ওষুধ স্ট্যাটিন বাণিজ্যিকভাবে কোন ঈস্ট জাতীয় ছত্রাক থেকে নিষ্কাশন করা হয়?',
        "opts": {
            "en": ['Monascus purpureus', 'Saccharomyces cerevisiae', 'Trichoderma polysporum', 'Aspergillus niger'],
            "bn": ['মোনাস্কাস পারপিউরিয়াস (Monascus purpureus)', 'স্যাকারোমাইসিস সেরিভিসি', 'ট্রাইকোডার্মা পলিস্পোরাম', 'অ্যাসপারজিলাস নাইজার']
        },
        "correct": 0,
        "expl_en": 'Statins produced by the yeast Monascus purpureus act by competitively inhibiting HMG-CoA reductase, the rate-limiting enzyme responsible for cholesterol synthesis.',
        "expl_bn": 'মোনাস্কাস পারপিউরিয়াস নামক ঈস্ট থেকে স্ট্যাটিন উৎপাদিত হয়, যা কোলেস্টেরল সংশ্লেষণকারী HMG-CoA রিডাক্টেজ উৎসেচককে প্রতিযোগিতামূলকভাবে প্রতিরোধ করে।',
    },
    {
        "id": 'BIO-067',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Microbes in Human Welfare & Bioactive Molecules',
        "difficulty": 'Easy',
        "en": 'Cyclosporin A, used as an immunosuppressive agent in organ transplant patients, is produced by the fungus:',
        "bn": 'অঙ্গ প্রতিস্থাপনে ব্যবহৃত রোগপ্রতিরোধ-দমনকারী (immunosuppressive) ওষুধ সাইক্লোস্পোরিন-এ কোন ছত্রাক থেকে প্রস্তুত করা হয়?',
        "opts": {
            "en": ['Trichoderma polysporum', 'Penicillium notatum', 'Streptococcus', 'Monascus purpureus'],
            "bn": ['ট্রাইকোডার্মা পলিস্পোরাম (Trichoderma polysporum)', 'পেনিসিলিয়াম নোটেটাম', 'স্ট্রেপ্টোকক্কাস', 'মোনাস্কাস পারপিউরিয়াস']
        },
        "correct": 0,
        "expl_en": 'Cyclosporin A, a bioactive molecule used as an immunosuppressive agent in organ-transplant patients to prevent tissue rejection, is produced by the fungus Trichoderma polysporum.',
        "expl_bn": 'ট্রাইকোডার্মা পলিস্পোরাম নামক ছত্রাক থেকে সাইক্লোস্পোরিন-এ উৎপন্ন হয়, যা অঙ্গ প্রতিস্থাপনের সময় অনাক্রম্যতা দমন করে টিস্যু রিজেকশন প্রতিরোধ করে।',
    },
    {
        "id": 'BIO-068',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biotechnology: Principles and Processes & Restriction Enzymes',
        "difficulty": 'Easy',
        "en": 'The restriction endonuclease EcoRI specifically recognizes which palindromic nucleotide sequence in DNA?',
        "bn": 'EcoRI রেস্ট্রিকশন এন্ডোনিউক্লিয়েজ DNA-র কোন নির্দিষ্ট প্যালিন্ড্রোমিক নিউক্লিওটাইড সজ্জা সনাক্ত করে খণ্ডন করে?',
        "opts": {
            "en": ["5'-GAATTC-3'", "5'-GGATCC-3'", "5'-AAGCTT-3'", "5'-CTGCAG-3'"],
            "bn": ["5'-GAATTC-3'", "5'-GGATCC-3'", "5'-AAGCTT-3'", "5'-CTGCAG-3'"]
        },
        "correct": 0,
        "expl_en": "EcoRI cuts the DNA between bases G and A only when the sequence 5'-GAATTC-3' (and complementary 3'-CTTAAG-5') is present, creating cohesive sticky single-stranded ends.",
        "expl_bn": "EcoRI নির্দিষ্টভাবে 5'-GAATTC-3' সিকোয়েন্সে G ও A বেসের মাঝে ফসফোডাইএস্টার বন্ধন কেটে স্টিকি প্রান্ত (sticky ends) তৈরি করে।",
    },
    {
        "id": 'BIO-069',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biotechnology: Principles and Processes & PCR',
        "difficulty": 'Easy',
        "en": 'Taq polymerase used in Polymerase Chain Reaction (PCR) is isolated from the thermophilic bacterium:',
        "bn": 'পলিমারেজ শৃঙ্খল বিক্রিয়ায় (PCR) ব্যবহৃত তাপসহনশীল Taq পলিমারেজ কোন ব্যাকটেরিয়া থেকে নিষ্কাশন করা হয়?',
        "opts": {
            "en": ['Thermus aquaticus', 'Thermotoga maritima', 'Bacillus thuringiensis', 'Escherichia coli'],
            "bn": ['থার্মাস অ্যাকোয়াটিকাস (Thermus aquaticus)', 'থার্মোটোগা ম্যারিটিমা', 'ব্যাসিলাস থুরিনজিয়েনসিস', 'এসচেরিচিয়া কোলাই']
        },
        "correct": 0,
        "expl_en": 'Taq polymerase is a thermostable DNA polymerase extracted from the thermophilic bacterium Thermus aquaticus. It remains active during the high temperature denaturation step (~94°C) of PCR.',
        "expl_bn": 'থার্মাস অ্যাকোয়াটিকাস নামক তাপপ্রিয় ব্যাকটেরিয়া থেকে Taq পলিমারেজ পাওয়া যায়, যা PCR-এর ৯৪°C ডিন্যাচুরেশন তাপমাত্রাতেও নষ্ট হয় না।',
    },
    {
        "id": 'BIO-070',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biotechnology and Its Applications & Bt Cotton',
        "difficulty": 'Easy',
        "en": 'Bt toxin protein produced by Bacillus thuringiensis does not kill the bacterium itself because:',
        "bn": 'ব্যাসিলাস থুরিনজিয়েনসিস ব্যাকটেরিয়া কর্তৃক উৎপন্ন Bt টক্সিন প্রোটিন ব্যাকটেরিয়াটিকে নিজে ধ্বংস করে না কারণ:',
        "opts": {
            "en": ['It exists as an inactive protoxin within the bacterium', 'The bacterium is completely impermeable to the protein', 'The toxin is immediately degraded by bacterial proteases', 'The bacterium encapsulates the toxin in thick chitin'],
            "bn": ['এটি ব্যাকটেরিয়ার অভ্যন্তরে নিষ্ক্রিয় প্রোটক্সিন (Protoxin) রূপে থাকে', 'ব্যাকটেরিয়া পর্দা প্রোটিনটির জন্য সম্পূর্ণ অভেদ্য', 'ব্যাকটেরিয়ার প্রোটিয়েজ উৎসেচক টক্সিনটিকে সাথে সাথে নষ্ট করে', 'টক্সিনটি পুরু কাইটিনের ভেতর আবদ্ধ থাকে']
        },
        "correct": 0,
        "expl_en": 'Bt toxin exists as an inactive protoxin in Bacillus thuringiensis. When an insect ingests it, the alkaline pH of the insect midgut solubilizes the crystals and converts it into active toxin, creating pores.',
        "expl_bn": 'Bt টক্সিন ব্যাকটেরিয়ায় নিষ্ক্রিয় প্রোটক্সিন রূপে থাকে। ক্ষারীয় পতঙ্গ অন্ত্রে পৌঁছালে এটি সক্রিয় টক্সিনে পরিণত হয়ে অন্ত্রের কোষে ছিদ্র তৈরি করে।',
    },
    {
        "id": 'BIO-071',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biotechnology and Its Applications & Gene Therapy',
        "difficulty": 'Medium',
        "en": 'The first clinical gene therapy was given in 1990 to a 4-year-old girl suffering from which genetic deficiency?',
        "bn": '১৯৯০ সালে ৪ বছর বয়সী এক কন্যাশিশুর ওপর প্রথম ক্লিনিকাল জিন থেরাপি প্রয়োগ করা হয়েছিল কোন জিনগত ত্রুটির চিকিৎসার জন্য?',
        "opts": {
            "en": ['Adenosine Deaminase (ADA) deficiency causing SCID', 'Cystic fibrosis', 'Phenylketonuria', 'Beta-thalassemia'],
            "bn": ['অ্যাডেনোসিন ডিঅ্যামিনেজ (ADA) ঘাটতিজনিত SCID', 'সিস্টিক ফাইব্রোসিস', 'ফিনাইলকিটোনিউরিয়া', 'বিটা-থ্যালাসেমিয়া']
        },
        "correct": 0,
        "expl_en": 'The first clinical gene therapy was performed in 1990 on a 4-year-old girl with adenosine deaminase (ADA) deficiency, a hereditary disorder that severely impairs the immune system (causing severe combined immunodeficiency, SCID).',
        "expl_bn": '১৯৯০ সালে মারাত্মক রোগপ্রতিরোধ ঘাটতিজনিত (SCID) রোগে আক্রান্ত ৪ বছর বয়সী শিশুর মধ্যে ADA জিনের ত্রুটি দূর করতে প্রথম সফল জিন থেরাপি পরিচালিত হয়।',
    },
    {
        "id": 'BIO-072',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Organisms and Populations & Adaptations',
        "difficulty": 'Easy',
        "en": "According to Allen's Rule, mammals from colder climates typically have:",
        "bn": "অ্যালেনের নিয়ম (Allen's Rule) অনুসারে শীতল জলবায়ুর স্তন্যপায়ী প্রাণীদের দেহে সাধারণত কী ধরনের অভিযোজন দেখা যায়?",
        "opts": {
            "en": ['Shorter ears and shorter limbs to minimize heat loss', 'Longer ears and longer limbs to radiate heat', 'Larger surface area to volume ratio', 'Thinner subcutaneous fat layer'],
            "bn": ['তাপ ক্ষয় কমাতে ছোট কান এবং ছোট হাত-পা (অঙ্গপ্রত্যঙ্গ)', 'তাপ বিকিরণের জন্য বড় কান ও দীর্ঘ পা', 'আয়তনের তুলনায় বৃহত্তর পৃষ্ঠতলের ক্ষেত্রফল', 'ত্বকের নিচে পাতলা চর্বি স্তর']
        },
        "correct": 0,
        "expl_en": "Allen's Rule states that mammals from colder climates generally have shorter ears and limbs (extremities) to minimize heat loss by reducing surface area relative to volume.",
        "expl_bn": 'অ্যালেনের নীতি অনুযায়ী ঠান্ডার দেশে বসবাসকারী স্তন্যপায়ীদের কান ও উপাঙ্গ ছোট হয়, যাতে পৃষ্ঠতলের ক্ষেত্রফল কমে দেহের তাপ ক্ষয় ন্যূনতম হয়।',
    },
    {
        "id": 'BIO-073',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Organisms and Populations & Population Growth Models',
        "difficulty": 'Medium',
        "en": 'In the logistic growth equation dN/dt = rN((K - N)/K), what does the term (K - N)/K represent?',
        "bn": 'লজিস্টিক বৃদ্ধির সমীকরণ dN/dt = rN((K - N)/K)-এ (K - N)/K রাশিটি কী নির্দেশ করে?',
        "opts": {
            "en": ['Environmental resistance to population growth', 'Intrinsic rate of natural increase', 'Carrying capacity of the environment', 'Generation time'],
            "bn": ['পপুলেশন বৃদ্ধিতে পরিবেশীয় বাধা (Environmental resistance)', 'স্বাভাবিক বৃদ্ধির অন্তর্নিহিত হার', 'পরিবেশের বহন ক্ষমতা', 'প্রজন্ম কাল']
        },
        "correct": 0,
        "expl_en": 'In the Verhulst-Pearl Logistic Growth equation, K is the carrying capacity, and the term (K - N)/K represents the fraction of resources remaining or the environmental resistance that slows population growth as N approaches K.',
        "expl_bn": 'লজিস্টিক গ্রোথ সমীকরণে K হলো বহন ক্ষমতা এবং (K - N)/K রাশিটি বৃদ্ধি রোধকারী পরিবেশীয় বাধাকে (Environmental resistance) প্রকাশ করে।',
    },
    {
        "id": 'BIO-074',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Ecosystem & Ecological Pyramids',
        "difficulty": 'Easy',
        "en": 'Which ecological pyramid is NEVER inverted in any natural ecosystem?',
        "bn": 'কোন বাস্তুতান্ত্রিক পিরামিড যেকোনো প্রাকৃতিক বাস্তুতন্ত্রে সর্বদা সোজা থাকে এবং কখনো উল্টানো (inverted) হয় না?',
        "opts": {
            "en": ['Pyramid of energy', 'Pyramid of biomass', 'Pyramid of numbers', 'Pyramid of standing crop'],
            "bn": ['শক্তির পিরামিড (Pyramid of energy)', 'জীবভরের পিরামিড', 'সংখ্যার পিরামিড', 'স্ট্যান্ডিং ক্রপের পিরামিড']
        },
        "correct": 0,
        "expl_en": 'The pyramid of energy is always upright and can never be inverted because energy is continuously lost as metabolic heat (10% law of Lindeman) as it flows from one trophic level to the next.',
        "expl_bn": 'শক্তির পিরামিড সর্বদা খাড়া থাকে কারণ এক পুষ্টিস্তর থেকে অন্য স্তরে যাওয়ার সময় শক্তির অপচয় ঘটে (১০% সূত্র), ফলে উচ্চ স্তরে শক্তি সর্বদা হ্রাস পায়।',
    },
    {
        "id": 'BIO-075',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Ecosystem & Productivity',
        "difficulty": 'Easy',
        "en": 'The rate of formation of new organic matter by consumers is defined as:',
        "bn": 'বাস্তুতন্ত্রে খাদকদের (consumers) দ্বারা নতুন জৈব পদার্থ গঠনের হারকে কী বলা হয়?',
        "opts": {
            "en": ['Secondary productivity', 'Net primary productivity (NPP)', 'Gross primary productivity (GPP)', 'Community respiration'],
            "bn": ['গৌণ উৎপাদনশীলতা (Secondary productivity)', 'প্রকৃত প্রাথমিক উৎপাদনশীলতা (NPP)', 'মোট প্রাথমিক উৎপাদনশীলতা (GPP)', 'কমিউনিটি শ্বসন']
        },
        "correct": 0,
        "expl_en": 'Secondary productivity is defined as the rate of assimilation and synthesis of new organic matter by consumers (herbivores and carnivores) over a given period.',
        "expl_bn": 'খাদক বা ভোক্তাদের দ্বারা খাদ্যের আত্মীকরণ ও নতুন জীবভর সংশ্লেষণের হারকে গৌণ উৎপাদনশীলতা (Secondary productivity) বলে।',
    },
    {
        "id": 'BIO-076',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biodiversity and Conservation & Threats',
        "difficulty": 'Easy',
        "en": "The 'Evil Quartet' refers to the four major causes of biodiversity loss. Among these, the most important driver leading to extinction of species is:",
        "bn": "'ইভিল কোয়ার্টেট' হলো জীববৈচিত্র্য হ্রাসের চারটি প্রধান কারণ। এর মধ্যে প্রজাতি বিলুপ্তির সর্বাধিক গুরুত্বপূর্ণ কারণ কোনটি?",
        "opts": {
            "en": ['Habitat loss and fragmentation', 'Over-exploitation', 'Alien species invasions', 'Co-extinctions'],
            "bn": ['বাসস্থান ধ্বংস এবং খণ্ডীকরণ (Habitat loss and fragmentation)', 'অতিরিক্ত ব্যবহার বা শোষণ', 'বিদেশী প্রজাতির অনুপ্রবেশ', 'সহ-বিলুপ্তি']
        },
        "correct": 0,
        "expl_en": 'Habitat loss and fragmentation is the single most important cause driving animals and plants to extinction (e.g., destruction of the Amazon rainforest for soybean cultivation).',
        "expl_bn": 'প্রাকৃতিক বাসস্থান ধ্বংস এবং তার খণ্ডীকরণ হলো জীববৈচিত্র্য ধ্বংসের এক নম্বর ও প্রধানতম কারণ।',
    },
    {
        "id": 'BIO-077',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biodiversity and Conservation & In-situ and Ex-situ',
        "difficulty": 'Easy',
        "en": 'Which of the following is an example of ex-situ (off-site) biodiversity conservation?',
        "bn": 'নিচের কোনটি এক্স-সিটু (স্থানান্তর) জীববৈচিত্র্য সংরক্ষণের উদাহরণ?',
        "opts": {
            "en": ['Botanical gardens and Zoological parks', 'National Parks', 'Wildlife Sanctuaries', 'Biosphere Reserves'],
            "bn": ['বোটানিক্যাল গার্ডেন এবং চিড়িয়াখানা', 'জাতীয় উদ্যান', 'অভয়ারণ্য', 'বায়োস্ফিয়ার রিজার্ভ']
        },
        "correct": 0,
        "expl_en": 'In ex-situ conservation, threatened animals and plants are taken out from their natural habitat and placed in special care settings such as zoological parks, botanical gardens, and seed banks.',
        "expl_bn": 'বোটানিক্যাল গার্ডেন, চিড়িয়াখানা এবং বীজ ব্যাংক হলো এক্স-সিটু সংরক্ষণের উদাহরণ যেখানে বিপন্ন জীবকে নিজস্ব বাসস্থানের বাইরে সুরক্ষিত রাখা হয়।',
    },
    {
        "id": 'BIO-078',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Environmental Issues & Biomagnification',
        "difficulty": 'Easy',
        "en": 'Biomagnification of non-biodegradable pollutants like DDT through aquatic food chains reaches its maximum concentration in:',
        "bn": 'জলজ খাদ্য শৃঙ্খলে DDT-এর মতো অপচনশীল পদার্থের জৈব-বিবর্ধন (Biomagnification) সর্বোচ্চ স্তরে কার দেহে পৌঁছায়?',
        "opts": {
            "en": ['Fish-eating birds (top carnivores, ~25 ppm)', 'Zooplankton (~0.04 ppm)', 'Small fish (~0.5 ppm)', 'Phytoplankton (~0.003 ppm)'],
            "bn": ['মাছখেকো পাখি (শীর্ষ খাদক, ~২৫ ppm)', 'জুপ্ল্যাঙ্কটন (~০.০৪ ppm)', 'ছোট মাছ (~০.৫ ppm)', 'ফাইটোপ্ল্যাঙ্কটন (~০.০০৩ ppm)']
        },
        "correct": 0,
        "expl_en": 'DDT is lipophilic and non-metabolizable. As it moves up trophic levels from water (0.003 ppb) → zooplankton (0.04 ppm) → small fish (0.5 ppm) → large fish (2 ppm), it accumulates to 25 ppm in fish-eating birds, causing thinning of eggshells.',
        "expl_bn": 'DDT খাদ্যশৃঙ্খলের প্রতিটি স্তরে ক্রমাগত ঘনীভূত হয়ে শীর্ষ স্তরে মাছখেকো পাখির দেহে সর্বোচ্চ ২৫ ppm পর্যন্ত পৌঁছায়, যা ডিমের খোলস পাতলা করে প্রজনন ব্যাহত করে।',
    },
    {
        "id": 'BIO-079',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Environmental Issues & Ozone Depletion',
        "difficulty": 'Easy',
        "en": 'The international treaty signed in 1987 to control emissions of ozone-depleting substances is known as the:',
        "bn": 'ওজোন স্তর ক্ষয়কারী পদার্থের নির্গমন নিয়ন্ত্রণের জন্য ১৯৮৭ সালে স্বাক্ষরিত আন্তর্জাতিক চুক্তিটি কী নামে পরিচিত?',
        "opts": {
            "en": ['Montreal Protocol', 'Kyoto Protocol', 'Paris Agreement', 'Ramsar Convention'],
            "bn": ['মন্ট্রিল প্রোটোকল (Montreal Protocol)', 'কিয়োটো প্রোটোকল', 'প্যারিস চুক্তি', 'রামসার সম্মেলন']
        },
        "correct": 0,
        "expl_en": 'The Montreal Protocol was signed in Montreal (Canada) in 1987 (effective in 1989) to curb the production and consumption of ozone depleting substances such as CFCs.',
        "expl_bn": '১৯৮৭ সালে কানাডার মন্ট্রিলে সিএফসি সহ ওজোন স্তর বিনাশকারী রাসায়নিক রোধ করতে ঐতিহাসিক মন্ট্রিল প্রোটোকল স্বাক্ষরিত হয়।',
    },
    {
        "id": 'BIO-080',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Ecology & Species-Area Relationship',
        "difficulty": 'Medium',
        "en": 'Alexander von Humboldt observed that within a region, species richness increases with increasing explored area up to a limit, represented by the rectangular hyperbola equation:',
        "bn": 'আলেকজান্ডার ভন হামবোল্ট পর্যবেক্ষণ করেন যে নির্দিষ্ট অঞ্চলে অন্বেষণ এলাকা বাড়ার সাথে প্রজাতির প্রাচুর্য বাড়ে, যার সমীকরণ হলো:',
        "opts": {
            "en": ['log S = log C + Z log A', 'log S = log A + Z log C', 'S = C · A<sup>r</sup>', 'dN/dt = rN(1 - N/K)'],
            "bn": ['log S = log C + Z log A', 'log S = log A + Z log C', 'S = C · A<sup>r</sup>', 'dN/dt = rN(1 - N/K)']
        },
        "correct": 0,
        "expl_en": "Alexander von Humboldt's species-area relationship is described by S = C A<sup>Z</sup>, which on a logarithmic scale gives a straight line equation: log S = log C + Z log A (where S = species richness, A = area, Z = regression coefficient/slope, C = Y-intercept).",
        "expl_bn": 'হামবোল্টের প্রজাতি-এলাকা সম্পর্কের সমীকরণ S = C A<sup>Z</sup>। লগ স্কেলে এটি সরলরেখার রূপ নেয়: log S = log C + Z log A।',
    },
    {
        "id": 'BIO-LW-001',
        "exam": 'NEET, AIIMS, AFMC, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": "Which of the following pairs are considered the 'twin characteristics' of growth in all living organisms according to NCERT?",
        "bn": "NCERT অনুসারে সমস্ত জীবের ক্ষেত্রে বৃদ্ধির 'যমজ বৈশিষ্ট্য' (twin characteristics) হিসেবে কোন জোড়াটিকে বিবেচনা করা হয়?",
        "opts": {
            "en": ['Increase in mass and increase in number of individuals', 'Increase in height and increase in volume', 'Cellular differentiation and response to stimuli', 'Metabolic synthesis and cell division'],
            "bn": ['ভরের বৃদ্ধি এবং জীবের সংখ্যার বৃদ্ধি', 'উচ্চতা বৃদ্ধি এবং আয়তন বৃদ্ধি', 'কোষীয় বিভেদন এবং উদ্দীপনায় সাড়া দেওয়া', 'বিপাকীয় সংশ্লেষ এবং কোষ বিভাজন']
        },
        "correct": 0,
        "expl_en": 'According to NCERT, increase in mass and increase in number of individuals are twin characteristics of growth. In unicellular organisms, growth and reproduction are synonymous as both involve an increase in cell number.',
        "expl_bn": 'NCERT অনুযায়ী, সামগ্রিক ভর বৃদ্ধি এবং জীবসংখ্যার বৃদ্ধি হলো বৃদ্ধির যমজ বৈশিষ্ট্য। এককোষী জীবে কোষ বিভাজনের মাধ্যমে সংখ্যাবৃদ্ধি বৃদ্ধি ও জনন উভয়কেই বোঝায়।',
    },
    {
        "id": 'BIO-LW-002',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'In plants, growth by cell division occurs ________, whereas in animals, this growth is seen ________.',
        "bn": 'উদ্ভিদে কোষ বিভাজনের মাধ্যমে বৃদ্ধি ঘটে ________, যেখানে প্রাণীদের ক্ষেত্রে এই বৃদ্ধি দেখা যায় ________।',
        "opts": {
            "en": ['continuously throughout their life span; only up to a certain age', 'only up to a certain age; continuously throughout their life span', 'only during reproductive phase; only during embryonic phase', 'only in localized zones; uniformly across the entire body continuously'],
            "bn": ['সারা জীবনকাল ধরে নিরবচ্ছিন্নভাবে; শুধুমাত্র নির্দিষ্ট বয়স পর্যন্ত', 'শুধুমাত্র নির্দিষ্ট বয়স পর্যন্ত; সারা জীবনকাল ধরে নিরবচ্ছিন্নভাবে', 'শুধুমাত্র প্রজনন দশায়; শুধুমাত্র ভ্রূণীয় দশায়', 'শুধুমাত্র নির্দিষ্ট অঞ্চলে; সারা দেহে সর্বদা সুষমভাবে']
        },
        "correct": 0,
        "expl_en": 'In plants, growth by cell division occurs continuously throughout their life span due to the presence of active meristematic tissues, whereas in animals, growth is determinate and seen only up to a certain age.',
        "expl_bn": 'উদ্ভিদে ভাজক কলার উপস্থিতির কারণে সারা জীবন ধরে বৃদ্ধি ঘটতে পারে, কিন্তু প্রাণীদের ক্ষেত্রে বৃদ্ধি সীমিত এবং শুধুমাত্র নির্দিষ্ট বয়স পর্যন্ত ঘটে।',
    },
    {
        "id": 'BIO-LW-003',
        "exam": 'NEET, CUET, OLYMPIAD',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Why is growth alone NOT considered an all-inclusive defining property of living organisms?',
        "bn": 'কেবলমাত্র বৃদ্ধিকে কেন সজীব বস্তুর সর্বজনীন সংজ্ঞাবহ বৈশিষ্ট্য (defining property) হিসেবে গণ্য করা যায় না?',
        "opts": {
            "en": ['Non-living objects like mountains, boulders, and sand mounds also grow by extrinsic accumulation of material', 'Living organisms stop growing after reaching sexual maturity', 'Growth cannot be measured quantitatively in microorganisms', 'Certain living organisms show negative growth throughout life'],
            "bn": ['পাহাড়, বোল্ডার ও বালিয়াড়ির মতো নির্জীব বস্তুও বাইরে থেকে পদার্থ জমা হয়ে বৃদ্ধি পায়', 'যৌন পরিপক্বতা অর্জনের পর জীবদেহের বৃদ্ধি সম্পূর্ণ বন্ধ হয়ে যায়', 'অণুজীবের ক্ষেত্রে বৃদ্ধিকে পরিমাপগতভাবে গণনা করা যায় না', 'কিছু জীব সারা জীবন ধরে ঋণাত্মক বৃদ্ধি প্রদর্শন করে']
        },
        "correct": 0,
        "expl_en": 'Non-living objects such as mountains, boulders, and sand dunes also exhibit growth by extrinsic surface accumulation (accretion). In living organisms, growth is from inside (intrinsic). Hence, growth cannot be taken as an absolute defining property without qualifying it as intrinsic.',
        "expl_bn": 'পাহাড় বা বালিয়াড়ির মতো জড় বস্তুও বাইরের পদার্থ সঞ্চিত হয়ে আকারে বাড়ে (বহিঃস্থ বৃদ্ধি)। জীবের বৃদ্ধি ঘটে ভেতর থেকে (অভ্যন্তরীণ বৃদ্ধি)। তাই শর্তহীনভাবে বৃদ্ধি কোনো পরম সংজ্ঞাবহ বৈশিষ্ট্য নয়।',
    },
    {
        "id": 'BIO-LW-004',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'Fungi multiply and spread easily due to the production of millions of asexual spores. Which of the following organisms reproduces by true regeneration (where a fragmented body regenerates the lost part)?',
        "bn": 'লক্ষ লক্ষ অযৌন রেণু উৎপাদনের মাধ্যমে ছত্রাক দ্রুত বংশবৃদ্ধি করে। নিচের কোন জীবটিতে প্রকৃত পুনরুৎপত্তি (true regeneration) দেখা যায়, যেখানে দেহের খণ্ডিত অংশ থেকে সম্পূর্ণ নতুন জীব গঠিত হয়?',
        "opts": {
            "en": ['Planaria (flatworm)', 'Amoeba', 'Yeast', 'Hydra'],
            "bn": ['প্ল্যানেরিয়া (চ্যাপ্টাকৃমি)', 'অ্যামিবা', 'ইস্ট', 'হাইড্রা']
        },
        "correct": 0,
        "expl_en": 'Planaria (flatworms) exhibit true regeneration, where a fragmented organism regenerates the lost parts of its body and develops into a complete new individual.',
        "expl_bn": 'প্ল্যানেরিয়া (Planaria) নামক চ্যাপ্টাকৃমিতে প্রকৃত পুনরুৎপত্তি ক্ষমতা দেখা যায়, যার দেহের খণ্ডিত অংশ বিনষ্ট অংশ পুনর্গঠন করে নতুন জীবে পরিণত হয়।',
    },
    {
        "id": 'BIO-LW-005',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Which of the following groups of organisms reproduce exclusively or predominantly by fragmentation?',
        "bn": 'নিচের কোন জীবগোষ্ঠীটি প্রধানত বা বিশেষভাবে খণ্ডীভবন (fragmentation) প্রক্রিয়ায় বংশবৃদ্ধি করে?',
        "opts": {
            "en": ['Fungi, filamentous algae, and protonema of mosses', 'Amoeba, Paramecium, and Euglena', 'Yeast, Hydra, and Sycon', 'Bacteria, Cyanobacteria, and Mycoplasma'],
            "bn": ['ছত্রাক, সূত্রাকার শৈবাল এবং মসের প্রোটোনেমা', 'অ্যামিবা, প্যারামেসিয়াম এবং ইউগ্লিনা', 'ইস্ট, হাইড্রা এবং সাইকন', 'ব্যাকটেরিয়া, সায়ানোব্যাকটেরিয়া এবং মাইকোপ্লাজমা']
        },
        "correct": 0,
        "expl_en": "NCERT explicitly mentions: 'The fungi, the filamentous algae, the protonema of mosses, all easily multiply by fragmentation.'",
        "expl_bn": 'NCERT-তে সুস্পষ্টভাবে উল্লেখ রয়েছে যে ছত্রাক, সূত্রাকার শৈবাল এবং মসের প্রোটোনেমা—এরা সকলেই খণ্ডীভবন প্রক্রিয়ায় অতি সহজে বংশবৃদ্ধি করে।',
    },
    {
        "id": 'BIO-LW-006',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Reproduction cannot be an all-inclusive defining characteristic of living organisms primarily because:',
        "bn": 'প্রজননকে সজীব বস্তুর সর্বজনীন সংজ্ঞাবহ বৈশিষ্ট্য বলা যায় না, কারণ প্রধানত:',
        "opts": {
            "en": ['Many living organisms like mules, sterile worker bees, and infertile human couples do not reproduce', 'Unicellular organisms do not exhibit any form of genetic exchange', 'Reproduction requires an immense expenditure of metabolic energy', 'Lower plants reproduce only once during their life cycle'],
            "bn": ['খচ্চর, বন্ধ্যা শ্রমিক মৌমাছি এবং বন্ধ্যা মানব দম্পতির মতো বহু জীবিত প্রাণী প্রজননে অক্ষম', 'এককোষী জীবে কোনো প্রকার জিনগত আদান-প্রদান ঘটে না', 'প্রজনন প্রক্রিয়ায় বিপুল পরিমাণ বিপাকীয় শক্তির অপচয় ঘটে', 'নিম্নশ্রেণীর উদ্ভিদ তাদের সমগ্র জীবনকালে কেবল একবারই প্রজনন সম্পন্ন করে']
        },
        "correct": 0,
        "expl_en": 'There are many living organisms which do not reproduce (e.g., mules, sterile worker bees, infertile human couples). While non-living objects cannot reproduce, failure to reproduce does not make an entity non-living. Hence, reproduction is not an all-inclusive defining feature.',
        "expl_bn": 'খচ্চর, বন্ধ্যা শ্রমিক মৌমাছি বা বন্ধ্যা মানব দম্পতি বেঁচে থাকা সত্ত্বেও সন্তান জন্মদানে অক্ষম। তাই প্রজনন জীবদেহের একটি অপরিহার্য সাধারণ বৈশিষ্ট্য হলেও এটি সর্বজনীন সংজ্ঞাবহ (defining) বৈশিষ্ট্য নয়।',
    },
    {
        "id": 'BIO-LW-007',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'What is metabolism according to biological definitions?',
        "bn": 'জীববিজ্ঞান অনুযায়ী বিপাক (Metabolism) বলতে কী বোঝায়?',
        "opts": {
            "en": ["The sum total of all biochemical reactions occurring inside an organism's body", 'The catabolic breakdown of glucose into ATP inside mitochondria', 'The exchange of gases between cellular membranes and environment', 'The physical movement of cytoplasm within eukaryotic cells'],
            "bn": ['জীবদেহের অভ্যন্তরে সংঘটিত সমস্ত জৈব রাসায়নিক বিক্রিয়ার সামগ্রিক যোগফল', 'মাইটোকনড্রিয়ায় গ্লুকোজ ভেঙে ATP উৎপন্ন হওয়ার অপচিতিমূলক প্রক্রিয়া', 'কোষপর্দা ও পরিবেশের মধ্যে গ্যাসের ভৌত বিনিময়', 'ইউক্যারিওটিক কোষে সাইটোপ্লাজমের অভ্যন্তরীণ পরিচলন গতি']
        },
        "correct": 0,
        "expl_en": 'Metabolism is defined as the sum total of all the chemical reactions occurring in our body. Thousands of metabolic reactions occur simultaneously inside all living organisms (unicellular and multicellular).',
        "expl_bn": 'বিপাক হলো জীবদেহে সংঘটিত সমস্ত গঠনমূলক (উপচিতি) ও ধ্বংসাত্মক (অপচিতি) রাসায়নিক বিক্রিয়ার সমষ্টি।',
    },
    {
        "id": 'BIO-LW-008',
        "exam": 'NEET, AIIMS, CUET, OLYMPIAD',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'An isolated metabolic reaction performed in a test tube (in vitro cell-free system) is best described as:',
        "bn": 'টেস্ট টিউবে কোষমুক্ত পরিবেশে (in vitro) পরিচালিত একটি পৃথক বিপাকীয় বিক্রিয়াকে সঠিকভাবে কীভাবে ব্যাখ্যা করা যায়?',
        "opts": {
            "en": ['Neither living nor non-living as a thing, but surely a living reaction', 'A complete living organism because it generates biological products', 'A purely non-living physical phenomenon', 'An artificial artifact that cannot occur in nature'],
            "bn": ['বস্তু হিসেবে সজীব বা নির্জীব কোনটিই নয়, তবে নিশ্চিতভাবেই একটি সজীব বিক্রিয়া (living reaction)', 'একটি পূর্ণাঙ্গ সজীব সত্তা কারণ এটি জৈব পদার্থ তৈরি করে', 'সম্পূর্ণ নির্জীব একটি সাধারণ ভৌত ঘটনা', 'একটি কৃত্রিম ঘটনা যা প্রকৃতিতে ঘটতে পারে না']
        },
        "correct": 0,
        "expl_en": "NCERT specifies: 'An isolated metabolic reaction outside the body of an organism, performed in a test tube is neither living nor non-living. Isolated metabolic reactions in vitro are not living things but surely living reactions.'",
        "expl_bn": "NCERT-তে বলা হয়েছে: টেস্ট টিউবে ঘটিত কোনো বিচ্ছিন্ন বিপাকীয় বিক্রিয়া বস্তু হিসেবে সজীব বা নির্জীব কোনটিই নয়, তবে এটি নিশ্চিতভাবেই একটি 'সজীব বিক্রিয়া' (living reaction)।",
    },
    {
        "id": 'BIO-LW-009',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Which of the following is considered an absolute, exceptional-free defining feature of all life forms?',
        "bn": 'নিচের কোনটিকে সমস্ত জীবের কোনো ব্যতিক্রমহীন পরম সংজ্ঞাবহ বৈশিষ্ট্য (defining feature) হিসেবে বিবেচনা করা হয়?',
        "opts": {
            "en": ['Cellular organisation of the body and metabolism', 'Growth and reproduction', 'Locomotion and sexual reproduction', 'Morphological development and spore formation'],
            "bn": ['দেহের কোষীয় সংগঠন এবং বিপাক ক্রিয়া', 'বৃদ্ধি এবং প্রজনন', 'চলন-গমন এবং যৌন জনন', 'বাহ্যিক বৃদ্ধি এবং রেণু উৎপাদন']
        },
        "correct": 0,
        "expl_en": 'Metabolism and cellular organization of the body are defining features of life forms without exception, because no non-living object exhibits metabolism or cellular architecture.',
        "expl_bn": 'বিপাক এবং দেহের কোষীয় সংগঠন হলো সজীবতার ব্যতিক্রমহীন সংজ্ঞাবহ বৈশিষ্ট্য, কারণ কোনো নির্জীব বস্তুতে কোষীয় সংগঠন বা বিপাকীয় বিক্রিয়া ঘটে না।',
    },
    {
        "id": 'BIO-LW-010',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'The most technically complicated and defining property of all living organisms is:',
        "bn": 'সমস্ত সজীব বস্তুর সবচেয়ে জটিল ও প্রযুক্তিগতভাবে প্রধান সংজ্ঞাবহ বৈশিষ্ট্য কোনটি?',
        "opts": {
            "en": ['Consciousness and the ability to sense environmental stimuli and respond to them', 'Ability to produce multicellular gametes', 'Possession of a double-membrane bounded nucleus', 'Continuous increase in dry biomass throughout life'],
            "bn": ['চেতনা (Consciousness) এবং পরিবেশের উদ্দীপনা উপলব্ধি করে সাড়া দেওয়ার ক্ষমতা', 'বহুকোষী গ্যামেট উৎপাদনের সামর্থ্য', 'দ্বি-স্তরবিশিষ্ট আবরণীযুক্ত নিউক্লিয়াসের উপস্থিতি', 'সারা জীবনব্যাপী শুষ্ক ওজনের ক্রমাগত বৃদ্ধি']
        },
        "correct": 0,
        "expl_en": 'According to NCERT, the most obvious and technically complicated feature of all living organisms is the ability to sense their surroundings or environment and respond to these environmental stimuli (physical, chemical, or biological), termed consciousness.',
        "expl_bn": 'NCERT-র মতে, সমস্ত জীবের সবচেয়ে সুস্পষ্ট অথচ প্রযুক্তিগতভাবে সবচেয়ে জটিল বৈশিষ্ট্য হলো পারিপার্শ্বিক পরিবেশের উদ্দীপনা অনুধাবন করা এবং তার প্রতি সাড়া দেওয়া (চেতনা)।',
    },
    {
        "id": 'BIO-LW-011',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'Photoperiod directly influences reproduction in which of the following categories of organisms?',
        "bn": 'আলোককাল (Photoperiod) সরাসরি কোন শ্রেণীর জীবের প্রজননকে প্রভাবিত করে?',
        "opts": {
            "en": ['Seasonal breeders, both plants and animals', 'Continuous breeders among domestic mammals only', 'Deep-sea hydrothermal benthic fauna only', 'Non-photosynthetic parasitic fungi only'],
            "bn": ['উদ্ভিদ ও প্রাণী উভয়ের মধ্যে ঋতুভিত্তিক প্রজননকারীদের (seasonal breeders)', 'শুধুমাত্র গৃহপালিত স্তন্যপায়ী প্রাণীদের', 'কেবলমাত্র গভীর সমুদ্রের তলদেশের জীবদের', 'শুধুমাত্র সালোকসংশ্লেষে অক্ষম পরজীবী ছত্রাকদের']
        },
        "correct": 0,
        "expl_en": "NCERT states: 'Photoperiod affects reproduction in seasonal breeders, both plants and animals. All organisms handle chemicals entering their bodies.'",
        "expl_bn": 'আলোককাল উদ্ভিদ এবং প্রাণী উভয়েরই ঋতুভিত্তিক প্রজননকারীদের (seasonal breeders) জননক্রিয়াকে সরাসরি প্রভাবিত করে।',
    },
    {
        "id": 'BIO-LW-012',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Self-consciousness (the awareness of oneself) is a unique attribute found exclusively in:',
        "bn": 'আত্ম-সচেতনতা (Self-consciousness) নামক অনন্য বৈশিষ্ট্যটি কেবলমাত্র কার মধ্যে দেখতে পাওয়া যায়?',
        "opts": {
            "en": ['Human beings (Homo sapiens)', 'All mammals and birds', 'All primates and cetaceans', 'All eukaryotic multicellular organisms'],
            "bn": ['মানুষ (Homo sapiens)', 'সমস্ত স্তন্যপায়ী প্রাণী ও পাখিদের', 'সমস্ত প্রাইমেট এবং সিটাসিয়ানদের', 'সমস্ত ইউক্যারিওটিক বহুকোষী জীবে']
        },
        "correct": 0,
        "expl_en": "While all living organisms possess consciousness (awareness of their surroundings), human beings are the only organisms that possess 'self-consciousness', i.e., awareness of oneself.",
        "expl_bn": "সমস্ত জীবের পরিবেশীয় চেতনা থাকলেও কেবলমাত্র মানুষই একমাত্র জীব যার 'আত্ম-সচেতনতা' (self-consciousness) রয়েছে।",
    },
    {
        "id": 'BIO-LW-013',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'A patient lying in a coma in a hospital supported by machines with a brain-dead status:',
        "bn": 'হাসপাতালে লাইফ-সাপোর্ট যন্ত্রের সাহায্যে কোমায় থাকা এবং ব্রেন-ডেড ঘোষিত একজন রোগী সম্পর্কে কোনটি সঠিক?',
        "opts": {
            "en": ['Has no self-consciousness, making the determination of living vs non-living state a profound medical dilemma', 'Is scientifically classified as a non-living thermodynamic system', 'Has completely ceased all cellular metabolic biochemical reactions', 'Is classified as dead under all biological nomenclatures'],
            "bn": ['কোনো আত্ম-সচেতনতা নেই, যা জীবন্ত নাকি মৃত তা নির্ধারণে গভীর দার্শনিক ও চিকিৎসাগত দ্বিধা সৃষ্টি করে', 'বিজ্ঞানের দৃষ্টিতে একটি সম্পূর্ণ জড় পদার্থ হিসেবে গণ্য হয়', 'কোষীয় সমস্ত বিপাকীয় রাসায়নিক বিক্রিয়া সম্পূর্ণ বন্ধ হয়ে গেছে', 'সমস্ত জৈবিক নামকরণে আনুষ্ঠানিকভাবে মৃত ঘোষিত হয়']
        },
        "correct": 0,
        "expl_en": 'NCERT notes: A brain-dead patient in a coma has no self-consciousness. Such cases highlight the conceptual boundary between living and non-living, since metabolic processes are maintained artificially by machines.',
        "expl_bn": 'কোমায় থাকা ব্রেন-ডেড ব্যক্তির নিজস্ব আত্ম-সচেতনতা থাকে না, তবে যন্ত্রের সাহায্যে বিপাক বজায় থাকায় তিনি জীবন্ত না মৃত তা নির্ধারণ করা এক জটিল বৈজ্ঞানিক প্রশ্ন।',
    },
    {
        "id": 'BIO-LW-014',
        "exam": 'NEET, CUET, OLYMPIAD',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Properties of tissues are not present in the constituent cells but arise as a result of:',
        "bn": 'কলা (Tissue)-র নিজস্ব বৈশিষ্ট্যগুলি তার উপাদান কোষগুলির মধ্যে পৃথকভাবে বিদ্যমান থাকে না, বরং এটি সৃষ্টি হয়:',
        "opts": {
            "en": ['Interactions among the constituent cells', 'Mutations occurring during mitotic divisions', 'Independent non-cooperative activities of cellular organelles', 'Simple additive accumulation of cellular cytoplasm'],
            "bn": ['উপাদান কোষগুলির পারস্পরিক আন্তঃক্রিয়ার (interactions) ফলে', 'মাইটোটিক বিভাজনের সময় আকস্মিক পরিব্যক্তির ফলে', 'কোষীয় অঙ্গাণুসমূহের স্বাধীন অসংযুক্ত ক্রিয়ার কারণে', 'কোষীয় সাইটোপ্লাজমের সরল গাণিতিক যোগফলের কারণে']
        },
        "correct": 0,
        "expl_en": 'NCERT emphasizes emergent properties: Properties of tissues are not present in constituent cells but arise as a result of interactions among the constituent cells. Similarly, organelle properties arise from molecular interactions.',
        "expl_bn": 'কলায় এমন কিছু বিশেষ ধর্ম বা বৈশিষ্ট্য প্রকাশ পায় যা একক কোষে থাকে না; উপাদান কোষগুলির পারস্পরিক আন্তঃক্রিয়া ও সমন্বয়ের ফলেই এই অনন্য ধর্মের উদ্ভব ঘটে।',
    },
    {
        "id": 'BIO-LW-015',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": "Which comprehensive statement best defines 'living organisms' based on emergent biological principles?",
        "bn": "আবির্ভূত জৈবনীতির (emergent biological principles) ওপর ভিত্তি করে 'জীব'-এর সবচেয়ে নিখুঁত সংজ্ঞা কোনটি?",
        "opts": {
            "en": ['Self-replicating, evolving, and self-regulating interactive systems capable of responding to external stimuli', 'Static thermodynamic systems that exchange only energy with their surroundings', 'Entities that grow only by physical surface deposition of organic minerals', 'Machines programmed exclusively by RNA genomes without environmental feedback'],
            "bn": ['স্ব-প্রজননশীল, বিবর্তনীয় এবং স্ব-নিয়ন্ত্রিত মিথস্ক্রিয়াতন্ত্র যা বাহ্যিক উদ্দীপনায় সাড়া প্রদানে সক্ষম', 'স্থির তাপগতীয় ব্যবস্থা যা পরিবেশের সাথে কেবল শক্তির বিনিময় ঘটায়', 'এমন সত্তা যা কেবল বহিঃস্থ খনিজ পদার্থ সঞ্চিত হয়ে বৃদ্ধি পায়', 'পরিবেশের সাথে কোনো সম্পর্কহীন RNA চালিত একপ্রকার যান্ত্রিক ব্যবস্থা']
        },
        "correct": 0,
        "expl_en": "NCERT defines: 'Living organisms are self-replicating, evolving and self-regulating interactive systems capable of responding to external stimuli. Biology is the story of life on earth.'",
        "expl_bn": 'NCERT-র সংজ্ঞানুসারে: জীব হলো স্ব-প্রজননশীল, বিবর্তনশীল এবং স্ব-নিয়ন্ত্রক পারস্পরিক ক্রিয়াশীল ব্যবস্থা যা বাহ্যিক উদ্দীপনায় সাড়া দিতে সক্ষম।',
    },
    {
        "id": 'BIO-LW-016',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'All living organisms—present, past, and future—are linked to one another by:',
        "bn": 'অতীত, বর্তমান এবং ভবিষ্যতের সমস্ত জীব পরস্পর পরস্পরের সাথে সম্পর্কযুক্ত, কারণ:',
        "opts": {
            "en": ['The sharing of the common genetic material, but to varying degrees', 'Having an identical number of chromosomes in their nuclei', 'Possessing identical morphological features and body sizes', 'Relying upon the same exact enzymes for nitrogen fixation'],
            "bn": ['তারা সকলেই ভিন্ন ভিন্ন মাত্রায় একই সাধারণ জিনগত বস্তু (DNA/RNA) বহন করে', 'তাদের নিউক্লিয়াসে ক্রোমোজোম সংখ্যা হুবহু একই থাকে', 'তাদের সকলের দৈহিক গঠন ও আকার হুবহু একরকম হয়', 'তারা সকলেই নাইট্রোজেন সংবন্ধনের জন্য একই উৎসেচকের ওপর নির্ভরশীল']
        },
        "correct": 0,
        "expl_en": "NCERT states: 'All living organisms—present, past and future, are linked to one another by the sharing of the common genetic material, but to varying degrees.'",
        "expl_bn": 'অতীত, বর্তমান এবং ভবিষ্যতের সমস্ত জীব共通 জিনগত বস্তু (ডিএনএ) বহন করে, যদিও এদের মধ্যে পার্থক্যের মাত্রা বিভিন্ন।',
    },
    {
        "id": 'BIO-LW-017',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'According to current documented scientific records cited in NCERT, the estimated number of known and described species on Earth is:',
        "bn": 'NCERT পাঠ্যপুস্তক অনুযায়ী পৃথিবীতে এ পর্যন্ত আবিষ্কৃত ও বিজ্ঞানসম্মতভাবে বর্ণিত প্রজাতির আনুমানিক সংখ্যা কত?',
        "opts": {
            "en": ['1.7 to 1.8 million', '1.1 to 1.2 million', '2.5 to 3.0 million', '7.0 to 8.0 million'],
            "bn": ['১.৭ থেকে ১.৮ মিলিয়ন (১৭-১৮ লক্ষ)', '১.১ থেকে ১.২ মিলিয়ন', '২.৫ থেকে ৩.০ মিলিয়ন', '৭.০ থেকে ৮.০ মিলিয়ন']
        },
        "correct": 0,
        "expl_en": 'NCERT states that the number of species that are known and described ranges between 1.7–1.8 million. This refers to biodiversity on Earth.',
        "expl_bn": 'NCERT অনুসারে বর্তমানে পৃথিবীতে বর্ণিত ও পরিচিত প্রজাতির সংখ্যা প্রায় ১.৭ থেকে ১.৮ মিলিয়ন (১৭ থেকে ১৮ লক্ষ)।',
    },
    {
        "id": 'BIO-LW-018',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'What is the primary scientific purpose of standardizing the naming of living organisms through nomenclature?',
        "bn": 'নির্দিষ্ট বৈজ্ঞানিক নিয়মে নামকরণের (Nomenclature) মূল উদ্দেশ্য কী?',
        "opts": {
            "en": ['To ensure that each organism is known by the same unique name all over the world without confusion', 'To describe the physiological habitat and climatic tolerance of the organism', 'To assign common local vernacular names for ease of local farmers', 'To categorize organisms strictly based on commercial economic value'],
            "bn": ['সারা বিশ্বজুড়ে যাতে একটি নির্দিষ্ট জীব একটিমাত্র সার্বজনীন নামে পরিচিত হয় এবং কোনো বিভ্রান্তি না ঘটে', 'জীবটির প্রাকৃতিক বাসস্থান ও জলবায়ু সহনশীলতা প্রকাশ করা', 'স্থানীয় কৃষকদের সুবিধার্থে বিভিন্ন ভাষায় স্থানীয় নাম প্রদান করা', 'শুধুমাত্র বাণিজ্যিক গুরুত্বের ভিত্তিতে জীবকে ভাগ করা']
        },
        "correct": 0,
        "expl_en": 'Nomenclature standardizes the naming of living organisms such that a particular organism is known by the same name all over the world, preventing confusion caused by local vernacular names.',
        "expl_bn": 'নামকরণের মূল লক্ষ্য হলো বিশ্বজুড়ে একটি জীবকে কেবল একটি সুনির্দিষ্ট নামে চিহ্নিত করা, যাতে স্থানীয় বিভিন্ন ভাষার নামের কারণে কোনো বিভ্রান্তি তৈরি না হয়।',
    },
    {
        "id": 'BIO-LW-019',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'For plants, scientific names are provided and agreed upon under principles outlined by which international organization?',
        "bn": 'উদ্ভিদের বৈজ্ঞানিক নামকরণের নিয়মাবলী ও মূলনীতি কোন আন্তর্জাতিক সংস্থা কর্তৃক নির্ধারিত হয়?',
        "opts": {
            "en": ['ICBN (International Code of Botanical Nomenclature)', 'ICZN (International Code of Zoological Nomenclature)', 'IUCN (International Union for Conservation of Nature)', 'ICNB (International Code of Normal Bacteriology)'],
            "bn": ['ICBN (International Code of Botanical Nomenclature)', 'ICZN (International Code of Zoological Nomenclature)', 'IUCN (International Union for Conservation of Nature)', 'ICNB (International Code of Normal Bacteriology)']
        },
        "correct": 0,
        "expl_en": 'For plants, scientific principles and criteria are provided in the International Code of Botanical Nomenclature (ICBN). For animals, it is ICZN.',
        "expl_bn": 'উদ্ভিদের নামকরণের আন্তর্জাতিক নীতিমালা ICBN (International Code of Botanical Nomenclature) দ্বারা নির্ধারিত হয়।',
    },
    {
        "id": 'BIO-LW-020',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'The system of Binomial Nomenclature, where each scientific name has two components (generic name and specific epithet), was introduced by:',
        "bn": 'দ্বিপদ নামকরণ (Binomial Nomenclature) পদ্ধতি, যাতে প্রতিটি নামের দুটি অংশ (গণ ও প্রজাতি) থাকে, কার দ্বারা প্রবর্তিত হয়?',
        "opts": {
            "en": ['Carolus Linnaeus', 'Ernst Mayr', 'R.H. Whittaker', 'Bentham and Hooker'],
            "bn": ['ক্যারোলাস লিনিয়াস', 'আর্নস্ট মেয়ার', 'আর. এইচ. হুইটেকার', 'বেন্থাম ও হুকার']
        },
        "correct": 0,
        "expl_en": 'The system of providing a name with two components—the Generic name and the specific epithet—is called Binomial Nomenclature, introduced by Swedish naturalist Carolus Linnaeus.',
        "expl_bn": 'ক্যারোলাস লিনিয়াস দ্বিপদ নামকরণ পদ্ধতির প্রবর্তন করেন, যাতে প্রতিটি বৈজ্ঞানিক নামের দুটি অংশ থাকে: প্রথমটি গণ (Genus) এবং দ্বিতীয়টি প্রজাতি (Species)।',
    },
    {
        "id": 'BIO-LW-021',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": "In the scientific name Mangifera indica Linn., the term 'Linn.' indicates that:",
        "bn": "আমের বৈজ্ঞানিক নাম Mangifera indica Linn.-এ 'Linn.' শব্দটি কী নির্দেশ করে?",
        "opts": {
            "en": ['The species was first described by Linnaeus', 'The tree belongs to the family Linaceae', 'The specimen was collected from a linear geographical habitat', 'The binomial name is in Greek language'],
            "bn": ['প্রজাতিটি সর্বপ্রথম লিনিয়াস দ্বারা বিজ্ঞানসম্মতভাবে বর্ণিত হয়েছিল', 'গাছটি লিনাসি (Linaceae) গোত্রের অন্তর্ভুক্ত', 'নমুনাটি একটি রৈখিক ভৌগোলিক অঞ্চল থেকে সংগৃহীত', 'দ্বিপদ নামটি প্রাচীন গ্রিক ভাষার অন্তর্গত']
        },
        "correct": 0,
        "expl_en": 'Name of the author appears after the specific epithet at the end of the biological name and is written in an abbreviated form, e.g., Mangifera indica Linn. It indicates that this species was first described by Linnaeus.',
        "expl_bn": "নির্দিষ্ট নামের শেষে লেখকের নাম সংক্ষেপে লেখা হয় (Author citation)। 'Linn.' নির্দেশ করে যে এই প্রজাতিটি সর্বপ্রথম বিজ্ঞানী লিনিয়াস বর্ণনা করেছিলেন।",
    },
    {
        "id": 'BIO-LW-022',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'Biological names are generally derived from which language and written in which style?',
        "bn": 'জীববৈজ্ঞানিক নামগুলি সাধারণত কোন ভাষা থেকে গৃহীত হয় এবং কোন হরফে মুদ্রিত হয়?',
        "opts": {
            "en": ['Latin language, printed in italics', 'Greek language, printed in bold Roman', 'English language, printed in underlined script', 'Sanskrit language, printed in italics'],
            "bn": ['ল্যাটিন ভাষা থেকে গৃহীত এবং ইটালিক্স হরফে মুদ্রিত', 'গ্রিক ভাষা থেকে গৃহীত এবং বোল্ড রোমান হরফে মুদ্রিত', 'ইংরেজি ভাষা থেকে গৃহীত এবং নিম্নরেখাযুক্ত হরফে মুদ্রিত', 'সংস্কৃত ভাষা থেকে গৃহীত এবং ইটালিক্স হরফে মুদ্রিত']
        },
        "correct": 0,
        "expl_en": 'Biological names are generally in Latin and written in italics. They are Latinised or derived from Latin irrespective of their origin because Latin is a dead language and avoids ambiguity.',
        "expl_bn": 'জীবের বৈজ্ঞানিক নাম সাধারণত ল্যাটিন ভাষা থেকে গৃহীত হয় এবং মুদ্রণের সময় বাঁকা অক্ষরে (Italics) মুদ্রিত হয়।',
    },
    {
        "id": 'BIO-LW-023',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'When handwritten, how should the scientific names of organisms be formatted according to the rules of binomial nomenclature?',
        "bn": 'দ্বিপদ নামকরণের আন্তর্জাতিক নিয়ম অনুযায়ী হাতে লেখার সময় বৈজ্ঞানিক নাম কীভাবে লেখা উচিত?',
        "opts": {
            "en": ['Both words should be separately underlined to indicate their Latin origin', 'Both words should be written in capital letters without underlining', 'Only the specific epithet should be underlined', 'A continuous single underline should be drawn beneath both words'],
            "bn": ['ল্যাটিন উৎপত্তি নির্দেশ করতে উভয় শব্দকে আলাদা আলাদাভাবে নিম্নরেখাঙ্কিত (separately underlined) করতে হবে', 'কোনো দাগ না দিয়ে দুটি শব্দকেই সম্পূর্ণ বড় হাতের অক্ষরে লিখতে হবে', 'শুধুমাত্র প্রজাতির নামটিকে দাগ দিয়ে চিহ্নিত করতে হবে', 'দুটি শব্দের নিচে একটানা একটিমাত্র রেখা টানতে হবে']
        },
        "correct": 0,
        "expl_en": 'According to the universal rules of binomial nomenclature: Both the words in a biological name, when handwritten, are separately underlined, or printed in italics to indicate their Latin origin.',
        "expl_bn": 'হাতে লেখার সময় গণ এবং প্রজাতি উভয় শব্দের নিচেই পৃথক পৃথকভাবে দাগ (underline) দিতে হয়।',
    },
    {
        "id": 'BIO-LW-024',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'In a scientific name, the generic name begins with a ________ letter while the specific epithet begins with a ________ letter.',
        "bn": 'একটি বৈজ্ঞানিক নামে গণের নাম শুরু হয় ________ অক্ষর দিয়ে এবং প্রজাতির নাম শুরু হয় ________ অক্ষর দিয়ে।',
        "opts": {
            "en": ['capital; small', 'small; capital', 'capital; capital', 'small; small'],
            "bn": ['বড় হাতের (Capital); ছোট হাতের (Small)', 'ছোট হাতের; বড় হাতের', 'বড় হাতের; বড় হাতের', 'ছোট হাতের; ছোট হাতের']
        },
        "correct": 0,
        "expl_en": 'The first word denoting the genus starts with a capital letter while the specific epithet starts with a small letter (e.g., Mangifera indica).',
        "expl_bn": 'গণের নাম সর্বদাই বড় হাতের (Capital) অক্ষর দিয়ে শুরু হয় এবং প্রজাতির নাম ছোট হাতের (Small) অক্ষর দিয়ে শুরু হয়।',
    },
    {
        "id": 'BIO-LW-025',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Tautonyms (where the generic name and specific epithet are identical, e.g., Catla catla, Naja naja):',
        "bn": 'টোটোনিম (Tautonyms - যেখানে গণ ও প্রজাতির নাম একই হয়, যেমন Catla catla, Naja naja):',
        "opts": {
            "en": ['Are valid in zoological nomenclature (ICZN) but strictly invalid in botanical nomenclature (ICBN)', 'Are valid in botanical nomenclature but strictly invalid in zoological nomenclature', 'Are universally rejected across both zoology and botany', 'Are permitted only for extinct fossilized gymnosperms'],
            "bn": ['প্রাণী নামকরণে (ICZN) সম্পূর্ণ বৈধ কিন্তু উদ্ভিদ নামকরণে (ICBN) কঠোরভাবে অবৈধ', 'উদ্ভিদ নামকরণে বৈধ কিন্তু প্রাণী নামকরণে সম্পূর্ণ নিষিদ্ধ', 'উদ্ভিদ ও প্রাণী উভয় নামকরণের ক্ষেত্রেই সর্বজনীনভাবে বাতিল', 'শুধুমাত্র বিলুপ্ত ব্যক্তবীজী উদ্ভিদের জীবাশ্মের জন্য অনুমোদিত']
        },
        "correct": 0,
        "expl_en": 'Tautonyms are names where the genus and species name are identical (e.g., Naja naja, Rattus rattus). They are valid for animals under ICZN, but strictly prohibited for plants under ICBN.',
        "expl_bn": 'প্রাণী নামকরণে টোটোনিম (যেমন Naja naja, Catla catla) সম্পূর্ণ বৈধ, কিন্তু উদ্ভিদ নামকরণে (ICBN) তা সম্পূর্ণ নিষিদ্ধ ও অবৈধ।',
    },
    {
        "id": 'BIO-LW-026',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": "The word 'Systematics' is derived from the Latin word 'systema', which literally means:",
        "bn": "'Systematics' শব্দটি ল্যাটিন শব্দ 'systema' থেকে উৎপত্তি লাভ করেছে, যার আক্ষরিক অর্থ হলো:",
        "opts": {
            "en": ['Systematic arrangement of organisms', 'Internal anatomical structure of organs', 'Phylogenetic mutation rate over geological time', 'Ecosystem trophic interactions'],
            "bn": ['জীবসমূহের নিয়মানুগ বা সুশৃঙ্খল বিন্যাস (Systematic arrangement)', 'অঙ্গসমূহের অভ্যন্তরীণ শারীরস্থানিক গঠন', 'ভূতাত্ত্বিক যুগে জাতিজনি পরিব্যক্তির হার', 'বাস্তুতন্ত্রের পুষ্টিস্তরগত পারস্পরিক ক্রিয়া']
        },
        "correct": 0,
        "expl_en": "The word systematics is derived from the Latin word 'systema' which means systematic arrangement of organisms. Linnaeus used Systema Naturae as the title of his publication.",
        "expl_bn": "'Systematics' শব্দটি ল্যাটিন 'systema' থেকে এসেছে যার অর্থ জীবসমূহের সুশৃঙ্খল ও নিয়মানুগ বিন্যাস। বিজ্ঞানী লিনিয়াস তাঁর বিখ্যাত গ্রন্থের নাম দিয়েছিলেন 'Systema Naturae'।",
    },
    {
        "id": 'BIO-LW-027',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Modern systematics includes which critical evolutionary aspect that traditional classical taxonomy did not emphasize?',
        "bn": 'আধুনিক সিস্টেমেটিক্সে কোন গুরুত্বপূর্ণ দিকটি অন্তর্ভুক্ত রয়েছে যা সনাতন বা ক্লাসিক্যাল ট্যাক্সোনমিতে অন্তর্ভুক্ত ছিল না?',
        "opts": {
            "en": ['Evolutionary and phylogenetic relationships among organisms', 'External morphological characteristics only', 'Gross habitat preferences of plants', 'Economic uses of organisms in human agriculture'],
            "bn": ['জীবদের মধ্যে বিবর্তনীয় বা জাতিজনি (Phylogenetic) সম্পর্ক', 'শুধুমাত্র বাহ্যিক অঙ্গসংস্থানিক বৈশিষ্ট্য', 'উদ্ভিদের স্বাভাবিক প্রাকৃতিক বাসস্থান', 'কৃষিক্ষেত্রে জীবের বাণিজ্যিক ব্যবহার']
        },
        "correct": 0,
        "expl_en": 'Modern systematics takes into account identification, nomenclature, classification along with evolutionary (phylogenetic) relationships between organisms.',
        "expl_bn": 'আধুনিক সিস্টেমেটিক্স সনাক্তকরণ, নামকরণ ও শ্রেণীবিন্যাসের পাশাপাশি জীবদের মধ্যকার ঐতিহাসিক বিবর্তনীয় (Phylogenetic) সম্পর্ককে বিশেষভাবে বিবেচনা করে।',
    },
    {
        "id": 'BIO-LW-028',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": "Who is revered as 'The Darwin of the 20th century' and pioneered the modern biological concept of species?",
        "bn": "কাকে 'বিংশ শতাব্দীর ডারউইন' বলা হয় এবং যিনি প্রজাতির আধুনিক জৈবিক ধারণার প্রবর্তন করেন?",
        "opts": {
            "en": ['Ernst Mayr', 'Carolus Linnaeus', 'Julian Huxley', 'Theodosius Dobzhansky'],
            "bn": ['আর্নস্ট মেয়ার (Ernst Mayr)', 'ক্যারোলাস লিনিয়াস', 'জুলিয়ান হাক্সলি', 'থিওডোসিয়াস ডবঝানস্কি']
        },
        "correct": 0,
        "expl_en": "Ernst Mayr (1904–2004), known as 'The Darwin of the 20th century', almost single-handedly made the origin of species diversity the central question of evolutionary biology and pioneered the biological species concept based on reproductive isolation.",
        "expl_bn": "আর্নস্ট মেয়ারকে 'বিংশ শতাব্দীর ডারউইন' বলা হয়। তিনি জননগত বিচ্ছিন্নতার ওপর ভিত্তি করে প্রজাতির আধুনিক জৈবিক ধারণা প্রতিষ্ঠা করেন।",
    },
    {
        "id": 'BIO-LW-029',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'Each rank or level in the taxonomic hierarchy represents a unit of classification and is commonly designated as a:',
        "bn": 'ট্যাক্সোনমিক স্তরক্রমের (Taxonomic hierarchy) প্রতিটি ধাপ বা স্তর শ্রেণীবিন্যাসের একক নির্দেশ করে এবং তাকে সাধারণত কী বলা হয়?',
        "opts": {
            "en": ['Taxon (plural: taxa)', 'Cohort', 'Biotype', 'Ecophene'],
            "bn": ['ট্যাক্সন (Taxon, বহুবচনে Taxa)', 'কোহর্ট (Cohort)', 'বায়োটাইপ', 'ইকোফিন']
        },
        "correct": 0,
        "expl_en": "Each category in the taxonomic hierarchy represents a rank and is commonly termed as a taxon (plural: taxa). For example, 'Insects' or 'Mammals' or 'Plants' are taxa at different levels.",
        "expl_bn": "ট্যাক্সোনমিক হায়ারার্কির প্রতিটি নির্দিষ্ট স্তর বা বিভাগকে 'ট্যাক্সন' (Taxon) বলা হয়। যেমন—স্তন্যপায়ী, পতঙ্গ বা উদ্ভিদ প্রত্যেকেই বিভিন্ন স্তরের ট্যাক্সন।",
    },
    {
        "id": 'BIO-LW-030',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": "Consider the terms: 'Dogs', 'Mammals', and 'Animals'. Which statement correctly describes their scientific status?",
        "bn": "'কুকুর', 'স্তন্যপায়ী' এবং 'প্রাণী'—এই পদগুলি সম্পর্কে নিচের কোন বক্তব্যটি বৈজ্ঞানিকভাবে সঠিক?",
        "opts": {
            "en": ['They represent taxa at different taxonomic levels', 'They represent three different species in the same family', 'They are three distinct non-taxonomic artificial groupings', 'They are synonyms representing the exact same taxonomic category'],
            "bn": ['এরা বিভিন্ন স্তরের ট্যাক্সন (Taxa at different levels) নির্দেশ করে', 'এরা একই গোত্রের তিনটি ভিন্ন ভিন্ন প্রজাতি', 'এরা তিনটি সম্পূর্ণ অনিয়মিত কৃত্রিম গোষ্ঠী', 'এরা একই ট্যাক্সোনমিক ক্যাটাগরির সমার্থক শব্দ']
        },
        "correct": 0,
        "expl_en": "NCERT explains that 'Animals', 'Mammals', and 'Dogs' all represent taxa, but they represent taxa at different levels. Animal represents kingdom, mammal represents class, and dog represents a specific species/genus.",
        "expl_bn": "NCERT অনুসারে 'প্রাণী', 'স্তন্যপায়ী' এবং 'কুকুর' প্রত্যেকেই একেকটি ট্যাক্সন, তবে তারা হায়ারার্কির ভিন্ন ভিন্ন ধাপ বা স্তরের ট্যাক্সন।",
    },
    {
        "id": 'BIO-LW-031',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'Which of the following represents the basic, lowest, and real fundamental unit of biological classification?',
        "bn": 'জীববৈজ্ঞানিক শ্রেণীবিন্যাসের সর্বনিম্ন, বাস্তব ও মৌলিক একক কোনটি?',
        "opts": {
            "en": ['Species', 'Genus', 'Family', 'Kingdom'],
            "bn": ['প্রজাতি (Species)', 'গণ (Genus)', 'গোত্র (Family)', 'জগৎ (Kingdom)']
        },
        "correct": 0,
        "expl_en": 'Taxonomic studies consider a group of individual organisms with fundamental similarities as a species. Species is the lowest, basic, and only natural real unit of biological classification.',
        "expl_bn": 'প্রজাতি (Species) হলো জৈবিক শ্রেণীবিন্যাসের সর্বনিম্ন ও প্রকৃত প্রাকৃতিক একক, যার অন্তর্ভুক্ত সদস্যদের মধ্যে মৌলিক গঠনগত সাদৃশ্য থাকে।',
    },
    {
        "id": 'BIO-LW-032',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": "In the botanical names Solanum tuberosum, Solanum melongena, and Solanum nigrum, 'tuberosum', 'melongena', and 'nigrum' denote:",
        "bn": "Solanum tuberosum, Solanum melongena এবং Solanum nigrum বৈজ্ঞানিক নামগুলিতে 'tuberosum', 'melongena' এবং 'nigrum' কী প্রকাশ করে?",
        "opts": {
            "en": ['Specific epithets', 'Generic names', 'Subgeneric varieties', 'Agricultural cultivar codes'],
            "bn": ['প্রজাতিক পদ (Specific epithets)', 'গণের নাম (Generic names)', 'উপ-গণের প্রকারভেদ', 'কৃষিভিত্তিক জাত কোড']
        },
        "correct": 0,
        "expl_en": 'In these names, Solanum is the generic name (genus), while tuberosum (potato), melongena (brinjal), and nigrum (black nightshade / makoi) represent specific epithets.',
        "expl_bn": 'এখানে Solanum হলো গণ (Genus), এবং tuberosum (আলু), melongena (বেগুন) ও nigrum (মাকয়) হলো সংশ্লিষ্ট প্রজাতির নির্দেশক পদ (Specific epithet)।',
    },
    {
        "id": 'BIO-LW-033',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'The scientific name of the domestic lion is Panthera leo, while that of the tiger is Panthera tigris, and the leopard is Panthera pardus. These three organisms belong to:',
        "bn": 'সিংহের বৈজ্ঞানিক নাম Panthera leo, বাঘের নাম Panthera tigris এবং চিতাবাঘের নাম Panthera pardus। এই তিনটি প্রাণী:',
        "opts": {
            "en": ['The same genus Panthera, but different species', 'The same species leo, but different genera', 'Three entirely distinct taxonomic families', 'The same order, but three different classes'],
            "bn": ['একই গণ Panthera-র অন্তর্ভুক্ত, কিন্তু পৃথক পৃথক প্রজাতি', 'একই প্রজাতি leo-র অন্তর্ভুক্ত, কিন্তু বিভিন্ন গণের প্রাণী', 'তিনটি সম্পূর্ণ ভিন্ন প্রাণী গোত্রভুক্ত', 'একই বর্গের অন্তর্ভুক্ত, কিন্তু তিনটি পৃথক শ্রেণীর']
        },
        "correct": 0,
        "expl_en": 'Lion (P. leo), leopard (P. pardus), and tiger (P. tigris) share several common features and are all species of the same genus Panthera. This genus differs from another genus Felis which includes domestic cats.',
        "expl_bn": 'সিংহ, বাঘ এবং চিতাবাঘ প্রত্যেকেই Panthera নামক একই গণের অন্তর্ভুক্ত পৃথক প্রজাতি।',
    },
    {
        "id": 'BIO-LW-034',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'A genus can be characterized as:',
        "bn": 'একটি গণ (Genus)-কে কীভাবে সংজ্ঞায়িত করা যায়?',
        "opts": {
            "en": ['An aggregate of closely related species having more characters in common in comparison to species of other genera', 'An assemblage of unrelated orders showing phenotypic convergence', 'A collection of geographically isolated subspecies', 'A natural population that cannot interbreed under any circumstances'],
            "bn": ['ঘনিষ্ঠ সম্পর্কযুক্ত একাধিক প্রজাতির সমষ্টি যাদের মধ্যে অন্য গণের তুলনায় অধিক সাধারণ বৈশিষ্ট্য বিদ্যমান', 'বাহ্যিক সাদৃশ্যযুক্ত সম্পর্কহীন বর্গের সংকলন', 'ভৌগোলিকভাবে বিচ্ছিন্ন উপ-প্রজাতির সমাহার', 'একটি প্রাকৃতিক জীবগোষ্ঠী যা কখনোই অন্তর্বিজনন করতে পারে না']
        },
        "correct": 0,
        "expl_en": 'Genus comprises a group of related species which has more characters in common in comparison to species of other genera. Genera are aggregates of closely related species.',
        "expl_bn": 'গণ হলো পরস্পর নিকট সম্পর্কযুক্ত একাধিক প্রজাতির সমষ্টি, যাদের পরস্পরের মধ্যে অন্য কোনো গণের প্রজাতির তুলনায় বেশি সাদৃশ্য থাকে।',
    },
    {
        "id": 'BIO-LW-035',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'Plant genera like Solanum, Petunia, and Datura are grouped together into which common botanical family?',
        "bn": 'উদ্ভিদের Solanum, Petunia এবং Datura গণগুলিকে একসাথে কোন উদ্ভিদ গোত্রে (Family) অন্তর্ভুক্ত করা হয়েছে?',
        "opts": {
            "en": ['Solanaceae', 'Fabaceae', 'Liliaceae', 'Poaceae'],
            "bn": ['সোলানেসি (Solanaceae)', 'ফ্যাবেসি (Fabaceae)', 'লিলিয়েসি (Liliaceae)', 'পোয়েসি (Poaceae)']
        },
        "correct": 0,
        "expl_en": 'Three different genera Solanum, Petunia, and Datura are placed in the family Solanaceae based on both vegetative and floral characteristics.',
        "expl_bn": 'Solanum, Petunia এবং Datura গণ তিনটি তাদের অঙ্গজ ও জনন বৈশিষ্ট্যের সাদৃশ্যের ভিত্তিতে Solanaceae গোত্রে স্থান পেয়েছে।',
    },
    {
        "id": 'BIO-LW-036',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Taxonomic families are characterized on the basis of:',
        "bn": 'ট্যাক্সোনমিক গোত্র (Family)-সমূহ প্রধানত কোন বৈশিষ্ট্যের ভিত্তিতে নির্ধারিত ও বৈশিষ্ট্যমণ্ডিত হয়?',
        "opts": {
            "en": ['Both vegetative and reproductive features of plant species', 'Vegetative morphological features exclusively', 'Ecological geographic habitat alone', 'Anatomical secondary xylem ring count only'],
            "bn": ['উদ্ভিদ প্রজাতির অঙ্গজ (Vegetative) এবং জননগত (Reproductive) উভয় বৈশিষ্ট্যের ভিত্তিতে', 'একচেটিয়াভাবে কেবল অঙ্গসংস্থানিক অঙ্গজ বৈশিষ্ট্যের ভিত্তিতে', 'শুধুমাত্র ভৌগোলিক বাসস্থানের ভিত্তিতে', 'কেবলমাত্র গৌণ জাইলেমের বর্ষবলয়ের সংখ্যার ভিত্তিতে']
        },
        "correct": 0,
        "expl_en": "NCERT explicitly states: 'Families are characterized on the basis of both vegetative and reproductive features of plant species.'",
        "expl_bn": 'NCERT-তে পরিষ্কারভাবে বলা হয়েছে যে গোত্রগুলি উদ্ভিদ প্রজাতির অঙ্গজ ও জননগত—উভয় বৈশিষ্ট্যের ওপর ভিত্তি করে শ্রেণীবদ্ধ হয়।',
    },
    {
        "id": 'BIO-LW-037',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'Cats (genus Felis) and dogs (genus Canis) are placed into which two respective zoological families?',
        "bn": 'বিড়াল (গণ Felis) এবং কুকুর (গণ Canis) যথাক্রমে কোন দুটি প্রাণিজ গোত্রে অন্তর্ভুক্ত?',
        "opts": {
            "en": ['Felidae and Canidae', 'Canidae and Felidae', 'Muscidae and Hominidae', 'Carnivora and Primata'],
            "bn": ['ফেলিডি (Felidae) এবং ক্যানিডি (Canidae)', 'ক্যানিডি এবং ফেলিডি', 'মাসকিডি এবং হোমোনিডি', 'কার্নিভোরা এবং প্রাইমেট']
        },
        "correct": 0,
        "expl_en": 'Cats are placed in the family Felidae (along with lions and tigers in genus Panthera), while dogs are placed in the separate family Canidae.',
        "expl_bn": 'বিড়াল ফেলিডি (Felidae) গোত্রের অন্তর্ভুক্ত এবং কুকুর ক্যানিডি (Canidae) গোত্রের অন্তর্ভুক্ত।',
    },
    {
        "id": 'BIO-LW-038',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Plant families like Convolvulaceae and Solanaceae are included in the order Polymoniales mainly on the basis of:',
        "bn": 'কনভলভুলেসি (Convolvulaceae) এবং সোলানেসি (Solanaceae) গোত্র দুটি প্রধানত কোন বৈশিষ্ট্যের ভিত্তিতে পলিমোনিয়ালস (Polymoniales) বর্গে অন্তর্ভুক্ত হয়েছে?',
        "opts": {
            "en": ['Floral characters', 'Vegetative leaf venation only', 'Root nodule symbiosis', 'Seed dispersal mechanism by wind'],
            "bn": ['পুষ্পীয় বৈশিষ্ট্য (Floral characters)', 'শুধুমাত্র পাতার শিরাবিন্যাস', 'মূলের অর্বুদ মিথোজীবিতা', 'বায়ু দ্বারা বীজ বিস্তারের প্রক্রিয়া']
        },
        "correct": 0,
        "expl_en": "NCERT highlights: 'Plant families like Convolvulaceae, Solanaceae are included in the order Polymoniales mainly based on the floral characters.'",
        "expl_bn": 'NCERT অনুসারে, Convolvulaceae এবং Solanaceae গোত্র দুটিকে প্রধানত পুষ্পীয় বৈশিষ্ট্যের (Floral characters) ওপর ভিত্তি করে Polymoniales বর্গে স্থান দেওয়া হয়েছে।',
    },
    {
        "id": 'BIO-LW-039',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'The animal order Carnivora includes which of the following families?',
        "bn": 'প্রাণীদের কার্নিভোরা (Carnivora) বর্গের মধ্যে নিচের কোন গোত্রগুলি অন্তর্ভুক্ত রয়েছে?',
        "opts": {
            "en": ['Felidae and Canidae', 'Hominidae and Muscidae', 'Bovidae and Equidae', 'Cercopithecidae and Cebidae'],
            "bn": ['ফেলিডি (Felidae) এবং ক্যানিডি (Canidae)', 'হোমোনিডি এবং মাসকিডি', 'বোভিডি এবং ইকুইডি', 'সারকোপিথেসিডি এবং সেবিডি']
        },
        "correct": 0,
        "expl_en": 'The order Carnivora includes families like Felidae (cats, lions) and Canidae (dogs, foxes, wolves).',
        "expl_bn": 'মাংসাশী প্রাণীদের বর্গ Carnivora-র মধ্যে Felidae (বিড়াল জাতীয়) এবং Canidae (কুকুর জাতীয়) উভয় গোত্র অন্তর্ভুক্ত।',
    },
    {
        "id": 'BIO-LW-040',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'Class Mammalia includes diverse orders such as:',
        "bn": 'স্তন্যপায়ী শ্রেণী (Class Mammalia)-র মধ্যে কোন বিভিন্ন বর্গগুলি অন্তর্ভুক্ত?',
        "opts": {
            "en": ['Primata (monkey, gorilla, gibbon, human) and Carnivora (tiger, cat, dog)', 'Diptera and Hymenoptera', 'Poales and Sapindales', 'Anura and Urodela'],
            "bn": ['প্রাইমেট (বানর, গরিলা, মানুষ) এবং কার্নিভোরা (বাঘ, বিড়াল, কুকুর)', 'ডিপ্টেরা এবং হাইমেনপ্টেরা', 'পোয়েলস এবং স্যাপিন্ডেলস', 'অ্যানুরা এবং ইউরোডেলা']
        },
        "correct": 0,
        "expl_en": 'Class Mammalia includes order Primata comprising monkey, gorilla and gibbon along with order Carnivora that includes animals like tiger, cat and dog.',
        "expl_bn": 'ম্যামালিয়া (স্তন্যপায়ী) শ্রেণীর মধ্যে প্রাইমেটা (মানুষ, বানর ইত্যাদি) এবং কার্নিভোরা (বাঘ, কুকুর ইত্যাদি) বর্গ অন্তর্ভুক্ত।',
    },
    {
        "id": 'BIO-LW-041',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": "In plant classification, which category is used as the taxonomic equivalent of 'Phylum' in animal classification?",
        "bn": "প্রাণী শ্রেণীবিন্যাসে ব্যবহৃত 'Phylum' (পর্ব)-এর সমতুল্য হিসেবে উদ্ভিদ শ্রেণীবিন্যাসে কোন ধাপটি ব্যবহৃত হয়?",
        "opts": {
            "en": ['Division', 'Cohort', 'Class', 'Order'],
            "bn": ['বিভাগ (Division)', 'কোহর্ট (Cohort)', 'শ্রেণী (Class)', 'বর্গ (Order)']
        },
        "correct": 0,
        "expl_en": "In animal taxonomy, related classes are grouped into a 'Phylum', whereas in plant taxonomy, the equivalent category is called 'Division'.",
        "expl_bn": "প্রাণীদের ক্ষেত্রে পর্ব (Phylum) ব্যবহৃত হয়, আর উদ্ভিদের ক্ষেত্রে এর সমতুল্য বিভাগ হিসেবে 'Division' শব্দটি ব্যবহৃত হয়।",
    },
    {
        "id": 'BIO-LW-042',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'As we go up from species to kingdom in a taxonomic hierarchy, what happens to the number of common characteristics shared by organisms?',
        "bn": 'ট্যাক্সোনমিক স্তরক্রমে প্রজাতি থেকে জগতের দিকে (নিচ থেকে উপরে) ওঠার সাথে সাথে সদস্যদের মধ্যে সাধারণ বৈশিষ্ট্যের সংখ্যার কী পরিবর্তন ঘটে?',
        "opts": {
            "en": ['The number of common characteristics decreases', 'The number of common characteristics increases', 'The number of common characteristics remains constant', 'It first increases up to order and then rapidly decreases'],
            "bn": ['সাধারণ বৈশিষ্ট্যের সংখ্যা ক্রমাগত হ্রাস পায়', 'সাধারণ বৈশিষ্ট্যের সংখ্যা ক্রমাগত বৃদ্ধি পায়', 'সাধারণ বৈশিষ্ট্যের সংখ্যা সর্বদা অপরিবর্তিত থাকে', 'বর্গ পর্যন্ত বৃদ্ধি পায় এবং তারপর দ্রুত হ্রাস পায়']
        },
        "correct": 0,
        "expl_en": 'Lower the taxa, more are the characteristics that the members within the taxon share. Higher the category, greater is the difficulty of determining the relationship to other taxa at the same level because common characteristics decrease.',
        "expl_bn": 'প্রজাতি স্তরে সাদৃশ্য সবচেয়ে বেশি থাকে। স্তরক্রমের যত উপরের দিকে (জগতের দিকে) যাওয়া যায়, জীবের মধ্যে সাধারণ বৈশিষ্ট্যের সংখ্যা ততই কমতে থাকে।',
    },
    {
        "id": 'BIO-LW-043',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'What is the biological family of Housefly (Musca domestica) according to the NCERT reference table?',
        "bn": 'NCERT সারণি অনুযায়ী গৃহমাছি (Musca domestica)-র গোত্র (Family) কোনটি?',
        "opts": {
            "en": ['Muscidae', 'Diptera', 'Insecta', 'Arthropoda'],
            "bn": ['মাসকিডি (Muscidae)', 'ডিপ্টেরা (Diptera)', 'ইনসেক্টা (Insecta)', 'আর্থ্রোপোডা (Arthropoda)']
        },
        "correct": 0,
        "expl_en": 'Housefly (Musca domestica): Genus = Musca, Family = Muscidae, Order = Diptera, Class = Insecta, Phylum = Arthropoda.',
        "expl_bn": 'গৃহমাছি (Musca domestica)-র গোত্র হলো Muscidae, বর্গ হলো Diptera এবং শ্রেণী হলো Insecta।',
    },
    {
        "id": 'BIO-LW-044',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'To which taxonomic order does the housefly (Musca domestica) belong?',
        "bn": 'গৃহমাছি কোন ট্যাক্সোনমিক বর্গের (Order) অন্তর্ভুক্ত?',
        "opts": {
            "en": ['Diptera', 'Hymenoptera', 'Coleoptera', 'Lepidoptera'],
            "bn": ['ডিপ্টেরা (Diptera)', 'হাইমেনপ্টেরা', 'কোলিওপ্টেরা', 'লেপিডপ্টেরা']
        },
        "correct": 0,
        "expl_en": 'The housefly belongs to the order Diptera (two-winged insects).',
        "expl_bn": 'গৃহমাছি দুই ডানাযুক্ত পতঙ্গদের বর্গ Diptera-র অন্তর্ভুক্ত।',
    },
    {
        "id": 'BIO-LW-045',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'What is the family and order of Mango (Mangifera indica) respectively?',
        "bn": 'আম (Mangifera indica)-এর গোত্র এবং বর্গ যথাক্রমে কোনটি?',
        "opts": {
            "en": ['Anacardiaceae and Sapindales', 'Sapindaceae and Poales', 'Solanaceae and Polymoniales', 'Fabaceae and Rosales'],
            "bn": ['অ্যানাকার্ডিয়েসি এবং স্যাপিন্ডেলস', 'স্যাপিন্ডেসি এবং পোয়েলস', 'সোলানেসি এবং পলিমোনিয়ালস', 'ফ্যাবেসি এবং রোসেলস']
        },
        "correct": 0,
        "expl_en": 'Mango (Mangifera indica): Family = Anacardiaceae, Order = Sapindales, Class = Dicotyledonae, Division = Angiospermae.',
        "expl_bn": 'আমের গোত্র হলো Anacardiaceae এবং বর্গ হলো Sapindales।',
    },
    {
        "id": 'BIO-LW-046',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'What is the family and order of Wheat (Triticum aestivum) respectively?',
        "bn": 'গম (Triticum aestivum)-এর গোত্র ও বর্গ যথাক্রমে কোনটি?',
        "opts": {
            "en": ['Poaceae and Poales', 'Poaceae and Sapindales', 'Gramineae and Polymoniales', 'Liliaceae and Liliales'],
            "bn": ['পোয়েসি (Poaceae) এবং পোয়েলস (Poales)', 'পোয়েসি এবং স্যাপিন্ডেলস', 'গ্রামিনি এবং পলিমোনিয়ালস', 'লিলিয়েসি এবং লিলিয়েলস']
        },
        "correct": 0,
        "expl_en": 'Wheat (Triticum aestivum): Family = Poaceae, Order = Poales, Class = Monocotyledonae, Division = Angiospermae.',
        "expl_bn": 'গমের গোত্র হলো Poaceae এবং বর্গ হলো Poales।',
    },
    {
        "id": 'BIO-LW-047',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'To which class and order do modern human beings (Homo sapiens) belong?',
        "bn": 'আধুনিক মানুষ (Homo sapiens) কোন শ্রেণী ও বর্গের অন্তর্ভুক্ত?',
        "opts": {
            "en": ['Class Mammalia and Order Primata', 'Class Chordata and Order Hominidae', 'Class Mammalia and Order Carnivora', 'Class Vertebrata and Order Anthropoidea'],
            "bn": ['শ্রেণী ম্যামালিয়া এবং বর্গ প্রাইমেটা', 'শ্রেণী কর্ডাটা এবং বর্গ হোমোনিডি', 'শ্রেণী ম্যামালিয়া এবং বর্গ কার্নিভোরা', 'শ্রেণী ভার্টিব্রাটা এবং বর্গ অ্যানথ্রোপয়েডিয়া']
        },
        "correct": 0,
        "expl_en": 'Humans (Homo sapiens): Family = Hominidae, Order = Primata, Class = Mammalia, Phylum = Chordata.',
        "expl_bn": 'মানুষ স্তন্যপায়ী (Mammalia) শ্রেণীর অন্তর্ভুক্ত এবং প্রাইমেটা (Primata) বর্গের অন্তর্গত।',
    },
    {
        "id": 'BIO-LW-048',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": "Which of the following standardized suffixes is universally used to denote a plant 'Order' according to ICBN rules?",
        "bn": "ICBN-এর নিয়ম অনুযায়ী উদ্ভিদের 'বর্গ' (Order) নির্দেশ করতে সর্বজনীনভাবে কোন প্রত্যয়টি (Suffix) ব্যবহৃত হয়?",
        "opts": {
            "en": ['-ales (e.g., Sapindales, Poales)', '-aceae (e.g., Solanaceae)', '-phyta (e.g., Bryophyta)', '-opsida (e.g., Magnoliopsida)'],
            "bn": ['-ales (যেমন Sapindales, Poales)', '-aceae (যেমন Solanaceae)', '-phyta (যেমন Bryophyta)', '-opsida (যেমন Magnoliopsida)']
        },
        "correct": 0,
        "expl_en": 'In plant taxonomy, standard suffixes used are: Division = -phyta; Class = -opsida / -phyceae; Order = -ales; Family = -aceae.',
        "expl_bn": "উদ্ভিদের নামকরণে বর্গের (Order) নামের শেষে '-ales' প্রত্যয় যুক্ত থাকে (যেমন Poales, Sapindales, Polymoniales)।",
    },
    {
        "id": 'BIO-LW-049',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": "Which standardized suffix universally designates an animal 'Family' under ICZN rules?",
        "bn": "ICZN নিয়মাবলী অনুসারে প্রাণীদের 'গোত্র' (Family) নামের শেষে কোন প্রত্যয়টি যুক্ত থাকে?",
        "opts": {
            "en": ['-idae (e.g., Felidae, Canidae, Hominidae)', '-inae', '-oidea', '-ales'],
            "bn": ['-idae (যেমন Felidae, Canidae, Hominidae)', '-inae', '-oidea', '-ales']
        },
        "correct": 0,
        "expl_en": "In zoological nomenclature, the family suffix is always '-idae' (e.g., Felidae, Canidae, Muscidae, Hominidae). Subfamily ends in '-inae'.",
        "expl_bn": "প্রাণী নামকরণে গোত্র বা Family-র নামের শেষে সর্বদাই '-idae' প্রত্যয় যুক্ত হয়।",
    },
    {
        "id": 'BIO-LW-050',
        "exam": 'NEET, CUET, OLYMPIAD',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Select the correct sequence of obligate taxonomic categories in ascending hierarchical order (from lowest to highest):',
        "bn": 'ট্যাক্সোনমিক স্তরক্রমের সঠিক ঊর্ধ্বগামী ক্রমটি (সর্বনিম্ন থেকে সর্বোচ্চ) নির্বাচন করো:',
        "opts": {
            "en": ['Species → Genus → Family → Order → Class → Phylum/Division → Kingdom', 'Species → Genus → Order → Family → Class → Phylum → Kingdom', 'Kingdom → Phylum → Class → Order → Family → Genus → Species', 'Species → Family → Genus → Order → Phylum → Class → Kingdom'],
            "bn": ['প্রজাতি → গণ → গোত্র → বর্গ → শ্রেণী → পর্ব/বিভাগ → জগৎ', 'প্রজাতি → গণ → বর্গ → গোত্র → শ্রেণী → পর্ব → জগৎ', 'জগৎ → পর্ব → শ্রেণী → বর্গ → গোত্র → গণ → প্রজাতি', 'প্রজাতি → গোত্র → গণ → বর্গ → পর্ব → শ্রেণী → জগৎ']
        },
        "correct": 0,
        "expl_en": 'The ascending obligate taxonomic hierarchy is: Species → Genus → Family → Order → Class → Phylum/Division → Kingdom.',
        "expl_bn": 'সঠিক ঊর্ধ্বগামী স্তরক্রমটি হলো: প্রজাতি (Species) → গণ (Genus) → গোত্র (Family) → বর্গ (Order) → শ্রেণী (Class) → পর্ব/বিভাগ (Phylum/Division) → জগৎ (Kingdom)।',
    },
    {
        "id": 'BIO-LW-051',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'A Herbarium is best defined as a:',
        "bn": 'হার্বেরিয়াম (Herbarium)-এর সবচেয়ে নিখুঁত সংজ্ঞা কোনটি?',
        "opts": {
            "en": ['Storehouse of collected plant specimens that are dried, pressed, and preserved on sheets', 'Garden where living rare medicinal plants are grown under greenhouse conditions', 'Collection of preserved animal skeletons and stuffed migratory birds', 'Library containing original handwritten taxonomic manuscripts of ancient botanists'],
            "bn": ['সংগৃহীত উদ্ভিদ নমুনার ভাণ্ডার যা শুকিয়ে, চেপে কাগজের শিটে সংরক্ষণ করা হয়', 'এমন উদ্যান যেখানে গ্রিনহাউসে বিরল ভেষজ জীবন্ত উদ্ভিদ চাষ করা হয়', 'সংরক্ষিত প্রাণীর কঙ্কাল ও স্টাফ করা পরিযায়ী পাখির সংগ্রহশালা', 'প্রাচীন উদ্ভিদবিজ্ঞানীদের মূল হস্তলিখিত বই সম্বলিত গ্রন্থাগার']
        },
        "correct": 0,
        "expl_en": 'Herbarium is a store house of collected plant specimens that are dried, pressed and preserved on sheets. Subsequently, these sheets are arranged according to a universally accepted system of classification.',
        "expl_bn": 'হার্বেরিয়াম হলো সংগৃহীত উদ্ভিদ নমুনার এমন এক সংরক্ষণাগার যেখানে নমুনাগুলিকে শুকিয়ে, চাপে রেখে বিশেষ কাগজের শিটে সর্বজনীন শ্রেণীবিন্যাস নীতি মেনে সাজিয়ে রাখা হয়।',
    },
    {
        "id": 'BIO-LW-052',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'What are the standard international dimensions of an official herbarium sheet?',
        "bn": 'একটি আদর্শ আন্তর্জাতিক হার্বেরিয়াম শিটের পরিমাপ কত?',
        "opts": {
            "en": ['41 cm × 29 cm (approx. 16.5 × 11.5 inches)', '30 cm × 20 cm (approx. 12 × 8 inches)', '50 cm × 35 cm (approx. 20 × 14 inches)', '25 cm × 18 cm (approx. 10 × 7 inches)'],
            "bn": ['৪১ সেমি × ২৯ সেমি (প্রায় ১৬.৫ × ১১.৫ ইঞ্চি)', '৩০ সেমি × ২০ সেমি (প্রায় ১২ × ৮ ইঞ্চি)', '৫০ সেমি × ৩৫ সেমি (প্রায় ২০ × ১৪ ইঞ্চি)', '২৫ সেমি × ১৮ সেমি (প্রায় ১০ × ৭ ইঞ্চি)']
        },
        "correct": 0,
        "expl_en": 'Standard international herbarium sheets measure 41 cm × 29 cm (or 16.5 × 11.5 inches).',
        "expl_bn": 'আন্তর্জাতিকভাবে স্বীকৃত প্রমাণ হার্বেরিয়াম শিটের আকার হলো ৪১ সেমি × ২৯ সেমি (বা ১৬.৫ × ১১.৫ ইঞ্চি)।',
    },
    {
        "id": 'BIO-LW-053',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": "Which chemical solution is standardly used for 'poisoning' herbarium specimens to protect them from fungal and insect attack?",
        "bn": 'ছত্রাক ও পোকামাকড়ের আক্রমণ থেকে রক্ষা করতে হার্বেরিয়াম নমুনা বিষাক্তকরণে (Poisoning) কোন রাসায়নিক দ্রবণটি ব্যবহৃত হয়?',
        "opts": {
            "en": ['0.1% Mercuric chloride (HgCl2) solution', '70% Formaldehyde solution', '10% Sodium hypochlorite solution', '5% Copper sulphate solution'],
            "bn": ['০.১% মারকিউরিক ক্লোরাইড (HgCl2) দ্রবণ', '৭০% ফর্মালডিহাইড দ্রবণ', '১০% সোডিয়াম হাইপোক্লোরাইট দ্রবণ', '৫% কপার সালফেট দ্রবণ']
        },
        "correct": 0,
        "expl_en": 'Dried plant specimens are standardly poisoned with 0.1% solution of mercuric chloride (HgCl2) to prevent fungal and insect attacks, followed by drying and mounting.',
        "expl_bn": 'হার্বেরিয়াম শিটে মাউন্ট করার আগে ছত্রাক ও পোকার সংক্রমণ রোধ করতে ০.১% মারকিউরিক ক্লোরাইড (HgCl2) দ্রবণ দ্বারা বিষাক্তকরণ করা হয়।',
    },
    {
        "id": 'BIO-LW-054',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'The label pasted at the lower right corner of a herbarium sheet does NOT carry information on which of the following parameters?',
        "bn": 'হার্বেরিয়াম শিটের নিচের ডানদিকের লেবেলে নিচের কোন তথ্যটি উল্লিখিত থাকে না?',
        "opts": {
            "en": ['Height of the whole plant in nature', 'Date and place of collection', 'English, local, and botanical names', "Family and collector's name"],
            "bn": ['প্রকৃতিতে সম্পূর্ণ উদ্ভিদটির মোট উচ্চতা (Height of plant)', 'সংগ্রহের তারিখ এবং স্থান', 'ইংরেজি, স্থানীয় এবং উদ্ভিদবৈজ্ঞানিক নাম', 'গোত্রের নাম এবং সংগ্রহকারীর নাম']
        },
        "correct": 0,
        "expl_en": "NCERT explicitly lists: The herbarium sheets carry a label providing information about date and place of collection, English, local and botanical names, family, collector's name, etc. It does NOT carry the height or weight of the plant.",
        "expl_bn": 'হার্বেরিয়াম শিটের লেবেলে সংগ্রহের তারিখ, স্থান, নাম (ইংরেজি, স্থানীয়, বৈজ্ঞানিক), গোত্র এবং সংগ্রাহকের নাম থাকে; কিন্তু উদ্ভিদের উচ্চতা কখনোই থাকে না।',
    },
    {
        "id": 'BIO-LW-055',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": "Which taxonomic aid serves as a 'quick referral system' in taxonomical studies?",
        "bn": "ট্যাক্সোনমিক গবেষণায় কোনটি 'দ্রুত রেফারেন্স ব্যবস্থা' (Quick referral system) হিসেবে কাজ করে?",
        "opts": {
            "en": ['Herbarium', 'Botanical garden', 'Museum', 'Zoological park'],
            "bn": ['হার্বেরিয়াম (Herbarium)', 'বোটানিক্যাল গার্ডেন', 'মিউজিয়াম', 'চিড়িয়াখানা']
        },
        "correct": 0,
        "expl_en": "NCERT explicitly mentions: 'Herbaria also serve as quick referral systems in taxonomical studies.'",
        "expl_bn": 'NCERT অনুযায়ী ট্যাক্সোনমিক গবেষণার ক্ষেত্রে হার্বেরিয়াম একটি অতি দ্রুত রেফারেন্স ব্যবস্থা (Quick referral system) হিসেবে কাজ করে।',
    },
    {
        "id": 'BIO-LW-056',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'Botanical gardens differ fundamentally from herbaria in having:',
        "bn": 'বোটানিক্যাল গার্ডেন হার্বেরিয়ামের চেয়ে মূলত কোন বিষয়ে সম্পূর্ণ পৃথক?',
        "opts": {
            "en": ['Collections of living plants grown for identification and reference', 'Pressed and dried herbarium specimens preserved on paper', 'Exclusively aquatic microalgae culture ponds', 'Stuffed animals in glass enclosures'],
            "bn": ['শনাক্তকরণ ও গবেষণার উদ্দেশ্যে সংরক্ষিত জীবন্ত উদ্ভিদের সংগ্রহ', 'কাগজের শিটে শুকনো ও চাপযুক্ত উদ্ভিদের নমুনা', 'শুধুমাত্র জলজ ক্ষুদ্র শৈবাল চাষের জলাশয়', 'কাঁচের ঘরে সংরক্ষিত স্টাফ করা প্রাণী']
        },
        "correct": 0,
        "expl_en": 'Botanical gardens have collections of living plants for reference and identification. Plant species in these gardens are grown for identification purposes and each plant is labeled with its botanical/scientific name and family.',
        "expl_bn": 'বোটানিক্যাল গার্ডেনে জীবন্ত উদ্ভিদের সংগ্রহ থাকে যা পরিচিতি ও গবেষণার জন্য রোপণ করা হয় এবং প্রতিটি গাছে তার বৈজ্ঞানিক নাম ও গোত্রের ফলক লাগানো থাকে।',
    },
    {
        "id": 'BIO-LW-057',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'Where is the famous Royal Botanic Garden located?',
        "bn": 'বিখ্যাত রয়্যাল বোটানিক গার্ডেন (Royal Botanic Garden) কোথায় অবস্থিত?',
        "opts": {
            "en": ['Kew, England', 'Howrah, India', 'Lucknow, India', 'Paris, France'],
            "bn": ['কিউ (Kew), ইংল্যান্ড', 'হাওড়া, ভারত', 'লখনউ, ভারত', 'প্যারিস, ফ্রান্স']
        },
        "correct": 0,
        "expl_en": 'The famous botanical gardens are at Kew (England), Indian Botanical Garden (Howrah/Kolkata, India), and National Botanical Research Institute (Lucknow, India).',
        "expl_bn": 'বিশ্বখ্যাত রয়্যাল বোটানিক গার্ডেন ইংল্যান্ডের কিউ (Kew)-তে অবস্থিত।',
    },
    {
        "id": 'BIO-LW-058',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'The largest botanical garden in India, famous for its centuries-old Great Banyan Tree (Ficus benghalensis), is located at:',
        "bn": 'ভারতের বৃহত্তম বোটানিক্যাল গার্ডেন, যা তার শতাব্দী প্রাচীন সুবিশাল বটবৃক্ষের (Ficus benghalensis) জন্য বিখ্যাত, কোথায় অবস্থিত?',
        "opts": {
            "en": ['Acharya Jagadish Chandra Bose Indian Botanic Garden, Shibpur, Howrah', 'National Botanical Research Institute (NBRI), Lucknow', 'Lalbagh Botanical Garden, Bengaluru', 'Lloyd Botanical Garden, Darjeeling'],
            "bn": ['আচার্য জগদীশচন্দ্র বসু ভারতীয় বোটানিক গার্ডেন, শিবপুর, হাওড়া', 'ন্যাশনাল বোটানিক্যাল রিসার্চ ইনস্টিটিউট (NBRI), লখনউ', 'লালবাগ বোটানিক্যাল গার্ডেন, বেঙ্গালুরু', 'লয়েড বোটানিক্যাল গার্ডেন, দার্জিলিং']
        },
        "correct": 0,
        "expl_en": 'The Indian Botanical Garden is located at Shibpur, Howrah (near Kolkata, West Bengal), housing the Great Banyan Tree over 250 years old.',
        "expl_bn": 'ভারতের বিখ্যাত ভারতীয় বোটানিক গার্ডেন পশ্চিমবঙ্গের হাওড়ার শিবপুরে অবস্থিত, যা ২৫০ বছরেরও প্রাচীন সুবিশাল গ্রেট ব্যানিয়ান ট্রির জন্য বিশ্বখ্যাত।',
    },
    {
        "id": 'BIO-LW-059',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'The National Botanical Research Institute (NBRI) is situated in which Indian city?',
        "bn": 'ন্যাশনাল বোটানিক্যাল রিসার্চ ইনস্টিটিউট (NBRI) ভারতের কোন শহরে অবস্থিত?',
        "opts": {
            "en": ['Lucknow', 'Howrah', 'Dehradun', 'New Delhi'],
            "bn": ['লখনউ (Lucknow)', 'হাওড়া', 'দেরাদুন', 'নয়াদিল্লি']
        },
        "correct": 0,
        "expl_en": 'National Botanical Research Institute (NBRI) is located at Lucknow, Uttar Pradesh, India.',
        "expl_bn": 'ন্যাশনাল বোটানিক্যাল রিসার্চ ইনস্টিটিউট (NBRI) উত্তরপ্রদেশের লখনউ শহরে অবস্থিত।',
    },
    {
        "id": 'BIO-LW-060',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Biological museums set up in educational institutes generally preserve specimens in containers or jars in:',
        "bn": 'শিক্ষা প্রতিষ্ঠানে স্থাপিত বায়োলজিক্যাল মিউজিয়ামে নমুনাগুলিকে সাধারণত জারের মধ্যে কোন মাধ্যমে সংরক্ষণ করা হয়?',
        "opts": {
            "en": ['Preservative solutions like formalin (aqueous formaldehyde)', 'Pure concentrated hydrochloric acid', 'Absolute liquid nitrogen at -196 °C', 'Dry vacuum chambers without liquid'],
            "bn": ['ফর্মালিনের (জলীয় ফর্মালডিহাইড) মতো সংরক্ষক দ্রবণে', 'বিশুদ্ধ গাঢ় হাইড্রোক্লোরিক অ্যাসিডে', '-১৯৬ °C তাপমাত্রায় তরল নাইট্রোজেনে', 'তরলবিহীন শুষ্ক নির্বাত প্রকোষ্ঠে']
        },
        "correct": 0,
        "expl_en": 'Biological specimens are preserved in containers or jars in preservative solutions (commonly formalin, a 37-40% aqueous solution of formaldehyde).',
        "expl_bn": 'জৈবিক নমুনাগুলিকে কাঁচের পাত্রে বা জারে সংরক্ষক তরল হিসেবে ফর্মালিন দ্রবণে ডুবিয়ে দীর্ঘকাল সংরক্ষণ করা হয়।',
    },
    {
        "id": 'BIO-LW-061',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'In a biological museum, insects are preserved standardly by:',
        "bn": 'বায়োলজিক্যাল মিউজিয়ামে কীটপতঙ্গগুলিকে আদর্শ পদ্ধতিতে কীভাবে সংরক্ষণ করা হয়?',
        "opts": {
            "en": ['Collecting, killing, and pinning inside insect boxes', 'Stretching and freezing in liquid helium', 'Dissolving exoskeleton in potassium hydroxide', 'Embedding inside boiling paraffin wax'],
            "bn": ['সংগ্রহ করা, মেরে ফেলা এবং ইনসেক্ট বক্সে পিন দিয়ে গেঁথে রাখা (Collecting, killing, pinning)', 'তরল হিলিয়ামে হিমায়িত করা', 'পটাশিয়াম হাইড্রোক্সাইডে কাইটিনের খোলক দ্রবীভূত করা', 'ফুটন্ত প্যারাফিন মোমে ডুবিয়ে রাখা']
        },
        "correct": 0,
        "expl_en": "NCERT notes: 'Insects are preserved in insect boxes after collecting, killing and pinning.'",
        "expl_bn": 'NCERT অনুসারে কীটপতঙ্গগুলিকে প্রথমে সংগ্রহ করে, মেরে ফেলে এবং তারপর ইনসেক্ট বক্সে পিনের সাহায্যে গেঁথে সংরক্ষণ করা হয়।',
    },
    {
        "id": 'BIO-LW-062',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'Larger animals like birds and mammals are standardly preserved in biological museums through:',
        "bn": 'পাখি ও স্তন্যপায়ীর মতো অপেক্ষাকৃত বৃহৎ প্রাণীদের মিউজিয়ামে সংরক্ষণের প্রচলিত পদ্ধতি কোনটি?',
        "opts": {
            "en": ['Stuffing and preservation (Taxidermy)', 'Freezing in salt brine', 'Boiling in organic solvents', 'Mummification using bitumen'],
            "bn": ['স্টাফিং এবং ত্বক সংরক্ষণ (Taxidermy)', 'লবণাক্ত জলে হিমায়িতকরণ', 'জৈব দ্রাবকে ফুটিয়ে নেওয়া', 'আলকাতরা দিয়ে মমি তৈরি']
        },
        "correct": 0,
        "expl_en": 'Larger animals like birds and mammals are usually stuffed and preserved. Museums often also have collections of skeletons of animals.',
        "expl_bn": 'পাখি ও স্তন্যপায়ীদের অভ্যন্তরীণ অঙ্গ ফেলে দিয়ে উপযুক্ত তুলো বা খড় ভরে স্টাফিং (Taxidermy) করে অবিকল চেহারায় সংরক্ষণ করা হয়।',
    },
    {
        "id": 'BIO-LW-063',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'Zoological parks (zoos) are places where wild animals are kept in protected environments under human care, mainly enabling us to:',
        "bn": 'চিড়িয়াখানায় বন্য প্রাণীদের মানুষের তত্ত্বাবধানে সুরক্ষিত পরিবেশে রাখা হয়, যার প্রধান উদ্দেশ্য হলো:',
        "opts": {
            "en": ['Learn about their food habits, reproductive behavior, and ex-situ conservation', 'Domesticate them for commercial meat production', 'Perform selective genetic crossbreeding for circuses', 'Harvest organs for medical pharmaceutical research'],
            "bn": ['তাদের খাদ্যভ্যাস, আচরণ শেখা এবং এক্স-সিটু সংরক্ষণ নিশ্চিত করা', 'বাণিজ্যিক মাংস উৎপাদনের জন্য বন্য প্রাণীকে পোষ মানানো', 'সার্কাসের জন্য কৃত্রিম প্রজনন ঘটানো', 'চিকিৎসা গবেষণার জন্য অঙ্গ সংগ্রহ করা']
        },
        "correct": 0,
        "expl_en": "Zoological parks enable us to learn about animals' food habits and behavior. All animals in a zoo are provided conditions similar to their natural habitats as far as possible.",
        "expl_bn": 'চিড়িয়াখানায় বন্য প্রাণীদের প্রাকৃতিক পরিবেশের অনুরূপ সুরক্ষা প্রদান করে তাদের খাদ্যাভ্যাস ও স্বভাব পর্যবেক্ষণ এবং প্রজাতি সংরক্ষণ করা হয়।',
    },
    {
        "id": 'BIO-LW-064',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": "A taxonomic 'Key' is an essential tool used for identification of plants and animals based on:",
        "bn": "ট্যাক্সোনমিক 'কি' (Key) হলো উদ্ভিদ ও প্রাণী সনাক্তকরণের এক গুরুত্বপূর্ণ মাধ্যম যা গঠিত হয় কিসের ভিত্তিতে?",
        "opts": {
            "en": ['Similarities and dissimilarities using contrasting characters generally in a pair called couplet', 'The chronological geological epoch of fossil discovery', 'The biochemical nucleotide sequence of ribosomal 16S RNA', 'The commercial monetary market value of the timber'],
            "bn": ['বৈসাদৃশ্যমূলক জোড় বৈশিষ্ট্যের (Couplet) ওপর ভিত্তি করে সাদৃশ্য ও বৈসাদৃশ্য বিচার করে', 'জীবাশ্ম আবিষ্কারের ভূতাত্ত্বিক সময়কাল অনুযায়ী', 'রাইবোজোমাল 16S RNA-র নিউক্লিওটাইড সজ্জাক্রমের ভিত্তিতে', 'কাঠের বাণিজ্যিক আর্থিক মূল্যের ভিত্তিতে']
        },
        "correct": 0,
        "expl_en": 'Key is a taxonomical aid used for identification of plants and animals based on similarities and dissimilarities. The keys are based on contrasting characters generally in a pair called couplet.',
        "expl_bn": "ট্যাক্সোনমিক 'কি' হলো বিপরীতধর্মী জোড় বৈশিষ্ট্যের (যাকে কাপলেট বা Couplet বলে) ভিত্তিতে সাদৃশ্য ও পার্থক্যের দ্বারা জীবকে সনাক্ত করার এক বৈজ্ঞানিক মাধ্যম।",
    },
    {
        "id": 'BIO-LW-065',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Each statement present within a taxonomic key is called a:',
        "bn": "একটি ট্যাক্সোনমিক 'কি' (Key)-এর প্রতিটি একক বিবৃতি বা বাক্যকে কী বলা হয়?",
        "opts": {
            "en": ['Lead', 'Couplet', 'Taxon', 'Monograph'],
            "bn": ['লিড (Lead)', 'কাপলেট (Couplet)', 'ট্যাক্সন (Taxon)', 'মনোগ্রাফ (Monograph)']
        },
        "correct": 0,
        "expl_en": 'Each statement in the key is called a lead. A pair of contrasting statements is called a couplet.',
        "expl_bn": "ট্যাক্সোনমিক কি-এর অন্তর্ভুক্ত প্রতিটি পৃথক বাক্য বা বিবৃতিকে 'লিড' (Lead) বলা হয়, এবং দুটি বিপরীত বিবৃতি মিলে তৈরি হয় কাপলেট (Couplet)।",
    },
    {
        "id": 'BIO-LW-066',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Which statement correctly describes the analytical nature of taxonomic keys?',
        "bn": 'ট্যাক্সোনমিক কি-এর বিশ্লেষণাত্মক প্রকৃতি (Analytical nature) সম্পর্কে কোনটি সঠিক?',
        "opts": {
            "en": ['Separate taxonomic keys are required for each taxonomic category such as family, genus, and species', 'A single universal key can identify all organisms across all five kingdoms simultaneously', 'Keys are purely synthetic and do not require contrasting choices', 'Keys are applicable exclusively to extinct vertebrate fossils'],
            "bn": ['গোত্র, গণ এবং প্রজাতির মতো প্রতিটি ট্যাক্সোনমিক ক্যাটাগরির জন্য পৃথক পৃথক কি প্রয়োজন হয়', 'একটিমাত্র সার্বজনীন কি দিয়ে সমস্ত জগতের প্রাণীকে একসাথে সনাক্ত করা সম্ভব', 'কি সম্পূর্ণ কৃত্রিম এবং এতে কোনো বিপরীত বিকল্প বেছে নিতে হয় না', 'কি কেবলমাত্র বিলুপ্ত মেরুদণ্ডী জীবাশ্মের জন্য প্রযোজ্য']
        },
        "correct": 0,
        "expl_en": 'Keys are generally analytical in nature. Separate taxonomic keys are required for each taxonomic category such as family, genus and species for identification purposes.',
        "expl_bn": 'কি বিশ্লেষণধর্মী হয় এবং প্রতিটি ট্যাক্সোনমিক ধাপ (যেমন গোত্র, গণ, প্রজাতি)-এর জন্য সম্পূর্ণ পৃথক পৃথক কি ব্যবহার করতে হয়।',
    },
    {
        "id": 'BIO-LW-067',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Which publication contains the actual account of habitat and distribution of plants of a given geographic area?',
        "bn": 'কোন প্রকাশনায় একটি নির্দিষ্ট ভৌগোলিক অঞ্চলের উদ্ভিদের প্রকৃত বাসস্থান ও বিস্তারের পূর্ণ বিবরণ পাওয়া যায়?',
        "opts": {
            "en": ['Flora', 'Manual', 'Monograph', 'Catalogue'],
            "bn": ['ফ্লোরা (Flora)', 'ম্যানুয়াল (Manual)', 'মনোগ্রাফ (Monograph)', 'ক্যাটালগ (Catalogue)']
        },
        "correct": 0,
        "expl_en": 'Flora contains the actual account of habitat and distribution of plants of a given area. These provide the index to the plant species found in a particular area.',
        "expl_bn": 'ফ্লোরা (Flora)-তে কোনো নির্দিষ্ট ভৌগোলিক অঞ্চলের উদ্ভিদের বাসস্থান, বিস্তার এবং প্রজাতির নির্ঘণ্ট সন্নিবিষ্ট থাকে।',
    },
    {
        "id": 'BIO-LW-068',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Taxonomic aids that are useful in providing information for identification of names of species found in an area are termed:',
        "bn": 'কোনো নির্দিষ্ট অঞ্চলে প্রাপ্ত প্রজাতিসমূহের নাম সনাক্তকরণের প্রয়োজনীয় তথ্য যে ট্যাক্সোনমিক মাধ্যমে পাওয়া যায়, তাকে বলে:',
        "opts": {
            "en": ['Manuals', 'Monographs', 'Floras', 'Herbarium labels'],
            "bn": ['ম্যানুয়াল (Manuals)', 'মনোগ্রাফ (Monographs)', 'ফ্লোরা', 'হার্বেরিয়াম লেবেল']
        },
        "correct": 0,
        "expl_en": 'Manuals are useful in providing information for identification of names of species found in an area. Monographs contain information on any one taxon.',
        "expl_bn": 'ম্যানুয়াল (Manuals) কোনো এলাকায় উপস্থিত প্রজাতির নাম সনাক্ত করার জন্য ব্যবহারিক তথ্য সরবরাহ করে।',
    },
    {
        "id": 'BIO-LW-069',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'A taxonomic treatise containing comprehensive information on any ONE taxon is called a:',
        "bn": 'কেবলমাত্র যেকোনো একটি নির্দিষ্ট ট্যাক্সন (One taxon)-এর বিস্তারিত তথ্য সম্বলিত গ্রন্থকে কী বলা হয়?',
        "opts": {
            "en": ['Monograph', 'Manual', 'Flora', 'Catalogue'],
            "bn": ['মনোগ্রাফ (Monograph)', 'ম্যানুয়াল', 'ফ্লোরা', 'ক্যাটালগ']
        },
        "correct": 0,
        "expl_en": "NCERT explicitly defines: 'Monographs contain information on any one taxon.'",
        "expl_bn": 'যেকোনো একটিমাত্র ট্যাক্সন (যেমন একটি নির্দিষ্ট গোত্র বা গণ)-এর পূর্ণাঙ্গ তথ্য সম্বলিত বিবরণীকে মনোগ্রাফ (Monograph) বলে।',
    },
    {
        "id": 'BIO-LW-070',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'An alphabetical arrangement or systematic list of species available in a library or museum collection is termed a:',
        "bn": 'কোনো সংগ্রহশালা বা অঞ্চলে প্রাপ্ত প্রজাতিগুলির বর্ণানুক্রমিক বা নিয়মানুগ তালিকাকে কী বলা হয়?',
        "opts": {
            "en": ['Catalogue', 'Monograph', 'Manual', 'Lead'],
            "bn": ['ক্যাটালগ (Catalogue)', 'মনোগ্রাফ', 'ম্যানুয়াল', 'লিড']
        },
        "correct": 0,
        "expl_en": 'A Catalogue is an alphabetical register or list of organisms or taxonomic books found in an area or institution, providing concise metadata.',
        "expl_bn": 'ক্যাটালগ হলো কোনো অঞ্চল বা প্রতিষ্ঠানের অন্তর্ভুক্ত প্রজাতি বা বইসমূহের সংক্ষিপ্ত বর্ণানুক্রমিক তালিকা।',
    },
    {
        "id": 'BIO-LW-071',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Statement I: Increase in body mass is considered as growth.\nStatement II: In living organisms, growth comes from outside while in non-living objects, growth comes from inside.\nChoose the correct option:',
        "bn": 'বিবৃতি I: দৈহিক ভর বৃদ্ধিকে বৃদ্ধির একটি লক্ষণ হিসেবে গণ্য করা হয়।\nবিবৃতি II: জীবদেহে বৃদ্ধি বাইরে থেকে ঘটে, যেখানে নির্জীব বস্তুর ক্ষেত্রে বৃদ্ধি ভেতর থেকে ঘটে।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct', 'Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect'],
            "bn": ['বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল']
        },
        "correct": 0,
        "expl_en": 'Statement I is correct (increase in mass is growth). Statement II is incorrect because in living organisms, growth is intrinsic (from inside), whereas in non-living objects like sand dunes, growth is extrinsic (from outside).',
        "expl_bn": 'বিবৃতি I সঠিক। কিন্তু বিবৃতি II ভুল, কারণ সজীব বস্তুর বৃদ্ধি ভেতর থেকে (intrinsic) ঘটে এবং নির্জীব বস্তুর বৃদ্ধি বাইরে থেকে পদার্থ জমার মাধ্যমে ঘটে।',
    },
    {
        "id": 'BIO-LW-072',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Statement I: Non-living objects do not exhibit metabolism.\nStatement II: Isolated metabolic reactions performed in vitro are considered living things.\nChoose the correct option:',
        "bn": 'বিবৃতি I: নির্জীব বস্তু কখনোই কোনো বিপাক ক্রিয়া প্রদর্শন করে না।\nবিবৃতি II: টেস্ট টিউবে কোষহীন অবস্থায় সংঘটিত বিচ্ছিন্ন বিপাকীয় বিক্রিয়াগুলি এক একটি পূর্ণাঙ্গ জীব।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct', 'Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect'],
            "bn": ['বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল']
        },
        "correct": 0,
        "expl_en": 'Statement I is correct (no non-living object exhibits metabolism). Statement II is incorrect because isolated reactions in vitro are living reactions, but NOT living things.',
        "expl_bn": "বিবৃতি I সঠিক কারণ কোনো জড় বস্তুর বিপাক থাকে না। বিবৃতি II ভুল কারণ টেস্ট টিউবের বিক্রিয়াগুলি 'সজীব বিক্রিয়া', কিন্তু কোনো জীবন্ত সত্তা নয়।",
    },
    {
        "id": 'BIO-LW-073',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Statement I: Lower the taxon in hierarchy, fewer are the characteristics that the members share.\nStatement II: Order is an assemblage of related families resembling each other in a few characters.\nChoose the correct option:',
        "bn": 'বিবৃতি I: স্তরক্রমের যত নিচের স্তরে যাওয়া যায়, সদস্যদের সাধারণ বৈশিষ্ট্যের সংখ্যা ততই কমে যায়।\nবিবৃতি II: বর্গ হলো কয়েকটি সম্পর্কিত গোত্রের সমষ্টি যাদের মধ্যে অল্প কিছু সাধারণ সাদৃশ্য থাকে।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Statement I is incorrect but Statement II is correct', 'Statement I is correct but Statement II is incorrect', 'Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect'],
            "bn": ['বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল']
        },
        "correct": 0,
        "expl_en": 'Statement I is incorrect because lower the taxon, MORE are the characteristics that members share. Statement II is correct as order is indeed an assemblage of families resembling one another in fewer characters compared to genus.',
        "expl_bn": 'বিবৃতি I ভুল, কারণ নিচের স্তরের ট্যাক্সনে (যেমন প্রজাতি) সাধারণ বৈশিষ্ট্যের সংখ্যা সবচেয়ে বেশি হয়। বিবৃতি II সঠিক।',
    },
    {
        "id": 'BIO-LW-074',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Binomial nomenclature given by Carolus Linnaeus is being practiced by biologists all over the world.\nReason (R): Each scientific name has two components—the Generic name and the specific epithet—which prevents ambiguity.\nChoose the correct option:',
        "bn": 'Assertion (A): ক্যারোলাস লিনিয়াস কর্তৃক প্রবর্তিত দ্বিপদ নামকরণ আজ বিশ্বজুড়ে সমস্ত জীববিজ্ঞানীদের দ্বারা অনুসৃত হয়।\nReason (R): প্রতিটি বৈজ্ঞানিক নামের দুটি অংশ থাকে—গণ ও প্রজাতি, যা যেকোনো ধরণের বিভ্রান্তি দূর করে।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Both (A) and (R) are true and (R) is the correct explanation of (A)', 'Both (A) and (R) are true but (R) is NOT the correct explanation of (A)', '(A) is true but (R) is false', '(A) is false but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য কিন্তু (R) মিথ্যা', '(A) মিথ্যা কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": "Both (A) and (R) are true. Linnaeus's binomial naming system is globally accepted precisely because its two-component structure standardizes names universally across different languages.",
        "expl_bn": '(A) ও (R) উভয়ই সত্য এবং দ্বিপদ নামকরণের গণ ও প্রজাতির সমন্বিত কাঠামো নামকরণের বৈশ্বিক স্পষ্টতা আনে বলেই এটি বিশ্বব্যাপী গৃহীত।',
    },
    {
        "id": 'BIO-LW-075',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Reproduction cannot be taken as an all-inclusive defining characteristic of living organisms.\nReason (R): Non-living objects can replicate and reproduce under certain optimal atmospheric conditions.\nChoose the correct option:',
        "bn": 'Assertion (A): প্রজননকে সজীব বস্তুর কোনো সর্বজনীন সংজ্ঞাবহ বৈশিষ্ট্য বলা যায় না।\nReason (R): নির্জীব বস্তুও নির্দিষ্ট অনুকূল বায়ুমণ্ডলীয় পরিস্থিতিতে বংশবৃদ্ধি ও প্রতিলিপিকরণ করতে পারে।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['(A) is true but (R) is false', 'Both (A) and (R) are true and (R) is the correct explanation of (A)', 'Both (A) and (R) are true but (R) is NOT the correct explanation of (A)', '(A) is false but (R) is true'],
            "bn": ['(A) সত্য কিন্তু (R) মিথ্যা', '(A) এবং (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) মিথ্যা কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Assertion (A) is true because sterile organisms (worker bees, mules) are living but do not reproduce. Reason (R) is completely false because no non-living object is capable of reproducing or replicating by itself.',
        "expl_bn": '(A) সত্য কারণ বন্ধ্যা জীব প্রজনন করতে না পারলেও জীবিত। কিন্তু (R) সম্পূর্ণ মিথ্যা কারণ কোনো জড় বস্তু কখনোই বংশবৃদ্ধি করতে পারে না।',
    },
    {
        "id": 'BIO-LW-076',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Consciousness is a defining property of living organisms.\nReason (R): Human beings are the only organisms who are aware of themselves (have self-consciousness).\nChoose the correct option:',
        "bn": 'Assertion (A): চেতনা (Consciousness) হলো সজীব সত্তার একটি অনন্য সংজ্ঞাবহ বৈশিষ্ট্য।\nReason (R): মানুষ একমাত্র জীব যে নিজের সম্পর্কে সচেতন (যার আত্ম-সচেতনতা রয়েছে)।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Both (A) and (R) are true but (R) is NOT the correct explanation of (A)', 'Both (A) and (R) are true and (R) is the correct explanation of (A)', '(A) is true but (R) is false', '(A) is false but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) এবং (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) সত্য কিন্তু (R) মিথ্যা', '(A) মিথ্যা কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Both statements are true facts from NCERT. Consciousness is defining because ALL organisms respond to environmental stimuli. Human self-consciousness is an additional unique human trait, but does not explain why general consciousness is a defining feature of all life.',
        "expl_bn": '(A) ও (R) দুটি তথ্যই সম্পূর্ণ সত্য। চেতনা সমস্ত জীবের সংজ্ঞাবহ বৈশিষ্ট্য কারণ সকল জীব উদ্দীপনায় সাড়া দেয়; মানুষের আত্ম-সচেতনতা এর জন্য কোনো ব্যাখ্যামূলক কারণ নয়।',
    },
    {
        "id": 'BIO-LW-077',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Botanical gardens and herbaria are taxonomic aids.\nReason (R): Herbaria preserve living plant specimens while botanical gardens preserve dried and pressed specimens on paper sheets.\nChoose the correct option:',
        "bn": 'Assertion (A): বোটানিক্যাল গার্ডেন এবং হার্বেরিয়াম উভয়ই গুরুত্বপূর্ণ ট্যাক্সোনমিক সহায়ক মাধ্যম।\nReason (R): হার্বেরিয়ামে জীবন্ত উদ্ভিদ সংরক্ষিত থাকে এবং বোটানিক্যাল গার্ডেনে কাগজের শিটে শুকনো ও চাপা উদ্ভিদ সংরক্ষিত থাকে।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['(A) is true but (R) is false', 'Both (A) and (R) are true and (R) is the correct explanation of (A)', 'Both (A) and (R) are true but (R) is NOT the correct explanation of (A)', '(A) is false but (R) is true'],
            "bn": ['(A) সত্য কিন্তু (R) মিথ্যা', '(A) এবং (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) মিথ্যা কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Assertion (A) is true. Reason (R) is completely false because the roles are reversed: botanical gardens cultivate LIVING plants, whereas herbaria preserve DRIED, pressed plant specimens on sheets.',
        "expl_bn": '(A) সত্য। কিন্তু (R) সম্পূর্ণ মিথ্যা কারণ বোটানিক্যাল গার্ডেনে জীবন্ত উদ্ভিদ এবং হার্বেরিয়ামে শুকনো চাপা নমুনা সংরক্ষিত থাকে।',
    },
    {
        "id": 'BIO-LW-078',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Cellular organization of the body is the defining feature of life forms.\nReason (R): Molecular constituents of a cell independently carry out biological life in the absence of a cellular boundary.\nChoose the correct option:',
        "bn": 'Assertion (A): দেহের কোষীয় সংগঠন হলো সজীবতার একটি মৌলিক সংজ্ঞাবহ বৈশিষ্ট্য।\nReason (R): কোনো কোষীয় প্রাচীর বা পর্দা ছাড়াই কোষের আণবিক উপাদানগুলি স্বাধীনভাবে জীবন ধারণ করতে পারে।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['(A) is true but (R) is false', 'Both (A) and (R) are true and (R) is the correct explanation of (A)', 'Both (A) and (R) are true but (R) is NOT the correct explanation of (A)', '(A) is false but (R) is true'],
            "bn": ['(A) সত্য কিন্তু (R) মিথ্যা', '(A) এবং (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) মিথ্যা কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Assertion (A) is true. Reason (R) is false because anything less than a complete structure of a cell does not ensure independent living. Cellular organization is mandatory for life.',
        "expl_bn": '(A) সত্য। কিন্তু (R) সম্পূর্ণ মিথ্যা কারণ একটি পূর্ণাঙ্গ কোষীয় গঠন ব্যতীত কোনো জৈব অণু স্বাধীনভাবে জীবন প্রকাশ করতে পারে না।',
    },
    {
        "id": 'BIO-LW-079',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Assertion (A): In a taxonomic key, a pair of contrasting characters is called a couplet.\nReason (R): A key is based on the acceptance of only one choice and rejection of the other, leading to analytical identification.\nChoose the correct option:',
        "bn": 'Assertion (A): ট্যাক্সোনমিক কি-তে বিপরীতধর্মী জোড় চরিত্রকে কাপলেট (couplet) বলা হয়।\nReason (R): একটি কি-তে যেকোনো একটি বিকল্পকে গ্রহণ এবং অপরটিকে বর্জনের মাধ্যমে বিশ্লেষণমূলক সনাক্তকরণ ঘটে।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Both (A) and (R) are true and (R) is the correct explanation of (A)', 'Both (A) and (R) are true but (R) is NOT the correct explanation of (A)', '(A) is true but (R) is false', '(A) is false but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য কিন্তু (R) মিথ্যা', '(A) মিথ্যা কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Both (A) and (R) are true and (R) is the direct explanation of how a couplet functions: it presents two opposing leads, forcing acceptance of one and rejection of the other.',
        "expl_bn": '(A) ও (R) উভয়ই সত্য এবং (R) সঠিকভাবে ব্যাখ্যা করে যে কীভাবে কাপলেটের দুটি বিপরীতমুখী বিকল্পের একটিকে বেছে নিয়ে জীবকে সনাক্ত করা হয়।',
    },
    {
        "id": 'BIO-LW-080',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Solanum, Petunia, and Datura are placed in the same family Solanaceae.\nReason (R): Families are characterized based on vegetative features only, while floral features are ignored.\nChoose the correct option:',
        "bn": 'Assertion (A): Solanum, Petunia এবং Datura গণগুলিকে একই গোত্র Solanaceae-তে অন্তর্ভুক্ত করা হয়েছে।\nReason (R): গোত্র নির্ধারণে কেবল অঙ্গজ বৈশিষ্ট্য ব্যবহৃত হয় এবং পুষ্পীয় বৈশিষ্ট্য সম্পূর্ণ উপেক্ষা করা হয়।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['(A) is true but (R) is false', 'Both (A) and (R) are true and (R) is the correct explanation of (A)', 'Both (A) and (R) are true but (R) is NOT the correct explanation of (A)', '(A) is false but (R) is true'],
            "bn": ['(A) সত্য কিন্তু (R) মিথ্যা', '(A) এবং (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) মিথ্যা কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Assertion (A) is true. Reason (R) is false because families are characterized on the basis of BOTH vegetative AND reproductive (floral) features of plant species.',
        "expl_bn": '(A) সত্য। কিন্তু (R) মিথ্যা কারণ গোত্র গঠনে অঙ্গজ ও জননগত (পুষ্পীয়) উভয় বৈশিষ্ট্যকেই গুরুত্ব দেওয়া হয়।',
    },
    {
        "id": 'BIO-LW-081',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Match Column-I (Taxonomic category) with Column-II (Example in Homo sapiens) and select the correct code:\nColumn-I: (A) Family, (B) Order, (C) Class, (D) Phylum\nColumn-II: 1. Primata, 2. Chordata, 3. Hominidae, 4. Mammalia',
        "bn": 'কলাম-I (ট্যাক্সোনমিক ধাপ)-এর সাথে কলাম-II (মানুষের ক্ষেত্রে উদাহরণ) মিলিয়ে সঠিক কোড নির্বাচন করো:\nকলাম-I: (A) Family, (B) Order, (C) Class, (D) Phylum\nকলাম-II: 1. Primata, 2. Chordata, 3. Hominidae, 4. Mammalia',
        "opts": {
            "en": ['A-3, B-1, C-4, D-2', 'A-1, B-3, C-4, D-2', 'A-3, B-4, C-1, D-2', 'A-2, B-1, C-4, D-3'],
            "bn": ['A-3, B-1, C-4, D-2', 'A-1, B-3, C-4, D-2', 'A-3, B-4, C-1, D-2', 'A-2, B-1, C-4, D-3']
        },
        "correct": 0,
        "expl_en": 'For Homo sapiens: Family = Hominidae (A-3), Order = Primata (B-1), Class = Mammalia (C-4), Phylum = Chordata (D-2).',
        "expl_bn": 'মানুষের ক্ষেত্রে: Family = Hominidae (A-3), Order = Primata (B-1), Class = Mammalia (C-4), Phylum = Chordata (D-2)।',
    },
    {
        "id": 'BIO-LW-082',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Match Column-I (Organism) with Column-II (Taxonomic Order) and select the correct code:\nColumn-I: (A) Mango, (B) Housefly, (C) Wheat, (D) Tiger\nColumn-II: 1. Diptera, 2. Sapindales, 3. Carnivora, 4. Poales',
        "bn": 'কলাম-I (জীব)-এর সাথে কলাম-II (বর্গ বা Order) মিলিয়ে সঠিক কোডটি নির্বাচন করো:\nকলাম-I: (A) আম, (B) গৃহমাছি, (C) গম, (D) বাঘ\nকলাম-II: 1. Diptera, 2. Sapindales, 3. Carnivora, 4. Poales',
        "opts": {
            "en": ['A-2, B-1, C-4, D-3', 'A-1, B-2, C-4, D-3', 'A-2, B-4, C-1, D-3', 'A-4, B-1, C-2, D-3'],
            "bn": ['A-2, B-1, C-4, D-3', 'A-1, B-2, C-4, D-3', 'A-2, B-4, C-1, D-3', 'A-4, B-1, C-2, D-3']
        },
        "correct": 0,
        "expl_en": 'Mango = Sapindales (A-2); Housefly = Diptera (B-1); Wheat = Poales (C-4); Tiger = Carnivora (D-3).',
        "expl_bn": 'আমের বর্গ Sapindales (A-2); মাছির বর্গ Diptera (B-1); গমের বর্গ Poales (C-4); বাঘের বর্গ Carnivora (D-3)।',
    },
    {
        "id": 'BIO-LW-083',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Match Column-I (Taxonomical Aid) with Column-II (Characteristic Function) and select the correct code:\nColumn-I: (A) Herbarium, (B) Botanical Garden, (C) Museum, (D) Key\nColumn-II: 1. Preservation of plant and animal specimens in formalin, 2. Quick referral system of dried pressed specimens, 3. Analytical tool based on couplets, 4. Ex-situ collection of living plant species',
        "bn": 'কলাম-I (ট্যাক্সোনমিক এইড)-এর সাথে কলাম-II (কার্যকারিতা) মিলিয়ে সঠিক কোডটি নির্বাচন করো:\nকলাম-I: (A) হার্বেরিয়াম, (B) বোটানিক্যাল গার্ডেন, (C) মিউজিয়াম, (D) কি\nকলাম-II: 1. ফর্মালিনে উদ্ভিদ ও প্রাণীর নমুনা সংরক্ষণ, 2. শুকনো চাপা নমুনার দ্রুত রেফারেন্স ব্যবস্থা, 3. কাপলেটের ওপর ভিত্তি করে বিশ্লেষণাত্মক মাধ্যম, 4. জীবন্ত উদ্ভিদ প্রজাতির সংগ্রহ',
        "opts": {
            "en": ['A-2, B-4, C-1, D-3', 'A-4, B-2, C-1, D-3', 'A-2, B-1, C-4, D-3', 'A-3, B-4, C-1, D-2'],
            "bn": ['A-2, B-4, C-1, D-3', 'A-4, B-2, C-1, D-3', 'A-2, B-1, C-4, D-3', 'A-3, B-4, C-1, D-2']
        },
        "correct": 0,
        "expl_en": 'Herbarium = Quick referral system of dried specimens (A-2); Botanical garden = Ex-situ collection of living plants (B-4); Museum = Preserved specimens in containers/formalin (C-1); Key = Analytical tool using couplets (D-3).',
        "expl_bn": 'হার্বেরিয়াম = দ্রুত রেফারেন্স ব্যবস্থা (A-2); বোটানিক্যাল গার্ডেন = জীবন্ত উদ্ভিদের সংগ্রহ (B-4); মিউজিয়াম = জার বা ফর্মালিনে নমুনা সংরক্ষণ (C-1); কি = কাপলেট নির্ভর বিশ্লেষণাত্মক মাধ্যম (D-3)।',
    },
    {
        "id": 'BIO-LW-084',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Match Column-I with Column-II and choose the correct option:\nColumn-I: (A) Flora, (B) Manual, (C) Monograph, (D) Catalogue\nColumn-II: 1. Information on any one taxon, 2. Habitat and distribution of plants of a given area, 3. Alphabetical register of taxa, 4. Identification of names of species found in an area',
        "bn": 'কলাম-I এর সাথে কলাম-II মিলিয়ে সঠিক উত্তরটি বেছে নাও:\nকলাম-I: (A) ফ্লোরা, (B) ম্যানুয়াল, (C) মনোগ্রাফ, (D) ক্যাটালগ\nকলাম-II: 1. যেকোনো একটি ট্যাক্সনের তথ্য, 2. কোনো অঞ্চলের উদ্ভিদের বাসস্থান ও বিস্তার, 3. বর্ণানুক্রমিক প্রজাতির তালিকা, 4. কোনো অঞ্চলের প্রজাতির নাম সনাক্তকরণ',
        "opts": {
            "en": ['A-2, B-4, C-1, D-3', 'A-4, B-2, C-1, D-3', 'A-2, B-1, C-4, D-3', 'A-1, B-4, C-2, D-3'],
            "bn": ['A-2, B-4, C-1, D-3', 'A-4, B-2, C-1, D-3', 'A-2, B-1, C-4, D-3', 'A-1, B-4, C-2, D-3']
        },
        "correct": 0,
        "expl_en": 'Flora = Habitat and distribution of plants in an area (A-2); Manual = Identification of species names in an area (B-4); Monograph = Comprehensive account of any one taxon (C-1); Catalogue = Alphabetical index/register (D-3).',
        "expl_bn": 'ফ্লোরা = কোনো অঞ্চলের উদ্ভিদের বিস্তার (A-2); ম্যানুয়াল = প্রজাতির নাম সনাক্তকরণ (B-4); মনোগ্রাফ = একটিমাত্র ট্যাক্সনের পূর্ণাঙ্গ বিবরণ (C-1); ক্যাটালগ = বর্ণানুক্রমিক তালিকা (D-3)।',
    },
    {
        "id": 'BIO-LW-085',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Which of the following represents the correct taxonomic position of Wheat (Triticum aestivum)?',
        "bn": 'গম (Triticum aestivum)-এর সঠিক ট্যাক্সোনমিক বিন্যাস কোনটি?',
        "opts": {
            "en": ['Genus: Triticum, Family: Poaceae, Order: Poales, Class: Monocotyledonae, Division: Angiospermae', 'Genus: Triticum, Family: Anacardiaceae, Order: Sapindales, Class: Dicotyledonae, Division: Angiospermae', 'Genus: Triticum, Family: Poaceae, Order: Polymoniales, Class: Monocotyledonae, Division: Gymnospermae', 'Genus: Triticum, Family: Gramineae, Order: Diptera, Class: Insecta, Division: Spermatophyta'],
            "bn": ['গণ: Triticum, গোত্র: Poaceae, বর্গ: Poales, শ্রেণী: Monocotyledonae, বিভাগ: Angiospermae', 'গণ: Triticum, গোত্র: Anacardiaceae, বর্গ: Sapindales, শ্রেণী: Dicotyledonae, বিভাগ: Angiospermae', 'গণ: Triticum, গোত্র: Poaceae, বর্গ: Polymoniales, শ্রেণী: Monocotyledonae, বিভাগ: Gymnospermae', 'গণ: Triticum, গোত্র: Gramineae, বর্গ: Diptera, শ্রেণী: Insecta, বিভাগ: Spermatophyta']
        },
        "correct": 0,
        "expl_en": 'Wheat (Triticum aestivum): Genus = Triticum, Family = Poaceae, Order = Poales, Class = Monocotyledonae, Division = Angiospermae.',
        "expl_bn": 'গমের সঠিক শ্রেণীবিন্যাস: গণ = Triticum, গোত্র = Poaceae, বর্গ = Poales, শ্রেণী = Monocotyledonae, বিভাগ = Angiospermae।',
    },
    {
        "id": 'BIO-LW-086',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Examine the accompanying taxonomic hierarchy pyramid. Moving from the apex (Species) downward to the base (Kingdom), which of the following trends is scientifically observed?',
        "bn": 'সংযুক্ত ট্যাক্সোনমিক স্তরক্রম পিরামিডটি পর্যবেক্ষণ করো। শীর্ষবিন্দু (প্রজাতি) থেকে নিচের দিকে ভিত্তির (জগৎ) দিকে নামলে নিচের কোন প্রবণতাটি বিজ্ঞানসম্মতভাবে পরিলক্ষিত হয়?',
        "opts": {
            "en": ['Number of shared common characteristics decreases, while general diversity increases', 'Number of shared common characteristics increases, while morphological variation decreases', 'Specificity of anatomical attributes increases at each step', 'The organisms become reproductively isolated within the same taxon'],
            "bn": ['সদস্যদের সাধারণ সাদৃশ্যের সংখ্যা হ্রাস পায়, এবং সামগ্রিক বৈচিত্র্য বৃদ্ধি পায়', 'সাধারণ সাদৃশ্যের সংখ্যা বৃদ্ধি পায় এবং অঙ্গসংস্থানিক বৈচিত্র্য হ্রাস পায়', 'প্রতিটি ধাপে শারীরস্থানিক বৈশিষ্ট্যের নির্দিষ্টতা বৃদ্ধি পায়', 'একই ট্যাক্সনের অন্তর্গত জীবগুলি পারস্পরিক প্রজননে বিচ্ছিন্ন হয়ে পড়ে']
        },
        "correct": 0,
        "expl_en": 'As we proceed from species to kingdom (apex to base of pyramid), the number of common characteristics decreases, making it harder to determine relationships at higher levels.',
        "expl_bn": 'প্রজাতি থেকে জগতের দিকে (উপর থেকে নিচে) গেলে সদস্যদের সাধারণ বৈশিষ্ট্যের সংখ্যা ক্রমাগত হ্রাস পায় এবং সাধারণীকরণের মাত্রা বৃদ্ধি পায়।',
        "diagram": '<svg viewBox="0 0 500 240" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <polygon points="250,20 220,50 280,50" fill="#f43f5e" stroke="#be123c" stroke-width="1.5"/>\n  <text x="250" y="42" fill="#ffffff" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Species (Maximum Specificity)</text>\n  <polygon points="220,52 280,52 300,82 200,82" fill="#fb7185" stroke="#be123c" stroke-width="1.5"/>\n  <text x="250" y="72" fill="#881337" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Genus</text>\n  <polygon points="200,84 300,84 320,114 180,114" fill="#fda4af" stroke="#be123c" stroke-width="1.5"/>\n  <text x="250" y="104" fill="#881337" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Family (-aceae / -idae)</text>\n  <polygon points="180,116 320,116 340,146 160,146" fill="#fecdd3" stroke="#be123c" stroke-width="1.5"/>\n  <text x="250" y="136" fill="#9f1239" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Order (-ales)</text>\n  <polygon points="160,148 340,148 360,178 140,178" fill="#ffe4e6" stroke="#be123c" stroke-width="1.5"/>\n  <text x="250" y="168" fill="#9f1239" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Class</text>\n  <polygon points="140,180 360,180 380,210 120,210" fill="#fff1f2" stroke="#be123c" stroke-width="1.5"/>\n  <text x="250" y="200" fill="#9f1239" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Phylum / Division (-phyta)</text>\n  <polygon points="120,212 380,212 400,238 100,238" fill="#fda4af" stroke="#be123c" stroke-width="1.5"/>\n  <text x="250" y="230" fill="#881337" font-size="11" font-family="system-ui" font-weight="bold" text-anchor="middle">Kingdom (Highest Generality)</text>\n  <line x1="60" y1="230" x2="60" y2="30" stroke="#0284c7" stroke-width="2.5"/>\n  <text x="50" y="130" fill="#0369a1" font-size="10" font-family="system-ui" font-weight="bold" transform="rotate(-90,50,130)" text-anchor="middle">Increasing Common Characteristics →</text>\n  <line x1="440" y1="30" x2="440" y2="230" stroke="#059669" stroke-width="2.5"/>\n  <text x="455" y="130" fill="#047857" font-size="10" font-family="system-ui" font-weight="bold" transform="rotate(90,455,130)" text-anchor="middle">Increasing Diversity &amp; Generalisation →</text>\n</svg>',
    },
    {
        "id": 'BIO-LW-087',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'The provided diagram illustrates an official herbarium sheet with its standard label. If an examiner checks the label at the lower right corner, which entry MUST be absent from this label according to NCERT botanical guidelines?',
        "bn": 'প্রদত্ত চিত্রে একটি প্রমাণ হার্বেরিয়াম শিট এবং তার লেবেল দেখানো হয়েছে। NCERT-র নির্দেশিকা অনুযায়ী নিচের ডানদিকের লেবেলে কোন তথ্যটি কখনোই অন্তর্ভুক্ত থাকে না?',
        "opts": {
            "en": ['Height of the whole plant collected in the wild', 'Date of specimen collection', 'Botanical and English name', 'Name of the specimen collector'],
            "bn": ['প্রাকৃতিক পরিবেশে সংগৃহীত উদ্ভিদটির পূর্ণ উচ্চতা', 'নমুনা সংগ্রহের সুনির্দিষ্ট তারিখ', 'উদ্ভিদের বৈজ্ঞানিক ও ইংরেজি নাম', 'নমুনা সংগ্রহকারীর নাম']
        },
        "correct": 0,
        "expl_en": "Herbarium sheet labels provide date and place of collection, English, local and botanical names, family, and collector's name. Plant height and weight are NOT recorded on the label.",
        "expl_bn": 'হার্বেরিয়াম লেবেলে সংগ্রহের তারিখ, স্থান, ইংরেজি ও বৈজ্ঞানিক নাম, গোত্র এবং সংগ্রাহকের নাম থাকে; কিন্তু উদ্ভিদের উচ্চতা কখনোই লিপিবদ্ধ করা হয় না।',
        "diagram": '<svg viewBox="0 0 340 240" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <rect x="20" y="10" width="300" height="220" rx="4" fill="#fffbeb" stroke="#78350f" stroke-width="2"/>\n  <text x="170" y="28" fill="#92400e" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">Standard Herbarium Sheet (41 cm × 29 cm / 16.5" × 11.5")</text>\n  <path d="M 120 180 Q 130 110 160 50" fill="none" stroke="#15803d" stroke-width="3"/>\n  <path d="M 135 140 Q 105 130 95 140 Q 115 155 135 140" fill="#86efac" stroke="#16a34a" stroke-width="1.5"/>\n  <path d="M 145 105 Q 185 95 195 105 Q 175 120 145 105" fill="#86efac" stroke="#16a34a" stroke-width="1.5"/>\n  <path d="M 155 75 Q 125 65 115 75 Q 135 90 155 75" fill="#86efac" stroke="#16a34a" stroke-width="1.5"/>\n  <circle cx="160" cy="50" r="7" fill="#facc15" stroke="#ca8a04" stroke-width="1.5"/>\n  <rect x="180" y="150" width="130" height="70" rx="3" fill="#ffffff" stroke="#b45309" stroke-width="1.5"/>\n  <text x="185" y="165" fill="#78350f" font-size="8" font-family="system-ui" font-weight="bold">HERBARIUM LABEL</text>\n  <text x="185" y="177" fill="#451a03" font-size="7" font-family="system-ui">• Date &amp; Place of Collection</text>\n  <text x="185" y="187" fill="#451a03" font-size="7" font-family="system-ui">• English, Local &amp; Botanical Name</text>\n  <text x="185" y="197" fill="#451a03" font-size="7" font-family="system-ui">• Family</text>\n  <text x="185" y="207" fill="#451a03" font-size="7" font-family="system-ui">• Collector\'s Name (NO HEIGHT!)</text>\n</svg>',
    },
    {
        "id": 'BIO-LW-088',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Which of the following taxonomic categories contains organisms with the maximum degree of shared common characteristics?',
        "bn": 'নিচের কোন ট্যাক্সোনমিক ধাপটিতে অন্তর্ভুক্ত জীবদের মধ্যে সর্বোচ্চ মাত্রায় সাধারণ বৈশিষ্ট্য (maximum common characteristics) বিদ্যমান থাকে?',
        "opts": {
            "en": ['Species', 'Genus', 'Family', 'Class'],
            "bn": ['প্রজাতি (Species)', 'গণ (Genus)', 'গোত্র (Family)', 'শ্রেণী (Class)']
        },
        "correct": 0,
        "expl_en": 'Species is the lowest obligate taxonomic category. Members of a species share the maximum number of fundamental morphological and anatomical characteristics.',
        "expl_bn": 'প্রজাতি হলো সর্বনিম্ন একক, যার অন্তর্ভুক্ত সদস্যদের মধ্যে পারস্পরিক সর্বাধিক সাদৃশ্য এবং সাধারণ বৈশিষ্ট্য দেখতে পাওয়া যায়।',
    },
    {
        "id": 'BIO-LW-089',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Which of the following taxonomic categories contains organisms with the minimum number of common characteristics?',
        "bn": 'নিচের কোন শ্রেণীবদ্ধ ধাপে অন্তর্ভুক্ত জীবদের মধ্যে সর্বনিম্ন সংখ্যক সাধারণ বৈশিষ্ট্য (minimum common characteristics) থাকে?',
        "opts": {
            "en": ['Kingdom', 'Class', 'Order', 'Family'],
            "bn": ['জগৎ (Kingdom)', 'শ্রেণী (Class)', 'বর্গ (Order)', 'গোত্র (Family)']
        },
        "correct": 0,
        "expl_en": 'Kingdom is the highest category in the taxonomic hierarchy. Organisms in a kingdom share the least number of common characteristics compared to lower categories like class, order, or family.',
        "expl_bn": 'জগৎ (Kingdom) হলো স্তরক্রমের সর্বোচ্চ ধাপ, যেখানে অন্তর্ভুক্ত বিভিন্ন পর্বের প্রাণীদের মধ্যে সাধারণ বৈশিষ্ট্যের সংখ্যা সবচেয়ে কম থাকে।',
    },
    {
        "id": 'BIO-LW-090',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Which of the following statements regarding taxonomic keys is FALSE?',
        "bn": 'ট্যাক্সোনমিক কি (Key) সম্পর্কে নিচের কোন বক্তব্যটি ভুল?',
        "opts": {
            "en": ['A single universal key can identify all plant and animal species across the globe without separate category keys', 'Keys are based on contrasting characters in a pair called a couplet', 'Each individual statement in a taxonomic key is called a lead', 'Taxonomic keys are analytical in nature'],
            "bn": ['কোনো পৃথক ক্যাটাগরি কি ছাড়াই একটিমাত্র সার্বজনীন কি দিয়ে বিশ্বের সমস্ত উদ্ভিদ ও প্রাণীকে সনাক্ত করা যায়', 'কি একজোড়া বিপরীতধর্মী বৈশিষ্ট্যের (কাপলেট) ওপর ভিত্তি করে তৈরি হয়', 'ট্যাক্সোনমিক কি-এর প্রতিটি পৃথক বাক্যকে লিড বলা হয়', 'ট্যাক্সোনমিক কি প্রকৃতিগতভাবে বিশ্লেষণমূলক হয়']
        },
        "correct": 0,
        "expl_en": "The statement that a single key can identify all species is false. NCERT explicitly states: 'Separate taxonomic keys are required for each taxonomic category such as family, genus and species.'",
        "expl_bn": 'একটিমাত্র সার্বজনীন কি দিয়ে সমস্ত জীব সনাক্ত করা যায়—এই তথ্যটি সম্পূর্ণ ভুল; কারণ গোত্র, গণ ও প্রজাতির জন্য পৃথক পৃথক কি আবশ্যক।',
    },
    {
        "id": 'BIO-LW-091',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": 'What is the biological name of Housefly correctly printed according to binomial nomenclature rules?',
        "bn": 'দ্বিপদ নামকরণের সঠিক নিয়ম মেনে মুদ্রিত গৃহমাছির বৈজ্ঞানিক নাম কোনটি?',
        "opts": {
            "en": ['<i>Musca domestica</i>', '<i>musca Domestica</i>', 'Musca domestica (without italics/underline)', '<i>Musca Domestica</i>'],
            "bn": ['<i>Musca domestica</i>', '<i>musca Domestica</i>', 'Musca domestica (ইটালিক্স বা দাগ ছাড়া)', '<i>Musca Domestica</i>']
        },
        "correct": 0,
        "expl_en": "Musca domestica: Generic name begins with capital 'M', specific epithet begins with small 'd', and printed in italics.",
        "expl_bn": 'Musca domestica: গণের নাম বড় হাতের M এবং প্রজাতির নাম ছোট হাতের d দিয়ে শুরু হয়ে ইটালিক্স অক্ষরে মুদ্রিত।',
    },
    {
        "id": 'BIO-LW-092',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": "In taxonomic classification, 'Diptera' represents which taxonomic rank for Musca domestica?",
        "bn": "গৃহমাছির শ্রেণীবিন্যাসে 'Diptera' কোন ট্যাক্সোনমিক ধাপটিকে নির্দেশ করে?",
        "opts": {
            "en": ['Order', 'Family', 'Class', 'Phylum'],
            "bn": ['বর্গ (Order)', 'গোত্র (Family)', 'শ্রেণী (Class)', 'পর্ব (Phylum)']
        },
        "correct": 0,
        "expl_en": 'Diptera is the order of Musca domestica. Muscidae is the family, and Insecta is the class.',
        "expl_bn": 'Diptera হলো গৃহমাছির বর্গ (Order)।',
    },
    {
        "id": 'BIO-LW-093',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": "In taxonomic classification, 'Sapindales' represents which taxonomic rank for Mangifera indica?",
        "bn": "আমগাছের শ্রেণীবিন্যাসে 'Sapindales' কোন ট্যাক্সোনমিক ধাপটিকে নির্দেশ করে?",
        "opts": {
            "en": ['Order', 'Family', 'Class', 'Division'],
            "bn": ['বর্গ (Order)', 'গোত্র (Family)', 'শ্রেণী (Class)', 'বিভাগ (Division)']
        },
        "correct": 0,
        "expl_en": 'Sapindales is the order of mango (Mangifera indica). Anacardiaceae is the family, and Dicotyledonae is the class.',
        "expl_bn": 'Sapindales হলো আমগাছের বর্গ (Order)।',
    },
    {
        "id": 'BIO-LW-094',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Easy',
        "en": "In taxonomic classification, 'Poaceae' represents which taxonomic rank for Wheat (Triticum aestivum)?",
        "bn": "গমের শ্রেণীবিন্যাসে 'Poaceae' কোন ট্যাক্সোনমিক ধাপটিকে নির্দেশ করে?",
        "opts": {
            "en": ['Family', 'Order', 'Class', 'Division'],
            "bn": ['গোত্র (Family)', 'বর্গ (Order)', 'শ্রেণী (Class)', 'বিভাগ (Division)']
        },
        "correct": 0,
        "expl_en": 'Poaceae is the family of wheat (Triticum aestivum). Poales is the order, and Monocotyledonae is the class.',
        "expl_bn": 'Poaceae হলো গমের গোত্র (Family)।',
    },
    {
        "id": 'BIO-LW-095',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Which of the following includes unicellular organisms that reproduce by budding?',
        "bn": 'নিচের কোন এককোষী জীবটিতে কোরকোদ্গম বা বাডিং (Budding) প্রক্রিয়ায় জনন সম্পন্ন হয়?',
        "opts": {
            "en": ['Yeast (Saccharomyces)', 'Amoeba', 'Planaria', 'Spirogyra'],
            "bn": ['ইস্ট (Yeast)', 'অ্যামিবা', 'প্ল্যানেরিয়া', 'স্পাইরোগাইরা']
        },
        "correct": 0,
        "expl_en": 'In lower organisms like yeast and hydra, we observe budding. Yeast is a unicellular fungus reproducing by asymmetric budding.',
        "expl_bn": 'ইস্ট এবং হাইড্রাতে কোরকোদ্গম বা বাডিং দেখা যায়। ইস্ট হলো একটি এককোষী ছত্রাক যা বাডিং দ্বারা বংশবৃদ্ধি করে।',
    },
    {
        "id": 'BIO-LW-096',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Which of the following organisms can perceive and respond to environmental factors like light, water, temperature, other organisms, and pollutants?',
        "bn": 'নিচের কোন জীবগুলি আলো, জল, তাপমাত্রা, অন্যান্য জীব এবং দূষকের মতো পরিবেশগত উদ্দীপনা অনুধাবন ও সাড়া দিতে সক্ষম?',
        "opts": {
            "en": ['All living organisms, ranging from the simplest prokaryotes to the most complex eukaryotes', 'Multicellular vertebrates possessing a centralized nervous system only', 'Terrestrial flowering plants and mammals only', 'Organisms possessing self-consciousness exclusively'],
            "bn": ['সবচেয়ে সরল প্রোক্যারিওট থেকে শুরু করে সবচেয়ে জটিল ইউক্যারিওট পর্যন্ত সমস্ত জীব', 'শুধুমাত্র সুগঠিত স্নায়ুতন্ত্রযুক্ত বহুকোষী মেরুদণ্ডী প্রাণীরা', 'কেবলমাত্র স্থলজ সপুষ্পক উদ্ভিদ ও স্তন্যপায়ীরা', 'একচেটিয়াভাবে কেবল আত্ম-সচেতনতাযুক্ত জীবেরা']
        },
        "correct": 0,
        "expl_en": "NCERT explicitly asserts: 'All organisms, from the prokaryotes to the most complex eukaryotes can sense and respond to environmental cues.'",
        "expl_bn": 'NCERT-র সুস্পষ্ট বক্তব্য: আদিমতম প্রোক্যারিওট থেকে শুরু করে জটিলতম বহুকোষী ইউক্যারিওট পর্যন্ত প্রতিটি জীব পরিবেশীয় উদ্দীপনায় সাড়া দিতে সক্ষম।',
    },
    {
        "id": 'BIO-LW-097',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Which of the following books was published by Carolus Linnaeus to establish the scientific classification and naming of animal species (1758)?',
        "bn": 'ক্যারোলাস লিনিয়াস কর্তৃক প্রাণীদের শ্রেণীবিন্যাস ও দ্বিপদ নামকরণের ভিত্তি হিসেবে প্রকাশিত বিখ্যাত গ্রন্থ কোনটি (১৭৫৮)?',
        "opts": {
            "en": ['Systema Naturae (10th Edition)', 'Species Plantarum', 'Genera Plantarum', 'Philosophia Botanica'],
            "bn": ['Systema Naturae (দশম সংস্করণ)', 'Species Plantarum', 'Genera Plantarum', 'Philosophia Botanica']
        },
        "correct": 0,
        "expl_en": 'Linnaeus published Systema Naturae (10th edition, 1758) which is regarded as the starting point for zoological binomial nomenclature. Species Plantarum (1753) was for plants.',
        "expl_bn": '১৭৫৮ সালে প্রকাশিত Systema Naturae-র দশম সংস্করণকে প্রাণীদের দ্বিপদ নামকরণের আনুষ্ঠানিক সূচনা হিসেবে গণ্য করা হয়।',
    },
    {
        "id": 'BIO-LW-098',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Which of the following statements about taxonomical hierarchy is INCORRECT?',
        "bn": 'ট্যাক্সোনমিক স্তরক্রম সম্পর্কে নিচের কোন উক্তিটি ভুল?',
        "opts": {
            "en": ['As we move from kingdom down to species, the difficulty of determining relationships increases', 'As we move from species up to kingdom, the number of common characteristics decreases', 'Species is the lowest obligate taxonomic category', 'Genera are aggregates of closely related species'],
            "bn": ['জগৎ থেকে প্রজাতির দিকে নিচের দিকে নামলে জীবের মধ্যকার পারস্পরিক সম্পর্ক নির্ধারণের জটিলতা বৃদ্ধি পায়', 'প্রজাতি থেকে জগতের দিকে উঠলে সাধারণ বৈশিষ্ট্যের সংখ্যা হ্রাস পায়', 'প্রজাতি হলো সর্বনিম্ন আবশ্যিক ট্যাক্সোনমিক ধাপ', 'গণ হলো ঘনিষ্ঠ সম্পর্কযুক্ত প্রজাতির সমষ্টি']
        },
        "correct": 0,
        "expl_en": "NCERT notes: 'Higher the category, greater is the difficulty of determining the relationship to other taxa at the same level.' Thus, moving UP increases difficulty, not moving down.",
        "expl_bn": 'স্তরক্রমের যত উপরের দিকে (জগতের দিকে) যাওয়া যায়, সম্পর্ক নির্ধারণ তত জটিল হয়। নিচ নামলে সম্পর্ক স্পষ্ট হয়; তাই প্রথম উক্তিটি সম্পূর্ণ ভুল।',
    },
    {
        "id": 'BIO-LW-099',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Medium',
        "en": 'Which term describes a book containing information on the identification of names of species found in an area, but without extensive accounts of habitat and geographic distribution?',
        "bn": 'কোনো অঞ্চলে প্রাপ্ত প্রজাতির নাম সনাক্তকরণের সংক্ষেপিত তথ্য সম্বলিত কিন্তু পূর্ণাঙ্গ বিস্তার বিবরণীহীন গ্রন্থকে কী বলা হয়?',
        "opts": {
            "en": ['Manual', 'Flora', 'Monograph', 'Herbarium'],
            "bn": ['ম্যানুয়াল (Manual)', 'ফ্লোরা (Flora)', 'মনোগ্রাফ (Monograph)', 'হার্বেরিয়াম']
        },
        "correct": 0,
        "expl_en": 'Manuals provide information for identification of names of species found in an area, whereas Flora provides the complete account of habitat and distribution.',
        "expl_bn": 'ম্যানুয়াল (Manual) কেবল প্রজাতির নাম সনাক্তকরণের তথ্য দেয়, আর সম্পূর্ণ বাসস্থান ও বিস্তারের বিবরণ থাকে ফ্লোরায়।',
    },
    {
        "id": 'BIO-LW-100',
        "exam": 'NEET, AIIMS, CUET, OLYMPIAD',
        "subject": 'Biology',
        "topic": 'The Living World',
        "difficulty": 'Hard',
        "en": 'Consider the following four statements (I-IV) regarding biological classification:\nI. Cellular organisation is a defining feature of life forms.\nII. Isolated metabolic reactions in vitro are living things.\nIII. Photoperiod affects reproduction in seasonal breeders in plants and animals.\nIV. Species is an abstract concept without real physical biological individuals.\nWhich of the above statements are TRUE?',
        "bn": 'জৈবিক শ্রেণীবিন্যাস সম্পর্কিত নিচের চারটি বিবৃতি (I-IV) বিবেচনা করো:\nI. কোষীয় সংগঠন হলো সজীবতার একটি সংজ্ঞাবহ বৈশিষ্ট্য।\nII. টেস্ট টিউবে বিচ্ছিন্ন বিপাকীয় বিক্রিয়াগুলি সজীব সত্তা বা জীব।\nIII. আলোককাল উদ্ভিদ ও প্রাণীর ঋতুভিত্তিক প্রজননকারীদের প্রজননকে প্রভাবিত করে।\nIV. প্রজাতি হলো কোনো বাস্তব শারীরিক অস্তিত্বহীন একটি কাল্পনিক ধারণা।\nউপরের কোন বিবৃতিগুলি সত্য?',
        "opts": {
            "en": ['I and III only', 'I, II, and III only', 'II and IV only', 'I, III, and IV only'],
            "bn": ['শুধুমাত্র I এবং III', 'শুধুমাত্র I, II এবং III', 'শুধুমাত্র II এবং IV', 'শুধুমাত্র I, III এবং IV']
        },
        "correct": 0,
        "expl_en": 'Statements I and III are true according to NCERT. Statement II is false because in vitro reactions are living reactions, not living things. Statement IV is false because species is the real fundamental unit of biological classification consisting of physical individuals.',
        "expl_bn": 'বিবৃতি I এবং III সত্য। বিবৃতি II ভুল কারণ টেস্ট টিউবের বিক্রিয়া কোনো জীব নয়। বিবৃতি IV ভুল কারণ প্রজাতি হলো বাস্তব অস্তিত্বশীল জীবদের মৌলিক একক।',
    },
    {
        "id": 'BIO-BC-001',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Who was the earliest scientist to attempt a more scientific basis for classification, categorizing plants into trees, shrubs, and herbs, and animals into two groups based on whether they had red blood or not?',
        "bn": 'কে সর্বপ্রথম উদ্ভিদের ক্ষেত্রে বৃক্ষ, গুল্ম ও বিরুৎ এবং প্রাণীদের ক্ষেত্রে লোহিত রক্তকণিকার উপস্থিতি ও অনুপস্থিতির ভিত্তিতে শ্রেণীবিন্যাসের বৈজ্ঞানিক প্রচেষ্টা করেন?',
        "opts": {
            "en": ['Aristotle', 'Carolus Linnaeus', 'Pliny the Elder', 'Theophrastus'],
            "bn": ['অ্যারিস্টটল (Aristotle)', 'ক্যারোলাস লিনিয়াস', 'প্লিনি দ্য এল্ডার', 'থিওফ্রাস্টাস']
        },
        "correct": 0,
        "expl_en": 'Aristotle was the earliest to attempt a more scientific basis for biological classification. He used simple morphological characters to classify plants into trees, shrubs and herbs, and divided animals into two groups: those which had red blood (Enaima) and those that did not (Anaima).',
        "expl_bn": 'অ্যারিস্টটল সর্বপ্রথম সরল অঙ্গসংস্থানিক বৈশিষ্ট্যের ভিত্তিতে উদ্ভিদের বৃক্ষ, গুল্ম ও বিরুৎ এবং প্রাণীদের লোহিত রক্তযুক্ত ও লোহিত রক্তহীন এই দুটি ভাগে ভাগ করেন।',
    },
    {
        "id": 'BIO-BC-002',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'The Two-Kingdom classification system dividing all organisms into Plantae and Animalia was developed by:',
        "bn": 'সমস্ত জীবকে প্ল্যান্টি (Plantae) এবং অ্যানিম্যালিয়া (Animalia) এই দুই জগতে বিভক্তকারী দ্বি-রাজ্য শ্রেণীবিন্যাস কে প্রবর্তন করেন?',
        "opts": {
            "en": ['Carolus Linnaeus', 'R.H. Whittaker', 'Ernst Haeckel', 'Carl Woese'],
            "bn": ['ক্যারোলাস লিনিয়াস', 'আর. এইচ. হুইটেকার', 'আর্নস্ট হেকেল', 'কার্ল ওজ']
        },
        "correct": 0,
        "expl_en": "In Linnaeus' time a Two Kingdom system of classification with Plantae and Animalia kingdoms was developed that included all plants and animals respectively.",
        "expl_bn": 'ক্যারোলাস লিনিয়াস সমস্ত জীবকে উদ্ভিদ (Plantae) এবং প্রাণী (Animalia) এই দুটি প্রধান জগতে ভাগ করে দ্বি-রাজ্য শ্রেণীবিন্যাস চালু করেন।',
    },
    {
        "id": 'BIO-BC-003',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": "Which major scientific limitation led to the inadequacy of Linnaeus' Two-Kingdom classification system?",
        "bn": 'কোন প্রধান বৈজ্ঞানিক সীমাবদ্ধতার কারণে লিনিয়াসের দ্বি-রাজ্য শ্রেণীবিন্যাস পদ্ধতিটি বাতিল ও অপর্যাপ্ত বিবেচিত হয়?',
        "opts": {
            "en": ['It did not distinguish between eukaryotes and prokaryotes, unicellular and multicellular organisms, or photosynthetic and non-photosynthetic organisms', 'It classified viruses as higher multicellular plants', 'It excluded bacteria and fungi completely from living kingdoms', 'It failed to recognize the economic agricultural value of timber trees'],
            "bn": ['এটি প্রোক্যারিওট ও ইউক্যারিওট, এককোষী ও বহুকোষী এবং সালোকসংশ্লেষী ও অ-সালোকসংশ্লেষী জীবের মধ্যে কোনো পার্থক্য নির্দেশ করতে পারেনি', 'এটি ভাইরাসকে উন্নত বহুকোষী উদ্ভিদ হিসেবে শ্রেণীবদ্ধ করেছিল', 'এটি ব্যাকটেরিয়া এবং ছত্রাককে সজীব জগৎ থেকে সম্পূর্ণ বাদ দিয়েছিল', 'এটি কাঠজাতীয় বৃক্ষের বাণিজ্যিক কৃষিমূল্য স্বীকার করতে ব্যর্থ হয়েছিল']
        },
        "correct": 0,
        "expl_en": "Linnaeus' two-kingdom system did not distinguish between eukaryotes and prokaryotes, unicellular and multicellular organisms, and photosynthetic (green algae) and non-photosynthetic (fungi) organisms.",
        "expl_bn": 'লিনিয়াসের পদ্ধতিতে প্রোক্যারিওট ও ইউক্যারিওট, এককোষী ও বহুকোষী এবং স্বভোজী শৈবাল ও মৃতজীবী ছত্রাকের মধ্যে কোনো বিভাজন ছিল না।',
    },
    {
        "id": 'BIO-BC-004',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'In which year did R.H. Whittaker propose the famous Five-Kingdom classification system?',
        "bn": 'কোন সালে আর. এইচ. হুইটেকার তাঁর বিখ্যাত পঞ্চ-রাজ্য (Five-Kingdom) শ্রেণীবিন্যাস পদ্ধতি প্রস্তাব করেন?',
        "opts": {
            "en": ['1969', '1953', '1972', '1980'],
            "bn": ['১৯৬৯', '১৯৫৩', '১৯৭২', '১৯৮০']
        },
        "correct": 0,
        "expl_en": 'R.H. Whittaker proposed the Five Kingdom Classification in the year 1969. The kingdoms defined by him were named Monera, Protista, Fungi, Plantae and Animalia.',
        "expl_bn": '১৯৬৯ সালে আর. এইচ. হুইটেকার পঞ্চ-রাজ্য শ্রেণীবিন্যাস পদ্ধতি প্রস্তাব করেন: মনেরা, প্রোটিস্টা, ফাংগাই, প্ল্যান্টি এবং অ্যানিম্যালিয়া।',
    },
    {
        "id": 'BIO-BC-005',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Which of the following was NOT among the primary criteria used by R.H. Whittaker for the Five-Kingdom classification?',
        "bn": 'নিচের কোনটি আর. এইচ. হুইটেকারের পঞ্চ-রাজ্য শ্রেণীবিন্যাসের প্রধান মানদণ্ডগুলির অন্তর্ভুক্ত ছিল না?',
        "opts": {
            "en": ['Physiological blood pressure and excretory urea percentage', 'Cell structure and thallus body organisation', 'Mode of nutrition and reproduction', 'Phylogenetic (evolutionary) relationships'],
            "bn": ['শারীরবৃত্তীয় রক্তচাপ এবং রেচনে ইউরিয়ার শতকরা হার', 'কোষের গঠন এবং থ্যালাসের দৈহিক সংগঠন', 'পুষ্টির পদ্ধতি এবং প্রজনন প্রক্রিয়া', 'জাতিজনি বা বিবর্তনীয় সম্পর্ক (Phylogenetic relationships)']
        },
        "correct": 0,
        "expl_en": 'The main criteria for classification used by Whittaker included cell structure, body organisation, mode of nutrition, reproduction and phylogenetic relationships. Physiological blood pressure is not a criterion.',
        "expl_bn": 'হুইটেকারের পঞ্চ-রাজ্যের মূল পাঁচটি মাপকাঠি ছিল: কোষের গঠন, দৈহিক সংগঠন, পুষ্টি পদ্ধতি, প্রজনন এবং জাতিজনি বা বিবর্তনীয় সম্পর্ক।',
    },
    {
        "id": 'BIO-BC-006',
        "exam": 'NEET, CUET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": "In Carl Woese's Three-Domain (six-kingdom) system of classification, the kingdom Monera was divided into which two domains?",
        "bn": 'কার্ল ওজ (Carl Woese)-এর ত্রি-ডোমেন শ্রেণীবিন্যাস পদ্ধতিতে মনেরা জগৎটিকে কোন দুটি স্বতন্ত্র ডোমেনে বিভক্ত করা হয়?',
        "opts": {
            "en": ['Archaea and Bacteria', 'Prokarya and Eukarya', 'Cyanobacteria and Mycoplasma', 'Protista and Monera'],
            "bn": ['আর্কিয়া (Archaea) এবং ব্যাকটেরিয়া (Bacteria)', 'প্রোক্যারিয়া এবং ইউক্যারিয়া', 'সায়ানোব্যাকটেরিয়া এবং মাইকোপ্লাজমা', 'প্রোটিস্টা এবং মনেরা']
        },
        "correct": 0,
        "expl_en": 'Carl Woese introduced the three-domain system that divides kingdom Monera into two domains: Archaea (Archaebacteria) and Bacteria (Eubacteria), leaving the third domain Eukarya to contain all eukaryotic kingdoms.',
        "expl_bn": 'কার্ল ওজের ত্রি-ডোমেন পদ্ধতিতে মনেরা জগৎকে দুটি ডোমেন—আর্কিয়া ও ব্যাকটেরিয়ায় ভাগ করা হয় এবং সমস্ত ইউক্যারিওটকে ইউক্যারিয়া ডোমেনে রাখা হয়।',
    },
    {
        "id": 'BIO-BC-007',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": "Which kingdom in Whittaker's five-kingdom classification system exclusively contains all prokaryotic organisms?",
        "bn": 'হুইটেকারের পঞ্চ-রাজ্য শ্রেণীবিন্যাসে কোন জগৎটি সমস্ত প্রোক্যারিওটিক জীবকে বিশেষভাবে ধারণ করে?',
        "opts": {
            "en": ['Kingdom Monera', 'Kingdom Protista', 'Kingdom Fungi', 'Kingdom Plantae'],
            "bn": ['মনেরা জগৎ (Kingdom Monera)', 'প্রোটিস্টা জগৎ', 'ফাংগাই (ছত্রাক) জগৎ', 'প্ল্যান্টি জগৎ']
        },
        "correct": 0,
        "expl_en": 'Kingdom Monera contains all prokaryotic organisms (bacteria, cyanobacteria, mycoplasma, archaebacteria). All other four kingdoms are eukaryotic.',
        "expl_bn": 'মনেরা (Monera) জগতের সমস্ত সদস্যই হলো প্রোক্যারিওট বা আদি নিউক্লিয়াসযুক্ত এককোষী জীব।',
    },
    {
        "id": 'BIO-BC-008',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Bacteria are the sole and principal members of which biological kingdom?',
        "bn": 'ব্যাকটেরিয়া কোন জৈবিক জগতের একমাত্র ও প্রধান সদস্য?',
        "opts": {
            "en": ['Kingdom Monera', 'Kingdom Protista', 'Kingdom Fungi', 'Kingdom Archaea'],
            "bn": ['মনেরা জগৎ (Kingdom Monera)', 'প্রোটিস্টা জগৎ', 'ছত্রাক জগৎ', 'আর্কিয়া জগৎ']
        },
        "correct": 0,
        "expl_en": "NCERT explicitly states: 'Bacteria are the sole members of the Kingdom Monera. They are the most abundant micro-organisms.'",
        "expl_bn": 'NCERT অনুসারে: ব্যাকটেরিয়া হলো মনেরা জগতের একমাত্র ও সর্বাধিক প্রভাবশালী সদস্য।',
    },
    {
        "id": 'BIO-BC-009',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Based on their morphological shapes, bacteria are grouped into four categories: spherical, rod-shaped, comma-shaped, and spiral. What are spherical bacteria called?',
        "bn": 'আকৃতির ভিত্তিতে ব্যাকটেরিয়া চার প্রকার: গোলাকার, দণ্ডাকার, কমা-আকৃতির এবং সর্পিলাকার। গোলাকার ব্যাকটেরিয়াকে কী বলা হয়?',
        "opts": {
            "en": ['Coccus (plural: Cocci)', 'Bacillus (plural: Bacilli)', 'Vibrium (plural: Vibrio)', 'Spirillum (plural: Spirilla)'],
            "bn": ['কক্কাস (Coccus, বহুবচনে Cocci)', 'ব্যাসিলাস (দণ্ডাকার)', 'ভিব্রিও (কমা-আকৃতি)', 'স্পাইরিলাম (সর্পিলাকার)']
        },
        "correct": 0,
        "expl_en": 'Bacteria are grouped into four categories based on their shape: spherical Coccus (pl. cocci), rod-shaped Bacillus (pl. bacilli), comma-shaped Vibrium (pl. vibrio), and spiral Spirillum (pl. spirilla).',
        "expl_bn": 'গোলাকার ব্যাকটেরিয়াকে কক্কাস (Coccus), দণ্ডাকারকে ব্যাসিলাস, কমা-আকৃতিরকে ভিব্রিও এবং পেঁচানো সর্পিলাকারকে স্পাইরিলাম বলে।',
    },
    {
        "id": 'BIO-BC-010',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Though bacterial structure is very simple, they are very complex in their:',
        "bn": 'ব্যাকটেরিয়ার শারীরিক গঠন অত্যন্ত সরল হওয়া সত্ত্বেও তারা কোন ক্ষেত্রে সর্বাধিক জটিলতা প্রদর্শন করে?',
        "opts": {
            "en": ['Metabolic diversity and behavior', 'Nuclear envelope architecture', 'Mitotic spindle formation', 'Histone chromosome condensation'],
            "bn": ['বিপাকীয় বৈচিত্র্য ও আচরণে (Metabolic diversity)', 'নিউক্লিয় পর্দা ও ছিদ্রের জটিলতায়', 'মাইটোটিক স্পিন্ডল গঠনে', 'হিস্টোন প্রোটিনের দ্বারা ক্রোমোজোম ঘনীভবনে']
        },
        "correct": 0,
        "expl_en": "NCERT notes: 'Though the bacterial structure is very simple, they are very complex in behaviour. Compared to many other organisms, which show metabolic diversity, bacteria as a group show the most extensive metabolic diversity.'",
        "expl_bn": 'NCERT অনুসারে: ব্যাকটেরিয়ার গঠন সরল হলেও তাদের বিপাকীয় বৈচিত্র্য (Metabolic diversity) ও আচরণ জীবজগতে সর্বাধিক বিস্তৃত।',
    },
    {
        "id": 'BIO-BC-011',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Archaebacteria differ from other bacteria (Eubacteria) primarily in having a different:',
        "bn": 'আর্কিব্যাকটেরিয়া অন্যান্য সাধারণ ব্যাকটেরিয়া (ইউব্যাকটেরিয়া) থেকে মূলত কিসের পার্থক্যের কারণে চরম প্রতিকূল পরিবেশে টিকে থাকে?',
        "opts": {
            "en": ['Cell wall structure and branched-chain lipid membrane structure', 'Ribosome size (70S vs 80S)', 'Double-stranded circular genomic DNA', 'Absence of genetic code and transcription enzymes'],
            "bn": ['কোষপ্রাচীরের গঠন এবং শাখান্বিত লিপিডযুক্ত কোষপর্দার গঠন', 'রাইবোজোমের আকার (70S বনাম 80S)', 'দ্বি-তন্ত্রী বৃত্তাকার ডিএনএ-র উপস্থিতি', 'জিনগত কোড ও ট্রান্সক্রিপশন উৎসেচকের সম্পূর্ণ অনুপস্থিতি']
        },
        "correct": 0,
        "expl_en": 'Archaebacteria differ from other bacteria in having a different cell wall structure (lacking peptidoglycan, having pseudomurein) and branched-chain ether-linked lipids in their cell membranes, enabling them to survive under extreme conditions.',
        "expl_bn": 'আর্কিব্যাকটেরিয়ার কোষপ্রাচীরে পেপটিডোগ্লাইক্যান থাকে না এবং কোষপর্দায় শাখান্বিত ইথার-যুক্ত লিপিড থাকায় এরা চরম প্রতিকূল পরিবেশে বেঁচে থাকতে পারে।',
    },
    {
        "id": 'BIO-BC-012',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Archaebacteria that flourish in extreme saline/salty environments are scientifically called:',
        "bn": 'চরম লবণাক্ত পরিবেশে বসবাসকারী আর্কিব্যাকটেরিয়াকে কী বলা হয়?',
        "opts": {
            "en": ['Halophiles', 'Thermoacidophiles', 'Methanogens', 'Cyanobacteria'],
            "bn": ['হ্যালোফাইলস (Halophiles)', 'থার্মোঅ্যাসিডোফাইলস', 'মিথেনোজেনস', 'সায়ানোব্যাকটেরিয়া']
        },
        "correct": 0,
        "expl_en": 'Archaebacteria living in extreme salty areas are called Halophiles. Those living in hot springs are Thermoacidophiles, and those in marshy areas are Methanogens.',
        "expl_bn": 'চরম লবণাক্ত অঞ্চলে বসবাসকারী আর্কিব্যাকটেরিয়াদের হ্যালোফাইলস (Halophiles) বলা হয়।',
    },
    {
        "id": 'BIO-BC-013',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Archaebacteria that thrive in hot sulphur springs at high temperatures and acidic pH are termed:',
        "bn": 'উচ্চ তাপমাত্রা এবং অম্লীয় পরিবেশযুক্ত উষ্ণ সালফার প্রস্রবণে বসবাসকারী আর্কিব্যাকটেরিয়াকে কী বলা হয়?',
        "opts": {
            "en": ['Thermoacidophiles', 'Halophiles', 'Methanogens', 'Heliophiles'],
            "bn": ['থার্মোঅ্যাসিডোফাইলস (Thermoacidophiles)', 'হ্যালোফাইলস', 'মিথেনোজেনস', 'হেলিওফাইলস']
        },
        "correct": 0,
        "expl_en": 'Thermoacidophiles thrive in hot springs where temperatures often exceed 80 °C and pH is highly acidic (around pH 2), utilizing sulphur oxidation.',
        "expl_bn": 'উষ্ণ প্রস্রবণের উচ্চ তাপ ও অম্লীয় পরিবেশে বসবাসকারীদের থার্মোঅ্যাসিডোফাইলস বলে।',
    },
    {
        "id": 'BIO-BC-014',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Methanogens are present in the gut of several ruminant animals such as cows and buffaloes, and they are responsible for the commercial production of:',
        "bn": 'গরু ও মহিষের মতো রোমন্থক প্রাণীদের পাকস্থলীতে মিথেনোজেন ব্যাকটেরিয়া উপস্থিত থাকে এবং এরা কী উৎপাদনের জন্য দায়ী?',
        "opts": {
            "en": ['Biogas (methane gas) from the dung of these animals', 'Alcoholic biofuel by industrial fermentation of cellulose', 'Nitric oxide for pasture fertilisation', 'Lactic acid curd in ruminant milk'],
            "bn": ['প্রাণীগুলির গোবর থেকে উৎপন্ন বায়োগ্যাস (মিথেন গ্যাস)', 'সেলুলোজের শিল্প গাঁজন দ্বারা অ্যালকোহল জৈব-জ্বালানি', 'চারণভূমির সার হিসেবে নাইট্রিক অক্সাইড', 'দুগ্ধে ল্যাকটিক অ্যাসিডের দই']
        },
        "correct": 0,
        "expl_en": 'Methanogens are present in the gut of ruminant animals (cows, buffaloes) and produce methane (biogas) from the dung of these animals.',
        "expl_bn": 'মিথেনোজেন ব্যাকটেরিয়া রোমন্থক প্রাণীর অন্ত্রে বাস করে তাদের গোবর থেকে মিথেন বা বায়োগ্যাস তৈরি করে।',
    },
    {
        "id": 'BIO-BC-015',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Eubacteria are characterized by the presence of a rigid cell wall and, if motile, possess:',
        "bn": 'ইউব্যাকটেরিয়া (প্রকৃত ব্যাকটেরিয়া) দৃঢ় কোষপ্রাচীর এবং চলনশীল হলে কীসের উপস্থিতি দ্বারা চিহ্নিত হয়?',
        "opts": {
            "en": ['A flagellum (made of flagellin protein)', 'Cilia with a 9+2 axoneme', 'Pseudopodia made of actin microfilaments', 'Gliding pellicle of collagen'],
            "bn": ['ফ্ল্যাজেলা (ফ্ল্যাজেলিন প্রোটিন দ্বারা গঠিত)', '৯+২ সজ্জাযুক্ত সিলিয়া', 'অ্যাক্টিন নির্মিত ক্ষণপদ বা সিউডোপোডিয়া', 'কোলাজেন নির্মিত পেলিকল']
        },
        "correct": 0,
        "expl_en": 'Eubacteria (true bacteria) are characterized by the presence of a rigid cell wall and, if motile, a flagellum.',
        "expl_bn": 'প্রকৃত ব্যাকটেরিয়া বা ইউব্যাকটেরিয়ায় পেপটিডোগ্লাইক্যান নির্মিত অনমনীয় প্রাচীর থাকে এবং চলনক্ষম হলে ফ্ল্যাজেলাম থাকে।',
    },
    {
        "id": 'BIO-BC-016',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Cyanobacteria (blue-green algae) are photosynthetic autotrophs that possess which major pigment identical to that of higher green plants?',
        "bn": 'সায়ানোব্যাকটেরিয়া (নীলাভ-সবুজ শৈবাল) হলো সালোকসংশ্লেষী স্বভোজী যাদের মধ্যে উন্নত সবুজ উদ্ভিদের অনুরূপ কোন প্রধান রঞ্জকটি উপস্থিত থাকে?',
        "opts": {
            "en": ['Chlorophyll a', 'Chlorophyll b', 'Chlorophyll c', 'Fucoxanthin'],
            "bn": ['ক্লোরোফিল a (Chlorophyll a)', 'ক্লোরোফিল b', 'ক্লোরোফিল c', 'ফিউকোজ্যান্থিন']
        },
        "correct": 0,
        "expl_en": 'Cyanobacteria have chlorophyll a similar to green plants and are photosynthetic autotrophs producing oxygen (oxygenic photosynthesis).',
        "expl_bn": 'সায়ানোব্যাকটেরিয়াতে সবুজ উদ্ভিদের মতো ক্লোরোফিল a উপস্থিত থাকে এবং এরা অক্সিজেনিক সালোকসংশ্লেষ চালায়।',
    },
    {
        "id": 'BIO-BC-017',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'The colonies of cyanobacteria are generally surrounded by a protective layer called a:',
        "bn": 'সায়ানোব্যাকটেরিয়ার কলোনি বা উপনিবেশগুলি সাধারণত কোন প্রতিরক্ষামূলক স্তর দ্বারা পরিবেষ্টিত থাকে?',
        "opts": {
            "en": ['Gelatinous / mucilaginous sheath', 'Calcareous calcium carbonate shell', 'Lignified secondary wall', 'Silicon dioxide frustule'],
            "bn": ['মিউসিলেজ বা জিলেটিনের পিচ্ছিল আবরণী', 'ক্যালসিয়াম কার্বনেটের খোলক', 'লিগনিনযুক্ত গৌণ প্রাচীর', 'সিলিকা নির্মিত ফ্রুস্টুল']
        },
        "correct": 0,
        "expl_en": 'Cyanobacteria are unicellular, colonial or filamentous, freshwater/marine or terrestrial algae. The colonies are generally surrounded by a gelatinous sheath.',
        "expl_bn": 'সায়ানোব্যাকটেরিয়ার সূত্রাকার কলোনিগুলি পিচ্ছিল জিলেটিন বা মিউসিলেজের আবরণ দ্বারা আবৃত থাকে যা এদের শুকিয়ে যাওয়া থেকে রক্ষা করে।',
    },
    {
        "id": 'BIO-BC-018',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'In organisms like Nostoc and Anabaena, atmospheric nitrogen (N2) is fixed in specialized, thick-walled cells called:',
        "bn": 'নস্টক (Nostoc) এবং অ্যানাবিনা (Anabaena)-র মতো জীবে বায়ুমণ্ডলীয় নাইট্রোজেন সংবন্ধনের জন্য গঠিত বিশেষ পুরু প্রাচীরযুক্ত কোষগুলিকে কী বলে?',
        "opts": {
            "en": ['Heterocysts', 'Akinetes', 'Hormogonia', 'Endospores'],
            "bn": ['হেটারোসিস্ট (Heterocysts)', 'অ্যাকাইনিটস', 'হরমোগোনিয়া', 'এন্ডোস্পোর']
        },
        "correct": 0,
        "expl_en": 'Some cyanobacteria can fix atmospheric nitrogen in specialized cells called heterocysts, e.g., Nostoc and Anabaena. Heterocysts lack oxygenic photosystem II to protect oxygen-sensitive nitrogenase.',
        "expl_bn": 'নস্টক ও অ্যানাবিনায় হেটারোসিস্ট (Heterocyst) নামক অক্সিজেন-প্রতিরোধী পুরু প্রাচীরযুক্ত বিশেষ কোষে নাইট্রোজেন সংবন্ধন ঘটে।',
    },
    {
        "id": 'BIO-BC-019',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Chemosynthetic autotrophic bacteria play an indispensable global ecological role in:',
        "bn": 'রসায়ন-সংশ্লেষী স্বভোজী (Chemosynthetic autotrophic) ব্যাকটেরিয়া বিশ্বজুড়ে পরিবেশীয়ভাবে কোন ক্ষেত্রে অপরিহার্য ভূমিকা পালন করে?',
        "opts": {
            "en": ['Recycling essential biogeochemical nutrients like nitrogen, phosphorus, iron, and sulphur', 'Fixing carbon exclusively during night via CAM metabolism', 'Causing algal blooms in polluted urban reservoirs', 'Direct synthesis of animal glycogen from inorganic rocks'],
            "bn": ['নাইট্রোজেন, ফসফরাস, লোহা ও সালফারের মতো অপরিহার্য মৌলসমূহের জৈব-ভূরাসায়নিক চক্রাবর্তন ও পুনর্ব্যবহারে', 'CAM বিপাকের মাধ্যমে কেবল রাতের বেলা কার্বন সংবন্ধনে', 'নগরের দূষিত জলাশয়ে ক্ষতিকর অ্যালগাল ব্লুম সৃষ্টিতে', 'খনিজ পাথর থেকে সরাসরি প্রাণিজ গ্লাইকোজেন সংশ্লেষে']
        },
        "correct": 0,
        "expl_en": 'Chemosynthetic autotrophs oxidize inorganic substances like nitrates, nitrites, and ammonia and use the released energy for ATP production. They play a great role in recycling nutrients like nitrogen, phosphorus, iron and sulphur.',
        "expl_bn": 'রসায়ন-স্বভোজী ব্যাকটেরিয়া অজৈব পদার্থ জারিত করে শক্তি উৎপাদন করে এবং নাইট্রোজেন, ফসফরাস, আয়রন ও সালফারের মতো মৌলের পুষ্টিচক্রে প্রধান ভূমিকা নেয়।',
    },
    {
        "id": 'BIO-BC-020',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'The majority of bacteria occurring in nature are ecologically categorized as:',
        "bn": 'প্রকৃতিতে প্রাপ্ত সংখ্যাগরিষ্ঠ ব্যাকটেরিয়াকে পরিবেশগতভাবে কোন শ্রেণীতে অন্তর্ভুক্ত করা হয়?',
        "opts": {
            "en": ['Heterotrophs and decomposers', 'Photosynthetic autotrophs', 'Chemosynthetic lithotrophs', 'Obligate mutualistic symbionts'],
            "bn": ['পরভোজী এবং বিয়োজক (Heterotrophs & decomposers)', 'সালোকসংশ্লেষী স্বভোজী', 'রসায়ন-স্বভোজী লিথোট্রফ', 'বাধ্যতামূলক মিথোজীবী']
        },
        "correct": 0,
        "expl_en": 'The majority of bacteria are heterotrophs, and many of them are significant decomposers of organic matter in nature.',
        "expl_bn": 'প্রকৃতির অধিকাংশ ব্যাকটেরিয়াই হলো পরভোজী (Heterotrophic) এবং প্রধান বিয়োজক (Decomposer)।',
    },
    {
        "id": 'BIO-BC-021',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Which of the following diseases in human beings and crops is caused by bacterial infection?',
        "bn": 'নিচের কোন মানব ও শস্য রোগগুলি ব্যাকটেরিয়াঘটিত সংক্রমণের দ্বারা ঘটে?',
        "opts": {
            "en": ['Cholera, Typhoid, Tetanus, and Citrus canker', 'Smallpox, Influenza, AIDS, and Tobacco mosaic', 'Sleeping sickness, Malaria, Amoebiasis, and Giardiasis', 'Late blight of potato, Red rust of tea, and Black rot'],
            "bn": ['কলেরা, টাইফয়েড, টিটেনাস এবং সাইট্রাস ক্যাঙ্কার', 'গুটিবসন্ত, ইনফ্লুয়েঞ্জা, এইডস এবং টোবাকো মোজাইক', 'স্লিপিং সিকনেস, ম্যালেরিয়া, অ্যামিবিয়াসিস এবং জিয়ার্ডিয়াসিস', 'আলুর ধসা রোগ, চায়ের লাল মরচে এবং ব্ল্যাক রট']
        },
        "correct": 0,
        "expl_en": "NCERT notes: 'Cholera (Vibrio cholerae), typhoid (Salmonella typhi), tetanus (Clostridium tetani), citrus canker (Xanthomonas axonopodis) are well known diseases caused by different bacteria.'",
        "expl_bn": 'কলেরা, টাইফয়েড, টিটেনাস এবং লেবুর সাইট্রাস ক্যাঙ্কার রোগ ব্যাকটেরিয়ার সংক্রমণে ঘটে।',
    },
    {
        "id": 'BIO-BC-022',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Bacteria reproduce mainly by which process, and under unfavourable conditions, they produce:',
        "bn": 'ব্যাকটেরিয়া মূলত কোন প্রক্রিয়ায় বংশবৃদ্ধি করে এবং প্রতিকূল পরিবেশে তারা কী তৈরি করে?',
        "opts": {
            "en": ['Fission; spores (endospores)', 'Mitotic karyokinesis; gametes', 'Meiotic reduction; zoospores', 'Parthenogenesis; cysts'],
            "bn": ['দ্বি-বিভাজন (Fission); রেণু বা এন্ডোস্পোর (Spores)', 'মাইটোটিক নিউক্লিয়াস বিভাজন; গ্যামেট', 'মিয়োসিস বিভাজন; জুস্পোর', 'পার্থেনোজেনেসিস; সিস্ট']
        },
        "correct": 0,
        "expl_en": 'Bacteria reproduce mainly by fission. Under unfavorable conditions, they produce highly resistant spores (endospores).',
        "expl_bn": 'ব্যাকটেরিয়া মূলত সাধারণ দ্বি-বিভাজন দ্বারা বংশবৃদ্ধি করে এবং প্রতিকূল পরিবেশে প্রতিরোধী রেণু (Endospore) তৈরি করে।',
    },
    {
        "id": 'BIO-BC-023',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Sexual reproduction in bacteria involves which mechanism of genetic recombination?',
        "bn": 'ব্যাকটেরিয়াতে আদিম যৌন জনন মূলত কোন জিনগত পুনর্যোজন প্রক্রিয়ার মাধ্যমে ঘটে?',
        "opts": {
            "en": ['Primitive DNA transfer from one bacterium to another (conjugation / transformation / transduction)', 'True gametic fusion with syngamy and zygote meiosis', 'Oogamous fertilisation in flagellated female archegonia', 'Alternation of isomorphic haploid and diploid thalli'],
            "bn": ['এক ব্যাকটেরিয়া থেকে অন্য ব্যাকটেরিয়ায় আদিম ডিএনএ স্থানান্তর (কনজুগেশন/ট্রান্সফরমেশন/ট্রান্সডাকশন)', 'প্রকৃত গ্যামেট মিলন ও জাইগোট মিয়োসিস', 'ফ্ল্যাজেলাযুক্ত আর্কিগোনিয়ামে নিষেক', 'হ্যাপ্লয়েড ও ডিপ্লয়েড থ্যালাসের সমরূপ যৌন জনুক্রম']
        },
        "correct": 0,
        "expl_en": 'Bacteria also reproduce by a sort of sexual reproduction by adopting a primitive type of DNA transfer from one bacterium to the other (conjugation, transformation, transduction).',
        "expl_bn": 'ব্যাকটেরিয়াতে কোনো গ্যামেট মিলন হয় না; এদের যৌন পুনর্যোজন ঘটে এক দেহ থেকে অন্য দেহে ডিএনএ স্থানান্তরের মাধ্যমে (যেমন কনজুগেশন)।',
    },
    {
        "id": 'BIO-BC-024',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Which of the following characteristics uniquely distinguishes Mycoplasma from all other prokaryotes?',
        "bn": 'মাইকোপ্লাজমা (Mycoplasma)-কে অন্যান্য সমস্ত প্রোক্যারিওট থেকে পৃথককারী অনন্য বৈশিষ্ট্য কোনটি?',
        "opts": {
            "en": ['Complete lack of a cell wall, smallest living cells known, and ability to survive without oxygen', 'Presence of thick chitinous cell wall and flagella', 'Possession of membrane-bound chloroplasts and 80S ribosomes', 'Inability to cause any disease in animals or plants'],
            "bn": ['কোষপ্রাচীরের সম্পূর্ণ অনুপস্থিতি, ক্ষুদ্রতম স্বাধীন কোষ এবং অক্সিজেন ছাড়াই বেঁচে থাকার সামর্থ্য', 'পুরু কাইটিন নির্মিত প্রাচীর এবং ফ্ল্যাজেলা', 'পর্দাবৃত ক্লোরোপ্লাস্ট এবং 80S রাইবোজোম', 'উদ্ভিদ ও প্রাণীতে কোনো রোগ সৃষ্টিতে অক্ষমতা']
        },
        "correct": 0,
        "expl_en": 'Mycoplasma completely lack a cell wall, are the smallest living cells known (approx. 0.3 μm), can survive without oxygen, and many are pathogenic in animals and plants.',
        "expl_bn": 'মাইকোপ্লাজমায় কোনো কোষপ্রাচীর থাকে না, এরা আবিষ্কৃত ক্ষুদ্রতম স্বাধীন জীব (০.৩ মাইক্রোমিটার), অক্সিজেন ছাড়াই বাঁচতে পারে এবং রোগ সৃষ্টি করে।',
    },
    {
        "id": 'BIO-BC-025',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'The approximate average cell size of Mycoplasma is:',
        "bn": 'মাইকোপ্লাজমা কোষের আনুমানিক গড় আকার কত?',
        "opts": {
            "en": ['0.3 μm in length', '3.0 to 5.0 μm in length', '10 to 20 μm in length', '0.02 μm in length'],
            "bn": ['০.৩ মাইক্রোমিটার (0.3 μm)', '৩.০ থেকে ৫.০ মাইক্রোমিটার', '১০ থেকে ২০ মাইক্রোমিটার', '০.০২ মাইক্রোমিটার']
        },
        "correct": 0,
        "expl_en": "NCERT notes: 'Mycoplasma are the smallest living cells known (0.3 μm in length), whereas bacteria could be 3 to 5 μm.'",
        "expl_bn": 'NCERT অনুসারে মাইকোপ্লাজমার দৈর্ঘ্য প্রায় ০.৩ মাইক্রোমিটার (0.3 μm)।',
    },
    {
        "id": 'BIO-BC-026',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": "All single-celled eukaryotic organisms are placed under which kingdom in Whittaker's system?",
        "bn": 'হুইটেকারের শ্রেণীবিন্যাস অনুসারে সমস্ত এককোষী ইউক্যারিওটিক জীবকে কোন জগতে অন্তর্ভুক্ত করা হয়েছে?',
        "opts": {
            "en": ['Kingdom Protista', 'Kingdom Monera', 'Kingdom Fungi', 'Kingdom Animalia'],
            "bn": ['প্রোটিস্টা জগৎ (Kingdom Protista)', 'মনেরা জগৎ', 'ছত্রাক জগৎ', 'অ্যানিম্যালিয়া জগৎ']
        },
        "correct": 0,
        "expl_en": 'All single-celled eukaryotes are placed under Kingdom Protista. However, the boundaries of this kingdom are not well defined.',
        "expl_bn": 'হুইটেকারের পদ্ধতিতে সমস্ত এককোষী ইউক্যারিওটিক জীবকে প্রোটিস্টা (Protista) জগতের অন্তর্ভুক্ত করা হয়েছে।',
    },
    {
        "id": 'BIO-BC-027',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": "Why are the boundaries of Kingdom Protista considered 'not well defined' by evolutionary biologists?",
        "bn": "বিজ্ঞানী ও ট্যাক্সোনমিস্টদের মতে প্রোটিস্টা জগতের সীমানা কেন 'সুনির্দিষ্ট নয়' (not well defined)?",
        "opts": {
            "en": ["What is 'a photosynthetic protist' to one biologist may be 'a plant' to another", 'Protists have no cellular membranes or genetic material', 'They only live in extinct oceanic geological sediments', 'They do not reproduce by any known biological process'],
            "bn": ["এক বিজ্ঞানীর কাছে যা 'সালোকসংশ্লেষী প্রোটিস্ট', অন্য বিজ্ঞানীর কাছে তা 'উদ্ভিদ' হিসেবে গণ্য হতে পারে", 'প্রোটিস্টদের কোনো কোষপর্দা বা জিনগত বস্তু থাকে না', 'এরা কেবল বিলুপ্ত সামুদ্রিক ভূতাত্ত্বিক পাললিক শিলায় বাস করত', 'এরা কোনো জ্ঞাত জৈবিক পদ্ধতিতে প্রজনন সম্পন্ন করে না']
        },
        "correct": 0,
        "expl_en": "NCERT remarks: 'Boundaries of this kingdom are not well defined. What may be a photosynthetic protist to one biologist may be a plant to another.' It acts as a polyphyletic link to plants, fungi, and animals.",
        "expl_bn": 'প্রোটিস্টার সদস্যদের মধ্যে বৈচিত্র্য এত বেশি যে এক গবেষকের কাছে যা সালোকসংশ্লেষী এককোষী প্রোটিস্ট, অন্যের কাছে তা আদ্য উদ্ভিদ বলে মনে হতে পারে।',
    },
    {
        "id": 'BIO-BC-028',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Chrysophytes include which of the following groups of aquatic organisms?',
        "bn": 'ক্রাইসোফাইটস (Chrysophytes)-এর মধ্যে নিচের কোন জলজ জীবগোষ্ঠীগুলি অন্তর্ভুক্ত?',
        "opts": {
            "en": ['Diatoms and golden algae (desmids)', 'Dinoflagellates and euglenoids', 'Slime moulds and protozoans', 'Amoeba and Paramecium'],
            "bn": ['ডায়াটম (Diatoms) এবং সোনালী শৈবাল (ডেসমিডস)', 'ডাইনোফ্ল্যাজেলেটস এবং ইউগ্লিনয়েডস', 'স্লাইম মোল্ড এবং প্রোটোজোয়া', 'অ্যামিবা এবং প্যারামেসিয়াম']
        },
        "correct": 0,
        "expl_en": 'Chrysophytes group includes diatoms and golden algae (desmids). They are found in freshwater as well as in marine environments.',
        "expl_bn": 'ক্রাইসোফাইটসের অন্তর্ভুক্ত হলো ডায়াটম এবং সোনালী শৈবাল (যাদের ডেসমিডস বলা হয়)।',
    },
    {
        "id": 'BIO-BC-029',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'In diatoms, the cell walls form two thin overlapping shells that fit together like a:',
        "bn": 'ডায়াটমে কোষপ্রাচীর দুটি পাতলা পরস্পর-আচ্ছাদনকারী খোলের মতো যুক্ত থাকে, যা দেখতে অবিকল কিসের মতো?',
        "opts": {
            "en": ['Soap box', 'Pencil box', 'Match box', 'Circular watch glass'],
            "bn": ['সাবানের বাক্স (Soap box)', 'পেন্সিল বাক্স', 'দিয়াশলাইয়ের বাক্স', 'ঘড়ির কাঁচের ঢাকনা']
        },
        "correct": 0,
        "expl_en": 'In diatoms the cell walls form two thin overlapping shells, which fit together as in a soap box. The walls are embedded with silica and thus the walls are indestructible.',
        "expl_bn": 'ডায়াটমের কোষপ্রাচীর দুটি অর্ধের সমন্বয়ে সাবানের বাক্সের (Soap box) মতো পরস্পর যুক্ত থাকে।',
    },
    {
        "id": 'BIO-BC-030',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Diatomaceous earth (kieselguhr) is formed over billions of years primarily due to the accumulation of indestructible cell walls containing:',
        "bn": 'ডায়াটোমেশিয়াস আর্থ (Diatomaceous earth) কোটি কোটি বছর ধরে মূলত কোন অবিনশ্বর উপাদানে গঠিত কোষপ্রাচীর সঞ্চিত হয়ে সৃষ্টি হয়েছে?',
        "opts": {
            "en": ['Silica (silicon dioxide)', 'Calcium carbonate', 'Cellulose and lignin', 'Chitin and glucan'],
            "bn": ['সিলিকা (Silica / সিলিকন ডাই-অক্সাইড)', 'ক্যালসিয়াম কার্বনেট', 'সেলুলোজ এবং লিগনিন', 'কাইটিন এবং গ্লুকান']
        },
        "correct": 0,
        "expl_en": "The walls of diatoms are embedded with silica and are indestructible. Diatoms leave behind large amounts of cell wall deposits in their habitat over billions of years, called 'diatomaceous earth'.",
        "expl_bn": 'ডায়াটমের প্রাচীরে সিলিকা প্রবিষ্ট থাকায় তা বিনষ্ট হয় না এবং কোটি কোটি বছর ধরে সমুদ্রের তলদেশে জমা হয়ে ডায়াটোমেশিয়াস আর্থ গঠন করে।',
    },
    {
        "id": 'BIO-BC-031',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Being gritty, diatomaceous earth is extensively used in industries for:',
        "bn": 'দানাযুক্ত বা কর্কশ (gritty) হওয়ার কারণে ডায়াটোমেশিয়াস আর্থ শিল্পক্ষেত্রে কোন কাজে ব্যাপকভাবে ব্যবহৃত হয়?',
        "opts": {
            "en": ['Polishing, and filtration of oils and syrups', 'Manufacture of edible dairy cheese and yoghurt', 'Synthetic plastic polymerization', 'Direct extraction of crude kerosene oil'],
            "bn": ['পালিশ করার কাজে এবং তেল ও সিরাপ পরিস্রাবণে (Filtration)', 'ভোজ্য চিজ ও দই তৈরিতে', 'কৃত্রিম প্লাস্টিক পলিমারককরণে', 'সরাসরি অপরিশোধিত কেরোসিন নিষ্কাশনে']
        },
        "correct": 0,
        "expl_en": "Being gritty, diatomaceous earth is used in polishing, filtration of oils and syrups. Diatoms are also the chief 'producers' in the oceans.",
        "expl_bn": 'কর্কশ দানাদার বৈশিষ্ট্যের জন্য ডায়াটোমেশিয়াস আর্থ পালিশ করতে এবং তেল ও মিষ্টি সিরাপ পরিশ্রুত করার কাজে ব্যবহৃত হয়।',
    },
    {
        "id": 'BIO-BC-032',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": "Which group of organisms are recognized as the 'chief producers' in the oceans?",
        "bn": 'মহাসাগরের প্রধান উৎপাদক (Chief producers in the oceans) হিসেবে কোন জীবগোষ্ঠী পরিচিত?',
        "opts": {
            "en": ['Diatoms', 'Dinoflagellates', 'Euglenoids', 'Brown algae'],
            "bn": ['ডায়াটম (Diatoms)', 'ডাইনোফ্ল্যাজেলেটস', 'ইউগ্লিনয়েডস', 'বাদামী শৈবাল']
        },
        "correct": 0,
        "expl_en": "NCERT explicitly highlights: 'Diatoms are the chief producers in the oceans.'",
        "expl_bn": 'NCERT-র সুস্পষ্ট বাক্য: ডায়াটম হলো সমুদ্র ও মহাসাগরের প্রধান উৎপাদক (Chief producers)।',
    },
    {
        "id": 'BIO-BC-033',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Dinoflagellates typically possess two flagella arranged in which specific anatomical pattern?',
        "bn": 'ডাইনোফ্ল্যাজেলেটসে সাধারণত দুটি ফ্ল্যাজেলা কোন নির্দিষ্ট অবস্থানে সজ্জিত থাকে?',
        "opts": {
            "en": ['One lies longitudinally and the other transversely in a furrow between the wall plates', 'Both flagella emerge at the anterior pole in parallel', 'Both flagella are coiled around the posterior pellicle', 'One is inside the nucleus and the other extends out'],
            "bn": ['একটি অনুদৈর্ঘ্যভাবে এবং অন্যটি প্রাচীর ফলকের মধ্যবর্তী খাঁজে অনুপ্রস্থভাবে সজ্জিত থাকে', 'উভয় ফ্ল্যাজেলাই সমান্তরালভাবে অগ্রপ্রান্ত থেকে নির্গত হয়', 'উভয় ফ্ল্যাজেলা পশ্চাৎ পেলিকলকে বেষ্টন করে থাকে', 'একটি নিউক্লিয়াসের ভেতর থাকে এবং অপরটি বাইরে বিস্তৃত হয়']
        },
        "correct": 0,
        "expl_en": 'Most dinoflagellates have two flagella: one lies longitudinally and the other transversely in a furrow between the stiff cellulose wall plates.',
        "expl_bn": 'ডাইনোফ্ল্যাজেলেটসের দুটি ফ্ল্যাজেলার একটি অনুদৈর্ঘ্যভাবে এবং অন্যটি প্রাচীরের খাঁজে অনুপ্রস্থভাবে অবস্থান করে।',
    },
    {
        "id": 'BIO-BC-034',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Red tides in the Mediterranean and tropical seas are caused by rapid population blooms of which red dinoflagellate?',
        "bn": "ভূমধ্যসাগরীয় ও ক্রান্তীয় সাগরে 'লাল জোয়ার' (Red tides) কোন লাল ডাইনোফ্ল্যাজেলেটের দ্রুত বংশবৃদ্ধির ফলে সৃষ্টি হয়?",
        "opts": {
            "en": ['Gonyaulax', 'Noctiluca', 'Euglena', 'Gymnodinium'],
            "bn": ['গনিয়াউলাক্স (Gonyaulax)', 'নকটিলুকা', 'ইউগ্লিনা', 'জিম্নোডিনিয়াম']
        },
        "correct": 0,
        "expl_en": 'Red dinoflagellates (Example: Gonyaulax) undergo such rapid multiplication that they make the sea appear red (red tides). Toxins released by such large numbers may even kill marine animals like fishes.',
        "expl_bn": 'Gonyaulax নামক লাল ডাইনোফ্ল্যাজেলেট সাগরে অস্বাভাবিক হারে বৃদ্ধি পেয়ে লাল জোয়ার (Red tide) সৃষ্টি করে এবং এর বিষাক্ত ক্ষরণে মাছ মারা যায়।',
    },
    {
        "id": 'BIO-BC-035',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Euglenoids lack a cell wall; instead, their flexible body is surrounded by a protein-rich membrane called a:',
        "bn": 'ইউগ্লিনয়েডসে কোনো সেলুলোজ প্রাচীর থাকে না; এর পরিবর্তে তাদের নমনীয় দেহ কোন প্রোটিনসমৃদ্ধ স্তর দ্বারা আবৃত থাকে?',
        "opts": {
            "en": ['Pellicle', 'Capsule', 'Periderm', 'Siliceous frustule'],
            "bn": ['পেলিকল (Pellicle)', 'ক্যাপসুল', 'পেরিডার্ম', 'সিলিকা নির্মিত ফ্রুস্টুল']
        },
        "correct": 0,
        "expl_en": 'Instead of a cell wall, euglenoids have a protein-rich layer called pellicle which makes their body flexible. They have two flagella (one short and one long).',
        "expl_bn": "ইউগ্লিনয়েডসে কোষপ্রাচীরের বদলে 'পেলিকল' (Pellicle) নামক নমনীয় প্রোটিনময় স্তর থাকে যা দেহকে সংকোচনশীল করে তোলে।",
    },
    {
        "id": 'BIO-BC-036',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Though euglenoids are photosynthetic in the presence of sunlight, when deprived of sunlight they behave as heterotrophs by predating on other smaller organisms. This dual mode of nutrition is termed:',
        "bn": 'সূর্যালোকের উপস্থিতিতে ইউগ্লিনয়েডস সালোকসংশ্লেষ করলেও সূর্যালোকের অনুপস্থিতিতে তারা অন্য ছোট জীব শিকার করে পরভোজীর মতো আচরণ করে। পুষ্টির এই দ্বৈত রূপকে কী বলা হয়?',
        "opts": {
            "en": ['Mixotrophic nutrition', 'Holozoic nutrition', 'Chemosynthetic nutrition', 'Obligate saprophytism'],
            "bn": ['মিক্সোট্রফিক পুষ্টি (Mixotrophic nutrition)', 'হলোজোয়িক পুষ্টি', 'কেমোসিন্থেটিক পুষ্টি', 'বাধ্যতামূলক মৃতজীবী পুষ্টি']
        },
        "correct": 0,
        "expl_en": 'NCERT states: Though photosynthetic in the presence of sunlight, when deprived of sunlight they behave like heterotrophs by predating on other smaller organisms. Interestingly, the pigments of euglenoids are identical to those present in higher plants. Example: Euglena.',
        "expl_bn": 'ইউগ্লিনয়েডসের আলোতে স্বভোজী ও অন্ধকারে পরভোজী হওয়ার এই অনন্য পুষ্টিপদ্ধতিকে মিক্সোট্রফিক (Mixotrophic) পুষ্টি বলা হয়।',
    },
    {
        "id": 'BIO-BC-037',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Slime moulds are ecologically categorized under which nutritional mode in Kingdom Protista?',
        "bn": 'প্রোটিস্টা জগতের অন্তর্ভুক্ত স্লাইম মোল্ড (Slime moulds)-কে পরিবেশগতভাবে কোন পুষ্টির অধীনে রাখা হয়?',
        "opts": {
            "en": ['Saprophytic protists', 'Photosynthetic autotrophic protists', 'Chemosynthetic protists', 'Obligate intracellular parasites'],
            "bn": ['মৃতজীবী প্রোটিস্ট (Saprophytic protists)', 'সালোকসংশ্লেষী স্বভোজী প্রোটিস্ট', 'রসায়ন-স্বভোজী প্রোটিস্ট', 'বাধ্যতামূলক অন্তঃকোষীয় পরজীবী']
        },
        "correct": 0,
        "expl_en": 'Slime moulds are saprophytic protists. The body moves along decaying twigs and leaves engulfing organic material.',
        "expl_bn": 'স্লাইম মোল্ড হলো মৃতজীবী প্রোটিস্ট, যারা পচা কাঠ ও পাতার জৈব পদার্থ ভক্ষণ করে বেঁচে থাকে।',
    },
    {
        "id": 'BIO-BC-038',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Under suitable conditions, slime moulds form an aggregation of multinucleated protoplasm which may grow and spread over several feet, called:',
        "bn": 'অনুকূল পরিবেশে স্লাইম মোল্ড বহুনিউক্লিয়াসযুক্ত প্রোটোপ্লাজমের এক পুঞ্জীভূত দেহ গঠন করে যা কয়েক ফুট পর্যন্ত বিস্তৃত হতে পারে, একে কী বলে?',
        "opts": {
            "en": ['Plasmodium', 'Pseudoplasmodium', 'Syncytium', 'Mycelium'],
            "bn": ['প্লাজমোডিয়াম (Plasmodium)', 'সিউডোপ্লাজমোডিয়াম', 'সিনসিটিয়াম', 'মাইসেলিয়াম']
        },
        "correct": 0,
        "expl_en": 'Under suitable conditions, slime moulds form an aggregation called plasmodium which may grow and spread over several feet. (Note: do not confuse this with the malarial parasite genus Plasmodium).',
        "expl_bn": 'অনুকূল পরিবেশে স্লাইম মোল্ড একত্রিত হয়ে যে বহুনিউক্লিয়াসীয় পিণ্ডাকার কাঠামো গঠন করে তাকে প্লাজমোডিয়াম (Plasmodium) বলে।',
    },
    {
        "id": 'BIO-BC-039',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'During unfavourable conditions, the plasmodium of slime moulds differentiates and forms fruiting bodies bearing spores at their tips. These spores:',
        "bn": 'প্রতিকূল পরিবেশে স্লাইম মোল্ডের প্লাজমোডিয়াম পরিবর্তিত হয়ে শীর্ষে রেণুযুক্ত ফ্রুটিং বডি গঠন করে। এই রেণুগুলি:',
        "opts": {
            "en": ['Possess true cell walls, are extremely resistant, and are dispersed by air currents', 'Lack cell walls completely and swim via uniflagellate zoospores', 'Are encased in calcium carbonate and dispersed by marine water currents', 'Immediately germinate into binary fission trophozoites'],
            "bn": ['প্রকৃত কোষপ্রাচীরযুক্ত, অত্যন্ত প্রতিরোধী এবং বায়ুপ্রবাহ দ্বারা বিস্তৃত হয়', 'প্রাচীরহীন এবং ফ্ল্যাজেলার সাহায্যে সাঁতার কাটে', 'ক্যালসিয়াম কার্বনেট দ্বারা আবৃত এবং সামুদ্রিক স্রোতে ছড়ায়', 'অবিলম্বে দ্বি-বিভাজনের মাধ্যমে ট্রফোজয়েটে পরিণত হয়']
        },
        "correct": 0,
        "expl_en": 'During unfavourable conditions, the plasmodium differentiates and forms fruiting bodies bearing spores at their tips. The spores possess true walls. They are extremely resistant and survive for many years under adverse conditions. Spores are dispersed by air currents.',
        "expl_bn": 'স্লাইম মোল্ডের ফ্রুটিং বডিতে উৎপন্ন রেণুগুলির প্রকৃত সেলুলোজ প্রাচীর থাকে, চরম প্রতিকূলতায় দীর্ঘকাল বেঁচে থাকে এবং বাতাসের সাহায্যে ছড়ায়।',
    },
    {
        "id": 'BIO-BC-040',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Protozoans are believed to be primitive relatives of which biological group?',
        "bn": 'প্রোটোজোয়া বা আদ্যপ্রাণীদের কোন জৈবিক গোষ্ঠীর আদিম আত্মীয় (Primitive relatives) বলে মনে করা হয়?',
        "opts": {
            "en": ['Animals', 'Plants', 'Fungi', 'Cyanobacteria'],
            "bn": ['প্রাণী (Animals)', 'উদ্ভিদ', 'ছত্রাক', 'সায়ানোব্যাকটেরিয়া']
        },
        "correct": 0,
        "expl_en": 'All protozoans are heterotrophs and live as predators or parasites. They are believed to be primitive relatives of animals.',
        "expl_bn": 'সমস্ত প্রোটোজোয়াই পরভোজী (শিকারী বা পরজীবী) এবং এদের প্রাণীদের আদিম পূর্বপুরুষ বা আত্মীয় গণ্য করা হয়।',
    },
    {
        "id": 'BIO-BC-041',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Which of the following amoeboid protozoans is a parasite causing amoebic dysentery in humans?',
        "bn": 'নিচের কোন অ্যামিবয়েড প্রোটোজোয়াটি মানুষের অন্ত্রে অ্যামিবিক আমাশয় রোগ সৃষ্টিকারী পরজীবী?',
        "opts": {
            "en": ['Entamoeba histolytica', 'Amoeba proteus', 'Trypanosoma gambiense', 'Paramecium caudatum'],
            "bn": ['এন্টঅ্যামিবা হিস্টোলাইটিকা (Entamoeba)', 'অ্যামিবা প্রোটিয়াস', 'ট্রিপ্যানোসোমা', 'প্যারামেসিয়াম']
        },
        "correct": 0,
        "expl_en": 'Amoeboid protozoans move and capture prey by putting out pseudopodia (false feet) as in Amoeba. Marine forms have silica shells on their surface. Some of them such as Entamoeba are parasites.',
        "expl_bn": 'Entamoeba histolytica হলো একটি পরজীবী অ্যামিবয়েড প্রোটোজোয়া যা মানুষের অন্ত্রে আমাশয় সৃষ্টি করে।',
    },
    {
        "id": 'BIO-BC-042',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Sleeping sickness, a deadly disease prevalent in tropical Africa transmitted by the tsetse fly, is caused by which flagellated protozoan?',
        "bn": 'আফ্রিকান স্লিপিং সিকনেস রোগটি সেটসি (tsetse) মাছির মাধ্যমে সংক্রামিত হয়; এটি কোন ফ্ল্যাজেলাযুক্ত প্রোটোজোয়ার কারণে ঘটে?',
        "opts": {
            "en": ['Trypanosoma', 'Leishmania', 'Trichomonas', 'Giardia'],
            "bn": ['ট্রিপ্যানোসোমা (Trypanosoma)', 'লেইশম্যানিয়া', 'ট্রাইকোমোনাস', 'জিয়ার্ডিয়া']
        },
        "correct": 0,
        "expl_en": 'Flagellated protozoans are either free-living or parasitic. The parasitic forms cause diseases such as sleeping sickness, e.g., Trypanosoma.',
        "expl_bn": 'Trypanosoma নামক ফ্ল্যাজেলেটেড প্রোটোজোয়ার সংক্রমণে বিপজ্জনক স্লিপিং সিকনেস রোগ হয়।',
    },
    {
        "id": 'BIO-BC-043',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Paramecium is an aquatic, ciliated protozoan that directs water-laden food into its gullet (cytopharynx) through:',
        "bn": 'প্যারামেসিয়াম একটি জলজ সিলিয়াযুক্ত প্রোটোজোয়া যা খাদ্যকণাকে তার গলবিল বা গালেটে (gullet) প্রবেশ করায় কিসের মাধ্যমে?',
        "opts": {
            "en": ['The coordinated, rhythmic movement of rows of thousands of cilia', 'Extension of broad blunt pseudopodia', 'Sudden contraction of a single long posterior flagellum', 'Suction created by hydrostatic pressure of pseudocoelom'],
            "bn": ['হাজার হাজার সিলিয়ার সুসংহত ছন্দময় আন্দোলনের মাধ্যমে', 'বিস্তৃত ভোঁতা ক্ষণপদ প্রসারণের দ্বারা', 'একটিমাত্র লম্বা ফ্ল্যাজেলার আকস্মিক সংকোচনে', 'সিউডোসিলোমের জলীয় চাপের আকর্ষণে']
        },
        "correct": 0,
        "expl_en": 'Ciliated protozoans are aquatic, actively moving organisms because of the presence of thousands of cilia. They have a cavity (gullet) that opens to the outside. The coordinated movement of rows of cilia causes the water laden with food to be steered into the gullet, e.g., Paramecium.',
        "expl_bn": 'প্যারামেসিয়ামে হাজার হাজার সিলিয়ার সুসংহত ছন্দময় গতির কারণে জল ও খাদ্যকণা তার গালেট বা মুখগহ্বরে প্রবেশ করে।',
    },
    {
        "id": 'BIO-BC-044',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Which group of protozoans includes diverse organisms that have an infectious spore-like stage in their life cycle, exemplified by Plasmodium?',
        "bn": 'প্রোটোজোয়ার কোন গোষ্ঠীর জীবনচক্রে সংক্রামক রেণুর মতো দশা থাকে, যার সবচেয়ে কুখ্যাত উদাহরণ প্লাজমোডিয়াম (Plasmodium)?',
        "opts": {
            "en": ['Sporozoans', 'Ciliates', 'Flagellates', 'Amoeboids'],
            "bn": ['স্পোরোজোয়া (Sporozoans)', 'সিলিয়েটস', 'ফ্ল্যাজেলেটস', 'অ্যামিবয়েডস']
        },
        "correct": 0,
        "expl_en": 'Sporozoans includes diverse organisms that have an infectious spore-like stage in their life cycle. The most notorious is Plasmodium (malarial parasite) which causes malaria.',
        "expl_bn": 'স্পোরোজোয়াদের জীবনচক্রে সংক্রামক স্পোর বা রেণুর মতো দশা থাকে, যার উদাহরণ ম্যালেরিয়ার জীবাণু Plasmodium।',
    },
    {
        "id": 'BIO-BC-045',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Kingdom Fungi constitutes a unique kingdom of heterotrophic organisms. With the exception of unicellular yeasts, the bodies of fungi are:',
        "bn": 'ফাংগাই হলো পরভোজী জীবের এক অনন্য জগৎ। এককোষী ইস্ট ছাড়া সমস্ত ছত্রাকের দেহ মূলত কেমন হয়?',
        "opts": {
            "en": ['Filamentous, consisting of slender thread-like hyphae', 'Coelenterate polyps with calcium exoskeleton', 'Colonial spherical cocci with peptidoglycan walls', 'Non-flagellated parenchyma tissues'],
            "bn": ['সূত্রাকার, যা হাইফা (Hyphae) নামক সরু সুতোর মতো গঠন দ্বারা তৈরি', 'ক্যালসিয়াম খোলকযুক্ত পলিপ', 'পেপটিডোগ্লাইক্যান প্রাচীরযুক্ত গোলাকার কলোনি', 'ফ্ল্যাজেলাবিহীন প্যারেনকাইমা কলা']
        },
        "correct": 0,
        "expl_en": 'With the exception of yeasts which are unicellular, fungi are filamentous. Their bodies consist of long, slender thread-like structures called hyphae.',
        "expl_bn": 'এককোষী ইস্ট ব্যতীত ছত্রাকের দেহ মূলত সূত্রাকার হাইফা (Hyphae)-র সমন্বয়ে গঠিত।',
    },
    {
        "id": 'BIO-BC-046',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'A continuous fungal hypha filled with multinucleated cytoplasm without intervening cross-walls (septa) is termed:',
        "bn": 'কোনো প্রকার অনুপ্রস্থ প্রাচীর (septa) ছাড়া বহুনিউক্লিয়াসযুক্ত সাইটোপ্লাজমে পূর্ণ অবিচ্ছিন্ন ছত্রাকীয় হাইফাকে কী বলা হয়?',
        "opts": {
            "en": ['Coenocytic hypha', 'Septate hypha', 'Haustorium', 'Dikaryon'],
            "bn": ['সিনোসাইটিক হাইফা (Coenocytic hypha)', 'সেপ্টেট হাইফা', 'হস্টোরিয়াম', 'ডাইক্যারিওন']
        },
        "correct": 0,
        "expl_en": 'Some hyphae are continuous tubes filled with multinucleated cytoplasm—these are called coenocytic hyphae. Others have septa or cross walls in their hyphae.',
        "expl_bn": 'যেসব হাইফায় কোনো প্রস্থপ্রাচীর বা সেপ্টা থাকে না এবং সাইটোপ্লাজমে অসংখ্য নিউক্লিয়াস ছড়ানো থাকে, তাদের সিনোসাইটিক হাইফা বলে।',
    },
    {
        "id": 'BIO-BC-047',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'The cell walls of fungi are characteristically composed of which two primary biochemical substances?',
        "bn": 'ছত্রাকের কোষপ্রাচীর প্রধানত কোন দুটি জৈব রাসায়নিক উপাদান দ্বারা গঠিত?',
        "opts": {
            "en": ['Chitin and polysaccharides', 'Cellulose and pectin', 'Peptidoglycan and teichoic acid', 'Silica and calcium carbonate'],
            "bn": ['কাইটিন (Chitin) এবং পলিস্যাকারাইড', 'সেলুলোজ এবং পেকটিন', 'পেপটিডোগ্লাইক্যান এবং টিকোয়িক অ্যাসিড', 'সিলিকা এবং ক্যালসিয়াম কার্বনেট']
        },
        "correct": 0,
        "expl_en": 'The cell walls of fungi are composed of chitin and polysaccharides.',
        "expl_bn": 'ছত্রাকের কোষপ্রাচীর কাইটিন (Chitin) নামক নাইট্রোজেনযুক্ত পলিস্যাকারাইড দ্বারা গঠিত।',
    },
    {
        "id": 'BIO-BC-048',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'The reserve food materials stored inside fungal cells are predominantly in the form of:',
        "bn": 'ছত্রাকের কোষে সঞ্চিত খাদ্য উপাদান প্রধানত কী হিসেবে জমা থাকে?',
        "opts": {
            "en": ['Glycogen and oil globules', 'Starch and cellulose', 'Floridean starch', 'Laminarin and mannitol'],
            "bn": ['গ্লাইকোজেন এবং তেলের বিন্দু (Glycogen & oil)', 'স্টার্চ এবং সেলুলোজ', 'ফ্লোরিডিয়ান স্টার্চ', 'ল্যামিনারিন এবং ম্যানিটল']
        },
        "correct": 0,
        "expl_en": 'Fungi store reserve food material in the form of glycogen and oil droplets, similar to animal cells.',
        "expl_bn": 'ছত্রাক কোষের প্রধান সঞ্চিত খাদ্য হলো গ্লাইকোজেন এবং চর্বি বা তৈলবিন্দু।',
    },
    {
        "id": 'BIO-BC-049',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Fungi that live as symbionts in mutualistic association with algae are called ________, and those associated with the roots of higher plants are called ________.',
        "bn": 'শৈবালের সাথে মিথোজীবী সম্পর্কে যুক্ত ছত্রাককে ________ বলে এবং উচ্চতর উদ্ভিদের মূলের সাথে যুক্ত ছত্রাককে ________ বলে।',
        "opts": {
            "en": ['Lichens; Mycorrhiza', 'Mycorrhiza; Lichens', 'Haustoria; Epiphytes', 'Myxomycetes; Phycomycetes'],
            "bn": ['লাইকেন (Lichens); মাইকোরাইজা (Mycorrhiza)', 'মাইকোরাইজা; লাইকেন', 'হস্টোরিয়া; এপিফাইট', 'মিক্সোমাইসিটিস; ফাইকোমাইসিটিস']
        },
        "correct": 0,
        "expl_en": 'Fungi can live as symbionts—in association with algae as lichens and with roots of higher plants (e.g., Pinus) as mycorrhiza.',
        "expl_bn": 'শৈবাল ও ছত্রাকের মিথোজীবী রূপ হলো লাইকেন এবং উন্নত উদ্ভিদের মূলের সাথে ছত্রাকের মিথোজীবী রূপ হলো মাইকোরাইজা।',
    },
    {
        "id": 'BIO-BC-050',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'The sexual cycle in fungi involves three sequential events. What is the correct chronological sequence?',
        "bn": 'ছত্রাকের যৌন প্রজনন চক্রে তিনটি ঘটনা নির্দিষ্ট পর্যায়ক্রমে ঘটে। সঠিক পর্যায়ক্রমটি কোনটি?',
        "opts": {
            "en": ['Plasmogamy → Karyogamy → Meiosis', 'Karyogamy → Plasmogamy → Meiosis', 'Meiosis → Plasmogamy → Karyogamy', 'Plasmogamy → Meiosis → Karyogamy'],
            "bn": ['প্লাজমোগ্যামি → ক্যারিওগ্যামি → মিয়োসিস', 'ক্যারিওগ্যামি → প্লাজমোগ্যামি → মিয়োসিস', 'মিয়োসিস → প্লাজমোগ্যামি → ক্যারিওগ্যামি', 'প্লাজমোগ্যামি → মিয়োসিস → ক্যারিওগ্যামি']
        },
        "correct": 0,
        "expl_en": 'The sexual cycle in fungi involves three steps: 1. Fusion of protoplasms between two motile or non-motile gametes called plasmogamy. 2. Fusion of two nuclei called karyogamy. 3. Meiosis in zygote resulting in haploid spores.',
        "expl_bn": 'ছত্রাকের যৌন জননের সঠিক পর্যায়ক্রম: প্রথমে দুটি প্রোটোপ্লাজমের মিলন (প্লাজমোগ্যামি), এরপর নিউক্লিয়াসের মিলন (ক্যারিওগ্যামি) এবং শেষে জাইগোটে মিয়োসিস বিভাজন।',
    },
    {
        "id": 'BIO-BC-051',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'In fungi belonging to Ascomycetes and Basidiomycetes, an intervening stage between plasmogamy and karyogamy where each cell contains two unfused nuclei (n + n) is called:',
        "bn": 'অ্যাসকোমাইসিটিস ও ব্যাসিডিওমাইসিটিস ছত্রাকে প্লাজমোগ্যামির পর কিন্তু ক্যারিওগ্যামির পূর্বে প্রতিটি কোষে দুটি অবিচ্ছিন্ন নিউক্লিয়াস (n + n) অবস্থান করার দশাকে কী বলে?',
        "opts": {
            "en": ['Dikaryophase (Dikaryon stage)', 'Diplophase', 'Aplanospore phase', 'Haplontic syncytium'],
            "bn": ['ডাইক্যারিওদশা বা ডাইক্যারিওন (Dikaryophase / n + n)', 'ডিপ্লোদশা', 'অ্যাপ্ল্যানোস্পোর দশা', 'হ্যাপ্লন্টিক সিনসিটিয়াম']
        },
        "correct": 0,
        "expl_en": 'In ascomycetes and basidiomycetes, an intervening dikaryotic stage (n + n, i.e., two nuclei per cell) occurs; such a condition is called a dikaryon and the phase is called dikaryophase of fungus.',
        "expl_bn": 'অ্যাসকোমাইসিটিস ও ব্যাসিডিওমাইসিটিস ছত্রাকে অবিলম্বে ক্যারিওগ্যামি না ঘটে কোষে দুটি পৃথক নিউক্লিয়াস (n + n) অবস্থান করে, যাকে ডাইক্যারিওদশা বলে।',
    },
    {
        "id": 'BIO-BC-052',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Members of Phycomycetes are found in aquatic habitats, on decaying wood in moist damp places, or as obligate parasites on plants. The mycelium of Phycomycetes is:',
        "bn": 'ফাইকোমাইসিটিসের সদস্যরা জলজ পরিবেশে, স্যাঁতসেঁতে ভেজা কাঠে বা উদ্ভিদে পরজীবী হিসেবে বাস করে। এদের মাইসেলিয়াম কেমন হয়?',
        "opts": {
            "en": ['Aseptate and coenocytic', 'Branched and septate', 'Unicellular and flagellated', 'Pseudoparenchymatous and dikaryotic'],
            "bn": ['প্রস্থপ্রাচীরহীন এবং সিনোসাইটিক (Aseptate & coenocytic)', 'শাখান্বিত এবং সেপ্টামযুক্ত (Septate)', 'এককোষী এবং ফ্ল্যাজেলাযুক্ত', 'সিউডোপ্যারেনকাইমাযুক্ত ও ডাইক্যারিওটিক']
        },
        "correct": 0,
        "expl_en": 'The mycelium in Phycomycetes is aseptate and coenocytic. Asexual reproduction takes place by zoospores (motile) or by aplanospores (non-motile).',
        "expl_bn": 'ফাইকোমাইসিটিসের মাইসেলিয়াম প্রস্থপ্রাচীরহীন (aseptate) এবং বহুনিউক্লিয়াসময় সিনোসাইটিক (coenocytic) প্রকৃতির হয়।',
    },
    {
        "id": 'BIO-BC-053',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'In Phycomycetes, asexual reproduction takes place by motile ________ or by non-motile ________ produced endogenously in sporangia.',
        "bn": 'ফাইকোমাইসিটিসে স্পোরাঞ্জিয়ামে অন্তর্জনুভাবে উৎপন্ন চলনক্ষম ________ অথবা নিশ্চল ________ দ্বারা অযৌন জনন সম্পন্ন হয়।',
        "opts": {
            "en": ['zoospores; aplanospores', 'conidia; ascospores', 'basidiospores; oospores', 'akinetes; heterocysts'],
            "bn": ['জুস্পোর (Zoospores); অ্যাপ্ল্যানোস্পোর (Aplanospores)', 'কনিডিয়া; অ্যাসকোস্পোর', 'ব্যাসিডিওস্পোর; ঊস্পোর', 'অ্যাকাইনিটস; হেটারোসিস্ট']
        },
        "correct": 0,
        "expl_en": 'In Phycomycetes, asexual reproduction takes place by flagellated motile zoospores or by non-motile aplanospores. These spores are endogenously produced in sporangium.',
        "expl_bn": 'ফাইকোমাইসিটিসে চলনক্ষম জুস্পোর এবং নিশ্চল অ্যাপ্ল্যানোস্পোর স্পোরাঞ্জিয়ামের ভেতরে অন্তর্জনুভাবে (endogenously) তৈরি হয়।',
    },
    {
        "id": 'BIO-BC-054',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": "Which of the following common fungi is an example of Phycomycetes causing 'white rust of mustard'?",
        "bn": "নিচের কোন ফাইকোমাইসিটিস ছত্রাকটি সরিষা গাছের 'শ্বেত মরচে' (White rust of mustard) রোগ সৃষ্টির জন্য দায়ী?",
        "opts": {
            "en": ['Albugo candida', 'Rhizopus stolonifer', 'Mucor mucedo', 'Puccinia graminis'],
            "bn": ['অ্যালবুগো ক্যানডিডা (Albugo)', 'রাইজোপাস', 'মিউকর', 'পাকসিনিয়া']
        },
        "correct": 0,
        "expl_en": 'Albugo is the parasitic fungus on mustard causing white rust. Mucor, Rhizopus (the bread mould) and Albugo are examples of Phycomycetes.',
        "expl_bn": 'Albugo হলো ফাইকোমাইসিটিসের একটি সদস্য যা সরিষার পাতায় শ্বেত মরচে বা সাদা দাগের রোগ সৃষ্টি করে।',
    },
    {
        "id": 'BIO-BC-055',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Ascomycetes are commonly known as:',
        "bn": 'অ্যাসকোমাইসিটিস (Ascomycetes) ছত্রাককে সাধারণভাবে কী বলা হয়?',
        "opts": {
            "en": ['Sac-fungi', 'Club-fungi', 'Imperfect fungi', 'Algal-fungi'],
            "bn": ['থলি-ছত্রাক বা স্যাক-ফাংগাই (Sac-fungi)', 'ক্লাব-ফাংগাই', 'অপূর্ণাঙ্গ ছত্রাক', 'শৈবাল ছত্রাক']
        },
        "correct": 0,
        "expl_en": 'Commonly known as sac-fungi, the ascomycetes are mostly multicellular (e.g., Penicillium) or rarely unicellular (e.g., yeast Saccharomyces).',
        "expl_bn": "অ্যাসকোমাইসিটিসকে থলির মতো দেখতে অ্যাসকাসের উপস্থিতির কারণে 'স্যাক-ফাংগাই' বা থলি-ছত্রাক বলা হয়।",
    },
    {
        "id": 'BIO-BC-056',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Fungi that thrive and grow specifically on animal dung are scientifically referred to as:',
        "bn": 'যেসব ছত্রাক বিশেষভাবে গোবর বা প্রাণীর মলের ওপর জন্মায় তাদের বৈজ্ঞানিকভাবে কী বলা হয়?',
        "opts": {
            "en": ['Coprophilous', 'Epiphytic', 'Halophilic', 'Lithotrophic'],
            "bn": ['কপ্রোফিলাস (Coprophilous)', 'এপিফাইটিক', 'হ্যালোফিলিক', 'লিথোট্রফিক']
        },
        "correct": 0,
        "expl_en": 'Ascomycetes are saprophytic, decomposers, parasitic or coprophilous (growing on dung).',
        "expl_bn": "প্রাণীর মলের ওপর জন্মানো ছত্রাকদের 'কপ্রোফিলাস' (Coprophilous) বলা হয়।",
    },
    {
        "id": 'BIO-BC-057',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'In Ascomycetes, the asexual spores are ________ produced ________, whereas the sexual spores are ________ produced ________.',
        "bn": 'অ্যাসকোমাইসিটিসে অযৌন রেণু হলো ________ যা উৎপন্ন হয় ________, এবং যৌন রেণু হলো ________ যা উৎপন্ন হয় ________।',
        "opts": {
            "en": ['conidia produced exogenously; ascospores produced endogenously', 'ascospores produced endogenously; conidia produced exogenously', 'zoospores produced exogenously; basidiospores produced endogenously', 'conidia produced endogenously; aplanospores produced exogenously'],
            "bn": ['কনিডিয়া যা বহির্জনুভাবে উৎপন্ন হয়; অ্যাসকোস্পোর যা অন্তর্জনুভাবে উৎপন্ন হয়', 'অ্যাসকোস্পোর যা অন্তর্জনুভাবে উৎপন্ন হয়; কনিডিয়া যা বহির্জনুভাবে উৎপন্ন হয়', 'জুস্পোর যা বহির্জনুভাবে উৎপন্ন হয়; ব্যাসিডিওস্পোর যা অন্তর্জনুভাবে উৎপন্ন হয়', 'কনিডিয়া যা অন্তর্জনুভাবে উৎপন্ন হয়; অ্যাপ্ল্যানোস্পোর যা বহির্জনুভাবে উৎপন্ন হয়']
        },
        "correct": 0,
        "expl_en": 'In Ascomycetes, asexual spores are conidia produced EXOGENOUSLY on the special mycelium called conidiophores. Sexual spores are ascospores which are produced ENDOGENOUSLY in sac-like asci.',
        "expl_bn": 'অ্যাসকোমাইসিটিসে কনিডিয়া কনিডিওফোরের ওপর বহির্জনুভাবে (exogenously) তৈরি হয়, কিন্তু যৌন অ্যাসকোস্পোর থলি আকৃতির অ্যাসকাসের ভেতরে অন্তর্জনুভাবে (endogenously) তৈরি হয়।',
    },
    {
        "id": 'BIO-BC-058',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": "Which ascomycete fungus is extensively used in biochemical and genetic research, earning the moniker 'Drosophila of the plant kingdom'?",
        "bn": "কোন অ্যাসকোমাইসিটিস ছত্রাকটি জৈব রাসায়নিক ও বংশগতি গবেষণায় বহুল ব্যবহৃত হওয়ায় তাকে 'উদ্ভিদ জগতের ড্রসোফিলা' বলা হয়?",
        "opts": {
            "en": ['Neurospora crassa', 'Aspergillus niger', 'Claviceps purpurea', 'Penicillium notatum'],
            "bn": ['নিউরোস্পোরা (Neurospora)', 'অ্যাসপারজিলাস', 'ক্লাভিসেপস', 'পেনিসিলিয়াম']
        },
        "correct": 0,
        "expl_en": 'Neurospora is used extensively in biochemical and genetic work. Many members like morels and truffles are edible and are considered delicacies.',
        "expl_bn": 'Neurospora ছত্রাকটি জেনেটিক্স ও জৈব রসায়নে বিপুল গবেষণার জন্য ব্যবহৃত হওয়ায় অত্যন্ত বিখ্যাত।',
    },
    {
        "id": 'BIO-BC-059',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Edible delicacies like morels and truffles belong to which taxonomic class of fungi?',
        "bn": 'মরচেলা (Morels) এবং ট্রাফেলস (Truffles)-এর মতো সুস্বাদু ভোজ্য ছত্রাক কোন শ্রেণীর অন্তর্ভুক্ত?',
        "opts": {
            "en": ['Ascomycetes', 'Basidiomycetes', 'Phycomycetes', 'Deuteromycetes'],
            "bn": ['অ্যাসকোমাইসিটিস (Ascomycetes)', 'ব্যাসিডিওমাইসিটিস', 'ফাইকোমাইসিটিস', 'ডিউটেরোমাইসিটিস']
        },
        "correct": 0,
        "expl_en": 'Morels and truffles belong to Ascomycetes; they are edible delicacies and prized across global cuisines.',
        "expl_bn": 'মরচেলা এবং ট্রাফেলস হলো অ্যাসকোমাইসিটিস শ্রেণীর অত্যন্ত দামি ও সুস্বাদু খাদ্যোপযোগী ছত্রাক।',
    },
    {
        "id": 'BIO-BC-060',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Mushrooms, bracket fungi, and puffballs commonly belong to which class of fungi?',
        "bn": 'মাশরুম বা ব্যাঙের ছাতা, ব্র্যাকেট ফাংগাই এবং পাফবল কোন শ্রেণীর অন্তর্ভুক্ত ছত্রাক?',
        "opts": {
            "en": ['Basidiomycetes', 'Ascomycetes', 'Phycomycetes', 'Deuteromycetes'],
            "bn": ['ব্যাসিডিওমাইসিটিস (Basidiomycetes)', 'অ্যাসকোমাইসিটিস', 'ফাইকোমাইসিটিস', 'ডিউটেরোমাইসিটিস']
        },
        "correct": 0,
        "expl_en": 'Commonly known forms of basidiomycetes are mushrooms, bracket fungi or puffballs. They grow in soil, on logs and tree stumps and in living plant bodies as parasites (rusts and smuts).',
        "expl_bn": 'মাশরুম, ব্র্যাকেট ছত্রাক ও পাফবল হলো ব্যাসিডিওমাইসিটিসের প্রধান রূপ।',
    },
    {
        "id": 'BIO-BC-061',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'In Basidiomycetes, sex organs are absent, but plasmogamy is accomplished by:',
        "bn": 'ব্যাসিডিওমাইসিটিস ছত্রাকে কোনো জননাঙ্গ থাকে না, তাহলে এদের প্লাজমোগ্যামি কীভাবে সম্পন্ন হয়?',
        "opts": {
            "en": ['Fusion of two vegetative or somatic cells of different strains or genotypes', 'Oogamous fertilisation by swimming antherozoids in archegonia', 'Isogamous motile biflagellate planogametes', 'Direct wind pollination of free conidia'],
            "bn": ['ভিন্ন স্ট্রেন বা জেনোটাইপের দুটি সোমাটিক বা অঙ্গজ কোষের মিলনের মাধ্যমে', 'আর্কিগোনিয়ামে শুক্রাণুর সঞ্চালনে ঊগ্যামাস মিলন', 'চলনক্ষম দ্বি-ফ্ল্যাজেলাযুক্ত সমগ্যামেটের মিলন', 'কনিডিয়ার সরাসরি পরাগযোগ']
        },
        "correct": 0,
        "expl_en": 'In Basidiomycetes, sex organs are absent, but plasmogamy is brought about by fusion of two vegetative or somatic cells of different strains or genotypes. The resultant structure is dikaryotic which ultimately gives rise to basidium.',
        "expl_bn": 'ব্যাসিডিওমাইসিটিসে কোনো নির্দিষ্ট জননাঙ্গ থাকে না; ভিন্ন স্ট্রেনের দুটি দেহকোষ বা সোমাটিক কোষের মিলনে প্লাজমোগ্যামি ঘটে।',
    },
    {
        "id": 'BIO-BC-062',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'In Basidiomycetes, karyogamy and meiosis take place inside the basidium, producing how many basidiospores and in which spatial manner?',
        "bn": 'ব্যাসিডিওমাইসিটিসে ব্যাসিডিওমের ভেতর ক্যারিওগ্যামি ও মিয়োসিস সম্পন্ন হয়ে কয়টি ব্যাসিডিওস্পোর এবং কীভাবে উৎপন্ন হয়?',
        "opts": {
            "en": ['Four basidiospores produced exogenously', 'Eight basidiospores produced endogenously', 'Four basidiospores produced endogenously', 'Two basidiospores produced exogenously'],
            "bn": ['চারটি ব্যাসিডিওস্পোর যা বহির্জনুভাবে (exogenously) উৎপন্ন হয়', 'আটটি ব্যাসিডিওস্পোর যা অন্তর্জনুভাবে উৎপন্ন হয়', 'চারটি ব্যাসিডিওস্পোর যা অন্তর্জনুভাবে উৎপন্ন হয়', 'দুটি ব্যাসিডিওস্পোর যা বহির্জনুভাবে উৎপন্ন হয়']
        },
        "correct": 0,
        "expl_en": 'Karyogamy and meiosis take place in the basidium producing four basidiospores. The basidiospores are EXOGENOUSLY produced on the basidium.',
        "expl_bn": 'ব্যাসিডিওমাইসিটিসে ক্যারিওগ্যামি ও মিয়োসিসের ফলে ব্যাসিডিয়ামের অগ্রভাগে বহির্জনুভাবে (exogenously) চারটি ব্যাসিডিওস্পোর তৈরি হয়।',
    },
    {
        "id": 'BIO-BC-063',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Which of the following sets of fungi belong to Class Basidiomycetes?',
        "bn": 'নিচের কোন ছত্রাক দলটির সদস্যরা সকলেই ব্যাসিডিওমাইসিটিস শ্রেণীর অন্তর্ভুক্ত?',
        "opts": {
            "en": ['Agaricus (mushroom), Ustilago (smut), and Puccinia (rust)', 'Mucor, Rhizopus, and Albugo', 'Penicillium, Aspergillus, and Claviceps', 'Alternaria, Colletotrichum, and Trichoderma'],
            "bn": ['অ্যাগারিকাস (মাশরুম), উস্টিলাগো (স্মাট) এবং পাকসিনিয়া (রাস্ট)', 'মিউকর, রাইজোপাস এবং অ্যালবুগো', 'পেনিসিলিয়াম, অ্যাসপারজিলাস এবং ক্লাভিসেপস', 'অল্টারনারিয়া, কোলেটোট্রিকাম এবং ট্রাইকোডার্মা']
        },
        "correct": 0,
        "expl_en": 'Common examples of Basidiomycetes are Agaricus (mushroom), Ustilago (smut) and Puccinia (rust fungus).',
        "expl_bn": 'অ্যাগারিকাস (মাশরুম), উস্টিলাগো (স্মাট রোগ সৃষ্টিকারী) এবং পাকসিনিয়া (মরিচা বা রাস্ট সৃষ্টিকারী) হলো ব্যাসিডিওমাইসিটিসের সদস্য।',
    },
    {
        "id": 'BIO-BC-064',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": "Deuteromycetes are commonly called 'imperfect fungi' because:",
        "bn": "ডিউটেরোমাইসিটিস (Deuteromycetes)-কে সাধারণভাবে 'অপূর্ণাঙ্গ ছত্রাক' (Imperfect fungi) বলা হয়, কারণ:",
        "opts": {
            "en": ['Only the asexual or vegetative phases of these fungi are known, while sexual stages are absent or undiscovered', 'Their mycelium lacks a nuclei and cell membrane', 'They can never reproduce even by asexual conidia', 'They only parasitize imperfect flower organs'],
            "bn": ['কেবলমাত্র এদের অযৌন বা অঙ্গজ দশা জানা আছে, কিন্তু এদের কোনো যৌন দশা দেখা যায়নি বা আবিষ্কৃত হয়নি', 'এদের মাইসেলিয়ামে নিউক্লিয়াস বা কোষপর্দা থাকে না', 'এরা কখনোই অযৌন কনিডিয়া দ্বারাও বংশবৃদ্ধি করতে পারে না', 'এরা কেবল অপূর্ণাঙ্গ ফুলের ওপর পরজীবী হিসেবে জন্মায়']
        },
        "correct": 0,
        "expl_en": 'Deuteromycetes are commonly known as imperfect fungi because only the asexual or vegetative phases of these fungi are known. When the sexual forms were discovered, they were moved into Ascomycetes or Basidiomycetes.',
        "expl_bn": 'ডিউটেরোমাইসিটিসের কোনো পরিচিত যৌন দশা নেই, কেবল অযৌন দশা লক্ষ্য করা যায় বলেই এদের অপূর্ণাঙ্গ ছত্রাক (Imperfect fungi) বলা হয়।',
    },
    {
        "id": 'BIO-BC-065',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'A large number of members of Deuteromycetes play a vital terrestrial ecological role as:',
        "bn": 'ডিউটেরোমাইসিটিসের বহুসংখ্যক সদস্য স্থলজ বাস্তুতন্ত্রে কোন গুরুত্বপূর্ণ ভূমিকা পালন করে?',
        "opts": {
            "en": ['Decomposers of litter that help significantly in mineral cycling', 'Primary photosynthetic carbon fixers in desert sands', 'Nitrogen-fixing root nodule endosymbionts', 'Producers of atmospheric molecular oxygen'],
            "bn": ['উদ্ভিজ্জ আবর্জনার বিয়োজক হিসেবে যা খনিজ মৌল চক্রাবর্তনে প্রধান ভূমিকা নেয়', 'মরুভূমির প্রধান সালোকসংশ্লেষী উৎপাদক হিসেবে', 'মূলে নাইট্রোজেন সংবন্ধনকারী মিথোজীবী হিসেবে', 'বায়ুমণ্ডলের আণবিক অক্সিজেন উৎপাদক হিসেবে']
        },
        "correct": 0,
        "expl_en": 'Some members are saprophytes or parasites while a large number of them are decomposers of litter and help in mineral cycling. Examples: Alternaria, Colletotrichum and Trichoderma.',
        "expl_bn": 'ডিউটেরোমাইসিটিসের অধিকাংশ সদস্যই হলো মাটির আবর্জনার বিয়োজক, যা খনিজ পুষ্টির চক্রাবর্তন অব্যাহত রাখতে অত্যন্ত গুরুত্বপূর্ণ।',
    },
    {
        "id": 'BIO-BC-066',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Which of the following trios of fungal genera belong strictly to Class Deuteromycetes?',
        "bn": 'নিচের কোন তিনটি ছত্রাকের গণ কঠোরভাবে ডিউটেরোমাইসিটিস (Deuteromycetes) শ্রেণীর অন্তর্ভুক্ত?',
        "opts": {
            "en": ['Alternaria, Colletotrichum, and Trichoderma', 'Agaricus, Ustilago, and Puccinia', 'Mucor, Rhizopus, and Albugo', 'Aspergillus, Claviceps, and Neurospora'],
            "bn": ['অল্টারনারিয়া, কোলেটোট্রিকাম এবং ট্রাইকোডার্মা', 'অ্যাগারিকাস, উস্টিলাগো এবং পাকসিনিয়া', 'মিউকর, রাইজোপাস এবং অ্যালবুগো', 'অ্যাসপারজিলাস, ক্লাভিসেপস এবং নিউরোস্পোরা']
        },
        "correct": 0,
        "expl_en": 'Examples of Deuteromycetes are Alternaria (early blight of potato), Colletotrichum (red rot of sugarcane), and Trichoderma.',
        "expl_bn": 'Alternaria, Colletotrichum এবং Trichoderma হলো ডিউটেরোমাইসিটিসের আদর্শ উদাহরণ।',
    },
    {
        "id": 'BIO-BC-067',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": "Why were viruses, viroids, and prions excluded from Whittaker's Five-Kingdom classification system?",
        "bn": 'হুইটেকারের পঞ্চ-রাজ্য শ্রেণীবিন্যাস পদ্ধতিতে ভাইরাস, ভিরয়েড ও প্রিয়নদের কেন স্থান দেওয়া হয়নি?',
        "opts": {
            "en": ['They are acellular / non-cellular entities and are not considered truly living organisms with cellular organization', 'They reproduce only in oceanic hydrothermal volcanic vents', 'They possess prokaryotic 70S ribosomes inside their capsids', 'They were discovered only after the 21st century'],
            "bn": ['এরা অকোষীয় (Acellular) সত্তা এবং এদের কোনো সুনির্দিষ্ট কোষীয় সংগঠন না থাকায় প্রকৃত জীব হিসেবে গণ্য করা হয়নি', 'এরা কেবল সমুদ্রের আগ্নেয় ভেন্টে বংশবৃদ্ধি করে', 'এদের ক্যাপসিডের ভেতরে প্রোক্যারিওটিক 70S রাইবোজোম থাকে', 'এরা একবিংশ শতাব্দীর পর আবিষ্কৃত হয়েছিল']
        },
        "correct": 0,
        "expl_en": "In the five kingdom classification of Whittaker there is no mention of lichens and some acellular organisms like viruses, viroids and prions because they are not truly 'living' if we understand living as those organisms that have a cell structure.",
        "expl_bn": 'হুইটেকার কোষীয় সংগঠনের ওপর ভিত্তি করে শ্রেণীবিন্যাস করেছিলেন; ভাইরাস ও ভিরয়েড অকোষীয় সত্তা হওয়ায় তাদের কোনো রাজ্যে স্থান পাননি।',
    },
    {
        "id": 'BIO-BC-068',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": "The name 'virus' that means venom or poisonous fluid was coined by:",
        "bn": "'ভাইরাস' (Virus) শব্দটি, যার অর্থ বিষ বা বিষাক্ত রস, কার দ্বারা প্রবর্তিত হয়েছিল?",
        "opts": {
            "en": ['Dmitri Ivanowsky / Pasteur', 'W.M. Stanley', 'T.O. Diener', 'Robert Koch'],
            "bn": ['দিমিত্রি আইভানোভস্কি / পাস্তুর', 'ডব্লিউ. এম. স্ট্যানলি', 'টি. ও. ডাইনার', 'রবার্ট কখ']
        },
        "correct": 0,
        "expl_en": 'The name virus that means venom or poisonous fluid was given by Pasteur. Dmitri Ivanowsky (1892) recognized certain microbes as causal organism of the mosaic disease of tobacco.',
        "expl_bn": 'ভাইরাস শব্দের অর্থ বিষাক্ত তরল। ১৮৯২ সালে দিমিত্রি আইভানোভস্কি তামাকের মোজাইক রোগের জন্য দায়ী জীবাণু হিসেবে এদের প্রথম চিহ্নিত করেন।',
    },
    {
        "id": 'BIO-BC-069',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'M.W. Beijerinck (1898) demonstrated that the extract of infected tobacco plants could infect healthy plants, and coined the famous Latin phrase:',
        "bn": '১৮৯৮ সালে এম. ডব্লিউ. বেইজেরিঙ্ক দেখান যে আক্রান্ত তামাকের রস সুস্থ গাছে রোগ সংক্রমণ ঘটাতে পারে এবং তিনি কোন বিখ্যাত ল্যাটিন উক্তিটি করেন?',
        "opts": {
            "en": ['Contagium vivum fluidum (infectious living fluid)', 'Omnis cellula-e cellula', 'Scala naturae', 'Systema vegetabile'],
            "bn": ['Contagium vivum fluidum (সংক্রামক সজীব তরল রস)', 'Omnis cellula-e cellula', 'Scala naturae', 'Systema vegetabile']
        },
        "correct": 0,
        "expl_en": 'M.W. Beijerinck (1898) demonstrated that the extract of the infected plants of tobacco could cause infection in healthy plants and named the new pathogen virus and called the fluid as Contagium vivum fluidum (infectious living fluid).',
        "expl_bn": "বেইজেরিঙ্ক ভাইরাসের সংক্রমণক্ষম রসকে 'Contagium vivum fluidum' বা সংক্রামক সজীব তরল হিসেবে আখ্যায়িত করেন।",
    },
    {
        "id": 'BIO-BC-070',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Who first crystallized viruses in 1935 and demonstrated that viral crystals consist largely of proteins?',
        "bn": '১৯৩৫ সালে কে সর্বপ্রথম ভাইরাসকে কেলাসিত (crystallized) করেন এবং প্রমাণ করেন যে এই কেলাস মূলত প্রোটিন দ্বারা গঠিত?',
        "opts": {
            "en": ['W.M. Stanley', 'Dmitri Ivanowsky', 'M.W. Beijerinck', 'Alexander Fleming'],
            "bn": ['ডব্লিউ. এম. স্ট্যানলি (W.M. Stanley)', 'দিমিত্রি আইভানোভস্কি', 'এম. ডব্লিউ. বেইজেরিঙ্ক', 'আলেকজান্ডার ফ্লেমিং']
        },
        "correct": 0,
        "expl_en": 'W.M. Stanley (1935) showed that viruses could be crystallized and crystals consist largely of proteins. They are inert outside their specific host cell.',
        "expl_bn": 'ডব্লিউ. এম. স্ট্যানলি ১৯৩৫ সালে ভাইরাসকে কেলাসিত করে নোবেল পুরস্কার পান এবং দেখান যে এর কেলাস মূলত প্রোটিন।',
    },
    {
        "id": 'BIO-BC-071',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'A virus is chemically a nucleoprotein whose genetic material is infectious. In any given virus, the genetic material consists of:',
        "bn": 'রাসায়নিকভাবে ভাইরাস একটি নিউক্লিওপ্রোটিন যার জিনগত অংশটি সংক্রামক। যেকোনো একটি ভাইরাসে জিনগত পদার্থ হিসেবে কী উপস্থিত থাকে?',
        "opts": {
            "en": ['Either DNA or RNA, but never both simultaneously', 'Both DNA and RNA together at all times', 'Only high molecular weight RNA without exceptions', 'Double-stranded DNA intertwined with ribosomal RNA'],
            "bn": ['হয় DNA অথবা RNA, কিন্তু কখনোই দুটি একসাথে নয়', 'সর্বদাই DNA এবং RNA উভয়ই একসাথে', 'ব্যতিক্রমহীনভাবে কেবল ভারী আণবিক ওজনের RNA', 'রাইবোজোমাল RNA-র সাথে পেঁচানো দ্বি-তন্ত্রী DNA']
        },
        "correct": 0,
        "expl_en": 'NCERT explicitly stresses: In addition to proteins, viruses also contain genetic material, which could be either RNA or DNA. No virus contains both RNA and DNA.',
        "expl_bn": 'NCERT-র মূল বক্তব্য: ভাইরাসে হয় DNA থাকে অথবা RNA থাকে; কোনো ভাইরাসে কখনোই DNA এবং RNA উভয়টি একসাথে থাকে না।',
    },
    {
        "id": 'BIO-BC-072',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'In general, viruses that infect plants possess which type of nucleic acid genome?',
        "bn": 'সাধারণভাবে যেসব ভাইরাস উদ্ভিদকে আক্রমণ ও সংক্রামিত করে, তাদের জিনোম মূলত কেমন প্রকৃতির হয়?',
        "opts": {
            "en": ['Single-stranded RNA (ssRNA)', 'Double-stranded DNA (dsDNA)', 'Circular closed double-stranded RNA', 'Linear double-stranded RNA only'],
            "bn": ['এক-তন্ত্রী আরএনএ (Single-stranded RNA / ssRNA)', 'দ্বি-তন্ত্রী ডিএনএ (dsDNA)', 'বৃত্তাকার দ্বি-তন্ত্রী আরএনএ', 'রৈখিক দ্বি-তন্ত্রী আরএনএ']
        },
        "correct": 0,
        "expl_en": 'In general, viruses that infect plants have single stranded RNA (e.g., Tobacco Mosaic Virus).',
        "expl_bn": 'সাধারণত উদ্ভিদ আক্রমণকারী ভাইরাসগুলির জিনগত পদার্থ এক-তন্ত্রী আরএনএ (ssRNA) হয় (যেমন TMV)।',
    },
    {
        "id": 'BIO-BC-073',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Bacteriophages (viruses that infect bacteria) are usually characterized by having which genetic genome?',
        "bn": 'ব্যাকটেরিওফায (ব্যাকটেরিয়া আক্রমণকারী ভাইরাস)-এর জিনগত উপাদান সাধারণত কী ধরনের হয়?',
        "opts": {
            "en": ['Double-stranded DNA (dsDNA)', 'Single-stranded RNA (ssRNA)', 'Single-stranded DNA (ssDNA)', 'Triple-stranded hybrid DNA-RNA'],
            "bn": ['দ্বি-তন্ত্রী ডিএনএ (Double-stranded DNA / dsDNA)', 'এক-তন্ত্রী আরএনএ (ssRNA)', 'এক-তন্ত্রী ডিএনএ (ssDNA)', 'ত্রি-তন্ত্রী হাইব্রিড ডিএনএ-আরএনএ']
        },
        "correct": 0,
        "expl_en": 'Bacterial viruses or bacteriophages (viruses that infect bacteria) are usually double stranded DNA viruses (e.g., T4 phage, Lambda phage).',
        "expl_bn": 'ব্যাকটেরিওফায বা ব্যাকটেরিয়ার আক্রমণকারী ভাইরাসগুলি সাধারণত দ্বি-তন্ত্রী ডিএনএ (dsDNA) ভাইরাস হয়।',
    },
    {
        "id": 'BIO-BC-074',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'The protein coat of a virus that encloses and protects its central nucleic acid is called the ________, which is composed of small repeating subunits called ________.',
        "bn": 'ভাইরাসের নিউক্লিক অ্যাসিডকে বেষ্টন করে রাখা সুরক্ষাকারী প্রোটিন আবরণকে ________ বলে, যা ________ নামক ক্ষুদ্র পুনরাবৃত্তিমূলক একক দ্বারা গঠিত।',
        "opts": {
            "en": ['Capsid; capsomeres', 'Pellicle; peplomers', 'Envelope; viroids', 'Capsule; peptidoglycans'],
            "bn": ['ক্যাপসিড (Capsid); ক্যাপসোমিয়ার (Capsomeres)', 'পেলিকল; পেপলোমিয়ার', 'এনভেলপ; ভিরয়েড', 'ক্যাপসুল; পেপটিডোগ্লাইক্যান']
        },
        "correct": 0,
        "expl_en": 'The protein coat called capsid made of small subunits called capsomeres, protects the nucleic acid. These capsomeres are arranged in helical or polyhedral geometric forms.',
        "expl_bn": 'ভাইরাসের প্রোটিন আবরণকে ক্যাপসিড বলে এবং এর প্রতিটি ক্ষুদ্র উপ-একককে ক্যাপসোমিয়ার (Capsomeres) বলা হয়।',
    },
    {
        "id": 'BIO-BC-075',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Which of the following human diseases is NOT caused by a virus?',
        "bn": 'নিচের কোন মানব রোগটি ভাইরাসঘটিত সংক্রমণ নয়?',
        "opts": {
            "en": ['Typhoid', 'Mumps', 'Smallpox', 'Herpes and Influenza'],
            "bn": ['টাইফয়েড (Typhoid)', 'মাম্পস (Mumps)', 'গুটিবসন্ত (Smallpox)', 'হারপিস এবং ইনফ্লুয়েঞ্জা']
        },
        "correct": 0,
        "expl_en": 'Typhoid is caused by the bacterium Salmonella typhi. Mumps, smallpox, herpes, influenza, and AIDS are viral diseases in humans.',
        "expl_bn": 'টাইফয়েড হলো সালমোনেলা টাইফি নামক ব্যাকটেরিয়া দ্বারা সৃষ্ট রোগ। অপরপক্ষে মাম্পস, গুটিবসন্ত, হারপিস ও ইনফ্লুয়েঞ্জা ভাইরাসঘটিত।',
    },
    {
        "id": 'BIO-BC-076',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Common symptoms of viral infection in cultivated plants include:',
        "bn": 'চাষকৃত ফসলি উদ্ভিদে ভাইরাস সংক্রমণের সাধারণ লক্ষণগুলির মধ্যে কোনগুলি অন্তর্ভুক্ত?',
        "opts": {
            "en": ['Mosaic formation, leaf rolling and curling, yellowing and vein clearing, dwarfing, and stunted growth', 'Excessive lateral root nodule elongation and starch accumulation', 'Spontaneous conversion into heterotrophic carnivorous pitchers', 'Extensive secondary wood thickening without cambium'],
            "bn": ['পাতায় মোজাইক সৃষ্টি, পাতা কুঁকড়ে যাওয়া ও মোচড়ানো, শিরা হলুদ হয়ে যাওয়া, খর্বাকৃতি এবং বৃদ্ধি থমকে যাওয়া', 'মূলে অস্বাভাবিক অর্বুদ গঠন ও শ্বেতসার জমা', 'স্বতঃস্ফূর্তভাবে মাংসাশী উদ্ভিদের কলসে রূপান্তর', 'ক্যাম্বিয়াম ছাড়াই অতিরিক্ত কাঠের সৃষ্টি']
        },
        "correct": 0,
        "expl_en": 'NCERT notes: In plants, the symptoms of viral disease can be mosaic formation, leaf rolling and curling, yellowing and vein clearing, dwarfing and stunted growth.',
        "expl_bn": 'উদ্ভিদে ভাইরাসের সংক্রমণে পাতার মোজাইক রোগ, পাতা কোঁকড়ানো, শিরা স্বচ্ছ বা হলুদ হওয়া এবং বৃদ্ধি স্তব্ধ হয়ে খর্বাকৃতি হওয়ার লক্ষণ প্রকাশ পায়।',
    },
    {
        "id": 'BIO-BC-077',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": "In 1971, T.O. Diener discovered a novel infectious agent smaller than viruses that caused 'potato spindle tuber disease'. This agent was termed a:",
        "bn": "১৯৭১ সালে টি. ও. ডাইনার ভাইরাস অপেক্ষাও ক্ষুদ্রতর এক নতুন সংক্রামক কণা আবিষ্কার করেন যা আলুর 'স্পিন্ডল টিউবার ডিজিজ' ঘটায়; একে কী নাম দেওয়া হয়?",
        "opts": {
            "en": ['Viroid', 'Prion', 'Virion', 'Bacteriophage'],
            "bn": ['ভিরয়েড (Viroid)', 'প্রিয়ন (Prion)', 'ভিরিয়ন (Virion)', 'ব্যাকটেরিওফায']
        },
        "correct": 0,
        "expl_en": 'In 1971, T.O. Diener discovered a new infectious agent that was smaller than viruses and caused potato spindle tuber disease. It was found to be a free RNA; it lacked the protein coat that is found in viruses, hence the name viroid.',
        "expl_bn": '১৯৭১ সালে টি. ও. ডাইনার ভিরয়েড (Viroid) আবিষ্কার করেন, যা আলুর স্পিন্ডল টিউবার রোগ সৃষ্টিকারী প্রোটিনহীন সংক্রামক আরএনএ।',
    },
    {
        "id": 'BIO-BC-078',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'A viroid differs fundamentally from a virus in:',
        "bn": 'ভিরয়েড একটি ভাইরাস থেকে মূলত কোন বৈশিষ্ট্যে পৃথক?',
        "opts": {
            "en": ['Lacking a protein coat (capsid) and consisting solely of free low molecular weight RNA', 'Having a double-stranded DNA enclosed by peptidoglycan', 'Possessing an 80S ribosome inside its lipid envelope', 'Being capable of independent metabolic ATP generation'],
            "bn": ['কোনো প্রোটিন আবরণ (ক্যাপসিড) না থাকা এবং কেবল কম আণবিক ওজনের মুক্ত RNA দ্বারা গঠিত হওয়া', 'পেপটিডোগ্লাইক্যান দ্বারা আবৃত দ্বি-তন্ত্রী DNA থাকা', 'লিপিড পর্দার ভেতরে 80S রাইবোজোম থাকা', 'স্বাধীনভাবে বিপাকীয় শক্তি বা ATP তৈরি করতে পারা']
        },
        "correct": 0,
        "expl_en": 'A viroid is a free RNA molecule that completely lacks the protein coat found in viruses. The RNA of the viroid was of low molecular weight.',
        "expl_bn": 'ভিরয়েডে ভাইরাসের মতো কোনো প্রোটিন ক্যাপসিড থাকে না, এটি কেবলমাত্র কম আণবিক ভরবিশিষ্ট ক্ষতিকর মুক্ত RNA কণা।',
    },
    {
        "id": 'BIO-BC-079',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Prions are notorious infectious agents that cause fatal neurodegenerative diseases. Structurally, prions consist of:',
        "bn": 'প্রিয়ন (Prions) হলো বিপজ্জনক সংক্রামক কণা যা প্রাণিদেহে মারাত্মক স্নায়বিক রোগ ঘটায়। গঠনগতভাবে প্রিয়ন কী দ্বারা গঠিত?',
        "opts": {
            "en": ['Abnormally folded proteins without any detectable nucleic acid genome', 'Free circular single-stranded DNA without proteins', 'Double-stranded RNA wrapped in cellulose envelopes', 'Chitinous crystalline filaments'],
            "bn": ['কোনো নিউক্লিক অ্যাসিডহীন অস্বাভাবিকভাবে ভাঁজ হওয়া প্রোটিন (Abnormally folded protein)', 'প্রোটিনবিহীন মুক্ত বৃত্তাকার এক-তন্ত্রী DNA', 'সেলুলোজ আবরণে মোড়ানো দ্বি-তন্ত্রী RNA', 'কাইটিন নির্মিত স্ফটিকাকার তন্তু']
        },
        "correct": 0,
        "expl_en": 'In modern medicine certain neurological diseases were found to be transmitted by an agent consisting of abnormally folded protein. The agent was similar in size to viruses. These agents were called prions.',
        "expl_bn": 'প্রিয়ন হলো অস্বাভাবিকভাবে ত্রুটিপূর্ণ ভাঁজযুক্ত প্রোটিন কণা, যার মধ্যে কোনো DNA বা RNA থাকে না কিন্তু এরা স্নায়বিক রোগ সংক্রমণ ঘটাতে পারে।',
    },
    {
        "id": 'BIO-BC-080',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": "Bovine Spongiform Encephalopathy (BSE), commonly known as 'mad cow disease' in cattle, and its human analogue Cr-Jacob disease (CJD), are caused by:",
        "bn": "গরুর 'ম্যাড কাউ ডিজিজ' (BSE) এবং মানুষের ক্রুজফেল্ট-জ্যাকব ডিজিজ (CJD) নামক মস্তিষ্ক বিকলকারী রোগ কার দ্বারা ঘটে?",
        "opts": {
            "en": ['Prions', 'Viroids', 'Retroviruses', 'Archaebacteria'],
            "bn": ['প্রিয়ন (Prions)', 'ভিরয়েড (Viroids)', 'রেট্রোভাইরাস', 'আর্কিব্যাকটেরিয়া']
        },
        "correct": 0,
        "expl_en": 'The most notable diseases caused by prions are bovine spongiform encephalopathy (BSE) commonly called mad cow disease in cattle and its analogous variant Cr-Jacob disease (CJD) in humans.',
        "expl_bn": 'গরুর ম্যাড কাউ ডিজিজ এবং মানুষের CJD রোগ প্রিয়ন (Prions) দ্বারা সংক্রামিত হয়।',
    },
    {
        "id": 'BIO-BC-081',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Lichens are mutually symbiotic associations between:',
        "bn": 'লাইকেন (Lichens) হলো কোন দুটি জীবের মধ্যকার পারস্পরিক মিথোজীবী সহাবস্থান?',
        "opts": {
            "en": ['Algae (phycobiont) and Fungi (mycobiont)', 'Fungi and Roots of higher gymnosperms', 'Cyanobacteria and Mosquito larvae', 'Green algae and Protozoans'],
            "bn": ['শৈবাল (Phycobiont) এবং ছত্রাক (Mycobiont)', 'ছত্রাক এবং উন্নত ব্যক্তবীজী উদ্ভিদের মূল', 'সায়ানোব্যাকটেরিয়া এবং মশার লার্ভা', 'সবুজ শৈবাল এবং প্রোটোজোয়া']
        },
        "correct": 0,
        "expl_en": 'Lichens are symbiotic associations, i.e., mutually useful associations, between algae (phycobiont) and fungi (mycobiont).',
        "expl_bn": 'লাইকেন হলো শৈবাল (ফাইকোবায়োন্ট) এবং ছত্রাক (মাইকোবায়োন্ট)-এর মধ্যে গঠিত এক ঘনিষ্ঠ মিথোজীবী সম্পর্ক।',
    },
    {
        "id": 'BIO-BC-082',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'In a lichen association, what is the specific division of physiological labor between the algal partner (phycobiont) and fungal partner (mycobiont)?',
        "bn": 'লাইকেনে শৈবাল উপাদান (Phycobiont) এবং ছত্রাক উপাদানের (Mycobiont) মধ্যে শারীরবৃত্তীয় কাজের সুনির্দিষ্ট বণ্টন কী?',
        "opts": {
            "en": ['Algae synthesize food via photosynthesis, while fungi provide shelter and absorb mineral nutrients and water', 'Fungi synthesize carbohydrates in darkness, while algae provide mechanical anchorage', 'Both partners fix atmospheric nitrogen simultaneously', 'Algae absorb groundwater while fungi protect against herbivores'],
            "bn": ['শৈবাল সালোকসংশ্লেষের মাধ্যমে খাদ্য তৈরি করে, এবং ছত্রাক আশ্রয় দেয় ও খনিজ পুষ্টি ও জল শোষণ করে', 'ছত্রাক অন্ধকারে শর্করা তৈরি করে এবং শৈবাল যান্ত্রিক দৃঢ়তা দেয়', 'উভয় অংশীদারই একইসাথে বায়ুমণ্ডলীয় নাইট্রোজেন সংবন্ধন করে', 'শৈবাল ভূগর্ভস্থ জল শোষণ করে এবং ছত্রাক তৃণভোজী প্রাণীদের হাত থেকে রক্ষা করে']
        },
        "correct": 0,
        "expl_en": 'Algal partner (phycobiont) prepares food for fungi, and fungi (mycobiont) provide shelter and absorb mineral nutrients and water for its partner. So close is their association that if one saw a lichen in nature one would never imagine that they had two different organisms within them.',
        "expl_bn": 'শৈবাল অংশটি সালোকসংশ্লেষে খাদ্য তৈরি করে ছত্রাককে দেয়, আর ছত্রাক অংশটি শৈবালকে আশ্রয় দেয় এবং পরিবেশ থেকে জল ও খনিজ লবণ শোষণ করে সরবরাহ করে।',
    },
    {
        "id": 'BIO-BC-083',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Lichens are exceptionally sensitive bioindicators of which environmental pollutant?',
        "bn": 'লাইকেন কোন পরিবেশগত বায়ুদূষকের প্রতি অত্যন্ত সংবেদনশীল নির্দেশক (bioindicator)?',
        "opts": {
            "en": ['Sulphur dioxide (SO2) pollution', 'Lead (Pb) exhaust fumes', 'Carbon dioxide (CO2)', 'Methane (CH4) gas'],
            "bn": ['সালফার ডাই-অক্সাইড (SO2) বায়ুদূষণ', 'লেড বা সীসাযুক্ত ধোঁয়া', 'কার্বন ডাই-অক্সাইড', 'মিথেন গ্যাস']
        },
        "correct": 0,
        "expl_en": 'Lichens are very good pollution indicators—they do not grow in polluted areas, particularly areas with high sulphur dioxide (SO2) air pollution.',
        "expl_bn": 'লাইকেন সালফার ডাই-অক্সাইড (SO2) বায়ুদূষণের অন্যতম প্রধান জৈব-নির্দেশক; অতিরিক্ত দূষিত নগরাঞ্চলে এরা একেবারেই জন্মাতে পারে না।',
    },
    {
        "id": 'BIO-BC-084',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Which of the following fungal structures is EXOGENOUSLY produced?',
        "bn": 'নিচের কোন ছত্রাকীয় রেণু গঠনটি বহির্জনুভাবে (Exogenously) উৎপন্ন হয়?',
        "opts": {
            "en": ['Basidiospores of Agaricus and Conidia of Aspergillus', 'Ascospores of Neurospora and Zoospores of Albugo', 'Sporangiospores of Rhizopus and Ascospores of Penicillium', 'Aplanospores of Mucor and Ascospores of Claviceps'],
            "bn": ['অ্যাগারিকাসের ব্যাসিডিওস্পোর এবং অ্যাসপারজিলাসের কনিডিয়া', 'নিউরোস্পোরার অ্যাসকোস্পোর এবং অ্যালবুগোর জুস্পোর', 'রাইজোপাসের স্পোরাঞ্জিওস্পোর এবং পেনিসিলিয়ামের অ্যাসকোস্পোর', 'মিউকরের অ্যাপ্ল্যানোস্পোর এবং ক্লাভিসেপসের অ্যাসকোস্পোর']
        },
        "correct": 0,
        "expl_en": 'Both conidia (in Ascomycetes) and basidiospores (in Basidiomycetes) are produced EXOGENOUSLY. In contrast, sporangiospores/zoospores (Phycomycetes) and ascospores (Ascomycetes) are produced ENDOGENOUSLY.',
        "expl_bn": 'অ্যাসকোমাইসিটিসের কনিডিয়া এবং ব্যাসিডিওমাইসিটিসের ব্যাসিডিওস্পোর—উভয়ই দেহের বাইরে বহির্জনুভাবে (Exogenously) তৈরি হয়।',
    },
    {
        "id": 'BIO-BC-085',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Which of the following fungal structures is ENDOGENOUSLY produced?',
        "bn": 'নিচের কোন ছত্রাকীয় রেণুগুলি অঙ্গের অভ্যন্তরে অন্তর্জনুভাবে (Endogenously) উৎপন্ন হয়?',
        "opts": {
            "en": ['Ascospores inside the ascus and sporangiospores inside the sporangium', 'Basidiospores on the basidium and conidia on conidiophores', 'Conidia on sterigmata and basidiospores on basidiocarps', 'Oidia on hyphae and gemmae on thallus'],
            "bn": ['অ্যাসকাসের ভেতরে অ্যাসকোস্পোর এবং স্পোরাঞ্জিয়ামের ভেতরে স্পোরাঞ্জিওস্পোর', 'ব্যাসিডিয়ামের ওপর ব্যাসিডিওস্পোর এবং কনিডিওফোরের ওপর কনিডিয়া', 'স্টেরিগ্রমাটার ওপর কনিডিয়া এবং ব্যাসিডিওকার্পে ব্যাসিডিওস্পোর', 'হাইফায় ওইডিয়া এবং থ্যালাসে জেমা']
        },
        "correct": 0,
        "expl_en": 'Ascospores are produced endogenously in sac-like asci. Zoospores and aplanospores in Phycomycetes are produced endogenously inside sporangia.',
        "expl_bn": 'অ্যাসকাসের ভেতরে অ্যাসকোস্পোর এবং স্পোরাঞ্জিয়ামের ভেতরে জুস্পোর/অ্যাপ্ল্যানোস্পোর অন্তর্জনুভাবে (Endogenously) তৈরি হয়।',
    },
    {
        "id": 'BIO-BC-086',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Statement I: Methanogens are archaebacteria that produce methane gas from the dung of ruminants.\nStatement II: Archaebacteria possess peptidoglycan cell walls identical to that of cyanobacteria.\nChoose the correct option:',
        "bn": 'বিবৃতি I: মিথেনোজেন হলো আর্কিব্যাকটেরিয়া যা রোমন্থক প্রাণীর গোবর থেকে মিথেন গ্যাস তৈরি করে।\nবিবৃতি II: আর্কিব্যাকটেরিয়ায় সায়ানোব্যাকটেরিয়ার অনুরূপ হুবহু পেপটিডোগ্লাইক্যান নির্মিত কোষপ্রাচীর থাকে।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct', 'Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect'],
            "bn": ['বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল']
        },
        "correct": 0,
        "expl_en": 'Statement I is correct. Statement II is incorrect because Archaebacteria lack true peptidoglycan (muramic acid); their cell wall contains pseudomurein and non-cellulosic polysaccharides.',
        "expl_bn": 'বিবৃতি I সঠিক। কিন্তু বিবৃতি II ভুল কারণ আর্কিব্যাকটেরিয়ার প্রাচীরে পেপটিডোগ্লাইক্যান থাকে না (সিউডোমিউরিন থাকে)।',
    },
    {
        "id": 'BIO-BC-087',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Statement I: In diatoms, the cell walls are embedded with silica and are indestructible.\nStatement II: Diatoms are the chief producers in oceanic ecosystems.\nChoose the correct option:',
        "bn": 'বিবৃতি I: ডায়াটমে কোষপ্রাচীর সিলিকা দ্বারা গঠিত এবং অবিনশ্বর।\nবিবৃতি II: ডায়াটম হলো মহাসাগরীয় বাস্তুতন্ত্রের প্রধান উৎপাদক।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct', 'Both Statement I and Statement II are incorrect'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল']
        },
        "correct": 0,
        "expl_en": 'Both Statement I and Statement II are verbatim accurate statements from NCERT Biology.',
        "expl_bn": 'বিবৃতি I এবং বিবৃতি II উভয় তথ্যই NCERT অনুসারে সম্পূর্ণ সঠিক।',
    },
    {
        "id": 'BIO-BC-088',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Statement I: Viroids contain free low molecular weight RNA lacking a protein capsid.\nStatement II: Prions contain abnormally folded DNA molecules that cause bovine spongiform encephalopathy.\nChoose the correct option:',
        "bn": 'বিবৃতি I: ভিরয়েডে কোনো প্রোটিন ক্যাপসিড থাকে না, এটি কম আণবিক ভরের মুক্ত RNA দিয়ে গঠিত।\nবিবৃতি II: প্রিয়ন অস্বাভাবিকভাবে ভাঁজ হওয়া DNA কণা দ্বারা গঠিত যা ম্যাড কাউ ডিজিজ সৃষ্টি করে।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct', 'Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect'],
            "bn": ['বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল']
        },
        "correct": 0,
        "expl_en": 'Statement I is correct. Statement II is incorrect because prions consist of abnormally folded PROTEIN, not DNA.',
        "expl_bn": 'বিবৃতি I সঠিক। কিন্তু বিবৃতি II ভুল কারণ প্রিয়ন হলো অস্বাভাবিক ভাঁজযুক্ত সংক্রামক প্রোটিন, কোনো DNA নয়।',
    },
    {
        "id": 'BIO-BC-089',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Statement I: Mycoplasma are the smallest living cells known and can survive without oxygen.\nStatement II: Mycoplasma are completely resistant to cell-wall synthesis inhibiting antibiotics like penicillin.\nChoose the correct option:',
        "bn": 'বিবৃতি I: মাইকোপ্লাজমা হলো আবিষ্কৃত ক্ষুদ্রতম সজীব কোষ যা অক্সিজেন ছাড়াই বাঁচতে পারে।\nবিবৃতি II: কোষপ্রাচীর সংশ্লেষণে বাধাদানকারী অ্যান্টিবায়োটিক পেনিসিলিনের বিরুদ্ধে মাইকোপ্লাজমা সম্পূর্ণ প্রতিরোধী।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct', 'Both Statement I and Statement II are incorrect'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল']
        },
        "correct": 0,
        "expl_en": 'Both Statement I and Statement II are correct. Since penicillin specifically targets bacterial peptidoglycan cell-wall synthesis and Mycoplasma naturally lacks a cell wall entirely, Mycoplasma is inherently insensitive to penicillin.',
        "expl_bn": 'উভয় বিবৃতিই সঠিক। পেনিসিলিন কোষপ্রাচীর গঠনে বাধা দেয়, কিন্তু মাইকোপ্লাজমায় কোষপ্রাচীরই থাকে না, তাই পেনিসিলিন এদের কোনো ক্ষতি করতে পারে না।',
    },
    {
        "id": 'BIO-BC-090',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Statement I: Heterocysts in Nostoc lack Photosystem II (PS II) to maintain an anaerobic microenvironment for nitrogenase.\nStatement II: Cyanobacteria perform oxygenic photosynthesis using chlorophyll a.\nChoose the correct option:',
        "bn": 'বিবৃতি I: নস্টকের হেটারোসিস্টে ফটোসিস্টেম II (PS II) অনুপস্থিত থাকে যাতে নাইট্রোজিনেজ উৎসেচকের জন্য অবাত পরিবেশ বজায় থাকে।\nবিবৃতি II: সায়ানোব্যাকটেরিয়া ক্লোরোফিল a ব্যবহার করে অক্সিজেনিক সালোকসংশ্লেষ সম্পন্ন করে।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct', 'Both Statement I and Statement II are incorrect'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল']
        },
        "correct": 0,
        "expl_en": 'Both statements are correct. Heterocysts lack oxygen-evolving PS II and have thick walls impermeable to O2, protecting oxygen-sensitive nitrogenase, while vegetative cells perform oxygenic photosynthesis.',
        "expl_bn": 'উভয় বিবৃতি সঠিক। হেটারোসিস্টে অক্সিজেন সংবেদনশীল নাইট্রোজিনেজকে সুরক্ষা দিতে PS II থাকে না এবং ভেজিটেটিভ কোষে ক্লোরোফিল a দ্বারা অক্সিজেনিক সালোকসংশ্লেষ চলে।',
    },
    {
        "id": 'BIO-BC-091',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Yeast and Penicillium belong to Kingdom Fungi.\nReason (R): Both are filamentous fungi having branched and septate coenocytic mycelium.\nChoose the correct option:',
        "bn": 'Assertion (A): ইস্ট এবং পেনিসিলিয়াম উভয়ই ছত্রাক (Fungi) জগতের অন্তর্ভুক্ত।\nReason (R): উভয়ই শাখান্বিত ও প্রস্থপ্রাচীরযুক্ত সিনোসাইটিক মাইসেলিয়ামধারী সূত্রাকার ছত্রাক।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['(A) is true but (R) is false', 'Both (A) and (R) are true and (R) is the correct explanation of (A)', 'Both (A) and (R) are true but (R) is NOT the correct explanation of (A)', '(A) is false but (R) is true'],
            "bn": ['(A) সত্য কিন্তু (R) মিথ্যা', '(A) এবং (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) মিথ্যা কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Assertion (A) is true. Reason (R) is false because yeast (Saccharomyces) is UNICELLULAR and non-filamentous, which is a major exception in Kingdom Fungi.',
        "expl_bn": '(A) সত্য। কিন্তু (R) সম্পূর্ণ মিথ্যা কারণ ইস্ট হলো এককোষী ছত্রাক, এটি সূত্রাকার বা মাইসেলিয়ামযুক্ত নয়।',
    },
    {
        "id": 'BIO-BC-092',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Deuteromycetes are known as imperfect fungi.\nReason (R): Only the asexual or vegetative phases of these fungi are known.\nChoose the correct option:',
        "bn": 'Assertion (A): ডিউটেরোমাইসিটিস ছত্রাককে অপূর্ণাঙ্গ ছত্রাক (Imperfect fungi) বলা হয়।\nReason (R): কেবলমাত্র এদের অযৌন বা অঙ্গজ দশা আবিষ্কৃত হয়েছে।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Both (A) and (R) are true and (R) is the correct explanation of (A)', 'Both (A) and (R) are true but (R) is NOT the correct explanation of (A)', '(A) is true but (R) is false', '(A) is false but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য কিন্তু (R) মিথ্যা', '(A) মিথ্যা কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Both (A) and (R) are true and (R) is the direct textbook explanation: they are called imperfect precisely because their sexual (perfect) stage is not known.',
        "expl_bn": '(A) ও (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক কারণ, কারণ যৌন (পারফেক্ট) দশা অনুপস্থিত বলেই এদের অপূর্ণাঙ্গ ছত্রাক বলা হয়।',
    },
    {
        "id": 'BIO-BC-093',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Lichens do not grow in polluted industrial areas.\nReason (R): Lichens are extremely sensitive to sulphur dioxide (SO2) pollution in the atmosphere.\nChoose the correct option:',
        "bn": 'Assertion (A): দূষিত শিল্পাঞ্চলে লাইকেন একেবারেই জন্মাতে পারে না।\nReason (R): লাইকেন বায়ুমণ্ডলের সালফার ডাই-অক্সাইড (SO2) দূষণের প্রতি অত্যন্ত সংবেদনশীল।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Both (A) and (R) are true and (R) is the correct explanation of (A)', 'Both (A) and (R) are true but (R) is NOT the correct explanation of (A)', '(A) is true but (R) is false', '(A) is false but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য কিন্তু (R) মিথ্যা', '(A) মিথ্যা কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Both (A) and (R) are true and (R) explains (A): SO2 destroys the photosynthetic chlorophyll of the phycobiont in lichens, causing death.',
        "expl_bn": '(A) ও (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা কারণ SO2 শৈবাল উপাদানের ক্লোরোফিল নষ্ট করে দেয়।',
    },
    {
        "id": 'BIO-BC-094',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Viruses are considered an exception to the Cell Theory.\nReason (R): Viruses are acellular entities having an inert crystalline structure outside living host cells.\nChoose the correct option:',
        "bn": 'Assertion (A): ভাইরাসকে কোষতত্ত্বের (Cell Theory) একটি প্রধান ব্যতিক্রম গণ্য করা হয়।\nReason (R): ভাইরাস হলো অকোষীয় সত্তা যা পোষক কোষের বাইরে নিষ্ক্রিয় স্ফটিকাকার অবস্থায় থাকে।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Both (A) and (R) are true and (R) is the correct explanation of (A)', 'Both (A) and (R) are true but (R) is NOT the correct explanation of (A)', '(A) is true but (R) is false', '(A) is false but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য কিন্তু (R) মিথ্যা', '(A) মিথ্যা কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Both (A) and (R) are true and (R) correctly explains (A): Cell theory states that all living organisms are composed of cells, but viruses lack cellular organization completely.',
        "expl_bn": '(A) এবং (R) উভয়ই সত্য এবং কোষতত্ত্বের মূল কথা সমস্ত জীব কোষে গঠিত হলেও ভাইরাসে কোনো কোষীয় গঠন না থাকায় এটি কোষতত্ত্বের ব্যতিক্রম।',
    },
    {
        "id": 'BIO-BC-095',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Archaebacteria can survive under extreme harsh habitats like hot springs and salt pans.\nReason (R): Archaebacteria possess an unusual branched-chain lipid membrane structure that decreases membrane fluidity and permeability.\nChoose the correct option:',
        "bn": 'Assertion (A): আর্কিব্যাকটেরিয়া উষ্ণ প্রস্রবণ ও চরম লবণাক্ত পরিবেশের মতো মারাত্মক প্রতিকূল স্থানে টিকে থাকতে পারে।\nReason (R): আর্কিব্যাকটেরিয়ার কোষপর্দায় অস্বাভাবিক শাখান্বিত লিপিড শৃঙ্খল থাকে যা পর্দার তরলতা ও ক্ষরণযোগ্যতা কমিয়ে প্রতিরোধ ক্ষমতা বাড়ায়।\nসঠিক বিকল্পটি নির্বাচন করো:',
        "opts": {
            "en": ['Both (A) and (R) are true and (R) is the correct explanation of (A)', 'Both (A) and (R) are true but (R) is NOT the correct explanation of (A)', '(A) is true but (R) is false', '(A) is false but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য কিন্তু (R) মিথ্যা', '(A) মিথ্যা কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Both (A) and (R) are true and (R) is the biochemical explanation: the branched ether-linked hydrocarbons in the archaeal cell membrane confer extreme thermal and osmotic stability.',
        "expl_bn": '(A) ও (R) উভয়ই সত্য এবং শাখান্বিত ইথার-যুক্ত লিপিড পর্দা চরম তাপ ও অসমোটিক চাপে কোষপর্দাকে অক্ষুণ্ণ রাখে।',
    },
    {
        "id": 'BIO-BC-096',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Match Column-I (Class of Fungi) with Column-II (Characteristic Feature / Spore Type) and select the correct code:\nColumn-I: (A) Phycomycetes, (B) Ascomycetes, (C) Basidiomycetes, (D) Deuteromycetes\nColumn-II: 1. Exogenous basidiospores on basidium, 2. Aseptate and coenocytic mycelium, 3. No sexual stage known, 4. Endogenous ascospores in sac-like asci',
        "bn": 'কলাম-I (ছত্রাকের শ্রেণী)-এর সাথে কলাম-II (প্রধান বৈশিষ্ট্য)-এর মিল করে সঠিক কোড নির্বাচন করো:\nকলাম-I: (A) Phycomycetes, (B) Ascomycetes, (C) Basidiomycetes, (D) Deuteromycetes\nকলাম-II: 1. বহির্জনুভাবে উৎপন্ন ব্যাসিডিওস্পোর, 2. সিনোসাইটিক ও প্রস্থপ্রাচীরহীন মাইসেলিয়াম, 3. কোনো পরিচিত যৌন দশা নেই, 4. থলির মধ্যে অন্তর্জনুভাবে উৎপন্ন অ্যাসকোস্পোর',
        "opts": {
            "en": ['A-2, B-4, C-1, D-3', 'A-4, B-2, C-1, D-3', 'A-2, B-1, C-4, D-3', 'A-3, B-4, C-1, D-2'],
            "bn": ['A-2, B-4, C-1, D-3', 'A-4, B-2, C-1, D-3', 'A-2, B-1, C-4, D-3', 'A-3, B-4, C-1, D-2']
        },
        "correct": 0,
        "expl_en": 'Phycomycetes = Aseptate & coenocytic mycelium (A-2); Ascomycetes = Endogenous ascospores in asci (B-4); Basidiomycetes = Exogenous basidiospores (C-1); Deuteromycetes = Imperfect fungi with no sexual stage (D-3).',
        "expl_bn": 'Phycomycetes = সিনোসাইটিক মাইসেলিয়াম (A-2); Ascomycetes = থলিতে অন্তর্জনু অ্যাসকোস্পোর (B-4); Basidiomycetes = বহির্জনু ব্যাসিডিওস্পোর (C-1); Deuteromycetes = যৌন দশাহীন অপূর্ণাঙ্গ ছত্রাক (D-3)।',
    },
    {
        "id": 'BIO-BC-097',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Match Column-I (Organism) with Column-II (Scientific Group / Attribute) and select the correct option:\nColumn-I: (A) Gonyaulax, (B) Euglena, (C) Trypanosoma, (D) Diatoms\nColumn-II: 1. Diatomaceous earth & soap-box shell, 2. Red tides, 3. Sleeping sickness, 4. Pellicle & mixotroph',
        "bn": 'কলাম-I এর সাথে কলাম-II মিলিয়ে সঠিক উত্তরটি নির্বাচন করো:\nকলাম-I: (A) Gonyaulax, (B) Euglena, (C) Trypanosoma, (D) Diatoms\nকলাম-II: 1. ডায়াটোমেশিয়াস আর্থ ও সাবানের বাক্সবৎ খোলক, 2. লাল জোয়ার (Red tides), 3. স্লিপিং সিকনেস রোগ, 4. পেলিকল ও মিক্সোট্রফ',
        "opts": {
            "en": ['A-2, B-4, C-3, D-1', 'A-1, B-4, C-3, D-2', 'A-2, B-1, C-3, D-4', 'A-3, B-4, C-2, D-1'],
            "bn": ['A-2, B-4, C-3, D-1', 'A-1, B-4, C-3, D-2', 'A-2, B-1, C-3, D-4', 'A-3, B-4, C-2, D-1']
        },
        "correct": 0,
        "expl_en": 'Gonyaulax = Red tides (A-2); Euglena = Pellicle & mixotrophic nutrition (B-4); Trypanosoma = Sleeping sickness (C-3); Diatoms = Soap-box silica shells & diatomaceous earth (D-1).',
        "expl_bn": 'Gonyaulax = লাল জোয়ার (A-2); Euglena = পেলিকল ও মিক্সোট্রফিক পুষ্টি (B-4); Trypanosoma = স্লিপিং সিকনেস (C-3); Diatoms = ডায়াটোমেশিয়াস আর্থ (D-1)।',
    },
    {
        "id": 'BIO-BC-098',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Match Column-I (Disease) with Column-II (Causative Microorganism) and choose the correct code:\nColumn-I: (A) Citrus canker, (B) Bovine spongiform encephalopathy, (C) Potato spindle tuber disease, (D) Sleeping sickness\nColumn-II: 1. Viroid, 2. Bacterium (Xanthomonas), 3. Prion, 4. Protozoan (Trypanosoma)',
        "bn": 'কলাম-I (রোগ)-এর সাথে কলাম-II (রোগ সৃষ্টিকারী জীবাণু)-এর মিল করো:\nকলাম-I: (A) সাইট্রাস ক্যাঙ্কার, (B) ম্যাড কাউ ডিজিজ (BSE), (C) পটেটো স্পিন্ডল টিউবার, (D) স্লিপিং সিকনেস\nকলাম-II: 1. ভিরয়েড, 2. ব্যাকটেরিয়া, 3. প্রিয়ন, 4. প্রোটোজোয়া',
        "opts": {
            "en": ['A-2, B-3, C-1, D-4', 'A-1, B-3, C-2, D-4', 'A-2, B-1, C-3, D-4', 'A-4, B-3, C-1, D-2'],
            "bn": ['A-2, B-3, C-1, D-4', 'A-1, B-3, C-2, D-4', 'A-2, B-1, C-3, D-4', 'A-4, B-3, C-1, D-2']
        },
        "correct": 0,
        "expl_en": 'Citrus canker = Bacterium Xanthomonas (A-2); BSE / Mad cow = Prion (B-3); Potato spindle tuber = Viroid T.O. Diener (C-1); Sleeping sickness = Protozoan Trypanosoma (D-4).',
        "expl_bn": 'সাইট্রাস ক্যাঙ্কার = ব্যাকটেরিয়া (A-2); BSE = প্রিয়ন (B-3); পটেটো স্পিন্ডল টিউবার = ভিরয়েড (C-1); স্লিপিং সিকনেস = প্রোটোজোয়া (D-4)।',
    },
    {
        "id": 'BIO-BC-099',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Match Column-I (Fungus) with Column-II (Common Name / Economic Role) and select the correct option:\nColumn-I: (A) Puccinia, (B) Ustilago, (C) Claviceps, (D) Saccharomyces\nColumn-II: 1. Smut fungus, 2. Rust fungus, 3. Brewing & baking yeast, 4. Ergot of rye',
        "bn": 'কলাম-I (ছত্রাক)-এর সাথে কলাম-II (সাধারণ নাম বা ভূমিকা) মিলিয়ে নাও:\nকলাম-I: (A) Puccinia, (B) Ustilago, (C) Claviceps, (D) Saccharomyces\nকলাম-II: 1. স্মাট ছত্রাক, 2. মরিচা (রাস্ট) ছত্রাক, 3. বেকারি ও অ্যালকোহল তৈরির ইস্ট, 4. আরগট রোগ সৃষ্টিকারী',
        "opts": {
            "en": ['A-2, B-1, C-4, D-3', 'A-1, B-2, C-4, D-3', 'A-2, B-4, C-1, D-3', 'A-3, B-1, C-4, D-2'],
            "bn": ['A-2, B-1, C-4, D-3', 'A-1, B-2, C-4, D-3', 'A-2, B-4, C-1, D-3', 'A-3, B-1, C-4, D-2']
        },
        "correct": 0,
        "expl_en": "Puccinia = Rust fungus (A-2); Ustilago = Smut fungus (B-1); Claviceps = Ergot of rye (C-4); Saccharomyces = Baker's/Brewer's yeast (D-3).",
        "expl_bn": 'Puccinia = মরিচা বা রাস্ট ছত্রাক (A-2); Ustilago = স্মাট ছত্রাক (B-1); Claviceps = আরগট রোগ (C-4); Saccharomyces = বেকিং ও ব্রিউইং ইস্ট (D-3)।',
    },
    {
        "id": 'BIO-BC-100',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Match Column-I (Scientist) with Column-II (Discovery / Contribution) and choose the correct code:\nColumn-I: (A) R.H. Whittaker, (B) Dmitri Ivanowsky, (C) M.W. Beijerinck, (D) T.O. Diener\nColumn-II: 1. Discovery of Viroids (1971), 2. Five-Kingdom Classification (1969), 3. Discovery of causal microbe of tobacco mosaic (1892), 4. Contagium vivum fluidum (1898)',
        "bn": 'কলাম-I (বিজ্ঞানী)-এর সাথে কলাম-II (আবিষ্কার বা অবদান) মিলিয়ে সঠিক কোডটি নির্বাচন করো:\nকলাম-I: (A) R.H. Whittaker, (B) Dmitri Ivanowsky, (C) M.W. Beijerinck, (D) T.O. Diener\nকলাম-II: 1. ভিরয়েড আবিষ্কার (১৯৭১), 2. পঞ্চ-রাজ্য শ্রেণীবিন্যাস (১৯৬৯), 3. তামাকের মোজাইক রোগের জীবাণু চিহ্নিতকরণ (১৮৯২), 4. Contagium vivum fluidum (১৮৯৮)',
        "opts": {
            "en": ['A-2, B-3, C-4, D-1', 'A-2, B-4, C-3, D-1', 'A-1, B-3, C-4, D-2', 'A-3, B-2, C-4, D-1'],
            "bn": ['A-2, B-3, C-4, D-1', 'A-2, B-4, C-3, D-1', 'A-1, B-3, C-4, D-2', 'A-3, B-2, C-4, D-1']
        },
        "correct": 0,
        "expl_en": 'Whittaker = Five kingdom system (A-2); Ivanowsky = Tobacco mosaic microbe (B-3); Beijerinck = Contagium vivum fluidum (C-4); Diener = Viroid discovery (D-1).',
        "expl_bn": 'হুইটেকার = পঞ্চ-রাজ্য শ্রেণীবিন্যাস (A-2); আইভানোভস্কি = তামাকের মোজাইক জীবাণু (B-3); বেইজেরিঙ্ক = Contagium vivum fluidum (C-4); ডাইনার = ভিরয়েড আবিষ্কার (D-1)।',
    },
    {
        "id": 'BIO-BC-101',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Cyanobacteria bloom frequently in water bodies polluted with domestic sewage, leading to:',
        "bn": 'গৃহস্থালির বর্জ্য দ্বারা দূষিত জলাশয়ে সায়ানোব্যাকটেরিয়ার অত্যধিক বংশবৃদ্ধির (bloom) ফলে কী ঘটে?',
        "opts": {
            "en": ['Deoxygenation of water and release of toxins harmful to aquatic fauna', 'Purification of water making it crystal clear and potable', 'Precipitation of pure calcium carbonate into limestone caves', 'Spontaneous synthesis of oceanic petroleum deposits'],
            "bn": ['জলে দ্রবীভূত অক্সিজেনের ঘাটতি এবং জলজ প্রাণীর জন্য ক্ষতিকর বিষাক্ত পদার্থ নিঃসরণ', 'জল বিশুদ্ধ হয়ে সম্পূর্ণ পানীয় জলে রূপান্তর', 'ক্যালসিয়াম কার্বনেট থিতিয়ে চুনাপাথরে রূপান্তর', 'সমুদ্রের তলদেশে পেট্রোলিয়াম সৃষ্টি']
        },
        "correct": 0,
        "expl_en": 'Cyanobacteria often form blooms in polluted water bodies. These algal blooms deplete dissolved oxygen (eutrophication) and secrete cyanotoxins, causing massive fish mortality.',
        "expl_bn": 'দূষিত জলে সায়ানোব্যাকটেরিয়ার অ্যালগাল ব্লুম জলাশয়ের দ্রবীভূত অক্সিজেন নিঃশেষ করে এবং বিষাক্ত ক্ষরণে মাছ ও জলজ প্রাণীর মৃত্যু ঘটায়।',
    },
    {
        "id": 'BIO-BC-102',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Which of the following organisms completely lacks a cell wall?',
        "bn": 'নিচের কোন জীবটিতে কোনো প্রকার কোষপ্রাচীর একেবারেই থাকে না?',
        "opts": {
            "en": ['Mycoplasma', 'Nostoc', 'Bacillus', 'Cyanobacteria'],
            "bn": ['মাইকোপ্লাজমা (Mycoplasma)', 'নস্টক', 'ব্যাসিলাস', 'সায়ানোব্যাকটেরিয়া']
        },
        "correct": 0,
        "expl_en": 'Mycoplasma are organisms that completely lack a cell wall. They are the smallest living cells known.',
        "expl_bn": 'মাইকোপ্লাজমার কোষে কোনো কোষপ্রাচীর থাকে না।',
    },
    {
        "id": 'BIO-BC-103',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Ciliate protozoans differ from all other protozoans in having:',
        "bn": 'সিলিয়াযুক্ত প্রোটোজোয়া (যেমন Paramecium) অন্য সমস্ত প্রোটোজোয়া থেকে মূলত কোন বৈশিষ্ট্যে পৃথক?',
        "opts": {
            "en": ['Two types of nuclei (macronucleus for vegetative functions and micronucleus for reproduction)', 'A contractile vacuole made of silicon dioxide', 'Pseudopodia for capturing prey in marine sand', 'An undulating flagellum running throughout the body'],
            "bn": ['দুটি ভিন্ন ধরনের নিউক্লিয়াস (শারীরবৃত্তীয় কাজের ম্যাক্রোনিউক্লিয়াস ও জননের মাইক্রোনিউক্লিয়াস)', 'সিলিকা নির্মিত সংকোচনশীল গহ্বর', 'শিকার ধরার জন্য ক্ষণপদ', 'সারা দেহজুড়ে বিস্তৃত একটি ফ্ল্যাজেলাম']
        },
        "correct": 0,
        "expl_en": 'Ciliates like Paramecium exhibit nuclear dualism, possessing a large vegetative polyploid macronucleus and a small diploid reproductive micronucleus.',
        "expl_bn": 'সিলিয়েটদের মধ্যে দ্বি-নিউক্লিয়াসী অবস্থা (Nuclear dualism) থাকে: একটি বড় ম্যাক্রোনিউক্লিয়াস এবং একটি ছোট মাইক্রোনিউক্লিয়াস।',
    },
    {
        "id": 'BIO-BC-104',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Which of the following statements about Euglena is FALSE?',
        "bn": 'ইউগ্লিনা (Euglena) সম্পর্কে নিচের কোন বক্তব্যটি ভুল?',
        "opts": {
            "en": ['It possesses an outer rigid cell wall made of cellulose and pectin', 'It has two flagella, one short and one long', 'It has a protein-rich flexible layer called pellicle', 'Its photosynthetic pigments are identical to those of higher plants'],
            "bn": ['এদের বাইরে সেলুলোজ ও পেকটিন নির্মিত দৃঢ় কোষপ্রাচীর থাকে', 'এদের দুটি ফ্ল্যাজেলা থাকে—একটি ছোট এবং একটি লম্বা', 'এদের প্রোটিনসমৃদ্ধ নমনীয় পেলিকল স্তর থাকে', 'এদের সালোকসংশ্লেষী রঞ্জক উচ্চশ্রেণীর উদ্ভিদের রঞ্জকের অনুরূপ']
        },
        "correct": 0,
        "expl_en": 'Euglena completely lacks a cellulosic cell wall; instead it possesses a protein-rich flexible pellicle. Thus, the first statement is false.',
        "expl_bn": 'ইউগ্লিনায় কোনো সেলুলোজ কোষপ্রাচীর থাকে না, তার পরিবর্তে প্রোটিনের পেলিকল থাকে। তাই প্রথম বাক্যটি মিথ্যা।',
    },
    {
        "id": 'BIO-BC-105',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": "Which organism is commonly known as 'bread mould'?",
        "bn": "কোন ছত্রাকটিকে সাধারণভাবে 'পাউরুটির ছত্রাক' বা ব্রেড মোল্ড (Bread mould) বলা হয়?",
        "opts": {
            "en": ['Rhizopus stolonifer', 'Penicillium notatum', 'Agaricus bisporus', 'Albugo candida'],
            "bn": ['রাইজোপাস (Rhizopus)', 'পেনিসিলিয়াম', 'অ্যাগারিকাস', 'অ্যালবুগো']
        },
        "correct": 0,
        "expl_en": 'Rhizopus is commonly known as the bread mould. It belongs to Phycomycetes.',
        "expl_bn": 'Rhizopus ছত্রাককে সাধারণ ভাষায় ব্রেড মোল্ড বা পাউরুটির ছত্রাক বলা হয়।',
    },
    {
        "id": 'BIO-BC-106',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Examine the given diagram representing a filament of Nostoc:<br><svg viewBox="0 0 500 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Mucilaginous Sheath outline -->\n  <path d="M 30 80 Q 80 50 140 50 T 250 50 T 360 50 T 460 80 Q 400 110 320 110 T 180 110 T 30 80 Z" fill="#dcfce7" stroke="#16a34a" stroke-dasharray="4,3" opacity="0.6"/>\n  <!-- Vegetative cells -->\n  <circle cx="60" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="95" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="130" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="165" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <!-- Heterocyst (Larger, thick-walled, labeled A) -->\n  <circle cx="215" cy="80" r="22" fill="#fed7aa" stroke="#c2410c" stroke-width="3"/>\n  <circle cx="215" cy="80" r="16" fill="#ffedd5" stroke="#ea580c" stroke-width="1.5" stroke-dasharray="2,2"/>\n  <text x="215" y="85" fill="#9a3412" font-size="14" font-weight="bold" font-family="system-ui" text-anchor="middle">A</text>\n  <!-- More vegetative cells (labeled B) -->\n  <circle cx="265" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <text x="265" y="85" fill="#14532d" font-size="12" font-weight="bold" font-family="system-ui" text-anchor="middle">B</text>\n  <circle cx="300" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="335" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="370" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="405" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="440" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <!-- Mucilage label C -->\n  <line x1="100" y1="35" x2="100" y2="55" stroke="#047857" stroke-width="1.5"/>\n  <text x="100" y="28" fill="#047857" font-size="12" font-weight="bold" font-family="system-ui" text-anchor="middle">C (Mucilaginous Sheath)</text>\n  <line x1="215" y1="115" x2="215" y2="135" stroke="#c2410c" stroke-width="1.5"/>\n  <text x="215" y="148" fill="#c2410c" font-size="12" font-weight="bold" font-family="system-ui" text-anchor="middle">Part A</text>\n  <line x1="335" y1="115" x2="335" y2="135" stroke="#15803d" stroke-width="1.5"/>\n  <text x="335" y="148" fill="#15803d" font-size="12" font-weight="bold" font-family="system-ui" text-anchor="middle">Part B (Vegetative Cell)</text>\n</svg><br>Identify the labeled parts A, B, and C along with their primary functions:',
        "bn": 'নস্টক (Nostoc)-এর ফিলামেন্ট নির্দেশকারী প্রদত্ত চিত্রটি লক্ষ্য করো:<br><svg viewBox="0 0 500 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Mucilaginous Sheath outline -->\n  <path d="M 30 80 Q 80 50 140 50 T 250 50 T 360 50 T 460 80 Q 400 110 320 110 T 180 110 T 30 80 Z" fill="#dcfce7" stroke="#16a34a" stroke-dasharray="4,3" opacity="0.6"/>\n  <!-- Vegetative cells -->\n  <circle cx="60" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="95" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="130" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="165" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <!-- Heterocyst (Larger, thick-walled, labeled A) -->\n  <circle cx="215" cy="80" r="22" fill="#fed7aa" stroke="#c2410c" stroke-width="3"/>\n  <circle cx="215" cy="80" r="16" fill="#ffedd5" stroke="#ea580c" stroke-width="1.5" stroke-dasharray="2,2"/>\n  <text x="215" y="85" fill="#9a3412" font-size="14" font-weight="bold" font-family="system-ui" text-anchor="middle">A</text>\n  <!-- More vegetative cells (labeled B) -->\n  <circle cx="265" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <text x="265" y="85" fill="#14532d" font-size="12" font-weight="bold" font-family="system-ui" text-anchor="middle">B</text>\n  <circle cx="300" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="335" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="370" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="405" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <circle cx="440" cy="80" r="16" fill="#4ade80" stroke="#15803d" stroke-width="2"/>\n  <!-- Mucilage label C -->\n  <line x1="100" y1="35" x2="100" y2="55" stroke="#047857" stroke-width="1.5"/>\n  <text x="100" y="28" fill="#047857" font-size="12" font-weight="bold" font-family="system-ui" text-anchor="middle">C (Mucilaginous Sheath)</text>\n  <line x1="215" y1="115" x2="215" y2="135" stroke="#c2410c" stroke-width="1.5"/>\n  <text x="215" y="148" fill="#c2410c" font-size="12" font-weight="bold" font-family="system-ui" text-anchor="middle">Part A</text>\n  <line x1="335" y1="115" x2="335" y2="135" stroke="#15803d" stroke-width="1.5"/>\n  <text x="335" y="148" fill="#15803d" font-size="12" font-weight="bold" font-family="system-ui" text-anchor="middle">Part B (Vegetative Cell)</text>\n</svg><br>A, B এবং C চিহ্নিত অংশগুলি এবং তাদের প্রধান কাজ শনাক্ত করো:',
        "opts": {
            "en": ['A = Heterocyst (Nitrogen fixation); B = Vegetative cell (Photosynthesis); C = Mucilaginous sheath (Protection)', 'A = Vegetative cell (Photosynthesis); B = Heterocyst (Nitrogen fixation); C = Cell wall', 'A = Akinete (Perennation); B = Hormogonium; C = Slime layer', 'A = Heterocyst (Photosynthesis); B = Vegetative cell (Nitrogen fixation); C = Gelatinous capsule'],
            "bn": ['A = হেটারোসিস্ট (নাইট্রোজেন সংবন্ধন); B = অঙ্গজ কোষ (সালোকসংশ্লেষ); C = মিউসিলেজের আবরণী (সুরক্ষা)', 'A = অঙ্গজ কোষ (সালোকসংশ্লেষ); B = হেটারোসিস্ট (নাইট্রোজেন সংবন্ধন); C = কোষপ্রাচীর', 'A = অ্যাকাইনেট (সুপ্তাবস্থা); B = হরমোগোনিয়াম; C = স্লাইম স্তর', 'A = হেটারোসিস্ট (সালোকসংশ্লেষ); B = অঙ্গজ কোষ (নাইট্রোজেন সংবন্ধন); C = ক্যাপসুল']
        },
        "correct": 0,
        "expl_en": 'In Nostoc: A is the specialized thick-walled, oxygen-impermeable Heterocyst housing nitrogenase enzyme for atmospheric nitrogen fixation. B is the photosynthetic vegetative cell containing chlorophyll a. C is the protective gelatinous/mucilaginous sheath surrounding the colony.',
        "expl_bn": 'নস্টক-এ: A হলো পুরু প্রাচীরযুক্ত হেটারোসিস্ট যাতে নাইট্রোজিনেজ উৎসেচক থাকে এবং এটি বায়বীয় নাইট্রোজেন সংবন্ধন করে। B হলো সালোকসংশ্লেষকারী অঙ্গজ কোষ। C হলো পুরো ফিলামেন্টকে আবৃতকারী মিউসিলেজ স্তর।',
    },
    {
        "id": 'BIO-BC-107',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Given below is the schematic structural diagram of a T4 Bacteriophage:<br><svg viewBox="0 0 320 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Head (Icosahedral Capsid, labeled A) -->\n  <polygon points="160,20 200,45 200,90 160,115 120,90 120,45" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>\n  <path d="M 140,55 Q 160,40 180,60 T 150,85 T 175,100" fill="none" stroke="#e11d48" stroke-width="2"/>\n  <text x="160" y="65" fill="#0369a1" font-size="13" font-weight="bold" font-family="system-ui" text-anchor="middle">A (Head)</text>\n  <!-- Collar labeled B -->\n  <rect x="145" y="115" width="30" height="10" rx="2" fill="#fde047" stroke="#ca8a04" stroke-width="1.5"/>\n  <text x="195" y="124" fill="#a16207" font-size="10" font-weight="bold" font-family="system-ui">B (Collar)</text>\n  <!-- Sheath labeled C -->\n  <rect x="148" y="125" width="24" height="60" fill="#cbd5e1" stroke="#475569" stroke-width="1.5"/>\n  <!-- Helical ridges on sheath -->\n  <line x1="148" y1="135" x2="172" y2="135" stroke="#64748b" stroke-width="1.5"/>\n  <line x1="148" y1="145" x2="172" y2="145" stroke="#64748b" stroke-width="1.5"/>\n  <line x1="148" y1="155" x2="172" y2="155" stroke="#64748b" stroke-width="1.5"/>\n  <line x1="148" y1="165" x2="172" y2="165" stroke="#64748b" stroke-width="1.5"/>\n  <line x1="148" y1="175" x2="172" y2="175" stroke="#64748b" stroke-width="1.5"/>\n  <text x="195" y="158" fill="#334155" font-size="10" font-weight="bold" font-family="system-ui">C (Sheath)</text>\n  <!-- Baseplate labeled D -->\n  <polygon points="135,185 185,185 190,195 130,195" fill="#f43f5e" stroke="#be123c" stroke-width="1.5"/>\n  <text x="200" y="193" fill="#be123c" font-size="10" font-weight="bold" font-family="system-ui">Base plate</text>\n  <!-- Tail Fibres labeled E -->\n  <path d="M 135 195 L 95 235 L 75 245" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>\n  <path d="M 145 195 L 125 240 L 115 250" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>\n  <path d="M 175 195 L 195 240 L 205 250" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>\n  <path d="M 185 195 L 225 235 L 245 245" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>\n  <text x="50" y="240" fill="#0f172a" font-size="10" font-weight="bold" font-family="system-ui">D (Tail fibres)</text>\n</svg><br>Which of the following correctly matches the labeled parts with their characteristics?',
        "bn": 'নিচে একটি T4 ব্যাকটিরিওফাজের গঠন সংক্রান্ত রেখাচিত্র দেওয়া হলো:<br><svg viewBox="0 0 320 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Head (Icosahedral Capsid, labeled A) -->\n  <polygon points="160,20 200,45 200,90 160,115 120,90 120,45" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>\n  <path d="M 140,55 Q 160,40 180,60 T 150,85 T 175,100" fill="none" stroke="#e11d48" stroke-width="2"/>\n  <text x="160" y="65" fill="#0369a1" font-size="13" font-weight="bold" font-family="system-ui" text-anchor="middle">A (Head)</text>\n  <!-- Collar labeled B -->\n  <rect x="145" y="115" width="30" height="10" rx="2" fill="#fde047" stroke="#ca8a04" stroke-width="1.5"/>\n  <text x="195" y="124" fill="#a16207" font-size="10" font-weight="bold" font-family="system-ui">B (Collar)</text>\n  <!-- Sheath labeled C -->\n  <rect x="148" y="125" width="24" height="60" fill="#cbd5e1" stroke="#475569" stroke-width="1.5"/>\n  <!-- Helical ridges on sheath -->\n  <line x1="148" y1="135" x2="172" y2="135" stroke="#64748b" stroke-width="1.5"/>\n  <line x1="148" y1="145" x2="172" y2="145" stroke="#64748b" stroke-width="1.5"/>\n  <line x1="148" y1="155" x2="172" y2="155" stroke="#64748b" stroke-width="1.5"/>\n  <line x1="148" y1="165" x2="172" y2="165" stroke="#64748b" stroke-width="1.5"/>\n  <line x1="148" y1="175" x2="172" y2="175" stroke="#64748b" stroke-width="1.5"/>\n  <text x="195" y="158" fill="#334155" font-size="10" font-weight="bold" font-family="system-ui">C (Sheath)</text>\n  <!-- Baseplate labeled D -->\n  <polygon points="135,185 185,185 190,195 130,195" fill="#f43f5e" stroke="#be123c" stroke-width="1.5"/>\n  <text x="200" y="193" fill="#be123c" font-size="10" font-weight="bold" font-family="system-ui">Base plate</text>\n  <!-- Tail Fibres labeled E -->\n  <path d="M 135 195 L 95 235 L 75 245" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>\n  <path d="M 145 195 L 125 240 L 115 250" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>\n  <path d="M 175 195 L 195 240 L 205 250" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>\n  <path d="M 185 195 L 225 235 L 245 245" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>\n  <text x="50" y="240" fill="#0f172a" font-size="10" font-weight="bold" font-family="system-ui">D (Tail fibres)</text>\n</svg><br>নিচের কোন বিকল্পটিতে চিহ্নিত অংশ ও তার বৈশিষ্ট্য সঠিকভাবে মেলানো হয়েছে?',
        "opts": {
            "en": ['A = Head enclosing double-stranded DNA; C = Contractile sheath; D = Tail fibres for attachment', 'A = Head enclosing single-stranded RNA; C = Collar; D = Pili', 'A = Head without nucleic acid; C = Capsomere sheath; D = Flagella', 'A = Tail enclosing plasmid; C = Head; D = Spikes'],
            "bn": ['A = দ্বিতন্ত্রী DNA যুক্ত মস্তক (Head); C = সংকোচনশীল আবরণী (Sheath); D = পোষক কোষে যুক্ত হওয়ার টেল ফাইবার', 'A = একতন্ত্রী RNA যুক্ত মস্তক; C = কলার; D = পিলি', 'A = নিউক্লিক অ্যাসিডহীন মস্তক; C = ক্যাপসোমিয়ার আবরণী; D = ফ্ল্যাজেলা', 'A = প্লাজমিড যুক্ত লেজ; C = মস্তক; D = স্পাইক']
        },
        "correct": 0,
        "expl_en": 'In a T-even bacteriophage (bacterial virus): A is the polyhedral icosahedral head enclosing a double-stranded DNA genome. B is the collar, C is the contractile helical sheath, and D represents tail fibres (usually 6) that recognize and attach to receptor sites on the bacterial wall.',
        "expl_bn": 'ব্যাকটিরিওফাজে: A হলো পলিহেড্রাল মস্তক যার ভেতর দ্বিতন্ত্রী DNA থাকে। C হলো সংকোচনশীল আবরণী (Sheath) এবং D হলো পোষক ব্যাকটিরিয়ার প্রাচীরে যুক্ত হওয়ার টেল ফাইবার।',
    },
    {
        "id": 'BIO-BC-108',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Observe the diagram comparing reproductive structures of two fungal classes:<br><svg viewBox="0 0 460 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Ascus (Ascomycetes): Sac with 8 endogenous spores -->\n  <g transform="translate(40, 20)">\n    <rect x="20" y="10" width="60" height="150" rx="30" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>\n    <text x="50" y="180" fill="#92400e" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Ascus (Sac-fungi)</text>\n    <text x="50" y="195" fill="#78350f" font-size="9" font-family="system-ui" text-anchor="middle">8 Endogenous Ascospores</text>\n    <!-- 8 spores inside -->\n    <circle cx="50" cy="30" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="48" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="66" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="84" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="102" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="120" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="138" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="154" r="6" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n  </g>\n  <!-- Basidium (Basidiomycetes): Club with 4 exogenous spores -->\n  <g transform="translate(260, 20)">\n    <!-- Club shaped basidium -->\n    <path d="M 50 160 L 50 80 C 30 70 30 40 50 40 C 70 40 70 70 50 80 Z" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>\n    <!-- 4 Sterigmata & 4 Exogenous Basidiospores on top -->\n    <line x1="38" y1="42" x2="30" y2="28" stroke="#4338ca" stroke-width="2"/>\n    <circle cx="28" cy="24" r="7" fill="#818cf8" stroke="#3730a3" stroke-width="1.5"/>\n    <line x1="46" y1="40" x2="42" y2="22" stroke="#4338ca" stroke-width="2"/>\n    <circle cx="42" cy="16" r="7" fill="#818cf8" stroke="#3730a3" stroke-width="1.5"/>\n    <line x1="54" y1="40" x2="58" y2="22" stroke="#4338ca" stroke-width="2"/>\n    <circle cx="58" cy="16" r="7" fill="#818cf8" stroke="#3730a3" stroke-width="1.5"/>\n    <line x1="62" y1="42" x2="70" y2="28" stroke="#4338ca" stroke-width="2"/>\n    <circle cx="72" cy="24" r="7" fill="#818cf8" stroke="#3730a3" stroke-width="1.5"/>\n    <text x="50" y="180" fill="#3730a3" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Basidium (Club-fungi)</text>\n    <text x="50" y="195" fill="#312e81" font-size="9" font-family="system-ui" text-anchor="middle">4 Exogenous Basidiospores</text>\n  </g>\n</svg><br>Which comparison between Ascus and Basidium is CORRECT?',
        "bn": 'ছত্রাকের দুটি শ্রেণির জনন অঙ্গের তুলনামূলক চিত্রটি লক্ষ্য করো:<br><svg viewBox="0 0 460 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Ascus (Ascomycetes): Sac with 8 endogenous spores -->\n  <g transform="translate(40, 20)">\n    <rect x="20" y="10" width="60" height="150" rx="30" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>\n    <text x="50" y="180" fill="#92400e" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Ascus (Sac-fungi)</text>\n    <text x="50" y="195" fill="#78350f" font-size="9" font-family="system-ui" text-anchor="middle">8 Endogenous Ascospores</text>\n    <!-- 8 spores inside -->\n    <circle cx="50" cy="30" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="48" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="66" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="84" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="102" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="120" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="138" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n    <circle cx="50" cy="154" r="6" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>\n  </g>\n  <!-- Basidium (Basidiomycetes): Club with 4 exogenous spores -->\n  <g transform="translate(260, 20)">\n    <!-- Club shaped basidium -->\n    <path d="M 50 160 L 50 80 C 30 70 30 40 50 40 C 70 40 70 70 50 80 Z" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>\n    <!-- 4 Sterigmata & 4 Exogenous Basidiospores on top -->\n    <line x1="38" y1="42" x2="30" y2="28" stroke="#4338ca" stroke-width="2"/>\n    <circle cx="28" cy="24" r="7" fill="#818cf8" stroke="#3730a3" stroke-width="1.5"/>\n    <line x1="46" y1="40" x2="42" y2="22" stroke="#4338ca" stroke-width="2"/>\n    <circle cx="42" cy="16" r="7" fill="#818cf8" stroke="#3730a3" stroke-width="1.5"/>\n    <line x1="54" y1="40" x2="58" y2="22" stroke="#4338ca" stroke-width="2"/>\n    <circle cx="58" cy="16" r="7" fill="#818cf8" stroke="#3730a3" stroke-width="1.5"/>\n    <line x1="62" y1="42" x2="70" y2="28" stroke="#4338ca" stroke-width="2"/>\n    <circle cx="72" cy="24" r="7" fill="#818cf8" stroke="#3730a3" stroke-width="1.5"/>\n    <text x="50" y="180" fill="#3730a3" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Basidium (Club-fungi)</text>\n    <text x="50" y="195" fill="#312e81" font-size="9" font-family="system-ui" text-anchor="middle">4 Exogenous Basidiospores</text>\n  </g>\n</svg><br>অ্যাসকাস (Ascus) এবং ব্যাসিডিয়াম (Basidium)-এর মধ্যে কোন তুলনাটি সঠিক?',
        "opts": {
            "en": ['Ascus produces 8 ascospores ENDOGENOUSLY; Basidium produces 4 basidiospores EXOGENOUSLY', 'Ascus produces 4 ascospores exogenously; Basidium produces 8 basidiospores endogenously', 'Both ascospores and basidiospores are formed endogenously inside fruiting cavities', 'Ascospores are diploid spores; Basidiospores are triploid spores'],
            "bn": ['অ্যাসকাসে ৮টি অ্যাসকোস্পোর অন্তর্জনিষ্ণুভাবে (endogenously) তৈরি হয়; ব্যাসিডিয়ামে ৪টি ব্যাসিডিওস্পোর বহির্জনিষ্ণুভাবে (exogenously) তৈরি হয়', 'অ্যাসকাসে ৪টি স্পোর বহির্জনিষ্ণুভাবে তৈরি হয়; ব্যাসিডিয়ামে ৮টি স্পোর অন্তর্জনিষ্ণুভাবে তৈরি হয়', 'উভয় প্রকার স্পোরই ফ্রুটিং বডির ভেতরে অন্তর্জনিষ্ণুভাবে তৈরি হয়', 'অ্যাসকোস্পোর ডিপ্লয়েড কিন্তু ব্যাসিডিওস্পোর ট্রিপ্লয়েড']
        },
        "correct": 0,
        "expl_en": 'In Ascomycetes, karyogamy and meiosis inside the ascus followed by one mitosis yields 8 haploid ascospores endogenously. In Basidiomycetes, karyogamy and meiosis in the basidium form 4 haploid basidiospores exogenously on sterigmata.',
        "expl_bn": 'অ্যাসকোমাইসিটিসে অ্যাসকাসের ভেতরে মায়োসিস ও মাইটোসিসের মাধ্যমে ৮টি অ্যাসকোস্পোর অন্তর্জনিষ্ণুভাবে (endogenously) তৈরি হয়। ব্যাসিডিওমাইসিটিসে ব্যাসিডিয়ামের শীর্ষদেশে ৪টি ব্যাসিডিওস্পোর বহির্জনিষ্ণুভাবে (exogenously) উৎপন্ন হয়।',
    },
    {
        "id": 'BIO-BC-109',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Methanogens are obligate anaerobes belonging to Archaebacteria found in the rumen of cattle.<br>Reason (R): Methanogens possess branched-chain lipid monolayers in their cell membranes that allow survival in extreme conditions and generate biogas (CH4) from dung.',
        "bn": 'নিশ্চিত বিবৃতি (A): মিথেনোজেনগুলি হলো আর্কিবা্যাকটেরিয়া পর্বভুক্ত বাধ্যতামূলক অবায়ুজীবী জীব যা গবাদি পশুর রুমেনে পাওয়া যায়।<br>যুক্তি (R): মিথেনোজেনের কোষপর্দায় শাখাযুক্ত লিপিডের মনোলেয়ার থাকে যা প্রতিকূল পরিবেশে টিকে থাকতে সাহায্য করে এবং গোবর থেকে বায়োগ্যাস (CH4) তৈরি করে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 1,
        "expl_en": 'Both (A) and (R) are factually true statements. However, the presence of branched-chain ether lipids explains their extreme survival in hot/anaerobic settings in general, but does not specifically explain why they reside symbiotically in the rumen of ruminants (which is due to the anaerobic cellulolytic niche).',
        "expl_bn": '(A) এবং (R) উভয় বিবৃতিই সত্য। তবে এদের শাখা-যুক্ত লিপিড পর্দা প্রতিকূল পরিবেশে বেঁচে থাকার সাধারণ কারণ ব্যাখ্যা করে, কিন্তু রুমেনে অবস্থানের নির্দিষ্ট জৈবনিক ব্যাখ্যা নয়। তাই (R), (A)-এর সঠিক ব্যাখ্যা নয়।',
    },
    {
        "id": 'BIO-BC-110',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": "Assertion (A): Cyanobacteria played a critical evolutionary role in converting the Earth's reducing primitive atmosphere into an oxidizing atmosphere.<br>Reason (R): Cyanobacteria are oxygenic photosynthetic organisms possessing Chlorophyll a identical to higher green plants.",
        "bn": 'নিশ্চিত বিবৃতি (A): আদিম পৃথিবীর বিজারক বায়ুমণ্ডলকে জারক বায়ুমণ্ডলে রূপান্তরিত করতে সায়ানোব্যাকটেরিয়ার ভূমিকা ছিল অত্যন্ত গুরুত্বপূর্ণ।<br>যুক্তি (R): সায়ানোব্যাকটেরিয়া হলো অক্সিজেনিক সালোকসংশ্লেষকারী জীব যাদের উচ্চশ্রেণীর সবুজ উদ্ভিদের মতো ক্লোরোফিল-a থাকে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Cyanobacteria were the earliest organisms to perform oxygenic photosynthesis using water as an electron donor (due to presence of Chl a and PS II), releasing molecular oxygen into the atmosphere and creating an oxidizing biosphere. Thus, (R) correctly explains (A).',
        "expl_bn": 'সায়ানোব্যাকটেরিয়ায় ক্লোরোফিল-a থাকার ফলে তারা জলকে ভেঙে অক্সিজেনিক সালোকসংশ্লেষ সম্পন্ন করে আণবিক অক্সিজেন পরিবেশে মুক্ত করেছিল, যা বিজারক বায়ুমণ্ডলকে জারক বায়ুমণ্ডলে পরিবর্তিত করে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-BC-111',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Mycoplasma are completely insensitive to beta-lactam antibiotics such as penicillin.<br>Reason (R): Penicillin specifically inhibits peptidoglycan cell wall biosynthesis, and Mycoplasma naturally lack any cell wall.',
        "bn": 'নিশ্চিত বিবৃতি (A): পেনিসিলিনের মতো বিটা-ল্যাকটাম অ্যান্টিবায়োটিক মাইকোপ্লাজমার উপর একেবারেই কোনো প্রভাব ফেলতে পারে না।<br>যুক্তি (R): পেনিসিলিন পেপটিডোগ্লাইক্যান কোষপ্রাচীর তৈরিতে বাধা দেয়, কিন্তু মাইকোপ্লাজমায় কোনো প্রকার কোষপ্রাচীর থাকেই না।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Penicillin acts by inhibiting transpeptidase enzymes responsible for cross-linking peptidoglycan in bacterial cell walls. Because Mycoplasmas naturally lack cell walls, there is no target site, making them completely resistant to penicillin. (R) correctly explains (A).',
        "expl_bn": 'পেনিসিলিন ব্যাকটিরিয়ার কোষপ্রাচীরের পেপটিডোগ্লাইক্যান গঠনে বাধা দেয়। কিন্তু মাইকোপ্লাজমার কোষে কোনো কোষপ্রাচীরই থাকে না, তাই পেনিসিলিন এদের কোনো ক্ষতি করতে পারে না। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-BC-112',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Diatomaceous earth is indestructible and used extensively in filtration of oils and syrups.<br>Reason (R): The cell walls of diatoms are embedded with indestructible silica forming two overlapping thin shells that fit together like a soap box.',
        "bn": 'নিশ্চিত বিবৃতি (A): ডায়াটমোসিয়াস মৃত্তিকা প্রায় অবিনশ্বর এবং এটি তেল ও সিরাপ ফিল্টার করার কাজে ব্যাপকভাবে ব্যবহৃত হয়।<br>যুক্তি (R): ডায়াটমের কোষপ্রাচীর সিলিকা সমন্বিত এবং সাবানদানির মতো একে অপরের ওপর চেপে বসা দুটি পাতলা খোলকের সমন্বয়ে গঠিত।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Because diatom frustules are impregnated with biogenic silica (SiO2), they do not decay and accumulate over billions of years as diatomaceous earth, which is gritty, porous, and ideal for polishing and industrial filtration. (R) correctly explains (A).',
        "expl_bn": 'ডায়াটমের কোষপ্রাচীরে সিলিকা সঞ্চিত থাকায় তা ক্ষয়প্রাপ্ত হয় না এবং কোটি কোটি বছর ধরে জমে ডায়াটোমাসিয়াস মৃত্তিকা গঠন করে। দানাদার হওয়ায় এটি তেল ও সিরাপ পরিস্রাবণে কাজে লাগে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-BC-113',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": "Assertion (A): Dinoflagellates like Gonyaulax cause deadly 'red tides' that kill marine fishes.<br>Reason (R): Rapid population explosions of Gonyaulax release massive amounts of water-soluble toxins (saxitoxins) into the sea.",
        "bn": "নিশ্চিত বিবৃতি (A): গনিয়াউলাক্স (Gonyaulax)-এর মতো ডাইনোফ্ল্যাজেলেট সমুদ্রের জলে মারাত্মক 'লাল জোয়ার' (Red tide) সৃষ্টি করে যা সামুদ্রিক মাছের মৃত্যু ঘটায়।<br>যুক্তি (R): গনিয়াউলাক্সের দ্রুত সংখ্যাবৃদ্ধির ফলে সমুদ্রে বিপুল পরিমাণে পানিতে দ্রবণীয় বিষাক্ত পদার্থ (স্যাক্সিটক্সিন) নিঃসৃত হয়।",
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Gonyaulax undergoes rapid multiplication turning the sea red. Toxins released in such large quantities kill marine animals such as fishes. (R) provides the exact scientific explanation of (A).',
        "expl_bn": 'গনিয়াউলাক্সের অস্বাভাবিক বৃদ্ধির ফলে সমুদ্রের জল লাল দেখায় এবং এদের নিঃসৃত মারাত্মক টক্সিনের বিষক্রিয়ায় মাছ ও সামুদ্রিক প্রাণী মারা যায়। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-BC-114',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Euglena is considered a connect between plants and animals exhibiting mixotrophic nutrition.<br>Reason (R): Euglena is photosynthetic in the presence of sunlight, but when deprived of light, it behaves as a heterotroph by predating on smaller organisms.',
        "bn": 'নিশ্চিত বিবৃতি (A): ইউগ্লিনাকে উদ্ভিদ ও প্রাণীর সংযোগকারী সেতু হিসেবে বিবেচনা করা হয় এবং এরা মিক্সোট্রফিক পুষ্টি প্রদর্শন করে।<br>যুক্তি (R): সূর্যের আলোর উপস্থিতিতে ইউগ্লিনা সালোকসংশ্লেষ করে, কিন্তু আলো না থাকলে এটি ছোট প্রাণীদের শিকার করে পরভোজী পুষ্টি চালায়।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'The dual nutritional mode (autotrophic in light, heterotrophic holozoic/saprobic in dark) is termed mixotrophic nutrition, which along with plant-like pigments and animal-like motility/pellicle bridges the two kingdoms. (R) correctly explains (A).',
        "expl_bn": 'আলোয় স্বভোজী এবং অন্ধকারে শিকার ধরে পরভোজী পুষ্টি চালানোর এই দ্বৈত পদ্ধতিকে মিক্সোট্রফিক পুষ্টি বলে, যা উদ্ভিদ ও প্রাণীর সংযোগ রক্ষা করে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-BC-115',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": "Assertion (A): Deuteromycetes are commonly termed 'imperfect fungi' (Fungi Imperfecti).<br>Reason (R): Only the asexual or vegetative phases of these fungi are known; when sexual stages are discovered, they are transferred to Ascomycetes or Basidiomycetes.",
        "bn": "নিশ্চিত বিবৃতি (A): ডিউটেরোমাইসিটিসকে সাধারণভাবে 'অসম্পূর্ণ ছত্রাক' (Fungi Imperfecti) বলা হয়।<br>যুক্তি (R): এই ছত্রাকগুলির কেবলমাত্র অযৌন বা অঙ্গজ দশা জানা গেছে; যখনই এদের যৌন জনন আবিষ্কৃত হয়, তখনই এদের অ্যাসকোমাইসিটিস বা ব্যাসিডিওমাইসিটিস শ্রেণিতে স্থানান্তরিত করা হয়।",
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": "Deuteromycetes lack any observed sexual teleomorphic stage. Because fungal classification is fundamentally rooted in sexual fruiting bodies, their classification is 'imperfect'. (R) correctly explains (A).",
        "expl_bn": "ডিউটেরোমাইসিটিসে কোনো যৌন জনন বা যৌন ফ্রুটিং বডি দেখা যায় না বলেই এদের 'অসম্পূর্ণ ছত্রাক' বলা হয়। যৌন দশা আবিষ্কার হওয়ামাত্র এদের যথোপযুক্ত শ্রেণিতে সরানো হয়। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।",
    },
    {
        "id": 'BIO-BC-116',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Lichens are described as pioneering organisms on barren rocks and excellent bioindicators of industrial air pollution.<br>Reason (R): Lichens cannot grow in environments with even trace concentrations of sulphur dioxide (SO2).',
        "bn": 'নিশ্চিত বিবৃতি (A): লাইকেনকে উন্মুক্ত অনুর্বর পাথরে বাস্তুতান্ত্রিক পর্যায়ক্রমের অগ্রদূত এবং বায়ুদূষণের উৎকৃষ্ট নির্দেশক বলা হয়।<br>যুক্তি (R): বাতাসে সামান্যতম সালফার ডাইঅক্সাইড (SO2) গ্যাস উপস্থিত থাকলে লাইকেন বেঁচে থাকতে পারে না।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 1,
        "expl_en": 'Both statements are true. However, being pioneers on bare rocks is due to their lichen acids (organic acids that weather rocks into soil), whereas being pollution indicators is due to their sensitivity to SO2. Hence, (R) is true but does not completely explain both parts of (A).',
        "expl_bn": 'উভয় বিবৃতিই সত্য। তবে পাথরের ওপর অগ্রদূত হওয়ার কারণ তাদের জৈব অ্যাসিড নিঃসরণ, আর দূষণ নির্দেশক হওয়ার কারণ SO2 সংবেদনশীলতা। তাই (R), (A)-এর সম্পূর্ণ সঠিক ব্যাখ্যা নয়।',
    },
    {
        "id": 'BIO-BC-117',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": "Assertion (A): Viruses are not included in Whittaker's Five Kingdom System of biological classification.<br>Reason (R): Viruses are non-cellular, inert crystalline entities outside a living host cell, and do not possess their own independent metabolic machinery.",
        "bn": 'নিশ্চিত বিবৃতি (A): হুইটেকারের পঞ্চ-রাজ্য শ্রেণীবিন্যাসে ভাইরাসকে কোনো স্থান দেওয়া হয়নি।<br>যুক্তি (R): ভাইরাস হলো অকোষীয়, সজীব পোষক কোষের বাইরে নিষ্ক্রিয় কেলাসাকার কণা এবং এদের নিজস্ব কোনো স্বাধীন বিপাকীয় ব্যবস্থা নেই।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": "Whittaker's classification was strictly based on cellular organization (prokaryotic vs eukaryotic, unicellular vs multicellular). Because viruses are acellular nucleoprotein complexes without cellular organization or independent metabolism, they could not be placed in any kingdom. (R) correctly explains (A).",
        "expl_bn": 'হুইটেকারের শ্রেণীবিন্যাস ছিল কোষীয় সংগঠনের ওপর ভিত্তি করে। ভাইরাস অকোষীয় ও স্বাধীন বিপাকহীন হওয়ায় তাদের পঞ্চ-রাজ্যের কোনোটিতেই রাখা সম্ভব হয়নি। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-BC-118',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Viroids are infectious agents that are smaller than viruses and lack a protein capsid.<br>Reason (R): Viroids consist of free, low molecular weight single-stranded RNA molecules that cause potato spindle tuber disease.',
        "bn": 'নিশ্চিত বিবৃতি (A): ভিরয়েড হলো ভাইরাসের চেয়েও ক্ষুদ্র সংক্রামক কণা যার কোনো প্রোটিন আবরণী (ক্যাপসিড) থাকে না।<br>যুক্তি (R): ভিরয়েড মূলত কম আণবিক গুরুত্ববিশিষ্ট মুক্ত একতন্ত্রী RNA দ্বারা গঠিত যা আলুর স্পিন্ডল টিউবার রোগ সৃষ্টি করে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'T.O. Diener discovered viroids in 1971; their hallmark distinction from viruses is the complete absence of a protein coat (capsid), existing solely as naked low-molecular-weight RNA. (R) provides the accurate scientific explanation of (A).',
        "expl_bn": '১৯৭১ সালে টি. ও. ডাইনার ভিরয়েড আবিষ্কার করেন। ভাইরাসের মতো প্রোটিন আবরণ না থাকায় এবং শুধুমাত্র কম আণবিক ওজনের নগ্ন RNA হওয়ায় এটি ভাইরাসের চেয়েও ছোট। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-BC-119',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Prions are infectious agents responsible for Bovine Spongiform Encephalopathy (BSE) and Cr-Jacob disease.<br>Reason (R): Prions consist solely of abnormally folded proteins without any detectable nucleic acid (DNA or RNA).',
        "bn": 'নিশ্চিত বিবৃতি (A): প্রিয়ন হলো সংক্রামক কণা যা গরুর বোভাইন স্পঞ্জিফর্ম এনসেফালোপ্যাথি (BSE) এবং মানুষের ক্রয়েটজফেল্ড-জ্যাকব রোগের জন্য দায়ী।<br>যুক্তি (R): প্রিয়নে কোনো সনাক্তকরণযোগ্য নিউক্লিক অ্যাসিড (DNA বা RNA) থাকে না, এটি কেবল অস্বাভাবিকভাবে ভাঁজ হওয়া প্রোটিন দ্বারা গঠিত।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 1,
        "expl_en": 'Both (A) and (R) are completely true statements. However, (R) describes the chemical composition of prions, while the pathogenesis of neurodegeneration involves templated misfolding of host PrPC into insoluble amyloid PrPSc plaques.',
        "expl_bn": '(A) এবং (R) উভয় বিবৃতিই সত্য। তবে (R) প্রিয়নের গঠন ব্যাখ্যা করে, রোগ সৃষ্টির স্নায়বিক প্যাথোজেনেসিস নয়। তাই (R), (A)-এর সঠিক ব্যাখ্যা নয়।',
    },
    {
        "id": 'BIO-BC-120',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Statement I: In Ascomycetes and Basidiomycetes, an intervening dikaryotic stage (n + n, i.e., two nuclei per cell) occurs during the sexual cycle before karyogamy.<br>Statement II: In Phycomycetes, plasmogamy is followed almost immediately by karyogamy to form a diploid zygospore without an extended dikaryophase.',
        "bn": 'বিবৃতি I: অ্যাসকোমাইসিটিস এবং ব্যাসিডিওমাইসিটিসের যৌন জননে প্লাজমোগ্যামি ও ক্য্যারিওগ্যামির মধ্যবর্তী সময়ে একটি দীর্ঘস্থায়ী ডাইক্যারিওটিক দশা (n + n, অর্থাৎ প্রতি কোষে দুটি নিউক্লিয়াস) দেখা যায়।<br>বিবৃতি II: ফাইকোমাইসিটিস-এ প্লাজমোগ্যামির পরপরই বিলম্ব না করে ক্য্যারিওগ্যামি ঘটে এবং কোনো দীর্ঘস্থায়ী ডাইক্যারিওদশা ছাড়াই ডিপ্লয়েড জাইগোস্পোর গঠিত হয়।',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক']
        },
        "correct": 0,
        "expl_en": 'Both statements are completely correct. Higher fungi (Ascomycetes and Basidiomycetes) exhibit a prolonged dikaryophase (n+n condition), whereas Phycomycetes fuse directly into a 2n zygospore.',
        "expl_bn": 'উভয় বিবৃতিই সম্পূর্ণ সঠিক। অ্যাসকোমাইসিটিস ও ব্যাসিডিওমাইসিটিস-এ দীর্ঘস্থায়ী ডাইক্যারিওদশা (n+n) থাকে, কিন্তু ফাইকোমাইসিটিসে প্লাজমোগ্যামির পরপরই ডিপ্লয়েড জাইগোস্পোর তৈরি হয়।',
    },
    {
        "id": 'BIO-BC-121',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Statement I: Slime moulds form an aggregation called plasmodium under suitable environmental conditions.<br>Statement II: During unfavorable conditions, the plasmodium differentiates to form fruiting bodies bearing true-walled spores at their tips.',
        "bn": 'বিবৃতি I: অনুকূল পরিবেশে স্লাইম মোল্ড পুঞ্জীভূত হয়ে প্লাজমোডিয়াম নামক গঠন তৈরি করে।<br>বিবৃতি II: প্রতিকূল পরিবেশে প্লাজমোডিয়াম বিভেদিত হয়ে ফ্রুটিং বডি গঠন করে যার শীর্ষে প্রকৃত প্রাচীরযুক্ত স্পোর তৈরি হয়।',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক']
        },
        "correct": 0,
        "expl_en": 'Both statements are exact NCERT lines: Under suitable conditions, slime moulds form an aggregation called plasmodium which may grow and spread over several feet. During unfavorable conditions, the plasmodium differentiates and forms fruiting bodies bearing spores with true cell walls at their tips.',
        "expl_bn": 'উভয় বিবৃতিই NCERT অনুসারে সঠিক। অনুকূল অবস্থায় স্লাইম মোল্ড প্লাজমোডিয়াম গঠন করে এবং প্রতিকূল অবস্থায় ফ্রুটিং বডির শীর্ষে প্রকৃত সেলুলোজ প্রাচীরযুক্ত প্রতিরোধী স্পোর তৈরি করে।',
    },
    {
        "id": 'BIO-BC-122',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Statement I: Amoeboid protozoans move and capture prey by putting out pseudopodia as in Amoeba.<br>Statement II: Marine forms of amoeboid protozoans possess silica shells on their surface.',
        "bn": 'বিবৃতি I: অ্যামিবয়েড প্রোটোজোয়া ক্ষণপদ বা সিউডোপোডিয়া তৈরি করে শিকার ধরে এবং চলাচল করে যেমন অ্যামিবা।<br>বিবৃতি II: অ্যামিবয়েড প্রোটোজোয়ার সামুদ্রিক প্রজাতিগুলির বহিরাবরণে সিলিকার খোলক উপস্থিত থাকে।',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক']
        },
        "correct": 0,
        "expl_en": 'Both statements are correct NCERT facts. Marine amoeboid protozoans (such as Radiolarians and Foraminiferans) have characteristic siliceous shells on their exterior surfaces.',
        "expl_bn": 'উভয় বিবৃতিই সঠিক। সামুদ্রিক অ্যামিবয়েড প্রোটোজোয়ার গায়ে সিলিকা নির্মিত খোলক থাকে এবং এরা ক্ষণপদের সাহায্যে শিকার ধরে।',
    },
    {
        "id": 'BIO-BC-123',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Statement I: Viruses contain both DNA and RNA simultaneously within their core.<br>Statement II: No virus contains both RNA and DNA; a virus is a nucleoprotein containing either DNA or RNA.',
        "bn": 'বিবৃতি I: ভাইরাসের কেন্দ্রীয় অংশে একই সাথে DNA এবং RNA উভয় নিউক্লিক অ্যাসিডই উপস্থিত থাকে।<br>বিবৃতি II: কোনো ভাইরাসে কখনোই একসাথে DNA ও RNA থাকে না; ভাইরাস হলো নিউক্লিওপ্রোটিন যাতে DNA অথবা RNA-র যেকোনো একটি থাকে।',
        "opts": {
            "en": ['Statement I is incorrect but Statement II is correct', 'Statement I is correct but Statement II is incorrect', 'Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect'],
            "bn": ['বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল']
        },
        "correct": 0,
        "expl_en": 'Statement I is incorrect while Statement II is correct. By fundamental virological definition, no virus ever contains both DNA and RNA simultaneously.',
        "expl_bn": 'বিবৃতি I সম্পূর্ণ ভুল এবং বিবৃতি II সঠিক। কোনো ভাইরাসের ভেতরেই কখনোই একসাথে DNA ও RNA থাকতে পারে না; যেকোনো একটিই জেনেটিক বস্তু হিসেবে থাকে।',
    },
    {
        "id": 'BIO-BC-124',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Match Column-I (Organisms) with Column-II (Key NCERT Features):<br>A. Puccinia<br>B. Ustilago<br>C. Agaricus<br>D. Claviceps<br>1. Smut fungus<br>2. Rust fungus<br>3. Ergot of rye<br>4. Edible mushroom',
        "bn": 'কলাম-I (ছত্রাক)-এর সাথে কলাম-II (NCERT বৈশিষ্ট্য) মেলাও:<br>A. Puccinia<br>B. Ustilago<br>C. Agaricus<br>D. Claviceps<br>1. স্মাট ছত্রাক<br>2. মরচে (রাস্ট) ছত্রাক<br>3. রাই ঘাসের এরগট<br>4. ভক্ষণযোগ্য মাশরুম',
        "opts": {
            "en": ['A-2, B-1, C-4, D-3', 'A-1, B-2, C-4, D-3', 'A-2, B-4, C-1, D-3', 'A-3, B-1, C-4, D-2'],
            "bn": ['A-2, B-1, C-4, D-3', 'A-1, B-2, C-4, D-3', 'A-2, B-4, C-1, D-3', 'A-3, B-1, C-4, D-2']
        },
        "correct": 0,
        "expl_en": 'Puccinia = Rust fungus (A-2); Ustilago = Smut fungus (B-1); Agaricus = Mushroom (C-4); Claviceps purpurea = Ergot fungus (D-3).',
        "expl_bn": 'Puccinia = রাস্ট ছত্রাক (A-2); Ustilago = স্মাট ছত্রাক (B-1); Agaricus = মাশরুম (C-4); Claviceps = এরগট ছত্রাক (D-3)।',
    },
    {
        "id": 'BIO-BC-125',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Match Column-I (Disease) with Column-II (Causative Agent):<br>A. Citrus canker<br>B. Potato spindle tuber disease<br>C. Mad cow disease (BSE)<br>D. Sleeping sickness<br>1. Viroid<br>2. Xanthomonas citri (Bacterium)<br>3. Trypanosoma (Flagellated protozoan)<br>4. Prion',
        "bn": 'কলাম-I (রোগ)-এর সাথে কলাম-II (রোগ সৃষ্টিকারী উপাদান) মেলাও:<br>A. সাইট্রাস ক্যাঙ্কার<br>B. আলুর স্পিন্ডল টিউবার রোগ<br>C. ম্যাড কাউ ডিজিজ (BSE)<br>D. স্লিপিং সিকনেস<br>1. ভিরয়েড<br>2. জ্যান্থোমোনাস সিট্রি (ব্যাকটেরিয়া)<br>3. ট্রাইপ্যানোসোমা (প্রোটোজোয়া)<br>4. প্রিয়ন',
        "opts": {
            "en": ['A-2, B-1, C-4, D-3', 'A-1, B-2, C-4, D-3', 'A-2, B-4, C-1, D-3', 'A-3, B-1, C-4, D-2'],
            "bn": ['A-2, B-1, C-4, D-3', 'A-1, B-2, C-4, D-3', 'A-2, B-4, C-1, D-3', 'A-3, B-1, C-4, D-2']
        },
        "correct": 0,
        "expl_en": 'Citrus canker is bacterial (Xanthomonas citri); Potato spindle tuber is caused by a viroid; Mad cow disease is caused by prions; Sleeping sickness is caused by Trypanosoma gambiense.',
        "expl_bn": 'সাইট্রাস ক্যাঙ্কার ব্যাকটেরিয়া ঘটিত (A-2); পটেটো স্পিন্ডল টিউবার ভিরয়েড ঘটিত (B-1); ম্যাড কাউ প্রিয়ন ঘটিত (C-4); স্লিপিং সিকনেস ট্রাইপ্যানোসোমা ঘটিত (D-3)।',
    },
    {
        "id": 'BIO-BC-126',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Match Column-I (Phylum/Group) with Column-II (Asexual spore type):<br>A. Phycomycetes<br>B. Ascomycetes<br>C. Basidiomycetes<br>D. Deuteromycetes<br>1. Conidia produced exogenously on conidiophores<br>2. Zoospores (motile) or Aplanospores (non-motile) endogenously inside sporangium<br>3. Asexual spores are generally NOT found; vegetative reproduction by fragmentation is common<br>4. Only conidia (no sexual spores known)',
        "bn": 'কলাম-I (শ্রেণি)-এর সাথে কলাম-II (অযৌন স্পোরের ধরণ) মেলাও:<br>A. ফাইকোমাইসিটিস<br>B. অ্যাসকোমাইসিটিস<br>C. ব্যাসিডিওমাইসিটিস<br>D. ডিউটেরোমাইসিটিস<br>1. কনিডিওফোরের ওপর বহির্জনিষ্ণুভাবে উৎপন্ন কনিডিয়া<br>2. স্পোরাঞ্জিয়ামের মধ্যে অন্তর্জনিষ্ণুভাবে উৎপন্ন জুস্পোর বা অ্যাপ্ল্যানোস্পোর<br>3. অযৌন স্পোর সাধারণত অনুপস্থিত; খণ্ডীভবন দ্বারা অঙ্গজ জনন ঘটে<br>4. কেবল কনিডিয়া (যৌন স্পোর সম্পূর্ণ অনুপস্থিত)',
        "opts": {
            "en": ['A-2, B-1, C-3, D-4', 'A-1, B-2, C-3, D-4', 'A-2, B-3, C-1, D-4', 'A-4, B-1, C-3, D-2'],
            "bn": ['A-2, B-1, C-3, D-4', 'A-1, B-2, C-3, D-4', 'A-2, B-3, C-1, D-4', 'A-4, B-1, C-3, D-2']
        },
        "correct": 0,
        "expl_en": 'Phycomycetes: zoospores/aplanospores endogenously in sporangia (A-2); Ascomycetes: conidia exogenously on conidiophores (B-1); Basidiomycetes: asexual spores generally absent (C-3); Deuteromycetes: conidia only (D-4).',
        "expl_bn": 'ফাইকোমাইসিটিস = জুস্পোর/অ্যাপ্ল্যানোস্পোর (A-2); অ্যাসকোমাইসিটিস = কনিডিয়া (B-1); ব্যাসিডিওমাইসিটিস = অযৌন স্পোর নেই (C-3); ডিউটেরোমাইসিটিস = কেবল কনিডিয়া (D-4)।',
    },
    {
        "id": 'BIO-BC-127',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Which of the following organisms shows the presence of heterotrophic nutrition through phagocytosis in an animal-like manner while lacking a cell wall?',
        "bn": 'কোষপ্রাচীরহীন নিচের কোন জীবটি প্রাণীদের ন্যায় ফ্যাগোসাইটোসিস পদ্ধতিতে পরভোজী পুষ্টি সম্পন্ন করে?',
        "opts": {
            "en": ['Amoeba proteus', 'Nostoc commune', 'Anabaena azollae', 'Chlamydomonas reinhardtii'],
            "bn": ['অ্যামিবা (Amoeba proteus)', 'নস্টক', 'অ্যানাবিনা', 'ক্ল্যামাইডোমোনাস']
        },
        "correct": 0,
        "expl_en": 'Amoeba proteus is a unicellular protozoan lacking a cell wall that ingests food particles by phagocytosis using pseudopodia.',
        "expl_bn": 'অ্যামিবার কোনো কোষপ্রাচীর থাকে না এবং এরা ক্ষণপদের মাধ্যমে ফ্যাগোসাইটোসিস পদ্ধতিতে খাদ্য গ্রহণ করে।',
    },
    {
        "id": 'BIO-BC-128',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Genetic material in majority of plant viruses (like TMV) is:',
        "bn": 'অধিকাংশ উদ্ভিদ ভাইরাসের (যেমন TMV) বংশগত পদার্থ বা জেনেটিক উপাদান কী?',
        "opts": {
            "en": ['Single-stranded RNA (ssRNA)', 'Double-stranded DNA (dsDNA)', 'Double-stranded RNA (dsRNA)', 'Single-stranded DNA (ssDNA)'],
            "bn": ['একতন্ত্রী RNA (ssRNA)', 'দ্বিতন্ত্রী DNA (dsDNA)', 'দ্বিতন্ত্রী RNA (dsRNA)', 'একতন্ত্রী DNA (ssDNA)']
        },
        "correct": 0,
        "expl_en": 'As per NCERT: In general, viruses that infect plants have single stranded RNA and viruses that infect animals have either single or double stranded RNA or double stranded DNA.',
        "expl_bn": 'NCERT অনুসারে, সাধারণ নিয়মে উদ্ভিদ আক্রমণকারী ভাইরাসে একতন্ত্রী RNA (ssRNA) থাকে।',
    },
    {
        "id": 'BIO-BC-129',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": "Which among the following fungi is widely exploited in biochemical and genetic research, earning the moniker 'Drosophila of the plant kingdom'?",
        "bn": 'নিচের কোন ছত্রাকটিকে প্রাণিজগতের ড্রসোফিলার সাথে তুলনা করে জৈব রাসায়নিক ও বংশগতিবিদ্যার গবেষণায় ব্যাপকভাবে ব্যবহার করা হয়?',
        "opts": {
            "en": ['Neurospora crassa', 'Rhizopus nigricans', 'Agaricus campestris', 'Saccharomyces cerevisiae'],
            "bn": ['নিউরোস্পোরা (Neurospora crassa)', 'রাইজোপাস', 'অ্যাগারিকাস', 'স্যাকারোমাইসিস']
        },
        "correct": 0,
        "expl_en": "Neurospora is an ascomycete fungus used extensively in biochemical genetics (e.g., Beadle and Tatum's 'one gene-one enzyme' hypothesis).",
        "expl_bn": 'নিউরোস্পোরা (Neurospora) ছত্রাকটি জেনেটিক্স ও জৈব রাসায়নিক গবেষণায় সর্বাধিক ব্যবহৃত হয়।',
    },
    {
        "id": 'BIO-BC-130',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Which of the following is an example of an obligate intracellular parasite?',
        "bn": 'নিচের কোনটি বাধ্যতামূলক অন্তর্কোষীয় পরজীবীর (obligate intracellular parasite) প্রকৃষ্ট উদাহরণ?',
        "opts": {
            "en": ['Tobacco Mosaic Virus (TMV)', 'Rhizopus', 'Agaricus', 'Lactobacillus'],
            "bn": ['টোবাকো মোজাইক ভাইরাস (TMV)', 'রাইজোপাস', 'অ্যাগারিকাস', 'ল্যাকটোব্যাসিলাস']
        },
        "correct": 0,
        "expl_en": 'Viruses (like TMV) are obligate intracellular parasites; they cannot metabolize or replicate outside a living host cell.',
        "expl_bn": 'ভাইরাস হলো বাধ্যতামূলক অন্তর্কোষীয় পরজীবী কারণ পোষক কোষের বাইরে এরা সম্পূর্ণ নিষ্ক্রিয়।',
    },
    {
        "id": 'BIO-BC-131',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'Which group of organisms possesses two flagella, one lying longitudinally and the other transversely in a furrow between the wall plates?',
        "bn": 'কোন শ্রেণির জীবের ক্ষেত্রে দুটি ফ্ল্যাজেলা থাকে—একটি অনুদৈর্ঘ্যভাবে এবং অন্যটি প্রাচীর ফলকদ্বয়ের মধ্যবর্তী খাঁজে অনুপ্রস্থভাবে বিন্যস্ত?',
        "opts": {
            "en": ['Dinoflagellates', 'Euglenoids', 'Chrysophytes', 'Slime moulds'],
            "bn": ['ডাইনোফ্ল্যাজেলেট (Dinoflagellates)', 'ইউগ্লেনয়েড', 'ক্রাইসোফাইট', 'স্লাইম মোল্ড']
        },
        "correct": 0,
        "expl_en": 'Dinoflagellates are characterized by two flagella: one directed longitudinally and another running transversely in a groove (sulcus and cingulum) between cellulosic plates.',
        "expl_bn": 'ডাইনোফ্ল্যাজেলেটের দুটি ফ্ল্যাজেলা থাকে: একটি অনুদৈর্ঘ্য এবং অপরটি প্রাচীরের খাঁজে অনুপ্রস্থভাবে অবস্থিত।',
    },
    {
        "id": 'BIO-BC-132',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Medium',
        "en": 'The protein coat of viruses that surrounds the nucleic acid and is composed of small structural subunits is called:',
        "bn": 'ভাইরাসের নিউক্লিক অ্যাসিডকে ঘিরে থাকা প্রোটিনের আবরণীকে কী বলে, যা ক্ষুদ্র ক্ষুদ্র একক দ্বারা গঠিত?',
        "opts": {
            "en": ['Capsid, composed of capsomeres', 'Pellicle, composed of tubulin', 'Peptidoglycan, composed of NAM and NAG', 'Lipopolysaccharide envelope, composed of teichoic acids'],
            "bn": ['ক্যাপসিড (Capsid), যা ক্যাপসোমিয়ার (Capsomeres) একক দ্বারা গঠিত', 'পেলিকল, যা টিউবুলিন দ্বারা গঠিত', 'পেপটিডোগ্লাইক্যান, যা NAM ও NAG দ্বারা গঠিত', 'লিপোপলিস্যাকারাইড, যা টাইকোয়িক অ্যাসিড দ্বারা গঠিত']
        },
        "correct": 0,
        "expl_en": 'The viral protein coat is termed the capsid, made up of repetitive subunits called capsomeres arranged in helical or polyhedral geometric forms.',
        "expl_bn": 'ভাইরাসের প্রোটিন আবরণকে ক্যাপসিড বলে এবং এর প্রতিটি উপ-একককে ক্যাপসোমিয়ার বলা হয়।',
    },
    {
        "id": 'BIO-BC-133',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Easy',
        "en": 'Which of the following structures is absent in both Kingdom Monera and Kingdom Protista?',
        "bn": 'নিচের কোন বৈশিষ্ট্যটি মনেরা এবং প্রোটিস্টা উভয় রাজ্যের জীবদের মধ্যেই অনুপস্থিত?',
        "opts": {
            "en": ['Multicellular tissue-level body organization', 'Ribosomes for translation', 'Genetic material composed of nucleic acids', 'Plasma membrane encompassing the cytoplasm'],
            "bn": ['বহুকোষীয় কলা-মাত্রার দৈহিক সংগঠন (Tissue-level organization)', 'প্রোটিন তৈরির জন্য রাইবোজোম', 'নিউক্লিক অ্যাসিড নির্মিত বংশগত বস্তু', 'সাইটোপ্লাজমকে আবৃতকারী প্লাজমা পর্দা']
        },
        "correct": 0,
        "expl_en": 'Monerans and Protistans are unicellular (cellular grade of organization). Tissue level organization first arises in multicellular Metazoans and higher Embryophytes.',
        "expl_bn": 'মনেরা ও প্রোটিস্টা উভয় রাজ্যের জীবরাই এককোষী। কোনোটিতেই কলা-মাত্রার সংগঠন দেখা যায় না।',
    },
    {
        "id": 'BIO-BC-134',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'How many of the following organisms belong to Kingdom Monera?<br>[Anabaena, Nostoc, Euglena, Paramecium, Methanococcus, Mycoplasma, Amoeba, Gonyaulax, Chlorella]',
        "bn": 'প্রদত্ত জীবগুলির মধ্যে কতগুলি মনেরা (Monera) রাজ্যের অন্তর্গত?<br>[Anabaena, Nostoc, Euglena, Paramecium, Methanococcus, Mycoplasma, Amoeba, Gonyaulax, Chlorella]',
        "opts": {
            "en": ['4 (Anabaena, Nostoc, Methanococcus, Mycoplasma)', '5', '6', '3'],
            "bn": ['৪টি (Anabaena, Nostoc, Methanococcus, Mycoplasma)', '৫টি', '৬টি', '৩টি']
        },
        "correct": 0,
        "expl_en": 'Monerans are prokaryotes: Anabaena, Nostoc (Cyanobacteria), Methanococcus (Archaebacteria), Mycoplasma (prokaryote without cell wall) = 4 organisms. Euglena, Paramecium, Amoeba, Gonyaulax, and Chlorella are unicellular eukaryotes belonging to Protista (or plant kingdom traditionally for Chlorella).',
        "expl_bn": 'মনেরার অন্তর্গত প্রোক্যারিওট হলো ৪টি: Anabaena, Nostoc, Methanococcus এবং Mycoplasma। বাকিগুলি ইউক্যারিওট (প্রোটিস্টা)।',
    },
    {
        "id": 'BIO-BC-135',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Biological Classification',
        "difficulty": 'Hard',
        "en": 'Which of the following represents the correct evolutionary progression of the main criteria used in biological classification from Artificial to Natural and then Phylogenetic systems?',
        "bn": 'শ্রেণীবিন্যাসের কৃত্রিম পদ্ধতি থেকে প্রাকৃতিক এবং পরবর্তীতে জাতিজনি (Phylogenetic) পদ্ধতিতে রূপান্তরের ক্ষেত্রে প্রধান মানদণ্ডের সঠিক বিবর্তনীয় ক্রম কোনটি?',
        "opts": {
            "en": ['Superficial morphological characters (habit, colour) → Natural affinities (anatomy, embryology, phytochemistry) → Evolutionary relationships (phylogeny and genetic lineage)', 'Evolutionary relationships → Gross morphology → Chromosomal numbers', 'Cytological data → Gross morphology → Floral numerical taxonomy', 'Single sexual floral character → Phylogenetic lineages → Embryological traits'],
            "bn": ['বাহ্যিক অঙ্গসংস্থানিক বৈশিষ্ট্য (আবাস, বর্ণ) → প্রাকৃতিক সাদৃশ্য (শারীরস্থান, ভ্রূণতত্ত্ব, ফাইটোকেমিস্ট্রি) → বিবর্তনীয় বা জাতিজনি সম্পর্ক (Phylogenetic lineage)', 'বিবর্তনীয় সম্পর্ক → স্থূল অঙ্গসংস্থান → ক্রোমোজোম সংখ্যা', 'কোশতত্ত্ব → স্থূল অঙ্গসংস্থান → ফ্লোরাল সংখ্যাগত শ্রেণীবিন্যাস', 'একটিমাত্র পুংকেশরীয় বৈশিষ্ট্য → জাতিজনি বিন্যাস → ভ্রূণতত্ত্ব']
        },
        "correct": 0,
        "expl_en": "Classification evolved from Linnaeus's artificial system (based on habit, androecium characters) to Bentham & Hooker's natural system (internal anatomy, embryology, affinities) to modern phylogenetic systems (Engler-Prantl, Hutchinson, Whittaker) reflecting evolutionary lineages.",
        "expl_bn": 'শ্রেণীবিন্যাস লিনিয়াসের কৃত্রিম পদ্ধতি (বাহ্যিক গঠন) থেকে বেন্থাম ও হুকারের প্রাকৃতিক পদ্ধতি (অভ্যন্তরীণ শারীরস্থান ও ভ্রূণতত্ত্ব) এবং সেখান থেকে আধুনিক জাতিজনি পদ্ধতিতে (বিবর্তনীয় সম্পর্ক) বিকশিত হয়েছে।',
    },
    {
        "id": 'BIO-PK-001',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Artificial systems of classification gave equal weightage to vegetative and sexual characteristics. This was unacceptable because:',
        "bn": 'শ্রেণীবিন্যাসের কৃত্রিম পদ্ধতিতে অঙ্গজ এবং যৌন বৈশিষ্ট্যকে সমান গুরুত্ব দেওয়া হয়েছিল। এটি অগ্রহণযোগ্য ছিল কারণ:',
        "opts": {
            "en": ['Vegetative characters are more easily affected by environmental factors', 'Sexual characters are easily altered by environmental variations', 'Vegetative characters never vary across seasons', 'Sexual organs are non-functional in lower cryptogams'],
            "bn": ['অঙ্গজ বৈশিষ্ট্যগুলি পরিবেশগত কারণ দ্বারা অনেক বেশি সহজে প্রভাবিত ও পরিবর্তিত হয়', 'যৌন বৈশিষ্ট্যগুলি পরিবেশ দ্বারা সহজে পরিবর্তিত হয়', 'অঙ্গজ বৈশিষ্ট্য ঋতু পরিবর্তনের সাথে কখনোই পরিবর্তিত হয় না', 'নিম্নশ্রেণীর ক্রিপ্টোগ্যামে জননাঙ্গ নিষ্ক্রিয় থাকে']
        },
        "correct": 0,
        "expl_en": 'According to NCERT, artificial systems gave equal weightage to vegetative and sexual characteristics; this is not acceptable since we know that often vegetative characters are more easily affected by environment.',
        "expl_bn": 'NCERT অনুসারে, কৃত্রিম শ্রেণীবিন্যাসে অঙ্গজ ও জনন বৈশিষ্ট্যকে সমান গুরুত্ব দেওয়া হয়েছিল; এটি ঠিক নয় কারণ অঙ্গজ বৈশিষ্ট্যগুলি পরিবেশের প্রভাবে সহজে পরিবর্তিত হয়ে যায়।',
    },
    {
        "id": 'BIO-PK-002',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": "Bentham and Hooker's system of classification of seeded plants is an example of:",
        "bn": 'বেন্থাম ও হুকার কর্তৃক বীজযুক্ত উদ্ভিদের শ্রেণীবিন্যাস পদ্ধতিটি কিসের উদাহরণ?',
        "opts": {
            "en": ['Natural system of classification based on natural affinities', 'Artificial system based only on habit and stamens', 'Phylogenetic system based strictly on evolutionary ancestry', 'Chemotaxonomic system based purely on DNA sequencing'],
            "bn": ['প্রাকৃতিক সাদৃশ্যের ওপর ভিত্তি করে রচিত প্রাকৃতিক শ্রেণীবিন্যাস পদ্ধতি (Natural system)', 'কেবল অভ্যাস ও পুংকেশরের ওপর ভিত্তি করে রচিত কৃত্রিম পদ্ধতি', 'বিবর্তনীয় পূর্বপুরুষের ওপর ভিত্তি করে রচিত জাতিজনি পদ্ধতি', 'DNA সিকোয়েন্সিং-এর ওপর ভিত্তি করে কেমোট্যাক্সনমিক পদ্ধতি']
        },
        "correct": 0,
        "expl_en": 'George Bentham and Joseph Dalton Hooker proposed the famous Natural System of classification, taking into account not only external features but also internal features like ultrastructure, anatomy, embryology, and phytochemistry.',
        "expl_bn": 'জর্জ বেন্থাম ও জে. ডি. হুকার প্রাকৃতিক শ্রেণীবিন্যাস পদ্ধতি প্রবর্তন করেন, যেখানে বাহ্যিক বৈশিষ্ট্যের পাশাপাশি অভ্যন্তরীণ শারীরস্থান, ভ্রূণতত্ত্ব এবং রাসায়নিক সাদৃশ্য বিবেচনা করা হয়।',
    },
    {
        "id": 'BIO-PK-003',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Phylogenetic systems of classification are based on:',
        "bn": 'জাতিজনি (Phylogenetic) শ্রেণীবিন্যাস পদ্ধতি মূলত কিসের ওপর প্রতিষ্ঠিত?',
        "opts": {
            "en": ['Evolutionary relationships between various organisms', 'Morphological similarities of vegetative stems only', 'Number and morphology of chromosomes only', 'Geographical distribution of current flora'],
            "bn": ['বিভিন্ন জীবের মধ্যে বিবর্তনীয় বা জাতিজনি সম্পর্ক (Evolutionary relationships)', 'কেবল অঙ্গজ কাণ্ডের রূপতাত্ত্বিক সাদৃশ্য', 'কেবল ক্রোমোজোমের সংখ্যা ও গঠন', 'বর্তমান উদ্ভিদকুলের ভৌগোলিক বিস্তৃতি']
        },
        "correct": 0,
        "expl_en": 'Phylogenetic classification systems assume that organisms belonging to the same taxa have a common ancestor, organizing taxa according to their evolutionary lineages.',
        "expl_bn": 'জাতিজনি শ্রেণীবিন্যাস পদ্ধতি বিবর্তনীয় সম্পর্কের ওপর ভিত্তি করে গড়ে উঠেছে, যা মনে করে একই ট্যাক্সনের অন্তর্ভুক্ত জীবেরা অভিন্ন পূর্বপুরুষ থেকে উদ্ভূত।',
    },
    {
        "id": 'BIO-PK-004',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Taxonomy that is based on all observable characteristics, utilizing computers where number and codes are assigned to each character, is called:',
        "bn": 'সমস্ত পর্যবেক্ষণযোগ্য বৈশিষ্ট্যের ওপর ভিত্তি করে কম্পিউটারের সাহায্যে কোড ও নম্বর বরাদ্দ করে যে শ্রেণীবিন্যাস করা হয়, তাকে কী বলে?',
        "opts": {
            "en": ['Numerical taxonomy (Phenetics)', 'Cytotaxonomy', 'Chemotaxonomy', 'Cladistics'],
            "bn": ['সংখ্যাগত ট্যাক্সনমি বা নিউমেরিক্যাল ট্যাক্সনমি (Numerical taxonomy)', 'সাইটোট্যাক্সনমি', 'কেমোট্যাক্সনমি', 'ক্ল্যাডিস্টিকস']
        },
        "correct": 0,
        "expl_en": 'Numerical taxonomy uses computers and considers hundreds of observable characters simultaneously, assigning numbers and equal weightage to each character.',
        "expl_bn": 'সংখ্যাগত ট্যাক্সনমি বা নিউমেরিক্যাল ট্যাক্সনমিতে কম্পিউটারের সাহায্যে সমস্ত পর্যবেক্ষণযোগ্য বৈশিষ্ট্যকে কোড বরাদ্দ করে একই সাথে শত শত বৈশিষ্ট্যের মূল্যায়ন করা হয়।',
    },
    {
        "id": 'BIO-PK-005',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Cytotaxonomy is based on cytological information including:',
        "bn": 'সাইটোট্যাক্সনমি (Cytotaxonomy) কোন কোষীয় তথ্যাবলীর ওপর প্রতিষ্ঠিত?',
        "opts": {
            "en": ['Chromosome number, structure, and behavior during meiosis', 'Chemical constituents like alkaloids and carotenoids', 'Gross leaf morphology and floral diagrams', 'Fossil pollen records in sedimentary rocks'],
            "bn": ['ক্রোমোজোম সংখ্যা, গঠন এবং মায়োসিস বিভাজনের সময় তাদের আচরণ', 'অ্যালকালয়েড ও ক্যারোটিনয়েডের মতো রাসায়নিক উপাদান', 'পাতার বাহ্যিক গঠন ও পুষ্প নকশা', 'পাললিক শিলায় সংরক্ষিত পরাগরেণুর জীবাশ্ম']
        },
        "correct": 0,
        "expl_en": 'Cytotaxonomy is based on cytological details such as chromosome number, chromosome morphology/structure, and their meiotic behavior.',
        "expl_bn": 'সাইটোট্যাক্সনমি কোষতাত্ত্বিক তথ্য যেমন ক্রোমোজোমের সংখ্যা, গঠন এবং জননকোষ বিভাজনে তাদের আচরণের ওপর ভিত্তি করে রচিত।',
    },
    {
        "id": 'BIO-PK-006',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Chemotaxonomy uses which of the following to resolve taxonomic confusions?',
        "bn": 'ট্যাক্সনমিক বিভ্রান্তি দূর করতে কেমোট্যাক্সনমিতে (Chemotaxonomy) নিচের কোনটি ব্যবহার করা হয়?',
        "opts": {
            "en": ['Chemical constituents of the plant (DNA, proteins, secondary metabolites)', 'External floral symmetry and petal coloration', 'Soil mineral profile where the plant grows', 'Atmospheric humidity and rainfall requirements'],
            "bn": ['উদ্ভিদের রাসায়নিক উপাদান (DNA, প্রোটিন, গৌণ বিপাকীয় পদার্থ)', 'ফুলের প্রতিসাম্য ও দলের রঙ', 'উদ্ভিদ যে মাটিতে জন্মায় তার খনিজ উপাদান', 'বায়ুর আর্দ্রতা ও বার্ষিক বৃষ্টিপাতের চাহিদা']
        },
        "correct": 0,
        "expl_en": 'Chemotaxonomy utilizes the chemical constituents of plants (amino acids, aromatic compounds, DNA sequences) to resolve taxonomic ambiguities.',
        "expl_bn": 'কেমোট্যাক্সনমিতে উদ্ভিদের নিজস্ব রাসায়নিক উপাদান যেমন প্রোটিন, অ্যামিনো অ্যাসিড, অ্যালকালয়েড ও নিউক্লিক অ্যাসিড বিশ্লেষণ করে শ্রেণীবিন্যাস করা হয়।',
    },
    {
        "id": 'BIO-PK-007',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Algae are chlorophyll-bearing, simple, thalloid, avascular, and largely:',
        "bn": 'শৈবাল হলো ক্লোরোফিলযুক্ত, সরল, সমাঙ্গদেহী (thalloid), সংবহনকলাহীন এবং প্রধানত:',
        "opts": {
            "en": ['Aquatic organisms (both fresh water and marine)', 'Obligate xerophytes inhabiting desert sand dunes', 'Subterranean root-dwelling parasitic organisms', 'Epiphytic organisms found exclusively on animal horns'],
            "bn": ['জলজ জীব (মিষ্ট জল এবং সামুদ্রিক উভয় পরিবেশেই)', 'মরুভূমির বালিয়াড়িতে বসবাসকারী বাধ্যতামূলক জেরোফাইট', 'মাটির নিচে শিকড়ে বসবাসকারী পরজীবী', 'প্রাণীর শিং-এর ওপর বসবাসকারী পরাশ্রয়ী']
        },
        "correct": 0,
        "expl_en": 'Algae are chlorophyll-bearing, simple, thalloid, autotrophic and largely aquatic (both fresh water and marine) organisms.',
        "expl_bn": 'শৈবাল হলো ক্লোরোফিলযুক্ত, সরল, থ্যালয়েড, স্বভোজী এবং প্রধানত জলজ জীব (মিষ্ট জল এবং সামুদ্রিক নোনা জলে বসবাসকারী)।',
    },
    {
        "id": 'BIO-PK-008',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following forms of algae is colonial?',
        "bn": 'নিচের শৈবালগুলির মধ্যে কোনটি উপনিবেশী বা কলোনিয়াল (colonial)?',
        "opts": {
            "en": ['Volvox', 'Chlamydomonas', 'Ulothrix', 'Spirogyra'],
            "bn": ['ভলভক্স (Volvox)', 'ক্ল্যামাইডোমোনাস', 'ইউলোথ্রিক্স', 'স্পাইরোগাইরা']
        },
        "correct": 0,
        "expl_en": 'Volvox is a colonial green alga forming spherical colonies called coenobia. Chlamydomonas is unicellular; Ulothrix and Spirogyra are filamentous.',
        "expl_bn": 'ভলভক্স (Volvox) একটি উপনিবেশী (colonial) সবুজ শৈবাল। ক্ল্যামাইডোমোনাস এককোষী এবং ইউলোথ্রিক্স ও স্পাইরোগাইরা সূত্রাকার শৈবাল।',
    },
    {
        "id": 'BIO-PK-009',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following algae are filamentous in organization?',
        "bn": 'নিচের শৈবালগুলির মধ্যে কোনগুলি সূত্রাকার (filamentous) গঠনের অধিকারী?',
        "opts": {
            "en": ['Ulothrix and Spirogyra', 'Volvox and Chlamydomonas', 'Chlorella and Acetabularia', 'Kelps and Sargassum'],
            "bn": ['ইউলোথ্রিক্স এবং স্পাইরোগাইরা', 'ভলভক্স এবং ক্ল্যামাইডোমোনাস', 'ক্লোরেলা এবং অ্যাসিটাবুলারিয়া', 'কেল্প এবং সারগাসাম']
        },
        "correct": 0,
        "expl_en": 'Ulothrix and Spirogyra are classic examples of unbranched filamentous green algae.',
        "expl_bn": 'ইউলোথ্রিক্স (Ulothrix) এবং স্পাইরোগাইরা (Spirogyra) হলো অশাখ সূত্রাকার সবুজ শৈবালের উদাহরণ।',
    },
    {
        "id": 'BIO-PK-010',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Massive marine plant bodies reaching heights of up to 100 metres are formed by brown algae known as:',
        "bn": '১০০ মিটার পর্যন্ত উচ্চতা বিশিষ্ট বিশাল সামুদ্রিক উদ্ভিদদেহ গঠনকারী বাদামী শৈবালকে কী বলা হয়?',
        "opts": {
            "en": ['Kelps', 'Porphyra', 'Gracilaria', 'Gelidium'],
            "bn": ['কেল্প (Kelps)', 'পরফাইরা', 'গ্র্যাসিলেয়ারিয়া', 'জেলিডিয়াম']
        },
        "correct": 0,
        "expl_en": 'Kelps (such as Macrocystis) are giant marine brown algae (Phaeophyceae) that possess massive plant bodies extending up to 100 meters.',
        "expl_bn": 'কেল্প (Kelps) হলো বিশাল সামুদ্রিক বাদামী শৈবাল যা ১০০ মিটার পর্যন্ত লম্বা হতে পারে।',
    },
    {
        "id": 'BIO-PK-011',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Isogamous sexual reproduction with FLAGELLATED gametes is observed in:',
        "bn": 'ফ্ল্যাজেলাযুক্ত চলনক্ষম গ্যামেটের সমন্বয়ে আইসোগ্যামাস (Isogamous) যৌন জনন কোনটিতে দেখা যায়?',
        "opts": {
            "en": ['Ulothrix (and flagellated forms of Chlamydomonas)', 'Spirogyra (non-flagellated)', 'Volvox (oogamous)', 'Fucus (oogamous)'],
            "bn": ['ইউলোথ্রিক্স (Ulothrix) - চলনক্ষম ফ্ল্যাজেলাযুক্ত', 'স্পাইরোগাইরা (চলনহীন গ্যামেট)', 'ভলভক্স (উগ্যামাস)', 'ফিউকাস (উগ্যামাস)']
        },
        "correct": 0,
        "expl_en": 'In Ulothrix, gametes are similar in size (isogamous) and flagellated (motile). In Spirogyra, gametes are similar in size but non-flagellated (non-motile).',
        "expl_bn": 'ইউলোথ্রিক্সে একই আকারের চলনক্ষম (ফ্ল্যাজেলাযুক্ত) গ্যামেটের মিলন ঘটে যা আইসোগ্যামির উদাহরণ। স্পাইরোগাইরায় গ্যামেটগুলি সমআকারের কিন্তু চলনহীন (ফ্ল্যাজেলাবিহীন)।',
    },
    {
        "id": 'BIO-PK-012',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Isogamous sexual reproduction involving NON-FLAGELLATED (non-motile) but similar-sized gametes is seen in:',
        "bn": 'ফ্ল্যাজেলাবিহীন (চলনহীন) অথচ সমআকৃতির গ্যামেটের সমন্বয়ে আইসোগ্যামাস যৌন জনন কোনটিতে দেখা যায়?',
        "opts": {
            "en": ['Spirogyra', 'Ulothrix', 'Volvox', 'Fucus'],
            "bn": ['স্পাইরোগাইরা (Spirogyra)', 'ইউলোথ্রিক্স', 'ভলভক্স', 'ফিউকাস']
        },
        "correct": 0,
        "expl_en": 'As per NCERT: Gametes can be non-flagellated (non-motile) but similar in size, as in Spirogyra. Such reproduction is called isogamous.',
        "expl_bn": 'NCERT অনুসারে: স্পাইরোগাইরায় গ্যামেট দুটি ফ্ল্যাজেলাবিহীন বা চলনহীন কিন্তু আকারে সমান হয়, যা আইসোগ্যামির একটি দৃষ্টান্ত।',
    },
    {
        "id": 'BIO-PK-013',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Fusion of two gametes that are DISSIMILAR in size (as in some species of Eudorina) is termed:',
        "bn": 'আকারে অসদৃশ দুটি গ্যামেটের মিলনকে (যেমন ইউডোরিনার ক্ষেত্রে) কী বলা হয়?',
        "opts": {
            "en": ['Anisogamous', 'Isogamous', 'Oogamous', 'Parthenogenesis'],
            "bn": ['অ্যানাইসোগ্যামাস (Anisogamous)', 'আইসোগ্যামাস', 'উগ্যামাস', 'পার্থেনোজেনেসিস']
        },
        "correct": 0,
        "expl_en": 'Fusion of two gametes dissimilar in size, as in species of Eudorina, is termed anisogamous.',
        "expl_bn": 'আকারে ভিন্ন বা অসদৃশ দুটি গ্যামেটের মিলনকে অ্যানাইসোগ্যামি (Anisogamy) বলা হয় (যেমন Eudorina শৈবালে)।',
    },
    {
        "id": 'BIO-PK-014',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Fusion between one large, non-motile female gamete and a smaller, motile male gamete is termed:',
        "bn": 'একটি বৃহৎ ও নিশ্চল স্ত্রী গ্যামেট এবং একটি ক্ষুদ্র ও চলনক্ষম পুং গ্যামেটের মিলনকে কী বলা হয়?',
        "opts": {
            "en": ['Oogamous (e.g., Volvox, Fucus)', 'Isogamous (e.g., Spirogyra)', 'Anisogamous (e.g., Eudorina)', 'Syngamy of zoospores'],
            "bn": ['উগ্যামাস (Oogamous) - যেমন ভলভক্স, ফিউকাস', 'আইসোগ্যামাস - যেমন স্পাইরোগাইরা', 'অ্যানাইসোগ্যামাস - যেমন ইউডোরিনা', 'জুস্পোরের মিলন']
        },
        "correct": 0,
        "expl_en": 'Fusion between one large, static female gamete and a smaller, motile male gamete is termed oogamous (e.g., Volvox, Fucus).',
        "expl_bn": 'একটি বৃহৎ নিশ্চল ডিম্বাণুর সাথে একটি ক্ষুদ্র সচল শুক্রাণুর মিলনকে উগ্যামি (Oogamy) বলে। উদাহরণ: Volvox এবং Fucus।',
    },
    {
        "id": 'BIO-PK-015',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Hydrocolloids (water-holding substances) algin and carrageen are commercially extracted respectively from:',
        "bn": 'বাণিজ্যিকভাবে গুরুত্বপূর্ণ জলধারণকারী পদার্থ অ্যালজিন (algin) এবং ক্যারাগিন (carrageen) যথাক্রমে কোন শৈবাল থেকে নিষ্কাশন করা হয়?',
        "opts": {
            "en": ['Brown algae and Red algae', 'Red algae and Brown algae', 'Green algae and Blue-green algae', 'Brown algae and Green algae'],
            "bn": ['বাদামী শৈবাল এবং লাল শৈবাল', 'লাল শৈবাল এবং বাদামী শৈবাল', 'সবুজ শৈবাল এবং নীলাভ সবুজ শৈবাল', 'বাদামী শৈবাল এবং সবুজ শৈবাল']
        },
        "correct": 0,
        "expl_en": 'Certain marine brown and red algae produce large amounts of hydrocolloids; algin is obtained from brown algae and carrageen from red algae.',
        "expl_bn": 'অ্যালজিন পাওয়া যায় বাদামী শৈবাল (Phaeophyceae) থেকে এবং ক্যারাগিন পাওয়া যায় লাল শৈবাল (Rhodophyceae) থেকে।',
    },
    {
        "id": 'BIO-PK-016',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Agar, one of the commercial products used to grow microbes in culture media and in ice-creams and jellies, is obtained from:',
        "bn": 'অণুজীব কালচার মিডিয়ায় এবং আইসক্রিম ও জেলি তৈরিতে ব্যবহৃত বাণিজ্যিক উপাদান অ্যাগার (Agar) কোন শৈবাল থেকে প্রস্তুত হয়?',
        "opts": {
            "en": ['Gelidium and Gracilaria', 'Chlorella and Spirulina', 'Sargassum and Laminaria', 'Volvox and Ulothrix'],
            "bn": ['জেলিডিয়াম (Gelidium) এবং গ্র্যাসিলেয়ারিয়া (Gracilaria)', 'ক্লোরেলা এবং স্পিরুলিনা', 'সারগাসাম এবং ল্যামিনারিয়া', 'ভলভক্স এবং ইউলোথ্রিক্স']
        },
        "correct": 0,
        "expl_en": 'Agar is obtained from red algae Gelidium and Gracilaria. It is widely used to solidify laboratory culture media.',
        "expl_bn": 'অ্যাগার পাওয়া যায় লাল শৈবাল জেলিডিয়াম এবং গ্র্যাসিলেয়ারিয়া থেকে।',
    },
    {
        "id": 'BIO-PK-017',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Which unicellular green alga is rich in proteins and used as a food supplement even by space travellers?',
        "bn": 'কোন এককোষী সবুজ শৈবালটি প্রোটিন সমৃদ্ধ এবং মহাকাশচারীদের খাদ্য পরিপূরক হিসেবে ব্যবহৃত হয়?',
        "opts": {
            "en": ['Chlorella', 'Spirogyra', 'Chara', 'Ulva'],
            "bn": ['ক্লোরেলা (Chlorella)', 'স্পাইরোগাইরা', 'কারা', 'উলভা']
        },
        "correct": 0,
        "expl_en": 'Chlorella is a unicellular green alga rich in proteins and vitamins, utilized as a nutrient supplement including space research flights.',
        "expl_bn": 'ক্লোরেলা (Chlorella) হলো প্রোটিনসমৃদ্ধ এককোষী শৈবাল যা মহাকাশচারীদের খাদ্য পরিপূরক হিসেবে ব্যবহৃত হয়।',
    },
    {
        "id": 'BIO-PK-018',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The photosynthetic pigments present in members of Chlorophyceae (green algae) are:',
        "bn": 'ক্লোরোফাইসি (সবুজ শৈবাল)-এর অন্তর্ভুক্ত সদস্যদের প্রধান সালোকসংশ্লেষী রঞ্জকগুলি কী কী?',
        "opts": {
            "en": ['Chlorophyll a and Chlorophyll b localized in definite chloroplasts', 'Chlorophyll a and Chlorophyll c with fucoxanthin', 'Chlorophyll a and Chlorophyll d with r-phycoerythrin', 'Chlorophyll b and Chlorophyll d with phycocyanin'],
            "bn": ['নির্দিষ্ট ক্লোরোপ্লাস্টে অবস্থিত ক্লোরোফিল-a এবং ক্লোরোফিল-b', 'ফিউকোজ্যান্থিন সহ ক্লোরোফিল-a এবং ক্লোরোফিল-c', 'r-ফাইকোইরিথ্রিন সহ ক্লোরোফিল-a এবং ক্লোরোফিল-d', 'ফাইকোসায়ানিন সহ ক্লোরোফিল-b এবং ক্লোরোফিল-d']
        },
        "correct": 0,
        "expl_en": 'Members of Chlorophyceae are grass green due to the dominance of pigments chlorophyll a and b located in definite chloroplasts.',
        "expl_bn": 'ক্লোরোফাইসির প্রধান রঞ্জক হলো ক্লোরোফিল-a এবং ক্লোরোফিল-b, যা উচ্চশ্রেণীর উদ্ভিদের সাথে সাদৃশ্যপূর্ণ।',
    },
    {
        "id": 'BIO-PK-019',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Pyrenoids located in the chloroplasts of most green algae contain:',
        "bn": 'অধিকাংশ সবুজ শৈবালের ক্লোরোপ্লাস্টে অবস্থিত পাইরিনয়েড (Pyrenoids)-এর কেন্দ্রীয় অংশে ও বাইরে কী থাকে?',
        "opts": {
            "en": ['Protein in the centre surrounded by a starch sheath', 'Pure lipid droplets surrounded by protein coat', 'Glycogen core surrounded by cellulose crystals', 'Silica core surrounded by pectin layers'],
            "bn": ['কেন্দ্রে প্রোটিন এবং তাকে ঘিরে স্টার্চের আবরণ', 'প্রোটিন দ্বারা আবৃত খাঁটি লিপিডের কণা', 'সেলুলোজ দ্বারা আবৃত গ্লাইকোজেনের কেন্দ্র', 'পেকটিন দ্বারা আবৃত সিলিকার দানা']
        },
        "correct": 0,
        "expl_en": 'Most green algae possess one or more storage bodies called pyrenoids located in chloroplasts. Pyrenoids contain protein besides starch (protein core surrounded by starch sheath).',
        "expl_bn": 'পাইরিনয়েডের কেন্দ্রে প্রোটিন থাকে এবং তার চারপাশ স্টার্চ বা শ্বেতসারের আবরণী দ্বারা বেষ্টিত থাকে।',
    },
    {
        "id": 'BIO-PK-020',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The cell wall of green algae (Chlorophyceae) is characteristically rigid and made of an:',
        "bn": 'সবুজ শৈবালের (Chlorophyceae) দৃঢ় কোষপ্রাচীরের অভ্যন্তরীণ ও বহিঃস্থ স্তর যথাক্রমে কী দ্বারা গঠিত?',
        "opts": {
            "en": ['Inner layer of cellulose and outer layer of pectose', 'Inner layer of chitin and outer layer of silica', 'Inner layer of algin and outer layer of peptidoglycan', 'Inner layer of pectin and outer layer of lignin'],
            "bn": ['অভ্যন্তরীণ সেলুলোজ স্তর এবং বহিঃস্থ পেকটোজ স্তর', 'অভ্যন্তরীণ কাইটিন এবং বহিঃস্থ সিলিকা', 'অভ্যন্তরীণ অ্যালজিন এবং বহিঃস্থ পেপটিডোগ্লাইক্যান', 'অভ্যন্তরীণ পেকটিন এবং বহিঃস্থ লিগনিন']
        },
        "correct": 0,
        "expl_en": 'As per NCERT: Chlorophyceae members have a rigid cell wall made of an inner layer of cellulose and an outer layer of pectose.',
        "expl_bn": 'NCERT অনুসারে: সবুজ শৈবালের কোষপ্রাচীরের ভেতরের স্তরটি সেলুলোজ এবং বাইরের স্তরটি পেকটোজ দিয়ে গঠিত।',
    },
    {
        "id": 'BIO-PK-021',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In Chlorophyceae, the asexual flagellated zoospores possess:',
        "bn": 'ক্লোরোফাইসিতে অযৌন চলনক্ষম জুস্পোরের ফ্ল্যাজেলা সংক্রান্ত কোন বৈশিষ্ট্যটি সঠিক?',
        "opts": {
            "en": ['2 to 8 equal, apical flagella', '2 unequal, lateral flagella', 'No flagella at any stage', '1 single posterior whiplash flagellum'],
            "bn": ['২ থেকে ৮টি সমান দৈর্ঘ্যের অগ্রস্থ (apical) ফ্ল্যাজেলা', '২টি অসমান দৈর্ঘ্যের পার্শ্বীয় (lateral) ফ্ল্যাজেলা', 'কোনো দশাতেই ফ্ল্যাজেলা থাকে না', '১টি মাত্র পশ্চাৎ ফ্ল্যাজেলা']
        },
        "correct": 0,
        "expl_en": 'Zoospores of green algae (Chlorophyceae) have 2-8 flagella that are equal in size and inserted apically (at the anterior end).',
        "expl_bn": 'সবুজ শৈবালের জুস্পোরে ২-৮টি সমদৈর্ঘ্যের অগ্রস্থ (apical) ফ্ল্যাজেলা থাকে।',
    },
    {
        "id": 'BIO-PK-022',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following belongs to Chlorophyceae?',
        "bn": 'নিচের কোনটি ক্লোরোফাইসি (Chlorophyceae) শ্রেণির অন্তর্ভুক্ত?',
        "opts": {
            "en": ['Chlamydomonas, Volvox, Ulothrix, Spirogyra, and Chara', 'Ectocarpus, Dictyota, Laminaria, Sargassum, and Fucus', 'Polysiphonia, Porphyra, Gracilaria, and Gelidium', 'Nostoc, Anabaena, Spirulina, and Oscillatoria'],
            "bn": ['ক্ল্যামাইডোমোনাস, ভলভক্স, ইউলোথ্রিক্স, স্পাইরোগাইরা এবং কারা (Chara)', 'এক্টোকার্পাস, ডিকটিওটা, ল্যামিনারিয়া, সারগাসাম এবং ফিউকাস', 'পলিসাইফোনিয়া, পরফাইরা, গ্র্যাসিলেয়ারিয়া এবং জেলিডিয়াম', 'নস্টক, অ্যানাবিনা, স্পিরুলিনা এবং অস্সিলেটোরিয়া']
        },
        "correct": 0,
        "expl_en": 'Common examples of Chlorophyceae listed in NCERT: Chlamydomonas, Volvox, Ulothrix, Spirogyra and Chara.',
        "expl_bn": 'সবুজ শৈবালের সাধারণ উদাহরণ: Chlamydomonas, Volvox, Ulothrix, Spirogyra এবং Chara।',
    },
    {
        "id": 'BIO-PK-023',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Members of Phaeophyceae (brown algae) range in colour from olive green to various shades of brown depending upon the amount of the xanthophyll pigment called:',
        "bn": 'ফিওফাইসি (বাদামী শৈবাল)-র উদ্ভিদের বর্ণ জলপাই সবুজ থেকে বাদামীর বিভিন্ন শেড হওয়ার কারণ কোন জ্যান্থোফিল রঞ্জকের উপস্থিতি?',
        "opts": {
            "en": ['Fucoxanthin', 'r-phycoerythrin', 'Haematochrome', 'Lycopene'],
            "bn": ['ফিউকোজ্যান্থিন (Fucoxanthin)', 'r-ফাইকোইরিথ্রিন', 'হেমাটোক্রোম', 'লাইকোপিন']
        },
        "correct": 0,
        "expl_en": 'Brown algae possess chlorophyll a, c, carotenoids and xanthophylls; they vary in color depending on the proportion of the xanthophyll fucoxanthin.',
        "expl_bn": 'বাদামী শৈবালে ক্লোরোফিল a, c ছাড়াও প্রচুর পরিমাণে ফিউকোজ্যান্থিন নামক জ্যান্থোফিল রঞ্জক থাকার কারণে এদের বর্ণ বাদামী হয়।',
    },
    {
        "id": 'BIO-PK-024',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Food is stored in brown algae (Phaeophyceae) as complex carbohydrates in the form of:',
        "bn": 'ফিওফাইসি বা বাদামী শৈবালে সঞ্চিত খাদ্য জটিল শর্করা হিসেবে কোন রূপে অবস্থান করে?',
        "opts": {
            "en": ['Laminarin or Mannitol', 'Floridean starch', 'True starch with amylose and amylopectin', 'Glycogen and cyanophycean starch'],
            "bn": ['ল্যামিনারিন (Laminarin) অথবা ম্যানিটল (Mannitol)', 'ফ্লোরিডিয়ান স্টার্চ', 'অ্যামাইলোজ ও অ্যামাইলোপেকটিন যুক্ত সাধারণ স্টার্চ', 'গ্লাইকোজেনের দানা']
        },
        "correct": 0,
        "expl_en": 'In Phaeophyceae, reserve food is stored as complex carbohydrates, which may be in the form of laminarin or mannitol (an alcoholic sugar).',
        "expl_bn": 'বাদামী শৈবালে সঞ্চিত খাদ্য থাকে জটিল কার্বোহাইড্রেট ল্যামিনারিন অথবা ম্যানিটল হিসেবে।',
    },
    {
        "id": 'BIO-PK-025',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The cellulosic cell wall of brown algae is usually covered on the outside by a gelatinous coating of:',
        "bn": 'বাদামী শৈবালের সেলুলোজ কোষপ্রাচীরের বাইরে কোন জেলাটিনাস পদার্থের আবরণ থাকে?',
        "opts": {
            "en": ['Algin', 'Pectose', 'Carrageen', 'Chitin'],
            "bn": ['অ্যালজিন (Algin)', 'পেকটোজ', 'ক্যারাগিন', 'কাইটিন']
        },
        "correct": 0,
        "expl_en": 'The vegetative cells in brown algae have a cellulosic wall usually covered on the outside by a gelatinous coating of algin (a phycocolloid).',
        "expl_bn": 'বাদামী শৈবালের কোষপ্রাচীরের বাইরের দিকে অ্যালজিন (algin) নামক জেলাটিনাস আস্তরণ থাকে।',
    },
    {
        "id": 'BIO-PK-026',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The plant body of brown algae is usually attached to the substratum by a ________, and has a stalk, the ________ and leaf like photosynthetic organ the ________.',
        "bn": 'বাদামী শৈবালের উদ্ভিদদেহটি সাবস্ট্রেটামের সাথে যুক্ত থাকে ________ দ্বারা, এবং এতে একটি ডাঁটার মতো ________ এবং পাতার মতো সালোকসংশ্লেষী অঙ্গ ________ থাকে।',
        "opts": {
            "en": ['Holdfast, stipe, frond', 'Rhizoid, stem, leaf', 'Root, culm, lamina', 'Foot, seta, capsule'],
            "bn": ['হোল্ডফাস্ট (Holdfast), স্ট্রাইপ (Stipe), ফ্রন্ড (Frond)', 'রাইজয়েড, কাণ্ড, পাতা', 'মূল, পর্ব, ল্যামিনা', 'ফুট, সিটা, ক্যাপসুল']
        },
        "correct": 0,
        "expl_en": 'As per NCERT: The plant body is usually attached to the substratum by a holdfast, and has a stalk, the stipe and leaf like photosynthetic organ - the frond.',
        "expl_bn": 'NCERT অনুসারে: বাদামী শৈবালের দেহটি সাবস্ট্রেটামের সাথে হোল্ডফাস্ট দ্বারা যুক্ত থাকে; এর সাথে ডাঁটার মতো স্ট্রাইপ এবং পাতার মতো সালোকসংশ্লেষী ফ্রন্ড থাকে।',
    },
    {
        "id": 'BIO-PK-027',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Asexual zoospores in brown algae (Phaeophyceae) are distinctively:',
        "bn": 'ফিওফাইসি বা বাদামী শৈবালের অযৌন জুস্পোরগুলির বৈশিষ্ট্য কী?',
        "opts": {
            "en": ['Pear-shaped (pyriform) with two laterally attached unequal flagella', 'Spherical with 2-8 apical equal flagella', 'Non-motile and cup-shaped', 'Comma-shaped with a single anterior flagellum'],
            "bn": ['নাশপাতি আকৃতির (pyriform) এবং দুটি অসমান পার্শ্বীয় ফ্ল্যাজেলাযুক্ত', 'গোলাকার এবং ২-৮টি অগ্রস্থ সমান ফ্ল্যাজেলাযুক্ত', 'চলনহীন এবং বাটির মতো', 'কমা আকৃতির একটিমাত্র ফ্ল্যাজেলাযুক্ত']
        },
        "correct": 0,
        "expl_en": 'Zoospores in Phaeophyceae are pear-shaped (pyriform) and bear two laterally attached, heterokont (unequal in length and type) flagella.',
        "expl_bn": 'বাদামী শৈবালের জুস্পোরগুলি নাশপাতি আকৃতির (pyriform) হয় এবং এদের পাশে দুটি অসমান দৈর্ঘ্যের ফ্ল্যাজেলা যুক্ত থাকে।',
    },
    {
        "id": 'BIO-PK-028',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following is a simple branched, filamentous brown alga?',
        "bn": 'নিচের কোনটি একটি সরল শাখাযুক্ত সূত্রাকার বাদামী শৈবাল?',
        "opts": {
            "en": ['Ectocarpus', 'Kelps', 'Fucus', 'Dictyota'],
            "bn": ['এক্টোকার্পাস (Ectocarpus)', 'কেল্প', 'ফিউকাস', 'ডিকটিওটা']
        },
        "correct": 0,
        "expl_en": 'Brown algae range from simple branched, filamentous forms (Ectocarpus) to profusely branched forms (Kelps).',
        "expl_bn": 'এক্টোকার্পাস (Ectocarpus) হলো একটি সরল শাখাযুক্ত সূত্রাকার বাদামী শৈবাল।',
    },
    {
        "id": 'BIO-PK-029',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The predominant photosynthetic pigment giving members of Rhodophyceae their characteristic red colour is:',
        "bn": 'রোডোফাইসি (Rhodophyceae বা লাল শৈবাল)-র বিশিষ্ট লাল রঙের জন্য দায়ী প্রধান রঞ্জকটি কী?',
        "opts": {
            "en": ['r-phycoerythrin', 'Chlorophyll c', 'Fucoxanthin', 'c-phycocyanin'],
            "bn": ['r-ফাইকোইরিথ্রিন (r-phycoerythrin)', 'ক্লোরোফিল c', 'ফিউকোজ্যান্থিন', 'ফাইকোসায়ানিন']
        },
        "correct": 0,
        "expl_en": 'The members of Rhodophyceae are commonly called red algae because of the predominance of the red pigment, r-phycoerythrin, in their body.',
        "expl_bn": 'রোডোফাইসির সদস্যরা লাল শৈবাল নামে পরিচিত কারণ এদের দেহে লাল রঙের রঞ্জক r-ফাইকোইরিথ্রিনের আধিক্য থাকে।',
    },
    {
        "id": 'BIO-PK-030',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Where are majority of red algae found, and at what oceanic depths can they survive?',
        "bn": 'অধিকাংশ লাল শৈবাল কোথায় পাওয়া যায় এবং সমুদ্রের কোন গভীরতায় এরা বেঁচে থাকতে পারে?',
        "opts": {
            "en": ['Mostly marine in warmer areas, occurring both at well-lighted surfaces and at great depths where little light penetrates', 'Exclusively in cold freshwater mountain streams only', 'Deep marine abyssal trenches only, never near the ocean surface', 'Stagnant polluted puddles and damp terrestrial rocks only'],
            "bn": ['বেশিরভাগই উষ্ণ সামুদ্রিক জলে, সমুদ্রপৃষ্ঠের সূর্যালোকিত এলাকা থেকে শুরু করে সমুদ্রের গভীর তলদেশ পর্যন্ত যেখানে অতি সামান্য আলো প্রবেশ করে', 'কেবল শীতল পাহাড়ী ঝর্ণার মিষ্ট জলে', 'কেবল সমুদ্রের গভীরতম খাদে, কখনোই পৃষ্ঠতলে নয়', 'কেবল বদ্ধ নোংরা ডোবায় এবং আর্দ্র পাথরে']
        },
        "correct": 0,
        "expl_en": 'Majority of red algae are marine with greater concentrations in warmer areas. They occur both in well-lighted regions close to the water surface and at great depths in oceans where relatively little light penetrates.',
        "expl_bn": 'লাল শৈবাল মূলত উষ্ণ সামুদ্রিক জলে বাস করে। এরা জলের উপরিভাগে যেমন থাকে, তেমনি সমুদ্রের গভীর তলদেশেও বেঁচে থাকে কারণ ফাইকোইরিথ্রিন নীল-সবুজ আলোক তরঙ্গ শোষণ করতে সক্ষম।',
    },
    {
        "id": 'BIO-PK-031',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In Rhodophyceae (red algae), the reserve food material is stored as Floridean starch, which is structurally very similar to:',
        "bn": 'রোডোফাইসিতে খাদ্য ফ্লোরিডিয়ান স্টার্চ (Floridean starch) হিসেবে সঞ্চিত থাকে, যা গঠনের দিক থেকে কার সাথে অত্যন্ত সাদৃশ্যপূর্ণ?',
        "opts": {
            "en": ['Amylopectin and Glycogen', 'Cellulose and Inulin', 'Mannitol and Laminarin', 'Chitin and Peptidoglycan'],
            "bn": ['অ্যামাইলোপেকটিন এবং গ্লাইকোজেন (Amylopectin and Glycogen)', 'সেলুলোজ এবং ইনুলিন', 'ম্যানিটল এবং ল্যামিনারিন', 'কাইটিন এবং পেপটিডোগ্লাইক্যান']
        },
        "correct": 0,
        "expl_en": 'Floridean starch is structurally very similar to amylopectin and glycogen, exhibiting alpha-(1,4) glucan chains with frequent alpha-(1,6) branches.',
        "expl_bn": 'ফ্লোরিডিয়ান স্টার্চ গঠনের দিক থেকে প্রাণীদেহের গ্লাইকোজেন এবং উদ্ভিদের অ্যামাইলোপেকটিনের অত্যন্ত অনুরূপ।',
    },
    {
        "id": 'BIO-PK-032',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'A unique hallmark feature of reproduction in Rhodophyceae (red algae) is that:',
        "bn": 'রোডোফাইসি বা লাল শৈবালের জননের একটি অনন্য প্রধান বৈশিষ্ট্য কী?',
        "opts": {
            "en": ['Both asexual spores (non-motile spores) and gametes (non-motile gametes) completely lack flagella at ALL stages of life cycle', 'They produce multiflagellate ciliated zoospores', 'Male gametes possess two unequal lateral flagella', 'Fertilization occurs externally by swimming flagellated antherozoids'],
            "bn": ['জীবনচক্রের কোনো দশাতেই কোনো প্রকার ফ্ল্যাজেলা থাকে না; অযৌন স্পোর এবং যৌন গ্যামেট উভয়েই সম্পূর্ণ নিশ্চল বা চলনহীন', 'এদের জুস্পোরগুলি বহু-ফ্ল্যাজেলাযুক্ত হয়', 'পুং গ্যামেটের দুটি অসমান পার্শ্বীয় ফ্ল্যাজেলা থাকে', 'সাঁতার কাটা ফ্ল্যাজেলাযুক্ত শুক্রাণু দ্বারা নিষেক ঘটে']
        },
        "correct": 0,
        "expl_en": 'Red algae completely lack any flagellated or motile stages throughout their entire life cycle. Asexual reproduction is by non-motile spores, and sexual reproduction is by non-motile gametes.',
        "expl_bn": 'লাল শৈবালের সমগ্র জীবনচক্রে কোনো অবস্থাতেই কোনো ফ্ল্যাজেলা থাকে না। এদের অযৌন স্পোর ও যৌন গ্যামেট উভয়েই সম্পূর্ণ নিশ্চল (non-motile)।',
    },
    {
        "id": 'BIO-PK-033',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Sexual reproduction in red algae (Rhodophyceae) is strictly:',
        "bn": 'লাল শৈবালে (Rhodophyceae) যৌন জনন সর্বদা কোন প্রকৃতির হয়?',
        "opts": {
            "en": ['Oogamous, accompanied by complex post-fertilization developments', 'Isogamous with flagellated gametes', 'Anisogamous without post-fertilization changes', 'Cleistogamous inside closed chambers'],
            "bn": ['উগ্যামাস (Oogamous) প্রকৃতির এবং নিষেক-পরবর্তী জটিল বিকাশ ও পরিবর্তনযুক্ত', 'ফ্ল্যাজেলাযুক্ত গ্যামেটের আইসোগ্যামাস মিলন', 'নিষেক-পরবর্তী পরিবর্তনহীন অ্যানাইসোগ্যামাস মিলন', 'বদ্ধ চেম্বারের ভেতরে ক্লিস্টোগ্যামাস মিলন']
        },
        "correct": 0,
        "expl_en": 'Sexual reproduction in Rhodophyceae is oogamous and accompanied by complex post-fertilization developments (forming carposporophytes).',
        "expl_bn": 'লাল শৈবালের যৌন জনন উন্নত উগ্যামাস প্রকৃতির এবং এতে নিষেক-পরবর্তী জটিল ভ্রূণীয় ও কার্পোস্পোরোফাইট বিকাশ দেখা যায়।',
    },
    {
        "id": 'BIO-PK-034',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Common examples of Rhodophyceae (red algae) listed in NCERT include:',
        "bn": 'NCERT-তে উল্লেখিত লাল শৈবাল (Rhodophyceae)-এর সাধারণ উদাহরণ কোনগুলি?',
        "opts": {
            "en": ['Polysiphonia, Porphyra, Gracilaria, and Gelidium', 'Ectocarpus, Dictyota, Laminaria, and Sargassum', 'Volvox, Chlamydomonas, Ulothrix, and Chara', 'Sphagnum, Funaria, Marchantia, and Riccia'],
            "bn": ['পলিসাইফোনিয়া (Polysiphonia), পরফাইরা (Porphyra), গ্র্যাসিলেয়ারিয়া (Gracilaria) এবং জেলিডিয়াম (Gelidium)', 'এক্টোকার্পাস, ডিকটিওটা, ল্যামিনারিয়া এবং সারগাসাম', 'ভলভক্স, ক্ল্যামাইডোমোনাস, ইউলোথ্রিক্স এবং কারা', 'স্ফ্যাগনাম, ফিউনারিয়া, মারকানশিয়া এবং রিকসিয়া']
        },
        "correct": 0,
        "expl_en": 'Common members of Rhodophyceae: Polysiphonia, Porphyra, Gracilaria and Gelidium.',
        "expl_bn": 'লাল শৈবালের উদাহরণ: Polysiphonia, Porphyra, Gracilaria এবং Gelidium।',
    },
    {
        "id": 'BIO-PK-035',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'At least a half of the total carbon dioxide fixation on earth is carried out by:',
        "bn": 'পৃথিবীর মোট কার্বন ডাইঅক্সাইড সংবন্ধনের অন্তত অর্ধেক অংশ কার মাধ্যমে সম্পন্ন হয়?',
        "opts": {
            "en": ['Algae through photosynthesis', 'Tropical rainforest gymnosperms', 'Bryophytes growing on peat bogs', 'Desert angiosperms through CAM pathway'],
            "bn": ['সালোকসংশ্লেষের মাধ্যমে শৈবাল দ্বারা', 'ক্রান্তীয় চিরসবুজ ব্যক্তবীজী উদ্ভিদ দ্বারা', 'পিট ভূমির ব্রায়োফাইটা দ্বারা', 'CAM পথের মাধ্যমে মরুভূমির গুপ্তবীজী দ্বারা']
        },
        "correct": 0,
        "expl_en": 'As per NCERT: At least a half of the total carbon dioxide fixation on earth is carried out by algae through photosynthesis, being of paramount importance as primary producers of energy-rich compounds.',
        "expl_bn": 'NCERT অনুসারে: পৃথিবীতে সালোকসংশ্লেষের মাধ্যমে মোট কার্বন ডাইঅক্সাইড সংবন্ধনের প্রায় অর্ধেক অংশই শৈবাল দ্বারা সম্পন্ন হয়।',
    },
    {
        "id": 'BIO-PK-036',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": "Why are Bryophytes commonly called the 'amphibians of the plant kingdom'?",
        "bn": "ব্রায়োফাইটাকে সাধারণভাবে 'উদ্ভিদজগতের উভচর' বলা হয় কেন?",
        "opts": {
            "en": ['They live in soil but are dependent on water for sexual reproduction (transfer of flagellated antherozoids)', 'They can swim in water using fins and crawl on land using tentacles', 'They spend half the day in ocean water and half the day on dry desert rocks', 'They possess vascular xylem vessels like terrestrial angiosperms and gills like aquatic fish'],
            "bn": ['এরা আর্দ্র মাটিতে বাস করে কিন্তু যৌন জননের (চলনক্ষম শুক্রাণুর চলনের) জন্য জলের ওপর সম্পূর্ণ নির্ভরশীল', 'এরা পাখনার সাহায্যে জলে সাঁতার কাটে এবং স্থলভাগে হামাগুড়ি দেয়', 'এরা দিনের অর্ধেক সময় সমুদ্রে এবং বাকি সময় শুষ্ক মরুভূমিতে কাটায়', 'এদের কাণ্ডে জাইলেম সংবহন কলা এবং জলে শ্বাস নেওয়ার ফুলকা থাকে']
        },
        "correct": 0,
        "expl_en": 'Bryophytes are called amphibians of the plant kingdom because these plants can live in soil but are dependent on water for sexual reproduction (the flagellated antherozoids swim through water to reach the archegonium).',
        "expl_bn": 'ব্রায়োফাইট মাটিতে বাস করতে পারলেও যৌন জননে শুক্রাণুর আর্কেগোনিয়ামে পৌঁছানোর জন্য বাহ্যিক জলের প্রয়োজন হয়, তাই এদের উদ্ভিদজগতের উভচর বলা হয়।',
    },
    {
        "id": 'BIO-PK-037',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'The dominant, independent, photosynthetic phase in the life cycle of bryophytes is the:',
        "bn": 'ব্রায়োফাইটার জীবনচক্রের প্রধান, স্বাধীন এবং সালোকসংশ্লেষকারী দশাটি কোনটি?',
        "opts": {
            "en": ['Haploid gametophyte (produces gametes)', 'Diploid sporophyte (produces spores)', 'Triploid endosperm', 'Vascular sporophytic leafy trunk'],
            "bn": ['হ্যাপ্লয়েড গ্যামেটোফাইট বা লিঙ্গধর উদ্ভিদ (গ্যামেট উৎপাদনকারী)', 'ডিপ্লয়েড স্পোরোফাইট বা রেণুধর উদ্ভিদ (স্পোর উৎপাদনকারী)', 'ট্রিপ্লয়েড এন্ডোস্পার্ম', 'সংবহনকলাযুক্ত রেণুধর গুঁড়ি']
        },
        "correct": 0,
        "expl_en": 'The main plant body of the bryophyte is haploid. It produces gametes, hence is called a gametophyte. It is independent and photosynthetic.',
        "expl_bn": 'ব্রায়োফাইটার মূল উদ্ভিদদেহটি হ্যাপ্লয়েড এবং এটি গ্যামেট তৈরি করে বলে একে গ্যামেটোফাইট বলে। এটি সম্পূর্ণ স্বাধীন ও সালোকসংশ্লেষকারী।',
    },
    {
        "id": 'BIO-PK-038',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Which of the following statements accurately describes the sporophyte of bryophytes?',
        "bn": 'নিচের কোন বক্তব্যটি ব্রায়োফাইটার স্পোরোফাইট (রেণুধর উদ্ভিদ) সম্পর্কে সঠিক বিবরণ দেয়?',
        "opts": {
            "en": ['It is not free-living, but physically attached to and nourished by the photosynthetic gametophyte', 'It is completely independent, free-living, and bears branched woody trunks', 'It possesses true roots, seeds, and fruits', 'It is unicellular and undergoes mitosis immediately after plasmogamy'],
            "bn": ['এটি স্বাধীনভাবে বাঁচতে পারে না, বরং সালোকসংশ্লেষকারী গ্যামেটোফাইটের সাথে যুক্ত থেকে তা থেকে পুষ্টি শোষণ করে', 'এটি সম্পূর্ণ স্বাধীন এবং শাখাযুক্ত কাষ্ঠল কাণ্ডবিশিষ্ট', 'এতে প্রকৃত মূল, বীজ ও ফল থাকে', 'এটি এককোষী এবং প্লাজমোগ্যামির সাথে সাথে মাইটোসিস বিভাজনে অংশ নেয়']
        },
        "correct": 0,
        "expl_en": 'The sporophyte is not free-living but attached to the photosynthetic gametophyte and derives nourishment from it.',
        "expl_bn": 'ব্রায়োফাইটার স্পোরোফাইট স্বাধীনজীবী নয়, এটি গ্যামেটোফাইটের ওপর পুষ্টির জন্য পুরোপুরি বা আংশিকভাবে নির্ভরশীল থাকে।',
    },
    {
        "id": 'BIO-PK-039',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'The sex organs in bryophytes are multicellular and jacketed. The male sex organ is called ________ and female sex organ is called ________.',
        "bn": 'ব্রায়োফাইটার জননাঙ্গ বহুকোষী ও বন্ধ্যা আবরণীযুক্ত। পুং জননাঙ্গকে ________ এবং স্ত্রী জননাঙ্গকে ________ বলে।',
        "opts": {
            "en": ['Antheridium (produces biflagellate antherozoids), Archegonium (flask-shaped, produces single egg)', 'Archegonium, Antheridium', 'Oogonium, Antheridium', 'Carpogonium, Spermatangium'],
            "bn": ['অ্যান্থেরিডিয়াম (দ্বি-ফ্ল্যাজেলাযুক্ত শুক্রাণু তৈরি করে), আর্কেগোনিয়াম (ফ্লাস্ক-আকৃতির, একটি ডিম্বাণু তৈরি করে)', 'আর্কেগোনিয়াম, অ্যান্থেরিডিয়াম', 'উগোনিয়াম, অ্যান্থেরিডিয়াম', 'কার্পোগোনিয়াম, স্পারমাটানজিয়াম']
        },
        "correct": 0,
        "expl_en": 'The male sex organ is called antheridium producing biflagellate antherozoids. The female sex organ called archegonium is flask-shaped and produces a single egg.',
        "expl_bn": 'পুং জননাঙ্গকে অ্যান্থেরিডিয়াম বলে যা দ্বি-ফ্ল্যাজেলাযুক্ত সচল শুক্রাণু তৈরি করে। স্ত্রী জননাঙ্গকে ফ্লাস্কের মতো দেখতে আর্কেগোনিয়াম বলে যাতে একটিমাত্র ডিম্বাণু থাকে।',
    },
    {
        "id": 'BIO-PK-040',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Peat, which has long been used as fuel and as packing material for trans-shipment of living material because of its water holding capacity, is provided by:',
        "bn": 'জলধারণ ক্ষমতার কারণে জীবিত উদ্ভিদ বা প্রাণীর এক স্থান থেকে অন্য স্থানে পরিবহনে এবং জ্বালানি হিসেবে ব্যবহৃত পিট (Peat) কোন ব্রায়োফাইট থেকে পাওয়া যায়?',
        "opts": {
            "en": ['Sphagnum (Peat moss)', 'Marchantia polymorpha', 'Riccia fluitans', 'Funaria hygrometrica'],
            "bn": ['স্ফ্যাগনাম বা পিট মস (Sphagnum)', 'মারকানশিয়া', 'রিকসিয়া', 'ফিউনারিয়া']
        },
        "correct": 0,
        "expl_en": 'Sphagnum, a moss, provides peat that has long been used as fuel, and as packing material for trans-shipment of living material because of its tremendous water-holding capacity.',
        "expl_bn": 'স্ফ্যাগনাম (Sphagnum) মস থেকে পিট পাওয়া যায় যা জ্বালানি হিসেবে এবং তার চমৎকার জলধারণ ক্ষমতার কারণে জীবিত সামগ্রী পরিবহনে প্যাকিং বস্তু হিসেবে ব্যবহৃত হয়।',
    },
    {
        "id": 'BIO-PK-041',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Mosses along with lichens are of great ecological significance because:',
        "bn": 'লাইকেনের পাশাপাশি মস অত্যন্ত গুরুত্বপূর্ণ বাস্তুতান্ত্রিক তাৎপর্য বহন করে কারণ:',
        "opts": {
            "en": ['They are the first organisms to colonise bare rocks and decompose them to make substrate suitable for higher plants', 'They fix nitrogen directly through their stem nodules', 'They produce timber and resin for industrial use', 'They prevent evaporation of seawater into clouds'],
            "bn": ['এরা প্রথম জীব যারা উন্মুক্ত পাথরে বসতি স্থাপন করে এবং পাথরকে ক্ষয় করে উন্নত উদ্ভিদের বৃদ্ধির উপযোগী মাটি তৈরি করে', 'এরা কাণ্ডের নডিউলের সাহায্যে সরাসরি নাইট্রোজেন সংবন্ধন করে', 'এরা কাঠ ও রজন সরবরাহ করে', 'এরা সমুদ্রের জলের বাষ্পীভবন রোধ করে']
        },
        "correct": 0,
        "expl_en": 'Mosses along with lichens are the pioneer organisms to colonise rocks and hence are of great ecological importance. They decompose rocks making the substrate fit for the growth of higher plants.',
        "expl_bn": 'লাইকেন ও মস পাথরের ওপর সর্বপ্রথম পর্যায়ক্রম শুরু করে এবং পাথর ক্ষয় করে মাটি তৈরি করে উন্নত উদ্ভিদের জন্ম নিশ্চিত করে। এছাড়া মাটির ওপর ঘন গালিচা তৈরি করে ভূমিক্ষয় রোধ করে।',
    },
    {
        "id": 'BIO-PK-042',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'In liverworts such as Marchantia, asexual reproduction occurs by specialized green, multicellular, asexual buds developed in small receptacles called:',
        "bn": 'মারকানশিয়ার মতো লিভারওয়ার্টে বিশেষ ধরনের সবুজ, বহুকোষী অযৌন মুকুলের মাধ্যমে জনন সম্পন্ন হয়, যা কোন পেয়ালাকার পাত্রে গঠিত হয়?',
        "opts": {
            "en": ['Gemmae produced in gemma cups', 'Akinetes produced in akinete sockets', 'Conidia produced on conidiophores', 'Zoospores produced in zoosporangia'],
            "bn": ['গেমা কাপে (Gemma cups) উৎপন্ন গেমা (Gemmae)', 'অ্যাকাইনেট সকেটে উৎপন্ন অ্যাকাইনেট', 'কনিডিওফোরের ওপর কনিডিয়া', 'জুস্পোরাঞ্জিয়ামে জুস্পোর']
        },
        "correct": 0,
        "expl_en": 'Asexual reproduction in liverworts takes place by fragmentation or by formation of specialised structures called gemmae. Gemmae are green, multicellular, asexual buds that develop in gemma cups located on the thallus.',
        "expl_bn": 'মারকানশিয়ার থ্যালাসের ওপর অবস্থিত গেমা কাপের মধ্যে সবুজ, বহুকোষী অযৌন মুকুল বা গেমা (Gemmae) তৈরি হয়।',
    },
    {
        "id": 'BIO-PK-043',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In Marchantia, the male and female sex organs are born on distinct thalli called respectively:',
        "bn": 'মারকানশিয়াতে পুং ও স্ত্রী জননাঙ্গ পৃথক পৃথক থ্যালাসের ওপর গঠিত হয়, যাদের যথাক্রমে কী বলা হয়?',
        "opts": {
            "en": ['Antheridiophore (on male thallus) and Archegoniophore (on female thallus)', 'Archegoniophore (on male) and Antheridiophore (on female)', 'Sporophore and Gametophore', 'Stamen and Carpel'],
            "bn": ['অ্যান্থেরিডিওফোর (পুং থ্যালাসে) এবং আর্কেগোনিওফোর (স্ত্রী থ্যালাসে)', 'আর্কেগোনিওফোর (পুং) এবং অ্যান্থেরিডিওফোর (স্ত্রী)', 'স্পোরোফোর এবং গ্যামেটোফোর', 'পুংকেশর এবং গর্ভকেশর']
        },
        "correct": 0,
        "expl_en": 'Marchantia is dioecious. The male receptacles are borne on stalks called antheridiophores, and female receptacles with ray-like projections are borne on archegoniophores.',
        "expl_bn": 'মারকানশিয়া একটি ভিন্নবাসী (dioecious) উদ্ভিদ। পুং জননাঙ্গ ধারণকারী শাখাকে অ্যান্থেরিডিওফোর এবং স্ত্রী জননাঙ্গ ধারণকারী শাখাকে আর্কেগোনিওফোর বলে।',
    },
    {
        "id": 'BIO-PK-044',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The sporophyte of liverworts and mosses is differentiated into:',
        "bn": 'লিভারওয়ার্ট এবং মসের রেণুধর দেহটি (Sporophyte) কোন তিনটি অংশে বিভক্ত?',
        "opts": {
            "en": ['Foot, seta, and capsule', 'Root, stem, and leaf', 'Holdfast, stipe, and frond', 'Rhizome, petiole, and blade'],
            "bn": ['ফুট (Foot), সিটা (Seta) এবং ক্যাপসুল (Capsule)', 'মূল, কাণ্ড এবং পাতা', 'হোল্ডফাস্ট, স্ট্রাইপ এবং ফ্রন্ড', 'রাইজোম, পত্রবৃন্ত এবং ফলক']
        },
        "correct": 0,
        "expl_en": 'The sporophyte of bryophytes is differentiated into foot (anchorage/absorption), seta (stalk), and capsule (site of meiosis and spore formation).',
        "expl_bn": 'ব্রায়োফাইটার স্পোরোফাইট ফুট, সিটা এবং ক্যাপসুল নামক তিনটি অংশে বিভক্ত থাকে। ক্যাপসুলের ভেতর মায়োসিসের মাধ্যমে হ্যাপ্লয়েড রেণু উৎপন্ন হয়।',
    },
    {
        "id": 'BIO-PK-045',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The predominant stage of the life cycle of a moss is the gametophyte which consists of two stages:',
        "bn": 'একটি মসের জীবনচক্রের প্রধান দশা হলো গ্যামেটোফাইট, যা কোন দুটি ক্রমান্বয়িক দশার সমন্বয়ে গঠিত?',
        "opts": {
            "en": ['Protonema stage (creeping, green, branched, developing directly from spore) and Leafy stage (upright, slender axes with spirally arranged leaves)', 'Rhizoid stage and Flower stage', 'Sporophore stage and Zygote stage', 'Primary thallus and Secondary wood'],
            "bn": ['প্রোটোনেমা দশা (রেণু থেকে সরাসরি উৎপন্ন শায়িত, সবুজ, শাখাযুক্ত) এবং পত্রল দশা (খাড়া অক্ষ ও সর্পিলাকারে সজ্জিত পাতাযুক্ত)', 'রাইজয়েড দশা এবং পুষ্প দশা', 'স্পোরোফোর দশা এবং জাইগোট দশা', 'প্রাথমিক থ্যালাস এবং গৌণ কাষ্ঠ']
        },
        "correct": 0,
        "expl_en": 'The first stage of moss gametophyte is the protonema stage, which develops directly from a spore. The second stage is the leafy stage, which develops from a secondary protonema as a lateral bud.',
        "expl_bn": 'মসের গ্যামেটোফাইটের প্রথম দশাটি হলো প্রোটোনেমা (রেণু অঙ্কুরিত হয়ে তৈরি সূত্রাকার দশা) এবং দ্বিতীয় দশাটি হলো পত্রল দশা যা গৌণ প্রোটোনেমা থেকে পার্শ্বীয় মুকুলরূপে বিকশিত হয়।',
    },
    {
        "id": 'BIO-PK-046',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In mosses, vegetative reproduction takes place by fragmentation and budding in the:',
        "bn": 'মসের ক্ষেত্রে অঙ্গজ জনন খণ্ডীভবন এবং মুকুলোদগমের মাধ্যমে কোন দশায় সংঘটিত হয়?',
        "opts": {
            "en": ['Secondary protonema', 'Capsule wall', 'Diploid zygote', 'Columella cells'],
            "bn": ['গৌণ প্রোটোনেমা (Secondary protonema)', 'ক্যাপসুলের প্রাচীর', 'ডিপ্লয়েড জাইগোট', 'কলুমেলা কোষ']
        },
        "correct": 0,
        "expl_en": 'Vegetative reproduction in mosses is by fragmentation and budding in the secondary protonema.',
        "expl_bn": 'মসের অঙ্গজ জনন ঘটে গৌণ প্রোটোনেমার (secondary protonema) খণ্ডীভবন ও মুকুলোদগমের মাধ্যমে।',
    },
    {
        "id": 'BIO-PK-047',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following is a representative moss?',
        "bn": 'নিচের কোনটি মসের (Bryopsida) অন্তর্ভুক্ত সঠিক উদাহরণগুচ্ছ?',
        "opts": {
            "en": ['Funaria, Polytrichum, and Sphagnum', 'Marchantia, Riccia, and Pellia', 'Psilotum, Lycopodium, and Selaginella', 'Cycas, Pinus, and Ginkgo'],
            "bn": ['ফিউনারিয়া (Funaria), পলিট্রিকাম (Polytrichum) এবং স্ফ্যাগনাম (Sphagnum)', 'মারকানশিয়া, রিকসিয়া এবং পেলিয়া', 'সাইলোটাম, লাইকোপোডিয়াম এবং সিলাজিনেলা', 'সাইকাস, পাইনাস এবং জিংগো']
        },
        "correct": 0,
        "expl_en": 'Common examples of mosses given in NCERT are Funaria, Polytrichum, and Sphagnum.',
        "expl_bn": 'NCERT অনুসারে মসের সাধারণ উদাহরণ হলো ফিউনারিয়া, পলিট্রিকাম এবং স্ফ্যাগনাম।',
    },
    {
        "id": 'BIO-PK-048',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The mechanism of spore dispersal is more elaborate and sophisticated in:',
        "bn": 'রেণু বিচ্ছুরণের কৌশলটি তুলনামূলকভাবে অনেক বেশি জটিল ও উন্নত কোনটিতে?',
        "opts": {
            "en": ['Mosses (due to peristome teeth)', 'Liverworts', 'Green algae', 'Slime moulds'],
            "bn": ['মসে (পেরিস্টোম দাঁতের উপস্থিতির কারণে)', 'লিভারওয়ার্টে', 'সবুজ শৈবালে', 'স্লাইম মোল্ডে']
        },
        "correct": 0,
        "expl_en": 'As per NCERT: The sporophyte in mosses is more elaborate than that in liverworts. The moss capsule has an elaborate mechanism of spore dispersal (involving hygroscopic peristome teeth).',
        "expl_bn": 'NCERT অনুসারে: লিভারওয়ার্টের তুলনায় মসের স্পোরোফাইট এবং ক্যাপসুল থেকে রেণু বিস্তারের কৌশল (হাইগ্রোস্কোপিক পেরিস্টোম দাঁতের মাধ্যমে) অনেক বেশি উন্নত ও জটিল।',
    },
    {
        "id": 'BIO-PK-049',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Which group of plants were the first terrestrial plants to possess vascular tissues (xylem and phloem)?',
        "bn": 'কোন উদ্ভিদ গোষ্ঠী স্থলভাগে সর্বপ্রথম সংবহন কলা (জাইলেম ও ফ্লোয়েম)-র অধিকারী হয়েছিল?',
        "opts": {
            "en": ['Pteridophytes', 'Bryophytes', 'Gymnosperms', 'Angiosperms'],
            "bn": ['টেরিডোফাইটা বা ফার্নবর্গ (Pteridophytes)', 'ব্রায়োফাইটা', 'ব্যক্তবীজী', 'গুপ্তবীজী']
        },
        "correct": 0,
        "expl_en": 'Evolutionarily, pteridophytes are the first terrestrial plants to possess vascular tissues — xylem and phloem.',
        "expl_bn": 'বিবর্তনীয় দৃষ্টিকোণ থেকে টেরিডোফাইট হলো পৃথিবীর সর্বপ্রথম সংবহনকলাযুক্ত (জাইলেম ও ফ্লোয়েম বিশিষ্ট) স্থলজ উদ্ভিদ।',
    },
    {
        "id": 'BIO-PK-050',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In pteridophytes, the dominant phase in the life cycle is the:',
        "bn": 'টেরিডোফাইটার জীবনচক্রের প্রধান বা আধিপত্যকারী দশাটি কোনটি?',
        "opts": {
            "en": ['Sporophyte (diploid, differentiated into true root, stem, and leaves)', 'Gametophyte (haploid thallus)', 'Free-floating protonema', 'Endospermic haustorium'],
            "bn": ['স্পোরোফাইট (ডিপ্লয়েড, যা প্রকৃত মূল, কাণ্ড এবং পাতায় বিভেদিত)', 'গ্যামেটোফাইট (হ্যাপ্লয়েড সমাঙ্গদেহ)', 'মুক্ত ভাসমান প্রোটোনেমা', 'এন্ডোস্পার্মিক চোষক']
        },
        "correct": 0,
        "expl_en": 'In bryophytes the dominant phase is the gametophyte, whereas in pteridophytes the main plant body is a sporophyte which is differentiated into true root, stem, and leaves.',
        "expl_bn": 'ব্রায়োফাইটার প্রধান দশা যেখানে গ্যামেটোফাইট, টেরিডোফাইটার ক্ষেত্রে প্রধান উদ্ভিদদেহটি হলো রেণুধর বা স্পোরোফাইট (2n), যা প্রকৃত মূল, কাণ্ড ও পাতায় বিভক্ত।',
    },
    {
        "id": 'BIO-PK-051',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Leaves in pteridophytes can be small (microphylls) as in ________ or large (macrophylls/fronds) as in ________.',
        "bn": 'টেরিডোফাইটার পাতা ক্ষুদ্রাকার (মাইক্রোফিল) হতে পারে যেমন ________-এ অথবা বৃহৎ (ম্যাক্রোফিল) হতে পারে যেমন ________-এ।',
        "opts": {
            "en": ['Selaginella; Ferns', 'Ferns; Selaginella', 'Marchantia; Funaria', 'Pinus; Cycas'],
            "bn": ['সিলাজিনেলা; ফার্ন', 'ফার্ন; সিলাজিনেলা', 'মারকানশিয়া; ফিউনারিয়া', 'পাইনাস; সাইকাস']
        },
        "correct": 0,
        "expl_en": 'The leaves in pteridophyta are small (microphylls) as in Selaginella or large (macrophylls) as in ferns.',
        "expl_bn": 'সিলাজিনেলায় ক্ষুদ্র মাইক্রোফিল পাতা থাকে এবং ফার্নে বৃহৎ ম্যাক্রোফিল বা ফ্রন্ড থাকে।',
    },
    {
        "id": 'BIO-PK-052',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In some pteridophytes, sporophylls may form distinct compact structures called strobili or cones. This is observed in:',
        "bn": 'কিছু টেরিডোফাইটে রেণুপত্রগুলি পুঞ্জীভূত হয়ে সুনির্দিষ্ট শঙ্কু বা স্ট্রোবিলাস (strobili/cones) গঠন করে। এটি কোনটিতে দেখা যায়?',
        "opts": {
            "en": ['Selaginella and Equisetum', 'Dryopteris and Pteris', 'Adiantum and Salvinia', 'Marchantia and Riccia'],
            "bn": ['সিলাজিনেলা (Selaginella) এবং ইকুইসিটাম (Equisetum)', 'ড্রায়োপ্টেরিস এবং টেরিস', 'অ্যাডিয়েন্টাম এবং সালভিনিয়া', 'মারকানশিয়া এবং রিকসিয়া']
        },
        "correct": 0,
        "expl_en": 'In some cases sporophylls may form distinct compact structures called strobili or cones (e.g., Selaginella, Equisetum).',
        "expl_bn": 'সিলাজিনেলা এবং ইকুইসিটামে রেণুপত্রগুলি ঘনভাবে সন্নিবেশিত হয়ে স্ট্রোবিলাস বা শঙ্কু (cone) গঠন করে।',
    },
    {
        "id": 'BIO-PK-053',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The spores in pteridophytes germinate to give rise to inconspicuous, small but multicellular, free-living, mostly photosynthetic thalloid gametophytes called:',
        "bn": 'টেরিডোফাইটার রেণু অঙ্কুরিত হয়ে যে ক্ষুদ্র, বহুকোষী, স্বাধীনজীবী এবং প্রধানত সালোকসংশ্লেষকারী সমাঙ্গদেহী লিঙ্গধর দেহ গঠন করে তাকে কী বলে?',
        "opts": {
            "en": ['Prothallus', 'Protonema', 'Archegoniophore', 'Endosperm'],
            "bn": ['প্রোথ্যালাস (Prothallus)', 'প্রোটোনেমা', 'আর্কেগোনিওফোর', 'এন্ডোস্পার্ম']
        },
        "correct": 0,
        "expl_en": 'The spores germinate to give rise to inconspicuous, small but multicellular, free-living, mostly photosynthetic thalloid gametophytes called prothallus.',
        "expl_bn": 'টেরিডোফাইটার হ্যাপ্লয়েড রেণু অঙ্কুরিত হয়ে যে স্বাধীন ও সবুজ সমাঙ্গদেহী লিঙ্গধর উদ্ভিদদেহ গঠন করে তাকে প্রোথ্যালাস (Prothallus) বলে।',
    },
    {
        "id": 'BIO-PK-054',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Why is the geographical spread and distribution of living pteridophytes restricted and narrow?',
        "bn": 'বর্তমান পৃথিবীতে জীবিত টেরিডোফাইটের ভৌগোলিক বিস্তৃতি কেন বেশ সীমিত এবং নির্দিষ্ট আর্দ্র অঞ্চলের মধ্যেই সীমাবদ্ধ?',
        "opts": {
            "en": ['Because their gametophytes require cool, damp, shady places to grow and flagellated antherozoids require water for fertilization', 'Because they are obligate halophytes unable to tolerate fresh water', 'Because their roots cannot absorb mineral ions without mycorrhiza', 'Because their seeds lack an impermeable protective coat'],
            "bn": ['কারণ এদের প্রোথ্যালাসের বৃদ্ধির জন্য শীতল, স্যাঁতসেঁতে ছায়াযুক্ত পরিবেশের প্রয়োজন এবং শুক্রাণুর মিলনের জন্য জলের উপস্থিতি অপরিহার্য', 'কারণ এরা নোনা জল ছাড়া মিষ্টি জলে বাঁচে না', 'কারণ এদের মূল মাইকোরাইজা ছাড়া খনিজ শোষণ করতে পারে না', 'কারণ এদের বীজে কোনো প্রতিরক্ষামূলক আবরণ নেই']
        },
        "correct": 0,
        "expl_en": 'Because of the specific restricted requirement of gametophytes (cool, damp, shady habitats) and the unconditional requirement of water for fertilization, the spread of living pteridophytes is limited and restricted to narrow geographical zones.',
        "expl_bn": 'প্রোথ্যালাসের বৃদ্ধির জন্য আর্দ্র ও ছায়াময় স্থানের প্রয়োজনীয়তা এবং নিষেকের জন্য জলের অপরিহার্যতার কারণেই টেরিডোফাইটার বিস্তৃতি সীমিত ভৌগোলিক অঞ্চলে আবদ্ধ থাকে।',
    },
    {
        "id": 'BIO-PK-055',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Majority of pteridophytes produce spores of a similar kind and are called homosporous. Genera which produce two kinds of spores, macro (large) and micro (small) spores, are called heterosporous. Which pair represents heterosporous pteridophytes?',
        "bn": 'অধিকাংশ টেরিডোফাইট একই ধরনের রেণু উৎপন্ন করে (হোমোস্পোরাস)। কিন্তু যেসকল প্রজাতি ম্যাক্রোস্পোর (বড়) ও মাইক্রোস্পোর (ছোট) নামক দুই ধরনের ভিন্ন রেণু উৎপন্ন করে তাদের হেটারোস্পোরাস বলে। নিচের কোন জোড়াটি হেটারোস্পোরাস টেরিডোফাইটের উদাহরণ?',
        "opts": {
            "en": ['Selaginella and Salvinia', 'Dryopteris and Pteris', 'Equisetum and Psilotum', 'Lycopodium and Adiantum'],
            "bn": ['সিলাজিনেলা (Selaginella) এবং সালভিনিয়া (Salvinia)', 'ড্রায়োপ্টেরিস এবং টেরিস', 'ইকুইসিটাম এবং সাইলোটাম', 'লাইকোপোডিয়াম এবং অ্যাডিয়েন্টাম']
        },
        "correct": 0,
        "expl_en": 'Genera like Selaginella and Salvinia produce two kinds of spores, macro (megaspores) and microspores, and are termed heterosporous.',
        "expl_bn": 'সিলাজিনেলা (Selaginella) এবং সালভিনিয়া (Salvinia) দুই ভিন্ন ধরনের রেণু উৎপন্ন করে, তাই এরা হেটারোস্পোরাস (heterosporous)।',
    },
    {
        "id": 'BIO-PK-056',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'In heterosporous pteridophytes, the megaspores and microspores germinate and give rise to:',
        "bn": 'হেটারোস্পোরাস টেরিডোফাইটে মেগাস্পোর ও মাইক্রোস্পোর অঙ্কুরিত হয়ে যথাক্রমে কী গঠন করে?',
        "opts": {
            "en": ['Female and male gametophytes respectively', 'Male and female gametophytes respectively', 'Diploid sporophytes directly without gametes', 'Peat moss cushions'],
            "bn": ['যথাক্রমে স্ত্রী গ্যামেটোফাইট এবং পুং গ্যামেটোফাইট', 'যথাক্রমে পুং গ্যামেটোফাইট এবং স্ত্রী গ্যামেটোফাইট', 'কোনো গ্যামেট ছাড়াই সরাসরি ডিপ্লয়েড স্পোরোফাইট', 'পিট মসের গালিচা']
        },
        "correct": 0,
        "expl_en": 'The megaspores and microspores germinate to give rise to female and male gametophytes, respectively. The female gametophytes in these plants are retained on the parent sporophytes for variable periods.',
        "expl_bn": 'মেগাস্পোর বা গুরুরেণু অঙ্কুরিত হয়ে স্ত্রী গ্যামেটোফাইট এবং মাইক্রোস্পোর বা ক্ষুদ্ররেণু অঙ্কুরিত হয়ে পুং গ্যামেটোফাইট উৎপন্ন করে।',
    },
    {
        "id": 'BIO-PK-057',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": "Which event in heterosporous pteridophytes (like Selaginella) is considered an important precursor to the evolution of the 'seed habit'?",
        "bn": "সিলাজিনেলা জাতীয় হেটারোস্পোরাস টেরিডোফাইটের কোন ঘটনাটিকে উদ্ভিদের 'বীজ স্বভাব' (Seed habit)-এর বিবর্তনের ক্ষেত্রে অত্যন্ত তাৎপর্যপূর্ণ অগ্রদূত হিসেবে গণ্য করা হয়?",
        "opts": {
            "en": ['Retention of the female gametophyte on the parent sporophyte and development of the zygote into young embryo within the female gametophyte', 'Loss of vascular bundles in the stem', 'Dispersal of free haploid flagellated spores in seawater', 'Absence of meiosis in the sporogenous tissue'],
            "bn": ['মাতৃ স্পোরোফাইটের গায়ে স্ত্রী গ্যামেটোফাইটের সংলগ্ন থাকা এবং স্ত্রী গ্যামেটোফাইটের ভেতরেই জাইগোট থেকে ভ্রূণের বিকাশ সাধন', 'কাণ্ডের সংবহন বান্ডিলের সম্পূর্ণ অবলুপ্তি', 'সমুদ্রের জলে হ্যাপ্লয়েড ফ্ল্যাজেলাযুক্ত স্পোর ত্যাগ করা', 'রেণুজনন কলায় মায়োসিসের অনুপস্থিতি']
        },
        "correct": 0,
        "expl_en": 'The female gametophyte is retained on the parent sporophyte for variable periods. The development of the zygote into a young embryo takes place within the female gametophyte. This event is a crucial precursor to the seed habit, considered an important evolutionary milestone.',
        "expl_bn": "স্ত্রী গ্যামেটোফাইটটি মাতৃ স্পোরোফাইটের ওপর যুক্ত থাকে এবং স্ত্রী গ্যামেটোফাইটের ভেতরেই জাইগোট থেকে ভ্রূণের বিকাশ ঘটে। এটিই বীজ স্বভাব বা 'Seed habit'-এর উৎপত্তি ও বিবর্তনের আদি ধাপ।",
    },
    {
        "id": 'BIO-PK-058',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": "Which class of Pteridophytes includes 'Horsetails'?",
        "bn": "টেরিডোফাইটার কোন শ্রেণিতে 'হর্সটেল' (Horsetail) অন্তর্ভুক্ত?",
        "opts": {
            "en": ['Sphenopsida (e.g., Equisetum)', 'Psilopsida (e.g., Psilotum)', 'Lycopsida (e.g., Lycopodium)', 'Pteropsida (e.g., Dryopteris)'],
            "bn": ['স্ফেনোপসিডা (যেমন ইকুইসিটাম)', 'সাইলোপসিডা (যেমন সাইলোটাম)', 'লাইকোপসিডা (যেমন লাইকোপোডিয়াম)', 'টেরোপসিডা (যেমন ড্রায়োপ্টেরিস)']
        },
        "correct": 0,
        "expl_en": 'Pteridophytes are classified into four classes: Psilopsida (Psilotum); Lycopsida (Selaginella, Lycopodium); Sphenopsida (Equisetum - horsetails); Pteropsida (Dryopteris, Pteris, Adiantum).',
        "expl_bn": 'টেরিডোফাইটাকে চারটি শ্রেণিতে ভাগ করা হয়। এর মধ্যে স্ফেনোপসিডা (Sphenopsida)-র অন্তর্ভুক্ত হলো ইকুইসিটাম যা হর্সটেল নামে পরিচিত।',
    },
    {
        "id": 'BIO-PK-059',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following belongs to class Lycopsida?',
        "bn": 'নিচের কোন জোড়াটি লাইকোপসিডা (Lycopsida) শ্রেণির অন্তর্গত?',
        "opts": {
            "en": ['Selaginella and Lycopodium', 'Psilotum and Rhynia', 'Equisetum and Sphenophyllum', 'Pteris and Adiantum'],
            "bn": ['সিলাজিনেলা এবং লাইকোপোডিয়াম', 'সাইলোটাম এবং রাইনিয়া', 'ইকুইসিটাম এবং স্ফেনোফাইলাম', 'টেরিস এবং অ্যাডিয়েন্টাম']
        },
        "correct": 0,
        "expl_en": 'Class Lycopsida includes club mosses like Selaginella and Lycopodium.',
        "expl_bn": 'লাইকোপসিডার অন্তর্ভুক্ত হলো সিলাজিনেলা এবং লাইকোপোডিয়াম।',
    },
    {
        "id": 'BIO-PK-060',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": "Adiantum is popularly referred to as the 'walking fern' because:",
        "bn": "অ্যাডিয়েন্টাম (Adiantum)-কে সাধারণভাবে 'ওয়াকিং ফার্ন' (Walking fern) বলা হয় কেন?",
        "opts": {
            "en": ['Its leaf tips bend and touch the soil to produce adventitious buds that establish new plants, making it appear to walk', 'It has legs that allow it to walk during rainstorms', 'Its rhizoids move rapidly by amoeboid contractions', 'Its spores possess walking wings'],
            "bn": ['এর পাতার অগ্রভাগ মাটিতে স্পর্শ করলে সেখান থেকে অস্থানিক মুকুল ও নতুন চারাগাছ জন্মায়, ফলে মনে হয় গাছটি হেঁটে চলেছে', 'বৃষ্টির দিনে চলার মতো পা থাকে', 'রাইজয়েড ক্ষণপদের মতো চলাচল করে', 'স্পোরের ডানা থাকে যা দিয়ে হেঁটে বেড়ায়']
        },
        "correct": 0,
        "expl_en": 'Adiantum caudatum is called the walking fern because when its vegetative frond tips touch moist soil, they produce adventitious roots and plantlets, propagating across the ground.',
        "expl_bn": 'অ্যাডিয়েন্টামের পাতার অগ্রভাগ ভিজে মাটি ছুঁলে সেখানে অস্থানিক মুকুল সৃষ্টি হয়ে নতুন উদ্ভিদ জন্মায়, তাই একে ওয়াকিং ফার্ন বলা হয়।',
    },
    {
        "id": 'BIO-PK-061',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Gymnosperms (gymnos: naked, sperma: seeds) are characterized by having:',
        "bn": 'ব্যক্তবীজী বা জিম্নোস্পার্ম (Gymnosperms)-এর প্রধান শনাক্তকারী বৈশিষ্ট্য কী?',
        "opts": {
            "en": ['Ovules that are not enclosed by any ovary wall and remain exposed both before and after fertilization', 'Seeds enclosed completely inside fleshy pericarp of fruits', 'Flowers with vibrant petals and sepals', 'Double fertilization leading to triploid endosperm'],
            "bn": ['ডিম্বকগুলি কোনো ডিম্বাশয় প্রাচীর দ্বারা আবৃত থাকে না এবং নিষেকের পূর্বে ও পরে উভয় সময়েই অনাবৃত অবস্থায় থাকে', 'বীজগুলি ফলের মাংসল ফলের ত্বকের ভেতরে সম্পূর্ণ ঢাকা থাকে', 'উজ্জ্বল পাপড়ি ও বৃত্যংশ বিশিষ্ট ফুল', 'দ্বি-নিষেক এবং ট্রিপ্লয়েড শস্য গঠন']
        },
        "correct": 0,
        "expl_en": 'Gymnosperms are plants in which the ovules are not enclosed by an ovary wall and remain exposed, both before and after fertilisation. The seeds that develop post-fertilisation are not covered, i.e., are naked.',
        "expl_bn": 'ব্যক্তবীজী উদ্ভিদে কোনো ডিম্বাশয় থাকে না, তাই ডিম্বকগুলি অনাবৃত অবস্থায় থাকে এবং নিষেকের পর গঠিত বীজগুলি নগ্ন অবস্থায় থাকে (কোনো ফল গঠিত হয় না)।',
    },
    {
        "id": 'BIO-PK-062',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'One of the tallest tree species in the world, the giant redwood tree Sequoia, belongs to:',
        "bn": 'বিশ্বের অন্যতম দীর্ঘতম কাষ্ঠল বৃক্ষদানব রেডউড (Sequoia) কোন উদ্ভিদ দলের অন্তর্ভুক্ত?',
        "opts": {
            "en": ['Gymnosperms', 'Pteridophytes', 'Angiosperms', 'Bryophytes'],
            "bn": ['ব্যক্তবীজী (Gymnosperms)', 'টেরিডোফাইটা', 'গুপ্তবীজী', 'ব্রায়োফাইটা']
        },
        "correct": 0,
        "expl_en": 'The giant redwood tree Sequoia is one of the tallest tree species and is a gymnosperm (conifer).',
        "expl_bn": 'বিশালকায় রেডউড গাছ সেকোয়া (Sequoia sempervirens) হলো একটি ব্যক্তবীজী (Gymnosperm) বৃক্ষ।',
    },
    {
        "id": 'BIO-PK-063',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In Pinus, the roots have a symbiotic association with fungi called ________, whereas in Cycas, specialized roots called ________ are associated with N2-fixing cyanobacteria.',
        "bn": 'পাইনাসে (Pinus) মূলের সাথে ছত্রাকের মিথোজীবী সম্পর্ককে ________ বলে, আর সাইকাসে (Cycas) নাইট্রোজেন সংবন্ধনকারী সায়ানোব্যাকটেরিয়া যুক্ত বিশেষ মূলকে ________ বলে।',
        "opts": {
            "en": ['Mycorrhiza; Coralloid roots', 'Coralloid roots; Mycorrhiza', 'Nodules; Haustoria', 'Pneumatophores; Epiphytic roots'],
            "bn": ['মাইকোরাইজা (Mycorrhiza); কোরালয়েড মূল (Coralloid roots)', 'কোরালয়েড মূল; মাইকোরাইজা', 'অর্বুদ; চোষক মূল', 'নিউম্যাটোফোর; পরাশ্রয়ী মূল']
        },
        "correct": 0,
        "expl_en": 'Roots in Pinus have fungal association in the form of mycorrhizae, while in Cycas small specialised roots called coralloid roots are associated with N2-fixing cyanobacteria (Anabaena/Nostoc).',
        "expl_bn": 'পাইনাসের মূলে ছত্রাকের মিথোজীবী সহাবস্থানকে মাইকোরাইজা বলে এবং সাইকাসের বিশেষ শাখান্বিত কোরালয়েড মূলে নাইট্রোজেন সংবন্ধনকারী অ্যানাবিনা বা নস্টক বাস করে।',
    },
    {
        "id": 'BIO-PK-064',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Regarding stem branching in gymnosperms, which statement is correct?',
        "bn": 'ব্যক্তবীজী উদ্ভিদের কাণ্ডের শাখা সংক্রান্ত কোন তথ্যটি সঠিক?',
        "opts": {
            "en": ['The stem is unbranched in Cycas and branched in Pinus and Cedrus', 'The stem is branched in Cycas and unbranched in Pinus', 'Stems are unbranched in all gymnosperms without exception', 'Stems are underground creeping runners in all conifers'],
            "bn": ['সাইকাসে (Cycas) কাণ্ড অশাখ (unbranched) কিন্তু পাইনাস (Pinus) ও সিড্রাসে (Cedrus) কাণ্ড শাখাপ্রশাখা বিশিষ্ট (branched)', 'সাইকাসে কাণ্ড শাখাযুক্ত এবং পাইনাসে অশাখ', 'ব্যতিক্রমহীনভাবে সমস্ত ব্যক্তবীজীর কাণ্ড অশাখ', 'সমস্ত কনিফারে কাণ্ড মাটির নিচে ধাবক হিসেবে থাকে']
        },
        "correct": 0,
        "expl_en": 'As per NCERT: The stems are unbranched (Cycas) or branched (Pinus, Cedrus).',
        "expl_bn": 'NCERT অনুসারে: সাইকাসের কাণ্ড অশাখ (স্তম্ভাকার) কিন্তু পাইনাস ও সিড্রাসের কাণ্ড প্রচুর শাখাযুক্ত।',
    },
    {
        "id": 'BIO-PK-065',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Conifers are adapted to withstand extremes of temperature, humidity and wind by possessing:',
        "bn": 'কনিফার উদ্ভিদেরা তীব্র তাপমাত্রা, শুষ্কতা ও প্রবল বাতাসের সাথে খাপ খাইয়ে টিকে থাকার জন্য কোন বৈশিষ্ট্যগুলি প্রদর্শন করে?',
        "opts": {
            "en": ['Needle-like leaves to reduce surface area, thick cuticle, and sunken stomata', 'Broad membranous leaves with abundant hydathodes', 'Thin cuticle with stomata protruding outward on leaf margins', 'Compound leaves with large surface area and no cuticle'],
            "bn": ['পৃষ্ঠতলের ক্ষেত্রফল কমানোর জন্য সুচালো ছুঁচলো পাতা, পুরু কিউটিকল এবং নিমজ্জিত পত্ররন্ধ্র (sunken stomata)', 'চওড়া পাতলা পাতা ও প্রচুর জলরন্ধ্র', 'পাতলা কিউটিকল এবং পাতার কিনারায় বাইরের দিকে বের হওয়া পত্ররন্ধ্র', 'কিউটিকলহীন বৃহৎ যৌগিক পাতা']
        },
        "correct": 0,
        "expl_en": 'In conifers, the needle-like leaves reduce surface area. Their thick cuticle and sunken stomata also help to reduce water loss.',
        "expl_bn": 'বাষ্পমোচন রোধের জন্য কনিফারদের পাতা সুচালো হয়, কিউটিকল অত্যন্ত পুরু হয় এবং পত্ররন্ধ্রগুলি গর্তের ভেতরে নিমজ্জিত (sunken) থাকে।',
    },
    {
        "id": 'BIO-PK-066',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Are gymnosperms homosporous or heterosporous?',
        "bn": 'ব্যক্তবীজী উদ্ভিদেরা হোমোস্পোরাস নাকি হেটারোস্পোরাস?',
        "opts": {
            "en": ['Strictly heterosporous; they produce haploid microspores and megaspores', 'Strictly homosporous; they produce identical spores', 'Primitive gymnosperms are homosporous; advanced conifers are heterosporous', 'They do not produce any spores at all'],
            "bn": ['সর্বদা হেটারোস্পোরাস (Heterosporous); এরা হ্যাপ্লয়েড ক্ষুদ্ররেণু (মাইক্রোস্পোর) এবং গুরুরেণু (মেগাস্পোর) তৈরি করে', 'সর্বদা হোমোস্পোরাস', 'আদি ব্যক্তবীজীরা হোমোস্পোরাস এবং উন্নতরা হেটারোস্পোরাস', 'এরা কোনো প্রকার রেণুই তৈরি করে না']
        },
        "correct": 0,
        "expl_en": 'Gymnosperms are heterosporous; they produce haploid microspores and megaspores.',
        "expl_bn": 'সমস্ত ব্যক্তবীজী উদ্ভিদই হেটারোস্পোরাস (heterosporous); এরা ক্ষুদ্ররেণু (মাইক্রোস্পোর) এবং গুরুরেণু (মেগাস্পোর) উৎপাদন করে।',
    },
    {
        "id": 'BIO-PK-067',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In gymnosperms, the two kinds of spores are borne in sporangia on sporophylls which are arranged spirally along an axis to form lax or compact strobili or cones. The strobili bearing microsporophylls and microsporangia are called:',
        "bn": 'ব্যক্তবীজীতে মাইক্রোস্পোরোফিল ও মাইক্রোস্পোরাঞ্জিয়া যুক্ত পুং শঙ্কু বা স্ট্রোবিলাসকে কী বলা হয়?',
        "opts": {
            "en": ['Microsporangiate or male strobili', 'Macrosporangiate or seed cones', 'Archegoniophores', 'Inflorescence spike'],
            "bn": ['মাইক্রোস্পোরাঞ্জিয়েট বা পুং স্ট্রোবিলাস (Male strobili)', 'ম্যাক্রোস্পোরাঞ্জিয়েট বা বীজ শঙ্কু', 'আর্কেগোনিওফোর', 'পুষ্পমঞ্জরী স্পাইক']
        },
        "correct": 0,
        "expl_en": 'The strobili bearing microsporophylls and microsporangia are called microsporangiate or male strobili.',
        "expl_bn": 'মাইক্রোস্পোরোফিল ও মাইক্রোস্পোরাঞ্জিয়া ধারণকারী শঙ্কুকে পুং স্ট্রোবিলাস বা মেল কোন বলা হয়।',
    },
    {
        "id": 'BIO-PK-068',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The microspores develop into a highly reduced male gametophyte generation consisting of only a limited number of cells. This reduced male gametophyte is known as a:',
        "bn": 'মাইক্রোস্পোর বা পুংরেণু বিকশিত হয়ে অত্যন্ত সংক্ষিপ্ত ও স্বল্পকোষীয় পুং গ্যামেটোফাইট প্রজন্মে পরিণত হয়। এই সংক্ষিপ্ত গঠনটিকে কী বলা হয়?',
        "opts": {
            "en": ['Pollen grain', 'Prothallus', 'Endosperm', 'Nucellus'],
            "bn": ['পরাগরেণু (Pollen grain)', 'প্রোথ্যালাস', 'শস্য বা এন্ডোস্পার্ম', 'নিউসেলাস']
        },
        "correct": 0,
        "expl_en": 'The microspores develop into a male gametophytic generation which is highly reduced and is confined to only a limited number of cells. This reduced gametophyte is called a pollen grain.',
        "expl_bn": 'মাইক্রোস্পোর বিকশিত হয়ে স্বল্পকোষযুক্ত সংক্ষিপ্ত পুং গ্যামেটোফাইটে পরিণত হয় যাকে পরাগরেণু (Pollen grain) বলে।',
    },
    {
        "id": 'BIO-PK-069',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In Pinus, the male and female cones are borne on ________, whereas in Cycas, male cones and megasporophylls are borne on ________.',
        "bn": 'পাইনাসে পুং ও স্ত্রী শঙ্কু ________ জন্মায়, অন্যদিকে সাইকাসে পুং শঙ্কু ও মেগাস্পোরোফিল ________ জন্মায়।',
        "opts": {
            "en": ['The same tree (monoecious); different trees (dioecious)', 'Different trees (dioecious); the same tree (monoecious)', 'Underground roots; aerial leaf tips', 'Aquatic branches; dry trunks'],
            "bn": ['একই গাছে (সহবাসী বা monoecious); পৃথক পৃথক গাছে (ভিন্নবাসী বা dioecious)', 'ভিন্ন ভিন্ন গাছে; একই গাছে', 'মাটির নিচের মূলে; বায়বীয় পাতার শীর্ষে', 'জলজ ডালে; শুষ্ক গুঁড়িতে']
        },
        "correct": 0,
        "expl_en": 'The male or female cones may be borne on the same tree in Pinus (monoecious). In Cycas, male cones and megasporophylls are borne on different trees (dioecious).',
        "expl_bn": 'পাইনাসের একই গাছে পুং ও স্ত্রী শঙ্কু উভয়ই জন্মায় (সহবাসী), কিন্তু সাইকাসে পুং গাছ এবং স্ত্রী গাছ সম্পূর্ণ পৃথক হয় (ভিন্নবাসী)।',
    },
    {
        "id": 'BIO-PK-070',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'In gymnosperms, the megaspore mother cell is differentiated from one of the cells of the:',
        "bn": 'ব্যক্তবীজী উদ্ভিদে মেগাস্পোর মাতৃকোষটি (Megaspore mother cell) কার একটি কোষ থেকে বিভেদিত হয়?',
        "opts": {
            "en": ['Nucellus (which is protected by envelopes and composite structure is ovule)', 'Outer tapetum layer of microsporangium', 'Stipe epidermis', 'Integumentary stone layer'],
            "bn": ['নিউসেলাস (Nucellus, যা ত্বক দ্বারা আবৃত থাকে এবং সমগ্র গঠনটি ডিম্বক গঠন করে)', 'মাইক্রোস্পোরাঞ্জিয়ামের বহিস্থ ট্যাপিটাম', 'স্ট্রাইপের বহিস্ত্বক', 'ত্বকের পাথুরে স্তর']
        },
        "correct": 0,
        "expl_en": 'The megaspore mother cell is differentiated from one of the cells of the nucellus. The nucellus is protected by envelopes and the composite structure is called an ovule.',
        "expl_bn": 'নিউসেলাসের (nucellus) একটি কোষ রূপান্তরিত হয়ে মেগাস্পোর মাতৃকোষ গঠন করে। নিউসেলাস ত্বক দ্বারা আবৃত হয়ে ডিম্বক (ovule) তৈরি করে।',
    },
    {
        "id": 'BIO-PK-071',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'In gymnosperms, the megaspore mother cell divides meiotically to form four megaspores. How many functional megaspores develop into a multicellular female gametophyte?',
        "bn": 'ব্যক্তবীজী উদ্ভিদে মেগাস্পোর মাতৃকোষ মায়োসিস বিভাজনের মাধ্যমে চারটি মেগাস্পোর তৈরি করে। এদের মধ্যে কতগুলি সক্রিয় মেগাস্পোর বহুকোষী স্ত্রী গ্যামেটোফাইটে পরিণত হয়?',
        "opts": {
            "en": ['One functional megaspore (which develops into female gametophyte enclosed within megasporangium)', 'All four functional megaspores', 'Two functional megaspores', 'Three functional megaspores'],
            "bn": ['একটিমাত্র সক্রিয় মেগাস্পোর (যা মেগাস্পোরাঞ্জিয়ামের ভেতরে বহুকোষী স্ত্রী গ্যামেটোফাইটে রূপান্তরিত হয়)', 'চারটি মেগাস্পোরই', 'দুটি মেগাস্পোর', 'তিনটি মেগাস্পোর']
        },
        "correct": 0,
        "expl_en": 'One of the megaspores enclosed within the megasporangium develops into a multicellular female gametophyte that bears two or more archegonia or female sex organs.',
        "expl_bn": 'চারটি মেগাস্পোরের মধ্যে তিনটি বিনষ্ট হয় এবং একটিমাত্র সক্রিয় মেগাস্পোর বহুকোষী স্ত্রী গ্যামেটোফাইটে পরিণত হয় যাতে দুই বা ততোধিক আর্কেগোনিয়া থাকে।',
    },
    {
        "id": 'BIO-PK-072',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'The endosperm of gymnosperms is ________ and formed ________ fertilization.',
        "bn": 'ব্যক্তবীজী উদ্ভিদের শস্য বা এন্ডোস্পার্ম (Endosperm) হলো ________ এবং এটি নিষেকের ________ গঠিত হয়।',
        "opts": {
            "en": ['Haploid (n); before', 'Triploid (3n); after', 'Diploid (2n); after', 'Tetraploid (4n); before'],
            "bn": ['হ্যাপ্লয়েড (n); পূর্বে', 'ট্রিপ্লয়েড (3n); পরে', 'ডিপ্লয়েড (2n); পরে', 'টেট্রাপ্লয়েড (4n); পূর্বে']
        },
        "correct": 0,
        "expl_en": 'In gymnosperms, the endosperm directly represents the multicellular vegetative tissue of the haploid female gametophyte and is formed BEFORE fertilization (hence haploid, n). In angiosperms, it is triploid (3n) formed after double fertilization.',
        "expl_bn": 'ব্যক্তবীজী উদ্ভিদে শস্য মূলত স্ত্রী গ্যামেটোফাইটের রূপান্তরিত পুষ্টি কলা, যা নিষেকের আগেই তৈরি হয়; তাই এটি সর্বদা হ্যাপ্লয়েড (n)। গুপ্তবীজীতে এটি নিষেকের পরে গঠিত ট্রিপ্লয়েড (3n)।',
    },
    {
        "id": 'BIO-PK-073',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Unlike bryophytes and pteridophytes, in gymnosperms the male and female gametophytes:',
        "bn": 'ব্রায়োফাইটা এবং টেরিডোফাইটার বিপরীতে, ব্যক্তবীজী উদ্ভিদে পুং এবং স্ত্রী গ্যামেটোফাইটগুলির ক্ষেত্রে কোন বৈশিষ্ট্যটি পরিলক্ষিত হয়?',
        "opts": {
            "en": ['Do not have an independent, free-living existence and remain within the sporangia retained on sporophytes', 'Are free-living, independent, and photosynthetic thalli', 'Bear multi-ciliated swimming antherozoids requiring open pond water', 'Form creeping green protonema on wet forest floors'],
            "bn": ['কোনো স্বাধীন বা মুক্তজীবী অস্তিত্ব থাকে না, বরং তারা স্পোরোফাইটের গায়ে সংলগ্ন স্পোরাঞ্জিয়ার ভেতরেই আবদ্ধ থাকে', 'সম্পূর্ণ স্বাধীনজীবী এবং সালোকসংশ্লেষকারী থ্যালাস', 'মুক্ত জলাশয়ে সাঁতার কাটার মতো বহু-সিলিয়াযুক্ত শুক্রাণু তৈরি করে', 'স্যাঁতসেঁতে মাটিতে সবুজ শায়িত প্রোটোনেমা গঠন করে']
        },
        "correct": 0,
        "expl_en": 'Unlike bryophytes and pteridophytes, in gymnosperms the male and female gametophytes do not have an independent free-living existence. They remain within the sporangia retained on the sporophytes.',
        "expl_bn": 'ব্রায়োফাইট বা ফার্নের মতো ব্যক্তবীজীর গ্যামেটোফাইটের কোনো স্বাধীন জীবন নেই; এরা মাতৃ স্পোরোফাইটের স্পোরাঞ্জিয়ামের ভেতরেই আশ্রয় ও পুষ্টি লাভ করে।',
    },
    {
        "id": 'BIO-PK-074',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In gymnosperms, pollination is primarily carried out by:',
        "bn": 'ব্যক্তবীজী উদ্ভিদে পরাগযোগ মূলত কার দ্বারা সম্পন্ন হয়?',
        "opts": {
            "en": ['Air currents (Anemophily)', 'Insects (Entomophily)', 'Water currents (Hydrophily)', 'Bats (Chiropterophily)'],
            "bn": ['বায়ু প্রবাহ দ্বারা (Anemophily)', 'পতঙ্গ দ্বারা', 'জলস্রোত দ্বারা', 'বাদুড় দ্বারা']
        },
        "correct": 0,
        "expl_en": 'Pollen grains are released from the microsporangium and carried in air currents (wind pollination) to come into contact with the opening of the ovules borne on megasporophylls.',
        "expl_bn": 'ব্যক্তবীজী উদ্ভিদে পরাগরেণুগুলি বায়ুপ্রবাহের মাধ্যমে পরিবাহিত হয়ে মেগাস্পোরোফিলের ডিম্বকরন্ধ্রে এসে পৌঁছায় (বায়ুপরাগী বা Anemophilous)।',
    },
    {
        "id": 'BIO-PK-075',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The transfer of male gametes to the archegonia in gymnosperms occurs via a structure called the:',
        "bn": 'ব্যক্তবীজীতে আর্কেগোনিয়ামের মুখে শুক্রাণু পৌঁছানোর জন্য কোন গঠনটি তৈরি হয়?',
        "opts": {
            "en": ['Pollen tube (Siphonogamy)', 'Flagellar undulating membrane', 'Mucilage thread', 'Water meniscus'],
            "bn": ['পরাগনালী বা পোলেন টিউব (Siphonogamy)', 'ফ্ল্যাজেলার আনডুলেটিং পর্দা', 'মিউসিলেজের সূত্র', 'জলের মেনিস্কাস']
        },
        "correct": 0,
        "expl_en": 'The pollen tube carrying the male gametes grows towards archegonia in the ovules and discharges its contents near the mouth of the archegonia (siphonogamous fertilization).',
        "expl_bn": 'পরাগরেণু থেকে পরাগনালী (pollen tube) উৎপন্ন হয়ে শুক্রাণুকে সরাসরি আর্কেগোনিয়ামের মুখে পৌঁছে দেয়। এই পদ্ধতিকে সাইফোনোগ্যামি (siphonogamy) বলে।',
    },
    {
        "id": 'BIO-PK-076',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following is a living fossil among gymnosperms that possesses motile flagellated sperm and fan-shaped leaves?',
        "bn": "ব্যক্তবীজী উদ্ভিদের মধ্যে কোনটিকে চলনক্ষম ফ্ল্যাজেলাযুক্ত শুক্রাণু এবং পাখার মতো পাতাবিশিষ্ট 'জীবন্ত জীবাশ্ম' বলা হয়?",
        "opts": {
            "en": ['Ginkgo biloba', 'Pinus roxburghii', 'Cedrus deodara', 'Ephedra foliata'],
            "bn": ['জিংগো বাইলোবা (Ginkgo biloba)', 'পাইনাস রক্সবারঘি', 'সিড্রাস দেওদারা', 'এফেড্রা']
        },
        "correct": 0,
        "expl_en": 'Ginkgo biloba (maidenhair tree) is a living fossil gymnosperm displaying primitive traits including flagellated male gametes and fan-shaped dichotomy in venation.',
        "expl_bn": 'Ginkgo biloba হলো ব্যক্তবীজীদের মধ্যে একটি জীবন্ত জীবাশ্ম যার আদিম বৈশিষ্ট্য হিসেবে ফ্ল্যাজেলাযুক্ত সচল শুক্রাণু দেখা যায়।',
    },
    {
        "id": 'BIO-PK-077',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": "The drug 'Ephedrine' used in curing respiratory ailments is extracted from the gymnosperm:",
        "bn": "শ্বাসকষ্ট ও হাঁপানির উপশমে ব্যবহৃত ওষুধ 'এফেড্রিন' (Ephedrine) কোন ব্যক্তবীজী উদ্ভিদ থেকে নিষ্কাশন করা হয়?",
        "opts": {
            "en": ['Ephedra', 'Pinus', 'Cycas', 'Gnetum'],
            "bn": ['এফেড্রা (Ephedra)', 'পাইনাস', 'সাইকাস', 'নিটাম']
        },
        "correct": 0,
        "expl_en": 'Ephedrine is an alkaloid obtained from Ephedra, a gymnosperm belonging to Gnetales, used to treat asthma and respiratory congestion.',
        "expl_bn": 'এফেড্রা (Ephedra) নামক ব্যক্তবীজী উদ্ভিদ থেকে হাঁপানির মহৌষধ এফেড্রিন পাওয়া যায়।',
    },
    {
        "id": 'BIO-PK-078',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Canada balsam, a mounting medium used for permanent microscopic slides, is obtained from:',
        "bn": "স্থায়ী মাইক্রোস্কোপিক স্লাইড তৈরিতে ব্যবহৃত মাউন্টিং মিডিয়াম 'কানাডা বালসাম' কোন ব্যক্তবীজী থেকে প্রস্তুত হয়?",
        "opts": {
            "en": ['Abies balsamea', 'Pinus sylvestris', 'Cycas revoluta', 'Taxus baccata'],
            "bn": ['অ্যাবিজ বালসামিয়া (Abies balsamea)', 'পাইনাস সিলভেস্ট্রিস', 'সাইকাস রেভোলুটা', 'ট্যাক্সাস ব্যাক্কাটা']
        },
        "correct": 0,
        "expl_en": 'Canada balsam is a resin obtained from the balsam fir tree (Abies balsamea), a gymnosperm conifer.',
        "expl_bn": 'অ্যাবিজ বালসামিয়া (Abies balsamea) নামক কনিফার ব্যক্তবীজীর রজন থেকে কানাডা বালসাম প্রস্তুত করা হয়।',
    },
    {
        "id": 'BIO-PK-079',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": "Which of the following is commonly known as 'Sago palm' yielding edible starch from its stem pith?",
        "bn": "কোন উদ্ভিদটিকে 'সাবু পাম' বলা হয় যার কাণ্ডের মজ্জা থেকে ভোজ্য সাবুদানা প্রস্তুত করা হয়?",
        "opts": {
            "en": ['Cycas revoluta', 'Pinus pinea', 'Ginkgo biloba', 'Taxus brevifolia'],
            "bn": ['সাইকাস রেভোলুটা (Cycas revoluta)', 'পাইনাস পাইনিয়া', 'জিংগো', 'ট্যাক্সাস']
        },
        "correct": 0,
        "expl_en": 'Starch extracted from the stem pith of Cycas revoluta and Cycas rumphii is processed to yield edible sago (sabudana).',
        "expl_bn": 'সাইকাসের (Cycas revoluta) কাণ্ডের মজ্জা থেকে স্টার্চ সংগ্রহ করে সাবু বা সাবুদানা প্রস্তুত করা হয়।',
    },
    {
        "id": 'BIO-PK-080',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Vessels in xylem and companion cells in phloem are characteristically absent in gymnosperms EXCEPT in which advanced order?',
        "bn": 'ব্যক্তবীজীদের জাইলেমে ভেসেল ও ফ্লোয়েমে সঙ্গী কোষ অনুপস্থিত থাকে, তবে এর ব্যতিক্রমী উন্নত কোন বর্গটিতে প্রকৃত ভেসেল উপস্থিত থাকে?',
        "opts": {
            "en": ['Gnetales (Gnetum, Ephedra, Welwitschia)', 'Coniferales (Pinus, Cedrus)', 'Cycadales (Cycas)', 'Ginkgoales (Ginkgo)'],
            "bn": ['নিটালেস বা Gnetales (Gnetum, Ephedra, Welwitschia)', 'কনিফারেলেস (পাইনাস, সিড্রাস)', 'সাইকাডালেস (সাইকাস)', 'জিংগোয়ালেস (জিংগো)']
        },
        "correct": 0,
        "expl_en": 'Gnetales (Gnetum, Ephedra, and Welwitschia) are advanced gymnosperms showing angiospermic affinities, including the presence of true vessels in their secondary xylem.',
        "expl_bn": 'ব্যক্তবীজী নিটালেস বর্গের (Gnetum, Ephedra, Welwitschia) জাইলেমে ব্যতিক্রমীভাবে গুপ্তবীজীর ন্যায় উন্নত ভেসেল উপাদান বর্তমান থাকে।',
    },
    {
        "id": 'BIO-PK-081',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'In Angiosperms, seeds are enclosed inside:',
        "bn": 'গুপ্তবীজী বা অ্যাঞ্জিওস্পার্ম উদ্ভিদে বীজগুলি কার ভেতরে আবদ্ধ থাকে?',
        "opts": {
            "en": ['Fruits (derived from the ripened ovary wall)', 'Naked cone scales', 'Archegonial neck canal', 'Peristome teeth'],
            "bn": ['ফল (পরিপক্ব ডিম্বাশয় প্রাচীর দ্বারা গঠিত)', 'অনাবৃত শঙ্কু শল্ক', 'আর্কেগোনিয়ামের গ্রীবানালী', 'পেরিস্টোম দাঁত']
        },
        "correct": 0,
        "expl_en": 'Unlike gymnosperms where ovules are naked, in angiosperms the pollen grains and ovules are developed in specialised structures called flowers and seeds are enclosed inside fruits.',
        "expl_bn": 'গুপ্তবীজীতে ডিম্বকগুলি ডিম্বাশয়ের ভেতরে আবদ্ধ থাকে এবং নিষেকের পর ডিম্বাশয়টি ফলে রূপান্তরিত হয়ে বীজকে আবৃত করে রাখে।',
    },
    {
        "id": 'BIO-PK-082',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'The smallest angiosperm is ________ and the tallest angiosperm tree is ________ reaching over 100 meters.',
        "bn": 'ক্ষুদ্রতম গুপ্তবীজী উদ্ভিদ হলো ________ এবং ১০০ মিটারেরও বেশি উচ্চতা বিশিষ্ট দীর্ঘতম গুপ্তবীজী বৃক্ষ হলো ________।',
        "opts": {
            "en": ['Wolffia; Eucalyptus', 'Eucalyptus; Wolffia', 'Lemna; Sequoia', 'Chlorella; Macrocystis'],
            "bn": ['উলফিয়া (Wolffia); ইউক্যালিপটাস (Eucalyptus)', 'ইউক্যালিপটাস; উলফিয়া', 'লেমনা; সেকোয়া', 'ক্লোরেলা; ম্যাক্রোসিস্টাস']
        },
        "correct": 0,
        "expl_en": 'The smallest angiosperm is microscopic Wolffia and the tallest is Eucalyptus (which can grow over 100 metres). Note that Sequoia is a gymnosperm!',
        "expl_bn": 'সবচেয়ে ক্ষুদ্রাকার গুপ্তবীজী হলো Wolffia (ক্ষুদ্র জলজ উদ্ভিদ) এবং সবচেয়ে উঁচু গুপ্তবীজী বৃক্ষ হলো Eucalyptus (১০০ মিটারের বেশি)। (Sequoia হলো ব্যক্তবীজী)।',
    },
    {
        "id": 'BIO-PK-083',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Angiosperms are divided into two primary classes: Dicotyledons and Monocotyledons. Which of the following features characterizes Dicotyledons?',
        "bn": 'গুপ্তবীজী উদ্ভিদকে দুটি প্রধান শ্রেণিতে ভাগ করা হয়: দ্বিবীজপত্রী এবং একবীজপত্রী। নিচের কোন বৈশিষ্ট্যটি দ্বিবীজপত্রী উদ্ভিদের পরিচায়ক?',
        "opts": {
            "en": ['Two cotyledons in seeds, reticulate venation in leaves, and tetramerous or pentamerous flowers', 'Single cotyledon in seeds, parallel venation in leaves, and trimerous flowers', 'Absence of secondary growth and scattered vascular bundles in stem', 'Fibrous root system without any primary taproot'],
            "bn": ['বীজে দুটি বীজপত্র, পাতায় জালকাকার শিরাবিন্যাস এবং চতুরংশ বা পঞ্চাংশক বিশিষ্ট ফুল', 'বীজে একটিমাত্র বীজপত্র, সমান্তরাল শিরাবিন্যাস এবং ত্রেয়াংশক ফুল', 'গৌণ বৃদ্ধির অনুপস্থিতি এবং কাণ্ডে বিক্ষিপ্ত সংবহন বান্ডিল', 'স্থানিক প্রধান মূলহীন গুচ্ছমূল ব্যবস্থা']
        },
        "correct": 0,
        "expl_en": 'The dicotyledons are characterized by seeds having two cotyledons, reticulate venation in leaves, and tetramerous or pentamerous flowers.',
        "expl_bn": 'দ্বিবীজপত্রী উদ্ভিদের বীজে দুটি বীজপত্র, পাতায় জালকাকার শিরাবিন্যাস এবং ফুলে ৪ বা ৫-এর গুণিতকে পুষ্পপত্র (টেট্রামেরাস বা পেন্টামেরাস) থাকে।',
    },
    {
        "id": 'BIO-PK-084',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The characteristic event unique to Angiosperms that involves Syngamy (yielding 2n zygote) and Triple Fusion (yielding 3n PEN) is known as:',
        "bn": 'গুপ্তবীজী উদ্ভিদের এক অনন্য বৈশিষ্ট্যপূর্ণ ঘটনা যাতে সিঙ্গ্যামি (ডিপ্লয়েড জাইগোট গঠন) এবং ট্রিপল ফিউশন (ট্রিপ্লয়েড প্রাথমিক শস্য নিউক্লিয়াস গঠন) একসাথে ঘটে, তাকে কী বলে?',
        "opts": {
            "en": ['Double fertilization', 'Apomixis', 'Parthenocarpy', 'Polyembryony'],
            "bn": ['দ্বি-নিষেক (Double fertilization)', 'অ্যাপোমিক্সিস', 'পার্থেনোকার্পি', 'পলিএমব্রায়োনি']
        },
        "correct": 0,
        "expl_en": 'Double fertilisation is an event unique to angiosperms, where one male gamete fuses with the egg (syngamy) and the other fuses with the secondary diploid nucleus (triple fusion).',
        "expl_bn": 'একটি পুং গ্যামেট ডিম্বাণুকে নিষিক্ত করে জাইগোট (2n) এবং অপর পুং গ্যামেট নির্ণীত নিউক্লিয়াসকে নিষিক্ত করে ট্রিপ্লয়েড শস্য (3n) তৈরি করে। এই জোড়া ঘটনাকে দ্বি-নিষেক বলে।',
    },
    {
        "id": 'BIO-PK-085',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'In a HAPLONTIC life cycle, which of the following statements is TRUE?',
        "bn": 'হ্যাপ্লন্টিক (Haplontic) জীবনচক্রের ক্ষেত্রে নিচের কোন বক্তব্যটি সঠিক?',
        "opts": {
            "en": ['Sporophytic generation is represented only by the one-celled diploid zygote; there are no free-living sporophytes', 'The dominant photosynthetic phase is a large multicellular diploid tree', 'Meiosis occurs in gametangia to produce haploid gametes', 'Both gametophyte and sporophyte are equally dominant and free-living'],
            "bn": ['স্পোরোফাইট প্রজন্মটি কেবলমাত্র এককোষী ডিপ্লয়েড জাইগোট দ্বারা প্রতিনিধিত্ব হয়; কোনো মুক্তজীবী স্পোরোফাইট থাকে না', 'প্রধান সালোকসংশ্লেষকারী দশাটি হলো বহুকোষী ডিপ্লয়েড বৃক্ষ', 'গ্যামেট তৈরিতে গ্যামেটানজিয়ামে মায়োসিস ঘটে', 'গ্যামেটোফাইট এবং স্পোরোফাইট উভয়ই সমানভাবে দীর্ঘজীবী ও মুক্তজীবী']
        },
        "correct": 0,
        "expl_en": 'In haplontic life cycles, the sporophytic generation is represented only by the one-celled zygote. There are no free-living sporophytes. Meiosis in the zygote results in the formation of haploid spores.',
        "expl_bn": 'হ্যাপ্লন্টিক জীবনচক্রে স্পোরোফাইট দশা বলতে কেবল ডিপ্লয়েড জাইগোটকেই বোঝায়। জাইগোটে সরাসরি মায়োসিস বিভাজন (Zygotic meiosis) ঘটে এবং হ্যাপ্লয়েড দশাটিই প্রধান উদ্ভিদদেহ হিসেবে থাকে।',
    },
    {
        "id": 'BIO-PK-086',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following algae exhibits a typical HAPLONTIC life cycle?',
        "bn": 'নিচের কোন শৈবালটিতে আদর্শ হ্যাপ্লন্টিক (Haplontic) জীবনচক্র দেখা যায়?',
        "opts": {
            "en": ['Volvox, Spirogyra, and Chlamydomonas', 'Fucus and Sargassum', 'Ectocarpus and Polysiphonia', 'Kelps and Laminaria'],
            "bn": ['ভলভক্স, স্পাইরোগাইরা এবং ক্ল্যামাইডোমোনাস', 'ফিউকাস এবং সারগাসাম', 'এক্টোকার্পাস এবং পলিসাইফোনিয়া', 'কেল্প এবং ল্যামিনারিয়া']
        },
        "correct": 0,
        "expl_en": 'Many algae such as Volvox, Spirogyra, and some species of Chlamydomonas represent the haplontic life cycle pattern.',
        "expl_bn": 'Volvox, Spirogyra এবং Chlamydomonas-এর জীবনচক্র হলো হ্যাপ্লন্টিক প্রকৃতির।',
    },
    {
        "id": 'BIO-PK-087',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'In a DIPLONTIC life cycle, which phase is the dominant, photosynthetic, independent phase of the plant?',
        "bn": 'ডিপ্লন্টিক (Diplontic) জীবনচক্রে উদ্ভিদের প্রধান, স্বাধীন এবং সালোকসংশ্লেষকারী দশাটি কোনটি?',
        "opts": {
            "en": ['Diploid sporophyte (gametophyte is reduced to single or few-celled stage)', 'Haploid gametophyte (sporophyte is reduced to one cell)', 'Prothallus', 'Secondary protonema'],
            "bn": ['ডিপ্লয়েড স্পোরোফাইট (গ্যামেটোফাইট দশা এককোষী বা স্বল্পকোষীতে সীমাবদ্ধ থাকে)', 'হ্যাপ্লয়েড গ্যামেটোফাইট', 'প্রোথ্যালাস', 'গৌণ প্রোটোনেমা']
        },
        "correct": 0,
        "expl_en": 'In a diplontic life cycle, the diploid sporophyte is the dominant, photosynthetic, independent phase of the plant. The gametophytic phase is represented by the single to few-celled haploid gametophyte.',
        "expl_bn": 'ডিপ্লন্টিক জীবনচক্রে ডিপ্লয়েড (2n) স্পোরোফাইট দশাটিই প্রধান ও স্বাধীন। গ্যামেটোফাইট অত্যন্ত সংক্ষিপ্ত এবং পরাগরেণু বা ভ্রূণস্থলীর কয়েক কোষে সীমাবদ্ধ থাকে।',
    },
    {
        "id": 'BIO-PK-088',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Which ALGA represents an exception by displaying a DIPLONTIC life cycle (unlike most other green algae)?',
        "bn": 'অধিকাংশ শৈবালের ব্যতিক্রম হিসেবে নিচের কোন শৈবালটিতে ডিপ্লন্টিক (Diplontic) জীবনচক্র দেখা যায়?',
        "opts": {
            "en": ['Fucus', 'Volvox', 'Spirogyra', 'Chara'],
            "bn": ['ফিউকাস (Fucus)', 'ভলভক্স', 'স্পাইরোগাইরা', 'কারা']
        },
        "correct": 0,
        "expl_en": 'An alga, Fucus sp., represents a diplontic life cycle pattern (NCERT specific exception highlight). In addition, all seed-bearing plants (gymnosperms and angiosperms) follow this pattern.',
        "expl_bn": 'NCERT-এর অত্যন্ত গুরুত্বপূর্ণ ব্যতিক্রম: Fucus নামক বাদামী শৈবালটিতে ডিপ্লন্টিক জীবনচক্র দেখা যায়।',
    },
    {
        "id": 'BIO-PK-089',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'In a HAPLODIPLONTIC life cycle, both phases are multicellular. Which plant groups characteristically exhibit a haplodiplontic life cycle?',
        "bn": 'হ্যাপ্লোডিপ্লন্টিক (Haplodiplontic) জীবনচক্রে উভয় দশাই বহুকোষী হয়। কোন উদ্ভিদ গোষ্ঠীগুলির জীবনচক্রের মূল বৈশিষ্ট্য হলো হ্যাপ্লোডিপ্লন্টিক ধরন?',
        "opts": {
            "en": ['Bryophytes and Pteridophytes', 'Angiosperms and Gymnosperms', 'Fucus and Volvox', 'Cyanobacteria and Mycoplasma'],
            "bn": ['ব্রায়োফাইটা এবং টেরিডোফাইটা', 'গুপ্তবীজী এবং ব্যক্তবীজী', 'ফিউকাস এবং ভলভক্স', 'সায়ানোব্যাকটেরিয়া এবং মাইকোপ্লাজমা']
        },
        "correct": 0,
        "expl_en": 'Bryophytes and pteridophytes, interestingly, exhibit an intermediate condition — haplodiplontic life cycle, wherein both haploid and diploid phases are multicellular.',
        "expl_bn": 'ব্রায়োফাইটা এবং টেরিডোফাইটা উভয় দলেই সুস্পষ্ট হ্যাপ্লোডিপ্লন্টিক (Haplodiplontic) জীবনচক্র দেখা যায়, যেখানে রেণুধর ও লিঙ্গধর উভয় দশাই বহুকোষী।',
    },
    {
        "id": 'BIO-PK-090',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'How does the haplodiplontic life cycle of a Bryophyte differ from that of a Pteridophyte?',
        "bn": 'ব্রায়োফাইটার হ্যাপ্লোডিপ্লন্টিক জীবনচক্র কীভাবে টেরিডোফাইটার হ্যাপ্লোডিপ্লন্টিক জীবনচক্র থেকে পৃথক?',
        "opts": {
            "en": ['In Bryophytes, the dominant phase is the free-living gametophyte; in Pteridophytes, the dominant phase is the independent vascular sporophyte', 'In Bryophytes, the sporophyte is free-living and vascular; in Pteridophytes, it is parasitic', 'In Bryophytes, meiosis is gametic; in Pteridophytes, meiosis is zygotic', 'In Bryophytes, seeds are formed; in Pteridophytes, seeds are naked'],
            "bn": ['ব্রায়োফাইটাতে প্রধান দশা হলো স্বাধীন গ্যামেটোফাইট; কিন্তু টেরিডোফাইটাতে প্রধান দশা হলো স্বাধীন সংবহনকলাযুক্ত স্পোরোফাইট', 'ব্রায়োফাইটাতে স্পোরোফাইট স্বাধীন ও সংবহনযুক্ত; কিন্তু টেরিডোফাইটাতে তা পরজীবী', 'ব্রায়োফাইটাতে গ্যামেটিক মায়োসিস এবং টেরিডোফাইটাতে জাইগোটিক মায়োসিস ঘটে', 'ব্রায়োফাইটাতে বীজ তৈরি হয় এবং টেরিডোফাইটাতে বীজ অনাবৃত থাকে']
        },
        "correct": 0,
        "expl_en": 'In Bryophytes, the dominant, independent, photosynthetic phase is a haploid gametophyte, alternating with a short-lived dependent sporophyte. In Pteridophytes, the diploid sporophyte is the dominant, independent, vascular phase alternating with a multicellular independent saprophytic/autotrophic prothallus.',
        "expl_bn": 'ব্রায়োফাইটাতে লিঙ্গধর বা গ্যামেটোফাইট দশা প্রধান ও স্বাধীন এবং স্পোরোফাইট তার ওপর নির্ভরশীল। কিন্তু টেরিডোফাইটাতে রেণুধর বা স্পোরোফাইট দশা প্রধান ও উন্নত সংবহনকলাযুক্ত।',
    },
    {
        "id": 'BIO-PK-091',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Which of the following algae exhibit HAPLODIPLONTIC life cycles (deviating from the typical haplontic condition of algae)?',
        "bn": 'নিচের কোন শৈবালগুলি সাধারণ শৈবালের হ্যাপ্লন্টিক দশার ব্যতিক্রম হিসেবে হ্যাপ্লোডিপ্লন্টিক (Haplodiplontic) জীবনচক্র প্রদর্শন করে?',
        "opts": {
            "en": ['Ectocarpus, Polysiphonia, and Kelps', 'Volvox, Spirogyra, and Chlamydomonas', 'Fucus and Sargassum', 'Chlorella and Scenedesmus'],
            "bn": ['এক্টোকার্পাস, পলিসাইফোনিয়া এবং কেল্প (Ectocarpus, Polysiphonia, Kelps)', 'ভলভক্স, স্পাইরোগাইরা এবং ক্ল্যামাইডোমোনাস', 'ফিউকাস এবং সারগাসাম', 'ক্লোরেলা এবং সিনেডেস্মাস']
        },
        "correct": 0,
        "expl_en": 'NCERT explicitly notes: Interestingly, while most algal genera are haplontic, some of them such as Ectocarpus, Polysiphonia, kelps are haplodiplontic. Fucus, an alga, is diplontic.',
        "expl_bn": 'NCERT-এর অতি গুরুত্বপূর্ণ তথ্য: অধিকাংশ শৈবাল হ্যাপ্লন্টিক হলেও Ectocarpus, Polysiphonia এবং Kelps হলো হ্যাপ্লোডিপ্লন্টিক (Haplodiplontic)।',
    },
    {
        "id": 'BIO-PK-092',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'In which plant group do the male gametes reach the female gamete exclusively by swimming through water droplets without forming a pollen tube?',
        "bn": 'কোন উদ্ভিদ গোষ্ঠীতে পুং গ্যামেট পরাগনালী গঠন না করে শুধুমাত্র জলের ফোঁটায় সাঁতার কেটে স্ত্রী গ্যামেটের কাছে পৌঁছায়?',
        "opts": {
            "en": ['Bryophytes and Pteridophytes (Zooidogamy)', 'Gymnosperms and Angiosperms', 'Angiosperms only', 'Conifers only'],
            "bn": ['ব্রায়োফাইটা এবং টেরিডোফাইটা (Zooidogamy)', 'ব্যক্তবীজী এবং গুপ্তবীজী', 'কেবল গুপ্তবীজী', 'কেবল কনিফার']
        },
        "correct": 0,
        "expl_en": 'Bryophytes and lower pteridophytes show zooidogamy, where ciliated/flagellated male gametes swim through film of water to reach the archegonium. Seed plants use siphonogamy (pollen tube).',
        "expl_bn": 'ব্রায়োফাইট এবং টেরিডোফাইটে ফ্ল্যাজেলাযুক্ত শুক্রাণু জলের ফিল্মের মধ্য দিয়ে সাঁতার কেটে ডিম্বাণুর কাছে যায় (Zooidogamy)।',
    },
    {
        "id": 'BIO-PK-093',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Coralloid roots of Cycas exhibit negative geotropism and contain endosymbionts in their cortical zone. These endosymbionts are:',
        "bn": 'সাইকাসের কোরালয়েড মূলগুলি ঋণাত্মক অভিকর্ষবর্তী এবং এদের কর্টেক্সে কোন মিথোজীবী বাস করে?',
        "opts": {
            "en": ['Nostoc and Anabaena (Cyanobacteria)', 'Glomus (Mycorrhizal fungus)', 'Rhizobium leguminosarum', 'Frankia actinomycete'],
            "bn": ['নস্টক এবং অ্যানাবিনা (সায়ানোব্যাকটেরিয়া)', 'গ্লোমাস (ছত্রাক)', 'রাইজোবিয়াম', 'ফ্রাঙ্কিয়া']
        },
        "correct": 0,
        "expl_en": 'Coralloid roots of Cycas possess a distinct blue-green algal zone in the middle cortex harbouring Nostoc and Anabaena for nitrogen fixation.',
        "expl_bn": 'সাইকাসের কোরালয়েড মূলের কর্টেক্সে নাইট্রোজেন সংবন্ধনকারী নীলাভ সবুজ শৈবাল নস্টক (Nostoc) ও অ্যানাবিনা (Anabaena) বাস করে।',
    },
    {
        "id": 'BIO-PK-094',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'The female cone of Pinus corresponds to:',
        "bn": 'পাইনাসের স্ত্রী শঙ্কু (Female cone) মূলত কিসের সমতুল্য?',
        "opts": {
            "en": ['A cluster of megasporophylls bearing ovuliferous scales arranged on a central axis', 'A single modified leaf with two ovules', 'An inflorescence of microsporophylls', 'A vegetative dwarf shoot with needle leaves'],
            "bn": ['একটি কেন্দ্রীয় অক্ষের চারদিকে সর্পিলাকারে সজ্জিত ওভিউলিফেরাস স্কেলযুক্ত মেগাস্পোরোফিলের স্তবক', 'দুটি ডিম্বকযুক্ত একটিমাত্র রূপান্তরিত পাতা', 'মাইক্রোস্পোরোফিলের পুষ্পমঞ্জরী', 'সূচাকার পাতাবিশিষ্ট ক্ষুদ্র বিটপ']
        },
        "correct": 0,
        "expl_en": 'The female cone in Pinus is a compound strobilus consisting of a central cone axis bearing bract scales and ovuliferous scales (megasporophyll complex).',
        "expl_bn": 'পাইনাসের স্ত্রী শঙ্কু একটি যৌগিক স্ট্রোবিলাস যাতে অক্ষের চারিদিকে ব্র্যাক্ট স্কেল ও ওভিউলিফেরাস স্কেলের ওপর ডিম্বক ধারণকারী মেগাস্পোরোফিল বিন্যস্ত থাকে।',
    },
    {
        "id": 'BIO-PK-095',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Chilgoza, an edible dry fruit rich in proteins and oil, is the seed of:',
        "bn": "প্রোটিন ও তেল সমৃদ্ধ সুস্বাদু শুষ্ক ফল 'চিলগোজা' (Chilgoza) কোন ব্যক্তবীজী গাছের বীজ?",
        "opts": {
            "en": ['Pinus gerardiana', 'Pinus roxburghii', 'Cycas circinalis', 'Ginkgo biloba'],
            "bn": ['পাইনাস জেরার্ডিয়ানা (Pinus gerardiana)', 'পাইনাস রক্সবারঘি', 'সাইকাস সারসিনালিস', 'জিংগো']
        },
        "correct": 0,
        "expl_en": 'Chilgoza nuts are the roasted seeds of Pinus gerardiana (the Chilgoza pine), native to northwestern Himalayas.',
        "expl_bn": 'চিলগোজা হলো পাইনাস জেরার্ডিয়ানা (Pinus gerardiana) নামক ব্যক্তবীজী বৃক্ষের পুষ্টিকর ভক্ষণযোগ্য বীজ।',
    },
    {
        "id": 'BIO-PK-096',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In Chara, the multicellular jacketed female sex organ (Nucule) and male sex organ (Globule) are located:',
        "bn": 'সবুজ শৈবাল কারায় (Chara) বহুকোষী স্ত্রী জননাঙ্গ (নাকিউল বা Nucule) এবং পুং জননাঙ্গ (গ্লোবিউল বা Globule) কীভাবে অবস্থিত?',
        "opts": {
            "en": ['Nucule is situated UPPER (above) and Globule is situated LOWER (below) on the same node', 'Globule is situated above and Nucule is situated below', 'Both are inside antheridial crypts', 'Nucule on leaf tips and Globule on roots'],
            "bn": ['নাকিউল (স্ত্রী অঙ্গ) উপরে এবং গ্লোবিউল (পুং অঙ্গ) নিচে একই পর্বের ওপর অবস্থিত', 'গ্লোবিউল উপরে এবং নাকিউল নিচে অবস্থিত', 'উভয়ই ক্রিপ্টের মধ্যে লুকানো', 'নাকিউল পাতার শীর্ষে এবং গ্লোবিউল মূলে']
        },
        "correct": 0,
        "expl_en": 'In the green alga Chara, the female oogonium (nucule) is oval and located above the spherical male antheridium (globule) on the nodes of short branches.',
        "expl_bn": 'কারা (Chara)-র ক্ষেত্রে স্ত্রী জননাঙ্গ নাকিউল (Nucule) উপরের দিকে এবং পুং জননাঙ্গ গ্লোবিউল (Globule) নিচের দিকে একই পর্বে অবস্থান করে।',
    },
    {
        "id": 'BIO-PK-097',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Which part of the moss capsule is responsible for releasing spores under dry conditions by hygroscopic movement?',
        "bn": 'মসের ক্যাপসুলের কোন অংশটি শুষ্ক অবস্থায় হাইগ্রোস্কোপিক চলনের মাধ্যমে রেণু মুক্ত করতে সাহায্য করে?',
        "opts": {
            "en": ['Peristome teeth', 'Operculum lid', 'Columella', 'Apophysis'],
            "bn": ['পেরিস্টোম দাঁত (Peristome teeth)', 'অপারকুলাম ঢাকনা', 'কলুমেলা', 'অ্যাপোফাইসিস']
        },
        "correct": 0,
        "expl_en": 'The peristome teeth (typically 16 + 16 in two rings in Funaria) exhibit hygroscopic movements, bending outward when dry to disperse spores into the wind.',
        "expl_bn": 'মসের ক্যাপসুলের মুখে থাকা হাইগ্রোস্কোপিক পেরিস্টোম দাঁত বাতাসে আর্দ্রতার পরিবর্তনে বেঁকে গিয়ে রেণু বিচ্ছুরণে সাহায্য করে।',
    },
    {
        "id": 'BIO-PK-098',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In fern sporangia, the row of specialized thick-walled cells that rupture the stomium to eject spores is called the:',
        "bn": 'ফার্নের স্পোরাঞ্জিয়ামে বিশেষ পুরু প্রাচীরযুক্ত যে কোষগুলির বলয় স্টোমিয়ামকে ফাটিয়ে স্পোর নিক্ষেপ করে তাকে কী বলে?',
        "opts": {
            "en": ['Annulus', 'Indusium', 'Tapetum', 'Ramenta'],
            "bn": ['অ্যানুলাস (Annulus)', 'ইন্ডুসিয়াম', 'ট্যাপিটাম', 'রামেন্তা']
        },
        "correct": 0,
        "expl_en": 'The annulus is a specialized ring of differentially thickened cells in the leptosporangiate fern sporangium that creates mechanical tension as it dries, catapulting spores outward.',
        "expl_bn": 'ফার্নের স্পোরাঞ্জিয়ামের অ্যানুলাস (Annulus) নামক বিশেষ কোষবলয় শুষ্ক অবস্থায় কুঁচকে গিয়ে স্টোমিয়ামকে ফাটিয়ে ক্যাটাপল্টের ন্যায় স্পোর বাইরে ছড়িয়ে দেয়।',
    },
    {
        "id": 'BIO-PK-099',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Brown hair-like scales covering the rhizome and petiole bases of young fern fronds for protection are called:',
        "bn": 'ফার্নের রাইজোম ও তরুণ পাতার বোঁটাকে ঢেকে রাখা বাদামী চুলের মতো সুরক্ষাকারী আঁশকে কী বলে?',
        "opts": {
            "en": ['Ramenta', 'Circinate vernation', 'Scale leaves', 'Bracteoles'],
            "bn": ['রামেন্তা (Ramenta)', 'সারসিনেট ভারনেশন', 'শল্কপত্র', 'ব্র্যাক্টিওল']
        },
        "correct": 0,
        "expl_en": 'Ramenta are chaffy, multicellular, dry brownish scales that cover and protect the young circinate fronds and rhizome in ferns.',
        "expl_bn": 'ফার্নের মুকুল ও রাইজোমকে আবৃতকারী বাদামী রঙের বহুকোষী শল্কের মতো রোমগুলিকে রামেন্তা (Ramenta) বলা হয়।',
    },
    {
        "id": 'BIO-PK-100',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'The coiled, spring-like arrangement of young leaves in ferns and Cycas before unfolding is termed:',
        "bn": 'ফার্ন এবং সাইকাসের কচি পাতার স্প্রিং-এর মতো কুন্ডলীকৃত বিন্যাসকে কী বলা হয়?',
        "opts": {
            "en": ['Circinate vernation', 'Ptyxis', 'Phyllotaxy', 'Aestivation'],
            "bn": ['সারসিনেট ভারনেশন (Circinate vernation)', 'টাইক্সিস', 'ফাইলোট্যাক্সি', 'এস্টিভেশন']
        },
        "correct": 0,
        "expl_en": 'Circinate vernation is the characteristic coiling of young fronds like a watch spring to protect the delicate growing tip, found in both ferns and cycads.',
        "expl_bn": 'ফার্ন ও সাইকাসের কচি পাতা ঘড়ির স্প্রিং-এর মতো গুটিয়ে থাকে। পাতার এই বৈশিষ্ট্যকে সারসিনেট ভারনেশন (Circinate vernation) বলে।',
    },
    {
        "id": 'BIO-PK-101',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Which of the following gymnosperms has the largest ovule, largest male cone, and largest sperm in the entire plant kingdom?',
        "bn": 'সমগ্র উদ্ভিদজগতের মধ্যে কোন ব্যক্তবীজী উদ্ভিদে বৃহত্তম ডিম্বক, বৃহত্তম পুং শঙ্কু এবং বৃহত্তম সচল শুক্রাণু দেখা যায়?',
        "opts": {
            "en": ['Cycas', 'Pinus', 'Ginkgo', 'Sequoia'],
            "bn": ['সাইকাস (Cycas)', 'পাইনাস', 'জিংগো', 'সেকোয়া']
        },
        "correct": 0,
        "expl_en": 'Cycas possesses the largest ovules (up to 6-7 cm), largest male cones (up to 50 cm), and largest top-shaped multiflagellated sperms visible to the naked eye.',
        "expl_bn": 'উদ্ভিদজগতের সর্ববৃহৎ ডিম্বক, সর্ববৃহৎ পুং শঙ্কু এবং খালি চোখে দৃশ্যমান সর্ববৃহৎ শুক্রাণু সাইকাসে (Cycas) দেখা যায়।',
    },
    {
        "id": 'BIO-PK-102',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Pollen grains of Pinus possess two lateral air sacs or wings (winged pollen). These wings are formed by the expansion of:',
        "bn": 'পাইনাসের পরাগরেণুতে দুটি পার্শ্বীয় ডানা (উইংড পোলেন) থাকে। এই ডানাগুলি কার প্রসারণের ফলে গঠিত হয়?',
        "opts": {
            "en": ['Exine layer', 'Intine layer', 'Tapetal fluid', 'Endothecium'],
            "bn": ['রেণুবহিস্ত্বক বা এক্সাইন (Exine)', 'রেণুঅন্তস্ত্বক বা ইনটাইন', 'ট্যাপিটাল তরল', 'এন্ডোথেসিয়াম']
        },
        "correct": 0,
        "expl_en": 'The yellow winged pollen grains of Pinus have two lateral air bladders formed by the ballooning or separation of the outer exine layer, facilitating anemophilous dispersal.',
        "expl_bn": 'পাইনাসের পরাগরেণুর ডানা দুটি এক্সাইন (exine) বা বহিঃত্বক প্রসারিত হয়ে বেলুনের মতো স্ফীত হয়ে তৈরি হয় যা বায়ুতে ভেসে থাকতে সাহায্য করে।',
    },
    {
        "id": 'BIO-PK-103',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": "The phenomenon of 'Sulphur shower' in pine forests refers to:",
        "bn": "পাইন বনে 'সালফার শাওয়ার' (Sulphur shower) বলতে কোন ঘটনাকে বোঝায়?",
        "opts": {
            "en": ['Massive cloud-like release of millions of yellow winged pollen grains in spring', 'Volcanic sulphur dioxide rain over pine needles', 'Secretion of yellow toxic resin from pine bark', 'Yellow rust disease caused by Puccinia'],
            "bn": ['বসন্তকালে কোটি কোটি হলুদ বর্ণের পক্ষল পরাগরেণুর মেঘের মতো বাতাসে উড়ে ঝরে পড়া', 'পাইন বনের ওপর আগ্নেয়গিরির সালফার বৃষ্টি', 'পাইন গাছের বাকল থেকে হলুদ বিষাক্ত রজন ক্ষরণ', 'পাকসিনিয়া ঘটিত হলুদ মরচে রোগ']
        },
        "correct": 0,
        "expl_en": "In spring, mature male cones of Pinus shed astronomical numbers of yellow winged pollen grains, forming yellow clouds in the atmosphere called the 'sulphur shower'.",
        "expl_bn": "বসন্তকালে পাইন গাছের পুং শঙ্কু থেকে কোটি কোটি হলুদ পরাগরেণু একসাথে মুক্ত হয়ে চারপাশের বাতাস হলুদ ধোঁয়ার মতো ঢেকে ফেলে, একে 'সালফার শাওয়ার' বলে।",
    },
    {
        "id": 'BIO-PK-104',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Turpentine and rosin are commercially distilled from the oleoresin of:',
        "bn": 'বাণিজ্যিকভাবে বহুল ব্যবহৃত টারপেনটাইন তেল এবং রজন কার তৈলাক্ত রেজিন থেকে পাতন করা হয়?',
        "opts": {
            "en": ['Pinus species', 'Cycas revoluta', 'Cedrus deodara', 'Taxus baccata'],
            "bn": ['পাইনাস (Pinus) প্রজাতির কাষ্ঠল কনিফার', 'সাইকাস', 'সিড্রাস', 'ট্যাক্সাস']
        },
        "correct": 0,
        "expl_en": 'Turpentine oil and rosin are obtained by steam distilling the crude oleoresin tapped from Pinus (such as Pinus roxburghii).',
        "expl_bn": 'পাইনাস গাছের কাণ্ড থেকে সংগৃহীত রজন পাতন করে টারপেনটাইন তেল ও রোসিন পাওয়া যায়।',
    },
    {
        "id": 'BIO-PK-105',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Which anticancer alkaloid is extracted from the bark of the Pacific Yew tree (Taxus brevifolia)?',
        "bn": 'ট্যাক্সাস (Taxus brevifolia) নামক ব্যক্তবীজী বৃক্ষের ছাল থেকে কোন বিখ্যাত ক্যানসার-প্রতিরোধী অ্যালকালয়েড প্রস্তুত করা হয়?',
        "opts": {
            "en": ['Taxol (Paclitaxel)', 'Vincristine', 'Colchicine', 'Morphine'],
            "bn": ['ট্যাক্সল বা প্যাক্লিট্যাক্সেল (Taxol)', 'ভিনক্রিস্টিন', 'কলচিসিন', 'মরফিন']
        },
        "correct": 0,
        "expl_en": 'Taxol (paclitaxel) is a vital anti-neoplastic drug that blocks tubulin depolymerization during mitosis, isolated from Taxus brevifolia (gymnosperm).',
        "expl_bn": 'ট্যাক্সাস গাছের বাকল থেকে ট্যাক্সল (Taxol) নামক জীবনদায়ী ক্যানসার প্রতিরোধী ওষুধ পাওয়া যায় যা কোষ বিভাজনে মাইক্রোটিউবিউল ভেঙে যাওয়া রোধ করে।',
    },
    {
        "id": 'BIO-PK-106',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Examine the given diagram representing Marchantia thalli:<br><svg viewBox="0 0 520 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Female Thallus (Archegoniophore with finger-like rays) -->\n  <g transform="translate(30, 20)">\n    <!-- Thallus -->\n    <path d="M 40 180 Q 20 150 50 130 Q 70 110 110 130 Q 150 110 170 140 Q 190 170 150 190 Q 90 200 40 180 Z" fill="#86efac" stroke="#15803d" stroke-width="2"/>\n    <!-- Midrib -->\n    <path d="M 50 180 Q 100 150 140 140" fill="none" stroke="#166534" stroke-width="2" stroke-dasharray="3,2"/>\n    <!-- Gemma Cup (A) -->\n    <ellipse cx="100" cy="145" rx="14" ry="8" fill="#4ade80" stroke="#14532d" stroke-width="1.5"/>\n    <text x="100" y="148" fill="#052e16" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">A</text>\n    <!-- Archegoniophore stalk and umbrella head (B) -->\n    <path d="M 110 130 L 110 60" fill="none" stroke="#15803d" stroke-width="3"/>\n    <!-- Umbrella with rays -->\n    <path d="M 80 60 Q 110 40 140 60 L 145 75 L 135 65 L 125 75 L 115 65 L 105 75 L 95 65 L 85 75 Z" fill="#22c55e" stroke="#14532d" stroke-width="1.5"/>\n    <text x="110" y="35" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">B (Archegoniophore)</text>\n    <!-- Rhizoids -->\n    <path d="M 60 190 L 50 210 M 80 195 L 75 215 M 120 195 L 125 215" stroke="#a16207" stroke-width="1.5"/>\n    <text x="110" y="210" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Female Thallus</text>\n  </g>\n\n  <!-- Male Thallus (Antheridiophore with scalloped disc) -->\n  <g transform="translate(290, 20)">\n    <!-- Thallus -->\n    <path d="M 40 180 Q 20 150 50 130 Q 70 110 110 130 Q 150 110 170 140 Q 190 170 150 190 Q 90 200 40 180 Z" fill="#86efac" stroke="#15803d" stroke-width="2"/>\n    <!-- Midrib -->\n    <path d="M 50 180 Q 100 150 140 140" fill="none" stroke="#166534" stroke-width="2" stroke-dasharray="3,2"/>\n    <!-- Gemma Cup -->\n    <ellipse cx="100" cy="145" rx="14" ry="8" fill="#4ade80" stroke="#14532d" stroke-width="1.5"/>\n    <!-- Antheridiophore stalk and peltate disc (C) -->\n    <path d="M 110 130 L 110 60" fill="none" stroke="#15803d" stroke-width="3"/>\n    <!-- Scalloped disc -->\n    <ellipse cx="110" cy="60" rx="28" ry="10" fill="#16a34a" stroke="#14532d" stroke-width="1.5"/>\n    <text x="110" y="35" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">C (Antheridiophore)</text>\n    <!-- Rhizoids -->\n    <path d="M 60 190 L 50 210 M 80 195 L 75 215 M 120 195 L 125 215" stroke="#a16207" stroke-width="1.5"/>\n    <text x="110" y="210" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Male Thallus</text>\n  </g>\n</svg><br>Identify parts labeled A, B, and C:',
        "bn": 'মারকানশিয়া থ্যালাসের প্রদত্ত চিত্রটি লক্ষ্য করো:<br><svg viewBox="0 0 520 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Female Thallus (Archegoniophore with finger-like rays) -->\n  <g transform="translate(30, 20)">\n    <!-- Thallus -->\n    <path d="M 40 180 Q 20 150 50 130 Q 70 110 110 130 Q 150 110 170 140 Q 190 170 150 190 Q 90 200 40 180 Z" fill="#86efac" stroke="#15803d" stroke-width="2"/>\n    <!-- Midrib -->\n    <path d="M 50 180 Q 100 150 140 140" fill="none" stroke="#166534" stroke-width="2" stroke-dasharray="3,2"/>\n    <!-- Gemma Cup (A) -->\n    <ellipse cx="100" cy="145" rx="14" ry="8" fill="#4ade80" stroke="#14532d" stroke-width="1.5"/>\n    <text x="100" y="148" fill="#052e16" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">A</text>\n    <!-- Archegoniophore stalk and umbrella head (B) -->\n    <path d="M 110 130 L 110 60" fill="none" stroke="#15803d" stroke-width="3"/>\n    <!-- Umbrella with rays -->\n    <path d="M 80 60 Q 110 40 140 60 L 145 75 L 135 65 L 125 75 L 115 65 L 105 75 L 95 65 L 85 75 Z" fill="#22c55e" stroke="#14532d" stroke-width="1.5"/>\n    <text x="110" y="35" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">B (Archegoniophore)</text>\n    <!-- Rhizoids -->\n    <path d="M 60 190 L 50 210 M 80 195 L 75 215 M 120 195 L 125 215" stroke="#a16207" stroke-width="1.5"/>\n    <text x="110" y="210" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Female Thallus</text>\n  </g>\n\n  <!-- Male Thallus (Antheridiophore with scalloped disc) -->\n  <g transform="translate(290, 20)">\n    <!-- Thallus -->\n    <path d="M 40 180 Q 20 150 50 130 Q 70 110 110 130 Q 150 110 170 140 Q 190 170 150 190 Q 90 200 40 180 Z" fill="#86efac" stroke="#15803d" stroke-width="2"/>\n    <!-- Midrib -->\n    <path d="M 50 180 Q 100 150 140 140" fill="none" stroke="#166534" stroke-width="2" stroke-dasharray="3,2"/>\n    <!-- Gemma Cup -->\n    <ellipse cx="100" cy="145" rx="14" ry="8" fill="#4ade80" stroke="#14532d" stroke-width="1.5"/>\n    <!-- Antheridiophore stalk and peltate disc (C) -->\n    <path d="M 110 130 L 110 60" fill="none" stroke="#15803d" stroke-width="3"/>\n    <!-- Scalloped disc -->\n    <ellipse cx="110" cy="60" rx="28" ry="10" fill="#16a34a" stroke="#14532d" stroke-width="1.5"/>\n    <text x="110" y="35" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">C (Antheridiophore)</text>\n    <!-- Rhizoids -->\n    <path d="M 60 190 L 50 210 M 80 195 L 75 215 M 120 195 L 125 215" stroke="#a16207" stroke-width="1.5"/>\n    <text x="110" y="210" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Male Thallus</text>\n  </g>\n</svg><br>A, B এবং C চিহ্নিত অংশগুলি সঠিকভাবে শনাক্ত করো:',
        "opts": {
            "en": ['A = Gemma cup; B = Archegoniophore (female); C = Antheridiophore (male)', 'A = Antheridiophore; B = Gemma cup; C = Archegoniophore', 'A = Capsule; B = Seta; C = Foot', 'A = Strobili; B = Sporophyll; C = Microphyll'],
            "bn": ['A = গেমা কাপ (Gemma cup); B = আর্কেগোনিওফোর (স্ত্রী); C = অ্যান্থেরিডিওফোর (পুং)', 'A = অ্যান্থেরিডিওফোর; B = গেমা কাপ; C = আর্কেগোনিওফোর', 'A = ক্যাপসুল; B = সিটা; C = ফুট', 'A = স্ট্রোবিলাস; B = স্পোরোফিল; C = মাইক্রোফিল']
        },
        "correct": 0,
        "expl_en": 'In Marchantia: A is the gemma cup containing vegetative green multicellular gemmae. B is the umbrella-like female archegoniophore bearing archegonia under its rays. C is the flattened male antheridiophore bearing antheridia.',
        "expl_bn": 'মারকানশিয়াতে: A হলো গেমা কাপ (অঙ্গজ জননকারী পেয়ালা); B হলো ছাতার মতো রশ্মিযুক্ত আর্কেগোনিওফোর (স্ত্রী জনন অঙ্গ ধারক); C হলো লোবযুক্ত অ্যান্থেরিডিওফোর (পুং জনন অঙ্গ ধারক)।',
    },
    {
        "id": 'BIO-PK-107',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Examine the diagrams of the three plant life cycles below:<br><svg viewBox="0 0 540 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Cycle A: Haplontic -->\n  <g transform="translate(10, 10)">\n    <rect x="10" y="10" width="150" height="150" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>\n    <text x="85" y="30" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Haplontic (A)</text>\n    <path d="M 40 90 A 45 45 0 1 1 130 90" fill="none" stroke="#16a34a" stroke-width="4"/>\n    <path d="M 130 90 A 45 45 0 0 1 40 90" fill="none" stroke="#dc2626" stroke-width="4"/>\n    <text x="85" y="70" fill="#15803d" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">Gametophyte (n)</text>\n    <text x="85" y="125" fill="#b91c1c" font-size="9" font-family="system-ui" text-anchor="middle">Zygote (2n) only</text>\n    <text x="85" y="150" fill="#047857" font-size="9" font-family="system-ui" text-anchor="middle">Volvox, Spirogyra</text>\n  </g>\n\n  <!-- Cycle B: Diplontic -->\n  <g transform="translate(185, 10)">\n    <rect x="10" y="10" width="150" height="150" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>\n    <text x="85" y="30" fill="#b91c1c" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Diplontic (B)</text>\n    <path d="M 40 90 A 45 45 0 1 1 130 90" fill="none" stroke="#dc2626" stroke-width="4"/>\n    <path d="M 130 90 A 45 45 0 0 1 40 90" fill="none" stroke="#16a34a" stroke-width="4"/>\n    <text x="85" y="70" fill="#b91c1c" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">Sporophyte (2n)</text>\n    <text x="85" y="125" fill="#15803d" font-size="9" font-family="system-ui" text-anchor="middle">Gametes (n) only</text>\n    <text x="85" y="150" fill="#991b1b" font-size="9" font-family="system-ui" text-anchor="middle">Gymno, Angio, Fucus</text>\n  </g>\n\n  <!-- Cycle C: Haplodiplontic -->\n  <g transform="translate(360, 10)">\n    <rect x="10" y="10" width="165" height="150" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>\n    <text x="92" y="30" fill="#1d4ed8" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Haplodiplontic (C)</text>\n    <path d="M 47 90 A 45 45 0 1 1 137 90" fill="none" stroke="#16a34a" stroke-width="4"/>\n    <path d="M 137 90 A 45 45 0 0 1 47 90" fill="none" stroke="#dc2626" stroke-width="4"/>\n    <text x="92" y="65" fill="#15803d" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Gametophyte (n)</text>\n    <text x="92" y="125" fill="#b91c1c" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Sporophyte (2n)</text>\n    <text x="92" y="150" fill="#1e40af" font-size="8.5" font-family="system-ui" text-anchor="middle">Bryo, Pterido, Kelps</text>\n  </g>\n</svg><br>Which of the following correctly pairs the life cycle type with its representative organisms?',
        "bn": 'উদ্ভিদের তিনটি প্রধান জীবনচক্রের প্রদত্ত রেখাচিত্রগুলি লক্ষ্য করো:<br><svg viewBox="0 0 540 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Cycle A: Haplontic -->\n  <g transform="translate(10, 10)">\n    <rect x="10" y="10" width="150" height="150" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>\n    <text x="85" y="30" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Haplontic (A)</text>\n    <path d="M 40 90 A 45 45 0 1 1 130 90" fill="none" stroke="#16a34a" stroke-width="4"/>\n    <path d="M 130 90 A 45 45 0 0 1 40 90" fill="none" stroke="#dc2626" stroke-width="4"/>\n    <text x="85" y="70" fill="#15803d" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">Gametophyte (n)</text>\n    <text x="85" y="125" fill="#b91c1c" font-size="9" font-family="system-ui" text-anchor="middle">Zygote (2n) only</text>\n    <text x="85" y="150" fill="#047857" font-size="9" font-family="system-ui" text-anchor="middle">Volvox, Spirogyra</text>\n  </g>\n\n  <!-- Cycle B: Diplontic -->\n  <g transform="translate(185, 10)">\n    <rect x="10" y="10" width="150" height="150" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>\n    <text x="85" y="30" fill="#b91c1c" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Diplontic (B)</text>\n    <path d="M 40 90 A 45 45 0 1 1 130 90" fill="none" stroke="#dc2626" stroke-width="4"/>\n    <path d="M 130 90 A 45 45 0 0 1 40 90" fill="none" stroke="#16a34a" stroke-width="4"/>\n    <text x="85" y="70" fill="#b91c1c" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">Sporophyte (2n)</text>\n    <text x="85" y="125" fill="#15803d" font-size="9" font-family="system-ui" text-anchor="middle">Gametes (n) only</text>\n    <text x="85" y="150" fill="#991b1b" font-size="9" font-family="system-ui" text-anchor="middle">Gymno, Angio, Fucus</text>\n  </g>\n\n  <!-- Cycle C: Haplodiplontic -->\n  <g transform="translate(360, 10)">\n    <rect x="10" y="10" width="165" height="150" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>\n    <text x="92" y="30" fill="#1d4ed8" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Haplodiplontic (C)</text>\n    <path d="M 47 90 A 45 45 0 1 1 137 90" fill="none" stroke="#16a34a" stroke-width="4"/>\n    <path d="M 137 90 A 45 45 0 0 1 47 90" fill="none" stroke="#dc2626" stroke-width="4"/>\n    <text x="92" y="65" fill="#15803d" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Gametophyte (n)</text>\n    <text x="92" y="125" fill="#b91c1c" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Sporophyte (2n)</text>\n    <text x="92" y="150" fill="#1e40af" font-size="8.5" font-family="system-ui" text-anchor="middle">Bryo, Pterido, Kelps</text>\n  </g>\n</svg><br>নিচের কোন বিকল্পটিতে জীবনচক্র ও তাদের প্রতিনিধি জীবকে সঠিকভাবে মেলানো হয়েছে?',
        "opts": {
            "en": ['A = Haplontic (Volvox, Spirogyra); B = Diplontic (Gymnosperms, Angiosperms, Fucus); C = Haplodiplontic (Bryophytes, Pteridophytes, Kelps)', 'A = Diplontic (Kelps); B = Haplontic (Fucus); C = Haplodiplontic (Volvox)', 'A = Haplodiplontic; B = Diplontic; C = Haplontic', 'A = Haplontic (Gymnosperms); B = Diplontic (Spirogyra); C = Haplodiplontic (Angiosperms)'],
            "bn": ['A = হ্যাপ্লন্টিক (ভলভক্স, স্পাইরোগাইরা); B = ডিপ্লন্টিক (ব্যক্তবীজী, গুপ্তবীজী, ফিউকাস); C = হ্যাপ্লোডিপ্লন্টিক (ব্রায়োফাইটা, টেরিডোফাইটা, কেল্প)', 'A = ডিপ্লন্টিক (কেল্প); B = হ্যাপ্লন্টিক (ফিউকাস); C = হ্যাপ্লোডিপ্লন্টিক (ভলভক্স)', 'A = হ্যাপ্লোডিপ্লন্টিক; B = ডিপ্লন্টিক; C = হ্যাপ্লন্টিক', 'A = হ্যাপ্লন্টিক (ব্যক্তবীজী); B = ডিপ্লন্টিক (স্পাইরোগাইরা); C = হ্যাপ্লোডিপ্লন্টিক (গুপ্তবীজী)']
        },
        "correct": 0,
        "expl_en": 'Cycle A is Haplontic (Volvox, Spirogyra, Chlamydomonas). Cycle B is Diplontic (all seed plants and the brown alga Fucus). Cycle C is Haplodiplontic (Bryophytes, Pteridophytes, Ectocarpus, Polysiphonia, Kelps).',
        "expl_bn": 'A হলো হ্যাপ্লন্টিক (ভলভক্স, স্পাইরোগাইরা); B হলো ডিপ্লন্টিক (ব্যক্তবীজী, গুপ্তবীজী ও শৈবাল ফিউকাস); C হলো হ্যাপ্লোডিপ্লন্টিক (ব্রায়োফাইট, টেরিডোফাইট, এক্টোকার্পাস ও কেল্প)।',
    },
    {
        "id": 'BIO-PK-108',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Examine the structure of the fern prothallus:<br><svg viewBox="0 0 320 230" width="100%" height="230" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Heart-shaped prothallus -->\n  <path d="M 160 50 C 130 10 70 20 60 70 C 50 120 110 180 160 210 C 210 180 270 120 260 70 C 250 20 190 10 160 50 Z" fill="#bbf7d0" stroke="#16a34a" stroke-width="2.5"/>\n  <!-- Apical notch (A) -->\n  <circle cx="160" cy="50" r="4" fill="#15803d"/>\n  <line x1="160" y1="50" x2="160" y2="20" stroke="#15803d" stroke-width="1.5"/>\n  <text x="160" y="15" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">A (Apical Notch)</text>\n  <!-- Archegonia near notch (B) -->\n  <g fill="#ec4899" stroke="#be185d" stroke-width="1">\n    <circle cx="150" cy="80" r="4"/>\n    <circle cx="160" cy="75" r="4"/>\n    <circle cx="170" cy="80" r="4"/>\n    <circle cx="155" cy="92" r="4"/>\n    <circle cx="165" cy="92" r="4"/>\n  </g>\n  <line x1="170" y1="80" x2="225" y2="80" stroke="#be185d" stroke-width="1.5"/>\n  <text x="230" y="84" fill="#9d174d" font-size="10" font-weight="bold" font-family="system-ui">B (Archegonia)</text>\n  <!-- Antheridia among rhizoids (C) -->\n  <g fill="#0284c7" stroke="#0369a1" stroke-width="1">\n    <circle cx="140" cy="140" r="3.5"/>\n    <circle cx="175" cy="145" r="3.5"/>\n    <circle cx="150" cy="160" r="3.5"/>\n    <circle cx="168" cy="165" r="3.5"/>\n  </g>\n  <line x1="135" y1="140" x2="80" y2="140" stroke="#0369a1" stroke-width="1.5"/>\n  <text x="75" y="144" fill="#0369a1" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="end">C (Antheridia)</text>\n  <!-- Rhizoids at base (D) -->\n  <path d="M 155 180 L 140 215 M 160 190 L 160 225 M 165 185 L 180 220 M 150 170 L 130 200" stroke="#a16207" stroke-width="1.5"/>\n  <text x="160" y="225" fill="#78350f" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">D (Rhizoids)</text>\n</svg><br>Identify the labeled regions A, B, C, and D:',
        "bn": 'ফার্নের প্রোথ্যালাসের প্রদত্ত চিত্রটি পরীক্ষা করো:<br><svg viewBox="0 0 320 230" width="100%" height="230" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Heart-shaped prothallus -->\n  <path d="M 160 50 C 130 10 70 20 60 70 C 50 120 110 180 160 210 C 210 180 270 120 260 70 C 250 20 190 10 160 50 Z" fill="#bbf7d0" stroke="#16a34a" stroke-width="2.5"/>\n  <!-- Apical notch (A) -->\n  <circle cx="160" cy="50" r="4" fill="#15803d"/>\n  <line x1="160" y1="50" x2="160" y2="20" stroke="#15803d" stroke-width="1.5"/>\n  <text x="160" y="15" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">A (Apical Notch)</text>\n  <!-- Archegonia near notch (B) -->\n  <g fill="#ec4899" stroke="#be185d" stroke-width="1">\n    <circle cx="150" cy="80" r="4"/>\n    <circle cx="160" cy="75" r="4"/>\n    <circle cx="170" cy="80" r="4"/>\n    <circle cx="155" cy="92" r="4"/>\n    <circle cx="165" cy="92" r="4"/>\n  </g>\n  <line x1="170" y1="80" x2="225" y2="80" stroke="#be185d" stroke-width="1.5"/>\n  <text x="230" y="84" fill="#9d174d" font-size="10" font-weight="bold" font-family="system-ui">B (Archegonia)</text>\n  <!-- Antheridia among rhizoids (C) -->\n  <g fill="#0284c7" stroke="#0369a1" stroke-width="1">\n    <circle cx="140" cy="140" r="3.5"/>\n    <circle cx="175" cy="145" r="3.5"/>\n    <circle cx="150" cy="160" r="3.5"/>\n    <circle cx="168" cy="165" r="3.5"/>\n  </g>\n  <line x1="135" y1="140" x2="80" y2="140" stroke="#0369a1" stroke-width="1.5"/>\n  <text x="75" y="144" fill="#0369a1" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="end">C (Antheridia)</text>\n  <!-- Rhizoids at base (D) -->\n  <path d="M 155 180 L 140 215 M 160 190 L 160 225 M 165 185 L 180 220 M 150 170 L 130 200" stroke="#a16207" stroke-width="1.5"/>\n  <text x="160" y="225" fill="#78350f" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">D (Rhizoids)</text>\n</svg><br>A, B, C এবং D চিহ্নিত অংশগুলি শনাক্ত করো:',
        "opts": {
            "en": ['A = Apical notch; B = Archegonia; C = Antheridia; D = Rhizoids', 'A = Sorus; B = Antheridia; C = Archegonia; D = Roots', 'A = Protonema; B = Sporangium; C = Gemma cup; D = Stipe', 'A = Stoma; B = Endosperm; C = Pollen grain; D = Holdfast'],
            "bn": ['A = অগ্রস্থ খাঁজ (Apical notch); B = আর্কেগোনিয়া (স্ত্রী অঙ্গ); C = অ্যান্থেরিডিয়া (পুং অঙ্গ); D = রাইজয়েড (Rhizoids)', 'A = সোরাস; B = অ্যান্থেরিডিয়া; C = আর্কেগোনিয়া; D = মূল', 'A = প্রোটোনেমা; B = স্পোরাঞ্জিয়াম; C = গেমা কাপ; D = স্ট্রাইপ', 'A = পত্ররন্ধ্র; B = শস্য; C = পরাগরেণু; D = হোল্ডফাস্ট']
        },
        "correct": 0,
        "expl_en": 'The fern prothallus is a green, heart-shaped, monoecious gametophyte: A is the apical notch, B represents female archegonia near the notch, C represents male antheridia near the basal cushion, and D represents unicellular anchoring rhizoids.',
        "expl_bn": 'ফার্নের প্রোথ্যালাস হলো হৃদপিণ্ডাকার সহবাসী গ্যামেটোফাইট: A হলো অগ্রস্থ খাঁজ; B হলো খাঁজের কাছে অবস্থিত স্ত্রী অঙ্গ আর্কেগোনিয়া; C হলো নিচের দিকে অবস্থিত পুং অঙ্গ অ্যান্থেরিডিয়া; এবং D হলো সংলগ্নকারী রাইজয়েড।',
    },
    {
        "id": 'BIO-PK-109',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Bryophytes cannot grow to significant heights and remain restricted to low creeping or small upright cushions.<br>Reason (R): Bryophytes completely lack true vascular tissues (xylem vessels/tracheids and phloem) and true lignified mechanical tissues.',
        "bn": 'নিশ্চিত বিবৃতি (A): ব্রায়োফাইটা কখনোই অনেক উঁচুতে বাড়তে পারে না এবং এরা মাটির কাছাকাছি শায়িত বা ক্ষুদ্র গালিচার মতো থাকে।<br>যুক্তি (R): ব্রায়োফাইটাতে প্রকৃত সংবহন কলা (জাইলেম ভেসেল/ট্র্যাকিড ও ফ্লোয়েম) এবং লিগনিনযুক্ত যান্ত্রিক কলার সম্পূর্ণ অভাব থাকে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Without vascular bundles to transport water to great vertical heights and without lignified secondary xylem to provide mechanical support against gravity, bryophytes are biophysically constrained to low heights. (R) correctly explains (A).',
        "expl_bn": 'জাইলেম ও ফ্লোয়েম সংবহন কলা এবং যান্ত্রিক দৃঢ়তাদানকারী লিগনিনের অনুপস্থিতির কারণেই ব্রায়োফাইটা বেশি উঁচু হতে পারে না। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-PK-110',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Red algae (Rhodophyceae) can flourish at great depths in oceans where other algae cannot survive.<br>Reason (R): Red algae contain the accessory pigment r-phycoerythrin, which efficiently absorbs the high-energy, short-wavelength blue-green light that penetrates deep oceanic waters.',
        "bn": 'নিশ্চিত বিবৃতি (A): লাল শৈবাল (Rhodophyceae) সমুদ্রের গভীর তলদেশে বেঁচে থাকতে পারে যেখানে অন্য শৈবাল বাঁচতে পারে না।<br>যুক্তি (R): লাল শৈবালে r-ফাইকোইরিথ্রিন নামক আনুষঙ্গিক রঞ্জক থাকে যা গভীর সমুদ্রে প্রবেশকারী উচ্চ-শক্তি ও ক্ষুদ্র-তরঙ্গদৈর্ঘ্যবিশিষ্ট নীল-সবুজ আলোক তরঙ্গ কার্যকরভাবে শোষণ করতে পারে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Blue-green light possesses maximum penetrating power in clear oceanic water. r-phycoerythrin absorbs this blue-green light spectrum (around 495-570 nm) and transfers energy to chlorophyll a, enabling photosynthesis in the abyss. (R) correctly explains (A).',
        "expl_bn": 'সমুদ্রের গভীর জলে কেবল নীল-সবুজ আলোক তরঙ্গ প্রবেশ করতে পারে। লাল শৈবালের r-ফাইকোইরিথ্রিন এই তরঙ্গ শোষণ করে সালোকসংশ্লেষ চালাতে পারে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-PK-111',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Pinus seeds fail to germinate and establish seedlings in the absence of mycorrhizal fungal association.<br>Reason (R): Pinus roots have obligate mycorrhizal association because their roots lack root hairs and require fungal hyphae for adequate water and mineral absorption.',
        "bn": 'নিশ্চিত বিবৃতি (A): মাইকোরাইজাল ছত্রাকের অনুষঙ্গ ব্যতীত পাইনাস গাছের বীজ কখনোই অঙ্কুরিত হয়ে চারাগাছ গঠন করতে পারে না।<br>যুক্তি (R): পাইনাসের শিকড়ে মূলরোম থাকে না এবং পর্যাপ্ত জল ও খনিজ শোষণের জন্য ছত্রাকের হাইফির ওপর বাধ্যতামূলকভাবে নির্ভরশীল থাকে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Pinus has an obligate association with ectomycorrhizae. The fungal mantle and Hartig net substitute for the poorly developed root hairs, absorbing water and phosphorus indispensable for seedling growth. (R) correctly explains (A).',
        "expl_bn": 'পাইনাসের মূলরোমহীন মূল পর্যাপ্ত জল ও ফসফরাস শোষণ করতে পারে না। ছত্রাকের মাইকোরাইজাল হাইফি মূলরোমের বিকল্প হিসেবে কাজ করে, তাই মাইকোরাইজা ছাড়া বীজ অঙ্কুরিত হতে পারে না। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-PK-112',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Heterospory in pteridophytes like Selaginella and Salvinia is regarded as a critical precursor to the seed habit of higher plants.<br>Reason (R): In heterosporous pteridophytes, the megaspore develops into a female gametophyte that is retained and nourished on the parent sporophyte, with the embryo initiating development in situ.',
        "bn": 'নিশ্চিত বিবৃতি (A): সিলাজিনেলা ও সালভিনিয়ার মতো টেরিডোফাইটে হেটারোস্পোরির আবির্ভাবকে উচ্চতর উদ্ভিদের বীজ স্বভাবের (Seed habit) বিবর্তনের প্রধান পূর্বসূরি মনে করা হয়।<br>যুক্তি (R): হেটারোস্পোরাস উদ্ভিদে মেগাস্পোর মাতৃ স্পোরোফাইটের গায়ে সংলগ্ন থেকে স্ত্রী গ্যামেটোফাইট গঠন করে এবং সেখানেই জাইগোট থেকে প্রাথমিক ভ্রূণের বিকাশ ঘটে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'The retention of the female gametophyte on the parent sporophyte and the nutrition of the developing zygote within it are the exact biological hallmarks defining the transition towards seeds. (R) correctly explains (A).',
        "expl_bn": 'মাতৃ স্পোরোফাইটে স্ত্রী গ্যামেটোফাইটের ধারণ এবং তার ভেতরেই ভ্রূণের সুরক্ষিত বিকাশই হলো বীজের উৎপত্তির মূল পূর্বশর্ত। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-PK-113',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Gymnosperms do not produce fruits.<br>Reason (R): Gymnosperms lack an ovary; their ovules are completely naked on megasporophylls and cannot form an enclosing pericarp after fertilization.',
        "bn": 'নিশ্চিত বিবৃতি (A): ব্যক্তবীজী উদ্ভিদে কখনোই ফল গঠিত হয় না।<br>যুক্তি (R): ব্যক্তবীজী উদ্ভিদে কোনো ডিম্বাশয় থাকে না; এদের ডিম্বকগুলি মেগাস্পোরোফিলের ওপর সম্পূর্ণ অনাবৃত থাকে এবং নিষেকের পর কোনো ফলত্বক তৈরি করতে পারে না।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'A fruit is anatomically a ripened ovary enclosing seeds. Because gymnosperms lack ovaries, their fertilized ovules ripen into naked seeds without any pericarp (fruit wall). (R) correctly explains (A).',
        "expl_bn": 'ফল হলো পরিপক্ব ডিম্বাশয়। ব্যক্তবীজীতে ডিম্বাশয় না থাকায় কোনো ফল গঠিত হতে পারে না, বীজগুলি নগ্ন অবস্থায় থাকে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-PK-114',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): The endosperm of gymnosperms is haploid (n), while that of angiosperms is triploid (3n).<br>Reason (R): In gymnosperms, endosperm is formed before fertilization directly from the female gametophyte tissue; in angiosperms, it is formed after double fertilization through triple fusion.',
        "bn": 'নিশ্চিত বিবৃতি (A): ব্যক্তবীজী উদ্ভিদের এন্ডোস্পার্ম (শস্য) হ্যাপ্লয়েড (n), কিন্তু গুপ্তবীজী উদ্ভিদের এন্ডোস্পার্ম ট্রিপ্লয়েড (3n)।<br>যুক্তি (R): ব্যক্তবীজীতে শস্য নিষেকের পূর্বেই স্ত্রী গ্যামেটোফাইট কলা থেকে সরাসরি গঠিত হয়; কিন্তু গুপ্তবীজীতে এটি নিষেকের পরে ট্রিপল ফিউশনের মাধ্যমে গঠিত হয়।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Pre-fertilization development from the haploid megaspore makes the gymnospermic endosperm (n), whereas triple fusion of a haploid sperm with the diploid secondary nucleus makes the angiospermic endosperm (3n). (R) correctly explains (A).',
        "expl_bn": 'ব্যক্তবীজীর এন্ডোস্পার্ম নিষেকের পূর্বে গঠিত হ্যাপ্লয়েড স্ত্রী গ্যামেটোফাইট (n), কিন্তু গুপ্তবীজীতে একটি শুক্রাণু (n) ও দুটি পোলার নিউক্লিয়াস (2n)-এর মিলনে ট্রিপ্লয়েড (3n) শস্য গঠিত হয়। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-PK-115',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Mosses are ecologically more important than liverworts in controlling soil erosion.<br>Reason (R): Mosses form dense, impenetrable carpets on soil surfaces that cushion the mechanical impact of falling raindrops and bind topsoil particles.',
        "bn": 'নিশ্চিত বিবৃতি (A): ভূমিক্ষয় রোধে লিভারওয়ার্টের তুলনায় মস বাস্তুতান্ত্রিকভাবে অনেক বেশি গুরুত্বপূর্ণ।<br>যুক্তি (R): মস মাটির ওপর ঘন গালিচার মতো আস্তরণ তৈরি করে যা বৃষ্টির ফোঁটার সরাসরি আঘাত হ্রাস করে এবং মাটির কণাগুলিকে শক্তভাবে ধরে রাখে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Since mosses form dense mats on the soil, they reduce the impact of falling rain and prevent soil erosion. (R) accurately explains (A).',
        "expl_bn": 'মাটির ওপর মসের তৈরি ঘন গালিচা বৃষ্টির তীব্রতাকে প্রতিহত করে মাটির ক্ষয় রোধ করে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-PK-116',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Spirogyra shows isogamy with non-flagellated gametes.<br>Reason (R): The gametes of Spirogyra are structurally similar and non-motile, transferring via a conjugation tube by amoeboid creeping.',
        "bn": 'নিশ্চিত বিবৃতি (A): স্পাইরোগাইরায় ফ্ল্যাজেলাবিহীন গ্যামেটের সমন্বয়ে আইসোগ্যামি দেখা যায়।<br>যুক্তি (R): স্পাইরোগাইরার গ্যামেটগুলি গঠনে সমান এবং চলনহীন, যা সংশ্লেষ নালী (conjugation tube)-র মাধ্যমে অ্যামিবয়েড চলনে স্থানান্তরিত হয়।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Spirogyra undergoes scalariform or lateral conjugation where morphologically indistinguishable, non-flagellated protoplasts fuse, exemplifying non-motile isogamy. (R) correctly explains (A).',
        "expl_bn": 'স্পাইরোগাইরাতে গ্যামেটগুলি সমআকৃতির এবং ফ্ল্যাজেলাবিহীন; কনজুগেশন নালীর মাধ্যমে এদের মিলন ঘটে। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-PK-117',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Cycas is a dioecious gymnosperm.<br>Reason (R): Male cones and megasporophylls are produced on completely separate male and female plants of Cycas.',
        "bn": 'নিশ্চিত বিবৃতি (A): সাইকাস (Cycas) একটি ভিন্নবাসী (dioecious) ব্যক্তবীজী উদ্ভিদ।<br>যুক্তি (R): সাইকাসের পুং শঙ্কু এবং মেগাস্পোরোফিল দুটি সম্পূর্ণ পৃথক পুরুষ ও স্ত্রী গাছে উৎপন্ন হয়।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Dioecy means male and female reproductive structures are on separate individuals. In Cycas, male cones and megasporophylls occur on separate trees. (R) correctly explains (A).',
        "expl_bn": 'সাইকাসের পুরুষ ও স্ত্রী গাছ আলাদা হওয়ায় এটি ভিন্নবাসী (dioecious)। পুরুষ গাছে পুং শঙ্কু এবং স্ত্রী গাছে মেগাস্পোরোফিল জন্মায়। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-PK-118',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Statement I: In Chlorophyceae, the major photosynthetic pigments are Chlorophyll a and b, and the food is stored as starch.<br>Statement II: In Phaeophyceae, the major pigments are Chlorophyll a and c with fucoxanthin, and the food is stored as laminarin or mannitol.',
        "bn": 'বিবৃতি I: ক্লোরোফাইসিতে প্রধান সালোকসংশ্লেষী রঞ্জক হলো ক্লোরোফিল a ও b এবং সঞ্চিত খাদ্য হলো স্টার্চ।<br>বিবৃতি II: ফিওফাইসিতে প্রধান রঞ্জক হলো ক্লোরোফিল a ও c সহ ফিউকোজ্যান্থিন এবং সঞ্চিত খাদ্য হলো ল্যামিনারিন বা ম্যানিটল।',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক']
        },
        "correct": 0,
        "expl_en": 'Both statements are completely accurate according to NCERT Summary Table 3.1.',
        "expl_bn": 'NCERT সারণি ৩.১ অনুসারে উভয় বিবৃতিই সম্পূর্ণ সঠিক।',
    },
    {
        "id": 'BIO-PK-119',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Statement I: In Rhodophyceae, flagella are completely absent in both spores and gametes.<br>Statement II: In Phaeophyceae, zoospores have 2 laterally inserted unequal flagella, while in Chlorophyceae, zoospores have 2 to 8 apically inserted equal flagella.',
        "bn": 'বিবৃতি I: রোডোফাইসিতে স্পোর এবং গ্যামেট উভয়ের ক্ষেত্রেই ফ্ল্যাজেলা সম্পূর্ণ অনুপস্থিত থাকে।<br>বিবৃতি II: ফিওফাইসিতে জুস্পোরে ২টি পার্শ্বীয় অসমান ফ্ল্যাজেলা থাকে, কিন্তু ক্লোরোফাইসিতে জুস্পোরে ২ থেকে ৮টি অগ্রস্থ সমান দৈর্ঘ্যের ফ্ল্যাজেলা থাকে।',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক']
        },
        "correct": 0,
        "expl_en": 'Both statements are direct, unadulterated facts from NCERT Table 3.1 on algal divisions.',
        "expl_bn": 'উভয় বিবৃতিই শৈবালের তুলনামূলক সারণি অনুসারে সম্পূর্ণ সঠিক।',
    },
    {
        "id": 'BIO-PK-120',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Statement I: In mosses, the leafy stage bears sex organs at its apex and develops from the secondary protonema as a lateral bud.<br>Statement II: In liverworts, the sporophyte is completely independent and photosynthetic, while the gametophyte is parasitic on it.',
        "bn": 'বিবৃতি I: মসের ক্ষেত্রে পত্রল দশার শীর্ষে জননাঙ্গ গঠিত হয় এবং এটি গৌণ প্রোটোনেমা থেকে পার্শ্বীয় মুকুল হিসেবে জন্মায়।<br>বিবৃতি II: লিভারওয়ার্টে স্পোরোফাইট সম্পূর্ণ স্বাধীন ও সালোকসংশ্লেষকারী, আর গ্যামেটোফাইট তার ওপর পরজীবী হিসেবে থাকে।',
        "opts": {
            "en": ['Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct', 'Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect'],
            "bn": ['বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল']
        },
        "correct": 0,
        "expl_en": 'Statement I is correct. Statement II is completely inverted: in liverworts (and all bryophytes), the gametophyte is the dominant, photosynthetic, independent phase, while the sporophyte is physically attached and parasitic on the gametophyte.',
        "expl_bn": 'বিবৃতি I সঠিক। কিন্তু বিবৃতি II ভুল কারণ সমস্ত ব্রায়োফাইটে গ্যামেটোফাইট স্বাধীন এবং স্পোরোফাইট তার ওপর নির্ভরশীল।',
    },
    {
        "id": 'BIO-PK-121',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Statement I: Volvox, Spirogyra, and Chlamydomonas represent the haplontic life cycle pattern.<br>Statement II: Fucus, a brown alga, represents a diplontic life cycle pattern.',
        "bn": 'বিবৃতি I: ভলভক্স, স্পাইরোগাইরা এবং ক্ল্যামাইডোমোনাস হ্যাপ্লন্টিক জীবনচক্রের নিদর্শন।<br>বিবৃতি II: ফিউকাস নামক বাদামী শৈবালটি ডিপ্লন্টিক জীবনচক্রের নিদর্শন।',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক']
        },
        "correct": 0,
        "expl_en": "Both statements are correct verbatim from the 'Plant Life Cycles and Alternation of Generations' section of NCERT.",
        "expl_bn": 'NCERT-এর জীবনচক্র অধ্যায় অনুসারে দুটি বিবৃতিই সম্পূর্ণ নির্ভুল।',
    },
    {
        "id": 'BIO-PK-122',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Statement I: All pteridophytes are heterosporous without any exception.<br>Statement II: All gymnosperms are heterosporous without any exception.',
        "bn": 'বিবৃতি I: ব্যতিক্রমহীনভাবে সমস্ত টেরিডোফাইটই হেটারোস্পোরাস।<br>বিবৃতি II: ব্যতিক্রমহীনভাবে সমস্ত ব্যক্তবীজীই হেটারোস্পোরাস।',
        "opts": {
            "en": ['Statement I is incorrect but Statement II is correct', 'Statement I is correct but Statement II is incorrect', 'Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect'],
            "bn": ['বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল']
        },
        "correct": 0,
        "expl_en": 'Statement I is incorrect because the majority of pteridophytes are homosporous (e.g., Dryopteris, Pteris); only a few like Selaginella and Salvinia are heterosporous. Statement II is correct because all gymnosperms are strictly heterosporous.',
        "expl_bn": 'বিবৃতি I ভুল কারণ অধিকাংশ টেরিডোফাইটই হোমোস্পোরাস (যেমন ফার্ন)। কিন্তু বিবৃতি II সঠিক কারণ সমস্ত ব্যক্তবীজীই বাধ্যতামূলকভাবে হেটারোস্পোরাস।',
    },
    {
        "id": 'BIO-PK-123',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Match Column-I (Algal class) with Column-II (Stored food):<br>A. Chlorophyceae<br>B. Phaeophyceae<br>C. Rhodophyceae<br>D. Cyanophyceae<br>1. Floridean starch<br>2. Laminarin or Mannitol<br>3. True Starch<br>4. Cyanophycean starch',
        "bn": 'কলাম-I (শৈবাল শ্রেণি)-এর সাথে কলাম-II (সঞ্চিত খাদ্য) মেলাও:<br>A. ক্লোরোফাইসি<br>B. ফিওফাইসি<br>C. রোডোফাইসি<br>D. সায়ানোফাইসি<br>1. ফ্লোরিডিয়ান স্টার্চ<br>2. ল্যামিনারিন বা ম্যানিটল<br>3. সাধারণ স্টার্চ<br>4. সায়ানোফাইসিয়ান স্টার্চ',
        "opts": {
            "en": ['A-3, B-2, C-1, D-4', 'A-1, B-2, C-3, D-4', 'A-3, B-1, C-2, D-4', 'A-2, B-3, C-1, D-4'],
            "bn": ['A-3, B-2, C-1, D-4', 'A-1, B-2, C-3, D-4', 'A-3, B-1, C-2, D-4', 'A-2, B-3, C-1, D-4']
        },
        "correct": 0,
        "expl_en": 'Chlorophyceae = Starch (A-3); Phaeophyceae = Laminarin/mannitol (B-2); Rhodophyceae = Floridean starch (C-1); Cyanophyceae = Cyanophycean starch (D-4).',
        "expl_bn": 'ক্লোরোফাইসি = স্টার্চ (A-3); ফিওফাইসি = ল্যামিনারিন/ম্যানিটল (B-2); রোডোফাইসি = ফ্লোরিডিয়ান স্টার্চ (C-1); সায়ানোফাইসি = সায়ানোফাইসিয়ান স্টার্চ (D-4)।',
    },
    {
        "id": 'BIO-PK-124',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Match Column-I (Organisms) with Column-II (Characteristic Structure):<br>A. Sphagnum<br>B. Marchantia<br>C. Selaginella<br>D. Pinus<br>1. Winged pollen grain<br>2. Peat formation<br>3. Gemma cups<br>4. Heterospory and precursor to seed habit',
        "bn": 'কলাম-I (জীব)-এর সাথে কলাম-II (বৈশিষ্ট্য) মেলাও:<br>A. Sphagnum<br>B. Marchantia<br>C. Selaginella<br>D. Pinus<br>1. উইংড বা পক্ষল পরাগরেণু<br>2. পিট গঠন<br>3. গেমা কাপ<br>4. হেটারোস্পোরি ও বীজ স্বভাবের অগ্রদূত',
        "opts": {
            "en": ['A-2, B-3, C-4, D-1', 'A-3, B-2, C-4, D-1', 'A-2, B-4, C-3, D-1', 'A-1, B-3, C-4, D-2'],
            "bn": ['A-2, B-3, C-4, D-1', 'A-3, B-2, C-4, D-1', 'A-2, B-4, C-3, D-1', 'A-1, B-3, C-4, D-2']
        },
        "correct": 0,
        "expl_en": 'Sphagnum = Peat (A-2); Marchantia = Gemma cups (B-3); Selaginella = Heterospory (C-4); Pinus = Winged pollen (D-1).',
        "expl_bn": 'Sphagnum = পিট মস (A-2); Marchantia = গেমা কাপ (B-3); Selaginella = হেটারোস্পোরি (C-4); Pinus = পক্ষল পরাগরেণু (D-1)।',
    },
    {
        "id": 'BIO-PK-125',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Match Column-I (Pteridophyte class) with Column-II (Genus):<br>A. Psilopsida<br>B. Lycopsida<br>C. Sphenopsida<br>D. Pteropsida<br>1. Equisetum<br>2. Psilotum<br>3. Dryopteris, Pteris, Adiantum<br>4. Selaginella, Lycopodium',
        "bn": 'কলাম-I (টেরিডোফাইটা শ্রেণি)-এর সাথে কলাম-II (গণ) মেলাও:<br>A. সাইলোপসিডা<br>B. লাইকোপসিডা<br>C. স্ফেনোপসিডা<br>D. টেরোপসিডা<br>1. ইকুইসিটাম<br>2. সাইলোটাম<br>3. ড্রায়োপ্টেরিস, টেরিস, অ্যাডিয়েন্টাম<br>4. সিলাজিনেলা, লাইকোপোডিয়াম',
        "opts": {
            "en": ['A-2, B-4, C-1, D-3', 'A-1, B-4, C-2, D-3', 'A-2, B-1, C-4, D-3', 'A-4, B-2, C-1, D-3'],
            "bn": ['A-2, B-4, C-1, D-3', 'A-1, B-4, C-2, D-3', 'A-2, B-1, C-4, D-3', 'A-4, B-2, C-1, D-3']
        },
        "correct": 0,
        "expl_en": 'Psilopsida = Psilotum (A-2); Lycopsida = Selaginella (B-4); Sphenopsida = Equisetum (C-1); Pteropsida = Dryopteris/Pteris (D-3).',
        "expl_bn": 'Psilopsida = Psilotum (A-2); Lycopsida = Selaginella (B-4); Sphenopsida = Equisetum (C-1); Pteropsida = Dryopteris (D-3)।',
    },
    {
        "id": 'BIO-PK-126',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Match Column-I (Alga) with Column-II (Economic product / feature):<br>A. Gelidium<br>B. Chlorella<br>C. Laminaria<br>D. Porphyra<br>1. Space food supplement<br>2. Agar-agar<br>3. Edible marine alga<br>4. Iodine and algin source',
        "bn": 'কলাম-I (শৈবাল)-এর সাথে কলাম-II (অর্থনৈতিক গুরুত্ব) মেলাও:<br>A. Gelidium<br>B. Chlorella<br>C. Laminaria<br>D. Porphyra<br>1. মহাকাশ খাদ্য পরিপূরক<br>2. অ্যাগার-অ্যাগার<br>3. ভক্ষণযোগ্য সামুদ্রিক খাদ্য<br>4. আয়োডিন ও অ্যালজিন উৎস',
        "opts": {
            "en": ['A-2, B-1, C-4, D-3', 'A-1, B-2, C-4, D-3', 'A-2, B-4, C-1, D-3', 'A-3, B-1, C-4, D-2'],
            "bn": ['A-2, B-1, C-4, D-3', 'A-1, B-2, C-4, D-3', 'A-2, B-4, C-1, D-3', 'A-3, B-1, C-4, D-2']
        },
        "correct": 0,
        "expl_en": 'Gelidium = Agar (A-2); Chlorella = Space food (B-1); Laminaria = Iodine/algin (C-4); Porphyra = Edible alga eaten as nori (D-3).',
        "expl_bn": 'জেলিডিয়াম = অ্যাগার (A-2); ক্লোরেলা = মহাকাশ খাদ্য (B-1); ল্যামিনারিয়া = আয়োডিন/অ্যালজিন (C-4); পরফাইরা = ভোজ্য খাদ্য (D-3)।',
    },
    {
        "id": 'BIO-PK-127',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following is NOT an unbranched colonial green alga?',
        "bn": 'নিচের কোনটি অশাখ কলোনিয়াল সবুজ শৈবাল নয়?',
        "opts": {
            "en": ['Ectocarpus (branched filamentous brown alga)', 'Volvox', 'Pandorina', 'Eudorina'],
            "bn": ['এক্টোকার্পাস (শাখাযুক্ত সূত্রাকার বাদামী শৈবাল)', 'ভলভক্স', 'প্যান্ডোরিনা', 'ইউডোরিনা']
        },
        "correct": 0,
        "expl_en": 'Ectocarpus is a filamentous, branched brown alga (Phaeophyceae), not a green colonial alga.',
        "expl_bn": 'এক্টোকার্পাস হলো একটি শাখাযুক্ত সূত্রাকার বাদামী শৈবাল, কলোনিয়াল সবুজ শৈবাল নয়।',
    },
    {
        "id": 'BIO-PK-128',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Read the following statements regarding gymnosperms:<br>(i) Ovules are naked on megasporophylls.<br>(ii) Roots are generally taproots.<br>(iii) In Cycas, male and female cones are borne on the same tree.<br>(iv) In Pinus, stem is branched.<br>How many of the above statements are CORRECT?',
        "bn": 'ব্যক্তবীজী সংক্রান্ত নিচের বক্তব্যগুলি বিবেচনা করো:<br>(i) ডিম্বকগুলি মেগাস্পোরোফিলের ওপর অনাবৃত থাকে।<br>(ii) মূলগুলি প্রধানত স্থানিক প্রধান মূল (taproot)।<br>(iii) সাইকাসে পুং ও স্ত্রী শঙ্কু একই গাছে জন্মায়।<br>(iv) পাইনাসে কাণ্ড শাখাপ্রশাখা যুক্ত।<br>উপরের বিবৃতিগুলির মধ্যে কতগুলি সঠিক?',
        "opts": {
            "en": ['3 statements: (i), (ii), and (iv)', 'All 4 statements', 'Only 2 statements', 'Only 1 statement'],
            "bn": ['৩টি বিবৃতি: (i), (ii), এবং (iv)', 'সবকটি ৪টি বিবৃতি', 'কেবল ২টি বিবৃতি', 'কেবল ১টি বিবৃতি']
        },
        "correct": 0,
        "expl_en": 'Statement (iii) is FALSE because Cycas is dioecious (male cone and megasporophylls are on separate plants). Statements (i), (ii), and (iv) are true NCERT facts.',
        "expl_bn": 'বিবৃতি (iii) ভুল কারণ সাইকাস ভিন্নবাসী (dioecious)। বাকি (i), (ii) এবং (iv) সঠিক। তাই মোট ৩টি বিবৃতি সঠিক।',
    },
    {
        "id": 'BIO-PK-129',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'How many of the following plants possess vascular tissues (Xylem & Phloem)?<br>[Volvox, Marchantia, Sphagnum, Selaginella, Equisetum, Pinus, Wolffia, Polysiphonia]',
        "bn": 'প্রদত্ত উদ্ভিদগুলির মধ্যে কতগুলির দেহে সংবহন কলা (জাইলেম ও ফ্লোয়েম) বর্তমান?<br>[Volvox, Marchantia, Sphagnum, Selaginella, Equisetum, Pinus, Wolffia, Polysiphonia]',
        "opts": {
            "en": ['4 (Selaginella, Equisetum, Pinus, Wolffia)', '3', '5', '6'],
            "bn": ['৪টি (Selaginella, Equisetum, Pinus, Wolffia)', '৩টি', '৫টি', '৬টি']
        },
        "correct": 0,
        "expl_en": 'Vascular plants (Tracheophytes) start from Pteridophytes onwards: Selaginella (pteridophyte), Equisetum (pteridophyte), Pinus (gymnosperm), and Wolffia (angiosperm) = 4 plants. Volvox and Polysiphonia are non-vascular algae; Marchantia and Sphagnum are non-vascular bryophytes.',
        "expl_bn": 'সংবহনকলাযুক্ত উদ্ভিদ (Tracheophytes) হলো টেরিডোফাইট থেকে শুরু: Selaginella, Equisetum, Pinus এবং Wolffia (মোট ৪টি)। শৈবাল ও ব্রায়োফাইটে সংবহন কলা থাকে না।',
    },
    {
        "id": 'BIO-PK-130',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Consider the following features:<br>1. Protonema stage<br>2. Multicellular branched rhizoids<br>3. Elaborate peristome teeth mechanism for spore dispersal<br>These diagnostic features collectively define:',
        "bn": 'নিচের বৈশিষ্ট্যগুলি বিবেচনা করো:<br>১. প্রোটোনেমা দশা<br>২. বহুকোষী শাখাযুক্ত রাইজয়েড<br>৩. রেণু বিচ্ছুরণে জটিল পেরিস্টোম দাঁতের উপস্থিতি<br>এই বৈশিষ্ট্যগুলি সামগ্রিকভাবে কাকে নির্দেশ করে?',
        "opts": {
            "en": ['Mosses (such as Funaria)', 'Liverworts (such as Marchantia)', 'Pteridophytes (such as Ferns)', 'Algae (such as Chara)'],
            "bn": ['মস (যেমন ফিউনারিয়া)', 'লিভারওয়ার্ট (যেমন মারকানশিয়া)', 'টেরিডোফাইটা (যেমন ফার্ন)', 'শৈবাল (যেমন কারা)']
        },
        "correct": 0,
        "expl_en": 'All three are signature defining features of mosses (Bryopsida): protonema, multicellular branched rhizoids with oblique septa, and capsule with peristome teeth.',
        "expl_bn": 'প্রোটোনেমা, বহুকোষী তির্যক প্রাচীরযুক্ত রাইজয়েড এবং পেরিস্টোম দাঁত—এগুলি মসের (যেমন ফিউনারিয়া) একক শনাক্তকারী বৈশিষ্ট্য।',
    },
    {
        "id": 'BIO-PK-131',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'Which of the following gymnosperms lacks motile ciliated male gametes and exhibits completely non-motile sperm transported by siphonogamy?',
        "bn": 'নিচের কোন ব্যক্তবীজীতে চলনক্ষম সিলিয়াযুক্ত শুক্রাণুর সম্পূর্ণ অভাব দেখা যায় এবং পরাগনালীর মাধ্যমে নিশ্চল শুক্রাণু পরিবাহিত হয়?',
        "opts": {
            "en": ['Pinus', 'Cycas', 'Ginkgo', 'Zamia'],
            "bn": ['পাইনাস (Pinus)', 'সাইকাস', 'জিংগো', 'জ্যামিয়া']
        },
        "correct": 0,
        "expl_en": 'Pinus has non-motile male gametes carried strictly by pollen tube (siphonogamy). Cycas and Ginkgo are primitive gymnosperms that still retain swimming multiflagellated sperm (zooidogamy combined with siphonogamy).',
        "expl_bn": 'পাইনাসের শুক্রাণু সম্পূর্ণ নিশ্চল এবং তা পরাগনালী দ্বারা বাহিত হয়। সাইকাস ও জিংগোতে আদিম বৈশিষ্ট্য হিসেবে সিলিয়াযুক্ত সচল শুক্রাণু থাকে।',
    },
    {
        "id": 'BIO-PK-132',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Easy',
        "en": 'Coralline algae like Corallina secrete heavy deposits of ________ in their cell walls, contributing significantly to coral reef formation.',
        "bn": 'কোরালিনা (Corallina)-র মতো কোরালাইন শৈবাল তাদের কোষপ্রাচীরে বিপুল পরিমাণ ________ সঞ্চয় করে প্রবাল প্রাচীর (Coral reef) গঠনে ভূমিকা রাখে।',
        "opts": {
            "en": ['Calcium carbonate (CaCO3)', 'Silicon dioxide (SiO2)', 'Magnesium sulphate', 'Sodium chloride'],
            "bn": ['ক্যালসিয়াম কার্বনেট (CaCO3)', 'সিলিকন ডাইঅক্সাইড (SiO2)', 'ম্যাগনেসিয়াম সালফেট', 'সোডিয়াম ক্লোরাইড']
        },
        "correct": 0,
        "expl_en": 'Coralline red algae deposit calcite (calcium carbonate) into their cell walls, making them stony and providing structural foundation for tropical marine coral reefs.',
        "expl_bn": 'কোরালাইন লাল শৈবাল তাদের প্রাচীরে ক্যালসিয়াম কার্বনেট সঞ্চয় করে পাথরের মতো শক্ত প্রাচীর তৈরি করে যা প্রবাল প্রাচীর সৃষ্টিতে সাহায্য করে।',
    },
    {
        "id": 'BIO-PK-133',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Medium',
        "en": 'In liverworts, which specialized hygroscopic diploid structures twist and coil to fling spores out of the ruptured capsule?',
        "bn": 'লিভারওয়ার্টে কোন বিশেষ হাইগ্রোস্কোপিক ডিপ্লয়েড গঠনগুলি আর্দ্রতার পরিবর্তনে কুঁচকে গিয়ে ক্যাপসুল থেকে স্পোর বাইরে নিক্ষেপ করে?',
        "opts": {
            "en": ['Elaters', 'Peristome teeth', 'Pseudoelaters', 'Annulus'],
            "bn": ['ইলেটার্স (Elaters)', 'পেরিস্টোম দাঁত', 'সিউডোইলেটার্স', 'অ্যানুলাস']
        },
        "correct": 0,
        "expl_en": 'In Marchantia capsule, spindle-shaped diploid cells with helical thickenings called elaters twist hygroscopically as they dry, flicking spores into passing air currents.',
        "expl_bn": 'মারকানশিয়ার ক্যাপসুলে সর্পিলাকার স্থূলীকরণযুক্ত ইলেটার্স (Elaters) থাকে যা আর্দ্রতার পরিবর্তনে পাক খেয়ে স্পোর নিক্ষেপ করে।',
    },
    {
        "id": 'BIO-PK-134',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'If a moss protonema cell has 18 chromosomes, how many chromosomes will be present respectively in its rhizoid, leaf cell, operculum cell, and spore mother cell?',
        "bn": 'একটি মসের প্রোটোনেমা কোষে যদি ১৮টি ক্রোমোজোম থাকে, তবে তার রাইজয়েড, পাতার কোষ, অপারকুলাম কোষ এবং স্পোর মাতৃকোষে ক্রোমোজোম সংখ্যা যথাক্রমে কত হবে?',
        "opts": {
            "en": ['18, 18, 36, 36', '18, 36, 36, 18', '9, 18, 36, 18', '18, 18, 18, 36'],
            "bn": ['১৮, ১৮, ৩৬, ৩৬', '১৮, ৩৬, ৩৬, ১৮', '৯, ১৮, ৩৬, ১৮', '১৮, ১৮, ১৮, ৩৬']
        },
        "correct": 0,
        "expl_en": 'Moss protonema is gametophytic (n = 18). Rhizoid is gametophytic (n = 18). Leaf cell is gametophytic (n = 18). Operculum is part of the capsule of the sporophyte (2n = 36). Spore mother cell is sporophytic (2n = 36). Hence: 18, 18, 36, 36.',
        "expl_bn": 'মসের গ্যামেটোফাইট হ্যাপ্লয়েড (n = 18), তাই প্রোটোনেমা, রাইজয়েড ও পাতার কোষ = ১৮। অপারকুলাম ও স্পোর মাতৃকোষ স্পোরোফাইটের অংশ হওয়ায় ডিপ্লয়েড (2n = 36)। অতএব ১৮, ১৮, ৩৬, ৩৬।',
    },
    {
        "id": 'BIO-PK-135',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Plant Kingdom',
        "difficulty": 'Hard',
        "en": 'Which of the following evolutionary sequences correctly outlines the progressive reduction of the gametophytic generation and dominance of the sporophytic generation in land plants?',
        "bn": 'স্থলজ উদ্ভিদের বিবর্তনে গ্যামেটোফাইট দশার ক্রমহ্রাস এবং স্পোরোফাইট দশার ক্রমবর্ধমান আধিপত্যের সঠিক বিবর্তনীয় ধারা কোনটি?',
        "opts": {
            "en": ['Bryophytes (Dominant gametophyte, dependent sporophyte) → Pteridophytes (Dominant sporophyte, independent gametophyte) → Gymnosperms (Dominant sporophyte, microscopic dependent gametophyte enclosed in ovule/pollen)', 'Pteridophytes → Bryophytes → Gymnosperms', 'Gymnosperms → Pteridophytes → Bryophytes', 'Bryophytes → Gymnosperms → Pteridophytes'],
            "bn": ['ব্রায়োফাইটা (প্রধান গ্যামেটোফাইট, নির্ভরশীল স্পোরোফাইট) → টেরিডোফাইটা (প্রধান স্পোরোফাইট, স্বাধীন গ্যামেটোফাইট) → ব্যক্তবীজী (প্রধান স্পোরোফাইট, ডিম্বক ও পরাগরেণুর ভেতরে আবদ্ধ আণুবীক্ষণিক নির্ভরশীল গ্যামেটোফাইট)', 'টেরিডোফাইটা → ব্রায়োফাইটা → ব্যক্তবীজী', 'ব্যক্তবীজী → টেরিডোফাইটা → ব্রায়োফাইটা', 'ব্রায়োফাইটা → ব্যক্তবীজী → টেরিডোফাইটা']
        },
        "correct": 0,
        "expl_en": 'Plant evolution demonstrates progressive reduction of the haploid gametophyte: in bryophytes it is the main plant; in pteridophytes it is reduced to a small prothallus; in gymnosperms/angiosperms it is reduced to microscopic cells completely enclosed inside sporangia on the sporophyte.',
        "expl_bn": 'উদ্ভিদ বিবর্তনে গ্যামেটোফাইট বা লিঙ্গধর দশাটি ক্রমশ সংকুচিত হয়েছে: ব্রায়োফাইটে এটি প্রধান উদ্ভিদ, টেরিডোফাইটে এটি ক্ষুদ্র প্রোথ্যালাস এবং ব্যক্তবীজী ও গুপ্তবীজীতে এটি স্পোরোফাইটের ভেতর আবদ্ধ কয়েকটি আণুবীক্ষণিক কোষে পরিণত হয়েছে।',
    },
    {
        "id": 'BIO-AK-001',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'In which phylum are cells arranged as loose cell aggregates exhibiting a cellular level of organization without forming true tissues?',
        "bn": 'কোন পর্বে কোষগুলি ঢিলেঢালাভাবে পুঞ্জীভূত হয়ে অবস্থান করে এবং প্রকৃত কলা গঠন না করে কোষীয় মাত্রার (cellular level) দৈহিক সংগঠন প্রদর্শন করে?',
        "opts": {
            "en": ['Porifera (Sponges)', 'Coelenterata', 'Ctenophora', 'Platyhelminthes'],
            "bn": ['পরিফেরা বা স্পঞ্জ (Porifera)', 'সিলেন্টারেটা', 'টিনোফোরা', 'প্লাটিহেলমিন্থেস']
        },
        "correct": 0,
        "expl_en": 'In sponges (Phylum Porifera), the cells are arranged as loose cell aggregates, i.e., they exhibit cellular level of organisation.',
        "expl_bn": 'পরিফেরা বা স্পঞ্জের দেহে কোষগুলি পৃথক বা ঢিলেঢালাভাবে পুঞ্জীভূত থাকে এবং কোনো সুসংগঠিত কলা তৈরি করে না, একে কোষীয় মাত্রার সংগঠন বলে।',
    },
    {
        "id": 'BIO-AK-002',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following phyla exhibits tissue level of body organization?',
        "bn": 'নিচের কোন পর্বটিতে কলা মাত্রার (tissue level) দৈহিক সংগঠন পরিলক্ষিত হয়?',
        "opts": {
            "en": ['Coelenterata (Cnidaria) and Ctenophora', 'Porifera only', 'Platyhelminthes and Aschelminthes', 'Annelida and Arthropoda'],
            "bn": ['সিলেন্টারেটা (নিডারিয়া) এবং টিনোফোরা', 'কেবল পরিফেরা', 'প্লাটিহেলমিন্থেস এবং অ্যাসকেলমিন্থেস', 'অ্যানেলিডা এবং আর্থ্রোপোডা']
        },
        "correct": 0,
        "expl_en": 'In coelenterates (cnidarians) and ctenophores, the arrangement of cells is more complex and cells performing the same function are arranged into tissues, hence tissue level of organization.',
        "expl_bn": 'সিলেন্টারেটা এবং টিনোফোরা পর্বের প্রাণীদের ক্ষেত্রে সমজাতীয় কাজের কোষগুলি মিলে কলা গঠন করে, অর্থাৎ এরা কলা-মাত্রার সংগঠনযুক্ত।',
    },
    {
        "id": 'BIO-AK-003',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'An incomplete digestive system having only a single opening to the outside of the body that serves as both mouth and anus is found in:',
        "bn": 'একটিমাত্র বহিস্থ ছিদ্রযুক্ত অসম্পূর্ণ পৌষ্টিকতন্ত্র যা মুখ ও পায়ু উভয় হিসেবেই কাজ করে, তা কোন পর্বে দেখা যায়?',
        "opts": {
            "en": ['Platyhelminthes (Flatworms)', 'Aschelminthes', 'Annelida', 'Chordata'],
            "bn": ['প্লাটিহেলমিন্থেস বা চ্যাপ্টাকৃমি (Platyhelminthes)', 'অ্যাসকেলমিন্থেস', 'অ্যানেলিডা', 'কর্ডাটা']
        },
        "correct": 0,
        "expl_en": 'Incomplete digestive system has only a single opening to the outside of the body that serves as both mouth and anus, as in Platyhelminthes. A complete digestive system has two openings (mouth and anus).',
        "expl_bn": 'প্লাটিহেলমিন্থেস বা চ্যাপ্টাকৃমির পৌষ্টিকনালীতে একটিমাত্র ছিদ্র থাকে যা খাদ্য গ্রহণ ও বর্জ্য নির্গমন উভয়ের কাজ করে (Blind sac body plan)।',
    },
    {
        "id": 'BIO-AK-004',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'When any plane passing through the central axis of the body divides the organism into two identical halves, it is called:',
        "bn": 'দেহের কেন্দ্রীয় অক্ষ বরাবর যেকোনো তল দিয়ে অতিক্রমকারী রেখা যদি দেহকে দুটি সদৃশ অর্ধাংশে বিভক্ত করে, তবে তাকে কী বলে?',
        "opts": {
            "en": ['Radial symmetry (e.g., Coelenterates, Ctenophores, adult Echinoderms)', 'Bilateral symmetry (e.g., Annelids, Arthropods)', 'Asymmetry (e.g., most sponges)', 'Spherical segmentation'],
            "bn": ['অরীয় প্রতিসাম্য বা রেডিয়াল সিমেট্রি (Radial symmetry - যেমন সিলেন্টারেটা, টিনোফোরা, পূর্ণাঙ্গ একাইনোডার্মাটা)', 'দ্বিপার্শ্বীয় প্রতিসাম্য (যেমন অ্যানেলিডা, আর্থ্রোপোডা)', 'অপ্রতিসাম্য (যেমন অধিকাংশ স্পঞ্জ)', 'গোলাকার খণ্ডায়ন']
        },
        "correct": 0,
        "expl_en": 'When any plane passing through the central axis of the body divides the organism into two identical halves, it is called radial symmetry. Coelenterates, ctenophores and echinoderms have this kind of body plan.',
        "expl_bn": 'কেন্দ্রীয় অক্ষ বরাবর যেকোনো তলে দেহকে সমান দুই ভাগে ভাগ করা গেলে তাকে অরীয় প্রতিসাম্য (Radial symmetry) বলে।',
    },
    {
        "id": 'BIO-AK-005',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Animals in which the body can be divided into identical left and right halves in only ONE plane exhibit:',
        "bn": 'যেসব প্রাণীর দেহকে কেবলমাত্র একটিমাত্র নির্দিষ্ট উল্লম্ব তলে সদৃশ বাম ও ডান অর্ধাংশে বিভক্ত করা যায়, তারা কী প্রদর্শন করে?',
        "opts": {
            "en": ['Bilateral symmetry (e.g., Platyhelminthes to Chordates)', 'Radial symmetry', 'Asymmetry', 'Biradial asymmetry'],
            "bn": ['দ্বিপার্শ্বীয় প্রতিসাম্য বা বাইল্যাটেরাল সিমেট্রি (Bilateral symmetry - যেমন প্লাটিহেলমিন্থেস থেকে কর্ডাটা)', 'অরীয় প্রতিসাম্য', 'অপ্রতিসাম্য', 'দ্বি-অরীয় অপ্রতিসাম্য']
        },
        "correct": 0,
        "expl_en": 'Animals like annelids, arthropods, etc., where the body can be divided into identical left and right halves in only one plane, exhibit bilateral symmetry.',
        "expl_bn": 'একটিমাত্র তলে দেহকে দুটি সদৃশ অর্ধাংশে (ডান ও বাম) ভাগ করা গেলে তাকে দ্বিপার্শ্বীয় প্রতিসাম্য (Bilateral symmetry) বলে।',
    },
    {
        "id": 'BIO-AK-006',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Animals in which the cells are arranged in two embryonic layers, an external ectoderm and an internal endoderm with an undifferentiated layer called mesoglea in between, are called:',
        "bn": 'যেসব প্রাণীর ভ্রূণীয় কোষগুলি বাইরের একটোডার্ম ও ভেতরের এন্ডোডার্ম নামক দুটি স্তরে এবং তাদের মাঝে অবিভেদিত মেসোগ্লিয়া (mesoglea) দ্বারা বিন্যস্ত থাকে, তাদের কী বলে?',
        "opts": {
            "en": ['Diploblastic animals (e.g., Coelenterates and Ctenophores)', 'Triploblastic animals (e.g., Platyhelminthes to Chordates)', 'Pseudocoelomates', 'Acoelomates'],
            "bn": ['দ্বিস্তরীয় বা ডিপ্লোব্লাস্টিক প্রাণী (Diploblastic - যেমন সিলেন্টারেটা ও টিনোফোরা)', 'ত্রিস্তরীয় বা ট্রিপ্লোব্লাস্টিক প্রাণী (প্লাটিহেলমিন্থেস থেকে কর্ডাটা)', 'সিউডোসিলোমেট', 'অ্যাসিলোমেট']
        },
        "correct": 0,
        "expl_en": 'Animals in which cells are arranged in two embryonic layers, external ectoderm and internal endoderm, are called diploblastic (e.g., coelenterates). An undifferentiated non-cellular layer, mesoglea, is present between them.',
        "expl_bn": 'এক্টোডার্ম ও এন্ডোডার্ম স্তরবিশিষ্ট এবং এদের মাঝে অকোষীয় মেসোগ্লিয়াযুক্ত প্রাণীদের দ্বিস্তরীয় বা ডিপ্লোব্লাস্টিক প্রাণী বলে।',
    },
    {
        "id": 'BIO-AK-007',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In which phylum is the body cavity NOT lined by mesoderm; instead, the mesoderm is present as scattered pouches between the ectoderm and endoderm (Pseudocoelom)?',
        "bn": 'কোন পর্বে দেহগহ্বরটি মেসোডার্ম দ্বারা সম্পূর্ণরূপে আবৃত থাকে না, বরং একটোডার্ম ও এন্ডোডার্মের মাঝে মেসোডার্মটি বিক্ষিপ্ত থলির (pouches) মতো অবস্থান করে (সিউডোসিলোম)?',
        "opts": {
            "en": ['Aschelminthes (Roundworms)', 'Platyhelminthes', 'Annelida', 'Mollusca'],
            "bn": ['অ্যাসকেলমিন্থেস বা গোলকৃমি (Aschelminthes)', 'প্লাটিহেলমিন্থেস', 'অ্যানেলিডা', 'মোলাস্কা']
        },
        "correct": 0,
        "expl_en": 'In some animals, the body cavity is not lined by mesoderm, instead, the mesoderm is present as scattered pouches in between the ectoderm and endoderm. Such a body cavity is called pseudocoelom and the animals possessing them are called pseudocoelomates (e.g., aschelminthes).',
        "expl_bn": 'অ্যাসকেলমিন্থেস বা গোলকৃমিতে প্রকৃত সিলোমের পরিবর্তে মেসোডার্মীয় থলি বিক্ষিপ্তভাবে থাকে, তাই এদের সিউডোসিলোমেট (Pseudocoelomate) বলে।',
    },
    {
        "id": 'BIO-AK-008',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Animals in which the body cavity is completely absent are called acoelomates. An example is:',
        "bn": 'যেসব প্রাণীর দেহে কোনো প্রকার সিলোম বা দেহগহ্বর থাকেই না (অ্যাসিলোমেট), তাদের উদাহরণ কোনটি?',
        "opts": {
            "en": ['Platyhelminthes (Flatworms)', 'Annelida (Earthworm)', 'Arthropoda (Cockroach)', 'Aschelminthes (Ascaris)'],
            "bn": ['প্লাটিহেলমিন্থেস বা চ্যাপ্টাকৃমি (Platyhelminthes)', 'অ্যানেলিডা', 'আর্থ্রোপোডা', 'অ্যাসকেলমিন্থেস']
        },
        "correct": 0,
        "expl_en": 'The animals in which the body cavity is absent are called acoelomates, e.g., platyhelminthes. The space between organs is filled with solid mesodermal parenchyma.',
        "expl_bn": 'প্লাটিহেলমিন্থেসের দেহে কোনো দেহগহ্বর বা সিলোম থাকে না (অ্যাসিলোমেট), অঙ্গগুলির মধ্যবর্তী স্থান প্যারেনকাইমা কলা দ্বারা পূর্ণ থাকে।',
    },
    {
        "id": 'BIO-AK-009',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'True internal and external serial segmentation of the body with repetition of at least some organs is known as metamerism (metameric segmentation). It is prominently exhibited by:',
        "bn": 'দেহের অন্তত কয়েকটি অঙ্গের পৌনঃপুনিক পুনরাবৃত্তিসহ প্রকৃত অভ্যন্তরীণ ও বাহ্যিক খণ্ডায়নকে মেটামারিজম বলে। এটি স্পষ্টভাবে কোন পর্বে দেখা যায়?',
        "opts": {
            "en": ['Annelida, Arthropoda, and Chordata', 'Porifera and Coelenterata', 'Platyhelminthes and Aschelminthes', 'Mollusca and Echinodermata'],
            "bn": ['অ্যানেলিডা, আর্থ্রোপোডা এবং কর্ডাটা', 'পরিফেরা এবং সিলেন্টারেটা', 'প্লাটিহেলমিন্থেস এবং অ্যাসকেলমিন্থেস', 'মোলাস্কা এবং একাইনোডার্মাটা']
        },
        "correct": 0,
        "expl_en": 'In animals like earthworm, the body shows true metameric segmentation where body is externally and internally divided into segments with serial repetition of at least some organs. True metamerism occurs in Annelids, Arthropods, and Chordates.',
        "expl_bn": 'প্রকৃত মেটামেরিক খণ্ডায়ন দেখা যায় অ্যানেলিডা (যেমন কেঁচো), আর্থ্রোপোডা এবং কর্ডাটাতে।',
    },
    {
        "id": 'BIO-AK-010',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'The notochord is a mesodermally derived rod-like structure formed on the ________ side during embryonic development in some animals.',
        "bn": 'নোটোকর্ড হলো মেসোডার্ম থেকে উৎপন্ন দণ্ডাকার গঠন যা ভ্রূণীয় বিকাশের সময় দেহের ________ দিকে গঠিত হয়।',
        "opts": {
            "en": ['Dorsal side', 'Ventral side', 'Lateral side', 'Anterior tip'],
            "bn": ['পৃষ্ঠীয় বা ডরসাল দিকে (Dorsal side)', 'অঙ্কীয় বা ভেন্ট্রাল দিকে', 'পার্শ্বীয় দিকে', 'অগ্রপ্রান্তে']
        },
        "correct": 0,
        "expl_en": 'Notochord is a mesodermally derived rod-like structure formed on the dorsal side during embryonic development in chordates.',
        "expl_bn": 'নোটোকর্ড হলো ভ্রূণের মেসোডার্ম থেকে উৎপন্ন একটি স্থিতিস্থাপক দণ্ডাকার গঠন যা দেহের পৃষ্ঠীয় (dorsal) দিকে গঠিত হয়।',
    },
    {
        "id": 'BIO-AK-011',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In sponges (Phylum Porifera), water enters through minute pores called ________ in the body wall into a central cavity called ________, from where it goes out through the ________.',
        "bn": 'স্পঞ্জে (Porifera) দেহপ্রাচীরের ক্ষুদ্র ক্ষুদ্র ছিদ্র ________ দিয়ে জল কেন্দ্রীয় গহ্বর ________-এ প্রবেশ করে এবং সেখান থেকে ________ দিয়ে বাইরে নির্গত হয়।',
        "opts": {
            "en": ['Ostia; Spongocoel; Osculum', 'Oscula; Spongocoel; Ostium', 'Hypostome; Gastrovascular cavity; Anus', 'Spicules; Paragastric chamber; Mouth'],
            "bn": ['অস্টিয়া (Ostia); স্পঞ্জোসিল (Spongocoel); অসকুলাম (Osculum)', 'অসকুলা; স্পঞ্জোসিল; অস্টিয়াম', 'হাইপোস্টোম; গ্যাস্ট্রোভাসকুলার গহ্বর; পায়ু', 'স্পিকিউল; প্যারাগ্যাস্ট্রিক প্রকোষ্ঠ; মুখ']
        },
        "correct": 0,
        "expl_en": 'Sponges have a water transport or canal system. Water enters through minute pores (ostia) in the body wall into a central cavity, spongocoel, from where it goes out through the osculum.',
        "expl_bn": 'জল সংবহন বা নালী তন্ত্রের মাধ্যমে জল অস্টিয়া (ostia) ছিদ্র দিয়ে কেন্দ্রীয় স্পঞ্জোসিলে ঢোকে এবং অসকুলাম (osculum) দিয়ে বাইরে বের হয়ে যায়।',
    },
    {
        "id": 'BIO-AK-012',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Specialized collar cells that line the spongocoel and canals in sponges are called:',
        "bn": 'স্পঞ্জের স্পঞ্জোসিল এবং নালীগুলিকে আবৃত করে রাখা বিশেষ ধরনের কলারযুক্ত কোষগুলিকে কী বলে?',
        "opts": {
            "en": ['Choanocytes (Collar cells)', 'Cnidocytes', 'Pinacocytes', 'Archaeocytes'],
            "bn": ['কোয়ানোসাইট বা কলার কোষ (Choanocytes)', 'নিডোসাইট', 'প্যাকোডোসাইট', 'আর্কিওসাইট']
        },
        "correct": 0,
        "expl_en": 'Choanocytes or collar cells line the spongocoel and the canals in sponges, maintaining water flow and trapping food particles by phagocytosis.',
        "expl_bn": 'কোয়ানোসাইট (Choanocytes) বা কলার কোষ হলো পরিফেরা পর্বের অনন্য বৈশিষ্ট্যপূর্ণ কোষ যা স্পঞ্জোসিলকে ঘিরে রাখে এবং জলপ্রবাহ বজায় রেখে খাদ্য সংগ্রহ করে।',
    },
    {
        "id": 'BIO-AK-013',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Digestion in sponges (Porifera) is strictly:',
        "bn": 'পরিফেরা বা স্পঞ্জের পুষ্টি ও পরিপাক পদ্ধতি কেমন প্রকৃতির?',
        "opts": {
            "en": ['Intracellular (takes place inside food vacuoles of cells)', 'Extracellular in an acidic stomach cavity', 'Both extracellular and intracellular in gastrovascular cavity', 'Holozoic through a keratinized beak'],
            "bn": ['অন্তঃকোষীয় বা ইন্ট্রাসেলুলার (কোষীয় খাদ্য গহ্বরের মধ্যে সম্পন্ন হয়)', 'বহিঃকোষীয়', 'বহিঃকোষীয় ও অন্তঃকোষীয় উভয়ই', 'কেরাটিনযুক্ত চঞ্চুর সাহায্যে']
        },
        "correct": 0,
        "expl_en": 'In sponges, digestion is intracellular. Food particles filtered by choanocytes are engulfed and digested inside food vacuoles within cells (amoebocytes/choanocytes).',
        "expl_bn": 'স্পঞ্জের দেহে পরিপাক প্রক্রিয়া সম্পূর্ণ অন্তঃকোষীয় (intracellular), যা কোষের খাদ্য গহ্বরের ভেতরে উৎসেচক দ্বারা সম্পন্ন হয়।',
    },
    {
        "id": 'BIO-AK-014',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'The body of sponges is supported by a skeleton made up of:',
        "bn": 'স্পঞ্জের দেহের অভ্যন্তরীণ কঙ্কাল কী দ্বারা গঠিত?',
        "opts": {
            "en": ['Spicules (calcareous/siliceous) or spongin fibres (proteinaceous)', 'Cartilage and calcium phosphate bones', 'Chitinous cuticle', 'Calcareous shells of calcium pectate'],
            "bn": ['স্পিকিউল (ক্যালসিয়াম/সিলিকা নির্মিত কাঁটা) অথবা স্পঞ্জিন তন্তু (প্রোটিন নির্মিত)', 'তরুণাস্থি ও ক্যালসিয়াম ফসফেট অস্থি', 'কাইটিনের বহিঃকঙ্কাল', 'ক্যালসিয়াম পেকটেটের খোলক']
        },
        "correct": 0,
        "expl_en": 'The body of sponges is supported by a skeleton made up of spicules (microscopic mineral spikes) or spongin fibres (flexible collagenous protein).',
        "expl_bn": 'স্পঞ্জের দেহ কঙ্কাল স্পিকিউল (ক্যালসিয়াম বা সিলিকা কাঁটা) বা স্পঞ্জিন তন্তু (spongin fibres) দিয়ে দৃঢ়তা লাভ করে।',
    },
    {
        "id": 'BIO-AK-015',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following is a freshwater sponge?',
        "bn": 'নিচের কোনটি একটি মিষ্ট জলের স্পঞ্জ (Freshwater sponge)?',
        "opts": {
            "en": ['Spongilla', 'Sycon (Scypha)', 'Euspongia (Bath sponge)', 'Euplectella (Venus flower basket)'],
            "bn": ['স্পঞ্জিলা (Spongilla)', 'সাইকন বা স্কাইফা', 'ইউস্পঞ্জিয়া বা স্নান স্পঞ্জ', 'ইউপ্লেকটেলা']
        },
        "correct": 0,
        "expl_en": 'Spongilla is the classic freshwater sponge. Sycon and Euspongia are marine sponges.',
        "expl_bn": 'স্পঞ্জিলা (Spongilla) হলো একটি অন্যতম প্রধান মিষ্ট জলের স্পঞ্জ।',
    },
    {
        "id": 'BIO-AK-016',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Cnidarians derive their name from specialized stinging cells called cnidoblasts or cnidocytes which contain stinging capsules called:',
        "bn": 'নিডারিয়া পর্বের প্রাণীদের নাম এসেছে বিশেষ দংশক কোষ নিডোসাইট বা নিডোব্লাস্ট থেকে, যার মধ্যে কোন বিষাক্ত দংশক অঙ্গাণু থাকে?',
        "opts": {
            "en": ['Nematocysts', 'Choanocytes', 'Statocysts', 'Colloblasts'],
            "bn": ['নেমাটোসিস্ট (Nematocysts)', 'কোয়ানোসাইট', 'স্ট্যাটোসিস্ট', 'কলোব্লাস্ট']
        },
        "correct": 0,
        "expl_en": 'The name cnidaria is derived from the cnidoblasts or cnidocytes (which contain stinging capsules or nematocysts) present on tentacles and body.',
        "expl_bn": 'নিডোব্লাস্ট কোষে নেমাটোসিস্ট (Nematocysts) নামক দংশন অঙ্গাণু থাকে যা হিপনোটক্সিন বিষ নিক্ষেপ করে শিকার ধরতে ও আত্মরক্ষায় সাহায্য করে।',
    },
    {
        "id": 'BIO-AK-017',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Cnidarians exhibit a central body cavity called ________ with a single opening on a conical projection called ________.',
        "bn": 'নিডারিয়ার দেহে একটি কেন্দ্রীয় গহ্বর ________ থাকে যার একমাত্র বহিঃছিদ্রটি ________ নামক কোণাকার অভিক্ষেপের শীর্ষে অবস্থিত।',
        "opts": {
            "en": ['Gastrovascular cavity (coelenteron); hypostome', 'Spongocoel; osculum', 'Pseudocoelom; proboscis', 'Enterocoel; ambulacral groove'],
            "bn": ['গ্যাস্ট্রোভাসকুলার গহ্বর বা সিলেন্টেরন; হাইপোস্টোম (Hypostome)', 'স্পঞ্জোসিল; অসকুলাম', 'সিউডোসিলোম; প্রোবোসিস', 'এন্টারোসিল; অ্যাম্বুল্যাক্রাল খাঁজ']
        },
        "correct": 0,
        "expl_en": 'Cnidarians have a central gastrovascular cavity with a single opening, mouth on hypostome. Digestion is both extracellular and intracellular.',
        "expl_bn": 'নিডারিয়ার কেন্দ্রীয় গহ্বরকে গ্যাস্ট্রোভাসকুলার গহ্বর বা সিলেন্টেরন বলে, যার মুখে একটিমাত্র ছিদ্র হাইপোস্টোম (hypostome)-এর ওপর থাকে।',
    },
    {
        "id": 'BIO-AK-018',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Cnidarians exhibit two basic body forms: Polyp and Medusa. Which statement correctly distinguishes them?',
        "bn": 'নিডারিয়ার দুটি প্রধান দৈহিক রূপ হলো পলিপ (Polyp) এবং মেদুসা (Medusa)। নিচের কোন বক্তব্যটি এদের মধ্যে সঠিক পার্থক্য নির্দেশ করে?',
        "opts": {
            "en": ['Polyp is sessile and cylindrical (e.g., Hydra, Adamsia); Medusa is umbrella-shaped and free-swimming (e.g., Aurelia / Jelly fish)', 'Polyp is free-swimming and umbrella-shaped; Medusa is sessile and cylindrical', 'Both Polyp and Medusa are always sessile and colonial', 'Polyp produces polyps sexually; Medusa produces medusae asexually'],
            "bn": ['পলিপ হলো স্থানু বা নিশ্চল এবং নলাকার (যেমন হাইড্রা, অ্যাডামসিয়া); মেদুসা হলো ছাতার মতো এবং মুক্ত সাঁতারু (যেমন অরেলিয়া বা জেলিফিশ)', 'পলিপ হলো সচল ছাতার মতো এবং মেদুসা নিশ্চল নলাকার', 'পলিপ ও মেদুসা উভয়ই সর্বদা স্থানু', 'পলিপ যৌন জননে নতুন পলিপ এবং মেদুসা অযৌন জননে মেদুসা তৈরি করে']
        },
        "correct": 0,
        "expl_en": 'Polyp is a sessile and cylindrical form like Hydra, Adamsia, etc., whereas Medusa is umbrella-shaped and free-swimming like Aurelia or jelly fish.',
        "expl_bn": 'পলিপ হলো নিশ্চল ও নলাকার দেহরূপ (যেমন Hydra ও Adamsia), আর মেদুসা হলো ছাতাসদৃশ ও মুক্ত সাঁতারু দেহরূপ (যেমন Aurelia বা জেলিফিশ)।',
    },
    {
        "id": 'BIO-AK-019',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'The phenomenon in which cnidarians exhibit alternation of generations between polyp and medusa (polyps produce medusae asexually and medusae form polyps sexually, e.g., in Obelia) is called:',
        "bn": 'যেসব নিডারিয়াতে পলিপ ও মেদুসার মধ্যে সুনির্দিষ্ট জনুক্রম দেখা যায় (পলিপ অযৌনভাবে মেদুসা তৈরি করে এবং মেদুসা যৌন জননে পলিপ তৈরি করে, যেমন Obelia-তে), তাকে কী বলা হয়?',
        "opts": {
            "en": ['Metagenesis', 'Metamorphosis', 'Ecdysis', 'Parthenogenesis'],
            "bn": ['মেটাজেনেসিস (Metagenesis)', 'মেটামরফোসিস বা রূপান্তর', 'একডাইসিস', 'পার্থেনোজেনেসিস']
        },
        "correct": 0,
        "expl_en": 'Those cnidarians which exist in both forms exhibit alternation of generation (Metagenesis), i.e., polyps produce medusae asexually and medusae form the polyps sexually (e.g., Obelia).',
        "expl_bn": 'অবেলিক জাতীয় নিডারিয়ায় অযৌন পলিপ ও যৌন মেদুসা দশার ক্রমান্বয়িক আবর্তনকে মেটাজেনেসিস (Metagenesis) বলে।',
    },
    {
        "id": 'BIO-AK-020',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": "Which cnidarian is commonly called the 'Portuguese man-of-war'?",
        "bn": "কোন নিডারিয়ান প্রাণীটিকে সাধারণভাবে 'পর্তুগিজ ম্যান-অফ-ওয়ার' (Portuguese man-of-war) বলা হয়?",
        "opts": {
            "en": ['Physalia', 'Adamsia', 'Pennatula', 'Gorgonia'],
            "bn": ['ফাইসিলিয়া (Physalia)', 'অ্যাডামসিয়া', 'পেন্নাটুলা', 'গর্গোনিয়া']
        },
        "correct": 0,
        "expl_en": 'Common names from NCERT: Physalia (Portuguese man-of-war), Adamsia (Sea anemone), Pennatula (Sea-pen), Gorgonia (Sea-fan), Meandrina (Brain coral).',
        "expl_bn": 'Physalia-কে সাধারণভাবে পর্তুগিজ ম্যান-অফ-ওয়ার বলা হয়।',
    },
    {
        "id": 'BIO-AK-021',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Corals have a skeleton composed of:',
        "bn": 'প্রবাল বা কোরাল (Corals)-এর শক্ত কঙ্কাল মূলত কী দ্বারা গঠিত?',
        "opts": {
            "en": ['Calcium carbonate (CaCO3)', 'Silica (SiO2)', 'Chitin', 'Spongin'],
            "bn": ['ক্যালসিয়াম কার্বনেট (CaCO3)', 'সিলিকা', 'কাইটিন', 'স্পঞ্জিন']
        },
        "correct": 0,
        "expl_en": 'Some cnidarians, for example, corals have a stony exoskeleton composed of calcium carbonate (CaCO3).',
        "expl_bn": 'কোরাল বা প্রবালের কঙ্কাল প্রধানত ক্যালসিয়াম কার্বনেট (CaCO3) দিয়ে গঠিত।',
    },
    {
        "id": 'BIO-AK-022',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Ctenophores are commonly known as:',
        "bn": 'টিনোফোরা (Ctenophora) পর্বের প্রাণীরা সাধারণভাবে কী নামে পরিচিত?',
        "opts": {
            "en": ['Sea walnuts or Comb jellies', 'Sponges or Bath sponges', 'Flatworms or Tapeworms', 'Roundworms or Hookworms'],
            "bn": ['সি-ওয়ালনাট (Sea walnuts) বা চিরুনি জেলি (Comb jellies)', 'স্নান স্পঞ্জ', 'ফিতাকৃমি', 'হুকওয়ার্ম']
        },
        "correct": 0,
        "expl_en": 'Ctenophores, commonly known as sea walnuts or comb jellies, are exclusively marine, radially symmetrical, diploblastic organisms with tissue level of organisation.',
        "expl_bn": 'টিনোফোরা পর্বের প্রাণীদের সাধারণভাবে সি-ওয়ালনাট (sea walnuts) বা চিরুনি জেলি (comb jellies) বলা হয়।',
    },
    {
        "id": 'BIO-AK-023',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'The body of ctenophores bears ________ external rows of ciliated comb plates, which help in ________.',
        "bn": 'টিনোফোরার দেহে ________টি সিলিয়াযুক্ত বহিস্থ কম্ব প্লেটের সারি থাকে, যা ________ সাহায্য করে।',
        "opts": {
            "en": ['Eight; locomotion', 'Six; digestion', 'Ten; reproduction', 'Four; excretion'],
            "bn": ['আটটি (8); চলনে (locomotion)', 'ছয়টি; পরিপাকে', 'দশটি; জননে', 'চারটি; রেচনে']
        },
        "correct": 0,
        "expl_en": 'The body bears eight external rows of ciliated comb plates, which help in locomotion.',
        "expl_bn": 'টিনোফোরার দেহে আটটি সিলিয়াযুক্ত চিরুনির মতো খাঁজকাটা প্লেট থাকে যা চলনে (locomotion) সহায়তা করে।',
    },
    {
        "id": 'BIO-AK-024',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'The property of a living organism to emit light, well-marked in ctenophores, is called:',
        "bn": 'সজীব প্রাণীদেহ থেকে আলো নির্গত হওয়ার যে দৃশ্যমান বৈশিষ্ট্য টিনোফোরাতে বিশেষভাবে লক্ষণীয়, তাকে কী বলে?',
        "opts": {
            "en": ['Bioluminescence', 'Fluorescence', 'Phosphorescence', 'Chemiluminescence'],
            "bn": ['বায়োলুমিনেসেন্স বা জৈব দ্যুতি (Bioluminescence)', 'প্রতিপ্রভা', 'অনুপ্রভা', 'রাসায়নিক দ্যুতি']
        },
        "correct": 0,
        "expl_en": 'Bioluminescence (the property of a living organism to emit light) is well-marked in ctenophores (e.g., Pleurobrachia and Ctenoplana).',
        "expl_bn": 'টিনোফোরা পর্বের প্রধান অন্যতম বৈশিষ্ট্য হলো তাদের দেহ থেকে নিজস্ব আলো নির্গমন বা বায়োলুমিনেসেন্স (Bioluminescence)।',
    },
    {
        "id": 'BIO-AK-025',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Which of the following statements about reproduction in Ctenophores is CORRECT?',
        "bn": 'টিনোফোরা পর্বের জনন সম্পর্কিত কোন বক্তব্যটি সঠিক?',
        "opts": {
            "en": ['Reproduction takes place only by sexual means; fertilization is external with indirect development', 'Asexual reproduction by budding is dominant', 'Fertilization is strictly internal with direct development', 'They are dioecious with viviparous birth'],
            "bn": ['জনন কেবলমাত্র যৌন উপায়ে ঘটে; বহিঃনিষেক ঘটে এবং পরোক্ষ রূপান্তরের মাধ্যমে বিকাশ ঘটে', 'মুকুলোদগম দ্বারা অযৌন জনন প্রধান', 'নিষেক অভ্যন্তরীণ এবং সরাসরি বিকাশ হয়', 'এরা একলিঙ্গ এবং জরায়ুজ']
        },
        "correct": 0,
        "expl_en": 'Ctenophores are hermaphrodites. Reproduction takes place only by sexual means. Fertilisation is external with indirect development (cydippid larva).',
        "expl_bn": 'টিনোফোরায় অযৌন জনন একেবারেই অনুপস্থিত; জনন কেবল যৌন উপায়ে ঘটে, বহিঃনিষেক হয় এবং সিডিপ্পিড লার্ভার মাধ্যমে পরোক্ষ বিকাশ সম্পন্ন হয়।',
    },
    {
        "id": 'BIO-AK-026',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Why are members of Phylum Platyhelminthes commonly called flatworms?',
        "bn": "প্লাটিহেলমিন্থেস পর্বের সদস্যদের সাধারণভাবে 'চ্যাপ্টাকৃমি' (flatworms) বলা হয় কেন?",
        "opts": {
            "en": ['They have a dorso-ventrally flattened body', 'They have a circular cylindrical body', 'They have flat feet for crawling on sand', 'Their eggs are flattened discs'],
            "bn": ['তাদের দেহটি পৃষ্ঠ-অঙ্কীয়ভাবে চ্যাপ্টা (dorso-ventrally flattened)', 'তাদের দেহ বৃত্তাকার নলাকার', 'বালিতে চলার জন্য চ্যাপ্টা পা থাকে', 'তাদের ডিমগুলি চ্যাপ্টা চাকতির মতো']
        },
        "correct": 0,
        "expl_en": 'They have dorso-ventrally flattened body, hence are called flatworms. They are mostly endoparasites found in animals including human beings.',
        "expl_bn": 'প্লাটিহেলমিন্থেসের দেহটি পৃষ্ঠ ও অঙ্কীয় উভয় দিক থেকেই চ্যাপ্টা ফিতার মতো, তাই এদের চ্যাপ্টাকৃমি (Flatworms) বলা হয়।',
    },
    {
        "id": 'BIO-AK-027',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Specialised excretory and osmoregulatory cells found in flatworms (Platyhelminthes) are called:',
        "bn": 'চ্যাপ্টাকৃমিতে (Platyhelminthes) রেচন ও অভিস্রবণ নিয়ন্ত্রণে সাহায্যকারী বিশেষ কোষগুলিকে কী বলে?',
        "opts": {
            "en": ['Flame cells (Protonephridia)', 'Nephridia', 'Malpighian tubules', 'Renette cells'],
            "bn": ['শিখা কোষ বা ফ্লেম সেল (Flame cells / Protonephridia)', 'নেফ্রিডিয়া', 'ম্যালপিজিয়ান নালিকা', 'রেনেট কোষ']
        },
        "correct": 0,
        "expl_en": 'Specialised cells called flame cells help in osmoregulation and excretion in platyhelminthes.',
        "expl_bn": 'প্লাটিহেলমিন্থেসের প্রধান রেচন অঙ্গ হলো শিখা কোষ (Flame cells বা Protonephridia) যা রেচন ও অভিস্রবণ নিয়ন্ত্রণে অংশ নেয়।',
    },
    {
        "id": 'BIO-AK-028',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Parasitic flatworms like tapeworms possess which special structures for adhering to the host intestinal lining?',
        "bn": 'ফিতাকৃমির মতো পরজীবী চ্যাপ্টাকৃমিতে পোষকের অন্ত্রপ্রাচীরে আটকে থাকার জন্য কোন বিশেষ অঙ্গ থাকে?',
        "opts": {
            "en": ['Hooks and suckers on the scolex', 'Tentacles and comb plates', 'Parapodia and setae', 'Radula and mantle'],
            "bn": ['স্কোলেক্সের ওপর হুক এবং চোষক বা সাকার (Hooks and suckers)', 'কর্ষিকা ও কম্ব প্লেট', 'প্যারাপোডিয়া ও সিটা', 'রেডুলা ও ম্যান্টল']
        },
        "correct": 0,
        "expl_en": 'Hooks and suckers are present in the parasitic forms (such as Taenia solium) on their scolex to anchor firmly into host tissue. Some absorb nutrients directly through body surface.',
        "expl_bn": 'পরজীবী ফিতাকৃমির মাথায় বা স্কোলেক্সে হুক ও চোষক (suckers) থাকে যা দিয়ে এরা পোষকের অন্ত্রের গায়ে দৃঢ়ভাবে আটকে থাকে।',
    },
    {
        "id": 'BIO-AK-029',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which free-living flatworm possesses high regeneration capacity?',
        "bn": 'নিচের কোন মুক্তজীবী চ্যাপ্টাকৃমিতে অপরিসীম পুনরুৎপাদন ক্ষমতা (high regeneration capacity) দেখা যায়?',
        "opts": {
            "en": ['Planaria', 'Taenia (Tapeworm)', 'Fasciola (Liver fluke)', 'Schistosoma (Blood fluke)'],
            "bn": ['প্ল্যানেরিয়া (Planaria)', 'টিনিয়া বা ফিতাকৃমি', 'ফ্যাসিওলা বা যকৃৎ কৃমি', 'সিস্টোসোমা']
        },
        "correct": 0,
        "expl_en": 'Planaria, a freshwater free-living flatworm, possesses high regeneration capacity; even a small severed fragment can reconstitute an entire organism.',
        "expl_bn": 'প্ল্যানেরিয়া (Planaria) হলো এমন এক মুক্তজীবী চ্যাপ্টাকৃমি যার দেহে অসাধারণ পুনরুৎপাদন ক্ষমতা বর্তমান।',
    },
    {
        "id": 'BIO-AK-030',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'The body of Aschelminthes is circular in cross-section, hence the name:',
        "bn": 'অ্যাসকেলমিন্থেস (Aschelminthes) পর্বের প্রাণীদের দেহের প্রস্থচ্ছেদ বৃত্তাকার হওয়ায় এদের কী নামে ডাকা হয়?',
        "opts": {
            "en": ['Roundworms', 'Flatworms', 'Segmented worms', 'Pinworms only'],
            "bn": ['গোলকৃমি (Roundworms)', 'চ্যাপ্টাকৃমি', 'খণ্ডায়িত কৃমি', 'পিনকৃমি']
        },
        "correct": 0,
        "expl_en": 'The body of the aschelminthes is circular in cross-section, hence, the name roundworms.',
        "expl_bn": 'দেহের প্রস্থচ্ছেদ সম্পূর্ণ বৃত্তাকার হওয়ায় অ্যাসকেলমিন্থেসদের গোলকৃমি বা Roundworms বলা হয়।',
    },
    {
        "id": 'BIO-AK-031',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In roundworms (Aschelminthes), the alimentary canal is complete with a well-developed:',
        "bn": 'গোলকৃমির (Aschelminthes) সম্পূর্ণ পৌষ্টিকনালীর অন্যতম প্রধান বৈশিষ্ট্য হলো এতে কোন সুগঠিত অঙ্গ থাকে?',
        "opts": {
            "en": ['Muscular pharynx', 'Teeth-bearing radula', 'Crop and gizzard', 'Typhlosole'],
            "bn": ['পেশিবহুল গলবিল বা ফ্যারিংস (Muscular pharynx)', 'দাঁতযুক্ত রেডুলা', 'ক্রপ এবং গিজার্ড', 'টিফ্লোসোল']
        },
        "correct": 0,
        "expl_en": 'Alimentary canal is complete in Aschelminthes with a well-developed muscular pharynx.',
        "expl_bn": 'গোলকৃমির পৌষ্টিকনালী সম্পূর্ণ এবং এদের একটি সুগঠিত ও শক্তিশালী পেশিবহুল গলবিল (muscular pharynx) থাকে যা খাদ্য চোষণে সাহায্য করে।',
    },
    {
        "id": 'BIO-AK-032',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Sexual dimorphism in Ascaris lumbricoides is distinctly characterized by:',
        "bn": 'অ্যাসকারিস বা সাধারণ গোলকৃমিতে যৌন দ্বিরূপতা কীভাবে সুস্পষ্টভাবে প্রকাশিত হয়?',
        "opts": {
            "en": ['Females are longer than males, and males have a curved posterior end with pineal spicules', 'Males are longer than females, and females have curved tail', 'Males and females are completely identical in external morphology', 'Females have wings while males are apterous'],
            "bn": ['স্ত্রী কৃমিরা পুরুষদের তুলনায় লম্বা হয় এবং পুরুষদের লেজের দিকটি বাঁকানো ও পিনিয়াল স্পিকিউলযুক্ত থাকে', 'পুরুষরা স্ত্রীদের তুলনায় অনেক লম্বা হয়', 'পুরুষ ও স্ত্রী বাহ্যিকভাবে সম্পূর্ণ সদৃশ', 'স্ত্রীদের ডানা থাকে কিন্তু পুরুষরা ডানাহীন']
        },
        "correct": 0,
        "expl_en": 'Sexes are separate (dioecious) in Ascaris. Often females are longer than males. Males are shorter and possess a curved posterior tail bearing copulatory pineal spicules.',
        "expl_bn": 'অ্যাসকারিসে স্ত্রী কৃমি পুরুষের চেয়ে আকারে দীর্ঘ হয়। পুরুষ কৃমির পশ্চাৎভাগ বাঁকানো থাকে এবং তাতে সঙ্গমে সাহায্যকারী পিনিয়াল স্পিকিউল থাকে।',
    },
    {
        "id": 'BIO-AK-033',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Wuchereria bancrofti, the filarial worm that causes chronic inflammation of lymphatic vessels (Elephantiasis), belongs to:',
        "bn": 'লসিকা নালীর দীর্ঘস্থায়ী প্রদাহজনিত গোদ বা ফাইলেরিয়াসিস রোগ সৃষ্টিকারী কৃমি উচেরেরিয়া (Wuchereria bancrofti) কোন পর্বভুক্ত?',
        "opts": {
            "en": ['Aschelminthes', 'Platyhelminthes', 'Annelida', 'Arthropoda'],
            "bn": ['অ্যাসকেলমিন্থেস বা গোলকৃমি (Aschelminthes)', 'প্লাটিহেলমিন্থেস', 'অ্যানেলিডা', 'আর্থ্রোপোডা']
        },
        "correct": 0,
        "expl_en": 'Wuchereria (filaria worm) is a nematode belonging to Phylum Aschelminthes.',
        "expl_bn": 'ফাইলেরিয়া কৃমি উচেরেরিয়া (Wuchereria) হলো অ্যাসকেলমিন্থেস পর্বভুক্ত নেমাটোড।',
    },
    {
        "id": 'BIO-AK-034',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Ancylostoma duodenale is commonly known as the:',
        "bn": 'অ্যানকাইলোস্টোমা (Ancylostoma duodenale)-কে সাধারণ ভাষায় কী কৃমি বলা হয়?',
        "opts": {
            "en": ['Hookworm', 'Roundworm', 'Tapeworm', 'Pinworm'],
            "bn": ['হুককৃমি বা হুকওয়ার্ম (Hookworm)', 'গোলকৃমি', 'ফিতাকৃমি', 'পিনকৃমি']
        },
        "correct": 0,
        "expl_en": 'Examples of Aschelminthes from NCERT: Ascaris (Roundworm), Wuchereria (Filaria worm), Ancylostoma (Hookworm).',
        "expl_bn": 'Ancylostoma-কে সাধারণ ভাষায় হুকওয়ার্ম (Hookworm) বলা হয়।',
    },
    {
        "id": 'BIO-AK-035',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In roundworms, an excretory tube removes body wastes from the body cavity through the:',
        "bn": 'গোলকৃমিতে দেহগহ্বর থেকে বর্জ্য পদার্থ বাইরে নিষ্কাশনের জন্য একটি রেচন নালী কার মাধ্যমে বাইরে উন্মুক্ত হয়?',
        "opts": {
            "en": ['Excretory pore', 'Flame cell duct', 'Osculum', 'Hypostome'],
            "bn": ['রেচন রন্ধ্র বা এক্সক্রিটরি পোর (Excretory pore)', 'শিখা কোষ নালী', 'অসকুলাম', 'হাইপোস্টোম']
        },
        "correct": 0,
        "expl_en": 'An excretory tube removes body wastes from the body cavity through the excretory pore located on the mid-ventral line behind the mouth.',
        "expl_bn": 'গোলকৃমির একটি H-আকৃতির রেচন নালীতন্ত্র রেচন রন্ধ্র (excretory pore)-র মাধ্যমে বর্জ্য পদার্থ দেহ থেকে বাইরে বের করে দেয়।',
    },
    {
        "id": 'BIO-AK-036',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'The phylum name Annelida (Latin, annulus: little ring) refers to which distinctive characteristic?',
        "bn": 'অ্যানেলিডা (ল্যাটিন annulus: ছোট আংটি) নামটি পর্বটির কোন স্বতন্ত্র বৈশিষ্ট্যের কারণে রাখা হয়েছে?',
        "opts": {
            "en": ['Body surface distinctly marked out into segments or metameres', 'Presence of ring-like calcareous shell', 'Ring-shaped tentacles around the hypostome', 'Circular swimming motion in water'],
            "bn": ['দেহের বহির্ভাগ সুস্পষ্টভাবে ছোট ছোট আংটির মতো খণ্ডক বা মেটামিয়ারে বিভক্ত', 'আংটির মতো ক্যালসিয়াম খোলকের উপস্থিতি', 'হাইপোস্টোমকে ঘিরে আংটির মতো কর্ষিকার বিন্যাস', 'জলের মধ্যে বৃত্তাকারে সাঁতার কাটার অভ্যাস']
        },
        "correct": 0,
        "expl_en": 'Their body surface is distinctly marked out into segments or metameres and, hence, the phylum name Annelida.',
        "expl_bn": 'অ্যানেলিডার দেহ সুস্পষ্টভাবে অসংখ্য বলয়ের মতো খণ্ডকে (metameres) বিভক্ত থাকে, তাই একে অ্যানেলিডা বা অঙ্গুরীমাল বলা হয়।',
    },
    {
        "id": 'BIO-AK-037',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Aquatic annelids like Nereis possess lateral appendages which help in swimming, known as:',
        "bn": 'নেরিসের (Nereis) মতো জলজ অ্যানেলিডায় সাঁতার কাটার জন্য যে পার্শ্বীয় উপাঙ্গ থাকে তাকে কী বলে?',
        "opts": {
            "en": ['Parapodia', 'Setae only', 'Tentacles', 'Radula'],
            "bn": ['প্যারাপোডিয়া (Parapodia)', 'কেবলমাত্র সিটা', 'কর্ষিকা', 'রেডুলা']
        },
        "correct": 0,
        "expl_en": 'Aquatic annelids like Nereis possess lateral unjointed flattened appendages called parapodia, which help in swimming.',
        "expl_bn": 'নেরিসের দেহের দুপাশে চ্যাপ্টা মাংসল উপাঙ্গ থাকে যাদের প্যারাপোডিয়া (Parapodia) বলে; এগুলি সাঁতারে সহায়তা করে।',
    },
    {
        "id": 'BIO-AK-038',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'The excretory organs of Annelids that also perform osmoregulation are called:',
        "bn": 'অ্যানেলিডার রেচন অঙ্গ যা অভিস্রবণ নিয়ন্ত্রণেও অংশ নেয় তাকে কী বলে?',
        "opts": {
            "en": ['Nephridia', 'Flame cells', 'Malpighian tubules', 'Proboscis gland'],
            "bn": ['নেফ্রিডিয়া (Nephridia)', 'শিখা কোষ', 'ম্যালপিজিয়ান নালিকা', 'প্রোবোসিস গ্রন্থি']
        },
        "correct": 0,
        "expl_en": 'Nephridia (sing. nephridium) help in osmoregulation and excretion in annelids.',
        "expl_bn": 'অ্যানেলিডার কুণ্ডলীকৃত রেচন অঙ্গকে নেফ্রিডিয়া (Nephridia) বলে যা বর্জ্য নিষ্কাশন ও জলের ভারসাম্য রক্ষা করে।',
    },
    {
        "id": 'BIO-AK-039',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Which of the following annelids is dioecious (unisexual), whereas earthworms and leeches are monoecious (hermaphrodites)?',
        "bn": 'নিচের কোন অ্যানেলিডটি একলিঙ্গ (dioecious), যেখানে কেঁচো ও জোঁক হলো উভলিঙ্গ (monoecious)?',
        "opts": {
            "en": ['Nereis', 'Pheretima (Earthworm)', 'Hirudinaria (Leech)', 'Lumbricus'],
            "bn": ['নেরিস (Nereis)', 'ফেরেটিমা বা কেঁচো', 'হিরুডিনারিয়া বা জোঁক', 'ল্যামব্রিকাস']
        },
        "correct": 0,
        "expl_en": 'Nereis, an aquatic form, is dioecious, but earthworms and leeches are monoecious.',
        "expl_bn": 'নেরিস (Nereis) হলো একলিঙ্গ প্রাণী (পুরুষ ও স্ত্রী পৃথক), কিন্তু কেঁচো ও জোঁক উভয়লিঙ্গ।',
    },
    {
        "id": 'BIO-AK-040',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which is the LARGEST phylum of Animalia which includes insects and accounts for over two-thirds of all named species on earth?',
        "bn": 'প্রাণীজগতের সর্ববৃহৎ পর্ব কোনটি যাতে পতঙ্গ অন্তর্ভুক্ত এবং যা পৃথিবীর মোট নামাঙ্কিত প্রাণীর দুই-তৃতীয়াংশের বেশি অংশ জুড়ে রয়েছে?',
        "opts": {
            "en": ['Arthropoda', 'Mollusca', 'Chordata', 'Protozoa'],
            "bn": ['আর্থ্রোপোডা বা সন্ধিপদ (Arthropoda)', 'মোলাস্কা', 'কর্ডাটা', 'প্রোটোজোয়া']
        },
        "correct": 0,
        "expl_en": 'This is the largest phylum of Animalia which includes insects. Over two-thirds of all named species on earth are arthropods.',
        "expl_bn": 'আর্থ্রোপোডা বা সন্ধিপদ পর্ব হলো প্রাণীজগতের বৃহত্তম পর্ব, যেখানে দুই-তৃতীয়াংশের বেশি প্রাণী প্রজাতি অবস্থান করে।',
    },
    {
        "id": 'BIO-AK-041',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'The body of arthropods is covered by a tough, protective exoskeleton made of:',
        "bn": 'আর্থ্রোপোডার সমগ্র দেহ কী দ্বারা গঠিত একটি শক্ত প্রতিরক্ষামূলক বহিঃকঙ্কাল দ্বারা আবৃত থাকে?',
        "opts": {
            "en": ['Chitin (a polymer of N-acetylglucosamine)', 'Calcium carbonate', 'Silica', 'Spongin'],
            "bn": ['কাইটিন বা কাইটিনাস বহিঃকঙ্কাল (Chitin)', 'ক্যালসিয়াম কার্বনেট', 'সিলিকা', 'স্পঞ্জিন']
        },
        "correct": 0,
        "expl_en": 'The body of arthropods is covered by a chitinous exoskeleton. It prevents water loss and protects internal tissues.',
        "expl_bn": 'আর্থ্রোপোডার দেহ কাইটিন নির্মিত শক্ত বহিঃকঙ্কাল দ্বারা আবৃত থাকে যা নির্দিষ্ট সময় পরপর মোচন (ecdysis) ঘটে।',
    },
    {
        "id": 'BIO-AK-042',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'The respiratory organs in arthropods vary widely across classes. Match the respiratory organs with their representative arthropods:<br>1. Book lungs — Scorpions and Spiders<br>2. Book gills — King crab (Limulus)<br>3. Tracheal system — Insects (Cockroach)<br>Which of the above pairings are correct?',
        "bn": 'আর্থ্রোপোডার বিভিন্ন শ্রেণিতে শ্বাসঅঙ্গ বিভিন্ন প্রকৃতির হয়। নিচের কোন জোড়াগুলি সঠিকভাবে মিলেছে?<br>১. বুক লাংস — বৃশ্চিক ও মাকড়সা<br>২. বুক গিলস — রাজ কাঁকড়া (Limulus)<br>৩. ট্র্যাকিয়াল তন্ত্র — পতঙ্গ (আরশোলা)',
        "opts": {
            "en": ['1, 2, and 3 (All are correct)', '1 and 3 only', '2 and 3 only', '1 and 2 only'],
            "bn": ['১, ২ এবং ৩ (সবকটিই সঠিক)', 'কেবল ১ ও ৩', 'কেবল ২ ও ৩', 'কেবল ১ ও ২']
        },
        "correct": 0,
        "expl_en": 'All three pairs are accurate NCERT examples: Respiratory organs are gills, book gills (Limulus), book lungs (scorpions/spiders) or tracheal system (insects).',
        "expl_bn": 'বুক লাংস (মাকড়সা/বৃশ্চিক), বুক গিলস (লিমুলাস) এবং ট্র্যাকিয়াল নালী (পতঙ্গ)—সবকটি তথ্যই NCERT অনুসারে সঠিক।',
    },
    {
        "id": 'BIO-AK-043',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Balancing organs or statocysts are present in which phylum?',
        "bn": 'ভারসাম্য রক্ষাকারী সংবেদী অঙ্গ স্ট্যাটোসিস্ট (Statocysts) কোন পর্বে দেখা যায়?',
        "opts": {
            "en": ['Arthropoda (e.g., in prawns)', 'Platyhelminthes', 'Aschelminthes', 'Porifera'],
            "bn": ['আর্থ্রোপোডা (যেমন চিংড়িতে)', 'প্লাটিহেলমিন্থেস', 'অ্যাসকেলমিন্থেস', 'পরিফেরা']
        },
        "correct": 0,
        "expl_en": 'Sensory organs like antennae, eyes (compound and simple), statocysts or balancing organs are present in Arthropoda.',
        "expl_bn": 'আর্থ্রোপোডার সংবেদী অঙ্গের মধ্যে অ্যান্টেনা, সরল ও পুঞ্জাক্ষি এবং ভারসাম্য রক্ষাকারী স্ট্যাটোসিস্ট উপস্থিত থাকে।',
    },
    {
        "id": 'BIO-AK-044',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Excretion in majority of terrestrial arthropods (like insects) takes place through:',
        "bn": 'অধিকাংশ স্থলজ সন্ধিপদ বা পতঙ্গের রেচন কোন অঙ্গের মাধ্যমে সম্পন্ন হয়?',
        "opts": {
            "en": ['Malpighian tubules', 'Green glands (Antennal glands in prawns)', 'Flame cells', 'Nephridia'],
            "bn": ['ম্যালপিজিয়ান নালিকা (Malpighian tubules)', 'সবুজ গ্রন্থি', 'শিখা কোষ', 'নেফ্রিডিয়া']
        },
        "correct": 0,
        "expl_en": 'Excretion in insects and many arthropods takes place through Malpighian tubules, converting nitrogenous waste into uric acid.',
        "expl_bn": 'পতঙ্গ ও স্থলজ সন্ধিপদদের প্রধান রেচন অঙ্গ হলো ম্যালপিজিয়ান নালিকা (Malpighian tubules)।',
    },
    {
        "id": 'BIO-AK-045',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": "Which of the following is a 'living fossil' arthropod?",
        "bn": "নিচের কোনটি সন্ধিপদ বা আর্থ্রোপোডার একটি বিখ্যাত 'জীবন্ত জীবাশ্ম' (Living fossil)?",
        "opts": {
            "en": ['Limulus (King crab)', 'Locusta (Locust)', 'Bombyx (Silkworm)', 'Laccifer (Lac insect)'],
            "bn": ['লিমুলাস বা রাজ কাঁকড়া (Limulus / King crab)', 'পঙ্গপাল বা লোকাস্টা', 'রেশম মথ বা বম্বিক্স', 'লাক্ষা কীট বা ল্যাসিফার']
        },
        "correct": 0,
        "expl_en": 'Limulus (King crab) is an ancient marine chelicerate that has remained virtually unchanged for over 400 million years, hence termed a living fossil.',
        "expl_bn": 'লিমুলাস (Limulus বা King crab) হলো আর্থ্রোপোডার অন্তর্ভুক্ত একটি জীবন্ত জীবাশ্ম।',
    },
    {
        "id": 'BIO-AK-046',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following is a gregarious, destructive pest belonging to Arthropoda?',
        "bn": 'আর্থ্রোপোডার অন্তর্গত কোন ক্ষতিকারক পতঙ্গটি ঝাঁক বেঁধে শস্য ধ্বংসকারী পেস্ট (gregarious pest) হিসেবে পরিচিত?',
        "opts": {
            "en": ['Locusta (Locust)', 'Apis (Honey bee)', 'Aedes (Mosquito)', 'Culex'],
            "bn": ['লোকাস্টা বা পঙ্গপাল (Locusta)', 'মৌমাছি', 'এডিস মশা', 'কিউলেক্স']
        },
        "correct": 0,
        "expl_en": 'Locusta (Locust) is a gregarious pest that migrates in billions, decimating agricultural fields.',
        "expl_bn": 'লোকাস্টা (Locusta) বা পঙ্গপাল হলো একটি মারাত্মক ঝাঁকবদ্ধ ক্ষতিকর শস্যনাশক কীট।',
    },
    {
        "id": 'BIO-AK-047',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which is the SECOND LARGEST animal phylum?',
        "bn": 'প্রাণীজগতের দ্বিতীয় বৃহত্তম (Second largest) পর্ব কোনটি?',
        "opts": {
            "en": ['Mollusca', 'Arthropoda', 'Annelida', 'Echinodermata'],
            "bn": ['মোলাস্কা বা কম্বোজ (Mollusca)', 'আর্থ্রোপোডা', 'অ্যানেলিডা', 'একাইনোডার্মাটা']
        },
        "correct": 0,
        "expl_en": 'Mollusca is the second largest animal phylum after Arthropoda.',
        "expl_bn": 'আর্থ্রোপোডার পরেই প্রাণীজগতের দ্বিতীয় বৃহত্তম পর্ব হলো মোলাস্কা (Mollusca)।',
    },
    {
        "id": 'BIO-AK-048',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'The unsegmented soft body of a mollusc is typically divided into which three regions?',
        "bn": 'মোলাস্কার অখণ্ডায়িত নরম দেহটি সাধারণত কোন তিনটি প্রধান অঞ্চলে বিভক্ত থাকে?',
        "opts": {
            "en": ['Head, muscular foot, and visceral hump', 'Head, thorax, and abdomen', 'Proboscis, collar, and trunk', 'Cephalothorax, abdomen, and telson'],
            "bn": ['মস্তক (Head), পেশিবহুল পদ (Muscular foot) এবং ভিসেরাল কুঁজ (Visceral hump)', 'মস্তক, বক্ষ এবং উদর', 'প্রোবোসিস, কলার এবং ধড়', 'শিরোবক্ষ, উদর এবং টেলসন']
        },
        "correct": 0,
        "expl_en": 'Body of molluscs is covered by a calcareous shell and is unsegmented with a distinct head, muscular foot and visceral hump.',
        "expl_bn": 'মোলাস্কার দেহটি সুস্পষ্ট মস্তক, অঙ্কীয় পেশিবহুল পদ এবং পৃষ্ঠীয় ভিসেরাল কুঁজে (visceral hump) বিভক্ত থাকে।',
    },
    {
        "id": 'BIO-AK-049',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In molluscs, a soft and spongy layer of skin forms a mantle over the visceral hump. The space between the hump and the mantle is called the ________, in which ________ are present.',
        "bn": 'মোলাস্কায় ভিসেরাল কুঁজের ওপর ত্বক একটি নরম আস্তরণ বা ম্যান্টল গঠন করে। কুঁজ ও ম্যান্টলের মধ্যবর্তী স্থানকে ________ বলে, যাতে পালকের মতো ________ অবস্থিত।',
        "opts": {
            "en": ['Mantle cavity; feather-like gills (ctenidia)', 'Pseudocoelom; flame cells', 'Haemocoel; green glands', 'Spongocoel; choanocytes'],
            "bn": ['ম্যান্টল গহ্বর (Mantle cavity); পালকসদৃশ ফুলকা বা টেনিডিয়া (ctenidia)', 'সিউডোসিলোম; শিখা কোষ', 'হিমোসিল; সবুজ গ্রন্থি', 'স্পঞ্জোসিল; কোয়ানোসাইট']
        },
        "correct": 0,
        "expl_en": 'The space between the hump and the mantle is called the mantle cavity in which feather-like gills are present. They have respiratory and excretory functions.',
        "expl_bn": 'ভিসেরাল কুঁজ ও ম্যান্টলের মধ্যবর্তী ম্যান্টল গহ্বরে পালকাকৃতি ফুলকা বা টেনিডিয়া থাকে যা শ্বাসকার্য ও রেচনে অংশ নেয়।',
    },
    {
        "id": 'BIO-AK-050',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'The file-like rasping organ present in the mouth of molluscs used for feeding is called the:',
        "bn": 'মোলাস্কার মুখবিবরে অবস্থিত খাদ্য চর্বনকারী করাত বা রেতির মতো অঙ্গকে কী বলে?',
        "opts": {
            "en": ['Radula', 'Parapodia', 'Statocyst', 'Trochophore'],
            "bn": ['রেডুলা (Radula)', 'প্যারাপোডিয়া', 'স্ট্যাটোসিস্ট', 'ট্রোকোফোর']
        },
        "correct": 0,
        "expl_en": 'The mouth contains a file-like rasping organ for feeding, called radula, bearing transverse rows of chitinous teeth.',
        "expl_bn": 'মোলাস্কার মুখে কাইটিনের সূক্ষ্ম দাঁতযুক্ত রেতির মতো খাদ্য চূর্ণকারী অঙ্গ থাকে যাকে রেডুলা (Radula) বলে।',
    },
    {
        "id": 'BIO-AK-051',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": "Which of the following molluscs completely lacks a shell and is commonly called the 'Devil fish'?",
        "bn": "নিচের কোন মোলাস্কায় কোনো খোলক থাকে না এবং একে সাধারণভাবে 'ডেভিল ফিশ' (Devil fish) বলা হয়?",
        "opts": {
            "en": ['Octopus', 'Sepia (Cuttlefish)', 'Loligo (Squid)', 'Aplysia (Sea hare)'],
            "bn": ['অক্টোপাস (Octopus)', 'সেপিয়া বা কাটলফিশ', 'ললিগো বা স্কুইড', 'অ্যাপ্লাইসিয়া বা সি-হেয়ার']
        },
        "correct": 0,
        "expl_en": 'Octopus completely lacks an external or internal shell and is commonly called the devil fish.',
        "expl_bn": 'অক্টোপাসকে সাধারণ ভাষায় ডেভিল ফিশ বলা হয় এবং এতে কোনো খোলক থাকে না।',
    },
    {
        "id": 'BIO-AK-052',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Pinctada is commercially cultivated for the production of:',
        "bn": 'পিঙ্কটাডা (Pinctada) বাণিজ্যিকভাবে কী উৎপাদনের জন্য চাষ করা হয়?',
        "opts": {
            "en": ['Natural Pearls (Pearl oyster)', 'Natural Silk', 'Shellac and wax', 'Iodine crystals'],
            "bn": ['প্রাকৃতিক মুক্তা (Pearl oyster)', 'প্রাকৃতিক রেশম', 'গালা ও মোম', 'আয়োডিন']
        },
        "correct": 0,
        "expl_en": 'Pinctada is the pearl oyster from which commercial natural and cultured pearls are harvested.',
        "expl_bn": 'পিঙ্কটাডা (Pinctada) হলো মুক্তা ঝিনুক যার ম্যান্টল থেকে মূল্যবান মুক্তা তৈরি হয়।',
    },
    {
        "id": 'BIO-AK-053',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Echinoderms (Phylum Echinodermata) are so named because of their:',
        "bn": 'একাইনোডার্মাটা (Echinodermata) পর্বের প্রাণীদের নামটির উৎপত্তি কিসের ওপর ভিত্তি করে হয়েছে?',
        "opts": {
            "en": ['Spiny skin (endoskeleton of calcareous ossicles)', 'Echinoid teeth in buccal cavity', 'Spiny wings on thorax', 'Naked shell with spikes'],
            "bn": ['কণ্টকযুক্ত ত্বক বা স্পাইনি স্কিন (ক্যালসিয়াম নির্মিত অস্থির অন্তকঙ্কাল)', 'মুখের ভেতর একাইনয়েড দাঁত', 'বক্ষের ওপর কাঁটাযুক্ত ডানা', 'কাঁটাযুক্ত অনাবৃত খোলক']
        },
        "correct": 0,
        "expl_en": 'These animals have an endoskeleton of calcareous ossicles and, hence, the name Echinodermata (spiny bodied).',
        "expl_bn": 'এদের দেহে চুন নির্মিত কণ্টকময় পাত বা অস্থির অন্তকঙ্কাল থাকে, তাই এদের একাইনোডার্মাটা বা কণ্টকত্কী প্রাণী বলে।',
    },
    {
        "id": 'BIO-AK-054',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'A unique developmental hallmark of Phylum Echinodermata regarding body symmetry is that:',
        "bn": 'দেহের প্রতিসাম্যের ক্ষেত্রে একাইনোডার্মাটা পর্বের অনন্য বিকাশমূলক বৈশিষ্ট্যটি কী?',
        "opts": {
            "en": ['Adults are radially symmetrical, but free-swimming larvae are bilaterally symmetrical', 'Adults are bilaterally symmetrical, but larvae are radially symmetrical', 'Both adults and larvae are strictly asymmetrical', 'Both adults and larvae have bilateral symmetry'],
            "bn": ['পূর্ণাঙ্গ প্রাণীরা অরীয় প্রতিসম (radial), কিন্তু এদের মুক্ত সাঁতারু লার্ভাগুলি দ্বিপার্শ্বীয় প্রতিসম (bilateral)', 'পূর্ণাঙ্গরা দ্বিপার্শ্বীয় প্রতিসম, কিন্তু লার্ভা অরীয় প্রতিসম', 'উভয় দশাই সম্পূর্ণ অপ্রতিসম', 'উভয় দশাই দ্বিপার্শ্বীয় প্রতিসম']
        },
        "correct": 0,
        "expl_en": 'The adult echinoderms are radially symmetrical (pentamerous radial) but larvae are bilaterally symmetrical. This proves their evolutionary descent from bilateral triploblastic ancestors.',
        "expl_bn": 'একাইনোডার্মাটার লার্ভা দ্বিপার্শ্বীয় প্রতিসম হলেও পূর্ণাঙ্গ দশায় পঞ্চ-অরীয় প্রতিসাম্য দেখা যায়। এটি একটি অত্যন্ত গুরুত্বপূর্ণ NEET প্রশ্ন।',
    },
    {
        "id": 'BIO-AK-055',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'The most distinctive, signature feature of echinoderms is the presence of a:',
        "bn": 'একাইনোডার্মাটার সর্বাধিক স্বতন্ত্র ও শনাক্তকারী বৈশিষ্ট্য হলো এদের দেহে কোন তন্ত্রের উপস্থিতি?',
        "opts": {
            "en": ['Water vascular system (Ambulacral system) with tube feet', 'Water canal system lined with choanocytes', 'Closed circulatory system with hemoglobin', 'Open haemocoel with Malpighian tubules'],
            "bn": ['নালিপদযুক্ত জলসংবহন তন্ত্র বা অ্যাম্বুল্যাক্রাল তন্ত্র (Water vascular system)', 'কোয়ানোসাইটযুক্ত নালী তন্ত্র', 'হিমোগ্লোবিনযুক্ত বদ্ধ রক্ত সংবহন', 'ম্যালপিজিয়ান নালিকাযুক্ত হিমোসিল']
        },
        "correct": 0,
        "expl_en": "The most distinctive feature of echinoderms is the presence of water vascular system (ambulacral system) which helps in locomotion, capture and transport of food and respiration. (Do not confuse with Porifera's canal system!)",
        "expl_bn": 'একাইনোডার্মাটার সবচেয়ে অনন্য বৈশিষ্ট্য হলো জল সংবহন তন্ত্র (Water vascular system) যা চলন, খাদ্য গ্রহণ ও শ্বসনে সাহায্য করে। (স্পঞ্জের ক্যানাল সিস্টেমের সাথে গুলিয়ে ফেলা যাবে না)।',
    },
    {
        "id": 'BIO-AK-056',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which major physiological system is completely ABSENT in Phylum Echinodermata?',
        "bn": 'একাইনোডার্মাটা পর্বের প্রাণীদের দেহে কোন প্রধান শারীরবৃত্তীয় তন্ত্রটি সম্পূর্ণ অনুপস্থিত থাকে?',
        "opts": {
            "en": ['Excretory system', 'Digestive system', 'Reproductive system', 'Water vascular system'],
            "bn": ['রেচন তন্ত্র বা এক্সক্রিটরি সিস্টেম (Excretory system)', 'পৌষ্টিকতন্ত্র', 'জননতন্ত্র', 'জলসংবহন তন্ত্র']
        },
        "correct": 0,
        "expl_en": 'An excretory system is absent in echinoderms; nitrogenous wastes (ammonia) diffuse out directly across the thin walls of tube feet and dermal branchiae/papulae.',
        "expl_bn": 'একাইনোডার্মাটায় কোনো নির্দিষ্ট রেচনতন্ত্র থাকে না; নালিপদ ও ত্বকের ব্র্যাঙ্কির মাধ্যমে ব্যাপন পদ্ধতিতে বর্জ্য নিষ্কাশিত হয়।',
    },
    {
        "id": 'BIO-AK-057',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In echinoderms, the mouth is located on the ________ side and the anus on the ________ side.',
        "bn": 'একাইনোডার্মাটায় মুখছিদ্রটি দেহের ________ দিকে এবং পায়ুছিদ্রটি দেহের ________ দিকে অবস্থিত।',
        "opts": {
            "en": ['Lower (ventral) side; upper (dorsal) side', 'Upper (dorsal); lower (ventral)', 'Anterior tip; posterior tip', 'Lateral; medial'],
            "bn": ['নিচের (অঙ্কীয় বা ventral) দিকে; উপরের (পৃষ্ঠীয় বা dorsal) দিকে', 'উপরের দিকে; নিচের দিকে', 'অগ্রপ্রান্তে; পশ্চাৎপ্রান্তে', 'পার্শ্বদেশে; কেন্দ্রে']
        },
        "correct": 0,
        "expl_en": 'Mouth is on the lower (ventral/oral) side and anus on the upper (dorsal/aboral) side in echinoderms.',
        "expl_bn": 'একাইনোডার্মাটায় মুখ থাকে দেহের নিচের দিকে (অঙ্কীয় তল) এবং পায়ু থাকে উপরের দিকে (পৃষ্ঠীয় তল)।',
    },
    {
        "id": 'BIO-AK-058',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": "Which of the following is commonly known as 'Sea lily'?",
        "bn": "নিচের কোন একাইনোডার্মটিকে সাধারণভাবে 'সি লিলি' (Sea lily) বলা হয়?",
        "opts": {
            "en": ['Antedon', 'Asterias (Star fish)', 'Echinus (Sea urchin)', 'Cucumaria (Sea cucumber)'],
            "bn": ['অ্যান্টিডন (Antedon)', 'অ্যাস্টেরিয়াস', 'একাইনাস', 'কুকুমারিয়া']
        },
        "correct": 0,
        "expl_en": 'Examples of Echinodermata from NCERT: Asterias (Star fish), Echinus (Sea urchin), Antedon (Sea lily), Cucumaria (Sea cucumber), Ophiura (Brittle star).',
        "expl_bn": 'Antedon-কে সি লিলি (Sea lily) বলা হয়।',
    },
    {
        "id": 'BIO-AK-059',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Hemichordates were earlier considered as a sub-phylum under Chordata. But now they are placed as a separate phylum under Non-Chordata because the structure in the collar region previously thought to be a notochord is actually a:',
        "bn": 'হெமிকর্ডাটাকে পূর্বে কর্ডাটার উপপর্ব মনে করা হতো। বর্তমানে এদের নন-কর্ডাটার পৃথক পর্ব হিসেবে গণ্য করা হয় কারণ এদের কলার অঞ্চলের যে গঠনকে নোটোকর্ড ভাবা হয়েছিল তা আসলে কী?',
        "opts": {
            "en": ['Stomochord (a hollow outgrowth of the gut roof)', 'True mesodermal notochord', 'Spinal cord', 'Ventral nerve cord'],
            "bn": ['স্টোমোকর্ড (Stomochord - গলবিলের প্রাচীর থেকে উৎপন্ন উপবৃদ্ধি)', 'প্রকৃত মেসোডার্মাল নোটোকর্ড', 'সুষুম্নাকাণ্ড', 'অঙ্কীয় স্নায়ুরজ্জু']
        },
        "correct": 0,
        "expl_en": 'Hemichordates have a rudimentary structure in the collar region called stomochord, a structure similar to notochord in location, but endodermal and hollow (a buccal diverticulum).',
        "expl_bn": 'হெமிকর্ডাটার কলার অঞ্চলে স্টোমোকর্ড (stomochord) নামক গঠন থাকে যা প্রকৃত মেসোডার্মাল নোটোকর্ড নয়, তাই এদের নন-কর্ডাটায় স্থান দেওয়া হয়েছে।',
    },
    {
        "id": 'BIO-AK-060',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'The cylindrical body of a hemichordate (like Balanoglossus) is composed of:',
        "bn": 'একটি হெமிকর্ডাটার (যেমন Balanoglossus) নলাকার দেহটি কোন তিনটি অংশে বিভক্ত?',
        "opts": {
            "en": ['Anterior proboscis, a collar, and a long trunk', 'Head, thorax, and abdomen', 'Head, muscular foot, and visceral hump', 'Holdfast, stipe, and frond'],
            "bn": ['অগ্রস্থ প্রোবোসিস (Proboscis), একটি কলার (Collar) এবং একটি দীর্ঘ ধড় (Trunk)', 'মস্তক, বক্ষ এবং উদর', 'মস্তক, পদ এবং কুঁজ', 'হোল্ডফাস্ট, স্ট্রাইপ এবং ফ্রন্ড']
        },
        "correct": 0,
        "expl_en": 'The body of hemichordates is cylindrical and is composed of an anterior proboscis, a collar and a long trunk.',
        "expl_bn": 'হெமிকর্ডাটার দেহ তিনটি অংশে বিভক্ত: অগ্রস্থ প্রোবোসিস, মধ্যবর্তী কলার এবং দীর্ঘ ধড় বা ট্রাঙ্ক।',
    },
    {
        "id": 'BIO-AK-061',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'The excretory organ in Hemichordata is the:',
        "bn": 'হெமிকর্ডাটা পর্বের প্রধান রেচন অঙ্গ কোনটি?',
        "opts": {
            "en": ['Proboscis gland (Glomerulus)', 'Nephridia', 'Malpighian tubules', 'Flame cells'],
            "bn": ['প্রোবোসিস গ্রন্থি (Proboscis gland)', 'নেফ্রিডিয়া', 'ম্যালপিজিয়ান নালিকা', 'শিখা কোষ']
        },
        "correct": 0,
        "expl_en": 'Excretory organ is proboscis gland located in the proboscis of hemichordates.',
        "expl_bn": 'হெமிকর্ডাটার প্রধান রেচন অঙ্গ হলো প্রোবোসিস অঞ্চলে অবস্থিত প্রোবোসিস গ্রন্থি (Proboscis gland)।',
    },
    {
        "id": 'BIO-AK-062',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Common examples of Hemichordata listed in NCERT are:',
        "bn": 'NCERT-তে উল্লেখিত হெமிকর্ডাটা পর্বের সাধারণ উদাহরণ কোনগুলি?',
        "opts": {
            "en": ['Balanoglossus and Saccoglossus', 'Ascidia and Salpa', 'Branchiostoma and Amphioxus', 'Petromyzon and Myxine'],
            "bn": ['ব্যালানোগ্লসাস (Balanoglossus) এবং স্যাক্কোগ্লসাস (Saccoglossus)', 'অ্যাসিডিয়া এবং সালপা', 'ব্রাঙ্কিওস্টোমা এবং অ্যাম্ফিঅক্সাস', 'পেট্রোমাইজন এবং মিক্সিন']
        },
        "correct": 0,
        "expl_en": 'Examples of Hemichordata: Balanoglossus and Saccoglossus (tongue worms / acorn worms).',
        "expl_bn": 'হெமிকর্ডাটার উদাহরণ হলো Balanoglossus এবং Saccoglossus।',
    },
    {
        "id": 'BIO-AK-063',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Which of the following sets of four fundamental characteristics fundamentally defines Phylum Chordata?',
        "bn": 'নিচের কোন চারটি মৌলিক বৈশিষ্ট্যের উপস্থিতি কর্ডাটা পর্বের প্রাণীদের অবিসংবাদিতভাবে সংজ্ঞায়িত করে?',
        "opts": {
            "en": ['Notochord, dorsal hollow nerve cord, paired pharyngeal gill slits, and post-anal tail', 'Ventral solid nerve cord, notochord, scales, and two-chambered heart', 'Stomochord, dorsal nerve cord, gills, and radula', 'Vertebral column, lungs, claws, and mammary glands'],
            "bn": ['নোটোকর্ড, পৃষ্ঠীয় ফাঁপা স্নায়ুরজ্জু, যুগ্ম গলবিলীয় ফুলকা ছিদ্র এবং পায়ু-পশ্চাৎ পুচ্ছ (Post-anal tail)', 'অঙ্কীয় নিরেট স্নায়ুরজ্জু, নোটোকর্ড, আঁশ এবং দ্বি-প্রকোষ্ঠী হৃদপিণ্ড', 'স্টোমোকর্ড, পৃষ্ঠীয় স্নায়ুরজ্জু, ফুলকা এবং রেডুলা', 'মেরুদণ্ড, ফুসফুস, নখর এবং স্তনগ্রন্থি']
        },
        "correct": 0,
        "expl_en": 'Animals belonging to phylum Chordata are fundamentally characterized by the presence of a notochord, a dorsal hollow nerve cord, paired pharyngeal gill slits, and a post-anal tail.',
        "expl_bn": 'কর্ডাটার চারটি অপরিহার্য মৌলিক বৈশিষ্ট্য: নোটোকর্ড, পৃষ্ঠীয় ফাঁপা নার্ভ কর্ড, গলবিলীয় ফুলকা ছিদ্র এবং পায়ু-পশ্চাৎ পুচ্ছ।',
    },
    {
        "id": 'BIO-AK-064',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In non-chordates, the central nervous system is:',
        "bn": 'নন-কর্ডাটা বা অমেরুদণ্ডী প্রাণীদের কেন্দ্রীয় স্নায়ুতন্ত্র কেমন প্রকৃতির হয়?',
        "opts": {
            "en": ['Ventral, solid, and double', 'Dorsal, hollow, and single', 'Lateral, hollow, and segmented', 'Completely absent in all invertebrate phyla'],
            "bn": ['অঙ্কীয় (ventral), নিরেট (solid) এবং দ্বি-রজ্জুযুক্ত (double)', 'পৃষ্ঠীয়, ফাঁপা এবং একক', 'পার্শ্বীয় ও ফাঁপা', 'সমস্ত অমেরুদণ্ডীতে সম্পূর্ণ অনুপস্থিত']
        },
        "correct": 0,
        "expl_en": 'In chordates, the CNS is dorsal, hollow, and single. In non-chordates, the CNS (when present) is ventral, solid, and double.',
        "expl_bn": 'কর্ডাটায় স্নায়ুতন্ত্র পৃষ্ঠীয়, ফাঁপা ও একক হলেও নন-কর্ডাটায় তা অঙ্কীয় (ventral), নিরেট (solid) ও যুগ্ম (double) হয়।',
    },
    {
        "id": 'BIO-AK-065',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In which subphylum of Chordata is the notochord present ONLY in the larval tail and disappears in the adult (Retrogressive metamorphosis)?',
        "bn": 'কর্ডাটার কোন উপপর্বে নোটোকর্ড কেবলমাত্র লার্ভার লেজে থাকে এবং পূর্ণাঙ্গ দশায় তা সম্পূর্ণ অবলুপ্ত হয়ে যায় (প্রতিগামী রূপান্তর)?',
        "opts": {
            "en": ['Urochordata (Tunicata, e.g., Ascidia, Salpa, Doliolum)', 'Cephalochordata (e.g., Branchiostoma)', 'Vertebrata', 'Cyclostomata'],
            "bn": ['ইউরোকর্ডাটা বা টিউনিকাটা (Urochordata - যেমন অ্যাসিডিয়া, সালপা, ডোলিওলাম)', 'সেফালোকর্ডাটা', 'ভার্টিব্রাটা', 'সাইক্লোস্টোমাটা']
        },
        "correct": 0,
        "expl_en": 'In Urochordata, notochord is present only in larval tail, whereas in Cephalochordata, it extends from head to tail region and is persistent throughout their life.',
        "expl_bn": 'ইউরোকর্ডাটায় নোটোকর্ড কেবল লার্ভার লেজে থাকে এবং রূপান্তরের সময় অবলুপ্ত হয়। উদাহরণ: Ascidia, Salpa, Doliolum।',
    },
    {
        "id": 'BIO-AK-066',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In Cephalochordata (such as Branchiostoma or Amphioxus / Lancelet), the notochord:',
        "bn": 'সেফালোকর্ডাটা (যেমন Branchiostoma বা Amphioxus)-তে নোটোকর্ড সংক্রান্ত কোন তথ্যটি সঠিক?',
        "opts": {
            "en": ['Extends from head to tail region and persists throughout life', 'Is present only in the larval tail', 'Is replaced by a bony vertebral column in adults', 'Disappears before hatching'],
            "bn": ['মাথা থেকে লেজ পর্যন্ত বিস্তৃত থাকে এবং সারাজীবন স্থায়ী হয়', 'কেবলমাত্র লার্ভার লেজে থাকে', 'পূর্ণাঙ্গ অবস্থায় অস্থিময় মেরুদণ্ড দ্বারা প্রতিস্থাপিত হয়', 'ডিম ফোটার আগেই বিলুপ্ত হয়']
        },
        "correct": 0,
        "expl_en": 'In Cephalochordata, notochord extends from head to tail region and is persistent throughout their life (e.g., Branchiostoma / Amphioxus / Lancelet).',
        "expl_bn": 'সেফালোকর্ডাটায় নোটোকর্ড মস্তক থেকে লেজ পর্যন্ত বিস্তৃত এবং সারাজীবন বিদ্যমান থাকে।',
    },
    {
        "id": 'BIO-AK-067',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": "'All vertebrates are chordates but all chordates are not vertebrates.' Why?",
        "bn": "'সমস্ত ভার্টিব্রাট বা মেরুদণ্ডী প্রাণীই কর্ডাট, কিন্তু সমস্ত কর্ডাট মেরুদণ্ডী নয়'—কেন?",
        "opts": {
            "en": ['Because in vertebrates the embryonic notochord is replaced by a cartilaginous or bony vertebral column in the adult, whereas protochordates retain a notochord without a vertebral column', 'Because protochordates possess mammary glands while vertebrates do not', 'Because non-vertebrate chordates lack hearts', 'Because vertebrates do not possess a dorsal hollow nerve cord'],
            "bn": ['কারণ ভার্টিব্রাটাতে ভ্রূণীয় নোটোকর্ড পূর্ণাঙ্গ অবস্থায় তরুণাস্থি বা অস্থিময় মেরুদণ্ড দ্বারা প্রতিস্থাপিত হয়, কিন্তু প্রোটোকর্ডাটদের কোনো মেরুদণ্ড থাকে না', 'কারণ প্রোটোকর্ডেটদের স্তনগ্রন্থি থাকে', 'কারণ অমেরুদণ্ডী কর্ডাটদের হৃদপিণ্ড থাকে না', 'কারণ ভার্টিব্রাটদের পৃষ্ঠীয় স্নায়ুরজ্জু থাকে না']
        },
        "correct": 0,
        "expl_en": 'Members of subphylum Vertebrata possess notochord during the embryonic period. The notochord is replaced by a cartilaginous or bony vertebral column in the adult. Thus all vertebrates are chordates, but all chordates (e.g., Urochordates and Cephalochordates) are not vertebrates.',
        "expl_bn": 'ভার্টিব্রাটাতে ভ্রূণের নোটোকর্ড পরবর্তীতে কশেরুকাযুক্ত মেরুদণ্ডে পরিণত হয়। কিন্তু ইউরোকর্ডাটা ও সেফালোকর্ডাটায় কোনো মেরুদণ্ড তৈরি হয় না। তাই সব ভার্টিব্রাট কর্ডাট হলেও সব কর্ডাট ভার্টিব্রাট নয়।',
    },
    {
        "id": 'BIO-AK-068',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'All living members of the Class Cyclostomata are ectoparasites on some fishes. They are characterized by having a:',
        "bn": 'সাইক্লোস্টোমাটা (Cyclostomata) শ্রেণির সকল জীবিত সদস্যরা কিছু মাছের ওপর বহিঃপরজীবী। এদের প্রধান বৈশিষ্ট্য হলো এদের কেমন মুখ থাকে?',
        "opts": {
            "en": ['Sucking and circular mouth without jaws', 'Ventral mouth with powerful dentate jaws', 'Terminal beak-like mouth with bony teeth', 'Mouth flanked by pincers'],
            "bn": ['চোয়ালবিহীন চোষক প্রকৃতির গোলাকার মুখ (Sucking and circular mouth without jaws)', 'শক্তিশালী চোয়ালযুক্ত অঙ্কীয় মুখ', 'অস্থিময় দাঁতযুক্ত চঞ্চু', 'াঁড়াশির মতো মুখ']
        },
        "correct": 0,
        "expl_en": 'Cyclostomes have an elongated body bearing 6-15 pairs of gill slits for respiration and a sucking and circular mouth without jaws (Agnatha).',
        "expl_bn": 'সাইক্লোস্টোমদের কোনো চোয়াল থাকে না (Agnatha); এদের মুখটি গোলাকার এবং চোষক প্রকৃতির হয়।',
    },
    {
        "id": 'BIO-AK-069',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Which of the following is true regarding cyclostomes like Petromyzon (Lamprey)?',
        "bn": 'পেট্রোমাইজন (ল্যাম্প্রে)-এর মতো সাইক্লোস্টোমদের ক্ষেত্রে নিচের কোন তথ্যটি সত্য?',
        "opts": {
            "en": ['They are marine, but migrate for spawning to fresh water; after spawning, within a few days, they die, and their larvae return to the ocean after metamorphosis', 'They live in freshwater and migrate to the sea for spawning (Catadromous)', 'They retain paired pectoral and pelvic fins with bony scales', 'Their cranium and vertebral column are made of dense calcium carbonate bone'],
            "bn": ['এরা সামুদ্রিক, কিন্তু ডিম পাড়ার জন্য নদীতে যায় (Anadromous); ডিম পাড়ার কয়েকদিনের মধ্যেই মারা যায় এবং লার্ভা রূপান্তরের পর সমুদ্রে ফিরে আসে', 'এরা নদীতে বাস করে এবং ডিম পাড়তে সমুদ্রে যায়', 'এদের যুগ্ম পাখনা ও অস্থিময় আঁশ থাকে', 'এদের খুলি ও কশেরুকা শক্ত অস্থি নির্মিত']
        },
        "correct": 0,
        "expl_en": 'Cyclostomes are marine but migrate for spawning to fresh water (anadromous migration). After spawning, within a few days, they die. Their ammocoetes larvae, after metamorphosis, return to the ocean.',
        "expl_bn": 'ল্যাম্প্রে সামুদ্রিক হলেও ডিম পাড়তে নদীতে যায়। ডিম পাড়ার পর পূর্ণাঙ্গ প্রাণী মারা যায় এবং অ্যামোসিট লার্ভা রূপান্তরের পর পুনরায় সমুদ্রে ফিরে আসে।',
    },
    {
        "id": 'BIO-AK-070',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Myxine is commonly known as the:',
        "bn": 'মিক্সিন (Myxine)-কে সাধারণ ভাষায় কী নামে ডাকা হয়?',
        "opts": {
            "en": ['Hagfish', 'Lamprey', 'Dogfish', 'Sawfish'],
            "bn": ['হ্যাগফিশ (Hagfish)', 'ল্যাম্প্রে', 'ডগফিশ', 'স-ফিশ']
        },
        "correct": 0,
        "expl_en": 'Examples of Cyclostomata: Petromyzon (Lamprey) and Myxine (Hagfish).',
        "expl_bn": 'Myxine-কে সাধারণভাবে হ্যাগফিশ (Hagfish) বলা হয়।',
    },
    {
        "id": 'BIO-AK-071',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Why do cartilaginous fishes (Chondrichthyes) have to swim constantly without rest?',
        "bn": 'তরুণাস্থিময় মাছদের (Chondrichthyes) কেন বিশ্রাম না নিয়ে একটানা সাঁতার কেটে চলতে হয়?',
        "opts": {
            "en": ['Due to the absence of an air bladder, they have to swim constantly to avoid sinking', 'Because their gills only function when water is forced by swimming at top speed', 'Because they lack a heart to pump blood automatically', 'Because their fins are fused to their skull'],
            "bn": ['দেহে পটকা বা এয়ার ব্লাডার না থাকার কারণে জলে ডুবে যাওয়া রোধ করতে এদের অবিরাম সাঁতার কাটতে হয়', 'কারণ তীব্র গতিতে সাঁতার না কাটলে ফুলকা দিয়ে জল প্রবাহিত হয় না', 'কারণ এদের হৃদপিণ্ড রক্ত পাম্প করতে পারে না', 'কারণ এদের পাখনা খুলির সাথে যুক্ত']
        },
        "correct": 0,
        "expl_en": 'Due to the absence of air bladder, members of Chondrichthyes have to swim constantly to avoid sinking to the ocean floor.',
        "expl_bn": 'তরুণাস্থিময় মাছের (যেমন হাঙ্গর) দেহে বায়ুথলি বা পটকা (air bladder) না থাকার কারণে প্লবতা নিয়ন্ত্রণ করতে পারে না, তাই ডুবে যাওয়া থেকে বাঁচতে এদের অবিরত সাঁতার কাটতে হয়।',
    },
    {
        "id": 'BIO-AK-072',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'The skin of cartilaginous fishes (Chondrichthyes) is tough, containing minute placoid scales. Their teeth are:',
        "bn": 'তরুণাস্থিময় মাছের ত্বক শক্ত এবং আণুবীক্ষণিক প্লাকয়েড আঁশযুক্ত। এদের দাঁতগুলি মূলত কী?',
        "opts": {
            "en": ['Modified placoid scales which are backwardly directed', 'Enamel-less bony projections from the mandible', 'Ctenoid plates fused to the premaxilla', 'Keratinized epidermal combs'],
            "bn": ['রূপান্তরিত প্লাকয়েড আঁশ যা পেছনের দিকে বাঁকানো থাকে', 'এনামেলহীন চোয়ালের অস্থি', 'টিনয়েড প্লেট', 'কেরাটিন নির্মিত এপিডার্মাল চিরুনি']
        },
        "correct": 0,
        "expl_en": 'Teeth in Chondrichthyes are modified placoid scales which are backwardly directed. Their jaws are very powerful and predaceous.',
        "expl_bn": 'হাঙ্গরের দাঁতগুলি প্রকৃতপক্ষে পেছনের দিকে বাঁকানো রূপান্তরিত প্লাকয়েড আঁশ (placoid scales)।',
    },
    {
        "id": 'BIO-AK-073',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which cartilaginous fish possesses an electric organ capable of delivering electric shocks, and which possesses a poison sting?',
        "bn": 'কোন তরুণাস্থিময় মাছে বিদ্যুৎ অঙ্গ (electric organ) এবং কোনটিতে বিষাক্ত কাঁটা (poison sting) থাকে?',
        "opts": {
            "en": ['Torpedo (Electric ray); Trygon (Sting ray)', 'Trygon; Torpedo', 'Scoliodon; Pristis', 'Pristis; Carcharodon'],
            "bn": ['টরপেডো (Torpedo - বিদ্যুৎ অঙ্গ); ট্রাইগন (Trygon - বিষাক্ত কাঁটা)', 'ট্রাইগন; টরপেডো', 'স্কোলিওডন; প্রিস্টিস', 'প্রিস্টিস; কার্কারোডন']
        },
        "correct": 0,
        "expl_en": 'Some cartilaginous fishes possess electric organs (e.g., Torpedo) and some possess poison stings (e.g., Trygon).',
        "expl_bn": 'Torpedo মাছে বিদ্যুৎ অঙ্গ থাকে এবং Trygon মাছে লেজে বিষাক্ত কাঁটা (sting) থাকে।',
    },
    {
        "id": 'BIO-AK-074',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In male cartilaginous fishes (Chondrichthyes), copulatory organs called claspers are borne on the:',
        "bn": 'পুরুষ তরুণাস্থিময় মাছে সঙ্গমে সহায়তাকারী ক্লাস্পার (Claspers) কোন পাখনার ওপর অবস্থিত?',
        "opts": {
            "en": ['Pelvic fins', 'Pectoral fins', 'Dorsal fin', 'Caudal fin'],
            "bn": ['শ্রোণী পাখনা বা পেলভিক পাখনা (Pelvic fins)', 'বক্ষ পাখনা বা পেক্টোরাল পাখনা', 'পৃষ্ঠ পাখনা', 'পুচ্ছ পাখনা']
        },
        "correct": 0,
        "expl_en": 'In Chondrichthyes, in males pelvic fins bear claspers used for internal fertilization.',
        "expl_bn": 'পুরুষ হাঙ্গরের পেলভিক বা শ্রোণী পাখনার ভেতরের প্রান্তে ক্লাস্পার (claspers) নামক বিশেষ সঙ্গম অঙ্গ থাকে।',
    },
    {
        "id": 'BIO-AK-075',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Which of the following sets of features characterizes Bony fishes (Osteichthyes)?',
        "bn": 'নিচের কোন বৈশিষ্ট্যগুচ্ছটি অস্থিময় মাছদের (Osteichthyes) নির্ভুলভাবে শনাক্ত করে?',
        "opts": {
            "en": ['Bony endoskeleton, terminal mouth, 4 pairs of gills covered by operculum, cycloid/ctenoid scales, and air bladder present', 'Cartilaginous skeleton, ventral mouth, 5-7 pairs of naked gill slits, placoid scales, and air bladder absent', 'Jawless sucking mouth, 6-15 pairs of gill slits, scaleless body', 'Moist scaleless skin, 3-chambered heart, cloaca present'],
            "bn": ['অস্থিময় অন্তকঙ্কাল, প্রান্তীয় মুখছিদ্র, কানকো (অপারকুলাম) দ্বারা ঢাকা ৪ জোড়া ফুলকা, সাইক্লয়েড/টিনয়েড আঁশ এবং পটকা বা এয়ার ব্লাডার বর্তমান', 'তরুণাস্থিময় কঙ্কাল, অঙ্কীয় মুখ, কানকোহীন ফুলকা, প্লাকয়েড আঁশ', 'চোয়ালহীন মুখ, আঁশহীন দেহ', 'আঁশবিহীন ভেজা ত্বক, ৩-প্রকোষ্ঠী হৃদপিণ্ড']
        },
        "correct": 0,
        "expl_en": 'Osteichthyes have a bony endoskeleton, mostly terminal mouth, four pairs of gills covered by an operculum on each side, skin with cycloid/ctenoid scales, and an air bladder for buoyancy.',
        "expl_bn": 'অস্থিময় মাছের অগ্রভাগে মুখ, কানকোযুক্ত ৪ জোড়া ফুলকা, সাইক্লয়েড বা টিনয়েড আঁশ এবং প্লবতা নিয়ন্ত্রণকারী পটকা থাকে।',
    },
    {
        "id": 'BIO-AK-076',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following is a marine bony fish showing male parental care with a brood pouch?',
        "bn": 'নিচের কোন সামুদ্রিক অস্থিময় মাছটিতে পুরুষ দেহে ব্রুড পাউচ (বাচ্চা ধারণের থলি) থাকার মাধ্যমে অপত্য লালন পরিলক্ষিত হয়?',
        "opts": {
            "en": ['Hippocampus (Sea horse)', 'Exocoetus (Flying fish)', 'Betta (Fighting fish)', 'Labeo (Rohu)'],
            "bn": ['হিপ্পোক্যাম্পাস বা সিন্ধুঘোটক (Hippocampus / Sea horse)', 'এক্সোসিয়েটাস বা উড়ুক্কু মাছ', 'বেট্টা', 'রুই মাছ']
        },
        "correct": 0,
        "expl_en": 'Hippocampus (Sea horse) is a marine bony fish in which the male possesses a brood pouch on its abdomen to carry eggs until hatching.',
        "expl_bn": 'হিপ্পোক্যাম্পাস বা সি-হর্স মাছের পুরুষটির পেটে ব্রুড পাউচ থাকে যেখানে ডিম ফুটে বাচ্চা বের হওয়া পর্যন্ত সে তা বহন করে।',
    },
    {
        "id": 'BIO-AK-077',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following is an aquarium bony fish?',
        "bn": 'নিচের কোনটি অ্যাকোয়ারিয়ামে পোষা রঙিন অস্থিময় মাছের উদাহরণ?',
        "opts": {
            "en": ['Betta (Fighting fish) and Pterophyllum (Angel fish)', 'Scoliodon and Pristis', 'Clarias and Catla', 'Exocoetus and Hippocampus'],
            "bn": ['বেট্টা বা ফাইটিং ফিশ এবং টেরোফাইলাম বা অ্যাঞ্জেল ফিশ', 'স্কোলিওডন এবং প্রিস্টিস', 'মাগুর এবং কাতলা', 'উড়ুক্কু মাছ এবং সি-হর্স']
        },
        "correct": 0,
        "expl_en": 'Aquarium fishes listed in NCERT: Betta (Fighting fish) and Pterophyllum (Angel fish).',
        "expl_bn": 'NCERT-তে অ্যাকোয়ারিয়ামের মাছ হিসেবে Betta (ফাইটিং ফিশ) এবং Pterophyllum (অ্যাঞ্জেল ফিশ)-এর উল্লেখ রয়েছে।',
    },
    {
        "id": 'BIO-AK-078',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'The name Amphibia (Greek, amphi: dual, bios: life) indicates that amphibians can:',
        "bn": 'অ্যাম্ফিবিয়া বা উভচর (গ্রিক amphi: দ্বৈত, bios: জীবন) নামটি দ্বারা কী বোঝানো হয়?',
        "opts": {
            "en": ['Live in aquatic as well as terrestrial habitats', 'Fly in air and swim in deep sea', 'Breathe only through gills in adult life', 'Survive without food and water for 50 years'],
            "bn": ['জলে এবং ডাঙায় উভয় পরিবেশে বসবাস করতে পারে', 'আকাশে উড়তে ও গভীর সমুদ্রে ডুব দিতে পারে', 'পূর্ণাঙ্গ জীবনে কেবল ফুলকা দিয়ে শ্বাস নেয়', 'খাদ্য ও জল ছাড়া ৫০ বছর বাঁচতে পারে']
        },
        "correct": 0,
        "expl_en": 'As the name indicates (Amphi: dual, bios: life), amphibians can live in aquatic as well as terrestrial habitats.',
        "expl_bn": 'উভচর প্রাণীরা তাদের জীবনচক্রে জল ও স্থল উভয় পরিবেশের ওপর নির্ভরশীল হওয়ায় এদের অ্যাম্ফিবিয়া বলা হয়।',
    },
    {
        "id": 'BIO-AK-079',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In amphibians, the alimentary canal, urinary and reproductive tracts open into a common posterior chamber called the:',
        "bn": 'উভচর প্রাণীদের পৌষ্টিকনালী, মূত্রনালী এবং জনননালী একটি সাধারণ প্রকোষ্ঠে উন্মুক্ত হয়, তাকে কী বলে?',
        "opts": {
            "en": ['Cloaca', 'Tympanum', 'Operculum', 'Coelom'],
            "bn": ['ক্লোয়াকা বা অবসারণী (Cloaca)', 'টিম্প্যানাম', 'অপারকুলাম', 'সিলোম']
        },
        "correct": 0,
        "expl_en": 'The alimentary canal, urinary and reproductive tracts open into a common chamber called cloaca which opens to the exterior in amphibians.',
        "expl_bn": 'উভচরদের মলমূত্র ও জননকোষ একটি অভিন্ন প্রকোষ্ঠ ক্লোয়াকা (Cloaca) বা অবসারণীতে এসে জমা হয় এবং তা বাইরে উন্মুক্ত হয়।',
    },
    {
        "id": 'BIO-AK-080',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following is a LIMBLESS amphibian?',
        "bn": 'নিচের কোনটি পদহীন উভচর (Limbless amphibian)-এর উদাহরণ?',
        "opts": {
            "en": ['Ichthyophis', 'Salamandra', 'Hyla (Tree frog)', 'Bufo (Toad)'],
            "bn": ['ইকথিয়োফিস (Ichthyophis)', 'সালামান্ডার', 'হাইলা বা গেছো ব্যাঙ', 'বুফো বা কুনোব্যাঙ']
        },
        "correct": 0,
        "expl_en": 'Ichthyophis is a blind, burrowing limbless amphibian (Gymnophiona / Apoda).',
        "expl_bn": 'ইকথিয়োফিস (Ichthyophis) হলো একটি পদহীন অন্ধ উভচর প্রাণী।',
    },
    {
        "id": 'BIO-AK-081',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'The heart in amphibians is:',
        "bn": 'উভচর বা অ্যাম্ফিবিয়া শ্রেণির প্রাণীদের হৃদপিণ্ড কেমন প্রকৃতির হয়?',
        "opts": {
            "en": ['Three-chambered (two auricles and one ventricle)', 'Two-chambered (one auricle and one ventricle)', 'Four-chambered (two auricles and two ventricles)', 'Single-chambered tubular contractile vessel'],
            "bn": ['তিন-প্রকোষ্ঠী (দুটি অলিন্দ এবং একটি নিলয়)', 'দ্বি-প্রকোষ্ঠী (একটি অলিন্দ ও একটি নিলয়)', 'চার-প্রকোষ্ঠী (দুটি অলিন্দ ও দুটি নিলয়)', 'একক প্রকোষ্ঠযুক্ত']
        },
        "correct": 0,
        "expl_en": 'The heart in amphibians is three-chambered with two auricles and one ventricle, causing mixing of oxygenated and deoxygenated blood in the ventricle.',
        "expl_bn": 'উভচরদের হৃদপিণ্ড তিন প্রকোষ্ঠযুক্ত: দুটি অলিন্দ এবং একটি অভিন্ন নিলয়।',
    },
    {
        "id": 'BIO-AK-082',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Class Reptilia refers to their characteristic mode of locomotion, which is:',
        "bn": 'রেপটিলিয়া (Reptilia বা সরীসৃপ) নামটি এদের কোন ধরনের স্বভাব বা চলন রীতির পরিচায়ক?',
        "opts": {
            "en": ['Creeping or crawling locomotion (Latin, repere or reptum: to creep or crawl)', 'Flying by skin flaps', 'Hopping on powerful hindlegs', 'Jet propulsion through siphons'],
            "bn": ['বুকে হেঁটে বা বুকে ভর দিয়ে চলা বা ক্রলিং (Latin, repere: বুকে হাঁটা)', 'ত্বকের সাহায্যে ওড়া', 'লাফিয়ে চলা', 'জেট প্রপালশন']
        },
        "correct": 0,
        "expl_en": 'The class name refers to their creeping or crawling mode of locomotion (Latin, repere or reptum, to creep or crawl).',
        "expl_bn": 'ল্যাটিন repere শব্দের অর্থ বুকে হেঁটে চলা; সরীসৃপদের প্রধান বৈশিষ্ট্য হলো এরা বুকে ভর দিয়ে হামাগুড়ি দিয়ে চলে।',
    },
    {
        "id": 'BIO-AK-083',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'The heart in reptiles is usually three-chambered, but is distinctively FOUR-CHAMBERED in:',
        "bn": 'সরীসৃপদের হৃদপিণ্ড সাধারণত অসম্পূর্ণ তিন-প্রকোষ্ঠী হলেও কার ক্ষেত্রে তা সুস্পষ্ট চার-প্রকোষ্ঠী (Four-chambered)?',
        "opts": {
            "en": ['Crocodiles (Crocodilus and Alligator)', 'Chameleon and Calotes', 'Naja (Cobra) and Vipera', 'Chelone (Turtle) and Testudo'],
            "bn": ['কুমির বা ক্রোকোডাইল (Crocodiles)', 'গিরগিটি এবং রক্তচোষা', 'কেউটে এবং গোখরো', 'কচ্ছপ']
        },
        "correct": 0,
        "expl_en": 'Heart is usually three-chambered in reptiles, but four-chambered in crocodiles (possessing two complete auricles and two complete ventricles).',
        "expl_bn": 'সরীসৃপদের মধ্যে কুমিরের (Crocodiles) হৃদপিণ্ড সম্পূর্ণভাবে চার প্রকোষ্ঠ বিশিষ্ট (দুটি অলিন্দ ও দুটি নিলয়)।',
    },
    {
        "id": 'BIO-AK-084',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Snakes and lizards shed their scales as skin cast. The skin of reptiles is characteristically:',
        "bn": 'সাপ এবং টিকটিকি খোলস ত্যাগের মাধ্যমে আঁশ পরিবর্তন করে। সরীসৃপদের ত্বকের মূল বৈশিষ্ট্য কী?',
        "opts": {
            "en": ['Dry and cornified, covered by epidermal scales or scutes', 'Moist and glandular without scales', 'Covered with placoid teeth and slime pores', 'Ciliated and highly vascularized with no keratin'],
            "bn": ['শুষ্ক ও শৃঙ্গায়িত (dry and cornified) এবং এপিডার্মাল আঁশ বা স্কুট দ্বারা আবৃত', 'ভেজা ও গ্রন্থিময়', 'প্লাকয়েড আঁশযুক্ত', 'সিলিয়াযুক্ত']
        },
        "correct": 0,
        "expl_en": 'Their body is covered by dry and cornified skin, epidermal scales or scutes. Tympanum represents ear.',
        "expl_bn": 'সরীসৃপের ত্বক শুষ্ক, গ্রন্থিহীন এবং কেরাটিনযুক্ত শক্ত এপিডার্মাল আঁশ বা স্কুট (scutes) দ্বারা আবৃত থাকে।',
    },
    {
        "id": 'BIO-AK-085',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following is a flightless bird?',
        "bn": 'নিচের কোনটি উড্ডয়নহীন পাখি (Flightless bird)?',
        "opts": {
            "en": ['Struthio (Ostrich)', 'Columba (Pigeon)', 'Corvus (Crow)', 'Psittacula (Parrot)'],
            "bn": ['স্ট্রুথিও বা উটপাখি (Struthio / Ostrich)', 'পায়রা', 'কাক', 'টিয়া']
        },
        "correct": 0,
        "expl_en": 'The characteristic features of Aves (birds) are the presence of feathers and most of them can fly except flightless birds like Struthio (Ostrich).',
        "expl_bn": 'উটপাখি বা অস্ট্রিচ (Struthio) হলো উড়তে অক্ষম দৌড়বাজ পাখি।',
    },
    {
        "id": 'BIO-AK-086',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'The long bones of birds (Aves) are hollow with air cavities to reduce body weight for flight. Such bones are called:',
        "bn": 'পাখিদের ওড়ার সুবিধার্থে দেহের ওজন কমানোর জন্য তাদের দীর্ঘ অস্থিগুলি ফাঁপা ও বায়ুগহ্বরযুক্ত হয়। এই ধরনের অস্থিকে কী বলে?',
        "opts": {
            "en": ['Pneumatic bones', 'Sesamoid bones', 'Compact haversian bones', 'Cartilaginous epiphyses'],
            "bn": ['নিউম্যাটিক অস্থি বা বায়বীয় অস্থি (Pneumatic bones)', 'সিসাময়েড অস্থি', 'হ্যাভারশিয়ান অস্থি', 'তরুণাস্থি']
        },
        "correct": 0,
        "expl_en": 'Endoskeleton of birds is fully ossified (bony) and the long bones are hollow with air cavities (pneumatic) to minimize weight during flight.',
        "expl_bn": 'পাখিদের ওড়ার অভিযোজন হিসেবে তাদের অস্থিগুলি ভেতর থেকে ফাঁপা ও বায়ুগহ্বরযুক্ত হয়, এদের নিউম্যাটিক অস্থি (pneumatic bones) বলে।',
    },
    {
        "id": 'BIO-AK-087',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In birds, the skin is completely dry without glands EXCEPT for which gland located at the base of the tail?',
        "bn": 'পাখিদের সম্পূর্ণ ত্বক গ্রন্থিহীন ও শুষ্ক, কেবলমাত্র লেজের গোড়ায় কোন গ্রন্থিটি উপস্থিত থাকে?',
        "opts": {
            "en": ['Oil gland (Uropygial or preen gland)', 'Sweat gland', 'Sebaceous gland', 'Mammary gland'],
            "bn": ['তৈল গ্রন্থি বা প্রীন গ্রন্থি (Oil / Preen gland)', 'ঘর্মগ্রন্থি', 'সিবেসিয়াস গ্রন্থি', 'স্তনগ্রন্থি']
        },
        "correct": 0,
        "expl_en": 'Skin of birds is dry without glands except the oil gland (preen gland) at the base of the tail used for preening and waterproofing feathers.',
        "expl_bn": 'পাখির ত্বকে কোনো গ্রন্থি থাকে না, কেবল লেজের গোড়ায় ইউরোপাইজিয়াল বা প্রীন গ্রন্থি (oil gland) থাকে যার তেল পাখি ঠোঁট দিয়ে পালকে মাখিয়ে জলরোধী করে।',
    },
    {
        "id": 'BIO-AK-088',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'The digestive tract of birds possesses which two additional specialized chambers?',
        "bn": 'পাখিদের পৌষ্টিকনালীতে খাদ্য সাময়িক সঞ্চয় ও পেষাইয়ের জন্য কোন দুটি অতিরিক্ত প্রকোষ্ঠ থাকে?',
        "opts": {
            "en": ['Crop and Gizzard', 'Rumen and Reticulum', 'Caecum and Vermiform appendix', 'Cardia and Pylorus'],
            "bn": ['ক্রপ (Crop) এবং গিজার্ড (Gizzard)', 'রুমেন ও রেটিকুলাম', 'সিকাম ও অ্যাপেন্ডিক্স', 'কার্ডিয়া ও পাইলোরাস']
        },
        "correct": 0,
        "expl_en": 'The digestive tract of birds has additional chambers, the crop (for food storage and softening) and gizzard (muscular grinding chamber with grit).',
        "expl_bn": 'পাখির কোনো দাঁত থাকে না, তাই খাদ্য সঞ্চয়ের জন্য ক্রপ (crop) এবং খাদ্য পেষাইয়ের জন্য পেশিবহুল গিজার্ড (gizzard) থাকে।',
    },
    {
        "id": 'BIO-AK-089',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Organisms that are capable of maintaining a constant internal body temperature regardless of ambient environmental fluctuations are termed:',
        "bn": 'যেসব প্রাণী পরিবেশের তাপমাত্রার তারতম্য সত্ত্বেও দেহের অভ্যন্তরীণ তাপমাত্রা সর্বদা নির্দিষ্ট ও স্থির রাখতে পারে, তাদের কী বলে?',
        "opts": {
            "en": ['Homoiothermous / Warm-blooded (Aves and Mammals)', 'Poikilothermous / Cold-blooded (Fishes, Amphibians, Reptiles)', 'Stenothermal', 'Eurythermal'],
            "bn": ['হোমিওথার্মাস বা উষ্ণশোণিত প্রাণী (পাখি এবং স্তন্যপায়ী)', 'পোইকিলোথার্মাস বা শীতলশোণিত প্রাণী (মাছ, উভচর, সরীসৃপ)', 'স্টেনোথার্মাল', 'ইউরিথার্মাল']
        },
        "correct": 0,
        "expl_en": 'Birds and mammals are homoiothermous (warm-blooded) animals, i.e., they are able to maintain a constant body temperature.',
        "expl_bn": 'পাখি এবং স্তন্যপায়ী প্রাণীরা হোমিওথার্মাস বা উষ্ণশোণিত (warm-blooded) কারণ তারা দেহের তাপমাত্রা নির্দিষ্ট বজায় রাখে।',
    },
    {
        "id": 'BIO-AK-090',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'The most unique, defining mammalian characteristic which is found in no other class of vertebrates is:',
        "bn": 'স্তন্যপায়ী বা ম্যামালিয়া শ্রেণির সর্বপ্রধান অনন্য বৈশিষ্ট্য যা অন্য কোনো মেরুদণ্ডী শ্রেণিতে দেখা যায় না তা হলো:',
        "opts": {
            "en": ['Presence of milk-producing mammary glands to nourish the young ones', 'Presence of a four-chambered heart', 'Presence of lungs for breathing', 'Presence of paired eyes with eyelids'],
            "bn": ['নবজাতক শাবককে স্তন্যপান করানোর জন্য দুগ্ধ নিঃসরণকারী স্তনগ্রন্থির (Mammary glands) উপস্থিতি', 'চার-প্রকোষ্ঠী হৃদপিণ্ডের উপস্থিতি', 'শ্বাস নেওয়ার জন্য ফুসফুস', 'চোখের পাতার উপস্থিতি']
        },
        "correct": 0,
        "expl_en": 'The most unique mammalian characteristic is the presence of milk producing glands (mammary glands) by which the young ones are nourished.',
        "expl_bn": 'স্তন্যপায়ী প্রাণীর সবচেয়ে অনন্য বৈশিষ্ট্য হলো তাদের দেহে স্তনগ্রন্থির (Mammary glands) উপস্থিতি যা থেকে দুগ্ধ ক্ষরিত হয়ে শাবক পুষ্টি লাভ করে।',
    },
    {
        "id": 'BIO-AK-091',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following mammals is OVIPAROUS (egg-laying)?',
        "bn": 'নিচের কোন স্তন্যপায়ী প্রাণীটি ব্যতিক্রমীভাবে ডিম্বজ বা ডিম প্রসবকারী (Oviparous)?',
        "opts": {
            "en": ['Ornithorhynchus (Duck-billed Platypus)', 'Macropus (Kangaroo)', 'Pteropus (Flying fox)', 'Balaenoptera (Blue whale)'],
            "bn": ['অর্নিথোরিঙ্কাস বা প্লাটিপাস (Ornithorhynchus / Duck-billed Platypus)', 'ক্যাঙ্গারু', 'বাদুড়', 'নীল তিমি']
        },
        "correct": 0,
        "expl_en": 'Ornithorhynchus (Platypus) is a monotreme mammal that lays eggs (oviparous) while still suckling its hatched young with milk from mammary slits.',
        "expl_bn": 'প্লাটিপাস বা অর্নিথোরিঙ্কাস হলো একটি ডিম্বজ স্তন্যপায়ী (oviparous mammal) যা ডিম পাড়ে কিন্তু বাচ্চাকে দুধ খাওয়ায়।',
    },
    {
        "id": 'BIO-AK-092',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following is a flying mammal?',
        "bn": 'নিচের কোনটি উড়ুক্কু স্তন্যপায়ী প্রাণীর উদাহরণ?',
        "opts": {
            "en": ['Pteropus (Flying fox / Bat)', 'Exocoetus (Flying fish)', 'Draco (Flying lizard)', 'Petaurista'],
            "bn": ['টেরোপাস বা বাদুড় (Pteropus / Flying fox)', 'উড়ুক্কু মাছ', 'উড়ুক্কু গিরগিটি', 'উড়ুক্কু কাঠবিড়ালি']
        },
        "correct": 0,
        "expl_en": 'Pteropus (Flying fox / Bat) is a true mammal adapted for powered flight using skin flaps (patagium) between elongated digits.',
        "expl_bn": 'টেরোপাস (বাদুড়) হলো ডানাযুক্ত উড়তে সক্ষম স্তন্যপায়ী প্রাণী।',
    },
    {
        "id": 'BIO-AK-093',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which of the following are aquatic mammals?',
        "bn": 'নিচের কোন জোড়াটি জলজ স্তন্যপায়ী প্রাণীর সঠিক উদাহরণ?',
        "opts": {
            "en": ['Delphinus (Common dolphin) and Balaenoptera (Blue whale)', 'Scoliodon and Pristis', 'Chelone and Crocodilus', 'Hippocampus and Exocoetus'],
            "bn": ['ডলফিন (Delphinus) এবং নীল তিমি (Balaenoptera)', 'হাঙ্গর এবং করাত মাছ', 'কচ্ছপ এবং কুমির', 'সি-হর্স এবং উড়ুক্কু মাছ']
        },
        "correct": 0,
        "expl_en": 'Delphinus (Dolphin) and Balaenoptera (Blue whale) are fully aquatic, placental mammals that breathe air using lungs and give birth to live calves.',
        "expl_bn": 'ডলফিন এবং নীল তিমি হলো স্তন্যপায়ী প্রাণী; এরা মাছের মতো জলে বাস করলেও ফুসফুস দিয়ে শ্বাস নেয় এবং সরাসরি শাবক প্রসব করে।',
    },
    {
        "id": 'BIO-AK-094',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Presence of pinna (external ear), hair on skin, and heterodont dentition embedded in sockets of the jaw (thecodont) are characteristic hallmarks of:',
        "bn": 'বহিস্থ কান বা পিনা (Pinna), ত্বকে রোম এবং চোয়ালের গর্তে প্রোথিত ভিন্ন ভিন্ন প্রকৃতির দাঁত (thecodont dentition)—কোন শ্রেণির মূল বৈশিষ্ট্য?',
        "opts": {
            "en": ['Mammalia', 'Aves', 'Reptilia', 'Amphibia'],
            "bn": ['স্তন্যপায়ী বা ম্যামালিয়া (Mammalia)', 'পক্ষী বা এভিস', 'সরীসৃপ', 'উভচর']
        },
        "correct": 0,
        "expl_en": 'External ears or pinnae are present, hair is present on skin, and different types of teeth (heterodont) are present in the jaw in Class Mammalia.',
        "expl_bn": 'বহিঃকর্ণের পিনা, গায়ে লোম এবং চোয়ালের সকেটে দাঁত প্রোথিত থাকা স্তন্যপায়ী শ্রেণির বৈশিষ্ট্য।',
    },
    {
        "id": 'BIO-AK-095',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Which of the following sets of animals are all URICOTELIC, excreting nitrogenous waste as paste or pellets of uric acid to conserve water?',
        "bn": 'জল সংরক্ষণের উদ্দেশ্যে ইউরিক অ্যাসিডের পেলেট বা পেস্ট নির্গমনকারী ইউরিকোটেলিক (Uricotelic) প্রাণীদের সঠিক দল কোনটি?',
        "opts": {
            "en": ['Reptiles, Birds, Land snails, and Insects', 'Mammals, adult amphibians, and sharks', 'Aquatic bony fishes and aquatic larvae', 'Sponges, cnidarians, and planarians'],
            "bn": ['সরীসৃপ, পাখি, স্থলজ শামুক এবং পতঙ্গ', 'স্তন্যপায়ী, পূর্ণাঙ্গ ব্যাঙ এবং হাঙ্গর', 'জলজ অস্থিময় মাছ ও জলজ লার্ভা', 'স্পঞ্জ, নিডারিয়া এবং প্ল্যানেরিয়া']
        },
        "correct": 0,
        "expl_en": 'Reptiles, birds, land snails and insects excrete nitrogenous wastes as uric acid in the form of pellet or paste with minimum loss of water and are called uricotelic animals.',
        "expl_bn": 'পাখি, সরীসৃপ, পতঙ্গ এবং স্থলজ শামুক ইউরিক অ্যাসিড নির্গমন করে (Uricotelic)।',
    },
    {
        "id": 'BIO-AK-096',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which organ in cartilaginous fishes senses minute electrical fields generated by prey in water?',
        "bn": 'তরুণাস্থিময় মাছে (যেমন হাঙ্গরে) শিকারের তৈরি অতি ক্ষুদ্র বৈদ্যুতিক ক্ষেত্র শনাক্তকারী সংবেদী অঙ্গের নাম কী?',
        "opts": {
            "en": ['Ampullae of Lorenzini', 'Statocysts', 'Rhabdites', 'Ommatidia'],
            "bn": ['অ্যাম্পুলা অব লরেঞ্জিনি (Ampullae of Lorenzini)', 'স্ট্যাটোসিস্ট', 'র\u200d্যাবডাইটস', 'ওমাটিডিয়া']
        },
        "correct": 0,
        "expl_en": 'Ampullae of Lorenzini are specialized electroreceptors located on the snout of elasmobranchs (sharks and rays) that detect microvolt electric potentials of struggling prey.',
        "expl_bn": 'হাঙ্গরের থলথলে মাথায় অবস্থিত অ্যাম্পুলা অব লরেঞ্জিনি হলো শিকারের পেশি সঞ্চালনে তৈরি বৈদ্যুতিক স্পন্দন ধরার অত্যন্ত সংবেদনশীল গ্রাহক অঙ্গ।',
    },
    {
        "id": 'BIO-AK-097',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In sponges, asexual internal buds formed to tide over unfavorable conditions are called:',
        "bn": 'প্রতিকূল পরিবেশে টিকে থাকার জন্য স্পঞ্জের দেহের ভেতরে সৃষ্ট অযৌন অভ্যন্তরীণ মুকুলকে কী বলে?',
        "opts": {
            "en": ['Gemmules', 'Gemmae', 'Planula', 'Trochophore'],
            "bn": ['গেমিউল (Gemmules)', 'গেমা', 'প্ল্যানুলা', 'ট্রোকোফোর']
        },
        "correct": 0,
        "expl_en": 'Gemmules are internal asexual dormant buds produced by freshwater sponges (Spongilla) containing archaeocytes surrounded by a thick spicular coat to survive desiccation.',
        "expl_bn": 'মিষ্ট জলের স্পঞ্জে শীতকালে বা খরার হাত থেকে বাঁচতে অভ্যন্তরীণ মুকুল বা গেমিউল (Gemmule) গঠিত হয়।',
    },
    {
        "id": 'BIO-AK-098',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'A free-swimming ciliated larva of cnidarians (coelenterates) is called a:',
        "bn": 'নিডারিয়া বা সিলেন্টারেটা পর্বের প্রাণীদের মুক্ত সাঁতারু সিলিয়াযুক্ত লার্ভাকে কী বলা হয়?',
        "opts": {
            "en": ['Planula', 'Parenchymula', 'Amphiblastula', 'Trochophore'],
            "bn": ['প্ল্যানুলা (Planula)', 'প্যারেনকাইমুলা', 'অ্যাম্ফিব্লাস্টুলা', 'ট্রোকোফোর']
        },
        "correct": 0,
        "expl_en": 'The typical motile, ciliated, solid gastrula larva of cnidarians (such as Obelia and jellyfish) is the Planula larva.',
        "expl_bn": 'নিডারিয়ার সিলিয়াযুক্ত মুক্ত সাঁতারু লার্ভাকে প্ল্যানুলা (Planula) লার্ভা বলা হয়।',
    },
    {
        "id": 'BIO-AK-099',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'The larva of acorn worms (Hemichordata, e.g., Balanoglossus) is called the:',
        "bn": 'হெமிকর্ডাটা পর্বের (যেমন ব্যালানোগ্লসাস) মুক্ত সাঁতারু লার্ভাটির নাম কী?',
        "opts": {
            "en": ['Tornaria larva', 'Bipinnaria larva', 'Trochophore larva', 'Glochidium larva'],
            "bn": ['টোরনারিয়া লার্ভা (Tornaria larva)', 'বাইপিনারিয়া লার্ভা', 'ট্রোকোফোর লার্ভা', 'গ্লোচিডিয়াম']
        },
        "correct": 0,
        "expl_en": 'The free-swimming ciliated larva of Hemichordata is the Tornaria larva, structurally closely related to echinoderm bipinnaria.',
        "expl_bn": 'ব্যালানোগ্লসাসের লার্ভাকে টোরনারিয়া (Tornaria) লার্ভা বলে যা একাইনোডার্মাটার লার্ভার সাথে অত্যন্ত সাদৃশ্যপূর্ণ।',
    },
    {
        "id": 'BIO-AK-100',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Green glands (antennal glands) serve as excretory organs in:',
        "bn": 'সবুজ গ্রন্থি বা গ্রিন গ্ল্যান্ড (অ্যান্টেনাল গ্রন্থি) কার রেচন অঙ্গ হিসেবে কাজ করে?',
        "opts": {
            "en": ['Crustaceans like Prawns (Palaemon)', 'Insects like Cockroaches', 'Arachnids like Spiders', 'Myriapods like Centipedes'],
            "bn": ['চিংড়ির মতো ক্রাস্টাশিয়ানদের (Prawns)', 'আরশোলার মতো পতঙ্গদের', 'মাকড়সার মতো অ্যারাকনিডদের', 'শতপদীর মতো মিরিয়াপডদের']
        },
        "correct": 0,
        "expl_en": 'Antennal glands or green glands perform the excretory function in crustaceans such as prawns.',
        "expl_bn": 'চিংড়ি বা প্রন (Prawn)-এর প্রধান রেচন অঙ্গ হলো মাথার কাছে অবস্থিত সবুজ গ্রন্থি বা অ্যান্টিনারি গ্রন্থি।',
    },
    {
        "id": 'BIO-AK-101',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": "Which of the following molluscs is commonly known as 'Sea hare'?",
        "bn": "নিচের কোন মোলাস্কটিকে সাধারণ ভাষায় 'সি হেয়ার' (Sea hare) বলা হয়?",
        "opts": {
            "en": ['Aplysia', 'Dentalium (Tusk shell)', 'Chaetopleura (Chiton)', 'Pila (Apple snail)'],
            "bn": ['অ্যাপ্লাইসিয়া (Aplysia)', 'ডেন্টালিয়াম', 'কিটোপ্লিউরা', 'পিলা বা আপেল শামুক']
        },
        "correct": 0,
        "expl_en": 'Common names from NCERT: Pila (Apple snail), Pinctada (Pearl oyster), Sepia (Cuttlefish), Loligo (Squid), Octopus (Devil fish), Aplysia (Sea hare), Dentalium (Tusk shell), and Chaetopleura (Chiton).',
        "expl_bn": 'Aplysia-কে সি হেয়ার (Sea hare) বলা হয়।',
    },
    {
        "id": 'BIO-AK-102',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Dentalium is commonly known as:',
        "bn": 'ডেন্টালিয়াম (Dentalium)-এর সাধারণ নাম কী?',
        "opts": {
            "en": ['Tusk shell', 'Chiton', 'Apple snail', 'Pearl oyster'],
            "bn": ['টাস্ক শেল বা হাতির দাঁতের মতো খোলক (Tusk shell)', 'কাইটন', 'আপেল শামুক', 'মুক্তা ঝিনুক']
        },
        "correct": 0,
        "expl_en": 'Dentalium possesses a tusk-like tubular shell open at both ends and is commonly called the tusk shell.',
        "expl_bn": 'Dentalium-কে সাধারণ ভাষায় টাস্ক শেল (Tusk shell) বলা হয়।',
    },
    {
        "id": 'BIO-AK-103',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which snake among the following is NON-POISONOUS?',
        "bn": 'নিচের সাপগুলির মধ্যে কোনটি বিষহীন (Non-poisonous)?',
        "opts": {
            "en": ['Python molurus', 'Naja naja (Cobra)', 'Bangarus caeruleus (Krait)', 'Vipera russelli (Viper)'],
            "bn": ['অজগর বা পাইথন (Python)', 'গোখরো বা কেউটে', 'কালাচ বা ক্রেইট', 'চন্দ্রবোড়া বা ভাইপার']
        },
        "correct": 0,
        "expl_en": 'Python is a large non-venomous constrictor snake. Cobra (Naja), Krait (Bangarus), and Viper (Vipera) are venomous poisonous snakes listed in NCERT.',
        "expl_bn": 'পাইথন বা অজগর হলো একটি বিষহীন সাপ; কোবরা, কালাচ ও ভাইপার হলো মারাত্মক বিষধর সাপ।',
    },
    {
        "id": 'BIO-AK-104',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'In birds, which organ produces vocal sounds instead of a mammalian larynx?',
        "bn": 'পাখিদের ক্ষেত্রে স্তন্যপায়ী প্রাণীর ল্যারিঙ্কসের পরিবর্তে কোন অঙ্গটি সুমধুর শব্দ বা ডাক তৈরি করে?',
        "opts": {
            "en": ['Syrinx (located at tracheal bifurcation)', 'Pharynx', 'Larynx', 'Gizzard'],
            "bn": ['সিরিঙ্কস বা শব্দথলি (Syrinx)', 'গলবিল', 'ল্যারিঙ্কস', 'গিজার্ড']
        },
        "correct": 0,
        "expl_en": 'Birds produce sound using the syrinx, a cartilaginous voice box situated at the base of the trachea near the bronchi.',
        "expl_bn": 'পাখির ডাক উৎপন্নকারী বিশেষ অঙ্গ হলো সিরিঙ্কস (Syrinx) যা শ্বাসনালীর গোড়ায় অবস্থিত।',
    },
    {
        "id": 'BIO-AK-105',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Sea squirts like Ascidia belong to which chordate subphylum?',
        "bn": 'অ্যাসিডিয়া (Ascidia)-র মতো সি-স্কুইর্ট কোন কর্ডাটা উপপর্বের অন্তর্গত?',
        "opts": {
            "en": ['Urochordata (Tunicata)', 'Cephalochordata', 'Vertebrata', 'Hemichordata'],
            "bn": ['ইউরোকর্ডাটা বা টিউনিকাটা (Urochordata)', 'সেফালোকর্ডাটা', 'ভার্টিব্রাটা', 'হெமிকর্ডাটা']
        },
        "correct": 0,
        "expl_en": 'Ascidia is a classic tunicated marine invertebrate belonging to Urochordata.',
        "expl_bn": 'অ্যাসিডিয়া (Ascidia) হলো ইউরোকর্ডাটা উপপর্বের অন্তর্ভুক্ত প্রাণী।',
    },
    {
        "id": 'BIO-AK-106',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Examine the cross-sectional diagrams of the three coelom body plans:<br><svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- (A) Eucoelomate (Coelomate) -->\n  <g transform="translate(10, 10)">\n    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>\n    <!-- Mesoderm lining body wall and gut with true cavity -->\n    <circle cx="80" cy="80" r="60" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <!-- Coelom cavity (white) -->\n    <circle cx="80" cy="80" r="48" fill="#ffffff" stroke="#ef4444" stroke-width="1"/>\n    <!-- Gut with mesoderm lining -->\n    <circle cx="80" cy="80" r="28" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>\n    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Gut</text>\n    <text x="80" y="48" fill="#b91c1c" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Coelom</text>\n    <text x="80" y="168" fill="#991b1b" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">A: Coelomate</text>\n  </g>\n\n  <!-- (B) Pseudocoelomate -->\n  <g transform="translate(180, 10)">\n    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>\n    <!-- Pseudocoelom cavity space -->\n    <circle cx="80" cy="80" r="60" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>\n    <!-- Scattered mesodermal pouches -->\n    <circle cx="50" cy="60" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <circle cx="110" cy="60" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <circle cx="50" cy="100" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <circle cx="110" cy="100" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <!-- Endodermal gut -->\n    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>\n    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Gut</text>\n    <text x="80" y="168" fill="#0369a1" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">B: Pseudocoelomate</text>\n  </g>\n\n  <!-- (C) Acoelomate -->\n  <g transform="translate(350, 10)">\n    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>\n    <!-- Solid mesoderm (parenchyma) without any cavity -->\n    <circle cx="80" cy="80" r="60" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <!-- Endodermal gut -->\n    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>\n    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Gut</text>\n    <text x="80" y="45" fill="#991b1b" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Parenchyma</text>\n    <text x="80" y="168" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">C: Acoelomate</text>\n  </g>\n</svg><br>Which of the following correctly matches the diagram with the animal phylum representing it?',
        "bn": 'তিনটি প্রধান সিলোম বা দেহগহ্বরের প্রদত্ত প্রস্থচ্ছেদগুলি লক্ষ্য করো:<br><svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- (A) Eucoelomate (Coelomate) -->\n  <g transform="translate(10, 10)">\n    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>\n    <!-- Mesoderm lining body wall and gut with true cavity -->\n    <circle cx="80" cy="80" r="60" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <!-- Coelom cavity (white) -->\n    <circle cx="80" cy="80" r="48" fill="#ffffff" stroke="#ef4444" stroke-width="1"/>\n    <!-- Gut with mesoderm lining -->\n    <circle cx="80" cy="80" r="28" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>\n    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Gut</text>\n    <text x="80" y="48" fill="#b91c1c" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Coelom</text>\n    <text x="80" y="168" fill="#991b1b" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">A: Coelomate</text>\n  </g>\n\n  <!-- (B) Pseudocoelomate -->\n  <g transform="translate(180, 10)">\n    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>\n    <!-- Pseudocoelom cavity space -->\n    <circle cx="80" cy="80" r="60" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>\n    <!-- Scattered mesodermal pouches -->\n    <circle cx="50" cy="60" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <circle cx="110" cy="60" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <circle cx="50" cy="100" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <circle cx="110" cy="100" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <!-- Endodermal gut -->\n    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>\n    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Gut</text>\n    <text x="80" y="168" fill="#0369a1" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">B: Pseudocoelomate</text>\n  </g>\n\n  <!-- (C) Acoelomate -->\n  <g transform="translate(350, 10)">\n    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>\n    <!-- Solid mesoderm (parenchyma) without any cavity -->\n    <circle cx="80" cy="80" r="60" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n    <!-- Endodermal gut -->\n    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>\n    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Gut</text>\n    <text x="80" y="45" fill="#991b1b" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Parenchyma</text>\n    <text x="80" y="168" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">C: Acoelomate</text>\n  </g>\n</svg><br>নিচের কোন বিকল্পে চিত্র এবং তার প্রতিনিধি প্রাণী পর্বকে সঠিকভাবে মেলানো হয়েছে?',
        "opts": {
            "en": ['A = Coelomate (Annelida to Chordata); B = Pseudocoelomate (Aschelminthes); C = Acoelomate (Platyhelminthes)', 'A = Acoelomate (Platyhelminthes); B = Coelomate (Annelida); C = Pseudocoelomate (Aschelminthes)', 'A = Pseudocoelomate; B = Coelomate; C = Acoelomate', 'A = Coelomate (Aschelminthes); B = Pseudocoelomate (Annelida); C = Acoelomate (Porifera)'],
            "bn": ['A = সিলোমেট (অ্যানেলিডা থেকে কর্ডাটা); B = সিউডোসিলোমেট (অ্যাসকেলমিন্থেস); C = অ্যাসিলোমেট (প্লাটিহেলমিন্থেস)', 'A = অ্যাসিলোমেট (প্লাটিহেলমিন্থেস); B = সিলোমেট (অ্যানেলিডা); C = সিউডোসিলোমেট (অ্যাসকেলমিন্থেস)', 'A = সিউডোসিলোমেট; B = সিলোমেট; C = অ্যাসিলোমেট', 'A = সিলোমেট (অ্যাসকেলমিন্থেস); B = সিউডোসিলোমেট (অ্যানেলিডা); C = অ্যাসিলোমেট (পরিফেরা)']
        },
        "correct": 0,
        "expl_en": 'Diagram A represents a true eucoelomate with body cavity lined completely by mesoderm peritoneum on both body wall and gut (Annelids to Chordates). Diagram B represents a pseudocoelomate with scattered mesodermal pouches (Aschelminthes). Diagram C represents an acoelomate with solid parenchyma (Platyhelminthes).',
        "expl_bn": 'A হলো প্রকৃত সিলোমেট (দেহগহ্বর মেসোডার্ম দ্বারা আবৃত - অ্যানেলিডা থেকে কর্ডাটা); B হলো মেসোডার্মের বিক্ষিপ্ত থলিযুক্ত সিউডোসিলোমেট (অ্যাসকেলমিন্থেস); এবং C হলো সিলোমহীন অ্যাসিলোমেট (প্লাটিহেলমিন্থেস)।',
    },
    {
        "id": 'BIO-AK-107',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Given below is the schematic diagram showing the fundamental body plan of a chordate:<br><svg viewBox="0 0 520 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- General chordate fish-like body outline -->\n  <path d="M 40 100 Q 150 20 400 30 Q 480 70 500 100 Q 480 130 400 170 Q 150 180 40 100 Z" fill="#f0f9ff" stroke="#0284c7" stroke-width="2.5"/>\n  \n  <!-- 1. Nerve cord (Dorsal hollow nerve cord, green, labeled A) -->\n  <path d="M 90 55 Q 250 40 450 65" fill="none" stroke="#16a34a" stroke-width="4"/>\n  <text x="250" y="45" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">A (Dorsal Hollow Nerve Cord)</text>\n  \n  <!-- 2. Notochord (Blue solid rod under nerve cord, labeled B) -->\n  <path d="M 70 75 Q 250 60 465 85" fill="none" stroke="#2563eb" stroke-width="6" stroke-linecap="round"/>\n  <text x="250" y="80" fill="#1d4ed8" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">B (Notochord)</text>\n  \n  <!-- Gut tube -->\n  <path d="M 40 100 Q 160 110 360 140" fill="none" stroke="#ca8a04" stroke-width="3"/>\n  <circle cx="360" cy="140" r="4" fill="#a16207"/>\n  <text x="360" y="158" fill="#a16207" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">Anus</text>\n  \n  <!-- 3. Pharyngeal Gill Slits (labeled C) -->\n  <g stroke="#dc2626" stroke-width="3" stroke-linecap="round">\n    <line x1="120" y1="95" x2="120" y2="120"/>\n    <line x1="135" y1="95" x2="135" y2="120"/>\n    <line x1="150" y1="95" x2="150" y2="120"/>\n    <line x1="165" y1="95" x2="165" y2="120"/>\n  </g>\n  <text x="142" y="145" fill="#b91c1c" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">C (Pharyngeal Gill Slits)</text>\n  \n  <!-- 4. Post-anal tail (labeled D) -->\n  <path d="M 360 140 Q 420 160 500 100" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-dasharray="3,2"/>\n  <text x="440" y="160" fill="#6d28d9" font-size="10" font-weight="bold" font-family="system-ui">D (Post-anal tail)</text>\n</svg><br>Identify the labeled structures A, B, C, and D:',
        "bn": 'নিচে একটি আদর্শ কর্ডাটা প্রাণীর মৌলিক দৈহিক গঠনের রেখাচিত্র দেওয়া হলো:<br><svg viewBox="0 0 520 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- General chordate fish-like body outline -->\n  <path d="M 40 100 Q 150 20 400 30 Q 480 70 500 100 Q 480 130 400 170 Q 150 180 40 100 Z" fill="#f0f9ff" stroke="#0284c7" stroke-width="2.5"/>\n  \n  <!-- 1. Nerve cord (Dorsal hollow nerve cord, green, labeled A) -->\n  <path d="M 90 55 Q 250 40 450 65" fill="none" stroke="#16a34a" stroke-width="4"/>\n  <text x="250" y="45" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">A (Dorsal Hollow Nerve Cord)</text>\n  \n  <!-- 2. Notochord (Blue solid rod under nerve cord, labeled B) -->\n  <path d="M 70 75 Q 250 60 465 85" fill="none" stroke="#2563eb" stroke-width="6" stroke-linecap="round"/>\n  <text x="250" y="80" fill="#1d4ed8" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">B (Notochord)</text>\n  \n  <!-- Gut tube -->\n  <path d="M 40 100 Q 160 110 360 140" fill="none" stroke="#ca8a04" stroke-width="3"/>\n  <circle cx="360" cy="140" r="4" fill="#a16207"/>\n  <text x="360" y="158" fill="#a16207" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">Anus</text>\n  \n  <!-- 3. Pharyngeal Gill Slits (labeled C) -->\n  <g stroke="#dc2626" stroke-width="3" stroke-linecap="round">\n    <line x1="120" y1="95" x2="120" y2="120"/>\n    <line x1="135" y1="95" x2="135" y2="120"/>\n    <line x1="150" y1="95" x2="150" y2="120"/>\n    <line x1="165" y1="95" x2="165" y2="120"/>\n  </g>\n  <text x="142" y="145" fill="#b91c1c" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">C (Pharyngeal Gill Slits)</text>\n  \n  <!-- 4. Post-anal tail (labeled D) -->\n  <path d="M 360 140 Q 420 160 500 100" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-dasharray="3,2"/>\n  <text x="440" y="160" fill="#6d28d9" font-size="10" font-weight="bold" font-family="system-ui">D (Post-anal tail)</text>\n</svg><br>A, B, C এবং D চিহ্নিত গঠনগুলি শনাক্ত করো:',
        "opts": {
            "en": ['A = Dorsal hollow nerve cord; B = Notochord; C = Pharyngeal gill slits; D = Post-anal tail', 'A = Notochord; B = Nerve cord; C = Gill slits; D = Caudal fin', 'A = Vertebral column; B = Spinal cord; C = Trachea; D = Anus', 'A = Dorsal vessel; B = Ventral nerve cord; C = Heart; D = Telson'],
            "bn": ['A = পৃষ্ঠীয় ফাঁপা স্নায়ুরজ্জু (Dorsal hollow nerve cord); B = নোটোকর্ড (Notochord); C = গলবিলীয় ফুলকা ছিদ্র (Gill slits); D = পায়ু-পশ্চাৎ পুচ্ছ (Post-anal tail)', 'A = নোটোকর্ড; B = নার্ভ কর্ড; C = ফুলকা ছিদ্র; D = পুচ্ছ পাখনা', 'A = মেরুদণ্ড; B = সুষুম্নাকাণ্ড; C = শ্বাসনালী; D = পায়ু', 'A = পৃষ্ঠীয় রক্তনালী; B = অঙ্কীয় স্নায়ুরজ্জু; C = হৃদপিণ্ড; D = টেলসন']
        },
        "correct": 0,
        "expl_en": 'In chordate body organization: A is the dorsal, hollow, single ectodermal nerve cord. B is the dorsal solid flexible mesodermal notochord underneath the nerve cord. C represents paired pharyngeal gill slits, and D is the muscular post-anal tail.',
        "expl_bn": 'কর্ডাটার চিত্রে: A হলো পৃষ্ঠীয় ফাঁপা স্নায়ুরজ্জু (সবুজ); B হলো তার ঠিক নিচে অবস্থিত মেসোডার্মাল নোটোকর্ড (নীল); C হলো গলবিলীয় ফুলকা ছিদ্র; এবং D হলো পায়ুর পেছনের পেশিবহুল লেজ (Post-anal tail)।',
    },
    {
        "id": 'BIO-AK-108',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Observe the two basic body forms of cnidarians depicted below:<br><svg viewBox="0 0 460 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Polyp Form (Hydra / Adamsia) -->\n  <g transform="translate(40, 20)">\n    <!-- Cylindrical stalk attached at base -->\n    <path d="M 40 160 L 40 60 Q 60 70 80 60 L 80 160 Z" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>\n    <!-- Tentacles directed upwards -->\n    <path d="M 45 60 Q 30 20 20 10 M 55 63 Q 50 15 60 5 M 65 63 Q 70 15 65 5 M 75 60 Q 90 20 100 10" fill="none" stroke="#1d4ed8" stroke-width="2.5" stroke-linecap="round"/>\n    <!-- Mouth on hypostome -->\n    <circle cx="60" cy="60" r="4" fill="#ef4444"/>\n    <text x="60" y="75" fill="#dc2626" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Mouth</text>\n    <text x="60" y="180" fill="#1e40af" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Polyp (A)</text>\n    <text x="60" y="195" fill="#3b82f6" font-size="9" font-family="system-ui" text-anchor="middle">Sessile &amp; Cylindrical</text>\n  </g>\n\n  <!-- Medusa Form (Aurelia / Jelly fish) -->\n  <g transform="translate(260, 20)">\n    <!-- Umbrella shaped bell -->\n    <path d="M 20 80 Q 80 15 140 80 Q 80 90 20 80 Z" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>\n    <!-- Mouth directed downwards on manubrium -->\n    <rect x="70" y="85" width="20" height="30" fill="#fca5a5" stroke="#b91c1c" stroke-width="1.5"/>\n    <circle cx="80" cy="115" r="4" fill="#7f1d1d"/>\n    <text x="80" y="130" fill="#991b1b" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Mouth</text>\n    <!-- Marginal tentacles hanging down -->\n    <path d="M 25 82 Q 20 130 15 160 M 45 86 Q 40 130 45 165 M 115 86 Q 120 130 115 165 M 135 82 Q 140 130 145 160" fill="none" stroke="#e11d48" stroke-width="2" stroke-linecap="round"/>\n    <text x="80" y="180" fill="#991b1b" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Medusa (B)</text>\n    <text x="80" y="195" fill="#e11d48" font-size="9" font-family="system-ui" text-anchor="middle">Free-swimming &amp; Umbrella</text>\n  </g>\n</svg><br>Which comparison between Form A and Form B is CORRECT?',
        "bn": 'নিডারিয়া পর্বের প্রাণীদের দুটি মৌলিক দৈহিক রূপ লক্ষ্য করো:<br><svg viewBox="0 0 460 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">\n  <!-- Polyp Form (Hydra / Adamsia) -->\n  <g transform="translate(40, 20)">\n    <!-- Cylindrical stalk attached at base -->\n    <path d="M 40 160 L 40 60 Q 60 70 80 60 L 80 160 Z" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>\n    <!-- Tentacles directed upwards -->\n    <path d="M 45 60 Q 30 20 20 10 M 55 63 Q 50 15 60 5 M 65 63 Q 70 15 65 5 M 75 60 Q 90 20 100 10" fill="none" stroke="#1d4ed8" stroke-width="2.5" stroke-linecap="round"/>\n    <!-- Mouth on hypostome -->\n    <circle cx="60" cy="60" r="4" fill="#ef4444"/>\n    <text x="60" y="75" fill="#dc2626" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Mouth</text>\n    <text x="60" y="180" fill="#1e40af" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Polyp (A)</text>\n    <text x="60" y="195" fill="#3b82f6" font-size="9" font-family="system-ui" text-anchor="middle">Sessile &amp; Cylindrical</text>\n  </g>\n\n  <!-- Medusa Form (Aurelia / Jelly fish) -->\n  <g transform="translate(260, 20)">\n    <!-- Umbrella shaped bell -->\n    <path d="M 20 80 Q 80 15 140 80 Q 80 90 20 80 Z" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>\n    <!-- Mouth directed downwards on manubrium -->\n    <rect x="70" y="85" width="20" height="30" fill="#fca5a5" stroke="#b91c1c" stroke-width="1.5"/>\n    <circle cx="80" cy="115" r="4" fill="#7f1d1d"/>\n    <text x="80" y="130" fill="#991b1b" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">Mouth</text>\n    <!-- Marginal tentacles hanging down -->\n    <path d="M 25 82 Q 20 130 15 160 M 45 86 Q 40 130 45 165 M 115 86 Q 120 130 115 165 M 135 82 Q 140 130 145 160" fill="none" stroke="#e11d48" stroke-width="2" stroke-linecap="round"/>\n    <text x="80" y="180" fill="#991b1b" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Medusa (B)</text>\n    <text x="80" y="195" fill="#e11d48" font-size="9" font-family="system-ui" text-anchor="middle">Free-swimming &amp; Umbrella</text>\n  </g>\n</svg><br>দেহরূপ A এবং দেহরূপ B-এর মধ্যে কোন তুলনাটি সঠিক?',
        "opts": {
            "en": ['Form A is a sessile, cylindrical Polyp (e.g., Hydra, Adamsia); Form B is a free-swimming, umbrella-shaped Medusa (e.g., Aurelia)', 'Form A is a free-swimming Medusa; Form B is a sessile Polyp', 'Form A is formed sexually from Form B; Form B is formed sexually from Form A', 'Both Form A and Form B are motile adult stages of corals'],
            "bn": ['A হলো নিশ্চল নলাকার পলিপ (যেমন হাইড্রা, অ্যাডামসিয়া); B হলো মুক্ত সাঁতারু ছাতার মতো মেদুসা (যেমন অরেলিয়া বা জেলিফিশ)', 'A হলো মেদুসা এবং B হলো পলিপ', 'A যৌন জননে B তৈরি করে এবং B যৌন জননে A তৈরি করে', 'A ও B উভয়ই প্রবালের সচল দশা']
        },
        "correct": 0,
        "expl_en": 'Form A is the sessile and cylindrical Polyp with upward mouth and tentacles (Hydra, Adamsia). Form B is the free-swimming umbrella-like Medusa with downward mouth (Aurelia/Jellyfish).',
        "expl_bn": 'A রূপটি হলো স্থানু ও নলাকার পলিপ (Polyp); B রূপটি হলো ছাতাসদৃশ মুক্ত সাঁতারু মেদুসা (Medusa)।',
    },
    {
        "id": 'BIO-AK-109',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Sponges (Phylum Porifera) have a cellular level of organization, yet the cells demonstrate functional coordination.<br>Reason (R): In sponges, the flagellated choanocytes create continuous water currents that bring food, respiratory oxygen, and carry away metabolic wastes through the osculum.',
        "bn": 'নিশ্চিত বিবৃতি (A): পরিফেরা পর্বের স্পঞ্জে কোষীয় মাত্রার সংগঠন থাকা সত্ত্বেও এদের কোষগুলির মধ্যে চমৎকার কার্যগত সমন্বয় দেখা যায়।<br>যুক্তি (R): স্পঞ্জের ফ্ল্যাজেলাযুক্ত কোয়ানোসাইট কোষগুলি অবিরাম জলপ্রবাহ সৃষ্টি করে যা খাদ্যকণা ও অক্সিজেন ভেতরে নিয়ে আসে এবং বর্জ্য পদার্থ অসকুলাম দিয়ে বাইরে বের করে দেয়।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Even without true tissues or nervous coordination, the physical beating of choanocyte flagella drives the hydrodynamics of the canal system, sustaining nutrition, respiration, and excretion for the entire cellular collective. (R) correctly explains (A).',
        "expl_bn": 'কলা না থাকলেও কোয়ানোসাইটের ফ্ল্যাজেলার স্পন্দনে সৃষ্ট জল সংবহন তন্ত্রই সমগ্র স্পঞ্জদেহের খাদ্য, শ্বসন ও রেচনের মৌলিক সমন্বয় সম্পন্ন করে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-AK-110',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Ctenophores are considered distinct from Cnidarians and are given their own separate phylum.<br>Reason (R): Ctenophores completely lack cnidocytes (nematocysts); instead, they possess eight ciliated comb plates for locomotion and capture prey using sticky colloblast cells.',
        "bn": 'নিশ্চিত বিবৃতি (A): টিনোফোরা পর্বের প্রাণীদের নিডারিয়া থেকে সম্পূর্ণ পৃথক করে একটি আলাদা পর্বের মর্যাদা দেওয়া হয়েছে।<br>যুক্তি (R): টিনোফোরায় নিডোসাইট (নেমাটোসিস্ট) একেবারেই থাকে না; তার পরিবর্তে এদের চলনের জন্য আটটি সিলিয়াযুক্ত কম্ব প্লেট এবং শিকার ধরতে আঠালো কলোব্লাস্ট কোষ থাকে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Because cnidarians are fundamentally defined by stinging cnidocytes, the absence of cnidocytes combined with 8 ciliated comb plates and colloblasts necessitated creating Phylum Ctenophora. (R) correctly explains (A).',
        "expl_bn": 'নিডারিয়ার মূল বৈশিষ্ট্য নিডোব্লাস্ট কোষের অনুপস্থিতি এবং আটটি কম্ব প্লেট ও আঠালো কলোব্লাস্ট কোষের উপস্থিতির কারণেই টিনোফোরাকে পৃথক পর্ব করা হয়েছে। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-AK-111',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": "Assertion (A): Tapeworms (Taenia) lack an alimentary canal of their own.<br>Reason (R): Tapeworms are gut endoparasites whose thin body wall directly absorbs pre-digested nutrients across their microtriches from the host's intestinal lumen.",
        "bn": 'নিশ্চিত বিবৃতি (A): ফিতাকৃমির (Taenia) নিজস্ব কোনো পৌষ্টিকনালী বা পরিপাকতন্ত্র থাকে না।<br>যুক্তি (R): ফিতাকৃমি হলো অন্ত্রের অন্তঃপরজীবী যা পোষকের অন্ত্র থেকে সরাসরি ত্বক ও মাইক্রোট্রিক্সের মাধ্যমে পূর্বে পরিপাক হওয়া পুষ্টিরস শোষণ করে নেয়।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Endoparasitic flatworms like tapeworms live bathed in host digestive juices. They adaptively lost their entire gut, absorbing simple sugars and amino acids directly across their surface tegument. (R) correctly explains (A).',
        "expl_bn": 'পোষকের অন্ত্রে সর্বদা সরল পাচিত খাদ্য উপস্থিত থাকায় ফিতাকৃমির পরিপাকতন্ত্র বিলুপ্ত হয়েছে; এরা পুরো দেহত্বকের মাধ্যমে সরাসরি পুষ্টিরস শোষণ করে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-AK-112',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Arthropoda is the most taxonomically diverse and ecologically successful animal phylum on Earth.<br>Reason (R): Arthropods possess a lightweight, waterproof chitinous exoskeleton, jointed appendages, and highly developed sensory systems that enable adaptation to diverse ecological niches.',
        "bn": 'নিশ্চিত বিবৃতি (A): আর্থ্রোপোডা হলো পৃথিবীর সর্বাপেক্ষা সফল এবং সর্বাধিক প্রজাতিসমৃদ্ধ প্রাণী পর্ব।<br>যুক্তি (R): আর্থ্রোপোডার দেহে হালকা ও জলরোধী কাইটিনযুক্ত বহিঃকঙ্কাল, নমনীয় সন্ধিল উপাঙ্গ এবং সুবিকশিত সংবেদী অঙ্গ থাকায় এরা প্রায় প্রতিটি বাস্তুতন্ত্রে অভিযোজিত হতে পেরেছে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'The chitinous cuticle protects against desiccation on land, jointed appendages provide versatile locomotion, and flight in insects opened aerial niches, driving immense evolutionary radiation. (R) correctly explains (A).',
        "expl_bn": 'জলরোধী কাইটিন বহিঃকঙ্কাল স্থলভাগে জলক্ষয় রোধ করে এবং সন্ধিল উপাঙ্গ ও ওড়ার ক্ষমতা এদের পৃথিবীর সর্বত্র আধিপত্য বিস্তার করতে সাহায্য করেছে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-AK-113',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Echinoderms show closer phylogenetic affinity to chordates than any other non-chordate invertebrate phylum.<br>Reason (R): Both echinoderms and chordates share deuterostome embryonic development (blastopore forms the anus first; mouth develops secondarily) and enterocoelic or mesodermal coelom formation.',
        "bn": 'নিশ্চিত বিবৃতি (A): অন্য যেকোনো নন-কর্ডাটা পর্বের তুলনায় একাইনোডার্মাটার সাথে কর্ডাটার জাতিজনি বা বিবর্তনীয় ঘনিষ্ঠতা সবচেয়ে বেশি।<br>যুক্তি (R): একাইনোডার্মাটা এবং কর্ডাটা উভয় পর্বেই ডিউটেরোস্টোম (Deuterostome) ভ্রূণ বিকাশ দেখা যায় (ব্লাস্টোপোর থেকে প্রথমে পায়ু গঠিত হয় এবং মুখ পরে তৈরি হয়)।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Echinoderms, Hemichordates, and Chordates form the monophyletic clade Deuterostomia based on embryonic cleavage and blastopore fate (anus first, mouth second), linking them evolutionarily. (R) correctly explains (A).',
        "expl_bn": 'ভ্রূণের ব্লাস্টোপোর থেকে পায়ু তৈরি হওয়া (Deuterostomia) এবং মেসোডার্মাল সিলোম সৃষ্টির প্রক্রিয়ায় একাইনোডার্মাটা কর্ডাটার নিকটতম আত্মীয়। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-AK-114',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Osteichthyes (bony fishes) can stay motionless suspended at a chosen depth in water without expending muscular energy.<br>Reason (R): Osteichthyes possess a gas-filled swim bladder (air bladder) that regulates hydrostatic buoyancy.',
        "bn": 'নিশ্চিত বিবৃতি (A): অস্থিময় মাছেরা (Osteichthyes) পেশিশক্তি ব্যয় না করেই জলের নির্দিষ্ট গভীরতায় স্থিরভাবে ভেসে থাকতে পারে।<br>যুক্তি (R): অস্থিময় মাছের দেহে গ্যাসপূর্ণ পটকা বা এয়ার ব্লাডার থাকে যা এদের হাইড্রোস্ট্যাটিক প্লবতা নিখুঁতভাবে নিয়ন্ত্রণ করে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'The air bladder secretes or absorbs gas to adjust overall density to match water density at a given depth, allowing neutral buoyancy without continuous swimming. (R) correctly explains (A).',
        "expl_bn": 'পটকার গ্যাসের পরিমাণ কমিয়ে-বাড়িয়ে মাছেরা জলের যেকোনো স্তরে প্লবতা বজায় রেখে অনায়াসে ভেসে থাকতে পারে। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-AK-115',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Respiration in birds is remarkably efficient during high-altitude flight.<br>Reason (R): Birds possess thin-walled air sacs connected to their lungs that ensure continuous unidirectional airflow across parabronchi during both inhalation and exhalation.',
        "bn": 'নিশ্চিত বিবৃতি (A): আকাশে দ্রুত উড্ডয়নের সময় পাখিদের শ্বসন অত্যন্ত উচ্চক্ষমতাসম্পন্ন ও কার্যকর হয়।<br>যুক্তি (R): পাখিদের ফুসফুসের সাথে যুক্ত পাতলা প্রাচীরযুক্ত বায়ুথলি (Air sacs) শ্বাসগ্রহণ ও শ্বাসত্যাগ উভয় সময়েই ফুসফুসের ভেতর দিয়ে অবিরাম একমুখী বাতাস চলাচল নিশ্চিত করে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Air sacs function as bellows, providing continuous cross-current oxygen exchange in parabronchi with no residual stagnant air, meeting the intense aerobic metabolic demand of flight. (R) correctly explains (A).',
        "expl_bn": 'পাখির অতিরিক্ত ৯টি বায়ুথলি ফুসফুসে অক্সিজেনযুক্ত বাতাসের একমুখী অবিরাম প্রবাহ বজায় রাখে যা উড্ডয়নের বিপুল শক্তির চাহিদা পূরণ করে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-AK-116',
        "exam": 'NEET, AIIMS',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Assertion (A): Whales, dolphins, and bats are grouped alongside humans and dogs in Class Mammalia.<br>Reason (R): Whales, dolphins, and bats possess mammary glands to nourish their young with milk and have hair and a four-chambered heart.',
        "bn": 'নিশ্চিত বিবৃতি (A): তিমি, ডলফিন এবং বাদুড়কে মানুষের সাথে একই শ্রেণি ম্যামালিয়া বা স্তন্যপায়ীর অন্তর্ভুক্ত করা হয়েছে।<br>যুক্তি (R): তিমি, ডলফিন এবং বাদুড় সকলের দেহেই শাবককে দুগ্ধপান করানোর স্তনগ্রন্থি, লোম এবং চার-প্রকোষ্ঠী হৃদপিণ্ড উপস্থিত থাকে।',
        "opts": {
            "en": ['Both (A) and (R) are true, and (R) is the correct explanation of (A)', 'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)', '(A) is true, but (R) is false', '(A) is false, but (R) is true'],
            "bn": ['(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা', '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়', '(A) সত্য, কিন্তু (R) মিথ্যা', '(A) মিথ্যা, কিন্তু (R) সত্য']
        },
        "correct": 0,
        "expl_en": 'Despite secondary adaptations for swimming (whales) and flying (bats), their core diagnostic synapomorphies (mammary glands, hair, endothermy, 4-chambered heart, vivipary) place them unequivocally in Class Mammalia. (R) correctly explains (A).',
        "expl_bn": 'জলচর বা খেচর যাই হোক না কেন, স্তনগ্রন্থি এবং শাবককে দুধ খাওয়ানোর মৌলিক বৈশিষ্ট্যের কারণেই তিমি ও বাদুড়কে স্তন্যপায়ীর দলে রাখা হয়েছে। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    },
    {
        "id": 'BIO-AK-117',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Statement I: In open circulatory systems, blood is pumped out of the heart and the cells and tissues are directly bathed in it.<br>Statement II: In closed circulatory systems, blood is circulated through a continuous circuit of vessels of varying diameters (arteries, veins and capillaries).',
        "bn": 'বিবৃতি I: মুক্ত সংবহনতন্ত্রে হৃদপিণ্ড থেকে রক্ত সরাসরি দেহগহ্বরে পাম্প হয় এবং কোষ ও কলা সরাসরি রক্তে নিমজ্জিত থাকে।<br>বিবৃতি II: বদ্ধ সংবহনতন্ত্রে রক্ত সর্বদা সুনির্দিষ্ট নালীজালকের (ধমনী, শিরা ও রক্তজালক) মধ্য দিয়ে প্রবাহিত হয়।',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক']
        },
        "correct": 0,
        "expl_en": 'Both statements are direct definitions from NCERT Section 4.1.2 on Circulatory System patterns.',
        "expl_bn": 'উভয় বিবৃতিই NCERT-এর রক্ত সংবহনতন্ত্রের সংজ্ঞা অনুসারে সম্পূর্ণ সঠিক।',
    },
    {
        "id": 'BIO-AK-118',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Statement I: Aschelminthes are pseudocoelomates because the body cavity is not lined by mesoderm, but exists as scattered pouches.<br>Statement II: Annelids, Arthropods, Molluscs, Echinoderms, Hemichordates, and Chordates are all true coelomates (eucoelomates).',
        "bn": 'বিবৃতি I: অ্যাসকেলমিন্থেস হলো সিউডোসিলোমেট কারণ এদের দেহগহ্বর মেসোডার্ম দ্বারা সম্পূর্ণ আবৃত নয়, বরং মেসোডার্মের থলি হিসেবে থাকে।<br>বিবৃতি II: অ্যানেলিডা, আর্থ্রোপোডা, মোলাস্কা, একাইনোডার্মাটা, হெமிকর্ডাটা এবং কর্ডাটা প্রত্যেকেই প্রকৃত সিলোমেট (ইউসিলোমেট)।',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক']
        },
        "correct": 0,
        "expl_en": 'Both statements are completely correct. Aschelminthes is the only pseudocoelomate phylum; all phyla from Annelida onwards possess a true coelom.',
        "expl_bn": 'উভয় বিবৃতিই সঠিক। অ্যাসকেলমিন্থেস একমাত্র সিউডোসিলোমেট এবং অ্যানেলিডা থেকে কর্ডাটা পর্যন্ত সকল পর্বই প্রকৃত সিলোমেট।',
    },
    {
        "id": 'BIO-AK-119',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Statement I: Nereis is an aquatic annelid that is dioecious and possesses parapodia for swimming.<br>Statement II: Earthworms and leeches are monoecious annelids that lack parapodia.',
        "bn": 'বিবৃতি I: নেরিস হলো একটি জলজ অ্যানেলিড যা একলিঙ্গ এবং সাঁতার কাটার জন্য প্যারাপোডিয়া থাকে।<br>বিবৃতি II: কেঁচো এবং জোঁক হলো উভলিঙ্গ অ্যানেলিড যাদের কোনো প্যারাপোডিয়া থাকে না।',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক']
        },
        "correct": 0,
        "expl_en": 'Both statements are accurate facts from NCERT Annelida section.',
        "expl_bn": 'উভয় বিবৃতিই সঠিক। নেরিস একলিঙ্গ ও প্যারাপোডিয়াযুক্ত; কিন্তু কেঁচো ও জোঁক উভলিঙ্গ।',
    },
    {
        "id": 'BIO-AK-120',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Statement I: All living cyclostomes lack jaws and paired fins.<br>Statement II: Cyclostomes have a cartilaginous cranium and vertebral column.',
        "bn": 'বিবৃতি I: সমস্ত জীবিত সাইক্লোস্টোমদের চোয়াল এবং যুগ্ম পাখনার অভাব থাকে।<br>বিবৃতি II: সাইক্লোস্টোমদের খুলি (cranium) এবং কশেরুকা তরুণাস্থিময় কঙ্কাল দ্বারা গঠিত।',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক']
        },
        "correct": 0,
        "expl_en": 'Both statements are exact facts from NCERT Section 4.2.11.1 (Class Cyclostomata).',
        "expl_bn": 'উভয় বিবৃতিই সঠিক। সাইক্লোস্টোমদের কোনো চোয়াল ও যুগ্ম পাখনা থাকে না এবং এদের খুলি ও মেরুদণ্ড তরুণাস্থিময়।',
    },
    {
        "id": 'BIO-AK-121',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Statement I: In Chondrichthyes, fertilization is internal and many of them are viviparous.<br>Statement II: In Osteichthyes, fertilization is usually external and they are mostly oviparous.',
        "bn": 'বিবৃতি I: তরুণাস্থিময় মাছে (Chondrichthyes) নিষেক অভ্যন্তরীণ এবং এদের অনেকেই জরায়ুজ বা সরাসরি বাচ্চা প্রসব করে।<br>বিবৃতি II: অস্থিময় মাছে (Osteichthyes) নিষেক প্রধানত বাহ্যিক এবং এরা বেশিরভাগই ডিম্বজ বা ডিম পাড়ে।',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক']
        },
        "correct": 0,
        "expl_en": 'Both statements are correct NCERT contrasts between cartilaginous and bony fishes.',
        "expl_bn": 'উভয় বিবৃতিই সঠিক। হাঙ্গরে অভ্যন্তরীণ নিষেক ও সন্তান প্রসব দেখা যায়; কিন্তু রুই-কাতলায় জলে বহিঃনিষেক ঘটে ও ডিম পাড়ে।',
    },
    {
        "id": 'BIO-AK-122',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Statement I: In reptiles, birds, and mammals, fertilization is strictly internal.<br>Statement II: In amphibians and majority of bony fishes, fertilization is external and occurs in water.',
        "bn": 'বিবৃতি I: সরীসৃপ, পাখি এবং স্তন্যপায়ী প্রাণীদের ক্ষেত্রে নিষেক সর্বদা অভ্যন্তরীণ হয়।<br>বিবৃতি II: উভচর এবং অধিকাংশ অস্থিময় মাছের ক্ষেত্রে বহিঃনিষেক জলের মধ্যে সম্পন্ন হয়।',
        "opts": {
            "en": ['Both Statement I and Statement II are correct', 'Both Statement I and Statement II are incorrect', 'Statement I is correct but Statement II is incorrect', 'Statement I is incorrect but Statement II is correct'],
            "bn": ['বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক', 'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল', 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল', 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক']
        },
        "correct": 0,
        "expl_en": 'Both statements are accurate. Terrestrial amniotes (Reptiles, Aves, Mammals) require internal fertilization; aquatic anamniotes (Amphibia, Osteichthyes) utilize external fertilization in water.',
        "expl_bn": 'উভয় বিবৃতিই সঠিক। স্থলজ উন্নত মেরুদণ্ডীদের অভ্যন্তরীণ নিষেক হয়, আর ব্যাঙ ও অস্থিময় মাছেরা জলে ডিম ও শুক্রাণু ছেড়ে বহিঃনিষেক ঘটায়।',
    },
    {
        "id": 'BIO-AK-123',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Match Column-I (Animal) with Column-II (Excretory structure):<br>A. Planaria<br>B. Earthworm<br>C. Prawn<br>D. Cockroach<br>1. Green glands (Antennal glands)<br>2. Flame cells (Protonephridia)<br>3. Malpighian tubules<br>4. Nephridia',
        "bn": 'কলাম-I (প্রাণী)-এর সাথে কলাম-II (রেচন অঙ্গ) মেলাও:<br>A. প্ল্যানেরিয়া<br>B. কেঁচো<br>C. চিংড়ি<br>D. আরশোলা<br>1. সবুজ গ্রন্থি (গ্রিন গ্ল্যান্ড)<br>2. শিখা কোষ (ফ্লেম সেল)<br>3. ম্যালপিজিয়ান নালিকা<br>4. নেফ্রিডিয়া',
        "opts": {
            "en": ['A-2, B-4, C-1, D-3', 'A-4, B-2, C-1, D-3', 'A-2, B-1, C-4, D-3', 'A-3, B-4, C-1, D-2'],
            "bn": ['A-2, B-4, C-1, D-3', 'A-4, B-2, C-1, D-3', 'A-2, B-1, C-4, D-3', 'A-3, B-4, C-1, D-2']
        },
        "correct": 0,
        "expl_en": 'Planaria = Flame cells (A-2); Earthworm = Nephridia (B-4); Prawn = Green glands (C-1); Cockroach = Malpighian tubules (D-3).',
        "expl_bn": 'প্ল্যানেরিয়া = শিখা কোষ (A-2); কেঁচো = নেফ্রিডিয়া (B-4); চিংড়ি = সবুজ গ্রন্থি (C-1); আরশোলা = ম্যালপিজিয়ান নালিকা (D-3)।',
    },
    {
        "id": 'BIO-AK-124',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Match Column-I (Phylum) with Column-II (Hallmark feature):<br>A. Porifera<br>B. Cnidaria<br>C. Ctenophora<br>D. Echinodermata<br>1. Comb plates for locomotion and bioluminescence<br>2. Water vascular system with tube feet<br>3. Choanocytes lining canal system<br>4. Cnidocytes containing nematocysts',
        "bn": 'কলাম-I (পর্ব)-এর সাথে কলাম-II (স্বতন্ত্র বৈশিষ্ট্য) মেলাও:<br>A. পরিফেরা<br>B. নিডারিয়া<br>C. টিনোফোরা<br>D. একাইনোডার্মাটা<br>1. চলনের জন্য কম্ব প্লেট ও বায়োলুমিনেসেন্স<br>2. নালিপদযুক্ত জলসংবহন তন্ত্র<br>3. ক্যানাল সিস্টেমে কোয়ানোসাইট কোষ<br>4. নেমাটোসিস্টযুক্ত নিডোসাইট',
        "opts": {
            "en": ['A-3, B-4, C-1, D-2', 'A-4, B-3, C-1, D-2', 'A-3, B-1, C-4, D-2', 'A-2, B-4, C-1, D-3'],
            "bn": ['A-3, B-4, C-1, D-2', 'A-4, B-3, C-1, D-2', 'A-3, B-1, C-4, D-2', 'A-2, B-4, C-1, D-3']
        },
        "correct": 0,
        "expl_en": 'Porifera = Choanocytes (A-3); Cnidaria = Cnidocytes (B-4); Ctenophora = Comb plates (C-1); Echinodermata = Water vascular system (D-2).',
        "expl_bn": 'পরিফেরা = কোয়ানোসাইট (A-3); নিডারিয়া = নিডোসাইট (B-4); টিনোফোরা = কম্ব প্লেট (C-1); একাইনোডার্মাটা = জলসংবহন তন্ত্র (D-2)।',
    },
    {
        "id": 'BIO-AK-125',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Match Column-I (Scientific name) with Column-II (Common name):<br>A. Physalia<br>B. Pennatula<br>C. Gorgonia<br>D. Meandrina<br>1. Sea-fan<br>2. Brain coral<br>3. Portuguese man-of-war<br>4. Sea-pen',
        "bn": 'কলাম-I (বৈজ্ঞানিক নাম)-এর সাথে কলাম-II (সাধারণ নাম) মেলাও:<br>A. Physalia<br>B. Pennatula<br>C. Gorgonia<br>D. Meandrina<br>1. সি-ফ্যান (Sea-fan)<br>2. ব্রেন কোরাল (Brain coral)<br>3. পর্তুগিজ ম্যান-অফ-ওয়ার<br>4. সি-পেন (Sea-pen)',
        "opts": {
            "en": ['A-3, B-4, C-1, D-2', 'A-3, B-1, C-4, D-2', 'A-4, B-3, C-1, D-2', 'A-2, B-4, C-1, D-3'],
            "bn": ['A-3, B-4, C-1, D-2', 'A-3, B-1, C-4, D-2', 'A-4, B-3, C-1, D-2', 'A-2, B-4, C-1, D-3']
        },
        "correct": 0,
        "expl_en": 'Physalia = Portuguese man-of-war (A-3); Pennatula = Sea-pen (B-4); Gorgonia = Sea-fan (C-1); Meandrina = Brain coral (D-2).',
        "expl_bn": 'Physalia = পর্তুগিজ ম্যান-অফ-ওয়ার (A-3); Pennatula = সি-পেন (B-4); Gorgonia = সি-ফ্যান (C-1); Meandrina = ব্রেন কোরাল (D-2)।',
    },
    {
        "id": 'BIO-AK-126',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Match Column-I (Animal) with Column-II (Heart structure):<br>A. Rohu (Labeo)<br>B. Frog (Rana)<br>C. Crocodile (Crocodilus)<br>D. Pigeon (Columba)<br>1. 3-chambered (two auricles, one ventricle)<br>2. 2-chambered (one auricle, one ventricle)<br>3. 4-chambered with complete ventricular septum<br>4. 4-chambered with right systemic arch',
        "bn": 'কলাম-I (প্রাণী)-এর সাথে কলাম-II (হৃদপিণ্ডের গঠন) মেলাও:<br>A. রুই মাছ (Labeo)<br>B. ব্যাঙ (Rana)<br>C. কুমির (Crocodilus)<br>D. পায়রা (Columba)<br>1. ৩-প্রকোষ্ঠী (দুটি অলিন্দ, একটি নিলয়)<br>2. ২-প্রকোষ্ঠী (একটি অলিন্দ, একটি নিলয়)<br>3. ৪-প্রকোষ্ঠী (সরীসৃপের মধ্যে ব্যতিক্রম)<br>4. ৪-প্রকোষ্ঠী (উষ্ণশোণিত পক্ষী)',
        "opts": {
            "en": ['A-2, B-1, C-3, D-4', 'A-1, B-2, C-3, D-4', 'A-2, B-3, C-1, D-4', 'A-3, B-1, C-2, D-4'],
            "bn": ['A-2, B-1, C-3, D-4', 'A-1, B-2, C-3, D-4', 'A-2, B-3, C-1, D-4', 'A-3, B-1, C-2, D-4']
        },
        "correct": 0,
        "expl_en": 'Fish (Rohu) = 2-chambered; Amphibian (Frog) = 3-chambered; Crocodile = 4-chambered; Bird (Pigeon) = 4-chambered.',
        "expl_bn": 'মাছ = ২ প্রকোষ্ঠী (A-2); উভচর = ৩ প্রকোষ্ঠী (B-1); কুমির = ৪ প্রকোষ্ঠী (C-3); পাখি = ৪ প্রকোষ্ঠী (D-4)।',
    },
    {
        "id": 'BIO-AK-127',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Which of the following animals is cold-blooded (poikilothermous) with dry cornified skin, epidermal scales, and a 4-chambered heart?',
        "bn": 'নিচের কোন প্রাণীটি শীতলশোণিত (poikilothermous), যার ত্বক শুষ্ক ও এপিডার্মাল আঁশযুক্ত এবং হৃদপিণ্ড ৪-প্রকোষ্ঠ বিশিষ্ট?',
        "opts": {
            "en": ['Crocodilus (Crocodile)', 'Struthio (Ostrich)', 'Ornithorhynchus', 'Salamandra'],
            "bn": ['কুমির (Crocodilus)', 'উটপাখি', 'প্লাটিপাস', 'সালামান্ডার']
        },
        "correct": 0,
        "expl_en": 'Crocodiles are reptiles (hence poikilothermous with dry cornified scutes), but uniquely possess a 4-chambered heart.',
        "expl_bn": 'কুমির একটি সরীসৃপ হওয়ায় শীতলশোণিত ও আঁশযুক্ত ত্বকবিশিষ্ট, তবে ব্যতিক্রমীভাবে এর হৃদপিণ্ড ৪-প্রকোষ্ঠী।',
    },
    {
        "id": 'BIO-AK-128',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Read the following statements:<br>(i) All vertebrates are chordates.<br>(ii) In Urochordates, notochord extends from head to tail and persists throughout life.<br>(iii) Cyclostomes have an unjawed circular sucking mouth.<br>(iv) Cartilaginous fishes have operculum covering their gills.<br>Which of the above statements are FALSE?',
        "bn": 'নিচের বক্তব্যগুলি বিবেচনা করো:<br>(i) সমস্ত মেরুদণ্ডী প্রাণীই কর্ডাট।<br>(ii) ইউরোকর্ডাটাতে নোটোকর্ড মাথা থেকে লেজ পর্যন্ত থাকে এবং সারাজীবন স্থায়ী হয়।<br>(iii) সাইক্লোস্টোমদের চোয়ালবিহীন চোষক প্রকৃতির মুখ থাকে।<br>(iv) তরুণাস্থিময় মাছে কানকো (operculum) দ্বারা ফুলকা আবৃত থাকে।<br>উপরের কোন বক্তব্যগুলি মিথ্যা (FALSE)?',
        "opts": {
            "en": ['(ii) and (iv) are false', '(i) and (iii) are false', 'Only (iv) is false', 'All are false'],
            "bn": ['(ii) এবং (iv) মিথ্যা', '(i) এবং (iii) মিথ্যা', 'কেবল (iv) মিথ্যা', 'সবকটিই মিথ্যা']
        },
        "correct": 0,
        "expl_en": 'Statement (ii) is false because that describes Cephalochordates (in Urochordates, notochord is only in larval tail). Statement (iv) is false because Chondrichthyes lack an operculum. Statements (i) and (iii) are true.',
        "expl_bn": 'বিবৃতি (ii) মিথ্যা কারণ এটি সেফালোকর্ডাটার বৈশিষ্ট্য; এবং বিবৃতি (iv) মিথ্যা কারণ হাঙ্গরের কোনো কানকো থাকে না। সুতরাং (ii) ও (iv) মিথ্যা।',
    },
    {
        "id": 'BIO-AK-129',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'How many of the following animals possess bilateral symmetry as adults?<br>[Asterias, Adamsia, Nereis, Pila, Octopus, Pleurobrachia, Fasciola, Sycon]',
        "bn": 'প্রদত্ত প্রাণীগুলির মধ্যে কতগুলি পূর্ণাঙ্গ দশায় দ্বিপার্শ্বীয় প্রতিসাম্য (Bilateral symmetry) প্রদর্শন করে?<br>[Asterias, Adamsia, Nereis, Pila, Octopus, Pleurobrachia, Fasciola, Sycon]',
        "opts": {
            "en": ['4 (Nereis, Pila, Octopus, Fasciola)', '3', '5', '6'],
            "bn": ['৪টি (Nereis, Pila, Octopus, Fasciola)', '৩টি', '৫টি', '৬টি']
        },
        "correct": 0,
        "expl_en": 'Adult Asterias = radial; Adamsia = radial; Pleurobrachia = radial; Sycon = asymmetrical. Nereis (annelid), Pila (mollusc), Octopus (mollusc), and Fasciola (flatworm) = 4 animals with bilateral symmetry.',
        "expl_bn": 'দ্বিপার্শ্বীয় প্রতিসম প্রাণী হলো ৪টি: Nereis, Pila, Octopus এবং Fasciola। বাকিগুলি অরীয় বা অপ্রতিসম।',
    },
    {
        "id": 'BIO-AK-130',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'How many of the following organisms are exclusively marine without any known freshwater representatives?<br>[Porifera, Ctenophora, Echinodermata, Cnidaria, Protochordata (Urochordata and Cephalochordata)]',
        "bn": 'প্রদত্ত গোষ্ঠীগুলির মধ্যে কোনগুলি সম্পূর্ণ বা নিরঙ্কুশভাবে সামুদ্রিক (Exclusively marine), যাদের কোনো মিষ্ট জলের প্রজাতি নেই?<br>[Porifera, Ctenophora, Echinodermata, Cnidaria, Protochordata]',
        "opts": {
            "en": ['3 groups: Ctenophora, Echinodermata, and Protochordata', 'All 5 groups', 'Only Echinodermata', '2 groups: Porifera and Cnidaria'],
            "bn": ['৩টি গোষ্ঠী: Ctenophora, Echinodermata এবং Protochordata', 'সবকটি ৫টি গোষ্ঠী', 'কেবল একাইনোডার্মাটা', '২টি গোষ্ঠী: পরিফেরা ও নিডারিয়া']
        },
        "correct": 0,
        "expl_en": 'Porifera has Spongilla (freshwater). Cnidaria has Hydra (freshwater). Ctenophora, Echinodermata, and Protochordata are all explicitly highlighted in NCERT as exclusively marine.',
        "expl_bn": 'NCERT অনুসারে Ctenophora, Echinodermata এবং Protochordata হলো নিরঙ্কুশভাবে সামুদ্রিক (exclusively marine)। স্পঞ্জিলা (স্পঞ্জ) ও হাইড্রা (নিডারিয়া) মিষ্ট জলে থাকে।',
    },
    {
        "id": 'BIO-AK-131',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Which of the following animals has a closed circulatory system despite lacking a vertebral column?',
        "bn": 'অমেরুদণ্ডী হওয়া সত্ত্বেও নিচের কোন প্রাণীর দেহে উন্নত বদ্ধ রক্ত সংবহনতন্ত্র (Closed circulatory system) বিদ্যমান?',
        "opts": {
            "en": ['Earthworm (Pheretima) and Squid/Octopus', 'Cockroach and Prawn', 'Snail and Clam', 'Spider and Crab'],
            "bn": ['কেঁচো (Pheretima) এবং স্কুইড/অক্টোপাস (Cephalopod)', 'আরশোলা এবং চিংড়ি', 'শামুক এবং ঝিনুক', 'মাকড়সা এবং কাঁকড়া']
        },
        "correct": 0,
        "expl_en": 'Annelids (earthworm) and cephalopod molluscs (Squid, Octopus) have evolved a closed circulatory system where blood is confined to continuous vessels.',
        "expl_bn": 'কেঁচো এবং সেফালোপড মোলাস্কা (যেমন স্কুইড ও অক্টোপাস)-র রক্ত সংবহনতন্ত্র সম্পূর্ণ বদ্ধ প্রকৃতির।',
    },
    {
        "id": 'BIO-AK-132',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Easy',
        "en": 'Which bird possesses the largest egg in the living animal kingdom?',
        "bn": 'বর্তমান প্রাণীজগতের মধ্যে সবচেয়ে বৃহৎ ডিম কোন পাখিটির?',
        "opts": {
            "en": ['Struthio camelus (Ostrich)', 'Aptenodytes (Penguin)', 'Pavo cristatus (Peacock)', 'Neophron (Vulture)'],
            "bn": ['উটপাখি বা অস্ট্রিচ (Struthio camelus)', 'পেঙ্গুইন', 'ময়ূর', 'শকুন']
        },
        "correct": 0,
        "expl_en": 'The ostrich egg is the largest single biological cell in the contemporary living world.',
        "expl_bn": 'উটপাখির ডিম হলো বর্তমান জীবজগতের বৃহত্তম একক কোষ ও বৃহত্তম ডিম।',
    },
    {
        "id": 'BIO-AK-133',
        "exam": 'NEET, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Medium',
        "en": 'Which of the following represents a viviparous reptile?',
        "bn": 'অধিকাংশ সরীসৃপ ডিম্বজ হলেও নিচের কোনটি ব্যতিক্রমীভাবে জরায়ুজ বা বাচ্চা প্রসবকারী সরীসৃপ?',
        "opts": {
            "en": ['Vipera (Viper)', 'Crocodilus (Crocodile)', 'Chelone (Turtle)', 'Calotes (Garden lizard)'],
            "bn": ['ভাইপার বা চন্দ্রবোড়া সাপ (Vipera)', 'কুমির', 'কচ্ছপ', 'গিরগিটি']
        },
        "correct": 0,
        "expl_en": 'Most reptiles are oviparous, but vipers (Vipera russelli) are ovoviviparous/viviparous, retaining eggs internally and giving birth to active young ones.',
        "expl_bn": 'ভাইপার (চন্দ্রবোড়া) সাপ ডিম পাড়ে না, এটি সরাসরি জীবন্ত বাচ্চা প্রসব করে।',
    },
    {
        "id": 'BIO-AK-134',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Consider the following four animals:<br>1. Roundworm (Ascaris)<br>2. Earthworm (Pheretima)<br>3. Crab (Cancer)<br>4. Starfish (Asterias)<br>Which of these have true metameric segmentation?',
        "bn": 'প্রদত্ত চারটি প্রাণী বিবেচনা করো:<br>১. গোলকৃমি (Ascaris)<br>২. কেঁচো (Pheretima)<br>৩. কাঁকড়া (Cancer)<br>৪. তারা মাছ (Asterias)<br>এদের মধ্যে কোনটিতে প্রকৃত মেটামেরিক খণ্ডায়ন দেখা যায়?',
        "opts": {
            "en": ['2 and 3 (Earthworm and Crab)', '1 and 2 only', '3 and 4 only', '1, 2, and 3'],
            "bn": ['২ এবং ৩ (কেঁচো এবং কাঁকড়া)', 'কেবল ১ ও ২', 'কেবল ৩ ও ৪', '১, ২ এবং ৩']
        },
        "correct": 0,
        "expl_en": 'True metameric segmentation is restricted to Annelida (earthworm), Arthropoda (crab), and Chordata. Roundworms and starfish lack metamerism.',
        "expl_bn": 'প্রকৃত মেটামেরিজম কেবলমাত্র অ্যানেলিডা (কেঁচো) এবং আর্থ্রোপোডা (কাঁকড়া)-র মধ্যে সীমাবদ্ধ।',
    },
    {
        "id": 'BIO-AK-135',
        "exam": 'NEET, AIIMS, CUET',
        "subject": 'Biology',
        "topic": 'Animal Kingdom',
        "difficulty": 'Hard',
        "en": 'Which of the following represents the correct evolutionary sequence of heart chambers in vertebrates from ancestral fishes to mammals?',
        "bn": 'আদিম মাছ থেকে স্তন্যপায়ী পর্যন্ত মেরুদণ্ডীদের হৃদপিণ্ডের প্রকোষ্ঠের সঠিক বিবর্তনীয় ধারা কোনটি?',
        "opts": {
            "en": ['Fishes (2-chambered, single venous circulation) → Amphibians (3-chambered with 1 ventricle) → Reptiles (incomplete 4-chambered; 4-chambered in crocodile) → Birds and Mammals (completely separated 4-chambered, double circulation)', 'Fishes (3-chambered) → Amphibians (2-chambered) → Reptiles (4-chambered)', 'Amphibians (2-chambered) → Reptiles (3-chambered) → Birds (4-chambered)', 'Fishes (2-chambered) → Reptiles (3-chambered) → Amphibians (4-chambered)'],
            "bn": ['মাছ (২-প্রকোষ্ঠী, একক ভেনাস সংবহন) → উভচর (৩-প্রকোষ্ঠী, ১টি নিলয়) → সরীসৃপ (অসম্পূর্ণ ৪-প্রকোষ্ঠী; কুমিরে সম্পূর্ণ ৪-প্রকোষ্ঠী) → পাখি ও স্তন্যপায়ী (সম্পূর্ণ পৃথক ৪-প্রকোষ্ঠী, দ্বি-সংবহন)', 'মাছ (৩-প্রকোষ্ঠী) → উভচর (২-প্রকোষ্ঠী) → সরীসৃপ (৪-প্রকোষ্ঠী)', 'উভচর (২-প্রকোষ্ঠী) → সরীসৃপ (৩-প্রকোষ্ঠী) → পাখি (৪-প্রকোষ্ঠী)', 'মাছ (২-প্রকোষ্ঠী) → সরীসৃপ (৩-প্রকোষ্ঠী) → উভচর (৪-প্রকোষ্ঠী)']
        },
        "correct": 0,
        "expl_en": 'Vertebrate circulatory evolution progressed from a 2-chambered single circulation heart in fishes to a 3-chambered transitional heart in amphibians, transitional septation in reptiles, and completely separated 4-chambered double circulation in homeothermic birds and mammals.',
        "expl_bn": 'হৃদপিণ্ডের বিবর্তন ঘটেছে মাছের ২-প্রকোষ্ঠী একক সংবহন থেকে উভচরের ৩-প্রকোষ্ঠী, সরীসৃপের আংশিক ৪-প্রকোষ্ঠী এবং পাখি ও স্তন্যপায়ীর সম্পূর্ণ পৃথক ৪-প্রকোষ্ঠী দ্বৈত সংবহনতন্ত্রে।',
    },
]

# -----------------------------------------------------------------------------
# CHAPTER SLICES & EXPORTS
# -----------------------------------------------------------------------------
bio_living_world_questions = [q for q in biology_questions if q['id'].startswith('BIO-LW-')]
bio_classification_questions = [q for q in biology_questions if q['id'].startswith('BIO-BC-')]
bio_plant_kingdom_questions = [q for q in biology_questions if q['id'].startswith('BIO-PK-')]
bio_animal_kingdom_questions = [q for q in biology_questions if q['id'].startswith('BIO-AK-')]
