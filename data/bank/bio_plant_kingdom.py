# =============================================================================
# BIOLOGY QUESTION BANK - CHAPTER 3: PLANT KINGDOM (135 Questions)
# Graded Question Pyramid (MTG NCERT at your Fingertips Pattern)
# Mapped to NEET, AIIMS, CUET, IAT, OLYMPIAD
# =============================================================================

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

bio_plant_kingdom_questions = [ { 'bn': 'শ্রেণীবিন্যাসের কৃত্রিম পদ্ধতিতে অঙ্গজ এবং যৌন বৈশিষ্ট্যকে সমান গুরুত্ব দেওয়া হয়েছিল। এটি অগ্রহণযোগ্য ছিল '
          'কারণ:',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Artificial systems of classification gave equal weightage to vegetative and sexual characteristics. This '
          'was unacceptable because:',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'NCERT অনুসারে, কৃত্রিম শ্রেণীবিন্যাসে অঙ্গজ ও জনন বৈশিষ্ট্যকে সমান গুরুত্ব দেওয়া হয়েছিল; এটি ঠিক নয় '
               'কারণ অঙ্গজ বৈশিষ্ট্যগুলি পরিবেশের প্রভাবে সহজে পরিবর্তিত হয়ে যায়।',
    'expl_en': 'According to NCERT, artificial systems gave equal weightage to vegetative and sexual characteristics; '
               'this is not acceptable since we know that often vegetative characters are more easily affected by '
               'environment.',
    'id': 'BIO-PK-001',
    'opts': { 'bn': [ 'অঙ্গজ বৈশিষ্ট্যগুলি পরিবেশগত কারণ দ্বারা অনেক বেশি সহজে প্রভাবিত ও পরিবর্তিত হয়',
                      'যৌন বৈশিষ্ট্যগুলি পরিবেশ দ্বারা সহজে পরিবর্তিত হয়',
                      'অঙ্গজ বৈশিষ্ট্য ঋতু পরিবর্তনের সাথে কখনোই পরিবর্তিত হয় না',
                      'নিম্নশ্রেণীর ক্রিপ্টোগ্যামে জননাঙ্গ নিষ্ক্রিয় থাকে'],
              'en': [ 'Vegetative characters are more easily affected by environmental factors',
                      'Sexual characters are easily altered by environmental variations',
                      'Vegetative characters never vary across seasons',
                      'Sexual organs are non-functional in lower cryptogams']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'বেন্থাম ও হুকার কর্তৃক বীজযুক্ত উদ্ভিদের শ্রেণীবিন্যাস পদ্ধতিটি কিসের উদাহরণ?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': "Bentham and Hooker's system of classification of seeded plants is an example of:",
    'exam': 'NEET, CUET',
    'expl_bn': 'জর্জ বেন্থাম ও জে. ডি. হুকার প্রাকৃতিক শ্রেণীবিন্যাস পদ্ধতি প্রবর্তন করেন, যেখানে বাহ্যিক বৈশিষ্ট্যের '
               'পাশাপাশি অভ্যন্তরীণ শারীরস্থান, ভ্রূণতত্ত্ব এবং রাসায়নিক সাদৃশ্য বিবেচনা করা হয়।',
    'expl_en': 'George Bentham and Joseph Dalton Hooker proposed the famous Natural System of classification, taking '
               'into account not only external features but also internal features like ultrastructure, anatomy, '
               'embryology, and phytochemistry.',
    'id': 'BIO-PK-002',
    'opts': { 'bn': [ 'প্রাকৃতিক সাদৃশ্যের ওপর ভিত্তি করে রচিত প্রাকৃতিক শ্রেণীবিন্যাস পদ্ধতি (Natural system)',
                      'কেবল অভ্যাস ও পুংকেশরের ওপর ভিত্তি করে রচিত কৃত্রিম পদ্ধতি',
                      'বিবর্তনীয় পূর্বপুরুষের ওপর ভিত্তি করে রচিত জাতিজনি পদ্ধতি',
                      'DNA সিকোয়েন্সিং-এর ওপর ভিত্তি করে কেমোট্যাক্সনমিক পদ্ধতি'],
              'en': [ 'Natural system of classification based on natural affinities',
                      'Artificial system based only on habit and stamens',
                      'Phylogenetic system based strictly on evolutionary ancestry',
                      'Chemotaxonomic system based purely on DNA sequencing']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'জাতিজনি (Phylogenetic) শ্রেণীবিন্যাস পদ্ধতি মূলত কিসের ওপর প্রতিষ্ঠিত?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Phylogenetic systems of classification are based on:',
    'exam': 'NEET, CUET',
    'expl_bn': 'জাতিজনি শ্রেণীবিন্যাস পদ্ধতি বিবর্তনীয় সম্পর্কের ওপর ভিত্তি করে গড়ে উঠেছে, যা মনে করে একই ট্যাক্সনের '
               'অন্তর্ভুক্ত জীবেরা অভিন্ন পূর্বপুরুষ থেকে উদ্ভূত।',
    'expl_en': 'Phylogenetic classification systems assume that organisms belonging to the same taxa have a common '
               'ancestor, organizing taxa according to their evolutionary lineages.',
    'id': 'BIO-PK-003',
    'opts': { 'bn': [ 'বিভিন্ন জীবের মধ্যে বিবর্তনীয় বা জাতিজনি সম্পর্ক (Evolutionary relationships)',
                      'কেবল অঙ্গজ কাণ্ডের রূপতাত্ত্বিক সাদৃশ্য',
                      'কেবল ক্রোমোজোমের সংখ্যা ও গঠন',
                      'বর্তমান উদ্ভিদকুলের ভৌগোলিক বিস্তৃতি'],
              'en': [ 'Evolutionary relationships between various organisms',
                      'Morphological similarities of vegetative stems only',
                      'Number and morphology of chromosomes only',
                      'Geographical distribution of current flora']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'সমস্ত পর্যবেক্ষণযোগ্য বৈশিষ্ট্যের ওপর ভিত্তি করে কম্পিউটারের সাহায্যে কোড ও নম্বর বরাদ্দ করে যে '
          'শ্রেণীবিন্যাস করা হয়, তাকে কী বলে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Taxonomy that is based on all observable characteristics, utilizing computers where number and codes are '
          'assigned to each character, is called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'সংখ্যাগত ট্যাক্সনমি বা নিউমেরিক্যাল ট্যাক্সনমিতে কম্পিউটারের সাহায্যে সমস্ত পর্যবেক্ষণযোগ্য '
               'বৈশিষ্ট্যকে কোড বরাদ্দ করে একই সাথে শত শত বৈশিষ্ট্যের মূল্যায়ন করা হয়।',
    'expl_en': 'Numerical taxonomy uses computers and considers hundreds of observable characters simultaneously, '
               'assigning numbers and equal weightage to each character.',
    'id': 'BIO-PK-004',
    'opts': { 'bn': [ 'সংখ্যাগত ট্যাক্সনমি বা নিউমেরিক্যাল ট্যাক্সনমি (Numerical taxonomy)',
                      'সাইটোট্যাক্সনমি',
                      'কেমোট্যাক্সনমি',
                      'ক্ল্যাডিস্টিকস'],
              'en': ['Numerical taxonomy (Phenetics)', 'Cytotaxonomy', 'Chemotaxonomy', 'Cladistics']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'সাইটোট্যাক্সনমি (Cytotaxonomy) কোন কোষীয় তথ্যাবলীর ওপর প্রতিষ্ঠিত?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Cytotaxonomy is based on cytological information including:',
    'exam': 'NEET, CUET',
    'expl_bn': 'সাইটোট্যাক্সনমি কোষতাত্ত্বিক তথ্য যেমন ক্রোমোজোমের সংখ্যা, গঠন এবং জননকোষ বিভাজনে তাদের আচরণের ওপর '
               'ভিত্তি করে রচিত।',
    'expl_en': 'Cytotaxonomy is based on cytological details such as chromosome number, chromosome '
               'morphology/structure, and their meiotic behavior.',
    'id': 'BIO-PK-005',
    'opts': { 'bn': [ 'ক্রোমোজোম সংখ্যা, গঠন এবং মায়োসিস বিভাজনের সময় তাদের আচরণ',
                      'অ্যালকালয়েড ও ক্যারোটিনয়েডের মতো রাসায়নিক উপাদান',
                      'পাতার বাহ্যিক গঠন ও পুষ্প নকশা',
                      'পাললিক শিলায় সংরক্ষিত পরাগরেণুর জীবাশ্ম'],
              'en': [ 'Chromosome number, structure, and behavior during meiosis',
                      'Chemical constituents like alkaloids and carotenoids',
                      'Gross leaf morphology and floral diagrams',
                      'Fossil pollen records in sedimentary rocks']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ট্যাক্সনমিক বিভ্রান্তি দূর করতে কেমোট্যাক্সনমিতে (Chemotaxonomy) নিচের কোনটি ব্যবহার করা হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Chemotaxonomy uses which of the following to resolve taxonomic confusions?',
    'exam': 'NEET, CUET',
    'expl_bn': 'কেমোট্যাক্সনমিতে উদ্ভিদের নিজস্ব রাসায়নিক উপাদান যেমন প্রোটিন, অ্যামিনো অ্যাসিড, অ্যালকালয়েড ও '
               'নিউক্লিক অ্যাসিড বিশ্লেষণ করে শ্রেণীবিন্যাস করা হয়।',
    'expl_en': 'Chemotaxonomy utilizes the chemical constituents of plants (amino acids, aromatic compounds, DNA '
               'sequences) to resolve taxonomic ambiguities.',
    'id': 'BIO-PK-006',
    'opts': { 'bn': [ 'উদ্ভিদের রাসায়নিক উপাদান (DNA, প্রোটিন, গৌণ বিপাকীয় পদার্থ)',
                      'ফুলের প্রতিসাম্য ও দলের রঙ',
                      'উদ্ভিদ যে মাটিতে জন্মায় তার খনিজ উপাদান',
                      'বায়ুর আর্দ্রতা ও বার্ষিক বৃষ্টিপাতের চাহিদা'],
              'en': [ 'Chemical constituents of the plant (DNA, proteins, secondary metabolites)',
                      'External floral symmetry and petal coloration',
                      'Soil mineral profile where the plant grows',
                      'Atmospheric humidity and rainfall requirements']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'শৈবাল হলো ক্লোরোফিলযুক্ত, সরল, সমাঙ্গদেহী (thalloid), সংবহনকলাহীন এবং প্রধানত:',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Algae are chlorophyll-bearing, simple, thalloid, avascular, and largely:',
    'exam': 'NEET, CUET',
    'expl_bn': 'শৈবাল হলো ক্লোরোফিলযুক্ত, সরল, থ্যালয়েড, স্বভোজী এবং প্রধানত জলজ জীব (মিষ্ট জল এবং সামুদ্রিক নোনা জলে '
               'বসবাসকারী)।',
    'expl_en': 'Algae are chlorophyll-bearing, simple, thalloid, autotrophic and largely aquatic (both fresh water and '
               'marine) organisms.',
    'id': 'BIO-PK-007',
    'opts': { 'bn': [ 'জলজ জীব (মিষ্ট জল এবং সামুদ্রিক উভয় পরিবেশেই)',
                      'মরুভূমির বালিয়াড়িতে বসবাসকারী বাধ্যতামূলক জেরোফাইট',
                      'মাটির নিচে শিকড়ে বসবাসকারী পরজীবী',
                      'প্রাণীর শিং-এর ওপর বসবাসকারী পরাশ্রয়ী'],
              'en': [ 'Aquatic organisms (both fresh water and marine)',
                      'Obligate xerophytes inhabiting desert sand dunes',
                      'Subterranean root-dwelling parasitic organisms',
                      'Epiphytic organisms found exclusively on animal horns']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিচের শৈবালগুলির মধ্যে কোনটি উপনিবেশী বা কলোনিয়াল (colonial)?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following forms of algae is colonial?',
    'exam': 'NEET, CUET',
    'expl_bn': 'ভলভক্স (Volvox) একটি উপনিবেশী (colonial) সবুজ শৈবাল। ক্ল্যামাইডোমোনাস এককোষী এবং ইউলোথ্রিক্স ও '
               'স্পাইরোগাইরা সূত্রাকার শৈবাল।',
    'expl_en': 'Volvox is a colonial green alga forming spherical colonies called coenobia. Chlamydomonas is '
               'unicellular; Ulothrix and Spirogyra are filamentous.',
    'id': 'BIO-PK-008',
    'opts': { 'bn': ['ভলভক্স (Volvox)', 'ক্ল্যামাইডোমোনাস', 'ইউলোথ্রিক্স', 'স্পাইরোগাইরা'],
              'en': ['Volvox', 'Chlamydomonas', 'Ulothrix', 'Spirogyra']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিচের শৈবালগুলির মধ্যে কোনগুলি সূত্রাকার (filamentous) গঠনের অধিকারী?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following algae are filamentous in organization?',
    'exam': 'NEET, CUET',
    'expl_bn': 'ইউলোথ্রিক্স (Ulothrix) এবং স্পাইরোগাইরা (Spirogyra) হলো অশাখ সূত্রাকার সবুজ শৈবালের উদাহরণ।',
    'expl_en': 'Ulothrix and Spirogyra are classic examples of unbranched filamentous green algae.',
    'id': 'BIO-PK-009',
    'opts': { 'bn': [ 'ইউলোথ্রিক্স এবং স্পাইরোগাইরা',
                      'ভলভক্স এবং ক্ল্যামাইডোমোনাস',
                      'ক্লোরেলা এবং অ্যাসিটাবুলারিয়া',
                      'কেল্প এবং সারগাসাম'],
              'en': [ 'Ulothrix and Spirogyra',
                      'Volvox and Chlamydomonas',
                      'Chlorella and Acetabularia',
                      'Kelps and Sargassum']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': '১০০ মিটার পর্যন্ত উচ্চতা বিশিষ্ট বিশাল সামুদ্রিক উদ্ভিদদেহ গঠনকারী বাদামী শৈবালকে কী বলা হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Massive marine plant bodies reaching heights of up to 100 metres are formed by brown algae known as:',
    'exam': 'NEET, CUET',
    'expl_bn': 'কেল্প (Kelps) হলো বিশাল সামুদ্রিক বাদামী শৈবাল যা ১০০ মিটার পর্যন্ত লম্বা হতে পারে।',
    'expl_en': 'Kelps (such as Macrocystis) are giant marine brown algae (Phaeophyceae) that possess massive plant '
               'bodies extending up to 100 meters.',
    'id': 'BIO-PK-010',
    'opts': { 'bn': ['কেল্প (Kelps)', 'পরফাইরা', 'গ্র্যাসিলেয়ারিয়া', 'জেলিডিয়াম'],
              'en': ['Kelps', 'Porphyra', 'Gracilaria', 'Gelidium']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ফ্ল্যাজেলাযুক্ত চলনক্ষম গ্যামেটের সমন্বয়ে আইসোগ্যামাস (Isogamous) যৌন জনন কোনটিতে দেখা যায়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Isogamous sexual reproduction with FLAGELLATED gametes is observed in:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ইউলোথ্রিক্সে একই আকারের চলনক্ষম (ফ্ল্যাজেলাযুক্ত) গ্যামেটের মিলন ঘটে যা আইসোগ্যামির উদাহরণ। '
               'স্পাইরোগাইরায় গ্যামেটগুলি সমআকারের কিন্তু চলনহীন (ফ্ল্যাজেলাবিহীন)।',
    'expl_en': 'In Ulothrix, gametes are similar in size (isogamous) and flagellated (motile). In Spirogyra, gametes '
               'are similar in size but non-flagellated (non-motile).',
    'id': 'BIO-PK-011',
    'opts': { 'bn': [ 'ইউলোথ্রিক্স (Ulothrix) - চলনক্ষম ফ্ল্যাজেলাযুক্ত',
                      'স্পাইরোগাইরা (চলনহীন গ্যামেট)',
                      'ভলভক্স (উগ্যামাস)',
                      'ফিউকাস (উগ্যামাস)'],
              'en': [ 'Ulothrix (and flagellated forms of Chlamydomonas)',
                      'Spirogyra (non-flagellated)',
                      'Volvox (oogamous)',
                      'Fucus (oogamous)']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ফ্ল্যাজেলাবিহীন (চলনহীন) অথচ সমআকৃতির গ্যামেটের সমন্বয়ে আইসোগ্যামাস যৌন জনন কোনটিতে দেখা যায়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Isogamous sexual reproduction involving NON-FLAGELLATED (non-motile) but similar-sized gametes is seen in:',
    'exam': 'NEET, CUET',
    'expl_bn': 'NCERT অনুসারে: স্পাইরোগাইরায় গ্যামেট দুটি ফ্ল্যাজেলাবিহীন বা চলনহীন কিন্তু আকারে সমান হয়, যা '
               'আইসোগ্যামির একটি দৃষ্টান্ত।',
    'expl_en': 'As per NCERT: Gametes can be non-flagellated (non-motile) but similar in size, as in Spirogyra. Such '
               'reproduction is called isogamous.',
    'id': 'BIO-PK-012',
    'opts': { 'bn': ['স্পাইরোগাইরা (Spirogyra)', 'ইউলোথ্রিক্স', 'ভলভক্স', 'ফিউকাস'],
              'en': ['Spirogyra', 'Ulothrix', 'Volvox', 'Fucus']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'আকারে অসদৃশ দুটি গ্যামেটের মিলনকে (যেমন ইউডোরিনার ক্ষেত্রে) কী বলা হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Fusion of two gametes that are DISSIMILAR in size (as in some species of Eudorina) is termed:',
    'exam': 'NEET, CUET',
    'expl_bn': 'আকারে ভিন্ন বা অসদৃশ দুটি গ্যামেটের মিলনকে অ্যানাইসোগ্যামি (Anisogamy) বলা হয় (যেমন Eudorina শৈবালে)।',
    'expl_en': 'Fusion of two gametes dissimilar in size, as in species of Eudorina, is termed anisogamous.',
    'id': 'BIO-PK-013',
    'opts': { 'bn': ['অ্যানাইসোগ্যামাস (Anisogamous)', 'আইসোগ্যামাস', 'উগ্যামাস', 'পার্থেনোজেনেসিস'],
              'en': ['Anisogamous', 'Isogamous', 'Oogamous', 'Parthenogenesis']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'একটি বৃহৎ ও নিশ্চল স্ত্রী গ্যামেট এবং একটি ক্ষুদ্র ও চলনক্ষম পুং গ্যামেটের মিলনকে কী বলা হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Fusion between one large, non-motile female gamete and a smaller, motile male gamete is termed:',
    'exam': 'NEET, CUET',
    'expl_bn': 'একটি বৃহৎ নিশ্চল ডিম্বাণুর সাথে একটি ক্ষুদ্র সচল শুক্রাণুর মিলনকে উগ্যামি (Oogamy) বলে। উদাহরণ: Volvox '
               'এবং Fucus।',
    'expl_en': 'Fusion between one large, static female gamete and a smaller, motile male gamete is termed oogamous '
               '(e.g., Volvox, Fucus).',
    'id': 'BIO-PK-014',
    'opts': { 'bn': [ 'উগ্যামাস (Oogamous) - যেমন ভলভক্স, ফিউকাস',
                      'আইসোগ্যামাস - যেমন স্পাইরোগাইরা',
                      'অ্যানাইসোগ্যামাস - যেমন ইউডোরিনা',
                      'জুস্পোরের মিলন'],
              'en': [ 'Oogamous (e.g., Volvox, Fucus)',
                      'Isogamous (e.g., Spirogyra)',
                      'Anisogamous (e.g., Eudorina)',
                      'Syngamy of zoospores']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'বাণিজ্যিকভাবে গুরুত্বপূর্ণ জলধারণকারী পদার্থ অ্যালজিন (algin) এবং ক্যারাগিন (carrageen) যথাক্রমে কোন শৈবাল '
          'থেকে নিষ্কাশন করা হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Hydrocolloids (water-holding substances) algin and carrageen are commercially extracted respectively from:',
    'exam': 'NEET, CUET',
    'expl_bn': 'অ্যালজিন পাওয়া যায় বাদামী শৈবাল (Phaeophyceae) থেকে এবং ক্যারাগিন পাওয়া যায় লাল শৈবাল '
               '(Rhodophyceae) থেকে।',
    'expl_en': 'Certain marine brown and red algae produce large amounts of hydrocolloids; algin is obtained from '
               'brown algae and carrageen from red algae.',
    'id': 'BIO-PK-015',
    'opts': { 'bn': [ 'বাদামী শৈবাল এবং লাল শৈবাল',
                      'লাল শৈবাল এবং বাদামী শৈবাল',
                      'সবুজ শৈবাল এবং নীলাভ সবুজ শৈবাল',
                      'বাদামী শৈবাল এবং সবুজ শৈবাল'],
              'en': [ 'Brown algae and Red algae',
                      'Red algae and Brown algae',
                      'Green algae and Blue-green algae',
                      'Brown algae and Green algae']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'অণুজীব কালচার মিডিয়ায় এবং আইসক্রিম ও জেলি তৈরিতে ব্যবহৃত বাণিজ্যিক উপাদান অ্যাগার (Agar) কোন শৈবাল থেকে '
          'প্রস্তুত হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Agar, one of the commercial products used to grow microbes in culture media and in ice-creams and jellies, '
          'is obtained from:',
    'exam': 'NEET, CUET',
    'expl_bn': 'অ্যাগার পাওয়া যায় লাল শৈবাল জেলিডিয়াম এবং গ্র্যাসিলেয়ারিয়া থেকে।',
    'expl_en': 'Agar is obtained from red algae Gelidium and Gracilaria. It is widely used to solidify laboratory '
               'culture media.',
    'id': 'BIO-PK-016',
    'opts': { 'bn': [ 'জেলিডিয়াম (Gelidium) এবং গ্র্যাসিলেয়ারিয়া (Gracilaria)',
                      'ক্লোরেলা এবং স্পিরুলিনা',
                      'সারগাসাম এবং ল্যামিনারিয়া',
                      'ভলভক্স এবং ইউলোথ্রিক্স'],
              'en': [ 'Gelidium and Gracilaria',
                      'Chlorella and Spirulina',
                      'Sargassum and Laminaria',
                      'Volvox and Ulothrix']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'কোন এককোষী সবুজ শৈবালটি প্রোটিন সমৃদ্ধ এবং মহাকাশচারীদের খাদ্য পরিপূরক হিসেবে ব্যবহৃত হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which unicellular green alga is rich in proteins and used as a food supplement even by space travellers?',
    'exam': 'NEET, CUET',
    'expl_bn': 'ক্লোরেলা (Chlorella) হলো প্রোটিনসমৃদ্ধ এককোষী শৈবাল যা মহাকাশচারীদের খাদ্য পরিপূরক হিসেবে ব্যবহৃত হয়।',
    'expl_en': 'Chlorella is a unicellular green alga rich in proteins and vitamins, utilized as a nutrient supplement '
               'including space research flights.',
    'id': 'BIO-PK-017',
    'opts': { 'bn': ['ক্লোরেলা (Chlorella)', 'স্পাইরোগাইরা', 'কারা', 'উলভা'],
              'en': ['Chlorella', 'Spirogyra', 'Chara', 'Ulva']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ক্লোরোফাইসি (সবুজ শৈবাল)-এর অন্তর্ভুক্ত সদস্যদের প্রধান সালোকসংশ্লেষী রঞ্জকগুলি কী কী?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The photosynthetic pigments present in members of Chlorophyceae (green algae) are:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ক্লোরোফাইসির প্রধান রঞ্জক হলো ক্লোরোফিল-a এবং ক্লোরোফিল-b, যা উচ্চশ্রেণীর উদ্ভিদের সাথে সাদৃশ্যপূর্ণ।',
    'expl_en': 'Members of Chlorophyceae are grass green due to the dominance of pigments chlorophyll a and b located '
               'in definite chloroplasts.',
    'id': 'BIO-PK-018',
    'opts': { 'bn': [ 'নির্দিষ্ট ক্লোরোপ্লাস্টে অবস্থিত ক্লোরোফিল-a এবং ক্লোরোফিল-b',
                      'ফিউকোজ্যান্থিন সহ ক্লোরোফিল-a এবং ক্লোরোফিল-c',
                      'r-ফাইকোইরিথ্রিন সহ ক্লোরোফিল-a এবং ক্লোরোফিল-d',
                      'ফাইকোসায়ানিন সহ ক্লোরোফিল-b এবং ক্লোরোফিল-d'],
              'en': [ 'Chlorophyll a and Chlorophyll b localized in definite chloroplasts',
                      'Chlorophyll a and Chlorophyll c with fucoxanthin',
                      'Chlorophyll a and Chlorophyll d with r-phycoerythrin',
                      'Chlorophyll b and Chlorophyll d with phycocyanin']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'অধিকাংশ সবুজ শৈবালের ক্লোরোপ্লাস্টে অবস্থিত পাইরিনয়েড (Pyrenoids)-এর কেন্দ্রীয় অংশে ও বাইরে কী থাকে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Pyrenoids located in the chloroplasts of most green algae contain:',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাইরিনয়েডের কেন্দ্রে প্রোটিন থাকে এবং তার চারপাশ স্টার্চ বা শ্বেতসারের আবরণী দ্বারা বেষ্টিত থাকে।',
    'expl_en': 'Most green algae possess one or more storage bodies called pyrenoids located in chloroplasts. '
               'Pyrenoids contain protein besides starch (protein core surrounded by starch sheath).',
    'id': 'BIO-PK-019',
    'opts': { 'bn': [ 'কেন্দ্রে প্রোটিন এবং তাকে ঘিরে স্টার্চের আবরণ',
                      'প্রোটিন দ্বারা আবৃত খাঁটি লিপিডের কণা',
                      'সেলুলোজ দ্বারা আবৃত গ্লাইকোজেনের কেন্দ্র',
                      'পেকটিন দ্বারা আবৃত সিলিকার দানা'],
              'en': [ 'Protein in the centre surrounded by a starch sheath',
                      'Pure lipid droplets surrounded by protein coat',
                      'Glycogen core surrounded by cellulose crystals',
                      'Silica core surrounded by pectin layers']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'সবুজ শৈবালের (Chlorophyceae) দৃঢ় কোষপ্রাচীরের অভ্যন্তরীণ ও বহিঃস্থ স্তর যথাক্রমে কী দ্বারা গঠিত?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The cell wall of green algae (Chlorophyceae) is characteristically rigid and made of an:',
    'exam': 'NEET, CUET',
    'expl_bn': 'NCERT অনুসারে: সবুজ শৈবালের কোষপ্রাচীরের ভেতরের স্তরটি সেলুলোজ এবং বাইরের স্তরটি পেকটোজ দিয়ে গঠিত।',
    'expl_en': 'As per NCERT: Chlorophyceae members have a rigid cell wall made of an inner layer of cellulose and an '
               'outer layer of pectose.',
    'id': 'BIO-PK-020',
    'opts': { 'bn': [ 'অভ্যন্তরীণ সেলুলোজ স্তর এবং বহিঃস্থ পেকটোজ স্তর',
                      'অভ্যন্তরীণ কাইটিন এবং বহিঃস্থ সিলিকা',
                      'অভ্যন্তরীণ অ্যালজিন এবং বহিঃস্থ পেপটিডোগ্লাইক্যান',
                      'অভ্যন্তরীণ পেকটিন এবং বহিঃস্থ লিগনিন'],
              'en': [ 'Inner layer of cellulose and outer layer of pectose',
                      'Inner layer of chitin and outer layer of silica',
                      'Inner layer of algin and outer layer of peptidoglycan',
                      'Inner layer of pectin and outer layer of lignin']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ক্লোরোফাইসিতে অযৌন চলনক্ষম জুস্পোরের ফ্ল্যাজেলা সংক্রান্ত কোন বৈশিষ্ট্যটি সঠিক?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In Chlorophyceae, the asexual flagellated zoospores possess:',
    'exam': 'NEET, CUET',
    'expl_bn': 'সবুজ শৈবালের জুস্পোরে ২-৮টি সমদৈর্ঘ্যের অগ্রস্থ (apical) ফ্ল্যাজেলা থাকে।',
    'expl_en': 'Zoospores of green algae (Chlorophyceae) have 2-8 flagella that are equal in size and inserted '
               'apically (at the anterior end).',
    'id': 'BIO-PK-021',
    'opts': { 'bn': [ '২ থেকে ৮টি সমান দৈর্ঘ্যের অগ্রস্থ (apical) ফ্ল্যাজেলা',
                      '২টি অসমান দৈর্ঘ্যের পার্শ্বীয় (lateral) ফ্ল্যাজেলা',
                      'কোনো দশাতেই ফ্ল্যাজেলা থাকে না',
                      '১টি মাত্র পশ্চাৎ ফ্ল্যাজেলা'],
              'en': [ '2 to 8 equal, apical flagella',
                      '2 unequal, lateral flagella',
                      'No flagella at any stage',
                      '1 single posterior whiplash flagellum']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিচের কোনটি ক্লোরোফাইসি (Chlorophyceae) শ্রেণির অন্তর্ভুক্ত?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following belongs to Chlorophyceae?',
    'exam': 'NEET, CUET',
    'expl_bn': 'সবুজ শৈবালের সাধারণ উদাহরণ: Chlamydomonas, Volvox, Ulothrix, Spirogyra এবং Chara।',
    'expl_en': 'Common examples of Chlorophyceae listed in NCERT: Chlamydomonas, Volvox, Ulothrix, Spirogyra and '
               'Chara.',
    'id': 'BIO-PK-022',
    'opts': { 'bn': [ 'ক্ল্যামাইডোমোনাস, ভলভক্স, ইউলোথ্রিক্স, স্পাইরোগাইরা এবং কারা (Chara)',
                      'এক্টোকার্পাস, ডিকটিওটা, ল্যামিনারিয়া, সারগাসাম এবং ফিউকাস',
                      'পলিসাইফোনিয়া, পরফাইরা, গ্র্যাসিলেয়ারিয়া এবং জেলিডিয়াম',
                      'নস্টক, অ্যানাবিনা, স্পিরুলিনা এবং অস্সিলেটোরিয়া'],
              'en': [ 'Chlamydomonas, Volvox, Ulothrix, Spirogyra, and Chara',
                      'Ectocarpus, Dictyota, Laminaria, Sargassum, and Fucus',
                      'Polysiphonia, Porphyra, Gracilaria, and Gelidium',
                      'Nostoc, Anabaena, Spirulina, and Oscillatoria']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ফিওফাইসি (বাদামী শৈবাল)-র উদ্ভিদের বর্ণ জলপাই সবুজ থেকে বাদামীর বিভিন্ন শেড হওয়ার কারণ কোন জ্যান্থোফিল '
          'রঞ্জকের উপস্থিতি?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Members of Phaeophyceae (brown algae) range in colour from olive green to various shades of brown depending '
          'upon the amount of the xanthophyll pigment called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'বাদামী শৈবালে ক্লোরোফিল a, c ছাড়াও প্রচুর পরিমাণে ফিউকোজ্যান্থিন নামক জ্যান্থোফিল রঞ্জক থাকার কারণে '
               'এদের বর্ণ বাদামী হয়।',
    'expl_en': 'Brown algae possess chlorophyll a, c, carotenoids and xanthophylls; they vary in color depending on '
               'the proportion of the xanthophyll fucoxanthin.',
    'id': 'BIO-PK-023',
    'opts': { 'bn': ['ফিউকোজ্যান্থিন (Fucoxanthin)', 'r-ফাইকোইরিথ্রিন', 'হেমাটোক্রোম', 'লাইকোপিন'],
              'en': ['Fucoxanthin', 'r-phycoerythrin', 'Haematochrome', 'Lycopene']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ফিওফাইসি বা বাদামী শৈবালে সঞ্চিত খাদ্য জটিল শর্করা হিসেবে কোন রূপে অবস্থান করে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Food is stored in brown algae (Phaeophyceae) as complex carbohydrates in the form of:',
    'exam': 'NEET, CUET',
    'expl_bn': 'বাদামী শৈবালে সঞ্চিত খাদ্য থাকে জটিল কার্বোহাইড্রেট ল্যামিনারিন অথবা ম্যানিটল হিসেবে।',
    'expl_en': 'In Phaeophyceae, reserve food is stored as complex carbohydrates, which may be in the form of '
               'laminarin or mannitol (an alcoholic sugar).',
    'id': 'BIO-PK-024',
    'opts': { 'bn': [ 'ল্যামিনারিন (Laminarin) অথবা ম্যানিটল (Mannitol)',
                      'ফ্লোরিডিয়ান স্টার্চ',
                      'অ্যামাইলোজ ও অ্যামাইলোপেকটিন যুক্ত সাধারণ স্টার্চ',
                      'গ্লাইকোজেনের দানা'],
              'en': [ 'Laminarin or Mannitol',
                      'Floridean starch',
                      'True starch with amylose and amylopectin',
                      'Glycogen and cyanophycean starch']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'বাদামী শৈবালের সেলুলোজ কোষপ্রাচীরের বাইরে কোন জেলাটিনাস পদার্থের আবরণ থাকে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The cellulosic cell wall of brown algae is usually covered on the outside by a gelatinous coating of:',
    'exam': 'NEET, CUET',
    'expl_bn': 'বাদামী শৈবালের কোষপ্রাচীরের বাইরের দিকে অ্যালজিন (algin) নামক জেলাটিনাস আস্তরণ থাকে।',
    'expl_en': 'The vegetative cells in brown algae have a cellulosic wall usually covered on the outside by a '
               'gelatinous coating of algin (a phycocolloid).',
    'id': 'BIO-PK-025',
    'opts': { 'bn': ['অ্যালজিন (Algin)', 'পেকটোজ', 'ক্যারাগিন', 'কাইটিন'],
              'en': ['Algin', 'Pectose', 'Carrageen', 'Chitin']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'বাদামী শৈবালের উদ্ভিদদেহটি সাবস্ট্রেটামের সাথে যুক্ত থাকে ________ দ্বারা, এবং এতে একটি ডাঁটার মতো ________ '
          'এবং পাতার মতো সালোকসংশ্লেষী অঙ্গ ________ থাকে।',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The plant body of brown algae is usually attached to the substratum by a ________, and has a stalk, the '
          '________ and leaf like photosynthetic organ the ________.',
    'exam': 'NEET, CUET',
    'expl_bn': 'NCERT অনুসারে: বাদামী শৈবালের দেহটি সাবস্ট্রেটামের সাথে হোল্ডফাস্ট দ্বারা যুক্ত থাকে; এর সাথে ডাঁটার '
               'মতো স্ট্রাইপ এবং পাতার মতো সালোকসংশ্লেষী ফ্রন্ড থাকে।',
    'expl_en': 'As per NCERT: The plant body is usually attached to the substratum by a holdfast, and has a stalk, the '
               'stipe and leaf like photosynthetic organ - the frond.',
    'id': 'BIO-PK-026',
    'opts': { 'bn': [ 'হোল্ডফাস্ট (Holdfast), স্ট্রাইপ (Stipe), ফ্রন্ড (Frond)',
                      'রাইজয়েড, কাণ্ড, পাতা',
                      'মূল, পর্ব, ল্যামিনা',
                      'ফুট, সিটা, ক্যাপসুল'],
              'en': ['Holdfast, stipe, frond', 'Rhizoid, stem, leaf', 'Root, culm, lamina', 'Foot, seta, capsule']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ফিওফাইসি বা বাদামী শৈবালের অযৌন জুস্পোরগুলির বৈশিষ্ট্য কী?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Asexual zoospores in brown algae (Phaeophyceae) are distinctively:',
    'exam': 'NEET, CUET',
    'expl_bn': 'বাদামী শৈবালের জুস্পোরগুলি নাশপাতি আকৃতির (pyriform) হয় এবং এদের পাশে দুটি অসমান দৈর্ঘ্যের ফ্ল্যাজেলা '
               'যুক্ত থাকে।',
    'expl_en': 'Zoospores in Phaeophyceae are pear-shaped (pyriform) and bear two laterally attached, heterokont '
               '(unequal in length and type) flagella.',
    'id': 'BIO-PK-027',
    'opts': { 'bn': [ 'নাশপাতি আকৃতির (pyriform) এবং দুটি অসমান পার্শ্বীয় ফ্ল্যাজেলাযুক্ত',
                      'গোলাকার এবং ২-৮টি অগ্রস্থ সমান ফ্ল্যাজেলাযুক্ত',
                      'চলনহীন এবং বাটির মতো',
                      'কমা আকৃতির একটিমাত্র ফ্ল্যাজেলাযুক্ত'],
              'en': [ 'Pear-shaped (pyriform) with two laterally attached unequal flagella',
                      'Spherical with 2-8 apical equal flagella',
                      'Non-motile and cup-shaped',
                      'Comma-shaped with a single anterior flagellum']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিচের কোনটি একটি সরল শাখাযুক্ত সূত্রাকার বাদামী শৈবাল?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following is a simple branched, filamentous brown alga?',
    'exam': 'NEET, CUET',
    'expl_bn': 'এক্টোকার্পাস (Ectocarpus) হলো একটি সরল শাখাযুক্ত সূত্রাকার বাদামী শৈবাল।',
    'expl_en': 'Brown algae range from simple branched, filamentous forms (Ectocarpus) to profusely branched forms '
               '(Kelps).',
    'id': 'BIO-PK-028',
    'opts': { 'bn': ['এক্টোকার্পাস (Ectocarpus)', 'কেল্প', 'ফিউকাস', 'ডিকটিওটা'],
              'en': ['Ectocarpus', 'Kelps', 'Fucus', 'Dictyota']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'রোডোফাইসি (Rhodophyceae বা লাল শৈবাল)-র বিশিষ্ট লাল রঙের জন্য দায়ী প্রধান রঞ্জকটি কী?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The predominant photosynthetic pigment giving members of Rhodophyceae their characteristic red colour is:',
    'exam': 'NEET, CUET',
    'expl_bn': 'রোডোফাইসির সদস্যরা লাল শৈবাল নামে পরিচিত কারণ এদের দেহে লাল রঙের রঞ্জক r-ফাইকোইরিথ্রিনের আধিক্য থাকে।',
    'expl_en': 'The members of Rhodophyceae are commonly called red algae because of the predominance of the red '
               'pigment, r-phycoerythrin, in their body.',
    'id': 'BIO-PK-029',
    'opts': { 'bn': ['r-ফাইকোইরিথ্রিন (r-phycoerythrin)', 'ক্লোরোফিল c', 'ফিউকোজ্যান্থিন', 'ফাইকোসায়ানিন'],
              'en': ['r-phycoerythrin', 'Chlorophyll c', 'Fucoxanthin', 'c-phycocyanin']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'অধিকাংশ লাল শৈবাল কোথায় পাওয়া যায় এবং সমুদ্রের কোন গভীরতায় এরা বেঁচে থাকতে পারে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Where are majority of red algae found, and at what oceanic depths can they survive?',
    'exam': 'NEET, CUET',
    'expl_bn': 'লাল শৈবাল মূলত উষ্ণ সামুদ্রিক জলে বাস করে। এরা জলের উপরিভাগে যেমন থাকে, তেমনি সমুদ্রের গভীর তলদেশেও '
               'বেঁচে থাকে কারণ ফাইকোইরিথ্রিন নীল-সবুজ আলোক তরঙ্গ শোষণ করতে সক্ষম।',
    'expl_en': 'Majority of red algae are marine with greater concentrations in warmer areas. They occur both in '
               'well-lighted regions close to the water surface and at great depths in oceans where relatively little '
               'light penetrates.',
    'id': 'BIO-PK-030',
    'opts': { 'bn': [ 'বেশিরভাগই উষ্ণ সামুদ্রিক জলে, সমুদ্রপৃষ্ঠের সূর্যালোকিত এলাকা থেকে শুরু করে সমুদ্রের গভীর তলদেশ '
                      'পর্যন্ত যেখানে অতি সামান্য আলো প্রবেশ করে',
                      'কেবল শীতল পাহাড়ী ঝর্ণার মিষ্ট জলে',
                      'কেবল সমুদ্রের গভীরতম খাদে, কখনোই পৃষ্ঠতলে নয়',
                      'কেবল বদ্ধ নোংরা ডোবায় এবং আর্দ্র পাথরে'],
              'en': [ 'Mostly marine in warmer areas, occurring both at well-lighted surfaces and at great depths '
                      'where little light penetrates',
                      'Exclusively in cold freshwater mountain streams only',
                      'Deep marine abyssal trenches only, never near the ocean surface',
                      'Stagnant polluted puddles and damp terrestrial rocks only']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'রোডোফাইসিতে খাদ্য ফ্লোরিডিয়ান স্টার্চ (Floridean starch) হিসেবে সঞ্চিত থাকে, যা গঠনের দিক থেকে কার সাথে '
          'অত্যন্ত সাদৃশ্যপূর্ণ?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In Rhodophyceae (red algae), the reserve food material is stored as Floridean starch, which is structurally '
          'very similar to:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ফ্লোরিডিয়ান স্টার্চ গঠনের দিক থেকে প্রাণীদেহের গ্লাইকোজেন এবং উদ্ভিদের অ্যামাইলোপেকটিনের অত্যন্ত '
               'অনুরূপ।',
    'expl_en': 'Floridean starch is structurally very similar to amylopectin and glycogen, exhibiting alpha-(1,4) '
               'glucan chains with frequent alpha-(1,6) branches.',
    'id': 'BIO-PK-031',
    'opts': { 'bn': [ 'অ্যামাইলোপেকটিন এবং গ্লাইকোজেন (Amylopectin and Glycogen)',
                      'সেলুলোজ এবং ইনুলিন',
                      'ম্যানিটল এবং ল্যামিনারিন',
                      'কাইটিন এবং পেপটিডোগ্লাইক্যান'],
              'en': [ 'Amylopectin and Glycogen',
                      'Cellulose and Inulin',
                      'Mannitol and Laminarin',
                      'Chitin and Peptidoglycan']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'রোডোফাইসি বা লাল শৈবালের জননের একটি অনন্য প্রধান বৈশিষ্ট্য কী?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'A unique hallmark feature of reproduction in Rhodophyceae (red algae) is that:',
    'exam': 'NEET, CUET',
    'expl_bn': 'লাল শৈবালের সমগ্র জীবনচক্রে কোনো অবস্থাতেই কোনো ফ্ল্যাজেলা থাকে না। এদের অযৌন স্পোর ও যৌন গ্যামেট '
               'উভয়েই সম্পূর্ণ নিশ্চল (non-motile)।',
    'expl_en': 'Red algae completely lack any flagellated or motile stages throughout their entire life cycle. Asexual '
               'reproduction is by non-motile spores, and sexual reproduction is by non-motile gametes.',
    'id': 'BIO-PK-032',
    'opts': { 'bn': [ 'জীবনচক্রের কোনো দশাতেই কোনো প্রকার ফ্ল্যাজেলা থাকে না; অযৌন স্পোর এবং যৌন গ্যামেট উভয়েই '
                      'সম্পূর্ণ নিশ্চল বা চলনহীন',
                      'এদের জুস্পোরগুলি বহু-ফ্ল্যাজেলাযুক্ত হয়',
                      'পুং গ্যামেটের দুটি অসমান পার্শ্বীয় ফ্ল্যাজেলা থাকে',
                      'সাঁতার কাটা ফ্ল্যাজেলাযুক্ত শুক্রাণু দ্বারা নিষেক ঘটে'],
              'en': [ 'Both asexual spores (non-motile spores) and gametes (non-motile gametes) completely lack '
                      'flagella at ALL stages of life cycle',
                      'They produce multiflagellate ciliated zoospores',
                      'Male gametes possess two unequal lateral flagella',
                      'Fertilization occurs externally by swimming flagellated antherozoids']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'লাল শৈবালে (Rhodophyceae) যৌন জনন সর্বদা কোন প্রকৃতির হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Sexual reproduction in red algae (Rhodophyceae) is strictly:',
    'exam': 'NEET, CUET',
    'expl_bn': 'লাল শৈবালের যৌন জনন উন্নত উগ্যামাস প্রকৃতির এবং এতে নিষেক-পরবর্তী জটিল ভ্রূণীয় ও কার্পোস্পোরোফাইট '
               'বিকাশ দেখা যায়।',
    'expl_en': 'Sexual reproduction in Rhodophyceae is oogamous and accompanied by complex post-fertilization '
               'developments (forming carposporophytes).',
    'id': 'BIO-PK-033',
    'opts': { 'bn': [ 'উগ্যামাস (Oogamous) প্রকৃতির এবং নিষেক-পরবর্তী জটিল বিকাশ ও পরিবর্তনযুক্ত',
                      'ফ্ল্যাজেলাযুক্ত গ্যামেটের আইসোগ্যামাস মিলন',
                      'নিষেক-পরবর্তী পরিবর্তনহীন অ্যানাইসোগ্যামাস মিলন',
                      'বদ্ধ চেম্বারের ভেতরে ক্লিস্টোগ্যামাস মিলন'],
              'en': [ 'Oogamous, accompanied by complex post-fertilization developments',
                      'Isogamous with flagellated gametes',
                      'Anisogamous without post-fertilization changes',
                      'Cleistogamous inside closed chambers']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'NCERT-তে উল্লেখিত লাল শৈবাল (Rhodophyceae)-এর সাধারণ উদাহরণ কোনগুলি?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Common examples of Rhodophyceae (red algae) listed in NCERT include:',
    'exam': 'NEET, CUET',
    'expl_bn': 'লাল শৈবালের উদাহরণ: Polysiphonia, Porphyra, Gracilaria এবং Gelidium।',
    'expl_en': 'Common members of Rhodophyceae: Polysiphonia, Porphyra, Gracilaria and Gelidium.',
    'id': 'BIO-PK-034',
    'opts': { 'bn': [ 'পলিসাইফোনিয়া (Polysiphonia), পরফাইরা (Porphyra), গ্র্যাসিলেয়ারিয়া (Gracilaria) এবং '
                      'জেলিডিয়াম (Gelidium)',
                      'এক্টোকার্পাস, ডিকটিওটা, ল্যামিনারিয়া এবং সারগাসাম',
                      'ভলভক্স, ক্ল্যামাইডোমোনাস, ইউলোথ্রিক্স এবং কারা',
                      'স্ফ্যাগনাম, ফিউনারিয়া, মারকানশিয়া এবং রিকসিয়া'],
              'en': [ 'Polysiphonia, Porphyra, Gracilaria, and Gelidium',
                      'Ectocarpus, Dictyota, Laminaria, and Sargassum',
                      'Volvox, Chlamydomonas, Ulothrix, and Chara',
                      'Sphagnum, Funaria, Marchantia, and Riccia']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'পৃথিবীর মোট কার্বন ডাইঅক্সাইড সংবন্ধনের অন্তত অর্ধেক অংশ কার মাধ্যমে সম্পন্ন হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'At least a half of the total carbon dioxide fixation on earth is carried out by:',
    'exam': 'NEET, CUET',
    'expl_bn': 'NCERT অনুসারে: পৃথিবীতে সালোকসংশ্লেষের মাধ্যমে মোট কার্বন ডাইঅক্সাইড সংবন্ধনের প্রায় অর্ধেক অংশই '
               'শৈবাল দ্বারা সম্পন্ন হয়।',
    'expl_en': 'As per NCERT: At least a half of the total carbon dioxide fixation on earth is carried out by algae '
               'through photosynthesis, being of paramount importance as primary producers of energy-rich compounds.',
    'id': 'BIO-PK-035',
    'opts': { 'bn': [ 'সালোকসংশ্লেষের মাধ্যমে শৈবাল দ্বারা',
                      'ক্রান্তীয় চিরসবুজ ব্যক্তবীজী উদ্ভিদ দ্বারা',
                      'পিট ভূমির ব্রায়োফাইটা দ্বারা',
                      'CAM পথের মাধ্যমে মরুভূমির গুপ্তবীজী দ্বারা'],
              'en': [ 'Algae through photosynthesis',
                      'Tropical rainforest gymnosperms',
                      'Bryophytes growing on peat bogs',
                      'Desert angiosperms through CAM pathway']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': "ব্রায়োফাইটাকে সাধারণভাবে 'উদ্ভিদজগতের উভচর' বলা হয় কেন?",
    'correct': 0,
    'difficulty': 'Easy',
    'en': "Why are Bryophytes commonly called the 'amphibians of the plant kingdom'?",
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'ব্রায়োফাইট মাটিতে বাস করতে পারলেও যৌন জননে শুক্রাণুর আর্কেগোনিয়ামে পৌঁছানোর জন্য বাহ্যিক জলের '
               'প্রয়োজন হয়, তাই এদের উদ্ভিদজগতের উভচর বলা হয়।',
    'expl_en': 'Bryophytes are called amphibians of the plant kingdom because these plants can live in soil but are '
               'dependent on water for sexual reproduction (the flagellated antherozoids swim through water to reach '
               'the archegonium).',
    'id': 'BIO-PK-036',
    'opts': { 'bn': [ 'এরা আর্দ্র মাটিতে বাস করে কিন্তু যৌন জননের (চলনক্ষম শুক্রাণুর চলনের) জন্য জলের ওপর সম্পূর্ণ '
                      'নির্ভরশীল',
                      'এরা পাখনার সাহায্যে জলে সাঁতার কাটে এবং স্থলভাগে হামাগুড়ি দেয়',
                      'এরা দিনের অর্ধেক সময় সমুদ্রে এবং বাকি সময় শুষ্ক মরুভূমিতে কাটায়',
                      'এদের কাণ্ডে জাইলেম সংবহন কলা এবং জলে শ্বাস নেওয়ার ফুলকা থাকে'],
              'en': [ 'They live in soil but are dependent on water for sexual reproduction (transfer of flagellated '
                      'antherozoids)',
                      'They can swim in water using fins and crawl on land using tentacles',
                      'They spend half the day in ocean water and half the day on dry desert rocks',
                      'They possess vascular xylem vessels like terrestrial angiosperms and gills like aquatic fish']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্রায়োফাইটার জীবনচক্রের প্রধান, স্বাধীন এবং সালোকসংশ্লেষকারী দশাটি কোনটি?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The dominant, independent, photosynthetic phase in the life cycle of bryophytes is the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ব্রায়োফাইটার মূল উদ্ভিদদেহটি হ্যাপ্লয়েড এবং এটি গ্যামেট তৈরি করে বলে একে গ্যামেটোফাইট বলে। এটি '
               'সম্পূর্ণ স্বাধীন ও সালোকসংশ্লেষকারী।',
    'expl_en': 'The main plant body of the bryophyte is haploid. It produces gametes, hence is called a gametophyte. '
               'It is independent and photosynthetic.',
    'id': 'BIO-PK-037',
    'opts': { 'bn': [ 'হ্যাপ্লয়েড গ্যামেটোফাইট বা লিঙ্গধর উদ্ভিদ (গ্যামেট উৎপাদনকারী)',
                      'ডিপ্লয়েড স্পোরোফাইট বা রেণুধর উদ্ভিদ (স্পোর উৎপাদনকারী)',
                      'ট্রিপ্লয়েড এন্ডোস্পার্ম',
                      'সংবহনকলাযুক্ত রেণুধর গুঁড়ি'],
              'en': [ 'Haploid gametophyte (produces gametes)',
                      'Diploid sporophyte (produces spores)',
                      'Triploid endosperm',
                      'Vascular sporophytic leafy trunk']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিচের কোন বক্তব্যটি ব্রায়োফাইটার স্পোরোফাইট (রেণুধর উদ্ভিদ) সম্পর্কে সঠিক বিবরণ দেয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Which of the following statements accurately describes the sporophyte of bryophytes?',
    'exam': 'NEET, CUET',
    'expl_bn': 'ব্রায়োফাইটার স্পোরোফাইট স্বাধীনজীবী নয়, এটি গ্যামেটোফাইটের ওপর পুষ্টির জন্য পুরোপুরি বা আংশিকভাবে '
               'নির্ভরশীল থাকে।',
    'expl_en': 'The sporophyte is not free-living but attached to the photosynthetic gametophyte and derives '
               'nourishment from it.',
    'id': 'BIO-PK-038',
    'opts': { 'bn': [ 'এটি স্বাধীনভাবে বাঁচতে পারে না, বরং সালোকসংশ্লেষকারী গ্যামেটোফাইটের সাথে যুক্ত থেকে তা থেকে '
                      'পুষ্টি শোষণ করে',
                      'এটি সম্পূর্ণ স্বাধীন এবং শাখাযুক্ত কাষ্ঠল কাণ্ডবিশিষ্ট',
                      'এতে প্রকৃত মূল, বীজ ও ফল থাকে',
                      'এটি এককোষী এবং প্লাজমোগ্যামির সাথে সাথে মাইটোসিস বিভাজনে অংশ নেয়'],
              'en': [ 'It is not free-living, but physically attached to and nourished by the photosynthetic '
                      'gametophyte',
                      'It is completely independent, free-living, and bears branched woody trunks',
                      'It possesses true roots, seeds, and fruits',
                      'It is unicellular and undergoes mitosis immediately after plasmogamy']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্রায়োফাইটার জননাঙ্গ বহুকোষী ও বন্ধ্যা আবরণীযুক্ত। পুং জননাঙ্গকে ________ এবং স্ত্রী জননাঙ্গকে ________ '
          'বলে।',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The sex organs in bryophytes are multicellular and jacketed. The male sex organ is called ________ and '
          'female sex organ is called ________.',
    'exam': 'NEET, CUET',
    'expl_bn': 'পুং জননাঙ্গকে অ্যান্থেরিডিয়াম বলে যা দ্বি-ফ্ল্যাজেলাযুক্ত সচল শুক্রাণু তৈরি করে। স্ত্রী জননাঙ্গকে '
               'ফ্লাস্কের মতো দেখতে আর্কেগোনিয়াম বলে যাতে একটিমাত্র ডিম্বাণু থাকে।',
    'expl_en': 'The male sex organ is called antheridium producing biflagellate antherozoids. The female sex organ '
               'called archegonium is flask-shaped and produces a single egg.',
    'id': 'BIO-PK-039',
    'opts': { 'bn': [ 'অ্যান্থেরিডিয়াম (দ্বি-ফ্ল্যাজেলাযুক্ত শুক্রাণু তৈরি করে), আর্কেগোনিয়াম (ফ্লাস্ক-আকৃতির, একটি '
                      'ডিম্বাণু তৈরি করে)',
                      'আর্কেগোনিয়াম, অ্যান্থেরিডিয়াম',
                      'উগোনিয়াম, অ্যান্থেরিডিয়াম',
                      'কার্পোগোনিয়াম, স্পারমাটানজিয়াম'],
              'en': [ 'Antheridium (produces biflagellate antherozoids), Archegonium (flask-shaped, produces single '
                      'egg)',
                      'Archegonium, Antheridium',
                      'Oogonium, Antheridium',
                      'Carpogonium, Spermatangium']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'জলধারণ ক্ষমতার কারণে জীবিত উদ্ভিদ বা প্রাণীর এক স্থান থেকে অন্য স্থানে পরিবহনে এবং জ্বালানি হিসেবে ব্যবহৃত '
          'পিট (Peat) কোন ব্রায়োফাইট থেকে পাওয়া যায়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Peat, which has long been used as fuel and as packing material for trans-shipment of living material '
          'because of its water holding capacity, is provided by:',
    'exam': 'NEET, CUET',
    'expl_bn': 'স্ফ্যাগনাম (Sphagnum) মস থেকে পিট পাওয়া যায় যা জ্বালানি হিসেবে এবং তার চমৎকার জলধারণ ক্ষমতার কারণে '
               'জীবিত সামগ্রী পরিবহনে প্যাকিং বস্তু হিসেবে ব্যবহৃত হয়।',
    'expl_en': 'Sphagnum, a moss, provides peat that has long been used as fuel, and as packing material for '
               'trans-shipment of living material because of its tremendous water-holding capacity.',
    'id': 'BIO-PK-040',
    'opts': { 'bn': ['স্ফ্যাগনাম বা পিট মস (Sphagnum)', 'মারকানশিয়া', 'রিকসিয়া', 'ফিউনারিয়া'],
              'en': ['Sphagnum (Peat moss)', 'Marchantia polymorpha', 'Riccia fluitans', 'Funaria hygrometrica']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'লাইকেনের পাশাপাশি মস অত্যন্ত গুরুত্বপূর্ণ বাস্তুতান্ত্রিক তাৎপর্য বহন করে কারণ:',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Mosses along with lichens are of great ecological significance because:',
    'exam': 'NEET, CUET',
    'expl_bn': 'লাইকেন ও মস পাথরের ওপর সর্বপ্রথম পর্যায়ক্রম শুরু করে এবং পাথর ক্ষয় করে মাটি তৈরি করে উন্নত উদ্ভিদের '
               'জন্ম নিশ্চিত করে। এছাড়া মাটির ওপর ঘন গালিচা তৈরি করে ভূমিক্ষয় রোধ করে।',
    'expl_en': 'Mosses along with lichens are the pioneer organisms to colonise rocks and hence are of great '
               'ecological importance. They decompose rocks making the substrate fit for the growth of higher plants.',
    'id': 'BIO-PK-041',
    'opts': { 'bn': [ 'এরা প্রথম জীব যারা উন্মুক্ত পাথরে বসতি স্থাপন করে এবং পাথরকে ক্ষয় করে উন্নত উদ্ভিদের বৃদ্ধির '
                      'উপযোগী মাটি তৈরি করে',
                      'এরা কাণ্ডের নডিউলের সাহায্যে সরাসরি নাইট্রোজেন সংবন্ধন করে',
                      'এরা কাঠ ও রজন সরবরাহ করে',
                      'এরা সমুদ্রের জলের বাষ্পীভবন রোধ করে'],
              'en': [ 'They are the first organisms to colonise bare rocks and decompose them to make substrate '
                      'suitable for higher plants',
                      'They fix nitrogen directly through their stem nodules',
                      'They produce timber and resin for industrial use',
                      'They prevent evaporation of seawater into clouds']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'মারকানশিয়ার মতো লিভারওয়ার্টে বিশেষ ধরনের সবুজ, বহুকোষী অযৌন মুকুলের মাধ্যমে জনন সম্পন্ন হয়, যা কোন '
          'পেয়ালাকার পাত্রে গঠিত হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'In liverworts such as Marchantia, asexual reproduction occurs by specialized green, multicellular, asexual '
          'buds developed in small receptacles called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'মারকানশিয়ার থ্যালাসের ওপর অবস্থিত গেমা কাপের মধ্যে সবুজ, বহুকোষী অযৌন মুকুল বা গেমা (Gemmae) তৈরি '
               'হয়।',
    'expl_en': 'Asexual reproduction in liverworts takes place by fragmentation or by formation of specialised '
               'structures called gemmae. Gemmae are green, multicellular, asexual buds that develop in gemma cups '
               'located on the thallus.',
    'id': 'BIO-PK-042',
    'opts': { 'bn': [ 'গেমা কাপে (Gemma cups) উৎপন্ন গেমা (Gemmae)',
                      'অ্যাকাইনেট সকেটে উৎপন্ন অ্যাকাইনেট',
                      'কনিডিওফোরের ওপর কনিডিয়া',
                      'জুস্পোরাঞ্জিয়ামে জুস্পোর'],
              'en': [ 'Gemmae produced in gemma cups',
                      'Akinetes produced in akinete sockets',
                      'Conidia produced on conidiophores',
                      'Zoospores produced in zoosporangia']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'মারকানশিয়াতে পুং ও স্ত্রী জননাঙ্গ পৃথক পৃথক থ্যালাসের ওপর গঠিত হয়, যাদের যথাক্রমে কী বলা হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In Marchantia, the male and female sex organs are born on distinct thalli called respectively:',
    'exam': 'NEET, CUET',
    'expl_bn': 'মারকানশিয়া একটি ভিন্নবাসী (dioecious) উদ্ভিদ। পুং জননাঙ্গ ধারণকারী শাখাকে অ্যান্থেরিডিওফোর এবং স্ত্রী '
               'জননাঙ্গ ধারণকারী শাখাকে আর্কেগোনিওফোর বলে।',
    'expl_en': 'Marchantia is dioecious. The male receptacles are borne on stalks called antheridiophores, and female '
               'receptacles with ray-like projections are borne on archegoniophores.',
    'id': 'BIO-PK-043',
    'opts': { 'bn': [ 'অ্যান্থেরিডিওফোর (পুং থ্যালাসে) এবং আর্কেগোনিওফোর (স্ত্রী থ্যালাসে)',
                      'আর্কেগোনিওফোর (পুং) এবং অ্যান্থেরিডিওফোর (স্ত্রী)',
                      'স্পোরোফোর এবং গ্যামেটোফোর',
                      'পুংকেশর এবং গর্ভকেশর'],
              'en': [ 'Antheridiophore (on male thallus) and Archegoniophore (on female thallus)',
                      'Archegoniophore (on male) and Antheridiophore (on female)',
                      'Sporophore and Gametophore',
                      'Stamen and Carpel']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'লিভারওয়ার্ট এবং মসের রেণুধর দেহটি (Sporophyte) কোন তিনটি অংশে বিভক্ত?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The sporophyte of liverworts and mosses is differentiated into:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ব্রায়োফাইটার স্পোরোফাইট ফুট, সিটা এবং ক্যাপসুল নামক তিনটি অংশে বিভক্ত থাকে। ক্যাপসুলের ভেতর মায়োসিসের '
               'মাধ্যমে হ্যাপ্লয়েড রেণু উৎপন্ন হয়।',
    'expl_en': 'The sporophyte of bryophytes is differentiated into foot (anchorage/absorption), seta (stalk), and '
               'capsule (site of meiosis and spore formation).',
    'id': 'BIO-PK-044',
    'opts': { 'bn': [ 'ফুট (Foot), সিটা (Seta) এবং ক্যাপসুল (Capsule)',
                      'মূল, কাণ্ড এবং পাতা',
                      'হোল্ডফাস্ট, স্ট্রাইপ এবং ফ্রন্ড',
                      'রাইজোম, পত্রবৃন্ত এবং ফলক'],
              'en': [ 'Foot, seta, and capsule',
                      'Root, stem, and leaf',
                      'Holdfast, stipe, and frond',
                      'Rhizome, petiole, and blade']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'একটি মসের জীবনচক্রের প্রধান দশা হলো গ্যামেটোফাইট, যা কোন দুটি ক্রমান্বয়িক দশার সমন্বয়ে গঠিত?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The predominant stage of the life cycle of a moss is the gametophyte which consists of two stages:',
    'exam': 'NEET, CUET',
    'expl_bn': 'মসের গ্যামেটোফাইটের প্রথম দশাটি হলো প্রোটোনেমা (রেণু অঙ্কুরিত হয়ে তৈরি সূত্রাকার দশা) এবং দ্বিতীয় '
               'দশাটি হলো পত্রল দশা যা গৌণ প্রোটোনেমা থেকে পার্শ্বীয় মুকুলরূপে বিকশিত হয়।',
    'expl_en': 'The first stage of moss gametophyte is the protonema stage, which develops directly from a spore. The '
               'second stage is the leafy stage, which develops from a secondary protonema as a lateral bud.',
    'id': 'BIO-PK-045',
    'opts': { 'bn': [ 'প্রোটোনেমা দশা (রেণু থেকে সরাসরি উৎপন্ন শায়িত, সবুজ, শাখাযুক্ত) এবং পত্রল দশা (খাড়া অক্ষ ও '
                      'সর্পিলাকারে সজ্জিত পাতাযুক্ত)',
                      'রাইজয়েড দশা এবং পুষ্প দশা',
                      'স্পোরোফোর দশা এবং জাইগোট দশা',
                      'প্রাথমিক থ্যালাস এবং গৌণ কাষ্ঠ'],
              'en': [ 'Protonema stage (creeping, green, branched, developing directly from spore) and Leafy stage '
                      '(upright, slender axes with spirally arranged leaves)',
                      'Rhizoid stage and Flower stage',
                      'Sporophore stage and Zygote stage',
                      'Primary thallus and Secondary wood']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'মসের ক্ষেত্রে অঙ্গজ জনন খণ্ডীভবন এবং মুকুলোদগমের মাধ্যমে কোন দশায় সংঘটিত হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In mosses, vegetative reproduction takes place by fragmentation and budding in the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'মসের অঙ্গজ জনন ঘটে গৌণ প্রোটোনেমার (secondary protonema) খণ্ডীভবন ও মুকুলোদগমের মাধ্যমে।',
    'expl_en': 'Vegetative reproduction in mosses is by fragmentation and budding in the secondary protonema.',
    'id': 'BIO-PK-046',
    'opts': { 'bn': ['গৌণ প্রোটোনেমা (Secondary protonema)', 'ক্যাপসুলের প্রাচীর', 'ডিপ্লয়েড জাইগোট', 'কলুমেলা কোষ'],
              'en': ['Secondary protonema', 'Capsule wall', 'Diploid zygote', 'Columella cells']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিচের কোনটি মসের (Bryopsida) অন্তর্ভুক্ত সঠিক উদাহরণগুচ্ছ?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following is a representative moss?',
    'exam': 'NEET, CUET',
    'expl_bn': 'NCERT অনুসারে মসের সাধারণ উদাহরণ হলো ফিউনারিয়া, পলিট্রিকাম এবং স্ফ্যাগনাম।',
    'expl_en': 'Common examples of mosses given in NCERT are Funaria, Polytrichum, and Sphagnum.',
    'id': 'BIO-PK-047',
    'opts': { 'bn': [ 'ফিউনারিয়া (Funaria), পলিট্রিকাম (Polytrichum) এবং স্ফ্যাগনাম (Sphagnum)',
                      'মারকানশিয়া, রিকসিয়া এবং পেলিয়া',
                      'সাইলোটাম, লাইকোপোডিয়াম এবং সিলাজিনেলা',
                      'সাইকাস, পাইনাস এবং জিংগো'],
              'en': [ 'Funaria, Polytrichum, and Sphagnum',
                      'Marchantia, Riccia, and Pellia',
                      'Psilotum, Lycopodium, and Selaginella',
                      'Cycas, Pinus, and Ginkgo']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'রেণু বিচ্ছুরণের কৌশলটি তুলনামূলকভাবে অনেক বেশি জটিল ও উন্নত কোনটিতে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The mechanism of spore dispersal is more elaborate and sophisticated in:',
    'exam': 'NEET, CUET',
    'expl_bn': 'NCERT অনুসারে: লিভারওয়ার্টের তুলনায় মসের স্পোরোফাইট এবং ক্যাপসুল থেকে রেণু বিস্তারের কৌশল '
               '(হাইগ্রোস্কোপিক পেরিস্টোম দাঁতের মাধ্যমে) অনেক বেশি উন্নত ও জটিল।',
    'expl_en': 'As per NCERT: The sporophyte in mosses is more elaborate than that in liverworts. The moss capsule has '
               'an elaborate mechanism of spore dispersal (involving hygroscopic peristome teeth).',
    'id': 'BIO-PK-048',
    'opts': { 'bn': ['মসে (পেরিস্টোম দাঁতের উপস্থিতির কারণে)', 'লিভারওয়ার্টে', 'সবুজ শৈবালে', 'স্লাইম মোল্ডে'],
              'en': ['Mosses (due to peristome teeth)', 'Liverworts', 'Green algae', 'Slime moulds']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'কোন উদ্ভিদ গোষ্ঠী স্থলভাগে সর্বপ্রথম সংবহন কলা (জাইলেম ও ফ্লোয়েম)-র অধিকারী হয়েছিল?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which group of plants were the first terrestrial plants to possess vascular tissues (xylem and phloem)?',
    'exam': 'NEET, CUET',
    'expl_bn': 'বিবর্তনীয় দৃষ্টিকোণ থেকে টেরিডোফাইট হলো পৃথিবীর সর্বপ্রথম সংবহনকলাযুক্ত (জাইলেম ও ফ্লোয়েম বিশিষ্ট) '
               'স্থলজ উদ্ভিদ।',
    'expl_en': 'Evolutionarily, pteridophytes are the first terrestrial plants to possess vascular tissues — xylem and '
               'phloem.',
    'id': 'BIO-PK-049',
    'opts': { 'bn': ['টেরিডোফাইটা বা ফার্নবর্গ (Pteridophytes)', 'ব্রায়োফাইটা', 'ব্যক্তবীজী', 'গুপ্তবীজী'],
              'en': ['Pteridophytes', 'Bryophytes', 'Gymnosperms', 'Angiosperms']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'টেরিডোফাইটার জীবনচক্রের প্রধান বা আধিপত্যকারী দশাটি কোনটি?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In pteridophytes, the dominant phase in the life cycle is the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ব্রায়োফাইটার প্রধান দশা যেখানে গ্যামেটোফাইট, টেরিডোফাইটার ক্ষেত্রে প্রধান উদ্ভিদদেহটি হলো রেণুধর বা '
               'স্পোরোফাইট (2n), যা প্রকৃত মূল, কাণ্ড ও পাতায় বিভক্ত।',
    'expl_en': 'In bryophytes the dominant phase is the gametophyte, whereas in pteridophytes the main plant body is a '
               'sporophyte which is differentiated into true root, stem, and leaves.',
    'id': 'BIO-PK-050',
    'opts': { 'bn': [ 'স্পোরোফাইট (ডিপ্লয়েড, যা প্রকৃত মূল, কাণ্ড এবং পাতায় বিভেদিত)',
                      'গ্যামেটোফাইট (হ্যাপ্লয়েড সমাঙ্গদেহ)',
                      'মুক্ত ভাসমান প্রোটোনেমা',
                      'এন্ডোস্পার্মিক চোষক'],
              'en': [ 'Sporophyte (diploid, differentiated into true root, stem, and leaves)',
                      'Gametophyte (haploid thallus)',
                      'Free-floating protonema',
                      'Endospermic haustorium']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'টেরিডোফাইটার পাতা ক্ষুদ্রাকার (মাইক্রোফিল) হতে পারে যেমন ________-এ অথবা বৃহৎ (ম্যাক্রোফিল) হতে পারে যেমন '
          '________-এ।',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Leaves in pteridophytes can be small (microphylls) as in ________ or large (macrophylls/fronds) as in '
          '________.',
    'exam': 'NEET, CUET',
    'expl_bn': 'সিলাজিনেলায় ক্ষুদ্র মাইক্রোফিল পাতা থাকে এবং ফার্নে বৃহৎ ম্যাক্রোফিল বা ফ্রন্ড থাকে।',
    'expl_en': 'The leaves in pteridophyta are small (microphylls) as in Selaginella or large (macrophylls) as in '
               'ferns.',
    'id': 'BIO-PK-051',
    'opts': { 'bn': ['সিলাজিনেলা; ফার্ন', 'ফার্ন; সিলাজিনেলা', 'মারকানশিয়া; ফিউনারিয়া', 'পাইনাস; সাইকাস'],
              'en': ['Selaginella; Ferns', 'Ferns; Selaginella', 'Marchantia; Funaria', 'Pinus; Cycas']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'কিছু টেরিডোফাইটে রেণুপত্রগুলি পুঞ্জীভূত হয়ে সুনির্দিষ্ট শঙ্কু বা স্ট্রোবিলাস (strobili/cones) গঠন করে। এটি '
          'কোনটিতে দেখা যায়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In some pteridophytes, sporophylls may form distinct compact structures called strobili or cones. This is '
          'observed in:',
    'exam': 'NEET, CUET',
    'expl_bn': 'সিলাজিনেলা এবং ইকুইসিটামে রেণুপত্রগুলি ঘনভাবে সন্নিবেশিত হয়ে স্ট্রোবিলাস বা শঙ্কু (cone) গঠন করে।',
    'expl_en': 'In some cases sporophylls may form distinct compact structures called strobili or cones (e.g., '
               'Selaginella, Equisetum).',
    'id': 'BIO-PK-052',
    'opts': { 'bn': [ 'সিলাজিনেলা (Selaginella) এবং ইকুইসিটাম (Equisetum)',
                      'ড্রায়োপ্টেরিস এবং টেরিস',
                      'অ্যাডিয়েন্টাম এবং সালভিনিয়া',
                      'মারকানশিয়া এবং রিকসিয়া'],
              'en': [ 'Selaginella and Equisetum',
                      'Dryopteris and Pteris',
                      'Adiantum and Salvinia',
                      'Marchantia and Riccia']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'টেরিডোফাইটার রেণু অঙ্কুরিত হয়ে যে ক্ষুদ্র, বহুকোষী, স্বাধীনজীবী এবং প্রধানত সালোকসংশ্লেষকারী সমাঙ্গদেহী '
          'লিঙ্গধর দেহ গঠন করে তাকে কী বলে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The spores in pteridophytes germinate to give rise to inconspicuous, small but multicellular, free-living, '
          'mostly photosynthetic thalloid gametophytes called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'টেরিডোফাইটার হ্যাপ্লয়েড রেণু অঙ্কুরিত হয়ে যে স্বাধীন ও সবুজ সমাঙ্গদেহী লিঙ্গধর উদ্ভিদদেহ গঠন করে '
               'তাকে প্রোথ্যালাস (Prothallus) বলে।',
    'expl_en': 'The spores germinate to give rise to inconspicuous, small but multicellular, free-living, mostly '
               'photosynthetic thalloid gametophytes called prothallus.',
    'id': 'BIO-PK-053',
    'opts': { 'bn': ['প্রোথ্যালাস (Prothallus)', 'প্রোটোনেমা', 'আর্কেগোনিওফোর', 'এন্ডোস্পার্ম'],
              'en': ['Prothallus', 'Protonema', 'Archegoniophore', 'Endosperm']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'বর্তমান পৃথিবীতে জীবিত টেরিডোফাইটের ভৌগোলিক বিস্তৃতি কেন বেশ সীমিত এবং নির্দিষ্ট আর্দ্র অঞ্চলের মধ্যেই '
          'সীমাবদ্ধ?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Why is the geographical spread and distribution of living pteridophytes restricted and narrow?',
    'exam': 'NEET, CUET',
    'expl_bn': 'প্রোথ্যালাসের বৃদ্ধির জন্য আর্দ্র ও ছায়াময় স্থানের প্রয়োজনীয়তা এবং নিষেকের জন্য জলের অপরিহার্যতার '
               'কারণেই টেরিডোফাইটার বিস্তৃতি সীমিত ভৌগোলিক অঞ্চলে আবদ্ধ থাকে।',
    'expl_en': 'Because of the specific restricted requirement of gametophytes (cool, damp, shady habitats) and the '
               'unconditional requirement of water for fertilization, the spread of living pteridophytes is limited '
               'and restricted to narrow geographical zones.',
    'id': 'BIO-PK-054',
    'opts': { 'bn': [ 'কারণ এদের প্রোথ্যালাসের বৃদ্ধির জন্য শীতল, স্যাঁতসেঁতে ছায়াযুক্ত পরিবেশের প্রয়োজন এবং '
                      'শুক্রাণুর মিলনের জন্য জলের উপস্থিতি অপরিহার্য',
                      'কারণ এরা নোনা জল ছাড়া মিষ্টি জলে বাঁচে না',
                      'কারণ এদের মূল মাইকোরাইজা ছাড়া খনিজ শোষণ করতে পারে না',
                      'কারণ এদের বীজে কোনো প্রতিরক্ষামূলক আবরণ নেই'],
              'en': [ 'Because their gametophytes require cool, damp, shady places to grow and flagellated '
                      'antherozoids require water for fertilization',
                      'Because they are obligate halophytes unable to tolerate fresh water',
                      'Because their roots cannot absorb mineral ions without mycorrhiza',
                      'Because their seeds lack an impermeable protective coat']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'অধিকাংশ টেরিডোফাইট একই ধরনের রেণু উৎপন্ন করে (হোমোস্পোরাস)। কিন্তু যেসকল প্রজাতি ম্যাক্রোস্পোর (বড়) ও '
          'মাইক্রোস্পোর (ছোট) নামক দুই ধরনের ভিন্ন রেণু উৎপন্ন করে তাদের হেটারোস্পোরাস বলে। নিচের কোন জোড়াটি '
          'হেটারোস্পোরাস টেরিডোফাইটের উদাহরণ?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Majority of pteridophytes produce spores of a similar kind and are called homosporous. Genera which produce '
          'two kinds of spores, macro (large) and micro (small) spores, are called heterosporous. Which pair '
          'represents heterosporous pteridophytes?',
    'exam': 'NEET, CUET',
    'expl_bn': 'সিলাজিনেলা (Selaginella) এবং সালভিনিয়া (Salvinia) দুই ভিন্ন ধরনের রেণু উৎপন্ন করে, তাই এরা '
               'হেটারোস্পোরাস (heterosporous)।',
    'expl_en': 'Genera like Selaginella and Salvinia produce two kinds of spores, macro (megaspores) and microspores, '
               'and are termed heterosporous.',
    'id': 'BIO-PK-055',
    'opts': { 'bn': [ 'সিলাজিনেলা (Selaginella) এবং সালভিনিয়া (Salvinia)',
                      'ড্রায়োপ্টেরিস এবং টেরিস',
                      'ইকুইসিটাম এবং সাইলোটাম',
                      'লাইকোপোডিয়াম এবং অ্যাডিয়েন্টাম'],
              'en': [ 'Selaginella and Salvinia',
                      'Dryopteris and Pteris',
                      'Equisetum and Psilotum',
                      'Lycopodium and Adiantum']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'হেটারোস্পোরাস টেরিডোফাইটে মেগাস্পোর ও মাইক্রোস্পোর অঙ্কুরিত হয়ে যথাক্রমে কী গঠন করে?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'In heterosporous pteridophytes, the megaspores and microspores germinate and give rise to:',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'মেগাস্পোর বা গুরুরেণু অঙ্কুরিত হয়ে স্ত্রী গ্যামেটোফাইট এবং মাইক্রোস্পোর বা ক্ষুদ্ররেণু অঙ্কুরিত হয়ে '
               'পুং গ্যামেটোফাইট উৎপন্ন করে।',
    'expl_en': 'The megaspores and microspores germinate to give rise to female and male gametophytes, respectively. '
               'The female gametophytes in these plants are retained on the parent sporophytes for variable periods.',
    'id': 'BIO-PK-056',
    'opts': { 'bn': [ 'যথাক্রমে স্ত্রী গ্যামেটোফাইট এবং পুং গ্যামেটোফাইট',
                      'যথাক্রমে পুং গ্যামেটোফাইট এবং স্ত্রী গ্যামেটোফাইট',
                      'কোনো গ্যামেট ছাড়াই সরাসরি ডিপ্লয়েড স্পোরোফাইট',
                      'পিট মসের গালিচা'],
              'en': [ 'Female and male gametophytes respectively',
                      'Male and female gametophytes respectively',
                      'Diploid sporophytes directly without gametes',
                      'Peat moss cushions']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': "সিলাজিনেলা জাতীয় হেটারোস্পোরাস টেরিডোফাইটের কোন ঘটনাটিকে উদ্ভিদের 'বীজ স্বভাব' (Seed habit)-এর বিবর্তনের "
          'ক্ষেত্রে অত্যন্ত তাৎপর্যপূর্ণ অগ্রদূত হিসেবে গণ্য করা হয়?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Which event in heterosporous pteridophytes (like Selaginella) is considered an important precursor to the '
          "evolution of the 'seed habit'?",
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'স্ত্রী গ্যামেটোফাইটটি মাতৃ স্পোরোফাইটের ওপর যুক্ত থাকে এবং স্ত্রী গ্যামেটোফাইটের ভেতরেই জাইগোট থেকে '
               "ভ্রূণের বিকাশ ঘটে। এটিই বীজ স্বভাব বা 'Seed habit'-এর উৎপত্তি ও বিবর্তনের আদি ধাপ।",
    'expl_en': 'The female gametophyte is retained on the parent sporophyte for variable periods. The development of '
               'the zygote into a young embryo takes place within the female gametophyte. This event is a crucial '
               'precursor to the seed habit, considered an important evolutionary milestone.',
    'id': 'BIO-PK-057',
    'opts': { 'bn': [ 'মাতৃ স্পোরোফাইটের গায়ে স্ত্রী গ্যামেটোফাইটের সংলগ্ন থাকা এবং স্ত্রী গ্যামেটোফাইটের ভেতরেই '
                      'জাইগোট থেকে ভ্রূণের বিকাশ সাধন',
                      'কাণ্ডের সংবহন বান্ডিলের সম্পূর্ণ অবলুপ্তি',
                      'সমুদ্রের জলে হ্যাপ্লয়েড ফ্ল্যাজেলাযুক্ত স্পোর ত্যাগ করা',
                      'রেণুজনন কলায় মায়োসিসের অনুপস্থিতি'],
              'en': [ 'Retention of the female gametophyte on the parent sporophyte and development of the zygote into '
                      'young embryo within the female gametophyte',
                      'Loss of vascular bundles in the stem',
                      'Dispersal of free haploid flagellated spores in seawater',
                      'Absence of meiosis in the sporogenous tissue']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': "টেরিডোফাইটার কোন শ্রেণিতে 'হর্সটেল' (Horsetail) অন্তর্ভুক্ত?",
    'correct': 0,
    'difficulty': 'Easy',
    'en': "Which class of Pteridophytes includes 'Horsetails'?",
    'exam': 'NEET, CUET',
    'expl_bn': 'টেরিডোফাইটাকে চারটি শ্রেণিতে ভাগ করা হয়। এর মধ্যে স্ফেনোপসিডা (Sphenopsida)-র অন্তর্ভুক্ত হলো '
               'ইকুইসিটাম যা হর্সটেল নামে পরিচিত।',
    'expl_en': 'Pteridophytes are classified into four classes: Psilopsida (Psilotum); Lycopsida (Selaginella, '
               'Lycopodium); Sphenopsida (Equisetum - horsetails); Pteropsida (Dryopteris, Pteris, Adiantum).',
    'id': 'BIO-PK-058',
    'opts': { 'bn': [ 'স্ফেনোপসিডা (যেমন ইকুইসিটাম)',
                      'সাইলোপসিডা (যেমন সাইলোটাম)',
                      'লাইকোপসিডা (যেমন লাইকোপোডিয়াম)',
                      'টেরোপসিডা (যেমন ড্রায়োপ্টেরিস)'],
              'en': [ 'Sphenopsida (e.g., Equisetum)',
                      'Psilopsida (e.g., Psilotum)',
                      'Lycopsida (e.g., Lycopodium)',
                      'Pteropsida (e.g., Dryopteris)']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিচের কোন জোড়াটি লাইকোপসিডা (Lycopsida) শ্রেণির অন্তর্গত?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following belongs to class Lycopsida?',
    'exam': 'NEET, CUET',
    'expl_bn': 'লাইকোপসিডার অন্তর্ভুক্ত হলো সিলাজিনেলা এবং লাইকোপোডিয়াম।',
    'expl_en': 'Class Lycopsida includes club mosses like Selaginella and Lycopodium.',
    'id': 'BIO-PK-059',
    'opts': { 'bn': [ 'সিলাজিনেলা এবং লাইকোপোডিয়াম',
                      'সাইলোটাম এবং রাইনিয়া',
                      'ইকুইসিটাম এবং স্ফেনোফাইলাম',
                      'টেরিস এবং অ্যাডিয়েন্টাম'],
              'en': [ 'Selaginella and Lycopodium',
                      'Psilotum and Rhynia',
                      'Equisetum and Sphenophyllum',
                      'Pteris and Adiantum']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': "অ্যাডিয়েন্টাম (Adiantum)-কে সাধারণভাবে 'ওয়াকিং ফার্ন' (Walking fern) বলা হয় কেন?",
    'correct': 0,
    'difficulty': 'Easy',
    'en': "Adiantum is popularly referred to as the 'walking fern' because:",
    'exam': 'NEET, CUET',
    'expl_bn': 'অ্যাডিয়েন্টামের পাতার অগ্রভাগ ভিজে মাটি ছুঁলে সেখানে অস্থানিক মুকুল সৃষ্টি হয়ে নতুন উদ্ভিদ জন্মায়, '
               'তাই একে ওয়াকিং ফার্ন বলা হয়।',
    'expl_en': 'Adiantum caudatum is called the walking fern because when its vegetative frond tips touch moist soil, '
               'they produce adventitious roots and plantlets, propagating across the ground.',
    'id': 'BIO-PK-060',
    'opts': { 'bn': [ 'এর পাতার অগ্রভাগ মাটিতে স্পর্শ করলে সেখান থেকে অস্থানিক মুকুল ও নতুন চারাগাছ জন্মায়, ফলে মনে '
                      'হয় গাছটি হেঁটে চলেছে',
                      'বৃষ্টির দিনে চলার মতো পা থাকে',
                      'রাইজয়েড ক্ষণপদের মতো চলাচল করে',
                      'স্পোরের ডানা থাকে যা দিয়ে হেঁটে বেড়ায়'],
              'en': [ 'Its leaf tips bend and touch the soil to produce adventitious buds that establish new plants, '
                      'making it appear to walk',
                      'It has legs that allow it to walk during rainstorms',
                      'Its rhizoids move rapidly by amoeboid contractions',
                      'Its spores possess walking wings']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্যক্তবীজী বা জিম্নোস্পার্ম (Gymnosperms)-এর প্রধান শনাক্তকারী বৈশিষ্ট্য কী?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Gymnosperms (gymnos: naked, sperma: seeds) are characterized by having:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ব্যক্তবীজী উদ্ভিদে কোনো ডিম্বাশয় থাকে না, তাই ডিম্বকগুলি অনাবৃত অবস্থায় থাকে এবং নিষেকের পর গঠিত '
               'বীজগুলি নগ্ন অবস্থায় থাকে (কোনো ফল গঠিত হয় না)।',
    'expl_en': 'Gymnosperms are plants in which the ovules are not enclosed by an ovary wall and remain exposed, both '
               'before and after fertilisation. The seeds that develop post-fertilisation are not covered, i.e., are '
               'naked.',
    'id': 'BIO-PK-061',
    'opts': { 'bn': [ 'ডিম্বকগুলি কোনো ডিম্বাশয় প্রাচীর দ্বারা আবৃত থাকে না এবং নিষেকের পূর্বে ও পরে উভয় সময়েই '
                      'অনাবৃত অবস্থায় থাকে',
                      'বীজগুলি ফলের মাংসল ফলের ত্বকের ভেতরে সম্পূর্ণ ঢাকা থাকে',
                      'উজ্জ্বল পাপড়ি ও বৃত্যংশ বিশিষ্ট ফুল',
                      'দ্বি-নিষেক এবং ট্রিপ্লয়েড শস্য গঠন'],
              'en': [ 'Ovules that are not enclosed by any ovary wall and remain exposed both before and after '
                      'fertilization',
                      'Seeds enclosed completely inside fleshy pericarp of fruits',
                      'Flowers with vibrant petals and sepals',
                      'Double fertilization leading to triploid endosperm']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'বিশ্বের অন্যতম দীর্ঘতম কাষ্ঠল বৃক্ষদানব রেডউড (Sequoia) কোন উদ্ভিদ দলের অন্তর্ভুক্ত?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'One of the tallest tree species in the world, the giant redwood tree Sequoia, belongs to:',
    'exam': 'NEET, CUET',
    'expl_bn': 'বিশালকায় রেডউড গাছ সেকোয়া (Sequoia sempervirens) হলো একটি ব্যক্তবীজী (Gymnosperm) বৃক্ষ।',
    'expl_en': 'The giant redwood tree Sequoia is one of the tallest tree species and is a gymnosperm (conifer).',
    'id': 'BIO-PK-062',
    'opts': { 'bn': ['ব্যক্তবীজী (Gymnosperms)', 'টেরিডোফাইটা', 'গুপ্তবীজী', 'ব্রায়োফাইটা'],
              'en': ['Gymnosperms', 'Pteridophytes', 'Angiosperms', 'Bryophytes']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'পাইনাসে (Pinus) মূলের সাথে ছত্রাকের মিথোজীবী সম্পর্ককে ________ বলে, আর সাইকাসে (Cycas) নাইট্রোজেন '
          'সংবন্ধনকারী সায়ানোব্যাকটেরিয়া যুক্ত বিশেষ মূলকে ________ বলে।',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In Pinus, the roots have a symbiotic association with fungi called ________, whereas in Cycas, specialized '
          'roots called ________ are associated with N2-fixing cyanobacteria.',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাইনাসের মূলে ছত্রাকের মিথোজীবী সহাবস্থানকে মাইকোরাইজা বলে এবং সাইকাসের বিশেষ শাখান্বিত কোরালয়েড মূলে '
               'নাইট্রোজেন সংবন্ধনকারী অ্যানাবিনা বা নস্টক বাস করে।',
    'expl_en': 'Roots in Pinus have fungal association in the form of mycorrhizae, while in Cycas small specialised '
               'roots called coralloid roots are associated with N2-fixing cyanobacteria (Anabaena/Nostoc).',
    'id': 'BIO-PK-063',
    'opts': { 'bn': [ 'মাইকোরাইজা (Mycorrhiza); কোরালয়েড মূল (Coralloid roots)',
                      'কোরালয়েড মূল; মাইকোরাইজা',
                      'অর্বুদ; চোষক মূল',
                      'নিউম্যাটোফোর; পরাশ্রয়ী মূল'],
              'en': [ 'Mycorrhiza; Coralloid roots',
                      'Coralloid roots; Mycorrhiza',
                      'Nodules; Haustoria',
                      'Pneumatophores; Epiphytic roots']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্যক্তবীজী উদ্ভিদের কাণ্ডের শাখা সংক্রান্ত কোন তথ্যটি সঠিক?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Regarding stem branching in gymnosperms, which statement is correct?',
    'exam': 'NEET, CUET',
    'expl_bn': 'NCERT অনুসারে: সাইকাসের কাণ্ড অশাখ (স্তম্ভাকার) কিন্তু পাইনাস ও সিড্রাসের কাণ্ড প্রচুর শাখাযুক্ত।',
    'expl_en': 'As per NCERT: The stems are unbranched (Cycas) or branched (Pinus, Cedrus).',
    'id': 'BIO-PK-064',
    'opts': { 'bn': [ 'সাইকাসে (Cycas) কাণ্ড অশাখ (unbranched) কিন্তু পাইনাস (Pinus) ও সিড্রাসে (Cedrus) কাণ্ড '
                      'শাখাপ্রশাখা বিশিষ্ট (branched)',
                      'সাইকাসে কাণ্ড শাখাযুক্ত এবং পাইনাসে অশাখ',
                      'ব্যতিক্রমহীনভাবে সমস্ত ব্যক্তবীজীর কাণ্ড অশাখ',
                      'সমস্ত কনিফারে কাণ্ড মাটির নিচে ধাবক হিসেবে থাকে'],
              'en': [ 'The stem is unbranched in Cycas and branched in Pinus and Cedrus',
                      'The stem is branched in Cycas and unbranched in Pinus',
                      'Stems are unbranched in all gymnosperms without exception',
                      'Stems are underground creeping runners in all conifers']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'কনিফার উদ্ভিদেরা তীব্র তাপমাত্রা, শুষ্কতা ও প্রবল বাতাসের সাথে খাপ খাইয়ে টিকে থাকার জন্য কোন বৈশিষ্ট্যগুলি '
          'প্রদর্শন করে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Conifers are adapted to withstand extremes of temperature, humidity and wind by possessing:',
    'exam': 'NEET, CUET',
    'expl_bn': 'বাষ্পমোচন রোধের জন্য কনিফারদের পাতা সুচালো হয়, কিউটিকল অত্যন্ত পুরু হয় এবং পত্ররন্ধ্রগুলি গর্তের '
               'ভেতরে নিমজ্জিত (sunken) থাকে।',
    'expl_en': 'In conifers, the needle-like leaves reduce surface area. Their thick cuticle and sunken stomata also '
               'help to reduce water loss.',
    'id': 'BIO-PK-065',
    'opts': { 'bn': [ 'পৃষ্ঠতলের ক্ষেত্রফল কমানোর জন্য সুচালো ছুঁচলো পাতা, পুরু কিউটিকল এবং নিমজ্জিত পত্ররন্ধ্র '
                      '(sunken stomata)',
                      'চওড়া পাতলা পাতা ও প্রচুর জলরন্ধ্র',
                      'পাতলা কিউটিকল এবং পাতার কিনারায় বাইরের দিকে বের হওয়া পত্ররন্ধ্র',
                      'কিউটিকলহীন বৃহৎ যৌগিক পাতা'],
              'en': [ 'Needle-like leaves to reduce surface area, thick cuticle, and sunken stomata',
                      'Broad membranous leaves with abundant hydathodes',
                      'Thin cuticle with stomata protruding outward on leaf margins',
                      'Compound leaves with large surface area and no cuticle']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্যক্তবীজী উদ্ভিদেরা হোমোস্পোরাস নাকি হেটারোস্পোরাস?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Are gymnosperms homosporous or heterosporous?',
    'exam': 'NEET, CUET',
    'expl_bn': 'সমস্ত ব্যক্তবীজী উদ্ভিদই হেটারোস্পোরাস (heterosporous); এরা ক্ষুদ্ররেণু (মাইক্রোস্পোর) এবং গুরুরেণু '
               '(মেগাস্পোর) উৎপাদন করে।',
    'expl_en': 'Gymnosperms are heterosporous; they produce haploid microspores and megaspores.',
    'id': 'BIO-PK-066',
    'opts': { 'bn': [ 'সর্বদা হেটারোস্পোরাস (Heterosporous); এরা হ্যাপ্লয়েড ক্ষুদ্ররেণু (মাইক্রোস্পোর) এবং গুরুরেণু '
                      '(মেগাস্পোর) তৈরি করে',
                      'সর্বদা হোমোস্পোরাস',
                      'আদি ব্যক্তবীজীরা হোমোস্পোরাস এবং উন্নতরা হেটারোস্পোরাস',
                      'এরা কোনো প্রকার রেণুই তৈরি করে না'],
              'en': [ 'Strictly heterosporous; they produce haploid microspores and megaspores',
                      'Strictly homosporous; they produce identical spores',
                      'Primitive gymnosperms are homosporous; advanced conifers are heterosporous',
                      'They do not produce any spores at all']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্যক্তবীজীতে মাইক্রোস্পোরোফিল ও মাইক্রোস্পোরাঞ্জিয়া যুক্ত পুং শঙ্কু বা স্ট্রোবিলাসকে কী বলা হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In gymnosperms, the two kinds of spores are borne in sporangia on sporophylls which are arranged spirally '
          'along an axis to form lax or compact strobili or cones. The strobili bearing microsporophylls and '
          'microsporangia are called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'মাইক্রোস্পোরোফিল ও মাইক্রোস্পোরাঞ্জিয়া ধারণকারী শঙ্কুকে পুং স্ট্রোবিলাস বা মেল কোন বলা হয়।',
    'expl_en': 'The strobili bearing microsporophylls and microsporangia are called microsporangiate or male strobili.',
    'id': 'BIO-PK-067',
    'opts': { 'bn': [ 'মাইক্রোস্পোরাঞ্জিয়েট বা পুং স্ট্রোবিলাস (Male strobili)',
                      'ম্যাক্রোস্পোরাঞ্জিয়েট বা বীজ শঙ্কু',
                      'আর্কেগোনিওফোর',
                      'পুষ্পমঞ্জরী স্পাইক'],
              'en': [ 'Microsporangiate or male strobili',
                      'Macrosporangiate or seed cones',
                      'Archegoniophores',
                      'Inflorescence spike']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'মাইক্রোস্পোর বা পুংরেণু বিকশিত হয়ে অত্যন্ত সংক্ষিপ্ত ও স্বল্পকোষীয় পুং গ্যামেটোফাইট প্রজন্মে পরিণত হয়। '
          'এই সংক্ষিপ্ত গঠনটিকে কী বলা হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The microspores develop into a highly reduced male gametophyte generation consisting of only a limited '
          'number of cells. This reduced male gametophyte is known as a:',
    'exam': 'NEET, CUET',
    'expl_bn': 'মাইক্রোস্পোর বিকশিত হয়ে স্বল্পকোষযুক্ত সংক্ষিপ্ত পুং গ্যামেটোফাইটে পরিণত হয় যাকে পরাগরেণু (Pollen '
               'grain) বলে।',
    'expl_en': 'The microspores develop into a male gametophytic generation which is highly reduced and is confined to '
               'only a limited number of cells. This reduced gametophyte is called a pollen grain.',
    'id': 'BIO-PK-068',
    'opts': { 'bn': ['পরাগরেণু (Pollen grain)', 'প্রোথ্যালাস', 'শস্য বা এন্ডোস্পার্ম', 'নিউসেলাস'],
              'en': ['Pollen grain', 'Prothallus', 'Endosperm', 'Nucellus']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'পাইনাসে পুং ও স্ত্রী শঙ্কু ________ জন্মায়, অন্যদিকে সাইকাসে পুং শঙ্কু ও মেগাস্পোরোফিল ________ জন্মায়।',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In Pinus, the male and female cones are borne on ________, whereas in Cycas, male cones and megasporophylls '
          'are borne on ________.',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাইনাসের একই গাছে পুং ও স্ত্রী শঙ্কু উভয়ই জন্মায় (সহবাসী), কিন্তু সাইকাসে পুং গাছ এবং স্ত্রী গাছ '
               'সম্পূর্ণ পৃথক হয় (ভিন্নবাসী)।',
    'expl_en': 'The male or female cones may be borne on the same tree in Pinus (monoecious). In Cycas, male cones and '
               'megasporophylls are borne on different trees (dioecious).',
    'id': 'BIO-PK-069',
    'opts': { 'bn': [ 'একই গাছে (সহবাসী বা monoecious); পৃথক পৃথক গাছে (ভিন্নবাসী বা dioecious)',
                      'ভিন্ন ভিন্ন গাছে; একই গাছে',
                      'মাটির নিচের মূলে; বায়বীয় পাতার শীর্ষে',
                      'জলজ ডালে; শুষ্ক গুঁড়িতে'],
              'en': [ 'The same tree (monoecious); different trees (dioecious)',
                      'Different trees (dioecious); the same tree (monoecious)',
                      'Underground roots; aerial leaf tips',
                      'Aquatic branches; dry trunks']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্যক্তবীজী উদ্ভিদে মেগাস্পোর মাতৃকোষটি (Megaspore mother cell) কার একটি কোষ থেকে বিভেদিত হয়?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'In gymnosperms, the megaspore mother cell is differentiated from one of the cells of the:',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'নিউসেলাসের (nucellus) একটি কোষ রূপান্তরিত হয়ে মেগাস্পোর মাতৃকোষ গঠন করে। নিউসেলাস ত্বক দ্বারা আবৃত '
               'হয়ে ডিম্বক (ovule) তৈরি করে।',
    'expl_en': 'The megaspore mother cell is differentiated from one of the cells of the nucellus. The nucellus is '
               'protected by envelopes and the composite structure is called an ovule.',
    'id': 'BIO-PK-070',
    'opts': { 'bn': [ 'নিউসেলাস (Nucellus, যা ত্বক দ্বারা আবৃত থাকে এবং সমগ্র গঠনটি ডিম্বক গঠন করে)',
                      'মাইক্রোস্পোরাঞ্জিয়ামের বহিস্থ ট্যাপিটাম',
                      'স্ট্রাইপের বহিস্ত্বক',
                      'ত্বকের পাথুরে স্তর'],
              'en': [ 'Nucellus (which is protected by envelopes and composite structure is ovule)',
                      'Outer tapetum layer of microsporangium',
                      'Stipe epidermis',
                      'Integumentary stone layer']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্যক্তবীজী উদ্ভিদে মেগাস্পোর মাতৃকোষ মায়োসিস বিভাজনের মাধ্যমে চারটি মেগাস্পোর তৈরি করে। এদের মধ্যে কতগুলি '
          'সক্রিয় মেগাস্পোর বহুকোষী স্ত্রী গ্যামেটোফাইটে পরিণত হয়?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'In gymnosperms, the megaspore mother cell divides meiotically to form four megaspores. How many functional '
          'megaspores develop into a multicellular female gametophyte?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'চারটি মেগাস্পোরের মধ্যে তিনটি বিনষ্ট হয় এবং একটিমাত্র সক্রিয় মেগাস্পোর বহুকোষী স্ত্রী গ্যামেটোফাইটে '
               'পরিণত হয় যাতে দুই বা ততোধিক আর্কেগোনিয়া থাকে।',
    'expl_en': 'One of the megaspores enclosed within the megasporangium develops into a multicellular female '
               'gametophyte that bears two or more archegonia or female sex organs.',
    'id': 'BIO-PK-071',
    'opts': { 'bn': [ 'একটিমাত্র সক্রিয় মেগাস্পোর (যা মেগাস্পোরাঞ্জিয়ামের ভেতরে বহুকোষী স্ত্রী গ্যামেটোফাইটে '
                      'রূপান্তরিত হয়)',
                      'চারটি মেগাস্পোরই',
                      'দুটি মেগাস্পোর',
                      'তিনটি মেগাস্পোর'],
              'en': [ 'One functional megaspore (which develops into female gametophyte enclosed within '
                      'megasporangium)',
                      'All four functional megaspores',
                      'Two functional megaspores',
                      'Three functional megaspores']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্যক্তবীজী উদ্ভিদের শস্য বা এন্ডোস্পার্ম (Endosperm) হলো ________ এবং এটি নিষেকের ________ গঠিত হয়।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'The endosperm of gymnosperms is ________ and formed ________ fertilization.',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'ব্যক্তবীজী উদ্ভিদে শস্য মূলত স্ত্রী গ্যামেটোফাইটের রূপান্তরিত পুষ্টি কলা, যা নিষেকের আগেই তৈরি হয়; '
               'তাই এটি সর্বদা হ্যাপ্লয়েড (n)। গুপ্তবীজীতে এটি নিষেকের পরে গঠিত ট্রিপ্লয়েড (3n)।',
    'expl_en': 'In gymnosperms, the endosperm directly represents the multicellular vegetative tissue of the haploid '
               'female gametophyte and is formed BEFORE fertilization (hence haploid, n). In angiosperms, it is '
               'triploid (3n) formed after double fertilization.',
    'id': 'BIO-PK-072',
    'opts': { 'bn': [ 'হ্যাপ্লয়েড (n); পূর্বে',
                      'ট্রিপ্লয়েড (3n); পরে',
                      'ডিপ্লয়েড (2n); পরে',
                      'টেট্রাপ্লয়েড (4n); পূর্বে'],
              'en': ['Haploid (n); before', 'Triploid (3n); after', 'Diploid (2n); after', 'Tetraploid (4n); before']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্রায়োফাইটা এবং টেরিডোফাইটার বিপরীতে, ব্যক্তবীজী উদ্ভিদে পুং এবং স্ত্রী গ্যামেটোফাইটগুলির ক্ষেত্রে কোন '
          'বৈশিষ্ট্যটি পরিলক্ষিত হয়?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Unlike bryophytes and pteridophytes, in gymnosperms the male and female gametophytes:',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'ব্রায়োফাইট বা ফার্নের মতো ব্যক্তবীজীর গ্যামেটোফাইটের কোনো স্বাধীন জীবন নেই; এরা মাতৃ স্পোরোফাইটের '
               'স্পোরাঞ্জিয়ামের ভেতরেই আশ্রয় ও পুষ্টি লাভ করে।',
    'expl_en': 'Unlike bryophytes and pteridophytes, in gymnosperms the male and female gametophytes do not have an '
               'independent free-living existence. They remain within the sporangia retained on the sporophytes.',
    'id': 'BIO-PK-073',
    'opts': { 'bn': [ 'কোনো স্বাধীন বা মুক্তজীবী অস্তিত্ব থাকে না, বরং তারা স্পোরোফাইটের গায়ে সংলগ্ন স্পোরাঞ্জিয়ার '
                      'ভেতরেই আবদ্ধ থাকে',
                      'সম্পূর্ণ স্বাধীনজীবী এবং সালোকসংশ্লেষকারী থ্যালাস',
                      'মুক্ত জলাশয়ে সাঁতার কাটার মতো বহু-সিলিয়াযুক্ত শুক্রাণু তৈরি করে',
                      'স্যাঁতসেঁতে মাটিতে সবুজ শায়িত প্রোটোনেমা গঠন করে'],
              'en': [ 'Do not have an independent, free-living existence and remain within the sporangia retained on '
                      'sporophytes',
                      'Are free-living, independent, and photosynthetic thalli',
                      'Bear multi-ciliated swimming antherozoids requiring open pond water',
                      'Form creeping green protonema on wet forest floors']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্যক্তবীজী উদ্ভিদে পরাগযোগ মূলত কার দ্বারা সম্পন্ন হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In gymnosperms, pollination is primarily carried out by:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ব্যক্তবীজী উদ্ভিদে পরাগরেণুগুলি বায়ুপ্রবাহের মাধ্যমে পরিবাহিত হয়ে মেগাস্পোরোফিলের ডিম্বকরন্ধ্রে এসে '
               'পৌঁছায় (বায়ুপরাগী বা Anemophilous)।',
    'expl_en': 'Pollen grains are released from the microsporangium and carried in air currents (wind pollination) to '
               'come into contact with the opening of the ovules borne on megasporophylls.',
    'id': 'BIO-PK-074',
    'opts': { 'bn': ['বায়ু প্রবাহ দ্বারা (Anemophily)', 'পতঙ্গ দ্বারা', 'জলস্রোত দ্বারা', 'বাদুড় দ্বারা'],
              'en': [ 'Air currents (Anemophily)',
                      'Insects (Entomophily)',
                      'Water currents (Hydrophily)',
                      'Bats (Chiropterophily)']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্যক্তবীজীতে আর্কেগোনিয়ামের মুখে শুক্রাণু পৌঁছানোর জন্য কোন গঠনটি তৈরি হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The transfer of male gametes to the archegonia in gymnosperms occurs via a structure called the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'পরাগরেণু থেকে পরাগনালী (pollen tube) উৎপন্ন হয়ে শুক্রাণুকে সরাসরি আর্কেগোনিয়ামের মুখে পৌঁছে দেয়। এই '
               'পদ্ধতিকে সাইফোনোগ্যামি (siphonogamy) বলে।',
    'expl_en': 'The pollen tube carrying the male gametes grows towards archegonia in the ovules and discharges its '
               'contents near the mouth of the archegonia (siphonogamous fertilization).',
    'id': 'BIO-PK-075',
    'opts': { 'bn': [ 'পরাগনালী বা পোলেন টিউব (Siphonogamy)',
                      'ফ্ল্যাজেলার আনডুলেটিং পর্দা',
                      'মিউসিলেজের সূত্র',
                      'জলের মেনিস্কাস'],
              'en': [ 'Pollen tube (Siphonogamy)',
                      'Flagellar undulating membrane',
                      'Mucilage thread',
                      'Water meniscus']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': "ব্যক্তবীজী উদ্ভিদের মধ্যে কোনটিকে চলনক্ষম ফ্ল্যাজেলাযুক্ত শুক্রাণু এবং পাখার মতো পাতাবিশিষ্ট 'জীবন্ত "
          "জীবাশ্ম' বলা হয়?",
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following is a living fossil among gymnosperms that possesses motile flagellated sperm and '
          'fan-shaped leaves?',
    'exam': 'NEET, CUET',
    'expl_bn': 'Ginkgo biloba হলো ব্যক্তবীজীদের মধ্যে একটি জীবন্ত জীবাশ্ম যার আদিম বৈশিষ্ট্য হিসেবে ফ্ল্যাজেলাযুক্ত '
               'সচল শুক্রাণু দেখা যায়।',
    'expl_en': 'Ginkgo biloba (maidenhair tree) is a living fossil gymnosperm displaying primitive traits including '
               'flagellated male gametes and fan-shaped dichotomy in venation.',
    'id': 'BIO-PK-076',
    'opts': { 'bn': ['জিংগো বাইলোবা (Ginkgo biloba)', 'পাইনাস রক্সবারঘি', 'সিড্রাস দেওদারা', 'এফেড্রা'],
              'en': ['Ginkgo biloba', 'Pinus roxburghii', 'Cedrus deodara', 'Ephedra foliata']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': "শ্বাসকষ্ট ও হাঁপানির উপশমে ব্যবহৃত ওষুধ 'এফেড্রিন' (Ephedrine) কোন ব্যক্তবীজী উদ্ভিদ থেকে নিষ্কাশন করা হয়?",
    'correct': 0,
    'difficulty': 'Medium',
    'en': "The drug 'Ephedrine' used in curing respiratory ailments is extracted from the gymnosperm:",
    'exam': 'NEET, CUET',
    'expl_bn': 'এফেড্রা (Ephedra) নামক ব্যক্তবীজী উদ্ভিদ থেকে হাঁপানির মহৌষধ এফেড্রিন পাওয়া যায়।',
    'expl_en': 'Ephedrine is an alkaloid obtained from Ephedra, a gymnosperm belonging to Gnetales, used to treat '
               'asthma and respiratory congestion.',
    'id': 'BIO-PK-077',
    'opts': {'bn': ['এফেড্রা (Ephedra)', 'পাইনাস', 'সাইকাস', 'নিটাম'], 'en': ['Ephedra', 'Pinus', 'Cycas', 'Gnetum']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': "স্থায়ী মাইক্রোস্কোপিক স্লাইড তৈরিতে ব্যবহৃত মাউন্টিং মিডিয়াম 'কানাডা বালসাম' কোন ব্যক্তবীজী থেকে প্রস্তুত "
          'হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Canada balsam, a mounting medium used for permanent microscopic slides, is obtained from:',
    'exam': 'NEET, CUET',
    'expl_bn': 'অ্যাবিজ বালসামিয়া (Abies balsamea) নামক কনিফার ব্যক্তবীজীর রজন থেকে কানাডা বালসাম প্রস্তুত করা হয়।',
    'expl_en': 'Canada balsam is a resin obtained from the balsam fir tree (Abies balsamea), a gymnosperm conifer.',
    'id': 'BIO-PK-078',
    'opts': { 'bn': [ 'অ্যাবিজ বালসামিয়া (Abies balsamea)',
                      'পাইনাস সিলভেস্ট্রিস',
                      'সাইকাস রেভোলুটা',
                      'ট্যাক্সাস ব্যাক্কাটা'],
              'en': ['Abies balsamea', 'Pinus sylvestris', 'Cycas revoluta', 'Taxus baccata']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': "কোন উদ্ভিদটিকে 'সাবু পাম' বলা হয় যার কাণ্ডের মজ্জা থেকে ভোজ্য সাবুদানা প্রস্তুত করা হয়?",
    'correct': 0,
    'difficulty': 'Easy',
    'en': "Which of the following is commonly known as 'Sago palm' yielding edible starch from its stem pith?",
    'exam': 'NEET, CUET',
    'expl_bn': 'সাইকাসের (Cycas revoluta) কাণ্ডের মজ্জা থেকে স্টার্চ সংগ্রহ করে সাবু বা সাবুদানা প্রস্তুত করা হয়।',
    'expl_en': 'Starch extracted from the stem pith of Cycas revoluta and Cycas rumphii is processed to yield edible '
               'sago (sabudana).',
    'id': 'BIO-PK-079',
    'opts': { 'bn': ['সাইকাস রেভোলুটা (Cycas revoluta)', 'পাইনাস পাইনিয়া', 'জিংগো', 'ট্যাক্সাস'],
              'en': ['Cycas revoluta', 'Pinus pinea', 'Ginkgo biloba', 'Taxus brevifolia']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্যক্তবীজীদের জাইলেমে ভেসেল ও ফ্লোয়েমে সঙ্গী কোষ অনুপস্থিত থাকে, তবে এর ব্যতিক্রমী উন্নত কোন বর্গটিতে '
          'প্রকৃত ভেসেল উপস্থিত থাকে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Vessels in xylem and companion cells in phloem are characteristically absent in gymnosperms EXCEPT in which '
          'advanced order?',
    'exam': 'NEET, CUET',
    'expl_bn': 'ব্যক্তবীজী নিটালেস বর্গের (Gnetum, Ephedra, Welwitschia) জাইলেমে ব্যতিক্রমীভাবে গুপ্তবীজীর ন্যায় '
               'উন্নত ভেসেল উপাদান বর্তমান থাকে।',
    'expl_en': 'Gnetales (Gnetum, Ephedra, and Welwitschia) are advanced gymnosperms showing angiospermic affinities, '
               'including the presence of true vessels in their secondary xylem.',
    'id': 'BIO-PK-080',
    'opts': { 'bn': [ 'নিটালেস বা Gnetales (Gnetum, Ephedra, Welwitschia)',
                      'কনিফারেলেস (পাইনাস, সিড্রাস)',
                      'সাইকাডালেস (সাইকাস)',
                      'জিংগোয়ালেস (জিংগো)'],
              'en': [ 'Gnetales (Gnetum, Ephedra, Welwitschia)',
                      'Coniferales (Pinus, Cedrus)',
                      'Cycadales (Cycas)',
                      'Ginkgoales (Ginkgo)']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'গুপ্তবীজী বা অ্যাঞ্জিওস্পার্ম উদ্ভিদে বীজগুলি কার ভেতরে আবদ্ধ থাকে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'In Angiosperms, seeds are enclosed inside:',
    'exam': 'NEET, CUET',
    'expl_bn': 'গুপ্তবীজীতে ডিম্বকগুলি ডিম্বাশয়ের ভেতরে আবদ্ধ থাকে এবং নিষেকের পর ডিম্বাশয়টি ফলে রূপান্তরিত হয়ে '
               'বীজকে আবৃত করে রাখে।',
    'expl_en': 'Unlike gymnosperms where ovules are naked, in angiosperms the pollen grains and ovules are developed '
               'in specialised structures called flowers and seeds are enclosed inside fruits.',
    'id': 'BIO-PK-081',
    'opts': { 'bn': [ 'ফল (পরিপক্ব ডিম্বাশয় প্রাচীর দ্বারা গঠিত)',
                      'অনাবৃত শঙ্কু শল্ক',
                      'আর্কেগোনিয়ামের গ্রীবানালী',
                      'পেরিস্টোম দাঁত'],
              'en': [ 'Fruits (derived from the ripened ovary wall)',
                      'Naked cone scales',
                      'Archegonial neck canal',
                      'Peristome teeth']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ক্ষুদ্রতম গুপ্তবীজী উদ্ভিদ হলো ________ এবং ১০০ মিটারেরও বেশি উচ্চতা বিশিষ্ট দীর্ঘতম গুপ্তবীজী বৃক্ষ হলো '
          '________।',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The smallest angiosperm is ________ and the tallest angiosperm tree is ________ reaching over 100 meters.',
    'exam': 'NEET, CUET',
    'expl_bn': 'সবচেয়ে ক্ষুদ্রাকার গুপ্তবীজী হলো Wolffia (ক্ষুদ্র জলজ উদ্ভিদ) এবং সবচেয়ে উঁচু গুপ্তবীজী বৃক্ষ হলো '
               'Eucalyptus (১০০ মিটারের বেশি)। (Sequoia হলো ব্যক্তবীজী)।',
    'expl_en': 'The smallest angiosperm is microscopic Wolffia and the tallest is Eucalyptus (which can grow over 100 '
               'metres). Note that Sequoia is a gymnosperm!',
    'id': 'BIO-PK-082',
    'opts': { 'bn': [ 'উলফিয়া (Wolffia); ইউক্যালিপটাস (Eucalyptus)',
                      'ইউক্যালিপটাস; উলফিয়া',
                      'লেমনা; সেকোয়া',
                      'ক্লোরেলা; ম্যাক্রোসিস্টাস'],
              'en': ['Wolffia; Eucalyptus', 'Eucalyptus; Wolffia', 'Lemna; Sequoia', 'Chlorella; Macrocystis']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'গুপ্তবীজী উদ্ভিদকে দুটি প্রধান শ্রেণিতে ভাগ করা হয়: দ্বিবীজপত্রী এবং একবীজপত্রী। নিচের কোন বৈশিষ্ট্যটি '
          'দ্বিবীজপত্রী উদ্ভিদের পরিচায়ক?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Angiosperms are divided into two primary classes: Dicotyledons and Monocotyledons. Which of the following '
          'features characterizes Dicotyledons?',
    'exam': 'NEET, CUET',
    'expl_bn': 'দ্বিবীজপত্রী উদ্ভিদের বীজে দুটি বীজপত্র, পাতায় জালকাকার শিরাবিন্যাস এবং ফুলে ৪ বা ৫-এর গুণিতকে '
               'পুষ্পপত্র (টেট্রামেরাস বা পেন্টামেরাস) থাকে।',
    'expl_en': 'The dicotyledons are characterized by seeds having two cotyledons, reticulate venation in leaves, and '
               'tetramerous or pentamerous flowers.',
    'id': 'BIO-PK-083',
    'opts': { 'bn': [ 'বীজে দুটি বীজপত্র, পাতায় জালকাকার শিরাবিন্যাস এবং চতুরংশ বা পঞ্চাংশক বিশিষ্ট ফুল',
                      'বীজে একটিমাত্র বীজপত্র, সমান্তরাল শিরাবিন্যাস এবং ত্রেয়াংশক ফুল',
                      'গৌণ বৃদ্ধির অনুপস্থিতি এবং কাণ্ডে বিক্ষিপ্ত সংবহন বান্ডিল',
                      'স্থানিক প্রধান মূলহীন গুচ্ছমূল ব্যবস্থা'],
              'en': [ 'Two cotyledons in seeds, reticulate venation in leaves, and tetramerous or pentamerous flowers',
                      'Single cotyledon in seeds, parallel venation in leaves, and trimerous flowers',
                      'Absence of secondary growth and scattered vascular bundles in stem',
                      'Fibrous root system without any primary taproot']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'গুপ্তবীজী উদ্ভিদের এক অনন্য বৈশিষ্ট্যপূর্ণ ঘটনা যাতে সিঙ্গ্যামি (ডিপ্লয়েড জাইগোট গঠন) এবং ট্রিপল ফিউশন '
          '(ট্রিপ্লয়েড প্রাথমিক শস্য নিউক্লিয়াস গঠন) একসাথে ঘটে, তাকে কী বলে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The characteristic event unique to Angiosperms that involves Syngamy (yielding 2n zygote) and Triple Fusion '
          '(yielding 3n PEN) is known as:',
    'exam': 'NEET, CUET',
    'expl_bn': 'একটি পুং গ্যামেট ডিম্বাণুকে নিষিক্ত করে জাইগোট (2n) এবং অপর পুং গ্যামেট নির্ণীত নিউক্লিয়াসকে নিষিক্ত '
               'করে ট্রিপ্লয়েড শস্য (3n) তৈরি করে। এই জোড়া ঘটনাকে দ্বি-নিষেক বলে।',
    'expl_en': 'Double fertilisation is an event unique to angiosperms, where one male gamete fuses with the egg '
               '(syngamy) and the other fuses with the secondary diploid nucleus (triple fusion).',
    'id': 'BIO-PK-084',
    'opts': { 'bn': ['দ্বি-নিষেক (Double fertilization)', 'অ্যাপোমিক্সিস', 'পার্থেনোকার্পি', 'পলিএমব্রায়োনি'],
              'en': ['Double fertilization', 'Apomixis', 'Parthenocarpy', 'Polyembryony']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'হ্যাপ্লন্টিক (Haplontic) জীবনচক্রের ক্ষেত্রে নিচের কোন বক্তব্যটি সঠিক?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'In a HAPLONTIC life cycle, which of the following statements is TRUE?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'হ্যাপ্লন্টিক জীবনচক্রে স্পোরোফাইট দশা বলতে কেবল ডিপ্লয়েড জাইগোটকেই বোঝায়। জাইগোটে সরাসরি মায়োসিস '
               'বিভাজন (Zygotic meiosis) ঘটে এবং হ্যাপ্লয়েড দশাটিই প্রধান উদ্ভিদদেহ হিসেবে থাকে।',
    'expl_en': 'In haplontic life cycles, the sporophytic generation is represented only by the one-celled zygote. '
               'There are no free-living sporophytes. Meiosis in the zygote results in the formation of haploid '
               'spores.',
    'id': 'BIO-PK-085',
    'opts': { 'bn': [ 'স্পোরোফাইট প্রজন্মটি কেবলমাত্র এককোষী ডিপ্লয়েড জাইগোট দ্বারা প্রতিনিধিত্ব হয়; কোনো মুক্তজীবী '
                      'স্পোরোফাইট থাকে না',
                      'প্রধান সালোকসংশ্লেষকারী দশাটি হলো বহুকোষী ডিপ্লয়েড বৃক্ষ',
                      'গ্যামেট তৈরিতে গ্যামেটানজিয়ামে মায়োসিস ঘটে',
                      'গ্যামেটোফাইট এবং স্পোরোফাইট উভয়ই সমানভাবে দীর্ঘজীবী ও মুক্তজীবী'],
              'en': [ 'Sporophytic generation is represented only by the one-celled diploid zygote; there are no '
                      'free-living sporophytes',
                      'The dominant photosynthetic phase is a large multicellular diploid tree',
                      'Meiosis occurs in gametangia to produce haploid gametes',
                      'Both gametophyte and sporophyte are equally dominant and free-living']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিচের কোন শৈবালটিতে আদর্শ হ্যাপ্লন্টিক (Haplontic) জীবনচক্র দেখা যায়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following algae exhibits a typical HAPLONTIC life cycle?',
    'exam': 'NEET, CUET',
    'expl_bn': 'Volvox, Spirogyra এবং Chlamydomonas-এর জীবনচক্র হলো হ্যাপ্লন্টিক প্রকৃতির।',
    'expl_en': 'Many algae such as Volvox, Spirogyra, and some species of Chlamydomonas represent the haplontic life '
               'cycle pattern.',
    'id': 'BIO-PK-086',
    'opts': { 'bn': [ 'ভলভক্স, স্পাইরোগাইরা এবং ক্ল্যামাইডোমোনাস',
                      'ফিউকাস এবং সারগাসাম',
                      'এক্টোকার্পাস এবং পলিসাইফোনিয়া',
                      'কেল্প এবং ল্যামিনারিয়া'],
              'en': [ 'Volvox, Spirogyra, and Chlamydomonas',
                      'Fucus and Sargassum',
                      'Ectocarpus and Polysiphonia',
                      'Kelps and Laminaria']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ডিপ্লন্টিক (Diplontic) জীবনচক্রে উদ্ভিদের প্রধান, স্বাধীন এবং সালোকসংশ্লেষকারী দশাটি কোনটি?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'In a DIPLONTIC life cycle, which phase is the dominant, photosynthetic, independent phase of the plant?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'ডিপ্লন্টিক জীবনচক্রে ডিপ্লয়েড (2n) স্পোরোফাইট দশাটিই প্রধান ও স্বাধীন। গ্যামেটোফাইট অত্যন্ত সংক্ষিপ্ত '
               'এবং পরাগরেণু বা ভ্রূণস্থলীর কয়েক কোষে সীমাবদ্ধ থাকে।',
    'expl_en': 'In a diplontic life cycle, the diploid sporophyte is the dominant, photosynthetic, independent phase '
               'of the plant. The gametophytic phase is represented by the single to few-celled haploid gametophyte.',
    'id': 'BIO-PK-087',
    'opts': { 'bn': [ 'ডিপ্লয়েড স্পোরোফাইট (গ্যামেটোফাইট দশা এককোষী বা স্বল্পকোষীতে সীমাবদ্ধ থাকে)',
                      'হ্যাপ্লয়েড গ্যামেটোফাইট',
                      'প্রোথ্যালাস',
                      'গৌণ প্রোটোনেমা'],
              'en': [ 'Diploid sporophyte (gametophyte is reduced to single or few-celled stage)',
                      'Haploid gametophyte (sporophyte is reduced to one cell)',
                      'Prothallus',
                      'Secondary protonema']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'অধিকাংশ শৈবালের ব্যতিক্রম হিসেবে নিচের কোন শৈবালটিতে ডিপ্লন্টিক (Diplontic) জীবনচক্র দেখা যায়?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Which ALGA represents an exception by displaying a DIPLONTIC life cycle (unlike most other green algae)?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'NCERT-এর অত্যন্ত গুরুত্বপূর্ণ ব্যতিক্রম: Fucus নামক বাদামী শৈবালটিতে ডিপ্লন্টিক জীবনচক্র দেখা যায়।',
    'expl_en': 'An alga, Fucus sp., represents a diplontic life cycle pattern (NCERT specific exception highlight). In '
               'addition, all seed-bearing plants (gymnosperms and angiosperms) follow this pattern.',
    'id': 'BIO-PK-088',
    'opts': { 'bn': ['ফিউকাস (Fucus)', 'ভলভক্স', 'স্পাইরোগাইরা', 'কারা'],
              'en': ['Fucus', 'Volvox', 'Spirogyra', 'Chara']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'হ্যাপ্লোডিপ্লন্টিক (Haplodiplontic) জীবনচক্রে উভয় দশাই বহুকোষী হয়। কোন উদ্ভিদ গোষ্ঠীগুলির জীবনচক্রের মূল '
          'বৈশিষ্ট্য হলো হ্যাপ্লোডিপ্লন্টিক ধরন?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'In a HAPLODIPLONTIC life cycle, both phases are multicellular. Which plant groups characteristically '
          'exhibit a haplodiplontic life cycle?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'ব্রায়োফাইটা এবং টেরিডোফাইটা উভয় দলেই সুস্পষ্ট হ্যাপ্লোডিপ্লন্টিক (Haplodiplontic) জীবনচক্র দেখা '
               'যায়, যেখানে রেণুধর ও লিঙ্গধর উভয় দশাই বহুকোষী।',
    'expl_en': 'Bryophytes and pteridophytes, interestingly, exhibit an intermediate condition — haplodiplontic life '
               'cycle, wherein both haploid and diploid phases are multicellular.',
    'id': 'BIO-PK-089',
    'opts': { 'bn': [ 'ব্রায়োফাইটা এবং টেরিডোফাইটা',
                      'গুপ্তবীজী এবং ব্যক্তবীজী',
                      'ফিউকাস এবং ভলভক্স',
                      'সায়ানোব্যাকটেরিয়া এবং মাইকোপ্লাজমা'],
              'en': [ 'Bryophytes and Pteridophytes',
                      'Angiosperms and Gymnosperms',
                      'Fucus and Volvox',
                      'Cyanobacteria and Mycoplasma']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্রায়োফাইটার হ্যাপ্লোডিপ্লন্টিক জীবনচক্র কীভাবে টেরিডোফাইটার হ্যাপ্লোডিপ্লন্টিক জীবনচক্র থেকে পৃথক?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'How does the haplodiplontic life cycle of a Bryophyte differ from that of a Pteridophyte?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'ব্রায়োফাইটাতে লিঙ্গধর বা গ্যামেটোফাইট দশা প্রধান ও স্বাধীন এবং স্পোরোফাইট তার ওপর নির্ভরশীল। কিন্তু '
               'টেরিডোফাইটাতে রেণুধর বা স্পোরোফাইট দশা প্রধান ও উন্নত সংবহনকলাযুক্ত।',
    'expl_en': 'In Bryophytes, the dominant, independent, photosynthetic phase is a haploid gametophyte, alternating '
               'with a short-lived dependent sporophyte. In Pteridophytes, the diploid sporophyte is the dominant, '
               'independent, vascular phase alternating with a multicellular independent saprophytic/autotrophic '
               'prothallus.',
    'id': 'BIO-PK-090',
    'opts': { 'bn': [ 'ব্রায়োফাইটাতে প্রধান দশা হলো স্বাধীন গ্যামেটোফাইট; কিন্তু টেরিডোফাইটাতে প্রধান দশা হলো স্বাধীন '
                      'সংবহনকলাযুক্ত স্পোরোফাইট',
                      'ব্রায়োফাইটাতে স্পোরোফাইট স্বাধীন ও সংবহনযুক্ত; কিন্তু টেরিডোফাইটাতে তা পরজীবী',
                      'ব্রায়োফাইটাতে গ্যামেটিক মায়োসিস এবং টেরিডোফাইটাতে জাইগোটিক মায়োসিস ঘটে',
                      'ব্রায়োফাইটাতে বীজ তৈরি হয় এবং টেরিডোফাইটাতে বীজ অনাবৃত থাকে'],
              'en': [ 'In Bryophytes, the dominant phase is the free-living gametophyte; in Pteridophytes, the '
                      'dominant phase is the independent vascular sporophyte',
                      'In Bryophytes, the sporophyte is free-living and vascular; in Pteridophytes, it is parasitic',
                      'In Bryophytes, meiosis is gametic; in Pteridophytes, meiosis is zygotic',
                      'In Bryophytes, seeds are formed; in Pteridophytes, seeds are naked']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিচের কোন শৈবালগুলি সাধারণ শৈবালের হ্যাপ্লন্টিক দশার ব্যতিক্রম হিসেবে হ্যাপ্লোডিপ্লন্টিক (Haplodiplontic) '
          'জীবনচক্র প্রদর্শন করে?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Which of the following algae exhibit HAPLODIPLONTIC life cycles (deviating from the typical haplontic '
          'condition of algae)?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'NCERT-এর অতি গুরুত্বপূর্ণ তথ্য: অধিকাংশ শৈবাল হ্যাপ্লন্টিক হলেও Ectocarpus, Polysiphonia এবং Kelps হলো '
               'হ্যাপ্লোডিপ্লন্টিক (Haplodiplontic)।',
    'expl_en': 'NCERT explicitly notes: Interestingly, while most algal genera are haplontic, some of them such as '
               'Ectocarpus, Polysiphonia, kelps are haplodiplontic. Fucus, an alga, is diplontic.',
    'id': 'BIO-PK-091',
    'opts': { 'bn': [ 'এক্টোকার্পাস, পলিসাইফোনিয়া এবং কেল্প (Ectocarpus, Polysiphonia, Kelps)',
                      'ভলভক্স, স্পাইরোগাইরা এবং ক্ল্যামাইডোমোনাস',
                      'ফিউকাস এবং সারগাসাম',
                      'ক্লোরেলা এবং সিনেডেস্মাস'],
              'en': [ 'Ectocarpus, Polysiphonia, and Kelps',
                      'Volvox, Spirogyra, and Chlamydomonas',
                      'Fucus and Sargassum',
                      'Chlorella and Scenedesmus']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'কোন উদ্ভিদ গোষ্ঠীতে পুং গ্যামেট পরাগনালী গঠন না করে শুধুমাত্র জলের ফোঁটায় সাঁতার কেটে স্ত্রী গ্যামেটের '
          'কাছে পৌঁছায়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'In which plant group do the male gametes reach the female gamete exclusively by swimming through water '
          'droplets without forming a pollen tube?',
    'exam': 'NEET, CUET',
    'expl_bn': 'ব্রায়োফাইট এবং টেরিডোফাইটে ফ্ল্যাজেলাযুক্ত শুক্রাণু জলের ফিল্মের মধ্য দিয়ে সাঁতার কেটে ডিম্বাণুর '
               'কাছে যায় (Zooidogamy)।',
    'expl_en': 'Bryophytes and lower pteridophytes show zooidogamy, where ciliated/flagellated male gametes swim '
               'through film of water to reach the archegonium. Seed plants use siphonogamy (pollen tube).',
    'id': 'BIO-PK-092',
    'opts': { 'bn': [ 'ব্রায়োফাইটা এবং টেরিডোফাইটা (Zooidogamy)',
                      'ব্যক্তবীজী এবং গুপ্তবীজী',
                      'কেবল গুপ্তবীজী',
                      'কেবল কনিফার'],
              'en': [ 'Bryophytes and Pteridophytes (Zooidogamy)',
                      'Gymnosperms and Angiosperms',
                      'Angiosperms only',
                      'Conifers only']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'সাইকাসের কোরালয়েড মূলগুলি ঋণাত্মক অভিকর্ষবর্তী এবং এদের কর্টেক্সে কোন মিথোজীবী বাস করে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Coralloid roots of Cycas exhibit negative geotropism and contain endosymbionts in their cortical zone. '
          'These endosymbionts are:',
    'exam': 'NEET, CUET',
    'expl_bn': 'সাইকাসের কোরালয়েড মূলের কর্টেক্সে নাইট্রোজেন সংবন্ধনকারী নীলাভ সবুজ শৈবাল নস্টক (Nostoc) ও অ্যানাবিনা '
               '(Anabaena) বাস করে।',
    'expl_en': 'Coralloid roots of Cycas possess a distinct blue-green algal zone in the middle cortex harbouring '
               'Nostoc and Anabaena for nitrogen fixation.',
    'id': 'BIO-PK-093',
    'opts': { 'bn': ['নস্টক এবং অ্যানাবিনা (সায়ানোব্যাকটেরিয়া)', 'গ্লোমাস (ছত্রাক)', 'রাইজোবিয়াম', 'ফ্রাঙ্কিয়া'],
              'en': [ 'Nostoc and Anabaena (Cyanobacteria)',
                      'Glomus (Mycorrhizal fungus)',
                      'Rhizobium leguminosarum',
                      'Frankia actinomycete']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'পাইনাসের স্ত্রী শঙ্কু (Female cone) মূলত কিসের সমতুল্য?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The female cone of Pinus corresponds to:',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাইনাসের স্ত্রী শঙ্কু একটি যৌগিক স্ট্রোবিলাস যাতে অক্ষের চারিদিকে ব্র্যাক্ট স্কেল ও ওভিউলিফেরাস '
               'স্কেলের ওপর ডিম্বক ধারণকারী মেগাস্পোরোফিল বিন্যস্ত থাকে।',
    'expl_en': 'The female cone in Pinus is a compound strobilus consisting of a central cone axis bearing bract '
               'scales and ovuliferous scales (megasporophyll complex).',
    'id': 'BIO-PK-094',
    'opts': { 'bn': [ 'একটি কেন্দ্রীয় অক্ষের চারদিকে সর্পিলাকারে সজ্জিত ওভিউলিফেরাস স্কেলযুক্ত মেগাস্পোরোফিলের স্তবক',
                      'দুটি ডিম্বকযুক্ত একটিমাত্র রূপান্তরিত পাতা',
                      'মাইক্রোস্পোরোফিলের পুষ্পমঞ্জরী',
                      'সূচাকার পাতাবিশিষ্ট ক্ষুদ্র বিটপ'],
              'en': [ 'A cluster of megasporophylls bearing ovuliferous scales arranged on a central axis',
                      'A single modified leaf with two ovules',
                      'An inflorescence of microsporophylls',
                      'A vegetative dwarf shoot with needle leaves']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': "প্রোটিন ও তেল সমৃদ্ধ সুস্বাদু শুষ্ক ফল 'চিলগোজা' (Chilgoza) কোন ব্যক্তবীজী গাছের বীজ?",
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Chilgoza, an edible dry fruit rich in proteins and oil, is the seed of:',
    'exam': 'NEET, CUET',
    'expl_bn': 'চিলগোজা হলো পাইনাস জেরার্ডিয়ানা (Pinus gerardiana) নামক ব্যক্তবীজী বৃক্ষের পুষ্টিকর ভক্ষণযোগ্য বীজ।',
    'expl_en': 'Chilgoza nuts are the roasted seeds of Pinus gerardiana (the Chilgoza pine), native to northwestern '
               'Himalayas.',
    'id': 'BIO-PK-095',
    'opts': { 'bn': ['পাইনাস জেরার্ডিয়ানা (Pinus gerardiana)', 'পাইনাস রক্সবারঘি', 'সাইকাস সারসিনালিস', 'জিংগো'],
              'en': ['Pinus gerardiana', 'Pinus roxburghii', 'Cycas circinalis', 'Ginkgo biloba']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'সবুজ শৈবাল কারায় (Chara) বহুকোষী স্ত্রী জননাঙ্গ (নাকিউল বা Nucule) এবং পুং জননাঙ্গ (গ্লোবিউল বা Globule) '
          'কীভাবে অবস্থিত?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In Chara, the multicellular jacketed female sex organ (Nucule) and male sex organ (Globule) are located:',
    'exam': 'NEET, CUET',
    'expl_bn': 'কারা (Chara)-র ক্ষেত্রে স্ত্রী জননাঙ্গ নাকিউল (Nucule) উপরের দিকে এবং পুং জননাঙ্গ গ্লোবিউল (Globule) '
               'নিচের দিকে একই পর্বে অবস্থান করে।',
    'expl_en': 'In the green alga Chara, the female oogonium (nucule) is oval and located above the spherical male '
               'antheridium (globule) on the nodes of short branches.',
    'id': 'BIO-PK-096',
    'opts': { 'bn': [ 'নাকিউল (স্ত্রী অঙ্গ) উপরে এবং গ্লোবিউল (পুং অঙ্গ) নিচে একই পর্বের ওপর অবস্থিত',
                      'গ্লোবিউল উপরে এবং নাকিউল নিচে অবস্থিত',
                      'উভয়ই ক্রিপ্টের মধ্যে লুকানো',
                      'নাকিউল পাতার শীর্ষে এবং গ্লোবিউল মূলে'],
              'en': [ 'Nucule is situated UPPER (above) and Globule is situated LOWER (below) on the same node',
                      'Globule is situated above and Nucule is situated below',
                      'Both are inside antheridial crypts',
                      'Nucule on leaf tips and Globule on roots']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'মসের ক্যাপসুলের কোন অংশটি শুষ্ক অবস্থায় হাইগ্রোস্কোপিক চলনের মাধ্যমে রেণু মুক্ত করতে সাহায্য করে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which part of the moss capsule is responsible for releasing spores under dry conditions by hygroscopic '
          'movement?',
    'exam': 'NEET, CUET',
    'expl_bn': 'মসের ক্যাপসুলের মুখে থাকা হাইগ্রোস্কোপিক পেরিস্টোম দাঁত বাতাসে আর্দ্রতার পরিবর্তনে বেঁকে গিয়ে রেণু '
               'বিচ্ছুরণে সাহায্য করে।',
    'expl_en': 'The peristome teeth (typically 16 + 16 in two rings in Funaria) exhibit hygroscopic movements, bending '
               'outward when dry to disperse spores into the wind.',
    'id': 'BIO-PK-097',
    'opts': { 'bn': ['পেরিস্টোম দাঁত (Peristome teeth)', 'অপারকুলাম ঢাকনা', 'কলুমেলা', 'অ্যাপোফাইসিস'],
              'en': ['Peristome teeth', 'Operculum lid', 'Columella', 'Apophysis']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ফার্নের স্পোরাঞ্জিয়ামে বিশেষ পুরু প্রাচীরযুক্ত যে কোষগুলির বলয় স্টোমিয়ামকে ফাটিয়ে স্পোর নিক্ষেপ করে '
          'তাকে কী বলে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In fern sporangia, the row of specialized thick-walled cells that rupture the stomium to eject spores is '
          'called the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ফার্নের স্পোরাঞ্জিয়ামের অ্যানুলাস (Annulus) নামক বিশেষ কোষবলয় শুষ্ক অবস্থায় কুঁচকে গিয়ে '
               'স্টোমিয়ামকে ফাটিয়ে ক্যাটাপল্টের ন্যায় স্পোর বাইরে ছড়িয়ে দেয়।',
    'expl_en': 'The annulus is a specialized ring of differentially thickened cells in the leptosporangiate fern '
               'sporangium that creates mechanical tension as it dries, catapulting spores outward.',
    'id': 'BIO-PK-098',
    'opts': { 'bn': ['অ্যানুলাস (Annulus)', 'ইন্ডুসিয়াম', 'ট্যাপিটাম', 'রামেন্তা'],
              'en': ['Annulus', 'Indusium', 'Tapetum', 'Ramenta']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ফার্নের রাইজোম ও তরুণ পাতার বোঁটাকে ঢেকে রাখা বাদামী চুলের মতো সুরক্ষাকারী আঁশকে কী বলে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Brown hair-like scales covering the rhizome and petiole bases of young fern fronds for protection are '
          'called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ফার্নের মুকুল ও রাইজোমকে আবৃতকারী বাদামী রঙের বহুকোষী শল্কের মতো রোমগুলিকে রামেন্তা (Ramenta) বলা হয়।',
    'expl_en': 'Ramenta are chaffy, multicellular, dry brownish scales that cover and protect the young circinate '
               'fronds and rhizome in ferns.',
    'id': 'BIO-PK-099',
    'opts': { 'bn': ['রামেন্তা (Ramenta)', 'সারসিনেট ভারনেশন', 'শল্কপত্র', 'ব্র্যাক্টিওল'],
              'en': ['Ramenta', 'Circinate vernation', 'Scale leaves', 'Bracteoles']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ফার্ন এবং সাইকাসের কচি পাতার স্প্রিং-এর মতো কুন্ডলীকৃত বিন্যাসকে কী বলা হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The coiled, spring-like arrangement of young leaves in ferns and Cycas before unfolding is termed:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ফার্ন ও সাইকাসের কচি পাতা ঘড়ির স্প্রিং-এর মতো গুটিয়ে থাকে। পাতার এই বৈশিষ্ট্যকে সারসিনেট ভারনেশন '
               '(Circinate vernation) বলে।',
    'expl_en': 'Circinate vernation is the characteristic coiling of young fronds like a watch spring to protect the '
               'delicate growing tip, found in both ferns and cycads.',
    'id': 'BIO-PK-100',
    'opts': { 'bn': ['সারসিনেট ভারনেশন (Circinate vernation)', 'টাইক্সিস', 'ফাইলোট্যাক্সি', 'এস্টিভেশন'],
              'en': ['Circinate vernation', 'Ptyxis', 'Phyllotaxy', 'Aestivation']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'সমগ্র উদ্ভিদজগতের মধ্যে কোন ব্যক্তবীজী উদ্ভিদে বৃহত্তম ডিম্বক, বৃহত্তম পুং শঙ্কু এবং বৃহত্তম সচল শুক্রাণু '
          'দেখা যায়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Which of the following gymnosperms has the largest ovule, largest male cone, and largest sperm in the '
          'entire plant kingdom?',
    'exam': 'NEET, CUET',
    'expl_bn': 'উদ্ভিদজগতের সর্ববৃহৎ ডিম্বক, সর্ববৃহৎ পুং শঙ্কু এবং খালি চোখে দৃশ্যমান সর্ববৃহৎ শুক্রাণু সাইকাসে '
               '(Cycas) দেখা যায়।',
    'expl_en': 'Cycas possesses the largest ovules (up to 6-7 cm), largest male cones (up to 50 cm), and largest '
               'top-shaped multiflagellated sperms visible to the naked eye.',
    'id': 'BIO-PK-101',
    'opts': {'bn': ['সাইকাস (Cycas)', 'পাইনাস', 'জিংগো', 'সেকোয়া'], 'en': ['Cycas', 'Pinus', 'Ginkgo', 'Sequoia']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'পাইনাসের পরাগরেণুতে দুটি পার্শ্বীয় ডানা (উইংড পোলেন) থাকে। এই ডানাগুলি কার প্রসারণের ফলে গঠিত হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Pollen grains of Pinus possess two lateral air sacs or wings (winged pollen). These wings are formed by the '
          'expansion of:',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাইনাসের পরাগরেণুর ডানা দুটি এক্সাইন (exine) বা বহিঃত্বক প্রসারিত হয়ে বেলুনের মতো স্ফীত হয়ে তৈরি হয় '
               'যা বায়ুতে ভেসে থাকতে সাহায্য করে।',
    'expl_en': 'The yellow winged pollen grains of Pinus have two lateral air bladders formed by the ballooning or '
               'separation of the outer exine layer, facilitating anemophilous dispersal.',
    'id': 'BIO-PK-102',
    'opts': { 'bn': ['রেণুবহিস্ত্বক বা এক্সাইন (Exine)', 'রেণুঅন্তস্ত্বক বা ইনটাইন', 'ট্যাপিটাল তরল', 'এন্ডোথেসিয়াম'],
              'en': ['Exine layer', 'Intine layer', 'Tapetal fluid', 'Endothecium']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': "পাইন বনে 'সালফার শাওয়ার' (Sulphur shower) বলতে কোন ঘটনাকে বোঝায়?",
    'correct': 0,
    'difficulty': 'Medium',
    'en': "The phenomenon of 'Sulphur shower' in pine forests refers to:",
    'exam': 'NEET, CUET',
    'expl_bn': 'বসন্তকালে পাইন গাছের পুং শঙ্কু থেকে কোটি কোটি হলুদ পরাগরেণু একসাথে মুক্ত হয়ে চারপাশের বাতাস হলুদ '
               "ধোঁয়ার মতো ঢেকে ফেলে, একে 'সালফার শাওয়ার' বলে।",
    'expl_en': 'In spring, mature male cones of Pinus shed astronomical numbers of yellow winged pollen grains, '
               "forming yellow clouds in the atmosphere called the 'sulphur shower'.",
    'id': 'BIO-PK-103',
    'opts': { 'bn': [ 'বসন্তকালে কোটি কোটি হলুদ বর্ণের পক্ষল পরাগরেণুর মেঘের মতো বাতাসে উড়ে ঝরে পড়া',
                      'পাইন বনের ওপর আগ্নেয়গিরির সালফার বৃষ্টি',
                      'পাইন গাছের বাকল থেকে হলুদ বিষাক্ত রজন ক্ষরণ',
                      'পাকসিনিয়া ঘটিত হলুদ মরচে রোগ'],
              'en': [ 'Massive cloud-like release of millions of yellow winged pollen grains in spring',
                      'Volcanic sulphur dioxide rain over pine needles',
                      'Secretion of yellow toxic resin from pine bark',
                      'Yellow rust disease caused by Puccinia']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'বাণিজ্যিকভাবে বহুল ব্যবহৃত টারপেনটাইন তেল এবং রজন কার তৈলাক্ত রেজিন থেকে পাতন করা হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Turpentine and rosin are commercially distilled from the oleoresin of:',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাইনাস গাছের কাণ্ড থেকে সংগৃহীত রজন পাতন করে টারপেনটাইন তেল ও রোসিন পাওয়া যায়।',
    'expl_en': 'Turpentine oil and rosin are obtained by steam distilling the crude oleoresin tapped from Pinus (such '
               'as Pinus roxburghii).',
    'id': 'BIO-PK-104',
    'opts': { 'bn': ['পাইনাস (Pinus) প্রজাতির কাষ্ঠল কনিফার', 'সাইকাস', 'সিড্রাস', 'ট্যাক্সাস'],
              'en': ['Pinus species', 'Cycas revoluta', 'Cedrus deodara', 'Taxus baccata']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ট্যাক্সাস (Taxus brevifolia) নামক ব্যক্তবীজী বৃক্ষের ছাল থেকে কোন বিখ্যাত ক্যানসার-প্রতিরোধী অ্যালকালয়েড '
          'প্রস্তুত করা হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Which anticancer alkaloid is extracted from the bark of the Pacific Yew tree (Taxus brevifolia)?',
    'exam': 'NEET, CUET',
    'expl_bn': 'ট্যাক্সাস গাছের বাকল থেকে ট্যাক্সল (Taxol) নামক জীবনদায়ী ক্যানসার প্রতিরোধী ওষুধ পাওয়া যায় যা কোষ '
               'বিভাজনে মাইক্রোটিউবিউল ভেঙে যাওয়া রোধ করে।',
    'expl_en': 'Taxol (paclitaxel) is a vital anti-neoplastic drug that blocks tubulin depolymerization during '
               'mitosis, isolated from Taxus brevifolia (gymnosperm).',
    'id': 'BIO-PK-105',
    'opts': { 'bn': ['ট্যাক্সল বা প্যাক্লিট্যাক্সেল (Taxol)', 'ভিনক্রিস্টিন', 'কলচিসিন', 'মরফিন'],
              'en': ['Taxol (Paclitaxel)', 'Vincristine', 'Colchicine', 'Morphine']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'মারকানশিয়া থ্যালাসের প্রদত্ত চিত্রটি লক্ষ্য করো:<br><svg viewBox="0 0 520 220" width="100%" height="220" '
          'xmlns="http://www.w3.org/2000/svg" class="select-none">\n'
          '  <!-- Female Thallus (Archegoniophore with finger-like rays) -->\n'
          '  <g transform="translate(30, 20)">\n'
          '    <!-- Thallus -->\n'
          '    <path d="M 40 180 Q 20 150 50 130 Q 70 110 110 130 Q 150 110 170 140 Q 190 170 150 190 Q 90 200 40 180 '
          'Z" fill="#86efac" stroke="#15803d" stroke-width="2"/>\n'
          '    <!-- Midrib -->\n'
          '    <path d="M 50 180 Q 100 150 140 140" fill="none" stroke="#166534" stroke-width="2" '
          'stroke-dasharray="3,2"/>\n'
          '    <!-- Gemma Cup (A) -->\n'
          '    <ellipse cx="100" cy="145" rx="14" ry="8" fill="#4ade80" stroke="#14532d" stroke-width="1.5"/>\n'
          '    <text x="100" y="148" fill="#052e16" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">A</text>\n'
          '    <!-- Archegoniophore stalk and umbrella head (B) -->\n'
          '    <path d="M 110 130 L 110 60" fill="none" stroke="#15803d" stroke-width="3"/>\n'
          '    <!-- Umbrella with rays -->\n'
          '    <path d="M 80 60 Q 110 40 140 60 L 145 75 L 135 65 L 125 75 L 115 65 L 105 75 L 95 65 L 85 75 Z" '
          'fill="#22c55e" stroke="#14532d" stroke-width="1.5"/>\n'
          '    <text x="110" y="35" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">B (Archegoniophore)</text>\n'
          '    <!-- Rhizoids -->\n'
          '    <path d="M 60 190 L 50 210 M 80 195 L 75 215 M 120 195 L 125 215" stroke="#a16207" '
          'stroke-width="1.5"/>\n'
          '    <text x="110" y="210" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Female Thallus</text>\n'
          '  </g>\n'
          '\n'
          '  <!-- Male Thallus (Antheridiophore with scalloped disc) -->\n'
          '  <g transform="translate(290, 20)">\n'
          '    <!-- Thallus -->\n'
          '    <path d="M 40 180 Q 20 150 50 130 Q 70 110 110 130 Q 150 110 170 140 Q 190 170 150 190 Q 90 200 40 180 '
          'Z" fill="#86efac" stroke="#15803d" stroke-width="2"/>\n'
          '    <!-- Midrib -->\n'
          '    <path d="M 50 180 Q 100 150 140 140" fill="none" stroke="#166534" stroke-width="2" '
          'stroke-dasharray="3,2"/>\n'
          '    <!-- Gemma Cup -->\n'
          '    <ellipse cx="100" cy="145" rx="14" ry="8" fill="#4ade80" stroke="#14532d" stroke-width="1.5"/>\n'
          '    <!-- Antheridiophore stalk and peltate disc (C) -->\n'
          '    <path d="M 110 130 L 110 60" fill="none" stroke="#15803d" stroke-width="3"/>\n'
          '    <!-- Scalloped disc -->\n'
          '    <ellipse cx="110" cy="60" rx="28" ry="10" fill="#16a34a" stroke="#14532d" stroke-width="1.5"/>\n'
          '    <text x="110" y="35" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">C (Antheridiophore)</text>\n'
          '    <!-- Rhizoids -->\n'
          '    <path d="M 60 190 L 50 210 M 80 195 L 75 215 M 120 195 L 125 215" stroke="#a16207" '
          'stroke-width="1.5"/>\n'
          '    <text x="110" y="210" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Male Thallus</text>\n'
          '  </g>\n'
          '</svg><br>A, B এবং C চিহ্নিত অংশগুলি সঠিকভাবে শনাক্ত করো:',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Examine the given diagram representing Marchantia thalli:<br><svg viewBox="0 0 520 220" width="100%" '
          'height="220" xmlns="http://www.w3.org/2000/svg" class="select-none">\n'
          '  <!-- Female Thallus (Archegoniophore with finger-like rays) -->\n'
          '  <g transform="translate(30, 20)">\n'
          '    <!-- Thallus -->\n'
          '    <path d="M 40 180 Q 20 150 50 130 Q 70 110 110 130 Q 150 110 170 140 Q 190 170 150 190 Q 90 200 40 180 '
          'Z" fill="#86efac" stroke="#15803d" stroke-width="2"/>\n'
          '    <!-- Midrib -->\n'
          '    <path d="M 50 180 Q 100 150 140 140" fill="none" stroke="#166534" stroke-width="2" '
          'stroke-dasharray="3,2"/>\n'
          '    <!-- Gemma Cup (A) -->\n'
          '    <ellipse cx="100" cy="145" rx="14" ry="8" fill="#4ade80" stroke="#14532d" stroke-width="1.5"/>\n'
          '    <text x="100" y="148" fill="#052e16" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">A</text>\n'
          '    <!-- Archegoniophore stalk and umbrella head (B) -->\n'
          '    <path d="M 110 130 L 110 60" fill="none" stroke="#15803d" stroke-width="3"/>\n'
          '    <!-- Umbrella with rays -->\n'
          '    <path d="M 80 60 Q 110 40 140 60 L 145 75 L 135 65 L 125 75 L 115 65 L 105 75 L 95 65 L 85 75 Z" '
          'fill="#22c55e" stroke="#14532d" stroke-width="1.5"/>\n'
          '    <text x="110" y="35" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">B (Archegoniophore)</text>\n'
          '    <!-- Rhizoids -->\n'
          '    <path d="M 60 190 L 50 210 M 80 195 L 75 215 M 120 195 L 125 215" stroke="#a16207" '
          'stroke-width="1.5"/>\n'
          '    <text x="110" y="210" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Female Thallus</text>\n'
          '  </g>\n'
          '\n'
          '  <!-- Male Thallus (Antheridiophore with scalloped disc) -->\n'
          '  <g transform="translate(290, 20)">\n'
          '    <!-- Thallus -->\n'
          '    <path d="M 40 180 Q 20 150 50 130 Q 70 110 110 130 Q 150 110 170 140 Q 190 170 150 190 Q 90 200 40 180 '
          'Z" fill="#86efac" stroke="#15803d" stroke-width="2"/>\n'
          '    <!-- Midrib -->\n'
          '    <path d="M 50 180 Q 100 150 140 140" fill="none" stroke="#166534" stroke-width="2" '
          'stroke-dasharray="3,2"/>\n'
          '    <!-- Gemma Cup -->\n'
          '    <ellipse cx="100" cy="145" rx="14" ry="8" fill="#4ade80" stroke="#14532d" stroke-width="1.5"/>\n'
          '    <!-- Antheridiophore stalk and peltate disc (C) -->\n'
          '    <path d="M 110 130 L 110 60" fill="none" stroke="#15803d" stroke-width="3"/>\n'
          '    <!-- Scalloped disc -->\n'
          '    <ellipse cx="110" cy="60" rx="28" ry="10" fill="#16a34a" stroke="#14532d" stroke-width="1.5"/>\n'
          '    <text x="110" y="35" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">C (Antheridiophore)</text>\n'
          '    <!-- Rhizoids -->\n'
          '    <path d="M 60 190 L 50 210 M 80 195 L 75 215 M 120 195 L 125 215" stroke="#a16207" '
          'stroke-width="1.5"/>\n'
          '    <text x="110" y="210" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Male Thallus</text>\n'
          '  </g>\n'
          '</svg><br>Identify parts labeled A, B, and C:',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'মারকানশিয়াতে: A হলো গেমা কাপ (অঙ্গজ জননকারী পেয়ালা); B হলো ছাতার মতো রশ্মিযুক্ত আর্কেগোনিওফোর '
               '(স্ত্রী জনন অঙ্গ ধারক); C হলো লোবযুক্ত অ্যান্থেরিডিওফোর (পুং জনন অঙ্গ ধারক)।',
    'expl_en': 'In Marchantia: A is the gemma cup containing vegetative green multicellular gemmae. B is the '
               'umbrella-like female archegoniophore bearing archegonia under its rays. C is the flattened male '
               'antheridiophore bearing antheridia.',
    'id': 'BIO-PK-106',
    'opts': { 'bn': [ 'A = গেমা কাপ (Gemma cup); B = আর্কেগোনিওফোর (স্ত্রী); C = অ্যান্থেরিডিওফোর (পুং)',
                      'A = অ্যান্থেরিডিওফোর; B = গেমা কাপ; C = আর্কেগোনিওফোর',
                      'A = ক্যাপসুল; B = সিটা; C = ফুট',
                      'A = স্ট্রোবিলাস; B = স্পোরোফিল; C = মাইক্রোফিল'],
              'en': [ 'A = Gemma cup; B = Archegoniophore (female); C = Antheridiophore (male)',
                      'A = Antheridiophore; B = Gemma cup; C = Archegoniophore',
                      'A = Capsule; B = Seta; C = Foot',
                      'A = Strobili; B = Sporophyll; C = Microphyll']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'উদ্ভিদের তিনটি প্রধান জীবনচক্রের প্রদত্ত রেখাচিত্রগুলি লক্ষ্য করো:<br><svg viewBox="0 0 540 180" '
          'width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">\n'
          '  <!-- Cycle A: Haplontic -->\n'
          '  <g transform="translate(10, 10)">\n'
          '    <rect x="10" y="10" width="150" height="150" rx="8" fill="#f0fdf4" stroke="#16a34a" '
          'stroke-width="1.5"/>\n'
          '    <text x="85" y="30" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Haplontic (A)</text>\n'
          '    <path d="M 40 90 A 45 45 0 1 1 130 90" fill="none" stroke="#16a34a" stroke-width="4"/>\n'
          '    <path d="M 130 90 A 45 45 0 0 1 40 90" fill="none" stroke="#dc2626" stroke-width="4"/>\n'
          '    <text x="85" y="70" fill="#15803d" font-size="10" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Gametophyte (n)</text>\n'
          '    <text x="85" y="125" fill="#b91c1c" font-size="9" font-family="system-ui" text-anchor="middle">Zygote '
          '(2n) only</text>\n'
          '    <text x="85" y="150" fill="#047857" font-size="9" font-family="system-ui" text-anchor="middle">Volvox, '
          'Spirogyra</text>\n'
          '  </g>\n'
          '\n'
          '  <!-- Cycle B: Diplontic -->\n'
          '  <g transform="translate(185, 10)">\n'
          '    <rect x="10" y="10" width="150" height="150" rx="8" fill="#fef2f2" stroke="#dc2626" '
          'stroke-width="1.5"/>\n'
          '    <text x="85" y="30" fill="#b91c1c" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Diplontic (B)</text>\n'
          '    <path d="M 40 90 A 45 45 0 1 1 130 90" fill="none" stroke="#dc2626" stroke-width="4"/>\n'
          '    <path d="M 130 90 A 45 45 0 0 1 40 90" fill="none" stroke="#16a34a" stroke-width="4"/>\n'
          '    <text x="85" y="70" fill="#b91c1c" font-size="10" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Sporophyte (2n)</text>\n'
          '    <text x="85" y="125" fill="#15803d" font-size="9" font-family="system-ui" text-anchor="middle">Gametes '
          '(n) only</text>\n'
          '    <text x="85" y="150" fill="#991b1b" font-size="9" font-family="system-ui" text-anchor="middle">Gymno, '
          'Angio, Fucus</text>\n'
          '  </g>\n'
          '\n'
          '  <!-- Cycle C: Haplodiplontic -->\n'
          '  <g transform="translate(360, 10)">\n'
          '    <rect x="10" y="10" width="165" height="150" rx="8" fill="#eff6ff" stroke="#2563eb" '
          'stroke-width="1.5"/>\n'
          '    <text x="92" y="30" fill="#1d4ed8" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Haplodiplontic (C)</text>\n'
          '    <path d="M 47 90 A 45 45 0 1 1 137 90" fill="none" stroke="#16a34a" stroke-width="4"/>\n'
          '    <path d="M 137 90 A 45 45 0 0 1 47 90" fill="none" stroke="#dc2626" stroke-width="4"/>\n'
          '    <text x="92" y="65" fill="#15803d" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Gametophyte (n)</text>\n'
          '    <text x="92" y="125" fill="#b91c1c" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Sporophyte (2n)</text>\n'
          '    <text x="92" y="150" fill="#1e40af" font-size="8.5" font-family="system-ui" text-anchor="middle">Bryo, '
          'Pterido, Kelps</text>\n'
          '  </g>\n'
          '</svg><br>নিচের কোন বিকল্পটিতে জীবনচক্র ও তাদের প্রতিনিধি জীবকে সঠিকভাবে মেলানো হয়েছে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Examine the diagrams of the three plant life cycles below:<br><svg viewBox="0 0 540 180" width="100%" '
          'height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">\n'
          '  <!-- Cycle A: Haplontic -->\n'
          '  <g transform="translate(10, 10)">\n'
          '    <rect x="10" y="10" width="150" height="150" rx="8" fill="#f0fdf4" stroke="#16a34a" '
          'stroke-width="1.5"/>\n'
          '    <text x="85" y="30" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Haplontic (A)</text>\n'
          '    <path d="M 40 90 A 45 45 0 1 1 130 90" fill="none" stroke="#16a34a" stroke-width="4"/>\n'
          '    <path d="M 130 90 A 45 45 0 0 1 40 90" fill="none" stroke="#dc2626" stroke-width="4"/>\n'
          '    <text x="85" y="70" fill="#15803d" font-size="10" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Gametophyte (n)</text>\n'
          '    <text x="85" y="125" fill="#b91c1c" font-size="9" font-family="system-ui" text-anchor="middle">Zygote '
          '(2n) only</text>\n'
          '    <text x="85" y="150" fill="#047857" font-size="9" font-family="system-ui" text-anchor="middle">Volvox, '
          'Spirogyra</text>\n'
          '  </g>\n'
          '\n'
          '  <!-- Cycle B: Diplontic -->\n'
          '  <g transform="translate(185, 10)">\n'
          '    <rect x="10" y="10" width="150" height="150" rx="8" fill="#fef2f2" stroke="#dc2626" '
          'stroke-width="1.5"/>\n'
          '    <text x="85" y="30" fill="#b91c1c" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Diplontic (B)</text>\n'
          '    <path d="M 40 90 A 45 45 0 1 1 130 90" fill="none" stroke="#dc2626" stroke-width="4"/>\n'
          '    <path d="M 130 90 A 45 45 0 0 1 40 90" fill="none" stroke="#16a34a" stroke-width="4"/>\n'
          '    <text x="85" y="70" fill="#b91c1c" font-size="10" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Sporophyte (2n)</text>\n'
          '    <text x="85" y="125" fill="#15803d" font-size="9" font-family="system-ui" text-anchor="middle">Gametes '
          '(n) only</text>\n'
          '    <text x="85" y="150" fill="#991b1b" font-size="9" font-family="system-ui" text-anchor="middle">Gymno, '
          'Angio, Fucus</text>\n'
          '  </g>\n'
          '\n'
          '  <!-- Cycle C: Haplodiplontic -->\n'
          '  <g transform="translate(360, 10)">\n'
          '    <rect x="10" y="10" width="165" height="150" rx="8" fill="#eff6ff" stroke="#2563eb" '
          'stroke-width="1.5"/>\n'
          '    <text x="92" y="30" fill="#1d4ed8" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Haplodiplontic (C)</text>\n'
          '    <path d="M 47 90 A 45 45 0 1 1 137 90" fill="none" stroke="#16a34a" stroke-width="4"/>\n'
          '    <path d="M 137 90 A 45 45 0 0 1 47 90" fill="none" stroke="#dc2626" stroke-width="4"/>\n'
          '    <text x="92" y="65" fill="#15803d" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Gametophyte (n)</text>\n'
          '    <text x="92" y="125" fill="#b91c1c" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Sporophyte (2n)</text>\n'
          '    <text x="92" y="150" fill="#1e40af" font-size="8.5" font-family="system-ui" text-anchor="middle">Bryo, '
          'Pterido, Kelps</text>\n'
          '  </g>\n'
          '</svg><br>Which of the following correctly pairs the life cycle type with its representative organisms?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'A হলো হ্যাপ্লন্টিক (ভলভক্স, স্পাইরোগাইরা); B হলো ডিপ্লন্টিক (ব্যক্তবীজী, গুপ্তবীজী ও শৈবাল ফিউকাস); C '
               'হলো হ্যাপ্লোডিপ্লন্টিক (ব্রায়োফাইট, টেরিডোফাইট, এক্টোকার্পাস ও কেল্প)।',
    'expl_en': 'Cycle A is Haplontic (Volvox, Spirogyra, Chlamydomonas). Cycle B is Diplontic (all seed plants and the '
               'brown alga Fucus). Cycle C is Haplodiplontic (Bryophytes, Pteridophytes, Ectocarpus, Polysiphonia, '
               'Kelps).',
    'id': 'BIO-PK-107',
    'opts': { 'bn': [ 'A = হ্যাপ্লন্টিক (ভলভক্স, স্পাইরোগাইরা); B = ডিপ্লন্টিক (ব্যক্তবীজী, গুপ্তবীজী, ফিউকাস); C = '
                      'হ্যাপ্লোডিপ্লন্টিক (ব্রায়োফাইটা, টেরিডোফাইটা, কেল্প)',
                      'A = ডিপ্লন্টিক (কেল্প); B = হ্যাপ্লন্টিক (ফিউকাস); C = হ্যাপ্লোডিপ্লন্টিক (ভলভক্স)',
                      'A = হ্যাপ্লোডিপ্লন্টিক; B = ডিপ্লন্টিক; C = হ্যাপ্লন্টিক',
                      'A = হ্যাপ্লন্টিক (ব্যক্তবীজী); B = ডিপ্লন্টিক (স্পাইরোগাইরা); C = হ্যাপ্লোডিপ্লন্টিক '
                      '(গুপ্তবীজী)'],
              'en': [ 'A = Haplontic (Volvox, Spirogyra); B = Diplontic (Gymnosperms, Angiosperms, Fucus); C = '
                      'Haplodiplontic (Bryophytes, Pteridophytes, Kelps)',
                      'A = Diplontic (Kelps); B = Haplontic (Fucus); C = Haplodiplontic (Volvox)',
                      'A = Haplodiplontic; B = Diplontic; C = Haplontic',
                      'A = Haplontic (Gymnosperms); B = Diplontic (Spirogyra); C = Haplodiplontic (Angiosperms)']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ফার্নের প্রোথ্যালাসের প্রদত্ত চিত্রটি পরীক্ষা করো:<br><svg viewBox="0 0 320 230" width="100%" height="230" '
          'xmlns="http://www.w3.org/2000/svg" class="select-none">\n'
          '  <!-- Heart-shaped prothallus -->\n'
          '  <path d="M 160 50 C 130 10 70 20 60 70 C 50 120 110 180 160 210 C 210 180 270 120 260 70 C 250 20 190 10 '
          '160 50 Z" fill="#bbf7d0" stroke="#16a34a" stroke-width="2.5"/>\n'
          '  <!-- Apical notch (A) -->\n'
          '  <circle cx="160" cy="50" r="4" fill="#15803d"/>\n'
          '  <line x1="160" y1="50" x2="160" y2="20" stroke="#15803d" stroke-width="1.5"/>\n'
          '  <text x="160" y="15" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">A (Apical Notch)</text>\n'
          '  <!-- Archegonia near notch (B) -->\n'
          '  <g fill="#ec4899" stroke="#be185d" stroke-width="1">\n'
          '    <circle cx="150" cy="80" r="4"/>\n'
          '    <circle cx="160" cy="75" r="4"/>\n'
          '    <circle cx="170" cy="80" r="4"/>\n'
          '    <circle cx="155" cy="92" r="4"/>\n'
          '    <circle cx="165" cy="92" r="4"/>\n'
          '  </g>\n'
          '  <line x1="170" y1="80" x2="225" y2="80" stroke="#be185d" stroke-width="1.5"/>\n'
          '  <text x="230" y="84" fill="#9d174d" font-size="10" font-weight="bold" font-family="system-ui">B '
          '(Archegonia)</text>\n'
          '  <!-- Antheridia among rhizoids (C) -->\n'
          '  <g fill="#0284c7" stroke="#0369a1" stroke-width="1">\n'
          '    <circle cx="140" cy="140" r="3.5"/>\n'
          '    <circle cx="175" cy="145" r="3.5"/>\n'
          '    <circle cx="150" cy="160" r="3.5"/>\n'
          '    <circle cx="168" cy="165" r="3.5"/>\n'
          '  </g>\n'
          '  <line x1="135" y1="140" x2="80" y2="140" stroke="#0369a1" stroke-width="1.5"/>\n'
          '  <text x="75" y="144" fill="#0369a1" font-size="10" font-weight="bold" font-family="system-ui" '
          'text-anchor="end">C (Antheridia)</text>\n'
          '  <!-- Rhizoids at base (D) -->\n'
          '  <path d="M 155 180 L 140 215 M 160 190 L 160 225 M 165 185 L 180 220 M 150 170 L 130 200" '
          'stroke="#a16207" stroke-width="1.5"/>\n'
          '  <text x="160" y="225" fill="#78350f" font-size="10" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">D (Rhizoids)</text>\n'
          '</svg><br>A, B, C এবং D চিহ্নিত অংশগুলি শনাক্ত করো:',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Examine the structure of the fern prothallus:<br><svg viewBox="0 0 320 230" width="100%" height="230" '
          'xmlns="http://www.w3.org/2000/svg" class="select-none">\n'
          '  <!-- Heart-shaped prothallus -->\n'
          '  <path d="M 160 50 C 130 10 70 20 60 70 C 50 120 110 180 160 210 C 210 180 270 120 260 70 C 250 20 190 10 '
          '160 50 Z" fill="#bbf7d0" stroke="#16a34a" stroke-width="2.5"/>\n'
          '  <!-- Apical notch (A) -->\n'
          '  <circle cx="160" cy="50" r="4" fill="#15803d"/>\n'
          '  <line x1="160" y1="50" x2="160" y2="20" stroke="#15803d" stroke-width="1.5"/>\n'
          '  <text x="160" y="15" fill="#14532d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">A (Apical Notch)</text>\n'
          '  <!-- Archegonia near notch (B) -->\n'
          '  <g fill="#ec4899" stroke="#be185d" stroke-width="1">\n'
          '    <circle cx="150" cy="80" r="4"/>\n'
          '    <circle cx="160" cy="75" r="4"/>\n'
          '    <circle cx="170" cy="80" r="4"/>\n'
          '    <circle cx="155" cy="92" r="4"/>\n'
          '    <circle cx="165" cy="92" r="4"/>\n'
          '  </g>\n'
          '  <line x1="170" y1="80" x2="225" y2="80" stroke="#be185d" stroke-width="1.5"/>\n'
          '  <text x="230" y="84" fill="#9d174d" font-size="10" font-weight="bold" font-family="system-ui">B '
          '(Archegonia)</text>\n'
          '  <!-- Antheridia among rhizoids (C) -->\n'
          '  <g fill="#0284c7" stroke="#0369a1" stroke-width="1">\n'
          '    <circle cx="140" cy="140" r="3.5"/>\n'
          '    <circle cx="175" cy="145" r="3.5"/>\n'
          '    <circle cx="150" cy="160" r="3.5"/>\n'
          '    <circle cx="168" cy="165" r="3.5"/>\n'
          '  </g>\n'
          '  <line x1="135" y1="140" x2="80" y2="140" stroke="#0369a1" stroke-width="1.5"/>\n'
          '  <text x="75" y="144" fill="#0369a1" font-size="10" font-weight="bold" font-family="system-ui" '
          'text-anchor="end">C (Antheridia)</text>\n'
          '  <!-- Rhizoids at base (D) -->\n'
          '  <path d="M 155 180 L 140 215 M 160 190 L 160 225 M 165 185 L 180 220 M 150 170 L 130 200" '
          'stroke="#a16207" stroke-width="1.5"/>\n'
          '  <text x="160" y="225" fill="#78350f" font-size="10" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">D (Rhizoids)</text>\n'
          '</svg><br>Identify the labeled regions A, B, C, and D:',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'ফার্নের প্রোথ্যালাস হলো হৃদপিণ্ডাকার সহবাসী গ্যামেটোফাইট: A হলো অগ্রস্থ খাঁজ; B হলো খাঁজের কাছে '
               'অবস্থিত স্ত্রী অঙ্গ আর্কেগোনিয়া; C হলো নিচের দিকে অবস্থিত পুং অঙ্গ অ্যান্থেরিডিয়া; এবং D হলো '
               'সংলগ্নকারী রাইজয়েড।',
    'expl_en': 'The fern prothallus is a green, heart-shaped, monoecious gametophyte: A is the apical notch, B '
               'represents female archegonia near the notch, C represents male antheridia near the basal cushion, and '
               'D represents unicellular anchoring rhizoids.',
    'id': 'BIO-PK-108',
    'opts': { 'bn': [ 'A = অগ্রস্থ খাঁজ (Apical notch); B = আর্কেগোনিয়া (স্ত্রী অঙ্গ); C = অ্যান্থেরিডিয়া (পুং '
                      'অঙ্গ); D = রাইজয়েড (Rhizoids)',
                      'A = সোরাস; B = অ্যান্থেরিডিয়া; C = আর্কেগোনিয়া; D = মূল',
                      'A = প্রোটোনেমা; B = স্পোরাঞ্জিয়াম; C = গেমা কাপ; D = স্ট্রাইপ',
                      'A = পত্ররন্ধ্র; B = শস্য; C = পরাগরেণু; D = হোল্ডফাস্ট'],
              'en': [ 'A = Apical notch; B = Archegonia; C = Antheridia; D = Rhizoids',
                      'A = Sorus; B = Antheridia; C = Archegonia; D = Roots',
                      'A = Protonema; B = Sporangium; C = Gemma cup; D = Stipe',
                      'A = Stoma; B = Endosperm; C = Pollen grain; D = Holdfast']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): ব্রায়োফাইটা কখনোই অনেক উঁচুতে বাড়তে পারে না এবং এরা মাটির কাছাকাছি শায়িত বা ক্ষুদ্র '
          'গালিচার মতো থাকে।<br>যুক্তি (R): ব্রায়োফাইটাতে প্রকৃত সংবহন কলা (জাইলেম ভেসেল/ট্র্যাকিড ও ফ্লোয়েম) এবং '
          'লিগনিনযুক্ত যান্ত্রিক কলার সম্পূর্ণ অভাব থাকে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Bryophytes cannot grow to significant heights and remain restricted to low creeping or small '
          'upright cushions.<br>Reason (R): Bryophytes completely lack true vascular tissues (xylem vessels/tracheids '
          'and phloem) and true lignified mechanical tissues.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'জাইলেম ও ফ্লোয়েম সংবহন কলা এবং যান্ত্রিক দৃঢ়তাদানকারী লিগনিনের অনুপস্থিতির কারণেই ব্রায়োফাইটা বেশি '
               'উঁচু হতে পারে না। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'Without vascular bundles to transport water to great vertical heights and without lignified secondary '
               'xylem to provide mechanical support against gravity, bryophytes are biophysically constrained to low '
               'heights. (R) correctly explains (A).',
    'id': 'BIO-PK-109',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): লাল শৈবাল (Rhodophyceae) সমুদ্রের গভীর তলদেশে বেঁচে থাকতে পারে যেখানে অন্য শৈবাল বাঁচতে '
          'পারে না।<br>যুক্তি (R): লাল শৈবালে r-ফাইকোইরিথ্রিন নামক আনুষঙ্গিক রঞ্জক থাকে যা গভীর সমুদ্রে প্রবেশকারী '
          'উচ্চ-শক্তি ও ক্ষুদ্র-তরঙ্গদৈর্ঘ্যবিশিষ্ট নীল-সবুজ আলোক তরঙ্গ কার্যকরভাবে শোষণ করতে পারে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Red algae (Rhodophyceae) can flourish at great depths in oceans where other algae cannot '
          'survive.<br>Reason (R): Red algae contain the accessory pigment r-phycoerythrin, which efficiently absorbs '
          'the high-energy, short-wavelength blue-green light that penetrates deep oceanic waters.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'সমুদ্রের গভীর জলে কেবল নীল-সবুজ আলোক তরঙ্গ প্রবেশ করতে পারে। লাল শৈবালের r-ফাইকোইরিথ্রিন এই তরঙ্গ শোষণ '
               'করে সালোকসংশ্লেষ চালাতে পারে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'Blue-green light possesses maximum penetrating power in clear oceanic water. r-phycoerythrin absorbs '
               'this blue-green light spectrum (around 495-570 nm) and transfers energy to chlorophyll a, enabling '
               'photosynthesis in the abyss. (R) correctly explains (A).',
    'id': 'BIO-PK-110',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): মাইকোরাইজাল ছত্রাকের অনুষঙ্গ ব্যতীত পাইনাস গাছের বীজ কখনোই অঙ্কুরিত হয়ে চারাগাছ গঠন '
          'করতে পারে না।<br>যুক্তি (R): পাইনাসের শিকড়ে মূলরোম থাকে না এবং পর্যাপ্ত জল ও খনিজ শোষণের জন্য ছত্রাকের '
          'হাইফির ওপর বাধ্যতামূলকভাবে নির্ভরশীল থাকে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Pinus seeds fail to germinate and establish seedlings in the absence of mycorrhizal fungal '
          'association.<br>Reason (R): Pinus roots have obligate mycorrhizal association because their roots lack root '
          'hairs and require fungal hyphae for adequate water and mineral absorption.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'পাইনাসের মূলরোমহীন মূল পর্যাপ্ত জল ও ফসফরাস শোষণ করতে পারে না। ছত্রাকের মাইকোরাইজাল হাইফি মূলরোমের '
               'বিকল্প হিসেবে কাজ করে, তাই মাইকোরাইজা ছাড়া বীজ অঙ্কুরিত হতে পারে না। অতএব (R) হলো (A)-এর সঠিক '
               'ব্যাখ্যা।',
    'expl_en': 'Pinus has an obligate association with ectomycorrhizae. The fungal mantle and Hartig net substitute '
               'for the poorly developed root hairs, absorbing water and phosphorus indispensable for seedling growth. '
               '(R) correctly explains (A).',
    'id': 'BIO-PK-111',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): সিলাজিনেলা ও সালভিনিয়ার মতো টেরিডোফাইটে হেটারোস্পোরির আবির্ভাবকে উচ্চতর উদ্ভিদের বীজ '
          'স্বভাবের (Seed habit) বিবর্তনের প্রধান পূর্বসূরি মনে করা হয়।<br>যুক্তি (R): হেটারোস্পোরাস উদ্ভিদে '
          'মেগাস্পোর মাতৃ স্পোরোফাইটের গায়ে সংলগ্ন থেকে স্ত্রী গ্যামেটোফাইট গঠন করে এবং সেখানেই জাইগোট থেকে প্রাথমিক '
          'ভ্রূণের বিকাশ ঘটে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Heterospory in pteridophytes like Selaginella and Salvinia is regarded as a critical '
          'precursor to the seed habit of higher plants.<br>Reason (R): In heterosporous pteridophytes, the megaspore '
          'develops into a female gametophyte that is retained and nourished on the parent sporophyte, with the embryo '
          'initiating development in situ.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'মাতৃ স্পোরোফাইটে স্ত্রী গ্যামেটোফাইটের ধারণ এবং তার ভেতরেই ভ্রূণের সুরক্ষিত বিকাশই হলো বীজের উৎপত্তির '
               'মূল পূর্বশর্ত। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'The retention of the female gametophyte on the parent sporophyte and the nutrition of the developing '
               'zygote within it are the exact biological hallmarks defining the transition towards seeds. (R) '
               'correctly explains (A).',
    'id': 'BIO-PK-112',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): ব্যক্তবীজী উদ্ভিদে কখনোই ফল গঠিত হয় না।<br>যুক্তি (R): ব্যক্তবীজী উদ্ভিদে কোনো '
          'ডিম্বাশয় থাকে না; এদের ডিম্বকগুলি মেগাস্পোরোফিলের ওপর সম্পূর্ণ অনাবৃত থাকে এবং নিষেকের পর কোনো ফলত্বক তৈরি '
          'করতে পারে না।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Gymnosperms do not produce fruits.<br>Reason (R): Gymnosperms lack an ovary; their ovules '
          'are completely naked on megasporophylls and cannot form an enclosing pericarp after fertilization.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'ফল হলো পরিপক্ব ডিম্বাশয়। ব্যক্তবীজীতে ডিম্বাশয় না থাকায় কোনো ফল গঠিত হতে পারে না, বীজগুলি নগ্ন '
               'অবস্থায় থাকে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'A fruit is anatomically a ripened ovary enclosing seeds. Because gymnosperms lack ovaries, their '
               'fertilized ovules ripen into naked seeds without any pericarp (fruit wall). (R) correctly explains '
               '(A).',
    'id': 'BIO-PK-113',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): ব্যক্তবীজী উদ্ভিদের এন্ডোস্পার্ম (শস্য) হ্যাপ্লয়েড (n), কিন্তু গুপ্তবীজী উদ্ভিদের '
          'এন্ডোস্পার্ম ট্রিপ্লয়েড (3n)।<br>যুক্তি (R): ব্যক্তবীজীতে শস্য নিষেকের পূর্বেই স্ত্রী গ্যামেটোফাইট কলা '
          'থেকে সরাসরি গঠিত হয়; কিন্তু গুপ্তবীজীতে এটি নিষেকের পরে ট্রিপল ফিউশনের মাধ্যমে গঠিত হয়।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): The endosperm of gymnosperms is haploid (n), while that of angiosperms is triploid '
          '(3n).<br>Reason (R): In gymnosperms, endosperm is formed before fertilization directly from the female '
          'gametophyte tissue; in angiosperms, it is formed after double fertilization through triple fusion.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'ব্যক্তবীজীর এন্ডোস্পার্ম নিষেকের পূর্বে গঠিত হ্যাপ্লয়েড স্ত্রী গ্যামেটোফাইট (n), কিন্তু গুপ্তবীজীতে '
               'একটি শুক্রাণু (n) ও দুটি পোলার নিউক্লিয়াস (2n)-এর মিলনে ট্রিপ্লয়েড (3n) শস্য গঠিত হয়। অতএব (R) হলো '
               '(A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'Pre-fertilization development from the haploid megaspore makes the gymnospermic endosperm (n), whereas '
               'triple fusion of a haploid sperm with the diploid secondary nucleus makes the angiospermic endosperm '
               '(3n). (R) correctly explains (A).',
    'id': 'BIO-PK-114',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): ভূমিক্ষয় রোধে লিভারওয়ার্টের তুলনায় মস বাস্তুতান্ত্রিকভাবে অনেক বেশি '
          'গুরুত্বপূর্ণ।<br>যুক্তি (R): মস মাটির ওপর ঘন গালিচার মতো আস্তরণ তৈরি করে যা বৃষ্টির ফোঁটার সরাসরি আঘাত '
          'হ্রাস করে এবং মাটির কণাগুলিকে শক্তভাবে ধরে রাখে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Mosses are ecologically more important than liverworts in controlling soil '
          'erosion.<br>Reason (R): Mosses form dense, impenetrable carpets on soil surfaces that cushion the '
          'mechanical impact of falling raindrops and bind topsoil particles.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'মাটির ওপর মসের তৈরি ঘন গালিচা বৃষ্টির তীব্রতাকে প্রতিহত করে মাটির ক্ষয় রোধ করে। অতএব (R) হলো (A)-এর '
               'সঠিক ব্যাখ্যা।',
    'expl_en': 'Since mosses form dense mats on the soil, they reduce the impact of falling rain and prevent soil '
               'erosion. (R) accurately explains (A).',
    'id': 'BIO-PK-115',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): স্পাইরোগাইরায় ফ্ল্যাজেলাবিহীন গ্যামেটের সমন্বয়ে আইসোগ্যামি দেখা যায়।<br>যুক্তি (R): '
          'স্পাইরোগাইরার গ্যামেটগুলি গঠনে সমান এবং চলনহীন, যা সংশ্লেষ নালী (conjugation tube)-র মাধ্যমে অ্যামিবয়েড '
          'চলনে স্থানান্তরিত হয়।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Spirogyra shows isogamy with non-flagellated gametes.<br>Reason (R): The gametes of '
          'Spirogyra are structurally similar and non-motile, transferring via a conjugation tube by amoeboid '
          'creeping.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'স্পাইরোগাইরাতে গ্যামেটগুলি সমআকৃতির এবং ফ্ল্যাজেলাবিহীন; কনজুগেশন নালীর মাধ্যমে এদের মিলন ঘটে। সুতরাং '
               '(R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'Spirogyra undergoes scalariform or lateral conjugation where morphologically indistinguishable, '
               'non-flagellated protoplasts fuse, exemplifying non-motile isogamy. (R) correctly explains (A).',
    'id': 'BIO-PK-116',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): সাইকাস (Cycas) একটি ভিন্নবাসী (dioecious) ব্যক্তবীজী উদ্ভিদ।<br>যুক্তি (R): সাইকাসের '
          'পুং শঙ্কু এবং মেগাস্পোরোফিল দুটি সম্পূর্ণ পৃথক পুরুষ ও স্ত্রী গাছে উৎপন্ন হয়।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Cycas is a dioecious gymnosperm.<br>Reason (R): Male cones and megasporophylls are produced '
          'on completely separate male and female plants of Cycas.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'সাইকাসের পুরুষ ও স্ত্রী গাছ আলাদা হওয়ায় এটি ভিন্নবাসী (dioecious)। পুরুষ গাছে পুং শঙ্কু এবং স্ত্রী '
               'গাছে মেগাস্পোরোফিল জন্মায়। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'Dioecy means male and female reproductive structures are on separate individuals. In Cycas, male cones '
               'and megasporophylls occur on separate trees. (R) correctly explains (A).',
    'id': 'BIO-PK-117',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'বিবৃতি I: ক্লোরোফাইসিতে প্রধান সালোকসংশ্লেষী রঞ্জক হলো ক্লোরোফিল a ও b এবং সঞ্চিত খাদ্য হলো '
          'স্টার্চ।<br>বিবৃতি II: ফিওফাইসিতে প্রধান রঞ্জক হলো ক্লোরোফিল a ও c সহ ফিউকোজ্যান্থিন এবং সঞ্চিত খাদ্য হলো '
          'ল্যামিনারিন বা ম্যানিটল।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Statement I: In Chlorophyceae, the major photosynthetic pigments are Chlorophyll a and b, and the food is '
          'stored as starch.<br>Statement II: In Phaeophyceae, the major pigments are Chlorophyll a and c with '
          'fucoxanthin, and the food is stored as laminarin or mannitol.',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'NCERT সারণি ৩.১ অনুসারে উভয় বিবৃতিই সম্পূর্ণ সঠিক।',
    'expl_en': 'Both statements are completely accurate according to NCERT Summary Table 3.1.',
    'id': 'BIO-PK-118',
    'opts': { 'bn': [ 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল',
                      'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল',
                      'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক'],
              'en': [ 'Both Statement I and Statement II are correct',
                      'Both Statement I and Statement II are incorrect',
                      'Statement I is correct but Statement II is incorrect',
                      'Statement I is incorrect but Statement II is correct']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'বিবৃতি I: রোডোফাইসিতে স্পোর এবং গ্যামেট উভয়ের ক্ষেত্রেই ফ্ল্যাজেলা সম্পূর্ণ অনুপস্থিত থাকে।<br>বিবৃতি II: '
          'ফিওফাইসিতে জুস্পোরে ২টি পার্শ্বীয় অসমান ফ্ল্যাজেলা থাকে, কিন্তু ক্লোরোফাইসিতে জুস্পোরে ২ থেকে ৮টি অগ্রস্থ '
          'সমান দৈর্ঘ্যের ফ্ল্যাজেলা থাকে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Statement I: In Rhodophyceae, flagella are completely absent in both spores and gametes.<br>Statement II: '
          'In Phaeophyceae, zoospores have 2 laterally inserted unequal flagella, while in Chlorophyceae, zoospores '
          'have 2 to 8 apically inserted equal flagella.',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'উভয় বিবৃতিই শৈবালের তুলনামূলক সারণি অনুসারে সম্পূর্ণ সঠিক।',
    'expl_en': 'Both statements are direct, unadulterated facts from NCERT Table 3.1 on algal divisions.',
    'id': 'BIO-PK-119',
    'opts': { 'bn': [ 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল',
                      'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল',
                      'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক'],
              'en': [ 'Both Statement I and Statement II are correct',
                      'Both Statement I and Statement II are incorrect',
                      'Statement I is correct but Statement II is incorrect',
                      'Statement I is incorrect but Statement II is correct']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'বিবৃতি I: মসের ক্ষেত্রে পত্রল দশার শীর্ষে জননাঙ্গ গঠিত হয় এবং এটি গৌণ প্রোটোনেমা থেকে পার্শ্বীয় মুকুল '
          'হিসেবে জন্মায়।<br>বিবৃতি II: লিভারওয়ার্টে স্পোরোফাইট সম্পূর্ণ স্বাধীন ও সালোকসংশ্লেষকারী, আর গ্যামেটোফাইট '
          'তার ওপর পরজীবী হিসেবে থাকে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Statement I: In mosses, the leafy stage bears sex organs at its apex and develops from the secondary '
          'protonema as a lateral bud.<br>Statement II: In liverworts, the sporophyte is completely independent and '
          'photosynthetic, while the gametophyte is parasitic on it.',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'বিবৃতি I সঠিক। কিন্তু বিবৃতি II ভুল কারণ সমস্ত ব্রায়োফাইটে গ্যামেটোফাইট স্বাধীন এবং স্পোরোফাইট তার '
               'ওপর নির্ভরশীল।',
    'expl_en': 'Statement I is correct. Statement II is completely inverted: in liverworts (and all bryophytes), the '
               'gametophyte is the dominant, photosynthetic, independent phase, while the sporophyte is physically '
               'attached and parasitic on the gametophyte.',
    'id': 'BIO-PK-120',
    'opts': { 'bn': [ 'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল',
                      'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল'],
              'en': [ 'Statement I is correct but Statement II is incorrect',
                      'Statement I is incorrect but Statement II is correct',
                      'Both Statement I and Statement II are correct',
                      'Both Statement I and Statement II are incorrect']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'বিবৃতি I: ভলভক্স, স্পাইরোগাইরা এবং ক্ল্যামাইডোমোনাস হ্যাপ্লন্টিক জীবনচক্রের নিদর্শন।<br>বিবৃতি II: ফিউকাস '
          'নামক বাদামী শৈবালটি ডিপ্লন্টিক জীবনচক্রের নিদর্শন।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Statement I: Volvox, Spirogyra, and Chlamydomonas represent the haplontic life cycle pattern.<br>Statement '
          'II: Fucus, a brown alga, represents a diplontic life cycle pattern.',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'NCERT-এর জীবনচক্র অধ্যায় অনুসারে দুটি বিবৃতিই সম্পূর্ণ নির্ভুল।',
    'expl_en': "Both statements are correct verbatim from the 'Plant Life Cycles and Alternation of Generations' "
               'section of NCERT.',
    'id': 'BIO-PK-121',
    'opts': { 'bn': [ 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল',
                      'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল',
                      'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক'],
              'en': [ 'Both Statement I and Statement II are correct',
                      'Both Statement I and Statement II are incorrect',
                      'Statement I is correct but Statement II is incorrect',
                      'Statement I is incorrect but Statement II is correct']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'বিবৃতি I: ব্যতিক্রমহীনভাবে সমস্ত টেরিডোফাইটই হেটারোস্পোরাস।<br>বিবৃতি II: ব্যতিক্রমহীনভাবে সমস্ত '
          'ব্যক্তবীজীই হেটারোস্পোরাস।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Statement I: All pteridophytes are heterosporous without any exception.<br>Statement II: All gymnosperms '
          'are heterosporous without any exception.',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'বিবৃতি I ভুল কারণ অধিকাংশ টেরিডোফাইটই হোমোস্পোরাস (যেমন ফার্ন)। কিন্তু বিবৃতি II সঠিক কারণ সমস্ত '
               'ব্যক্তবীজীই বাধ্যতামূলকভাবে হেটারোস্পোরাস।',
    'expl_en': 'Statement I is incorrect because the majority of pteridophytes are homosporous (e.g., Dryopteris, '
               'Pteris); only a few like Selaginella and Salvinia are heterosporous. Statement II is correct because '
               'all gymnosperms are strictly heterosporous.',
    'id': 'BIO-PK-122',
    'opts': { 'bn': [ 'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক',
                      'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল'],
              'en': [ 'Statement I is incorrect but Statement II is correct',
                      'Statement I is correct but Statement II is incorrect',
                      'Both Statement I and Statement II are correct',
                      'Both Statement I and Statement II are incorrect']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'কলাম-I (শৈবাল শ্রেণি)-এর সাথে কলাম-II (সঞ্চিত খাদ্য) মেলাও:<br>A. ক্লোরোফাইসি<br>B. ফিওফাইসি<br>C. '
          'রোডোফাইসি<br>D. সায়ানোফাইসি<br>1. ফ্লোরিডিয়ান স্টার্চ<br>2. ল্যামিনারিন বা ম্যানিটল<br>3. সাধারণ '
          'স্টার্চ<br>4. সায়ানোফাইসিয়ান স্টার্চ',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Match Column-I (Algal class) with Column-II (Stored food):<br>A. Chlorophyceae<br>B. Phaeophyceae<br>C. '
          'Rhodophyceae<br>D. Cyanophyceae<br>1. Floridean starch<br>2. Laminarin or Mannitol<br>3. True Starch<br>4. '
          'Cyanophycean starch',
    'exam': 'NEET, CUET',
    'expl_bn': 'ক্লোরোফাইসি = স্টার্চ (A-3); ফিওফাইসি = ল্যামিনারিন/ম্যানিটল (B-2); রোডোফাইসি = ফ্লোরিডিয়ান স্টার্চ '
               '(C-1); সায়ানোফাইসি = সায়ানোফাইসিয়ান স্টার্চ (D-4)।',
    'expl_en': 'Chlorophyceae = Starch (A-3); Phaeophyceae = Laminarin/mannitol (B-2); Rhodophyceae = Floridean starch '
               '(C-1); Cyanophyceae = Cyanophycean starch (D-4).',
    'id': 'BIO-PK-123',
    'opts': { 'bn': ['A-3, B-2, C-1, D-4', 'A-1, B-2, C-3, D-4', 'A-3, B-1, C-2, D-4', 'A-2, B-3, C-1, D-4'],
              'en': ['A-3, B-2, C-1, D-4', 'A-1, B-2, C-3, D-4', 'A-3, B-1, C-2, D-4', 'A-2, B-3, C-1, D-4']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'কলাম-I (জীব)-এর সাথে কলাম-II (বৈশিষ্ট্য) মেলাও:<br>A. Sphagnum<br>B. Marchantia<br>C. Selaginella<br>D. '
          'Pinus<br>1. উইংড বা পক্ষল পরাগরেণু<br>2. পিট গঠন<br>3. গেমা কাপ<br>4. হেটারোস্পোরি ও বীজ স্বভাবের অগ্রদূত',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Match Column-I (Organisms) with Column-II (Characteristic Structure):<br>A. Sphagnum<br>B. Marchantia<br>C. '
          'Selaginella<br>D. Pinus<br>1. Winged pollen grain<br>2. Peat formation<br>3. Gemma cups<br>4. Heterospory '
          'and precursor to seed habit',
    'exam': 'NEET, CUET',
    'expl_bn': 'Sphagnum = পিট মস (A-2); Marchantia = গেমা কাপ (B-3); Selaginella = হেটারোস্পোরি (C-4); Pinus = পক্ষল '
               'পরাগরেণু (D-1)।',
    'expl_en': 'Sphagnum = Peat (A-2); Marchantia = Gemma cups (B-3); Selaginella = Heterospory (C-4); Pinus = Winged '
               'pollen (D-1).',
    'id': 'BIO-PK-124',
    'opts': { 'bn': ['A-2, B-3, C-4, D-1', 'A-3, B-2, C-4, D-1', 'A-2, B-4, C-3, D-1', 'A-1, B-3, C-4, D-2'],
              'en': ['A-2, B-3, C-4, D-1', 'A-3, B-2, C-4, D-1', 'A-2, B-4, C-3, D-1', 'A-1, B-3, C-4, D-2']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'কলাম-I (টেরিডোফাইটা শ্রেণি)-এর সাথে কলাম-II (গণ) মেলাও:<br>A. সাইলোপসিডা<br>B. লাইকোপসিডা<br>C. '
          'স্ফেনোপসিডা<br>D. টেরোপসিডা<br>1. ইকুইসিটাম<br>2. সাইলোটাম<br>3. ড্রায়োপ্টেরিস, টেরিস, '
          'অ্যাডিয়েন্টাম<br>4. সিলাজিনেলা, লাইকোপোডিয়াম',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Match Column-I (Pteridophyte class) with Column-II (Genus):<br>A. Psilopsida<br>B. Lycopsida<br>C. '
          'Sphenopsida<br>D. Pteropsida<br>1. Equisetum<br>2. Psilotum<br>3. Dryopteris, Pteris, Adiantum<br>4. '
          'Selaginella, Lycopodium',
    'exam': 'NEET, CUET',
    'expl_bn': 'Psilopsida = Psilotum (A-2); Lycopsida = Selaginella (B-4); Sphenopsida = Equisetum (C-1); Pteropsida '
               '= Dryopteris (D-3)।',
    'expl_en': 'Psilopsida = Psilotum (A-2); Lycopsida = Selaginella (B-4); Sphenopsida = Equisetum (C-1); Pteropsida '
               '= Dryopteris/Pteris (D-3).',
    'id': 'BIO-PK-125',
    'opts': { 'bn': ['A-2, B-4, C-1, D-3', 'A-1, B-4, C-2, D-3', 'A-2, B-1, C-4, D-3', 'A-4, B-2, C-1, D-3'],
              'en': ['A-2, B-4, C-1, D-3', 'A-1, B-4, C-2, D-3', 'A-2, B-1, C-4, D-3', 'A-4, B-2, C-1, D-3']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'কলাম-I (শৈবাল)-এর সাথে কলাম-II (অর্থনৈতিক গুরুত্ব) মেলাও:<br>A. Gelidium<br>B. Chlorella<br>C. '
          'Laminaria<br>D. Porphyra<br>1. মহাকাশ খাদ্য পরিপূরক<br>2. অ্যাগার-অ্যাগার<br>3. ভক্ষণযোগ্য সামুদ্রিক '
          'খাদ্য<br>4. আয়োডিন ও অ্যালজিন উৎস',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Match Column-I (Alga) with Column-II (Economic product / feature):<br>A. Gelidium<br>B. Chlorella<br>C. '
          'Laminaria<br>D. Porphyra<br>1. Space food supplement<br>2. Agar-agar<br>3. Edible marine alga<br>4. Iodine '
          'and algin source',
    'exam': 'NEET, CUET',
    'expl_bn': 'জেলিডিয়াম = অ্যাগার (A-2); ক্লোরেলা = মহাকাশ খাদ্য (B-1); ল্যামিনারিয়া = আয়োডিন/অ্যালজিন (C-4); '
               'পরফাইরা = ভোজ্য খাদ্য (D-3)।',
    'expl_en': 'Gelidium = Agar (A-2); Chlorella = Space food (B-1); Laminaria = Iodine/algin (C-4); Porphyra = Edible '
               'alga eaten as nori (D-3).',
    'id': 'BIO-PK-126',
    'opts': { 'bn': ['A-2, B-1, C-4, D-3', 'A-1, B-2, C-4, D-3', 'A-2, B-4, C-1, D-3', 'A-3, B-1, C-4, D-2'],
              'en': ['A-2, B-1, C-4, D-3', 'A-1, B-2, C-4, D-3', 'A-2, B-4, C-1, D-3', 'A-3, B-1, C-4, D-2']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিচের কোনটি অশাখ কলোনিয়াল সবুজ শৈবাল নয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following is NOT an unbranched colonial green alga?',
    'exam': 'NEET, CUET',
    'expl_bn': 'এক্টোকার্পাস হলো একটি শাখাযুক্ত সূত্রাকার বাদামী শৈবাল, কলোনিয়াল সবুজ শৈবাল নয়।',
    'expl_en': 'Ectocarpus is a filamentous, branched brown alga (Phaeophyceae), not a green colonial alga.',
    'id': 'BIO-PK-127',
    'opts': { 'bn': ['এক্টোকার্পাস (শাখাযুক্ত সূত্রাকার বাদামী শৈবাল)', 'ভলভক্স', 'প্যান্ডোরিনা', 'ইউডোরিনা'],
              'en': ['Ectocarpus (branched filamentous brown alga)', 'Volvox', 'Pandorina', 'Eudorina']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'ব্যক্তবীজী সংক্রান্ত নিচের বক্তব্যগুলি বিবেচনা করো:<br>(i) ডিম্বকগুলি মেগাস্পোরোফিলের ওপর অনাবৃত '
          'থাকে।<br>(ii) মূলগুলি প্রধানত স্থানিক প্রধান মূল (taproot)।<br>(iii) সাইকাসে পুং ও স্ত্রী শঙ্কু একই গাছে '
          'জন্মায়।<br>(iv) পাইনাসে কাণ্ড শাখাপ্রশাখা যুক্ত।<br>উপরের বিবৃতিগুলির মধ্যে কতগুলি সঠিক?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Read the following statements regarding gymnosperms:<br>(i) Ovules are naked on megasporophylls.<br>(ii) '
          'Roots are generally taproots.<br>(iii) In Cycas, male and female cones are borne on the same tree.<br>(iv) '
          'In Pinus, stem is branched.<br>How many of the above statements are CORRECT?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'বিবৃতি (iii) ভুল কারণ সাইকাস ভিন্নবাসী (dioecious)। বাকি (i), (ii) এবং (iv) সঠিক। তাই মোট ৩টি বিবৃতি '
               'সঠিক।',
    'expl_en': 'Statement (iii) is FALSE because Cycas is dioecious (male cone and megasporophylls are on separate '
               'plants). Statements (i), (ii), and (iv) are true NCERT facts.',
    'id': 'BIO-PK-128',
    'opts': { 'bn': ['৩টি বিবৃতি: (i), (ii), এবং (iv)', 'সবকটি ৪টি বিবৃতি', 'কেবল ২টি বিবৃতি', 'কেবল ১টি বিবৃতি'],
              'en': ['3 statements: (i), (ii), and (iv)', 'All 4 statements', 'Only 2 statements', 'Only 1 statement']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'প্রদত্ত উদ্ভিদগুলির মধ্যে কতগুলির দেহে সংবহন কলা (জাইলেম ও ফ্লোয়েম) বর্তমান?<br>[Volvox, Marchantia, '
          'Sphagnum, Selaginella, Equisetum, Pinus, Wolffia, Polysiphonia]',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'How many of the following plants possess vascular tissues (Xylem & Phloem)?<br>[Volvox, Marchantia, '
          'Sphagnum, Selaginella, Equisetum, Pinus, Wolffia, Polysiphonia]',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'সংবহনকলাযুক্ত উদ্ভিদ (Tracheophytes) হলো টেরিডোফাইট থেকে শুরু: Selaginella, Equisetum, Pinus এবং '
               'Wolffia (মোট ৪টি)। শৈবাল ও ব্রায়োফাইটে সংবহন কলা থাকে না।',
    'expl_en': 'Vascular plants (Tracheophytes) start from Pteridophytes onwards: Selaginella (pteridophyte), '
               'Equisetum (pteridophyte), Pinus (gymnosperm), and Wolffia (angiosperm) = 4 plants. Volvox and '
               'Polysiphonia are non-vascular algae; Marchantia and Sphagnum are non-vascular bryophytes.',
    'id': 'BIO-PK-129',
    'opts': { 'bn': ['৪টি (Selaginella, Equisetum, Pinus, Wolffia)', '৩টি', '৫টি', '৬টি'],
              'en': ['4 (Selaginella, Equisetum, Pinus, Wolffia)', '3', '5', '6']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিচের বৈশিষ্ট্যগুলি বিবেচনা করো:<br>১. প্রোটোনেমা দশা<br>২. বহুকোষী শাখাযুক্ত রাইজয়েড<br>৩. রেণু বিচ্ছুরণে '
          'জটিল পেরিস্টোম দাঁতের উপস্থিতি<br>এই বৈশিষ্ট্যগুলি সামগ্রিকভাবে কাকে নির্দেশ করে?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Consider the following features:<br>1. Protonema stage<br>2. Multicellular branched rhizoids<br>3. '
          'Elaborate peristome teeth mechanism for spore dispersal<br>These diagnostic features collectively define:',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'প্রোটোনেমা, বহুকোষী তির্যক প্রাচীরযুক্ত রাইজয়েড এবং পেরিস্টোম দাঁত—এগুলি মসের (যেমন ফিউনারিয়া) একক '
               'শনাক্তকারী বৈশিষ্ট্য।',
    'expl_en': 'All three are signature defining features of mosses (Bryopsida): protonema, multicellular branched '
               'rhizoids with oblique septa, and capsule with peristome teeth.',
    'id': 'BIO-PK-130',
    'opts': { 'bn': [ 'মস (যেমন ফিউনারিয়া)',
                      'লিভারওয়ার্ট (যেমন মারকানশিয়া)',
                      'টেরিডোফাইটা (যেমন ফার্ন)',
                      'শৈবাল (যেমন কারা)'],
              'en': [ 'Mosses (such as Funaria)',
                      'Liverworts (such as Marchantia)',
                      'Pteridophytes (such as Ferns)',
                      'Algae (such as Chara)']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'নিচের কোন ব্যক্তবীজীতে চলনক্ষম সিলিয়াযুক্ত শুক্রাণুর সম্পূর্ণ অভাব দেখা যায় এবং পরাগনালীর মাধ্যমে নিশ্চল '
          'শুক্রাণু পরিবাহিত হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Which of the following gymnosperms lacks motile ciliated male gametes and exhibits completely non-motile '
          'sperm transported by siphonogamy?',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাইনাসের শুক্রাণু সম্পূর্ণ নিশ্চল এবং তা পরাগনালী দ্বারা বাহিত হয়। সাইকাস ও জিংগোতে আদিম বৈশিষ্ট্য '
               'হিসেবে সিলিয়াযুক্ত সচল শুক্রাণু থাকে।',
    'expl_en': 'Pinus has non-motile male gametes carried strictly by pollen tube (siphonogamy). Cycas and Ginkgo are '
               'primitive gymnosperms that still retain swimming multiflagellated sperm (zooidogamy combined with '
               'siphonogamy).',
    'id': 'BIO-PK-131',
    'opts': {'bn': ['পাইনাস (Pinus)', 'সাইকাস', 'জিংগো', 'জ্যামিয়া'], 'en': ['Pinus', 'Cycas', 'Ginkgo', 'Zamia']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'কোরালিনা (Corallina)-র মতো কোরালাইন শৈবাল তাদের কোষপ্রাচীরে বিপুল পরিমাণ ________ সঞ্চয় করে প্রবাল প্রাচীর '
          '(Coral reef) গঠনে ভূমিকা রাখে।',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Coralline algae like Corallina secrete heavy deposits of ________ in their cell walls, contributing '
          'significantly to coral reef formation.',
    'exam': 'NEET, CUET',
    'expl_bn': 'কোরালাইন লাল শৈবাল তাদের প্রাচীরে ক্যালসিয়াম কার্বনেট সঞ্চয় করে পাথরের মতো শক্ত প্রাচীর তৈরি করে যা '
               'প্রবাল প্রাচীর সৃষ্টিতে সাহায্য করে।',
    'expl_en': 'Coralline red algae deposit calcite (calcium carbonate) into their cell walls, making them stony and '
               'providing structural foundation for tropical marine coral reefs.',
    'id': 'BIO-PK-132',
    'opts': { 'bn': [ 'ক্যালসিয়াম কার্বনেট (CaCO3)',
                      'সিলিকন ডাইঅক্সাইড (SiO2)',
                      'ম্যাগনেসিয়াম সালফেট',
                      'সোডিয়াম ক্লোরাইড'],
              'en': ['Calcium carbonate (CaCO3)', 'Silicon dioxide (SiO2)', 'Magnesium sulphate', 'Sodium chloride']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'লিভারওয়ার্টে কোন বিশেষ হাইগ্রোস্কোপিক ডিপ্লয়েড গঠনগুলি আর্দ্রতার পরিবর্তনে কুঁচকে গিয়ে ক্যাপসুল থেকে '
          'স্পোর বাইরে নিক্ষেপ করে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In liverworts, which specialized hygroscopic diploid structures twist and coil to fling spores out of the '
          'ruptured capsule?',
    'exam': 'NEET, CUET',
    'expl_bn': 'মারকানশিয়ার ক্যাপসুলে সর্পিলাকার স্থূলীকরণযুক্ত ইলেটার্স (Elaters) থাকে যা আর্দ্রতার পরিবর্তনে পাক '
               'খেয়ে স্পোর নিক্ষেপ করে।',
    'expl_en': 'In Marchantia capsule, spindle-shaped diploid cells with helical thickenings called elaters twist '
               'hygroscopically as they dry, flicking spores into passing air currents.',
    'id': 'BIO-PK-133',
    'opts': { 'bn': ['ইলেটার্স (Elaters)', 'পেরিস্টোম দাঁত', 'সিউডোইলেটার্স', 'অ্যানুলাস'],
              'en': ['Elaters', 'Peristome teeth', 'Pseudoelaters', 'Annulus']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'একটি মসের প্রোটোনেমা কোষে যদি ১৮টি ক্রোমোজোম থাকে, তবে তার রাইজয়েড, পাতার কোষ, অপারকুলাম কোষ এবং স্পোর '
          'মাতৃকোষে ক্রোমোজোম সংখ্যা যথাক্রমে কত হবে?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'If a moss protonema cell has 18 chromosomes, how many chromosomes will be present respectively in its '
          'rhizoid, leaf cell, operculum cell, and spore mother cell?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'মসের গ্যামেটোফাইট হ্যাপ্লয়েড (n = 18), তাই প্রোটোনেমা, রাইজয়েড ও পাতার কোষ = ১৮। অপারকুলাম ও স্পোর '
               'মাতৃকোষ স্পোরোফাইটের অংশ হওয়ায় ডিপ্লয়েড (2n = 36)। অতএব ১৮, ১৮, ৩৬, ৩৬।',
    'expl_en': 'Moss protonema is gametophytic (n = 18). Rhizoid is gametophytic (n = 18). Leaf cell is gametophytic '
               '(n = 18). Operculum is part of the capsule of the sporophyte (2n = 36). Spore mother cell is '
               'sporophytic (2n = 36). Hence: 18, 18, 36, 36.',
    'id': 'BIO-PK-134',
    'opts': { 'bn': ['১৮, ১৮, ৩৬, ৩৬', '১৮, ৩৬, ৩৬, ১৮', '৯, ১৮, ৩৬, ১৮', '১৮, ১৮, ১৮, ৩৬'],
              'en': ['18, 18, 36, 36', '18, 36, 36, 18', '9, 18, 36, 18', '18, 18, 18, 36']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'},
  { 'bn': 'স্থলজ উদ্ভিদের বিবর্তনে গ্যামেটোফাইট দশার ক্রমহ্রাস এবং স্পোরোফাইট দশার ক্রমবর্ধমান আধিপত্যের সঠিক '
          'বিবর্তনীয় ধারা কোনটি?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Which of the following evolutionary sequences correctly outlines the progressive reduction of the '
          'gametophytic generation and dominance of the sporophytic generation in land plants?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'উদ্ভিদ বিবর্তনে গ্যামেটোফাইট বা লিঙ্গধর দশাটি ক্রমশ সংকুচিত হয়েছে: ব্রায়োফাইটে এটি প্রধান উদ্ভিদ, '
               'টেরিডোফাইটে এটি ক্ষুদ্র প্রোথ্যালাস এবং ব্যক্তবীজী ও গুপ্তবীজীতে এটি স্পোরোফাইটের ভেতর আবদ্ধ কয়েকটি '
               'আণুবীক্ষণিক কোষে পরিণত হয়েছে।',
    'expl_en': 'Plant evolution demonstrates progressive reduction of the haploid gametophyte: in bryophytes it is the '
               'main plant; in pteridophytes it is reduced to a small prothallus; in gymnosperms/angiosperms it is '
               'reduced to microscopic cells completely enclosed inside sporangia on the sporophyte.',
    'id': 'BIO-PK-135',
    'opts': { 'bn': [ 'ব্রায়োফাইটা (প্রধান গ্যামেটোফাইট, নির্ভরশীল স্পোরোফাইট) → টেরিডোফাইটা (প্রধান স্পোরোফাইট, '
                      'স্বাধীন গ্যামেটোফাইট) → ব্যক্তবীজী (প্রধান স্পোরোফাইট, ডিম্বক ও পরাগরেণুর ভেতরে আবদ্ধ '
                      'আণুবীক্ষণিক নির্ভরশীল গ্যামেটোফাইট)',
                      'টেরিডোফাইটা → ব্রায়োফাইটা → ব্যক্তবীজী',
                      'ব্যক্তবীজী → টেরিডোফাইটা → ব্রায়োফাইটা',
                      'ব্রায়োফাইটা → ব্যক্তবীজী → টেরিডোফাইটা'],
              'en': [ 'Bryophytes (Dominant gametophyte, dependent sporophyte) → Pteridophytes (Dominant sporophyte, '
                      'independent gametophyte) → Gymnosperms (Dominant sporophyte, microscopic dependent gametophyte '
                      'enclosed in ovule/pollen)',
                      'Pteridophytes → Bryophytes → Gymnosperms',
                      'Gymnosperms → Pteridophytes → Bryophytes',
                      'Bryophytes → Gymnosperms → Pteridophytes']},
    'subject': 'Biology',
    'topic': 'Plant Kingdom'}]
