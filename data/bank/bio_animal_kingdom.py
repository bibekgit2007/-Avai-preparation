# =============================================================================
# BIOLOGY QUESTION BANK - CHAPTER 4: ANIMAL KINGDOM (135 Questions)
# Graded Question Pyramid (MTG NCERT at your Fingertips Pattern)
# Mapped to NEET, AIIMS, CUET, IAT, OLYMPIAD
# =============================================================================

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

bio_animal_kingdom_questions = [ { 'bn': 'কোন পর্বে কোষগুলি ঢিলেঢালাভাবে পুঞ্জীভূত হয়ে অবস্থান করে এবং প্রকৃত কলা গঠন না করে কোষীয় মাত্রার '
          '(cellular level) দৈহিক সংগঠন প্রদর্শন করে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'In which phylum are cells arranged as loose cell aggregates exhibiting a cellular level of organization '
          'without forming true tissues?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'পরিফেরা বা স্পঞ্জের দেহে কোষগুলি পৃথক বা ঢিলেঢালাভাবে পুঞ্জীভূত থাকে এবং কোনো সুসংগঠিত কলা তৈরি করে '
               'না, একে কোষীয় মাত্রার সংগঠন বলে।',
    'expl_en': 'In sponges (Phylum Porifera), the cells are arranged as loose cell aggregates, i.e., they exhibit '
               'cellular level of organisation.',
    'id': 'BIO-AK-001',
    'opts': { 'bn': ['পরিফেরা বা স্পঞ্জ (Porifera)', 'সিলেন্টারেটা', 'টিনোফোরা', 'প্লাটিহেলমিন্থেস'],
              'en': ['Porifera (Sponges)', 'Coelenterata', 'Ctenophora', 'Platyhelminthes']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোন পর্বটিতে কলা মাত্রার (tissue level) দৈহিক সংগঠন পরিলক্ষিত হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following phyla exhibits tissue level of body organization?',
    'exam': 'NEET, CUET',
    'expl_bn': 'সিলেন্টারেটা এবং টিনোফোরা পর্বের প্রাণীদের ক্ষেত্রে সমজাতীয় কাজের কোষগুলি মিলে কলা গঠন করে, অর্থাৎ '
               'এরা কলা-মাত্রার সংগঠনযুক্ত।',
    'expl_en': 'In coelenterates (cnidarians) and ctenophores, the arrangement of cells is more complex and cells '
               'performing the same function are arranged into tissues, hence tissue level of organization.',
    'id': 'BIO-AK-002',
    'opts': { 'bn': [ 'সিলেন্টারেটা (নিডারিয়া) এবং টিনোফোরা',
                      'কেবল পরিফেরা',
                      'প্লাটিহেলমিন্থেস এবং অ্যাসকেলমিন্থেস',
                      'অ্যানেলিডা এবং আর্থ্রোপোডা'],
              'en': [ 'Coelenterata (Cnidaria) and Ctenophora',
                      'Porifera only',
                      'Platyhelminthes and Aschelminthes',
                      'Annelida and Arthropoda']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'একটিমাত্র বহিস্থ ছিদ্রযুক্ত অসম্পূর্ণ পৌষ্টিকতন্ত্র যা মুখ ও পায়ু উভয় হিসেবেই কাজ করে, তা কোন পর্বে দেখা '
          'যায়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'An incomplete digestive system having only a single opening to the outside of the body that serves as both '
          'mouth and anus is found in:',
    'exam': 'NEET, CUET',
    'expl_bn': 'প্লাটিহেলমিন্থেস বা চ্যাপ্টাকৃমির পৌষ্টিকনালীতে একটিমাত্র ছিদ্র থাকে যা খাদ্য গ্রহণ ও বর্জ্য নির্গমন '
               'উভয়ের কাজ করে (Blind sac body plan)।',
    'expl_en': 'Incomplete digestive system has only a single opening to the outside of the body that serves as both '
               'mouth and anus, as in Platyhelminthes. A complete digestive system has two openings (mouth and anus).',
    'id': 'BIO-AK-003',
    'opts': { 'bn': ['প্লাটিহেলমিন্থেস বা চ্যাপ্টাকৃমি (Platyhelminthes)', 'অ্যাসকেলমিন্থেস', 'অ্যানেলিডা', 'কর্ডাটা'],
              'en': ['Platyhelminthes (Flatworms)', 'Aschelminthes', 'Annelida', 'Chordata']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'দেহের কেন্দ্রীয় অক্ষ বরাবর যেকোনো তল দিয়ে অতিক্রমকারী রেখা যদি দেহকে দুটি সদৃশ অর্ধাংশে বিভক্ত করে, তবে '
          'তাকে কী বলে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'When any plane passing through the central axis of the body divides the organism into two identical halves, '
          'it is called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'কেন্দ্রীয় অক্ষ বরাবর যেকোনো তলে দেহকে সমান দুই ভাগে ভাগ করা গেলে তাকে অরীয় প্রতিসাম্য (Radial '
               'symmetry) বলে।',
    'expl_en': 'When any plane passing through the central axis of the body divides the organism into two identical '
               'halves, it is called radial symmetry. Coelenterates, ctenophores and echinoderms have this kind of '
               'body plan.',
    'id': 'BIO-AK-004',
    'opts': { 'bn': [ 'অরীয় প্রতিসাম্য বা রেডিয়াল সিমেট্রি (Radial symmetry - যেমন সিলেন্টারেটা, টিনোফোরা, পূর্ণাঙ্গ '
                      'একাইনোডার্মাটা)',
                      'দ্বিপার্শ্বীয় প্রতিসাম্য (যেমন অ্যানেলিডা, আর্থ্রোপোডা)',
                      'অপ্রতিসাম্য (যেমন অধিকাংশ স্পঞ্জ)',
                      'গোলাকার খণ্ডায়ন'],
              'en': [ 'Radial symmetry (e.g., Coelenterates, Ctenophores, adult Echinoderms)',
                      'Bilateral symmetry (e.g., Annelids, Arthropods)',
                      'Asymmetry (e.g., most sponges)',
                      'Spherical segmentation']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'যেসব প্রাণীর দেহকে কেবলমাত্র একটিমাত্র নির্দিষ্ট উল্লম্ব তলে সদৃশ বাম ও ডান অর্ধাংশে বিভক্ত করা যায়, তারা '
          'কী প্রদর্শন করে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Animals in which the body can be divided into identical left and right halves in only ONE plane exhibit:',
    'exam': 'NEET, CUET',
    'expl_bn': 'একটিমাত্র তলে দেহকে দুটি সদৃশ অর্ধাংশে (ডান ও বাম) ভাগ করা গেলে তাকে দ্বিপার্শ্বীয় প্রতিসাম্য '
               '(Bilateral symmetry) বলে।',
    'expl_en': 'Animals like annelids, arthropods, etc., where the body can be divided into identical left and right '
               'halves in only one plane, exhibit bilateral symmetry.',
    'id': 'BIO-AK-005',
    'opts': { 'bn': [ 'দ্বিপার্শ্বীয় প্রতিসাম্য বা বাইল্যাটেরাল সিমেট্রি (Bilateral symmetry - যেমন প্লাটিহেলমিন্থেস '
                      'থেকে কর্ডাটা)',
                      'অরীয় প্রতিসাম্য',
                      'অপ্রতিসাম্য',
                      'দ্বি-অরীয় অপ্রতিসাম্য'],
              'en': [ 'Bilateral symmetry (e.g., Platyhelminthes to Chordates)',
                      'Radial symmetry',
                      'Asymmetry',
                      'Biradial asymmetry']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'যেসব প্রাণীর ভ্রূণীয় কোষগুলি বাইরের একটোডার্ম ও ভেতরের এন্ডোডার্ম নামক দুটি স্তরে এবং তাদের মাঝে অবিভেদিত '
          'মেসোগ্লিয়া (mesoglea) দ্বারা বিন্যস্ত থাকে, তাদের কী বলে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Animals in which the cells are arranged in two embryonic layers, an external ectoderm and an internal '
          'endoderm with an undifferentiated layer called mesoglea in between, are called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'এক্টোডার্ম ও এন্ডোডার্ম স্তরবিশিষ্ট এবং এদের মাঝে অকোষীয় মেসোগ্লিয়াযুক্ত প্রাণীদের দ্বিস্তরীয় বা '
               'ডিপ্লোব্লাস্টিক প্রাণী বলে।',
    'expl_en': 'Animals in which cells are arranged in two embryonic layers, external ectoderm and internal endoderm, '
               'are called diploblastic (e.g., coelenterates). An undifferentiated non-cellular layer, mesoglea, is '
               'present between them.',
    'id': 'BIO-AK-006',
    'opts': { 'bn': [ 'দ্বিস্তরীয় বা ডিপ্লোব্লাস্টিক প্রাণী (Diploblastic - যেমন সিলেন্টারেটা ও টিনোফোরা)',
                      'ত্রিস্তরীয় বা ট্রিপ্লোব্লাস্টিক প্রাণী (প্লাটিহেলমিন্থেস থেকে কর্ডাটা)',
                      'সিউডোসিলোমেট',
                      'অ্যাসিলোমেট'],
              'en': [ 'Diploblastic animals (e.g., Coelenterates and Ctenophores)',
                      'Triploblastic animals (e.g., Platyhelminthes to Chordates)',
                      'Pseudocoelomates',
                      'Acoelomates']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'কোন পর্বে দেহগহ্বরটি মেসোডার্ম দ্বারা সম্পূর্ণরূপে আবৃত থাকে না, বরং একটোডার্ম ও এন্ডোডার্মের মাঝে '
          'মেসোডার্মটি বিক্ষিপ্ত থলির (pouches) মতো অবস্থান করে (সিউডোসিলোম)?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In which phylum is the body cavity NOT lined by mesoderm; instead, the mesoderm is present as scattered '
          'pouches between the ectoderm and endoderm (Pseudocoelom)?',
    'exam': 'NEET, CUET',
    'expl_bn': 'অ্যাসকেলমিন্থেস বা গোলকৃমিতে প্রকৃত সিলোমের পরিবর্তে মেসোডার্মীয় থলি বিক্ষিপ্তভাবে থাকে, তাই এদের '
               'সিউডোসিলোমেট (Pseudocoelomate) বলে।',
    'expl_en': 'In some animals, the body cavity is not lined by mesoderm, instead, the mesoderm is present as '
               'scattered pouches in between the ectoderm and endoderm. Such a body cavity is called pseudocoelom and '
               'the animals possessing them are called pseudocoelomates (e.g., aschelminthes).',
    'id': 'BIO-AK-007',
    'opts': { 'bn': ['অ্যাসকেলমিন্থেস বা গোলকৃমি (Aschelminthes)', 'প্লাটিহেলমিন্থেস', 'অ্যানেলিডা', 'মোলাস্কা'],
              'en': ['Aschelminthes (Roundworms)', 'Platyhelminthes', 'Annelida', 'Mollusca']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'যেসব প্রাণীর দেহে কোনো প্রকার সিলোম বা দেহগহ্বর থাকেই না (অ্যাসিলোমেট), তাদের উদাহরণ কোনটি?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Animals in which the body cavity is completely absent are called acoelomates. An example is:',
    'exam': 'NEET, CUET',
    'expl_bn': 'প্লাটিহেলমিন্থেসের দেহে কোনো দেহগহ্বর বা সিলোম থাকে না (অ্যাসিলোমেট), অঙ্গগুলির মধ্যবর্তী স্থান '
               'প্যারেনকাইমা কলা দ্বারা পূর্ণ থাকে।',
    'expl_en': 'The animals in which the body cavity is absent are called acoelomates, e.g., platyhelminthes. The '
               'space between organs is filled with solid mesodermal parenchyma.',
    'id': 'BIO-AK-008',
    'opts': { 'bn': [ 'প্লাটিহেলমিন্থেস বা চ্যাপ্টাকৃমি (Platyhelminthes)',
                      'অ্যানেলিডা',
                      'আর্থ্রোপোডা',
                      'অ্যাসকেলমিন্থেস'],
              'en': [ 'Platyhelminthes (Flatworms)',
                      'Annelida (Earthworm)',
                      'Arthropoda (Cockroach)',
                      'Aschelminthes (Ascaris)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'দেহের অন্তত কয়েকটি অঙ্গের পৌনঃপুনিক পুনরাবৃত্তিসহ প্রকৃত অভ্যন্তরীণ ও বাহ্যিক খণ্ডায়নকে মেটামারিজম বলে। '
          'এটি স্পষ্টভাবে কোন পর্বে দেখা যায়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'True internal and external serial segmentation of the body with repetition of at least some organs is known '
          'as metamerism (metameric segmentation). It is prominently exhibited by:',
    'exam': 'NEET, CUET',
    'expl_bn': 'প্রকৃত মেটামেরিক খণ্ডায়ন দেখা যায় অ্যানেলিডা (যেমন কেঁচো), আর্থ্রোপোডা এবং কর্ডাটাতে।',
    'expl_en': 'In animals like earthworm, the body shows true metameric segmentation where body is externally and '
               'internally divided into segments with serial repetition of at least some organs. True metamerism '
               'occurs in Annelids, Arthropods, and Chordates.',
    'id': 'BIO-AK-009',
    'opts': { 'bn': [ 'অ্যানেলিডা, আর্থ্রোপোডা এবং কর্ডাটা',
                      'পরিফেরা এবং সিলেন্টারেটা',
                      'প্লাটিহেলমিন্থেস এবং অ্যাসকেলমিন্থেস',
                      'মোলাস্কা এবং একাইনোডার্মাটা'],
              'en': [ 'Annelida, Arthropoda, and Chordata',
                      'Porifera and Coelenterata',
                      'Platyhelminthes and Aschelminthes',
                      'Mollusca and Echinodermata']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নোটোকর্ড হলো মেসোডার্ম থেকে উৎপন্ন দণ্ডাকার গঠন যা ভ্রূণীয় বিকাশের সময় দেহের ________ দিকে গঠিত হয়।',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The notochord is a mesodermally derived rod-like structure formed on the ________ side during embryonic '
          'development in some animals.',
    'exam': 'NEET, CUET',
    'expl_bn': 'নোটোকর্ড হলো ভ্রূণের মেসোডার্ম থেকে উৎপন্ন একটি স্থিতিস্থাপক দণ্ডাকার গঠন যা দেহের পৃষ্ঠীয় (dorsal) '
               'দিকে গঠিত হয়।',
    'expl_en': 'Notochord is a mesodermally derived rod-like structure formed on the dorsal side during embryonic '
               'development in chordates.',
    'id': 'BIO-AK-010',
    'opts': { 'bn': [ 'পৃষ্ঠীয় বা ডরসাল দিকে (Dorsal side)',
                      'অঙ্কীয় বা ভেন্ট্রাল দিকে',
                      'পার্শ্বীয় দিকে',
                      'অগ্রপ্রান্তে'],
              'en': ['Dorsal side', 'Ventral side', 'Lateral side', 'Anterior tip']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'স্পঞ্জে (Porifera) দেহপ্রাচীরের ক্ষুদ্র ক্ষুদ্র ছিদ্র ________ দিয়ে জল কেন্দ্রীয় গহ্বর ________-এ প্রবেশ '
          'করে এবং সেখান থেকে ________ দিয়ে বাইরে নির্গত হয়।',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In sponges (Phylum Porifera), water enters through minute pores called ________ in the body wall into a '
          'central cavity called ________, from where it goes out through the ________.',
    'exam': 'NEET, CUET',
    'expl_bn': 'জল সংবহন বা নালী তন্ত্রের মাধ্যমে জল অস্টিয়া (ostia) ছিদ্র দিয়ে কেন্দ্রীয় স্পঞ্জোসিলে ঢোকে এবং '
               'অসকুলাম (osculum) দিয়ে বাইরে বের হয়ে যায়।',
    'expl_en': 'Sponges have a water transport or canal system. Water enters through minute pores (ostia) in the body '
               'wall into a central cavity, spongocoel, from where it goes out through the osculum.',
    'id': 'BIO-AK-011',
    'opts': { 'bn': [ 'অস্টিয়া (Ostia); স্পঞ্জোসিল (Spongocoel); অসকুলাম (Osculum)',
                      'অসকুলা; স্পঞ্জোসিল; অস্টিয়াম',
                      'হাইপোস্টোম; গ্যাস্ট্রোভাসকুলার গহ্বর; পায়ু',
                      'স্পিকিউল; প্যারাগ্যাস্ট্রিক প্রকোষ্ঠ; মুখ'],
              'en': [ 'Ostia; Spongocoel; Osculum',
                      'Oscula; Spongocoel; Ostium',
                      'Hypostome; Gastrovascular cavity; Anus',
                      'Spicules; Paragastric chamber; Mouth']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'স্পঞ্জের স্পঞ্জোসিল এবং নালীগুলিকে আবৃত করে রাখা বিশেষ ধরনের কলারযুক্ত কোষগুলিকে কী বলে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Specialized collar cells that line the spongocoel and canals in sponges are called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'কোয়ানোসাইট (Choanocytes) বা কলার কোষ হলো পরিফেরা পর্বের অনন্য বৈশিষ্ট্যপূর্ণ কোষ যা স্পঞ্জোসিলকে ঘিরে '
               'রাখে এবং জলপ্রবাহ বজায় রেখে খাদ্য সংগ্রহ করে।',
    'expl_en': 'Choanocytes or collar cells line the spongocoel and the canals in sponges, maintaining water flow and '
               'trapping food particles by phagocytosis.',
    'id': 'BIO-AK-012',
    'opts': { 'bn': ['কোয়ানোসাইট বা কলার কোষ (Choanocytes)', 'নিডোসাইট', 'প্যাকোডোসাইট', 'আর্কিওসাইট'],
              'en': ['Choanocytes (Collar cells)', 'Cnidocytes', 'Pinacocytes', 'Archaeocytes']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'পরিফেরা বা স্পঞ্জের পুষ্টি ও পরিপাক পদ্ধতি কেমন প্রকৃতির?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Digestion in sponges (Porifera) is strictly:',
    'exam': 'NEET, CUET',
    'expl_bn': 'স্পঞ্জের দেহে পরিপাক প্রক্রিয়া সম্পূর্ণ অন্তঃকোষীয় (intracellular), যা কোষের খাদ্য গহ্বরের ভেতরে '
               'উৎসেচক দ্বারা সম্পন্ন হয়।',
    'expl_en': 'In sponges, digestion is intracellular. Food particles filtered by choanocytes are engulfed and '
               'digested inside food vacuoles within cells (amoebocytes/choanocytes).',
    'id': 'BIO-AK-013',
    'opts': { 'bn': [ 'অন্তঃকোষীয় বা ইন্ট্রাসেলুলার (কোষীয় খাদ্য গহ্বরের মধ্যে সম্পন্ন হয়)',
                      'বহিঃকোষীয়',
                      'বহিঃকোষীয় ও অন্তঃকোষীয় উভয়ই',
                      'কেরাটিনযুক্ত চঞ্চুর সাহায্যে'],
              'en': [ 'Intracellular (takes place inside food vacuoles of cells)',
                      'Extracellular in an acidic stomach cavity',
                      'Both extracellular and intracellular in gastrovascular cavity',
                      'Holozoic through a keratinized beak']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'স্পঞ্জের দেহের অভ্যন্তরীণ কঙ্কাল কী দ্বারা গঠিত?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The body of sponges is supported by a skeleton made up of:',
    'exam': 'NEET, CUET',
    'expl_bn': 'স্পঞ্জের দেহ কঙ্কাল স্পিকিউল (ক্যালসিয়াম বা সিলিকা কাঁটা) বা স্পঞ্জিন তন্তু (spongin fibres) দিয়ে '
               'দৃঢ়তা লাভ করে।',
    'expl_en': 'The body of sponges is supported by a skeleton made up of spicules (microscopic mineral spikes) or '
               'spongin fibres (flexible collagenous protein).',
    'id': 'BIO-AK-014',
    'opts': { 'bn': [ 'স্পিকিউল (ক্যালসিয়াম/সিলিকা নির্মিত কাঁটা) অথবা স্পঞ্জিন তন্তু (প্রোটিন নির্মিত)',
                      'তরুণাস্থি ও ক্যালসিয়াম ফসফেট অস্থি',
                      'কাইটিনের বহিঃকঙ্কাল',
                      'ক্যালসিয়াম পেকটেটের খোলক'],
              'en': [ 'Spicules (calcareous/siliceous) or spongin fibres (proteinaceous)',
                      'Cartilage and calcium phosphate bones',
                      'Chitinous cuticle',
                      'Calcareous shells of calcium pectate']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোনটি একটি মিষ্ট জলের স্পঞ্জ (Freshwater sponge)?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following is a freshwater sponge?',
    'exam': 'NEET, CUET',
    'expl_bn': 'স্পঞ্জিলা (Spongilla) হলো একটি অন্যতম প্রধান মিষ্ট জলের স্পঞ্জ।',
    'expl_en': 'Spongilla is the classic freshwater sponge. Sycon and Euspongia are marine sponges.',
    'id': 'BIO-AK-015',
    'opts': { 'bn': ['স্পঞ্জিলা (Spongilla)', 'সাইকন বা স্কাইফা', 'ইউস্পঞ্জিয়া বা স্নান স্পঞ্জ', 'ইউপ্লেকটেলা'],
              'en': ['Spongilla', 'Sycon (Scypha)', 'Euspongia (Bath sponge)', 'Euplectella (Venus flower basket)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিডারিয়া পর্বের প্রাণীদের নাম এসেছে বিশেষ দংশক কোষ নিডোসাইট বা নিডোব্লাস্ট থেকে, যার মধ্যে কোন বিষাক্ত '
          'দংশক অঙ্গাণু থাকে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Cnidarians derive their name from specialized stinging cells called cnidoblasts or cnidocytes which contain '
          'stinging capsules called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'নিডোব্লাস্ট কোষে নেমাটোসিস্ট (Nematocysts) নামক দংশন অঙ্গাণু থাকে যা হিপনোটক্সিন বিষ নিক্ষেপ করে শিকার '
               'ধরতে ও আত্মরক্ষায় সাহায্য করে।',
    'expl_en': 'The name cnidaria is derived from the cnidoblasts or cnidocytes (which contain stinging capsules or '
               'nematocysts) present on tentacles and body.',
    'id': 'BIO-AK-016',
    'opts': { 'bn': ['নেমাটোসিস্ট (Nematocysts)', 'কোয়ানোসাইট', 'স্ট্যাটোসিস্ট', 'কলোব্লাস্ট'],
              'en': ['Nematocysts', 'Choanocytes', 'Statocysts', 'Colloblasts']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিডারিয়ার দেহে একটি কেন্দ্রীয় গহ্বর ________ থাকে যার একমাত্র বহিঃছিদ্রটি ________ নামক কোণাকার '
          'অভিক্ষেপের শীর্ষে অবস্থিত।',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Cnidarians exhibit a central body cavity called ________ with a single opening on a conical projection '
          'called ________.',
    'exam': 'NEET, CUET',
    'expl_bn': 'নিডারিয়ার কেন্দ্রীয় গহ্বরকে গ্যাস্ট্রোভাসকুলার গহ্বর বা সিলেন্টেরন বলে, যার মুখে একটিমাত্র ছিদ্র '
               'হাইপোস্টোম (hypostome)-এর ওপর থাকে।',
    'expl_en': 'Cnidarians have a central gastrovascular cavity with a single opening, mouth on hypostome. Digestion '
               'is both extracellular and intracellular.',
    'id': 'BIO-AK-017',
    'opts': { 'bn': [ 'গ্যাস্ট্রোভাসকুলার গহ্বর বা সিলেন্টেরন; হাইপোস্টোম (Hypostome)',
                      'স্পঞ্জোসিল; অসকুলাম',
                      'সিউডোসিলোম; প্রোবোসিস',
                      'এন্টারোসিল; অ্যাম্বুল্যাক্রাল খাঁজ'],
              'en': [ 'Gastrovascular cavity (coelenteron); hypostome',
                      'Spongocoel; osculum',
                      'Pseudocoelom; proboscis',
                      'Enterocoel; ambulacral groove']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিডারিয়ার দুটি প্রধান দৈহিক রূপ হলো পলিপ (Polyp) এবং মেদুসা (Medusa)। নিচের কোন বক্তব্যটি এদের মধ্যে সঠিক '
          'পার্থক্য নির্দেশ করে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Cnidarians exhibit two basic body forms: Polyp and Medusa. Which statement correctly distinguishes them?',
    'exam': 'NEET, CUET',
    'expl_bn': 'পলিপ হলো নিশ্চল ও নলাকার দেহরূপ (যেমন Hydra ও Adamsia), আর মেদুসা হলো ছাতাসদৃশ ও মুক্ত সাঁতারু দেহরূপ '
               '(যেমন Aurelia বা জেলিফিশ)।',
    'expl_en': 'Polyp is a sessile and cylindrical form like Hydra, Adamsia, etc., whereas Medusa is umbrella-shaped '
               'and free-swimming like Aurelia or jelly fish.',
    'id': 'BIO-AK-018',
    'opts': { 'bn': [ 'পলিপ হলো স্থানু বা নিশ্চল এবং নলাকার (যেমন হাইড্রা, অ্যাডামসিয়া); মেদুসা হলো ছাতার মতো এবং '
                      'মুক্ত সাঁতারু (যেমন অরেলিয়া বা জেলিফিশ)',
                      'পলিপ হলো সচল ছাতার মতো এবং মেদুসা নিশ্চল নলাকার',
                      'পলিপ ও মেদুসা উভয়ই সর্বদা স্থানু',
                      'পলিপ যৌন জননে নতুন পলিপ এবং মেদুসা অযৌন জননে মেদুসা তৈরি করে'],
              'en': [ 'Polyp is sessile and cylindrical (e.g., Hydra, Adamsia); Medusa is umbrella-shaped and '
                      'free-swimming (e.g., Aurelia / Jelly fish)',
                      'Polyp is free-swimming and umbrella-shaped; Medusa is sessile and cylindrical',
                      'Both Polyp and Medusa are always sessile and colonial',
                      'Polyp produces polyps sexually; Medusa produces medusae asexually']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'যেসব নিডারিয়াতে পলিপ ও মেদুসার মধ্যে সুনির্দিষ্ট জনুক্রম দেখা যায় (পলিপ অযৌনভাবে মেদুসা তৈরি করে এবং '
          'মেদুসা যৌন জননে পলিপ তৈরি করে, যেমন Obelia-তে), তাকে কী বলা হয়?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'The phenomenon in which cnidarians exhibit alternation of generations between polyp and medusa (polyps '
          'produce medusae asexually and medusae form polyps sexually, e.g., in Obelia) is called:',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'অবেলিক জাতীয় নিডারিয়ায় অযৌন পলিপ ও যৌন মেদুসা দশার ক্রমান্বয়িক আবর্তনকে মেটাজেনেসিস (Metagenesis) '
               'বলে।',
    'expl_en': 'Those cnidarians which exist in both forms exhibit alternation of generation (Metagenesis), i.e., '
               'polyps produce medusae asexually and medusae form the polyps sexually (e.g., Obelia).',
    'id': 'BIO-AK-019',
    'opts': { 'bn': ['মেটাজেনেসিস (Metagenesis)', 'মেটামরফোসিস বা রূপান্তর', 'একডাইসিস', 'পার্থেনোজেনেসিস'],
              'en': ['Metagenesis', 'Metamorphosis', 'Ecdysis', 'Parthenogenesis']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': "কোন নিডারিয়ান প্রাণীটিকে সাধারণভাবে 'পর্তুগিজ ম্যান-অফ-ওয়ার' (Portuguese man-of-war) বলা হয়?",
    'correct': 0,
    'difficulty': 'Easy',
    'en': "Which cnidarian is commonly called the 'Portuguese man-of-war'?",
    'exam': 'NEET, CUET',
    'expl_bn': 'Physalia-কে সাধারণভাবে পর্তুগিজ ম্যান-অফ-ওয়ার বলা হয়।',
    'expl_en': 'Common names from NCERT: Physalia (Portuguese man-of-war), Adamsia (Sea anemone), Pennatula (Sea-pen), '
               'Gorgonia (Sea-fan), Meandrina (Brain coral).',
    'id': 'BIO-AK-020',
    'opts': { 'bn': ['ফাইসিলিয়া (Physalia)', 'অ্যাডামসিয়া', 'পেন্নাটুলা', 'গর্গোনিয়া'],
              'en': ['Physalia', 'Adamsia', 'Pennatula', 'Gorgonia']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'প্রবাল বা কোরাল (Corals)-এর শক্ত কঙ্কাল মূলত কী দ্বারা গঠিত?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Corals have a skeleton composed of:',
    'exam': 'NEET, CUET',
    'expl_bn': 'কোরাল বা প্রবালের কঙ্কাল প্রধানত ক্যালসিয়াম কার্বনেট (CaCO3) দিয়ে গঠিত।',
    'expl_en': 'Some cnidarians, for example, corals have a stony exoskeleton composed of calcium carbonate (CaCO3).',
    'id': 'BIO-AK-021',
    'opts': { 'bn': ['ক্যালসিয়াম কার্বনেট (CaCO3)', 'সিলিকা', 'কাইটিন', 'স্পঞ্জিন'],
              'en': ['Calcium carbonate (CaCO3)', 'Silica (SiO2)', 'Chitin', 'Spongin']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'টিনোফোরা (Ctenophora) পর্বের প্রাণীরা সাধারণভাবে কী নামে পরিচিত?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Ctenophores are commonly known as:',
    'exam': 'NEET, CUET',
    'expl_bn': 'টিনোফোরা পর্বের প্রাণীদের সাধারণভাবে সি-ওয়ালনাট (sea walnuts) বা চিরুনি জেলি (comb jellies) বলা হয়।',
    'expl_en': 'Ctenophores, commonly known as sea walnuts or comb jellies, are exclusively marine, radially '
               'symmetrical, diploblastic organisms with tissue level of organisation.',
    'id': 'BIO-AK-022',
    'opts': { 'bn': [ 'সি-ওয়ালনাট (Sea walnuts) বা চিরুনি জেলি (Comb jellies)',
                      'স্নান স্পঞ্জ',
                      'ফিতাকৃমি',
                      'হুকওয়ার্ম'],
              'en': [ 'Sea walnuts or Comb jellies',
                      'Sponges or Bath sponges',
                      'Flatworms or Tapeworms',
                      'Roundworms or Hookworms']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'টিনোফোরার দেহে ________টি সিলিয়াযুক্ত বহিস্থ কম্ব প্লেটের সারি থাকে, যা ________ সাহায্য করে।',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The body of ctenophores bears ________ external rows of ciliated comb plates, which help in ________.',
    'exam': 'NEET, CUET',
    'expl_bn': 'টিনোফোরার দেহে আটটি সিলিয়াযুক্ত চিরুনির মতো খাঁজকাটা প্লেট থাকে যা চলনে (locomotion) সহায়তা করে।',
    'expl_en': 'The body bears eight external rows of ciliated comb plates, which help in locomotion.',
    'id': 'BIO-AK-023',
    'opts': { 'bn': ['আটটি (8); চলনে (locomotion)', 'ছয়টি; পরিপাকে', 'দশটি; জননে', 'চারটি; রেচনে'],
              'en': ['Eight; locomotion', 'Six; digestion', 'Ten; reproduction', 'Four; excretion']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'সজীব প্রাণীদেহ থেকে আলো নির্গত হওয়ার যে দৃশ্যমান বৈশিষ্ট্য টিনোফোরাতে বিশেষভাবে লক্ষণীয়, তাকে কী বলে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The property of a living organism to emit light, well-marked in ctenophores, is called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'টিনোফোরা পর্বের প্রধান অন্যতম বৈশিষ্ট্য হলো তাদের দেহ থেকে নিজস্ব আলো নির্গমন বা বায়োলুমিনেসেন্স '
               '(Bioluminescence)।',
    'expl_en': 'Bioluminescence (the property of a living organism to emit light) is well-marked in ctenophores (e.g., '
               'Pleurobrachia and Ctenoplana).',
    'id': 'BIO-AK-024',
    'opts': { 'bn': ['বায়োলুমিনেসেন্স বা জৈব দ্যুতি (Bioluminescence)', 'প্রতিপ্রভা', 'অনুপ্রভা', 'রাসায়নিক দ্যুতি'],
              'en': ['Bioluminescence', 'Fluorescence', 'Phosphorescence', 'Chemiluminescence']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'টিনোফোরা পর্বের জনন সম্পর্কিত কোন বক্তব্যটি সঠিক?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Which of the following statements about reproduction in Ctenophores is CORRECT?',
    'exam': 'NEET, CUET',
    'expl_bn': 'টিনোফোরায় অযৌন জনন একেবারেই অনুপস্থিত; জনন কেবল যৌন উপায়ে ঘটে, বহিঃনিষেক হয় এবং সিডিপ্পিড লার্ভার '
               'মাধ্যমে পরোক্ষ বিকাশ সম্পন্ন হয়।',
    'expl_en': 'Ctenophores are hermaphrodites. Reproduction takes place only by sexual means. Fertilisation is '
               'external with indirect development (cydippid larva).',
    'id': 'BIO-AK-025',
    'opts': { 'bn': [ 'জনন কেবলমাত্র যৌন উপায়ে ঘটে; বহিঃনিষেক ঘটে এবং পরোক্ষ রূপান্তরের মাধ্যমে বিকাশ ঘটে',
                      'মুকুলোদগম দ্বারা অযৌন জনন প্রধান',
                      'নিষেক অভ্যন্তরীণ এবং সরাসরি বিকাশ হয়',
                      'এরা একলিঙ্গ এবং জরায়ুজ'],
              'en': [ 'Reproduction takes place only by sexual means; fertilization is external with indirect '
                      'development',
                      'Asexual reproduction by budding is dominant',
                      'Fertilization is strictly internal with direct development',
                      'They are dioecious with viviparous birth']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': "প্লাটিহেলমিন্থেস পর্বের সদস্যদের সাধারণভাবে 'চ্যাপ্টাকৃমি' (flatworms) বলা হয় কেন?",
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Why are members of Phylum Platyhelminthes commonly called flatworms?',
    'exam': 'NEET, CUET',
    'expl_bn': 'প্লাটিহেলমিন্থেসের দেহটি পৃষ্ঠ ও অঙ্কীয় উভয় দিক থেকেই চ্যাপ্টা ফিতার মতো, তাই এদের চ্যাপ্টাকৃমি '
               '(Flatworms) বলা হয়।',
    'expl_en': 'They have dorso-ventrally flattened body, hence are called flatworms. They are mostly endoparasites '
               'found in animals including human beings.',
    'id': 'BIO-AK-026',
    'opts': { 'bn': [ 'তাদের দেহটি পৃষ্ঠ-অঙ্কীয়ভাবে চ্যাপ্টা (dorso-ventrally flattened)',
                      'তাদের দেহ বৃত্তাকার নলাকার',
                      'বালিতে চলার জন্য চ্যাপ্টা পা থাকে',
                      'তাদের ডিমগুলি চ্যাপ্টা চাকতির মতো'],
              'en': [ 'They have a dorso-ventrally flattened body',
                      'They have a circular cylindrical body',
                      'They have flat feet for crawling on sand',
                      'Their eggs are flattened discs']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'চ্যাপ্টাকৃমিতে (Platyhelminthes) রেচন ও অভিস্রবণ নিয়ন্ত্রণে সাহায্যকারী বিশেষ কোষগুলিকে কী বলে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Specialised excretory and osmoregulatory cells found in flatworms (Platyhelminthes) are called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'প্লাটিহেলমিন্থেসের প্রধান রেচন অঙ্গ হলো শিখা কোষ (Flame cells বা Protonephridia) যা রেচন ও অভিস্রবণ '
               'নিয়ন্ত্রণে অংশ নেয়।',
    'expl_en': 'Specialised cells called flame cells help in osmoregulation and excretion in platyhelminthes.',
    'id': 'BIO-AK-027',
    'opts': { 'bn': [ 'শিখা কোষ বা ফ্লেম সেল (Flame cells / Protonephridia)',
                      'নেফ্রিডিয়া',
                      'ম্যালপিজিয়ান নালিকা',
                      'রেনেট কোষ'],
              'en': ['Flame cells (Protonephridia)', 'Nephridia', 'Malpighian tubules', 'Renette cells']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'ফিতাকৃমির মতো পরজীবী চ্যাপ্টাকৃমিতে পোষকের অন্ত্রপ্রাচীরে আটকে থাকার জন্য কোন বিশেষ অঙ্গ থাকে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Parasitic flatworms like tapeworms possess which special structures for adhering to the host intestinal '
          'lining?',
    'exam': 'NEET, CUET',
    'expl_bn': 'পরজীবী ফিতাকৃমির মাথায় বা স্কোলেক্সে হুক ও চোষক (suckers) থাকে যা দিয়ে এরা পোষকের অন্ত্রের গায়ে '
               'দৃঢ়ভাবে আটকে থাকে।',
    'expl_en': 'Hooks and suckers are present in the parasitic forms (such as Taenia solium) on their scolex to anchor '
               'firmly into host tissue. Some absorb nutrients directly through body surface.',
    'id': 'BIO-AK-028',
    'opts': { 'bn': [ 'স্কোলেক্সের ওপর হুক এবং চোষক বা সাকার (Hooks and suckers)',
                      'কর্ষিকা ও কম্ব প্লেট',
                      'প্যারাপোডিয়া ও সিটা',
                      'রেডুলা ও ম্যান্টল'],
              'en': [ 'Hooks and suckers on the scolex',
                      'Tentacles and comb plates',
                      'Parapodia and setae',
                      'Radula and mantle']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোন মুক্তজীবী চ্যাপ্টাকৃমিতে অপরিসীম পুনরুৎপাদন ক্ষমতা (high regeneration capacity) দেখা যায়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which free-living flatworm possesses high regeneration capacity?',
    'exam': 'NEET, CUET',
    'expl_bn': 'প্ল্যানেরিয়া (Planaria) হলো এমন এক মুক্তজীবী চ্যাপ্টাকৃমি যার দেহে অসাধারণ পুনরুৎপাদন ক্ষমতা বর্তমান।',
    'expl_en': 'Planaria, a freshwater free-living flatworm, possesses high regeneration capacity; even a small '
               'severed fragment can reconstitute an entire organism.',
    'id': 'BIO-AK-029',
    'opts': { 'bn': ['প্ল্যানেরিয়া (Planaria)', 'টিনিয়া বা ফিতাকৃমি', 'ফ্যাসিওলা বা যকৃৎ কৃমি', 'সিস্টোসোমা'],
              'en': ['Planaria', 'Taenia (Tapeworm)', 'Fasciola (Liver fluke)', 'Schistosoma (Blood fluke)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'অ্যাসকেলমিন্থেস (Aschelminthes) পর্বের প্রাণীদের দেহের প্রস্থচ্ছেদ বৃত্তাকার হওয়ায় এদের কী নামে ডাকা হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The body of Aschelminthes is circular in cross-section, hence the name:',
    'exam': 'NEET, CUET',
    'expl_bn': 'দেহের প্রস্থচ্ছেদ সম্পূর্ণ বৃত্তাকার হওয়ায় অ্যাসকেলমিন্থেসদের গোলকৃমি বা Roundworms বলা হয়।',
    'expl_en': 'The body of the aschelminthes is circular in cross-section, hence, the name roundworms.',
    'id': 'BIO-AK-030',
    'opts': { 'bn': ['গোলকৃমি (Roundworms)', 'চ্যাপ্টাকৃমি', 'খণ্ডায়িত কৃমি', 'পিনকৃমি'],
              'en': ['Roundworms', 'Flatworms', 'Segmented worms', 'Pinworms only']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'গোলকৃমির (Aschelminthes) সম্পূর্ণ পৌষ্টিকনালীর অন্যতম প্রধান বৈশিষ্ট্য হলো এতে কোন সুগঠিত অঙ্গ থাকে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In roundworms (Aschelminthes), the alimentary canal is complete with a well-developed:',
    'exam': 'NEET, CUET',
    'expl_bn': 'গোলকৃমির পৌষ্টিকনালী সম্পূর্ণ এবং এদের একটি সুগঠিত ও শক্তিশালী পেশিবহুল গলবিল (muscular pharynx) থাকে '
               'যা খাদ্য চোষণে সাহায্য করে।',
    'expl_en': 'Alimentary canal is complete in Aschelminthes with a well-developed muscular pharynx.',
    'id': 'BIO-AK-031',
    'opts': { 'bn': [ 'পেশিবহুল গলবিল বা ফ্যারিংস (Muscular pharynx)',
                      'দাঁতযুক্ত রেডুলা',
                      'ক্রপ এবং গিজার্ড',
                      'টিফ্লোসোল'],
              'en': ['Muscular pharynx', 'Teeth-bearing radula', 'Crop and gizzard', 'Typhlosole']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'অ্যাসকারিস বা সাধারণ গোলকৃমিতে যৌন দ্বিরূপতা কীভাবে সুস্পষ্টভাবে প্রকাশিত হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Sexual dimorphism in Ascaris lumbricoides is distinctly characterized by:',
    'exam': 'NEET, CUET',
    'expl_bn': 'অ্যাসকারিসে স্ত্রী কৃমি পুরুষের চেয়ে আকারে দীর্ঘ হয়। পুরুষ কৃমির পশ্চাৎভাগ বাঁকানো থাকে এবং তাতে '
               'সঙ্গমে সাহায্যকারী পিনিয়াল স্পিকিউল থাকে।',
    'expl_en': 'Sexes are separate (dioecious) in Ascaris. Often females are longer than males. Males are shorter and '
               'possess a curved posterior tail bearing copulatory pineal spicules.',
    'id': 'BIO-AK-032',
    'opts': { 'bn': [ 'স্ত্রী কৃমিরা পুরুষদের তুলনায় লম্বা হয় এবং পুরুষদের লেজের দিকটি বাঁকানো ও পিনিয়াল '
                      'স্পিকিউলযুক্ত থাকে',
                      'পুরুষরা স্ত্রীদের তুলনায় অনেক লম্বা হয়',
                      'পুরুষ ও স্ত্রী বাহ্যিকভাবে সম্পূর্ণ সদৃশ',
                      'স্ত্রীদের ডানা থাকে কিন্তু পুরুষরা ডানাহীন'],
              'en': [ 'Females are longer than males, and males have a curved posterior end with pineal spicules',
                      'Males are longer than females, and females have curved tail',
                      'Males and females are completely identical in external morphology',
                      'Females have wings while males are apterous']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'লসিকা নালীর দীর্ঘস্থায়ী প্রদাহজনিত গোদ বা ফাইলেরিয়াসিস রোগ সৃষ্টিকারী কৃমি উচেরেরিয়া (Wuchereria '
          'bancrofti) কোন পর্বভুক্ত?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Wuchereria bancrofti, the filarial worm that causes chronic inflammation of lymphatic vessels '
          '(Elephantiasis), belongs to:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ফাইলেরিয়া কৃমি উচেরেরিয়া (Wuchereria) হলো অ্যাসকেলমিন্থেস পর্বভুক্ত নেমাটোড।',
    'expl_en': 'Wuchereria (filaria worm) is a nematode belonging to Phylum Aschelminthes.',
    'id': 'BIO-AK-033',
    'opts': { 'bn': ['অ্যাসকেলমিন্থেস বা গোলকৃমি (Aschelminthes)', 'প্লাটিহেলমিন্থেস', 'অ্যানেলিডা', 'আর্থ্রোপোডা'],
              'en': ['Aschelminthes', 'Platyhelminthes', 'Annelida', 'Arthropoda']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'অ্যানকাইলোস্টোমা (Ancylostoma duodenale)-কে সাধারণ ভাষায় কী কৃমি বলা হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Ancylostoma duodenale is commonly known as the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'Ancylostoma-কে সাধারণ ভাষায় হুকওয়ার্ম (Hookworm) বলা হয়।',
    'expl_en': 'Examples of Aschelminthes from NCERT: Ascaris (Roundworm), Wuchereria (Filaria worm), Ancylostoma '
               '(Hookworm).',
    'id': 'BIO-AK-034',
    'opts': { 'bn': ['হুককৃমি বা হুকওয়ার্ম (Hookworm)', 'গোলকৃমি', 'ফিতাকৃমি', 'পিনকৃমি'],
              'en': ['Hookworm', 'Roundworm', 'Tapeworm', 'Pinworm']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'গোলকৃমিতে দেহগহ্বর থেকে বর্জ্য পদার্থ বাইরে নিষ্কাশনের জন্য একটি রেচন নালী কার মাধ্যমে বাইরে উন্মুক্ত হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In roundworms, an excretory tube removes body wastes from the body cavity through the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'গোলকৃমির একটি H-আকৃতির রেচন নালীতন্ত্র রেচন রন্ধ্র (excretory pore)-র মাধ্যমে বর্জ্য পদার্থ দেহ থেকে '
               'বাইরে বের করে দেয়।',
    'expl_en': 'An excretory tube removes body wastes from the body cavity through the excretory pore located on the '
               'mid-ventral line behind the mouth.',
    'id': 'BIO-AK-035',
    'opts': { 'bn': ['রেচন রন্ধ্র বা এক্সক্রিটরি পোর (Excretory pore)', 'শিখা কোষ নালী', 'অসকুলাম', 'হাইপোস্টোম'],
              'en': ['Excretory pore', 'Flame cell duct', 'Osculum', 'Hypostome']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'অ্যানেলিডা (ল্যাটিন annulus: ছোট আংটি) নামটি পর্বটির কোন স্বতন্ত্র বৈশিষ্ট্যের কারণে রাখা হয়েছে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The phylum name Annelida (Latin, annulus: little ring) refers to which distinctive characteristic?',
    'exam': 'NEET, CUET',
    'expl_bn': 'অ্যানেলিডার দেহ সুস্পষ্টভাবে অসংখ্য বলয়ের মতো খণ্ডকে (metameres) বিভক্ত থাকে, তাই একে অ্যানেলিডা বা '
               'অঙ্গুরীমাল বলা হয়।',
    'expl_en': 'Their body surface is distinctly marked out into segments or metameres and, hence, the phylum name '
               'Annelida.',
    'id': 'BIO-AK-036',
    'opts': { 'bn': [ 'দেহের বহির্ভাগ সুস্পষ্টভাবে ছোট ছোট আংটির মতো খণ্ডক বা মেটামিয়ারে বিভক্ত',
                      'আংটির মতো ক্যালসিয়াম খোলকের উপস্থিতি',
                      'হাইপোস্টোমকে ঘিরে আংটির মতো কর্ষিকার বিন্যাস',
                      'জলের মধ্যে বৃত্তাকারে সাঁতার কাটার অভ্যাস'],
              'en': [ 'Body surface distinctly marked out into segments or metameres',
                      'Presence of ring-like calcareous shell',
                      'Ring-shaped tentacles around the hypostome',
                      'Circular swimming motion in water']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নেরিসের (Nereis) মতো জলজ অ্যানেলিডায় সাঁতার কাটার জন্য যে পার্শ্বীয় উপাঙ্গ থাকে তাকে কী বলে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Aquatic annelids like Nereis possess lateral appendages which help in swimming, known as:',
    'exam': 'NEET, CUET',
    'expl_bn': 'নেরিসের দেহের দুপাশে চ্যাপ্টা মাংসল উপাঙ্গ থাকে যাদের প্যারাপোডিয়া (Parapodia) বলে; এগুলি সাঁতারে '
               'সহায়তা করে।',
    'expl_en': 'Aquatic annelids like Nereis possess lateral unjointed flattened appendages called parapodia, which '
               'help in swimming.',
    'id': 'BIO-AK-037',
    'opts': { 'bn': ['প্যারাপোডিয়া (Parapodia)', 'কেবলমাত্র সিটা', 'কর্ষিকা', 'রেডুলা'],
              'en': ['Parapodia', 'Setae only', 'Tentacles', 'Radula']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'অ্যানেলিডার রেচন অঙ্গ যা অভিস্রবণ নিয়ন্ত্রণেও অংশ নেয় তাকে কী বলে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The excretory organs of Annelids that also perform osmoregulation are called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'অ্যানেলিডার কুণ্ডলীকৃত রেচন অঙ্গকে নেফ্রিডিয়া (Nephridia) বলে যা বর্জ্য নিষ্কাশন ও জলের ভারসাম্য '
               'রক্ষা করে।',
    'expl_en': 'Nephridia (sing. nephridium) help in osmoregulation and excretion in annelids.',
    'id': 'BIO-AK-038',
    'opts': { 'bn': ['নেফ্রিডিয়া (Nephridia)', 'শিখা কোষ', 'ম্যালপিজিয়ান নালিকা', 'প্রোবোসিস গ্রন্থি'],
              'en': ['Nephridia', 'Flame cells', 'Malpighian tubules', 'Proboscis gland']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোন অ্যানেলিডটি একলিঙ্গ (dioecious), যেখানে কেঁচো ও জোঁক হলো উভলিঙ্গ (monoecious)?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Which of the following annelids is dioecious (unisexual), whereas earthworms and leeches are monoecious '
          '(hermaphrodites)?',
    'exam': 'NEET, CUET',
    'expl_bn': 'নেরিস (Nereis) হলো একলিঙ্গ প্রাণী (পুরুষ ও স্ত্রী পৃথক), কিন্তু কেঁচো ও জোঁক উভয়লিঙ্গ।',
    'expl_en': 'Nereis, an aquatic form, is dioecious, but earthworms and leeches are monoecious.',
    'id': 'BIO-AK-039',
    'opts': { 'bn': ['নেরিস (Nereis)', 'ফেরেটিমা বা কেঁচো', 'হিরুডিনারিয়া বা জোঁক', 'ল্যামব্রিকাস'],
              'en': ['Nereis', 'Pheretima (Earthworm)', 'Hirudinaria (Leech)', 'Lumbricus']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'প্রাণীজগতের সর্ববৃহৎ পর্ব কোনটি যাতে পতঙ্গ অন্তর্ভুক্ত এবং যা পৃথিবীর মোট নামাঙ্কিত প্রাণীর দুই-তৃতীয়াংশের '
          'বেশি অংশ জুড়ে রয়েছে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which is the LARGEST phylum of Animalia which includes insects and accounts for over two-thirds of all '
          'named species on earth?',
    'exam': 'NEET, CUET',
    'expl_bn': 'আর্থ্রোপোডা বা সন্ধিপদ পর্ব হলো প্রাণীজগতের বৃহত্তম পর্ব, যেখানে দুই-তৃতীয়াংশের বেশি প্রাণী প্রজাতি '
               'অবস্থান করে।',
    'expl_en': 'This is the largest phylum of Animalia which includes insects. Over two-thirds of all named species on '
               'earth are arthropods.',
    'id': 'BIO-AK-040',
    'opts': { 'bn': ['আর্থ্রোপোডা বা সন্ধিপদ (Arthropoda)', 'মোলাস্কা', 'কর্ডাটা', 'প্রোটোজোয়া'],
              'en': ['Arthropoda', 'Mollusca', 'Chordata', 'Protozoa']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'আর্থ্রোপোডার সমগ্র দেহ কী দ্বারা গঠিত একটি শক্ত প্রতিরক্ষামূলক বহিঃকঙ্কাল দ্বারা আবৃত থাকে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The body of arthropods is covered by a tough, protective exoskeleton made of:',
    'exam': 'NEET, CUET',
    'expl_bn': 'আর্থ্রোপোডার দেহ কাইটিন নির্মিত শক্ত বহিঃকঙ্কাল দ্বারা আবৃত থাকে যা নির্দিষ্ট সময় পরপর মোচন (ecdysis) '
               'ঘটে।',
    'expl_en': 'The body of arthropods is covered by a chitinous exoskeleton. It prevents water loss and protects '
               'internal tissues.',
    'id': 'BIO-AK-041',
    'opts': { 'bn': ['কাইটিন বা কাইটিনাস বহিঃকঙ্কাল (Chitin)', 'ক্যালসিয়াম কার্বনেট', 'সিলিকা', 'স্পঞ্জিন'],
              'en': ['Chitin (a polymer of N-acetylglucosamine)', 'Calcium carbonate', 'Silica', 'Spongin']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'আর্থ্রোপোডার বিভিন্ন শ্রেণিতে শ্বাসঅঙ্গ বিভিন্ন প্রকৃতির হয়। নিচের কোন জোড়াগুলি সঠিকভাবে মিলেছে?<br>১. '
          'বুক লাংস — বৃশ্চিক ও মাকড়সা<br>২. বুক গিলস — রাজ কাঁকড়া (Limulus)<br>৩. ট্র্যাকিয়াল তন্ত্র — পতঙ্গ '
          '(আরশোলা)',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The respiratory organs in arthropods vary widely across classes. Match the respiratory organs with their '
          'representative arthropods:<br>1. Book lungs — Scorpions and Spiders<br>2. Book gills — King crab '
          '(Limulus)<br>3. Tracheal system — Insects (Cockroach)<br>Which of the above pairings are correct?',
    'exam': 'NEET, CUET',
    'expl_bn': 'বুক লাংস (মাকড়সা/বৃশ্চিক), বুক গিলস (লিমুলাস) এবং ট্র্যাকিয়াল নালী (পতঙ্গ)—সবকটি তথ্যই NCERT অনুসারে '
               'সঠিক।',
    'expl_en': 'All three pairs are accurate NCERT examples: Respiratory organs are gills, book gills (Limulus), book '
               'lungs (scorpions/spiders) or tracheal system (insects).',
    'id': 'BIO-AK-042',
    'opts': { 'bn': ['১, ২ এবং ৩ (সবকটিই সঠিক)', 'কেবল ১ ও ৩', 'কেবল ২ ও ৩', 'কেবল ১ ও ২'],
              'en': ['1, 2, and 3 (All are correct)', '1 and 3 only', '2 and 3 only', '1 and 2 only']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'ভারসাম্য রক্ষাকারী সংবেদী অঙ্গ স্ট্যাটোসিস্ট (Statocysts) কোন পর্বে দেখা যায়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Balancing organs or statocysts are present in which phylum?',
    'exam': 'NEET, CUET',
    'expl_bn': 'আর্থ্রোপোডার সংবেদী অঙ্গের মধ্যে অ্যান্টেনা, সরল ও পুঞ্জাক্ষি এবং ভারসাম্য রক্ষাকারী স্ট্যাটোসিস্ট '
               'উপস্থিত থাকে।',
    'expl_en': 'Sensory organs like antennae, eyes (compound and simple), statocysts or balancing organs are present '
               'in Arthropoda.',
    'id': 'BIO-AK-043',
    'opts': { 'bn': ['আর্থ্রোপোডা (যেমন চিংড়িতে)', 'প্লাটিহেলমিন্থেস', 'অ্যাসকেলমিন্থেস', 'পরিফেরা'],
              'en': ['Arthropoda (e.g., in prawns)', 'Platyhelminthes', 'Aschelminthes', 'Porifera']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'অধিকাংশ স্থলজ সন্ধিপদ বা পতঙ্গের রেচন কোন অঙ্গের মাধ্যমে সম্পন্ন হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Excretion in majority of terrestrial arthropods (like insects) takes place through:',
    'exam': 'NEET, CUET',
    'expl_bn': 'পতঙ্গ ও স্থলজ সন্ধিপদদের প্রধান রেচন অঙ্গ হলো ম্যালপিজিয়ান নালিকা (Malpighian tubules)।',
    'expl_en': 'Excretion in insects and many arthropods takes place through Malpighian tubules, converting '
               'nitrogenous waste into uric acid.',
    'id': 'BIO-AK-044',
    'opts': { 'bn': ['ম্যালপিজিয়ান নালিকা (Malpighian tubules)', 'সবুজ গ্রন্থি', 'শিখা কোষ', 'নেফ্রিডিয়া'],
              'en': ['Malpighian tubules', 'Green glands (Antennal glands in prawns)', 'Flame cells', 'Nephridia']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': "নিচের কোনটি সন্ধিপদ বা আর্থ্রোপোডার একটি বিখ্যাত 'জীবন্ত জীবাশ্ম' (Living fossil)?",
    'correct': 0,
    'difficulty': 'Easy',
    'en': "Which of the following is a 'living fossil' arthropod?",
    'exam': 'NEET, CUET',
    'expl_bn': 'লিমুলাস (Limulus বা King crab) হলো আর্থ্রোপোডার অন্তর্ভুক্ত একটি জীবন্ত জীবাশ্ম।',
    'expl_en': 'Limulus (King crab) is an ancient marine chelicerate that has remained virtually unchanged for over '
               '400 million years, hence termed a living fossil.',
    'id': 'BIO-AK-045',
    'opts': { 'bn': [ 'লিমুলাস বা রাজ কাঁকড়া (Limulus / King crab)',
                      'পঙ্গপাল বা লোকাস্টা',
                      'রেশম মথ বা বম্বিক্স',
                      'লাক্ষা কীট বা ল্যাসিফার'],
              'en': ['Limulus (King crab)', 'Locusta (Locust)', 'Bombyx (Silkworm)', 'Laccifer (Lac insect)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'আর্থ্রোপোডার অন্তর্গত কোন ক্ষতিকারক পতঙ্গটি ঝাঁক বেঁধে শস্য ধ্বংসকারী পেস্ট (gregarious pest) হিসেবে '
          'পরিচিত?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following is a gregarious, destructive pest belonging to Arthropoda?',
    'exam': 'NEET, CUET',
    'expl_bn': 'লোকাস্টা (Locusta) বা পঙ্গপাল হলো একটি মারাত্মক ঝাঁকবদ্ধ ক্ষতিকর শস্যনাশক কীট।',
    'expl_en': 'Locusta (Locust) is a gregarious pest that migrates in billions, decimating agricultural fields.',
    'id': 'BIO-AK-046',
    'opts': { 'bn': ['লোকাস্টা বা পঙ্গপাল (Locusta)', 'মৌমাছি', 'এডিস মশা', 'কিউলেক্স'],
              'en': ['Locusta (Locust)', 'Apis (Honey bee)', 'Aedes (Mosquito)', 'Culex']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'প্রাণীজগতের দ্বিতীয় বৃহত্তম (Second largest) পর্ব কোনটি?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which is the SECOND LARGEST animal phylum?',
    'exam': 'NEET, CUET',
    'expl_bn': 'আর্থ্রোপোডার পরেই প্রাণীজগতের দ্বিতীয় বৃহত্তম পর্ব হলো মোলাস্কা (Mollusca)।',
    'expl_en': 'Mollusca is the second largest animal phylum after Arthropoda.',
    'id': 'BIO-AK-047',
    'opts': { 'bn': ['মোলাস্কা বা কম্বোজ (Mollusca)', 'আর্থ্রোপোডা', 'অ্যানেলিডা', 'একাইনোডার্মাটা'],
              'en': ['Mollusca', 'Arthropoda', 'Annelida', 'Echinodermata']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'মোলাস্কার অখণ্ডায়িত নরম দেহটি সাধারণত কোন তিনটি প্রধান অঞ্চলে বিভক্ত থাকে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The unsegmented soft body of a mollusc is typically divided into which three regions?',
    'exam': 'NEET, CUET',
    'expl_bn': 'মোলাস্কার দেহটি সুস্পষ্ট মস্তক, অঙ্কীয় পেশিবহুল পদ এবং পৃষ্ঠীয় ভিসেরাল কুঁজে (visceral hump) বিভক্ত '
               'থাকে।',
    'expl_en': 'Body of molluscs is covered by a calcareous shell and is unsegmented with a distinct head, muscular '
               'foot and visceral hump.',
    'id': 'BIO-AK-048',
    'opts': { 'bn': [ 'মস্তক (Head), পেশিবহুল পদ (Muscular foot) এবং ভিসেরাল কুঁজ (Visceral hump)',
                      'মস্তক, বক্ষ এবং উদর',
                      'প্রোবোসিস, কলার এবং ধড়',
                      'শিরোবক্ষ, উদর এবং টেলসন'],
              'en': [ 'Head, muscular foot, and visceral hump',
                      'Head, thorax, and abdomen',
                      'Proboscis, collar, and trunk',
                      'Cephalothorax, abdomen, and telson']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'মোলাস্কায় ভিসেরাল কুঁজের ওপর ত্বক একটি নরম আস্তরণ বা ম্যান্টল গঠন করে। কুঁজ ও ম্যান্টলের মধ্যবর্তী স্থানকে '
          '________ বলে, যাতে পালকের মতো ________ অবস্থিত।',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In molluscs, a soft and spongy layer of skin forms a mantle over the visceral hump. The space between the '
          'hump and the mantle is called the ________, in which ________ are present.',
    'exam': 'NEET, CUET',
    'expl_bn': 'ভিসেরাল কুঁজ ও ম্যান্টলের মধ্যবর্তী ম্যান্টল গহ্বরে পালকাকৃতি ফুলকা বা টেনিডিয়া থাকে যা শ্বাসকার্য ও '
               'রেচনে অংশ নেয়।',
    'expl_en': 'The space between the hump and the mantle is called the mantle cavity in which feather-like gills are '
               'present. They have respiratory and excretory functions.',
    'id': 'BIO-AK-049',
    'opts': { 'bn': [ 'ম্যান্টল গহ্বর (Mantle cavity); পালকসদৃশ ফুলকা বা টেনিডিয়া (ctenidia)',
                      'সিউডোসিলোম; শিখা কোষ',
                      'হিমোসিল; সবুজ গ্রন্থি',
                      'স্পঞ্জোসিল; কোয়ানোসাইট'],
              'en': [ 'Mantle cavity; feather-like gills (ctenidia)',
                      'Pseudocoelom; flame cells',
                      'Haemocoel; green glands',
                      'Spongocoel; choanocytes']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'মোলাস্কার মুখবিবরে অবস্থিত খাদ্য চর্বনকারী করাত বা রেতির মতো অঙ্গকে কী বলে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The file-like rasping organ present in the mouth of molluscs used for feeding is called the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'মোলাস্কার মুখে কাইটিনের সূক্ষ্ম দাঁতযুক্ত রেতির মতো খাদ্য চূর্ণকারী অঙ্গ থাকে যাকে রেডুলা (Radula) '
               'বলে।',
    'expl_en': 'The mouth contains a file-like rasping organ for feeding, called radula, bearing transverse rows of '
               'chitinous teeth.',
    'id': 'BIO-AK-050',
    'opts': { 'bn': ['রেডুলা (Radula)', 'প্যারাপোডিয়া', 'স্ট্যাটোসিস্ট', 'ট্রোকোফোর'],
              'en': ['Radula', 'Parapodia', 'Statocyst', 'Trochophore']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': "নিচের কোন মোলাস্কায় কোনো খোলক থাকে না এবং একে সাধারণভাবে 'ডেভিল ফিশ' (Devil fish) বলা হয়?",
    'correct': 0,
    'difficulty': 'Easy',
    'en': "Which of the following molluscs completely lacks a shell and is commonly called the 'Devil fish'?",
    'exam': 'NEET, CUET',
    'expl_bn': 'অক্টোপাসকে সাধারণ ভাষায় ডেভিল ফিশ বলা হয় এবং এতে কোনো খোলক থাকে না।',
    'expl_en': 'Octopus completely lacks an external or internal shell and is commonly called the devil fish.',
    'id': 'BIO-AK-051',
    'opts': { 'bn': ['অক্টোপাস (Octopus)', 'সেপিয়া বা কাটলফিশ', 'ললিগো বা স্কুইড', 'অ্যাপ্লাইসিয়া বা সি-হেয়ার'],
              'en': ['Octopus', 'Sepia (Cuttlefish)', 'Loligo (Squid)', 'Aplysia (Sea hare)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'পিঙ্কটাডা (Pinctada) বাণিজ্যিকভাবে কী উৎপাদনের জন্য চাষ করা হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Pinctada is commercially cultivated for the production of:',
    'exam': 'NEET, CUET',
    'expl_bn': 'পিঙ্কটাডা (Pinctada) হলো মুক্তা ঝিনুক যার ম্যান্টল থেকে মূল্যবান মুক্তা তৈরি হয়।',
    'expl_en': 'Pinctada is the pearl oyster from which commercial natural and cultured pearls are harvested.',
    'id': 'BIO-AK-052',
    'opts': { 'bn': ['প্রাকৃতিক মুক্তা (Pearl oyster)', 'প্রাকৃতিক রেশম', 'গালা ও মোম', 'আয়োডিন'],
              'en': ['Natural Pearls (Pearl oyster)', 'Natural Silk', 'Shellac and wax', 'Iodine crystals']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'একাইনোডার্মাটা (Echinodermata) পর্বের প্রাণীদের নামটির উৎপত্তি কিসের ওপর ভিত্তি করে হয়েছে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Echinoderms (Phylum Echinodermata) are so named because of their:',
    'exam': 'NEET, CUET',
    'expl_bn': 'এদের দেহে চুন নির্মিত কণ্টকময় পাত বা অস্থির অন্তকঙ্কাল থাকে, তাই এদের একাইনোডার্মাটা বা কণ্টকত্কী '
               'প্রাণী বলে।',
    'expl_en': 'These animals have an endoskeleton of calcareous ossicles and, hence, the name Echinodermata (spiny '
               'bodied).',
    'id': 'BIO-AK-053',
    'opts': { 'bn': [ 'কণ্টকযুক্ত ত্বক বা স্পাইনি স্কিন (ক্যালসিয়াম নির্মিত অস্থির অন্তকঙ্কাল)',
                      'মুখের ভেতর একাইনয়েড দাঁত',
                      'বক্ষের ওপর কাঁটাযুক্ত ডানা',
                      'কাঁটাযুক্ত অনাবৃত খোলক'],
              'en': [ 'Spiny skin (endoskeleton of calcareous ossicles)',
                      'Echinoid teeth in buccal cavity',
                      'Spiny wings on thorax',
                      'Naked shell with spikes']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'দেহের প্রতিসাম্যের ক্ষেত্রে একাইনোডার্মাটা পর্বের অনন্য বিকাশমূলক বৈশিষ্ট্যটি কী?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'A unique developmental hallmark of Phylum Echinodermata regarding body symmetry is that:',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'একাইনোডার্মাটার লার্ভা দ্বিপার্শ্বীয় প্রতিসম হলেও পূর্ণাঙ্গ দশায় পঞ্চ-অরীয় প্রতিসাম্য দেখা যায়। '
               'এটি একটি অত্যন্ত গুরুত্বপূর্ণ NEET প্রশ্ন।',
    'expl_en': 'The adult echinoderms are radially symmetrical (pentamerous radial) but larvae are bilaterally '
               'symmetrical. This proves their evolutionary descent from bilateral triploblastic ancestors.',
    'id': 'BIO-AK-054',
    'opts': { 'bn': [ 'পূর্ণাঙ্গ প্রাণীরা অরীয় প্রতিসম (radial), কিন্তু এদের মুক্ত সাঁতারু লার্ভাগুলি দ্বিপার্শ্বীয় '
                      'প্রতিসম (bilateral)',
                      'পূর্ণাঙ্গরা দ্বিপার্শ্বীয় প্রতিসম, কিন্তু লার্ভা অরীয় প্রতিসম',
                      'উভয় দশাই সম্পূর্ণ অপ্রতিসম',
                      'উভয় দশাই দ্বিপার্শ্বীয় প্রতিসম'],
              'en': [ 'Adults are radially symmetrical, but free-swimming larvae are bilaterally symmetrical',
                      'Adults are bilaterally symmetrical, but larvae are radially symmetrical',
                      'Both adults and larvae are strictly asymmetrical',
                      'Both adults and larvae have bilateral symmetry']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'একাইনোডার্মাটার সর্বাধিক স্বতন্ত্র ও শনাক্তকারী বৈশিষ্ট্য হলো এদের দেহে কোন তন্ত্রের উপস্থিতি?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The most distinctive, signature feature of echinoderms is the presence of a:',
    'exam': 'NEET, CUET',
    'expl_bn': 'একাইনোডার্মাটার সবচেয়ে অনন্য বৈশিষ্ট্য হলো জল সংবহন তন্ত্র (Water vascular system) যা চলন, খাদ্য '
               'গ্রহণ ও শ্বসনে সাহায্য করে। (স্পঞ্জের ক্যানাল সিস্টেমের সাথে গুলিয়ে ফেলা যাবে না)।',
    'expl_en': 'The most distinctive feature of echinoderms is the presence of water vascular system (ambulacral '
               'system) which helps in locomotion, capture and transport of food and respiration. (Do not confuse with '
               "Porifera's canal system!)",
    'id': 'BIO-AK-055',
    'opts': { 'bn': [ 'নালিপদযুক্ত জলসংবহন তন্ত্র বা অ্যাম্বুল্যাক্রাল তন্ত্র (Water vascular system)',
                      'কোয়ানোসাইটযুক্ত নালী তন্ত্র',
                      'হিমোগ্লোবিনযুক্ত বদ্ধ রক্ত সংবহন',
                      'ম্যালপিজিয়ান নালিকাযুক্ত হিমোসিল'],
              'en': [ 'Water vascular system (Ambulacral system) with tube feet',
                      'Water canal system lined with choanocytes',
                      'Closed circulatory system with hemoglobin',
                      'Open haemocoel with Malpighian tubules']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'একাইনোডার্মাটা পর্বের প্রাণীদের দেহে কোন প্রধান শারীরবৃত্তীয় তন্ত্রটি সম্পূর্ণ অনুপস্থিত থাকে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which major physiological system is completely ABSENT in Phylum Echinodermata?',
    'exam': 'NEET, CUET',
    'expl_bn': 'একাইনোডার্মাটায় কোনো নির্দিষ্ট রেচনতন্ত্র থাকে না; নালিপদ ও ত্বকের ব্র্যাঙ্কির মাধ্যমে ব্যাপন '
               'পদ্ধতিতে বর্জ্য নিষ্কাশিত হয়।',
    'expl_en': 'An excretory system is absent in echinoderms; nitrogenous wastes (ammonia) diffuse out directly across '
               'the thin walls of tube feet and dermal branchiae/papulae.',
    'id': 'BIO-AK-056',
    'opts': { 'bn': [ 'রেচন তন্ত্র বা এক্সক্রিটরি সিস্টেম (Excretory system)',
                      'পৌষ্টিকতন্ত্র',
                      'জননতন্ত্র',
                      'জলসংবহন তন্ত্র'],
              'en': ['Excretory system', 'Digestive system', 'Reproductive system', 'Water vascular system']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'একাইনোডার্মাটায় মুখছিদ্রটি দেহের ________ দিকে এবং পায়ুছিদ্রটি দেহের ________ দিকে অবস্থিত।',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In echinoderms, the mouth is located on the ________ side and the anus on the ________ side.',
    'exam': 'NEET, CUET',
    'expl_bn': 'একাইনোডার্মাটায় মুখ থাকে দেহের নিচের দিকে (অঙ্কীয় তল) এবং পায়ু থাকে উপরের দিকে (পৃষ্ঠীয় তল)।',
    'expl_en': 'Mouth is on the lower (ventral/oral) side and anus on the upper (dorsal/aboral) side in echinoderms.',
    'id': 'BIO-AK-057',
    'opts': { 'bn': [ 'নিচের (অঙ্কীয় বা ventral) দিকে; উপরের (পৃষ্ঠীয় বা dorsal) দিকে',
                      'উপরের দিকে; নিচের দিকে',
                      'অগ্রপ্রান্তে; পশ্চাৎপ্রান্তে',
                      'পার্শ্বদেশে; কেন্দ্রে'],
              'en': [ 'Lower (ventral) side; upper (dorsal) side',
                      'Upper (dorsal); lower (ventral)',
                      'Anterior tip; posterior tip',
                      'Lateral; medial']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': "নিচের কোন একাইনোডার্মটিকে সাধারণভাবে 'সি লিলি' (Sea lily) বলা হয়?",
    'correct': 0,
    'difficulty': 'Easy',
    'en': "Which of the following is commonly known as 'Sea lily'?",
    'exam': 'NEET, CUET',
    'expl_bn': 'Antedon-কে সি লিলি (Sea lily) বলা হয়।',
    'expl_en': 'Examples of Echinodermata from NCERT: Asterias (Star fish), Echinus (Sea urchin), Antedon (Sea lily), '
               'Cucumaria (Sea cucumber), Ophiura (Brittle star).',
    'id': 'BIO-AK-058',
    'opts': { 'bn': ['অ্যান্টিডন (Antedon)', 'অ্যাস্টেরিয়াস', 'একাইনাস', 'কুকুমারিয়া'],
              'en': ['Antedon', 'Asterias (Star fish)', 'Echinus (Sea urchin)', 'Cucumaria (Sea cucumber)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'হெமிকর্ডাটাকে পূর্বে কর্ডাটার উপপর্ব মনে করা হতো। বর্তমানে এদের নন-কর্ডাটার পৃথক পর্ব হিসেবে গণ্য করা হয় '
          'কারণ এদের কলার অঞ্চলের যে গঠনকে নোটোকর্ড ভাবা হয়েছিল তা আসলে কী?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Hemichordates were earlier considered as a sub-phylum under Chordata. But now they are placed as a separate '
          'phylum under Non-Chordata because the structure in the collar region previously thought to be a notochord '
          'is actually a:',
    'exam': 'NEET, CUET',
    'expl_bn': 'হெமிকর্ডাটার কলার অঞ্চলে স্টোমোকর্ড (stomochord) নামক গঠন থাকে যা প্রকৃত মেসোডার্মাল নোটোকর্ড নয়, তাই '
               'এদের নন-কর্ডাটায় স্থান দেওয়া হয়েছে।',
    'expl_en': 'Hemichordates have a rudimentary structure in the collar region called stomochord, a structure similar '
               'to notochord in location, but endodermal and hollow (a buccal diverticulum).',
    'id': 'BIO-AK-059',
    'opts': { 'bn': [ 'স্টোমোকর্ড (Stomochord - গলবিলের প্রাচীর থেকে উৎপন্ন উপবৃদ্ধি)',
                      'প্রকৃত মেসোডার্মাল নোটোকর্ড',
                      'সুষুম্নাকাণ্ড',
                      'অঙ্কীয় স্নায়ুরজ্জু'],
              'en': [ 'Stomochord (a hollow outgrowth of the gut roof)',
                      'True mesodermal notochord',
                      'Spinal cord',
                      'Ventral nerve cord']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'একটি হெமிকর্ডাটার (যেমন Balanoglossus) নলাকার দেহটি কোন তিনটি অংশে বিভক্ত?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The cylindrical body of a hemichordate (like Balanoglossus) is composed of:',
    'exam': 'NEET, CUET',
    'expl_bn': 'হெமிকর্ডাটার দেহ তিনটি অংশে বিভক্ত: অগ্রস্থ প্রোবোসিস, মধ্যবর্তী কলার এবং দীর্ঘ ধড় বা ট্রাঙ্ক।',
    'expl_en': 'The body of hemichordates is cylindrical and is composed of an anterior proboscis, a collar and a long '
               'trunk.',
    'id': 'BIO-AK-060',
    'opts': { 'bn': [ 'অগ্রস্থ প্রোবোসিস (Proboscis), একটি কলার (Collar) এবং একটি দীর্ঘ ধড় (Trunk)',
                      'মস্তক, বক্ষ এবং উদর',
                      'মস্তক, পদ এবং কুঁজ',
                      'হোল্ডফাস্ট, স্ট্রাইপ এবং ফ্রন্ড'],
              'en': [ 'Anterior proboscis, a collar, and a long trunk',
                      'Head, thorax, and abdomen',
                      'Head, muscular foot, and visceral hump',
                      'Holdfast, stipe, and frond']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'হெமிকর্ডাটা পর্বের প্রধান রেচন অঙ্গ কোনটি?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The excretory organ in Hemichordata is the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'হெமிকর্ডাটার প্রধান রেচন অঙ্গ হলো প্রোবোসিস অঞ্চলে অবস্থিত প্রোবোসিস গ্রন্থি (Proboscis gland)।',
    'expl_en': 'Excretory organ is proboscis gland located in the proboscis of hemichordates.',
    'id': 'BIO-AK-061',
    'opts': { 'bn': ['প্রোবোসিস গ্রন্থি (Proboscis gland)', 'নেফ্রিডিয়া', 'ম্যালপিজিয়ান নালিকা', 'শিখা কোষ'],
              'en': ['Proboscis gland (Glomerulus)', 'Nephridia', 'Malpighian tubules', 'Flame cells']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'NCERT-তে উল্লেখিত হெமிকর্ডাটা পর্বের সাধারণ উদাহরণ কোনগুলি?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Common examples of Hemichordata listed in NCERT are:',
    'exam': 'NEET, CUET',
    'expl_bn': 'হெமிকর্ডাটার উদাহরণ হলো Balanoglossus এবং Saccoglossus।',
    'expl_en': 'Examples of Hemichordata: Balanoglossus and Saccoglossus (tongue worms / acorn worms).',
    'id': 'BIO-AK-062',
    'opts': { 'bn': [ 'ব্যালানোগ্লসাস (Balanoglossus) এবং স্যাক্কোগ্লসাস (Saccoglossus)',
                      'অ্যাসিডিয়া এবং সালপা',
                      'ব্রাঙ্কিওস্টোমা এবং অ্যাম্ফিঅক্সাস',
                      'পেট্রোমাইজন এবং মিক্সিন'],
              'en': [ 'Balanoglossus and Saccoglossus',
                      'Ascidia and Salpa',
                      'Branchiostoma and Amphioxus',
                      'Petromyzon and Myxine']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোন চারটি মৌলিক বৈশিষ্ট্যের উপস্থিতি কর্ডাটা পর্বের প্রাণীদের অবিসংবাদিতভাবে সংজ্ঞায়িত করে?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Which of the following sets of four fundamental characteristics fundamentally defines Phylum Chordata?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'কর্ডাটার চারটি অপরিহার্য মৌলিক বৈশিষ্ট্য: নোটোকর্ড, পৃষ্ঠীয় ফাঁপা নার্ভ কর্ড, গলবিলীয় ফুলকা ছিদ্র '
               'এবং পায়ু-পশ্চাৎ পুচ্ছ।',
    'expl_en': 'Animals belonging to phylum Chordata are fundamentally characterized by the presence of a notochord, a '
               'dorsal hollow nerve cord, paired pharyngeal gill slits, and a post-anal tail.',
    'id': 'BIO-AK-063',
    'opts': { 'bn': [ 'নোটোকর্ড, পৃষ্ঠীয় ফাঁপা স্নায়ুরজ্জু, যুগ্ম গলবিলীয় ফুলকা ছিদ্র এবং পায়ু-পশ্চাৎ পুচ্ছ '
                      '(Post-anal tail)',
                      'অঙ্কীয় নিরেট স্নায়ুরজ্জু, নোটোকর্ড, আঁশ এবং দ্বি-প্রকোষ্ঠী হৃদপিণ্ড',
                      'স্টোমোকর্ড, পৃষ্ঠীয় স্নায়ুরজ্জু, ফুলকা এবং রেডুলা',
                      'মেরুদণ্ড, ফুসফুস, নখর এবং স্তনগ্রন্থি'],
              'en': [ 'Notochord, dorsal hollow nerve cord, paired pharyngeal gill slits, and post-anal tail',
                      'Ventral solid nerve cord, notochord, scales, and two-chambered heart',
                      'Stomochord, dorsal nerve cord, gills, and radula',
                      'Vertebral column, lungs, claws, and mammary glands']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নন-কর্ডাটা বা অমেরুদণ্ডী প্রাণীদের কেন্দ্রীয় স্নায়ুতন্ত্র কেমন প্রকৃতির হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In non-chordates, the central nervous system is:',
    'exam': 'NEET, CUET',
    'expl_bn': 'কর্ডাটায় স্নায়ুতন্ত্র পৃষ্ঠীয়, ফাঁপা ও একক হলেও নন-কর্ডাটায় তা অঙ্কীয় (ventral), নিরেট (solid) ও '
               'যুগ্ম (double) হয়।',
    'expl_en': 'In chordates, the CNS is dorsal, hollow, and single. In non-chordates, the CNS (when present) is '
               'ventral, solid, and double.',
    'id': 'BIO-AK-064',
    'opts': { 'bn': [ 'অঙ্কীয় (ventral), নিরেট (solid) এবং দ্বি-রজ্জুযুক্ত (double)',
                      'পৃষ্ঠীয়, ফাঁপা এবং একক',
                      'পার্শ্বীয় ও ফাঁপা',
                      'সমস্ত অমেরুদণ্ডীতে সম্পূর্ণ অনুপস্থিত'],
              'en': [ 'Ventral, solid, and double',
                      'Dorsal, hollow, and single',
                      'Lateral, hollow, and segmented',
                      'Completely absent in all invertebrate phyla']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'কর্ডাটার কোন উপপর্বে নোটোকর্ড কেবলমাত্র লার্ভার লেজে থাকে এবং পূর্ণাঙ্গ দশায় তা সম্পূর্ণ অবলুপ্ত হয়ে যায় '
          '(প্রতিগামী রূপান্তর)?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In which subphylum of Chordata is the notochord present ONLY in the larval tail and disappears in the adult '
          '(Retrogressive metamorphosis)?',
    'exam': 'NEET, CUET',
    'expl_bn': 'ইউরোকর্ডাটায় নোটোকর্ড কেবল লার্ভার লেজে থাকে এবং রূপান্তরের সময় অবলুপ্ত হয়। উদাহরণ: Ascidia, Salpa, '
               'Doliolum।',
    'expl_en': 'In Urochordata, notochord is present only in larval tail, whereas in Cephalochordata, it extends from '
               'head to tail region and is persistent throughout their life.',
    'id': 'BIO-AK-065',
    'opts': { 'bn': [ 'ইউরোকর্ডাটা বা টিউনিকাটা (Urochordata - যেমন অ্যাসিডিয়া, সালপা, ডোলিওলাম)',
                      'সেফালোকর্ডাটা',
                      'ভার্টিব্রাটা',
                      'সাইক্লোস্টোমাটা'],
              'en': [ 'Urochordata (Tunicata, e.g., Ascidia, Salpa, Doliolum)',
                      'Cephalochordata (e.g., Branchiostoma)',
                      'Vertebrata',
                      'Cyclostomata']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'সেফালোকর্ডাটা (যেমন Branchiostoma বা Amphioxus)-তে নোটোকর্ড সংক্রান্ত কোন তথ্যটি সঠিক?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In Cephalochordata (such as Branchiostoma or Amphioxus / Lancelet), the notochord:',
    'exam': 'NEET, CUET',
    'expl_bn': 'সেফালোকর্ডাটায় নোটোকর্ড মস্তক থেকে লেজ পর্যন্ত বিস্তৃত এবং সারাজীবন বিদ্যমান থাকে।',
    'expl_en': 'In Cephalochordata, notochord extends from head to tail region and is persistent throughout their life '
               '(e.g., Branchiostoma / Amphioxus / Lancelet).',
    'id': 'BIO-AK-066',
    'opts': { 'bn': [ 'মাথা থেকে লেজ পর্যন্ত বিস্তৃত থাকে এবং সারাজীবন স্থায়ী হয়',
                      'কেবলমাত্র লার্ভার লেজে থাকে',
                      'পূর্ণাঙ্গ অবস্থায় অস্থিময় মেরুদণ্ড দ্বারা প্রতিস্থাপিত হয়',
                      'ডিম ফোটার আগেই বিলুপ্ত হয়'],
              'en': [ 'Extends from head to tail region and persists throughout life',
                      'Is present only in the larval tail',
                      'Is replaced by a bony vertebral column in adults',
                      'Disappears before hatching']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': "'সমস্ত ভার্টিব্রাট বা মেরুদণ্ডী প্রাণীই কর্ডাট, কিন্তু সমস্ত কর্ডাট মেরুদণ্ডী নয়'—কেন?",
    'correct': 0,
    'difficulty': 'Hard',
    'en': "'All vertebrates are chordates but all chordates are not vertebrates.' Why?",
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'ভার্টিব্রাটাতে ভ্রূণের নোটোকর্ড পরবর্তীতে কশেরুকাযুক্ত মেরুদণ্ডে পরিণত হয়। কিন্তু ইউরোকর্ডাটা ও '
               'সেফালোকর্ডাটায় কোনো মেরুদণ্ড তৈরি হয় না। তাই সব ভার্টিব্রাট কর্ডাট হলেও সব কর্ডাট ভার্টিব্রাট নয়।',
    'expl_en': 'Members of subphylum Vertebrata possess notochord during the embryonic period. The notochord is '
               'replaced by a cartilaginous or bony vertebral column in the adult. Thus all vertebrates are chordates, '
               'but all chordates (e.g., Urochordates and Cephalochordates) are not vertebrates.',
    'id': 'BIO-AK-067',
    'opts': { 'bn': [ 'কারণ ভার্টিব্রাটাতে ভ্রূণীয় নোটোকর্ড পূর্ণাঙ্গ অবস্থায় তরুণাস্থি বা অস্থিময় মেরুদণ্ড দ্বারা '
                      'প্রতিস্থাপিত হয়, কিন্তু প্রোটোকর্ডাটদের কোনো মেরুদণ্ড থাকে না',
                      'কারণ প্রোটোকর্ডেটদের স্তনগ্রন্থি থাকে',
                      'কারণ অমেরুদণ্ডী কর্ডাটদের হৃদপিণ্ড থাকে না',
                      'কারণ ভার্টিব্রাটদের পৃষ্ঠীয় স্নায়ুরজ্জু থাকে না'],
              'en': [ 'Because in vertebrates the embryonic notochord is replaced by a cartilaginous or bony vertebral '
                      'column in the adult, whereas protochordates retain a notochord without a vertebral column',
                      'Because protochordates possess mammary glands while vertebrates do not',
                      'Because non-vertebrate chordates lack hearts',
                      'Because vertebrates do not possess a dorsal hollow nerve cord']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'সাইক্লোস্টোমাটা (Cyclostomata) শ্রেণির সকল জীবিত সদস্যরা কিছু মাছের ওপর বহিঃপরজীবী। এদের প্রধান বৈশিষ্ট্য '
          'হলো এদের কেমন মুখ থাকে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'All living members of the Class Cyclostomata are ectoparasites on some fishes. They are characterized by '
          'having a:',
    'exam': 'NEET, CUET',
    'expl_bn': 'সাইক্লোস্টোমদের কোনো চোয়াল থাকে না (Agnatha); এদের মুখটি গোলাকার এবং চোষক প্রকৃতির হয়।',
    'expl_en': 'Cyclostomes have an elongated body bearing 6-15 pairs of gill slits for respiration and a sucking and '
               'circular mouth without jaws (Agnatha).',
    'id': 'BIO-AK-068',
    'opts': { 'bn': [ 'চোয়ালবিহীন চোষক প্রকৃতির গোলাকার মুখ (Sucking and circular mouth without jaws)',
                      'শক্তিশালী চোয়ালযুক্ত অঙ্কীয় মুখ',
                      'অস্থিময় দাঁতযুক্ত চঞ্চু',
                      'াঁড়াশির মতো মুখ'],
              'en': [ 'Sucking and circular mouth without jaws',
                      'Ventral mouth with powerful dentate jaws',
                      'Terminal beak-like mouth with bony teeth',
                      'Mouth flanked by pincers']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'পেট্রোমাইজন (ল্যাম্প্রে)-এর মতো সাইক্লোস্টোমদের ক্ষেত্রে নিচের কোন তথ্যটি সত্য?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Which of the following is true regarding cyclostomes like Petromyzon (Lamprey)?',
    'exam': 'NEET, CUET',
    'expl_bn': 'ল্যাম্প্রে সামুদ্রিক হলেও ডিম পাড়তে নদীতে যায়। ডিম পাড়ার পর পূর্ণাঙ্গ প্রাণী মারা যায় এবং '
               'অ্যামোসিট লার্ভা রূপান্তরের পর পুনরায় সমুদ্রে ফিরে আসে।',
    'expl_en': 'Cyclostomes are marine but migrate for spawning to fresh water (anadromous migration). After spawning, '
               'within a few days, they die. Their ammocoetes larvae, after metamorphosis, return to the ocean.',
    'id': 'BIO-AK-069',
    'opts': { 'bn': [ 'এরা সামুদ্রিক, কিন্তু ডিম পাড়ার জন্য নদীতে যায় (Anadromous); ডিম পাড়ার কয়েকদিনের মধ্যেই '
                      'মারা যায় এবং লার্ভা রূপান্তরের পর সমুদ্রে ফিরে আসে',
                      'এরা নদীতে বাস করে এবং ডিম পাড়তে সমুদ্রে যায়',
                      'এদের যুগ্ম পাখনা ও অস্থিময় আঁশ থাকে',
                      'এদের খুলি ও কশেরুকা শক্ত অস্থি নির্মিত'],
              'en': [ 'They are marine, but migrate for spawning to fresh water; after spawning, within a few days, '
                      'they die, and their larvae return to the ocean after metamorphosis',
                      'They live in freshwater and migrate to the sea for spawning (Catadromous)',
                      'They retain paired pectoral and pelvic fins with bony scales',
                      'Their cranium and vertebral column are made of dense calcium carbonate bone']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'মিক্সিন (Myxine)-কে সাধারণ ভাষায় কী নামে ডাকা হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Myxine is commonly known as the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'Myxine-কে সাধারণভাবে হ্যাগফিশ (Hagfish) বলা হয়।',
    'expl_en': 'Examples of Cyclostomata: Petromyzon (Lamprey) and Myxine (Hagfish).',
    'id': 'BIO-AK-070',
    'opts': { 'bn': ['হ্যাগফিশ (Hagfish)', 'ল্যাম্প্রে', 'ডগফিশ', 'স-ফিশ'],
              'en': ['Hagfish', 'Lamprey', 'Dogfish', 'Sawfish']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'তরুণাস্থিময় মাছদের (Chondrichthyes) কেন বিশ্রাম না নিয়ে একটানা সাঁতার কেটে চলতে হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Why do cartilaginous fishes (Chondrichthyes) have to swim constantly without rest?',
    'exam': 'NEET, CUET',
    'expl_bn': 'তরুণাস্থিময় মাছের (যেমন হাঙ্গর) দেহে বায়ুথলি বা পটকা (air bladder) না থাকার কারণে প্লবতা নিয়ন্ত্রণ '
               'করতে পারে না, তাই ডুবে যাওয়া থেকে বাঁচতে এদের অবিরত সাঁতার কাটতে হয়।',
    'expl_en': 'Due to the absence of air bladder, members of Chondrichthyes have to swim constantly to avoid sinking '
               'to the ocean floor.',
    'id': 'BIO-AK-071',
    'opts': { 'bn': [ 'দেহে পটকা বা এয়ার ব্লাডার না থাকার কারণে জলে ডুবে যাওয়া রোধ করতে এদের অবিরাম সাঁতার কাটতে হয়',
                      'কারণ তীব্র গতিতে সাঁতার না কাটলে ফুলকা দিয়ে জল প্রবাহিত হয় না',
                      'কারণ এদের হৃদপিণ্ড রক্ত পাম্প করতে পারে না',
                      'কারণ এদের পাখনা খুলির সাথে যুক্ত'],
              'en': [ 'Due to the absence of an air bladder, they have to swim constantly to avoid sinking',
                      'Because their gills only function when water is forced by swimming at top speed',
                      'Because they lack a heart to pump blood automatically',
                      'Because their fins are fused to their skull']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'তরুণাস্থিময় মাছের ত্বক শক্ত এবং আণুবীক্ষণিক প্লাকয়েড আঁশযুক্ত। এদের দাঁতগুলি মূলত কী?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The skin of cartilaginous fishes (Chondrichthyes) is tough, containing minute placoid scales. Their teeth '
          'are:',
    'exam': 'NEET, CUET',
    'expl_bn': 'হাঙ্গরের দাঁতগুলি প্রকৃতপক্ষে পেছনের দিকে বাঁকানো রূপান্তরিত প্লাকয়েড আঁশ (placoid scales)।',
    'expl_en': 'Teeth in Chondrichthyes are modified placoid scales which are backwardly directed. Their jaws are very '
               'powerful and predaceous.',
    'id': 'BIO-AK-072',
    'opts': { 'bn': [ 'রূপান্তরিত প্লাকয়েড আঁশ যা পেছনের দিকে বাঁকানো থাকে',
                      'এনামেলহীন চোয়ালের অস্থি',
                      'টিনয়েড প্লেট',
                      'কেরাটিন নির্মিত এপিডার্মাল চিরুনি'],
              'en': [ 'Modified placoid scales which are backwardly directed',
                      'Enamel-less bony projections from the mandible',
                      'Ctenoid plates fused to the premaxilla',
                      'Keratinized epidermal combs']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'কোন তরুণাস্থিময় মাছে বিদ্যুৎ অঙ্গ (electric organ) এবং কোনটিতে বিষাক্ত কাঁটা (poison sting) থাকে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which cartilaginous fish possesses an electric organ capable of delivering electric shocks, and which '
          'possesses a poison sting?',
    'exam': 'NEET, CUET',
    'expl_bn': 'Torpedo মাছে বিদ্যুৎ অঙ্গ থাকে এবং Trygon মাছে লেজে বিষাক্ত কাঁটা (sting) থাকে।',
    'expl_en': 'Some cartilaginous fishes possess electric organs (e.g., Torpedo) and some possess poison stings '
               '(e.g., Trygon).',
    'id': 'BIO-AK-073',
    'opts': { 'bn': [ 'টরপেডো (Torpedo - বিদ্যুৎ অঙ্গ); ট্রাইগন (Trygon - বিষাক্ত কাঁটা)',
                      'ট্রাইগন; টরপেডো',
                      'স্কোলিওডন; প্রিস্টিস',
                      'প্রিস্টিস; কার্কারোডন'],
              'en': [ 'Torpedo (Electric ray); Trygon (Sting ray)',
                      'Trygon; Torpedo',
                      'Scoliodon; Pristis',
                      'Pristis; Carcharodon']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'পুরুষ তরুণাস্থিময় মাছে সঙ্গমে সহায়তাকারী ক্লাস্পার (Claspers) কোন পাখনার ওপর অবস্থিত?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In male cartilaginous fishes (Chondrichthyes), copulatory organs called claspers are borne on the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'পুরুষ হাঙ্গরের পেলভিক বা শ্রোণী পাখনার ভেতরের প্রান্তে ক্লাস্পার (claspers) নামক বিশেষ সঙ্গম অঙ্গ '
               'থাকে।',
    'expl_en': 'In Chondrichthyes, in males pelvic fins bear claspers used for internal fertilization.',
    'id': 'BIO-AK-074',
    'opts': { 'bn': [ 'শ্রোণী পাখনা বা পেলভিক পাখনা (Pelvic fins)',
                      'বক্ষ পাখনা বা পেক্টোরাল পাখনা',
                      'পৃষ্ঠ পাখনা',
                      'পুচ্ছ পাখনা'],
              'en': ['Pelvic fins', 'Pectoral fins', 'Dorsal fin', 'Caudal fin']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোন বৈশিষ্ট্যগুচ্ছটি অস্থিময় মাছদের (Osteichthyes) নির্ভুলভাবে শনাক্ত করে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Which of the following sets of features characterizes Bony fishes (Osteichthyes)?',
    'exam': 'NEET, CUET',
    'expl_bn': 'অস্থিময় মাছের অগ্রভাগে মুখ, কানকোযুক্ত ৪ জোড়া ফুলকা, সাইক্লয়েড বা টিনয়েড আঁশ এবং প্লবতা '
               'নিয়ন্ত্রণকারী পটকা থাকে।',
    'expl_en': 'Osteichthyes have a bony endoskeleton, mostly terminal mouth, four pairs of gills covered by an '
               'operculum on each side, skin with cycloid/ctenoid scales, and an air bladder for buoyancy.',
    'id': 'BIO-AK-075',
    'opts': { 'bn': [ 'অস্থিময় অন্তকঙ্কাল, প্রান্তীয় মুখছিদ্র, কানকো (অপারকুলাম) দ্বারা ঢাকা ৪ জোড়া ফুলকা, '
                      'সাইক্লয়েড/টিনয়েড আঁশ এবং পটকা বা এয়ার ব্লাডার বর্তমান',
                      'তরুণাস্থিময় কঙ্কাল, অঙ্কীয় মুখ, কানকোহীন ফুলকা, প্লাকয়েড আঁশ',
                      'চোয়ালহীন মুখ, আঁশহীন দেহ',
                      'আঁশবিহীন ভেজা ত্বক, ৩-প্রকোষ্ঠী হৃদপিণ্ড'],
              'en': [ 'Bony endoskeleton, terminal mouth, 4 pairs of gills covered by operculum, cycloid/ctenoid '
                      'scales, and air bladder present',
                      'Cartilaginous skeleton, ventral mouth, 5-7 pairs of naked gill slits, placoid scales, and air '
                      'bladder absent',
                      'Jawless sucking mouth, 6-15 pairs of gill slits, scaleless body',
                      'Moist scaleless skin, 3-chambered heart, cloaca present']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোন সামুদ্রিক অস্থিময় মাছটিতে পুরুষ দেহে ব্রুড পাউচ (বাচ্চা ধারণের থলি) থাকার মাধ্যমে অপত্য লালন '
          'পরিলক্ষিত হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following is a marine bony fish showing male parental care with a brood pouch?',
    'exam': 'NEET, CUET',
    'expl_bn': 'হিপ্পোক্যাম্পাস বা সি-হর্স মাছের পুরুষটির পেটে ব্রুড পাউচ থাকে যেখানে ডিম ফুটে বাচ্চা বের হওয়া '
               'পর্যন্ত সে তা বহন করে।',
    'expl_en': 'Hippocampus (Sea horse) is a marine bony fish in which the male possesses a brood pouch on its abdomen '
               'to carry eggs until hatching.',
    'id': 'BIO-AK-076',
    'opts': { 'bn': [ 'হিপ্পোক্যাম্পাস বা সিন্ধুঘোটক (Hippocampus / Sea horse)',
                      'এক্সোসিয়েটাস বা উড়ুক্কু মাছ',
                      'বেট্টা',
                      'রুই মাছ'],
              'en': ['Hippocampus (Sea horse)', 'Exocoetus (Flying fish)', 'Betta (Fighting fish)', 'Labeo (Rohu)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোনটি অ্যাকোয়ারিয়ামে পোষা রঙিন অস্থিময় মাছের উদাহরণ?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following is an aquarium bony fish?',
    'exam': 'NEET, CUET',
    'expl_bn': 'NCERT-তে অ্যাকোয়ারিয়ামের মাছ হিসেবে Betta (ফাইটিং ফিশ) এবং Pterophyllum (অ্যাঞ্জেল ফিশ)-এর উল্লেখ '
               'রয়েছে।',
    'expl_en': 'Aquarium fishes listed in NCERT: Betta (Fighting fish) and Pterophyllum (Angel fish).',
    'id': 'BIO-AK-077',
    'opts': { 'bn': [ 'বেট্টা বা ফাইটিং ফিশ এবং টেরোফাইলাম বা অ্যাঞ্জেল ফিশ',
                      'স্কোলিওডন এবং প্রিস্টিস',
                      'মাগুর এবং কাতলা',
                      'উড়ুক্কু মাছ এবং সি-হর্স'],
              'en': [ 'Betta (Fighting fish) and Pterophyllum (Angel fish)',
                      'Scoliodon and Pristis',
                      'Clarias and Catla',
                      'Exocoetus and Hippocampus']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'অ্যাম্ফিবিয়া বা উভচর (গ্রিক amphi: দ্বৈত, bios: জীবন) নামটি দ্বারা কী বোঝানো হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The name Amphibia (Greek, amphi: dual, bios: life) indicates that amphibians can:',
    'exam': 'NEET, CUET',
    'expl_bn': 'উভচর প্রাণীরা তাদের জীবনচক্রে জল ও স্থল উভয় পরিবেশের ওপর নির্ভরশীল হওয়ায় এদের অ্যাম্ফিবিয়া বলা '
               'হয়।',
    'expl_en': 'As the name indicates (Amphi: dual, bios: life), amphibians can live in aquatic as well as terrestrial '
               'habitats.',
    'id': 'BIO-AK-078',
    'opts': { 'bn': [ 'জলে এবং ডাঙায় উভয় পরিবেশে বসবাস করতে পারে',
                      'আকাশে উড়তে ও গভীর সমুদ্রে ডুব দিতে পারে',
                      'পূর্ণাঙ্গ জীবনে কেবল ফুলকা দিয়ে শ্বাস নেয়',
                      'খাদ্য ও জল ছাড়া ৫০ বছর বাঁচতে পারে'],
              'en': [ 'Live in aquatic as well as terrestrial habitats',
                      'Fly in air and swim in deep sea',
                      'Breathe only through gills in adult life',
                      'Survive without food and water for 50 years']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'উভচর প্রাণীদের পৌষ্টিকনালী, মূত্রনালী এবং জনননালী একটি সাধারণ প্রকোষ্ঠে উন্মুক্ত হয়, তাকে কী বলে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In amphibians, the alimentary canal, urinary and reproductive tracts open into a common posterior chamber '
          'called the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'উভচরদের মলমূত্র ও জননকোষ একটি অভিন্ন প্রকোষ্ঠ ক্লোয়াকা (Cloaca) বা অবসারণীতে এসে জমা হয় এবং তা বাইরে '
               'উন্মুক্ত হয়।',
    'expl_en': 'The alimentary canal, urinary and reproductive tracts open into a common chamber called cloaca which '
               'opens to the exterior in amphibians.',
    'id': 'BIO-AK-079',
    'opts': { 'bn': ['ক্লোয়াকা বা অবসারণী (Cloaca)', 'টিম্প্যানাম', 'অপারকুলাম', 'সিলোম'],
              'en': ['Cloaca', 'Tympanum', 'Operculum', 'Coelom']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোনটি পদহীন উভচর (Limbless amphibian)-এর উদাহরণ?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following is a LIMBLESS amphibian?',
    'exam': 'NEET, CUET',
    'expl_bn': 'ইকথিয়োফিস (Ichthyophis) হলো একটি পদহীন অন্ধ উভচর প্রাণী।',
    'expl_en': 'Ichthyophis is a blind, burrowing limbless amphibian (Gymnophiona / Apoda).',
    'id': 'BIO-AK-080',
    'opts': { 'bn': ['ইকথিয়োফিস (Ichthyophis)', 'সালামান্ডার', 'হাইলা বা গেছো ব্যাঙ', 'বুফো বা কুনোব্যাঙ'],
              'en': ['Ichthyophis', 'Salamandra', 'Hyla (Tree frog)', 'Bufo (Toad)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'উভচর বা অ্যাম্ফিবিয়া শ্রেণির প্রাণীদের হৃদপিণ্ড কেমন প্রকৃতির হয়?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The heart in amphibians is:',
    'exam': 'NEET, CUET',
    'expl_bn': 'উভচরদের হৃদপিণ্ড তিন প্রকোষ্ঠযুক্ত: দুটি অলিন্দ এবং একটি অভিন্ন নিলয়।',
    'expl_en': 'The heart in amphibians is three-chambered with two auricles and one ventricle, causing mixing of '
               'oxygenated and deoxygenated blood in the ventricle.',
    'id': 'BIO-AK-081',
    'opts': { 'bn': [ 'তিন-প্রকোষ্ঠী (দুটি অলিন্দ এবং একটি নিলয়)',
                      'দ্বি-প্রকোষ্ঠী (একটি অলিন্দ ও একটি নিলয়)',
                      'চার-প্রকোষ্ঠী (দুটি অলিন্দ ও দুটি নিলয়)',
                      'একক প্রকোষ্ঠযুক্ত'],
              'en': [ 'Three-chambered (two auricles and one ventricle)',
                      'Two-chambered (one auricle and one ventricle)',
                      'Four-chambered (two auricles and two ventricles)',
                      'Single-chambered tubular contractile vessel']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'রেপটিলিয়া (Reptilia বা সরীসৃপ) নামটি এদের কোন ধরনের স্বভাব বা চলন রীতির পরিচায়ক?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Class Reptilia refers to their characteristic mode of locomotion, which is:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ল্যাটিন repere শব্দের অর্থ বুকে হেঁটে চলা; সরীসৃপদের প্রধান বৈশিষ্ট্য হলো এরা বুকে ভর দিয়ে হামাগুড়ি '
               'দিয়ে চলে।',
    'expl_en': 'The class name refers to their creeping or crawling mode of locomotion (Latin, repere or reptum, to '
               'creep or crawl).',
    'id': 'BIO-AK-082',
    'opts': { 'bn': [ 'বুকে হেঁটে বা বুকে ভর দিয়ে চলা বা ক্রলিং (Latin, repere: বুকে হাঁটা)',
                      'ত্বকের সাহায্যে ওড়া',
                      'লাফিয়ে চলা',
                      'জেট প্রপালশন'],
              'en': [ 'Creeping or crawling locomotion (Latin, repere or reptum: to creep or crawl)',
                      'Flying by skin flaps',
                      'Hopping on powerful hindlegs',
                      'Jet propulsion through siphons']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'সরীসৃপদের হৃদপিণ্ড সাধারণত অসম্পূর্ণ তিন-প্রকোষ্ঠী হলেও কার ক্ষেত্রে তা সুস্পষ্ট চার-প্রকোষ্ঠী '
          '(Four-chambered)?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The heart in reptiles is usually three-chambered, but is distinctively FOUR-CHAMBERED in:',
    'exam': 'NEET, CUET',
    'expl_bn': 'সরীসৃপদের মধ্যে কুমিরের (Crocodiles) হৃদপিণ্ড সম্পূর্ণভাবে চার প্রকোষ্ঠ বিশিষ্ট (দুটি অলিন্দ ও দুটি '
               'নিলয়)।',
    'expl_en': 'Heart is usually three-chambered in reptiles, but four-chambered in crocodiles (possessing two '
               'complete auricles and two complete ventricles).',
    'id': 'BIO-AK-083',
    'opts': { 'bn': ['কুমির বা ক্রোকোডাইল (Crocodiles)', 'গিরগিটি এবং রক্তচোষা', 'কেউটে এবং গোখরো', 'কচ্ছপ'],
              'en': [ 'Crocodiles (Crocodilus and Alligator)',
                      'Chameleon and Calotes',
                      'Naja (Cobra) and Vipera',
                      'Chelone (Turtle) and Testudo']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'সাপ এবং টিকটিকি খোলস ত্যাগের মাধ্যমে আঁশ পরিবর্তন করে। সরীসৃপদের ত্বকের মূল বৈশিষ্ট্য কী?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Snakes and lizards shed their scales as skin cast. The skin of reptiles is characteristically:',
    'exam': 'NEET, CUET',
    'expl_bn': 'সরীসৃপের ত্বক শুষ্ক, গ্রন্থিহীন এবং কেরাটিনযুক্ত শক্ত এপিডার্মাল আঁশ বা স্কুট (scutes) দ্বারা আবৃত '
               'থাকে।',
    'expl_en': 'Their body is covered by dry and cornified skin, epidermal scales or scutes. Tympanum represents ear.',
    'id': 'BIO-AK-084',
    'opts': { 'bn': [ 'শুষ্ক ও শৃঙ্গায়িত (dry and cornified) এবং এপিডার্মাল আঁশ বা স্কুট দ্বারা আবৃত',
                      'ভেজা ও গ্রন্থিময়',
                      'প্লাকয়েড আঁশযুক্ত',
                      'সিলিয়াযুক্ত'],
              'en': [ 'Dry and cornified, covered by epidermal scales or scutes',
                      'Moist and glandular without scales',
                      'Covered with placoid teeth and slime pores',
                      'Ciliated and highly vascularized with no keratin']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোনটি উড্ডয়নহীন পাখি (Flightless bird)?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following is a flightless bird?',
    'exam': 'NEET, CUET',
    'expl_bn': 'উটপাখি বা অস্ট্রিচ (Struthio) হলো উড়তে অক্ষম দৌড়বাজ পাখি।',
    'expl_en': 'The characteristic features of Aves (birds) are the presence of feathers and most of them can fly '
               'except flightless birds like Struthio (Ostrich).',
    'id': 'BIO-AK-085',
    'opts': { 'bn': ['স্ট্রুথিও বা উটপাখি (Struthio / Ostrich)', 'পায়রা', 'কাক', 'টিয়া'],
              'en': ['Struthio (Ostrich)', 'Columba (Pigeon)', 'Corvus (Crow)', 'Psittacula (Parrot)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'পাখিদের ওড়ার সুবিধার্থে দেহের ওজন কমানোর জন্য তাদের দীর্ঘ অস্থিগুলি ফাঁপা ও বায়ুগহ্বরযুক্ত হয়। এই ধরনের '
          'অস্থিকে কী বলে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The long bones of birds (Aves) are hollow with air cavities to reduce body weight for flight. Such bones '
          'are called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাখিদের ওড়ার অভিযোজন হিসেবে তাদের অস্থিগুলি ভেতর থেকে ফাঁপা ও বায়ুগহ্বরযুক্ত হয়, এদের নিউম্যাটিক '
               'অস্থি (pneumatic bones) বলে।',
    'expl_en': 'Endoskeleton of birds is fully ossified (bony) and the long bones are hollow with air cavities '
               '(pneumatic) to minimize weight during flight.',
    'id': 'BIO-AK-086',
    'opts': { 'bn': [ 'নিউম্যাটিক অস্থি বা বায়বীয় অস্থি (Pneumatic bones)',
                      'সিসাময়েড অস্থি',
                      'হ্যাভারশিয়ান অস্থি',
                      'তরুণাস্থি'],
              'en': ['Pneumatic bones', 'Sesamoid bones', 'Compact haversian bones', 'Cartilaginous epiphyses']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'পাখিদের সম্পূর্ণ ত্বক গ্রন্থিহীন ও শুষ্ক, কেবলমাত্র লেজের গোড়ায় কোন গ্রন্থিটি উপস্থিত থাকে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In birds, the skin is completely dry without glands EXCEPT for which gland located at the base of the tail?',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাখির ত্বকে কোনো গ্রন্থি থাকে না, কেবল লেজের গোড়ায় ইউরোপাইজিয়াল বা প্রীন গ্রন্থি (oil gland) থাকে '
               'যার তেল পাখি ঠোঁট দিয়ে পালকে মাখিয়ে জলরোধী করে।',
    'expl_en': 'Skin of birds is dry without glands except the oil gland (preen gland) at the base of the tail used '
               'for preening and waterproofing feathers.',
    'id': 'BIO-AK-087',
    'opts': { 'bn': [ 'তৈল গ্রন্থি বা প্রীন গ্রন্থি (Oil / Preen gland)',
                      'ঘর্মগ্রন্থি',
                      'সিবেসিয়াস গ্রন্থি',
                      'স্তনগ্রন্থি'],
              'en': ['Oil gland (Uropygial or preen gland)', 'Sweat gland', 'Sebaceous gland', 'Mammary gland']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'পাখিদের পৌষ্টিকনালীতে খাদ্য সাময়িক সঞ্চয় ও পেষাইয়ের জন্য কোন দুটি অতিরিক্ত প্রকোষ্ঠ থাকে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'The digestive tract of birds possesses which two additional specialized chambers?',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাখির কোনো দাঁত থাকে না, তাই খাদ্য সঞ্চয়ের জন্য ক্রপ (crop) এবং খাদ্য পেষাইয়ের জন্য পেশিবহুল গিজার্ড '
               '(gizzard) থাকে।',
    'expl_en': 'The digestive tract of birds has additional chambers, the crop (for food storage and softening) and '
               'gizzard (muscular grinding chamber with grit).',
    'id': 'BIO-AK-088',
    'opts': { 'bn': [ 'ক্রপ (Crop) এবং গিজার্ড (Gizzard)',
                      'রুমেন ও রেটিকুলাম',
                      'সিকাম ও অ্যাপেন্ডিক্স',
                      'কার্ডিয়া ও পাইলোরাস'],
              'en': ['Crop and Gizzard', 'Rumen and Reticulum', 'Caecum and Vermiform appendix', 'Cardia and Pylorus']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'যেসব প্রাণী পরিবেশের তাপমাত্রার তারতম্য সত্ত্বেও দেহের অভ্যন্তরীণ তাপমাত্রা সর্বদা নির্দিষ্ট ও স্থির রাখতে '
          'পারে, তাদের কী বলে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Organisms that are capable of maintaining a constant internal body temperature regardless of ambient '
          'environmental fluctuations are termed:',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাখি এবং স্তন্যপায়ী প্রাণীরা হোমিওথার্মাস বা উষ্ণশোণিত (warm-blooded) কারণ তারা দেহের তাপমাত্রা '
               'নির্দিষ্ট বজায় রাখে।',
    'expl_en': 'Birds and mammals are homoiothermous (warm-blooded) animals, i.e., they are able to maintain a '
               'constant body temperature.',
    'id': 'BIO-AK-089',
    'opts': { 'bn': [ 'হোমিওথার্মাস বা উষ্ণশোণিত প্রাণী (পাখি এবং স্তন্যপায়ী)',
                      'পোইকিলোথার্মাস বা শীতলশোণিত প্রাণী (মাছ, উভচর, সরীসৃপ)',
                      'স্টেনোথার্মাল',
                      'ইউরিথার্মাল'],
              'en': [ 'Homoiothermous / Warm-blooded (Aves and Mammals)',
                      'Poikilothermous / Cold-blooded (Fishes, Amphibians, Reptiles)',
                      'Stenothermal',
                      'Eurythermal']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'স্তন্যপায়ী বা ম্যামালিয়া শ্রেণির সর্বপ্রধান অনন্য বৈশিষ্ট্য যা অন্য কোনো মেরুদণ্ডী শ্রেণিতে দেখা যায় না '
          'তা হলো:',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The most unique, defining mammalian characteristic which is found in no other class of vertebrates is:',
    'exam': 'NEET, CUET',
    'expl_bn': 'স্তন্যপায়ী প্রাণীর সবচেয়ে অনন্য বৈশিষ্ট্য হলো তাদের দেহে স্তনগ্রন্থির (Mammary glands) উপস্থিতি যা '
               'থেকে দুগ্ধ ক্ষরিত হয়ে শাবক পুষ্টি লাভ করে।',
    'expl_en': 'The most unique mammalian characteristic is the presence of milk producing glands (mammary glands) by '
               'which the young ones are nourished.',
    'id': 'BIO-AK-090',
    'opts': { 'bn': [ 'নবজাতক শাবককে স্তন্যপান করানোর জন্য দুগ্ধ নিঃসরণকারী স্তনগ্রন্থির (Mammary glands) উপস্থিতি',
                      'চার-প্রকোষ্ঠী হৃদপিণ্ডের উপস্থিতি',
                      'শ্বাস নেওয়ার জন্য ফুসফুস',
                      'চোখের পাতার উপস্থিতি'],
              'en': [ 'Presence of milk-producing mammary glands to nourish the young ones',
                      'Presence of a four-chambered heart',
                      'Presence of lungs for breathing',
                      'Presence of paired eyes with eyelids']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোন স্তন্যপায়ী প্রাণীটি ব্যতিক্রমীভাবে ডিম্বজ বা ডিম প্রসবকারী (Oviparous)?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following mammals is OVIPAROUS (egg-laying)?',
    'exam': 'NEET, CUET',
    'expl_bn': 'প্লাটিপাস বা অর্নিথোরিঙ্কাস হলো একটি ডিম্বজ স্তন্যপায়ী (oviparous mammal) যা ডিম পাড়ে কিন্তু '
               'বাচ্চাকে দুধ খাওয়ায়।',
    'expl_en': 'Ornithorhynchus (Platypus) is a monotreme mammal that lays eggs (oviparous) while still suckling its '
               'hatched young with milk from mammary slits.',
    'id': 'BIO-AK-091',
    'opts': { 'bn': [ 'অর্নিথোরিঙ্কাস বা প্লাটিপাস (Ornithorhynchus / Duck-billed Platypus)',
                      'ক্যাঙ্গারু',
                      'বাদুড়',
                      'নীল তিমি'],
              'en': [ 'Ornithorhynchus (Duck-billed Platypus)',
                      'Macropus (Kangaroo)',
                      'Pteropus (Flying fox)',
                      'Balaenoptera (Blue whale)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোনটি উড়ুক্কু স্তন্যপায়ী প্রাণীর উদাহরণ?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following is a flying mammal?',
    'exam': 'NEET, CUET',
    'expl_bn': 'টেরোপাস (বাদুড়) হলো ডানাযুক্ত উড়তে সক্ষম স্তন্যপায়ী প্রাণী।',
    'expl_en': 'Pteropus (Flying fox / Bat) is a true mammal adapted for powered flight using skin flaps (patagium) '
               'between elongated digits.',
    'id': 'BIO-AK-092',
    'opts': { 'bn': [ 'টেরোপাস বা বাদুড় (Pteropus / Flying fox)',
                      'উড়ুক্কু মাছ',
                      'উড়ুক্কু গিরগিটি',
                      'উড়ুক্কু কাঠবিড়ালি'],
              'en': ['Pteropus (Flying fox / Bat)', 'Exocoetus (Flying fish)', 'Draco (Flying lizard)', 'Petaurista']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোন জোড়াটি জলজ স্তন্যপায়ী প্রাণীর সঠিক উদাহরণ?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which of the following are aquatic mammals?',
    'exam': 'NEET, CUET',
    'expl_bn': 'ডলফিন এবং নীল তিমি হলো স্তন্যপায়ী প্রাণী; এরা মাছের মতো জলে বাস করলেও ফুসফুস দিয়ে শ্বাস নেয় এবং '
               'সরাসরি শাবক প্রসব করে।',
    'expl_en': 'Delphinus (Dolphin) and Balaenoptera (Blue whale) are fully aquatic, placental mammals that breathe '
               'air using lungs and give birth to live calves.',
    'id': 'BIO-AK-093',
    'opts': { 'bn': [ 'ডলফিন (Delphinus) এবং নীল তিমি (Balaenoptera)',
                      'হাঙ্গর এবং করাত মাছ',
                      'কচ্ছপ এবং কুমির',
                      'সি-হর্স এবং উড়ুক্কু মাছ'],
              'en': [ 'Delphinus (Common dolphin) and Balaenoptera (Blue whale)',
                      'Scoliodon and Pristis',
                      'Chelone and Crocodilus',
                      'Hippocampus and Exocoetus']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'বহিস্থ কান বা পিনা (Pinna), ত্বকে রোম এবং চোয়ালের গর্তে প্রোথিত ভিন্ন ভিন্ন প্রকৃতির দাঁত (thecodont '
          'dentition)—কোন শ্রেণির মূল বৈশিষ্ট্য?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Presence of pinna (external ear), hair on skin, and heterodont dentition embedded in sockets of the jaw '
          '(thecodont) are characteristic hallmarks of:',
    'exam': 'NEET, CUET',
    'expl_bn': 'বহিঃকর্ণের পিনা, গায়ে লোম এবং চোয়ালের সকেটে দাঁত প্রোথিত থাকা স্তন্যপায়ী শ্রেণির বৈশিষ্ট্য।',
    'expl_en': 'External ears or pinnae are present, hair is present on skin, and different types of teeth '
               '(heterodont) are present in the jaw in Class Mammalia.',
    'id': 'BIO-AK-094',
    'opts': { 'bn': ['স্তন্যপায়ী বা ম্যামালিয়া (Mammalia)', 'পক্ষী বা এভিস', 'সরীসৃপ', 'উভচর'],
              'en': ['Mammalia', 'Aves', 'Reptilia', 'Amphibia']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'জল সংরক্ষণের উদ্দেশ্যে ইউরিক অ্যাসিডের পেলেট বা পেস্ট নির্গমনকারী ইউরিকোটেলিক (Uricotelic) প্রাণীদের সঠিক '
          'দল কোনটি?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Which of the following sets of animals are all URICOTELIC, excreting nitrogenous waste as paste or pellets '
          'of uric acid to conserve water?',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাখি, সরীসৃপ, পতঙ্গ এবং স্থলজ শামুক ইউরিক অ্যাসিড নির্গমন করে (Uricotelic)।',
    'expl_en': 'Reptiles, birds, land snails and insects excrete nitrogenous wastes as uric acid in the form of pellet '
               'or paste with minimum loss of water and are called uricotelic animals.',
    'id': 'BIO-AK-095',
    'opts': { 'bn': [ 'সরীসৃপ, পাখি, স্থলজ শামুক এবং পতঙ্গ',
                      'স্তন্যপায়ী, পূর্ণাঙ্গ ব্যাঙ এবং হাঙ্গর',
                      'জলজ অস্থিময় মাছ ও জলজ লার্ভা',
                      'স্পঞ্জ, নিডারিয়া এবং প্ল্যানেরিয়া'],
              'en': [ 'Reptiles, Birds, Land snails, and Insects',
                      'Mammals, adult amphibians, and sharks',
                      'Aquatic bony fishes and aquatic larvae',
                      'Sponges, cnidarians, and planarians']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'তরুণাস্থিময় মাছে (যেমন হাঙ্গরে) শিকারের তৈরি অতি ক্ষুদ্র বৈদ্যুতিক ক্ষেত্র শনাক্তকারী সংবেদী অঙ্গের নাম '
          'কী?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which organ in cartilaginous fishes senses minute electrical fields generated by prey in water?',
    'exam': 'NEET, CUET',
    'expl_bn': 'হাঙ্গরের থলথলে মাথায় অবস্থিত অ্যাম্পুলা অব লরেঞ্জিনি হলো শিকারের পেশি সঞ্চালনে তৈরি বৈদ্যুতিক স্পন্দন '
               'ধরার অত্যন্ত সংবেদনশীল গ্রাহক অঙ্গ।',
    'expl_en': 'Ampullae of Lorenzini are specialized electroreceptors located on the snout of elasmobranchs (sharks '
               'and rays) that detect microvolt electric potentials of struggling prey.',
    'id': 'BIO-AK-096',
    'opts': { 'bn': [ 'অ্যাম্পুলা অব লরেঞ্জিনি (Ampullae of Lorenzini)',
                      'স্ট্যাটোসিস্ট',
                      'র\u200d্যাবডাইটস',
                      'ওমাটিডিয়া'],
              'en': ['Ampullae of Lorenzini', 'Statocysts', 'Rhabdites', 'Ommatidia']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'প্রতিকূল পরিবেশে টিকে থাকার জন্য স্পঞ্জের দেহের ভেতরে সৃষ্ট অযৌন অভ্যন্তরীণ মুকুলকে কী বলে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In sponges, asexual internal buds formed to tide over unfavorable conditions are called:',
    'exam': 'NEET, CUET',
    'expl_bn': 'মিষ্ট জলের স্পঞ্জে শীতকালে বা খরার হাত থেকে বাঁচতে অভ্যন্তরীণ মুকুল বা গেমিউল (Gemmule) গঠিত হয়।',
    'expl_en': 'Gemmules are internal asexual dormant buds produced by freshwater sponges (Spongilla) containing '
               'archaeocytes surrounded by a thick spicular coat to survive desiccation.',
    'id': 'BIO-AK-097',
    'opts': { 'bn': ['গেমিউল (Gemmules)', 'গেমা', 'প্ল্যানুলা', 'ট্রোকোফোর'],
              'en': ['Gemmules', 'Gemmae', 'Planula', 'Trochophore']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিডারিয়া বা সিলেন্টারেটা পর্বের প্রাণীদের মুক্ত সাঁতারু সিলিয়াযুক্ত লার্ভাকে কী বলা হয়?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'A free-swimming ciliated larva of cnidarians (coelenterates) is called a:',
    'exam': 'NEET, CUET',
    'expl_bn': 'নিডারিয়ার সিলিয়াযুক্ত মুক্ত সাঁতারু লার্ভাকে প্ল্যানুলা (Planula) লার্ভা বলা হয়।',
    'expl_en': 'The typical motile, ciliated, solid gastrula larva of cnidarians (such as Obelia and jellyfish) is the '
               'Planula larva.',
    'id': 'BIO-AK-098',
    'opts': { 'bn': ['প্ল্যানুলা (Planula)', 'প্যারেনকাইমুলা', 'অ্যাম্ফিব্লাস্টুলা', 'ট্রোকোফোর'],
              'en': ['Planula', 'Parenchymula', 'Amphiblastula', 'Trochophore']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'হெமிকর্ডাটা পর্বের (যেমন ব্যালানোগ্লসাস) মুক্ত সাঁতারু লার্ভাটির নাম কী?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'The larva of acorn worms (Hemichordata, e.g., Balanoglossus) is called the:',
    'exam': 'NEET, CUET',
    'expl_bn': 'ব্যালানোগ্লসাসের লার্ভাকে টোরনারিয়া (Tornaria) লার্ভা বলে যা একাইনোডার্মাটার লার্ভার সাথে অত্যন্ত '
               'সাদৃশ্যপূর্ণ।',
    'expl_en': 'The free-swimming ciliated larva of Hemichordata is the Tornaria larva, structurally closely related '
               'to echinoderm bipinnaria.',
    'id': 'BIO-AK-099',
    'opts': { 'bn': ['টোরনারিয়া লার্ভা (Tornaria larva)', 'বাইপিনারিয়া লার্ভা', 'ট্রোকোফোর লার্ভা', 'গ্লোচিডিয়াম'],
              'en': ['Tornaria larva', 'Bipinnaria larva', 'Trochophore larva', 'Glochidium larva']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'সবুজ গ্রন্থি বা গ্রিন গ্ল্যান্ড (অ্যান্টেনাল গ্রন্থি) কার রেচন অঙ্গ হিসেবে কাজ করে?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Green glands (antennal glands) serve as excretory organs in:',
    'exam': 'NEET, CUET',
    'expl_bn': 'চিংড়ি বা প্রন (Prawn)-এর প্রধান রেচন অঙ্গ হলো মাথার কাছে অবস্থিত সবুজ গ্রন্থি বা অ্যান্টিনারি '
               'গ্রন্থি।',
    'expl_en': 'Antennal glands or green glands perform the excretory function in crustaceans such as prawns.',
    'id': 'BIO-AK-100',
    'opts': { 'bn': [ 'চিংড়ির মতো ক্রাস্টাশিয়ানদের (Prawns)',
                      'আরশোলার মতো পতঙ্গদের',
                      'মাকড়সার মতো অ্যারাকনিডদের',
                      'শতপদীর মতো মিরিয়াপডদের'],
              'en': [ 'Crustaceans like Prawns (Palaemon)',
                      'Insects like Cockroaches',
                      'Arachnids like Spiders',
                      'Myriapods like Centipedes']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': "নিচের কোন মোলাস্কটিকে সাধারণ ভাষায় 'সি হেয়ার' (Sea hare) বলা হয়?",
    'correct': 0,
    'difficulty': 'Easy',
    'en': "Which of the following molluscs is commonly known as 'Sea hare'?",
    'exam': 'NEET, CUET',
    'expl_bn': 'Aplysia-কে সি হেয়ার (Sea hare) বলা হয়।',
    'expl_en': 'Common names from NCERT: Pila (Apple snail), Pinctada (Pearl oyster), Sepia (Cuttlefish), Loligo '
               '(Squid), Octopus (Devil fish), Aplysia (Sea hare), Dentalium (Tusk shell), and Chaetopleura (Chiton).',
    'id': 'BIO-AK-101',
    'opts': { 'bn': ['অ্যাপ্লাইসিয়া (Aplysia)', 'ডেন্টালিয়াম', 'কিটোপ্লিউরা', 'পিলা বা আপেল শামুক'],
              'en': ['Aplysia', 'Dentalium (Tusk shell)', 'Chaetopleura (Chiton)', 'Pila (Apple snail)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'ডেন্টালিয়াম (Dentalium)-এর সাধারণ নাম কী?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Dentalium is commonly known as:',
    'exam': 'NEET, CUET',
    'expl_bn': 'Dentalium-কে সাধারণ ভাষায় টাস্ক শেল (Tusk shell) বলা হয়।',
    'expl_en': 'Dentalium possesses a tusk-like tubular shell open at both ends and is commonly called the tusk shell.',
    'id': 'BIO-AK-102',
    'opts': { 'bn': ['টাস্ক শেল বা হাতির দাঁতের মতো খোলক (Tusk shell)', 'কাইটন', 'আপেল শামুক', 'মুক্তা ঝিনুক'],
              'en': ['Tusk shell', 'Chiton', 'Apple snail', 'Pearl oyster']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের সাপগুলির মধ্যে কোনটি বিষহীন (Non-poisonous)?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which snake among the following is NON-POISONOUS?',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাইথন বা অজগর হলো একটি বিষহীন সাপ; কোবরা, কালাচ ও ভাইপার হলো মারাত্মক বিষধর সাপ।',
    'expl_en': 'Python is a large non-venomous constrictor snake. Cobra (Naja), Krait (Bangarus), and Viper (Vipera) '
               'are venomous poisonous snakes listed in NCERT.',
    'id': 'BIO-AK-103',
    'opts': { 'bn': ['অজগর বা পাইথন (Python)', 'গোখরো বা কেউটে', 'কালাচ বা ক্রেইট', 'চন্দ্রবোড়া বা ভাইপার'],
              'en': ['Python molurus', 'Naja naja (Cobra)', 'Bangarus caeruleus (Krait)', 'Vipera russelli (Viper)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'পাখিদের ক্ষেত্রে স্তন্যপায়ী প্রাণীর ল্যারিঙ্কসের পরিবর্তে কোন অঙ্গটি সুমধুর শব্দ বা ডাক তৈরি করে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'In birds, which organ produces vocal sounds instead of a mammalian larynx?',
    'exam': 'NEET, CUET',
    'expl_bn': 'পাখির ডাক উৎপন্নকারী বিশেষ অঙ্গ হলো সিরিঙ্কস (Syrinx) যা শ্বাসনালীর গোড়ায় অবস্থিত।',
    'expl_en': 'Birds produce sound using the syrinx, a cartilaginous voice box situated at the base of the trachea '
               'near the bronchi.',
    'id': 'BIO-AK-104',
    'opts': { 'bn': ['সিরিঙ্কস বা শব্দথলি (Syrinx)', 'গলবিল', 'ল্যারিঙ্কস', 'গিজার্ড'],
              'en': ['Syrinx (located at tracheal bifurcation)', 'Pharynx', 'Larynx', 'Gizzard']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'অ্যাসিডিয়া (Ascidia)-র মতো সি-স্কুইর্ট কোন কর্ডাটা উপপর্বের অন্তর্গত?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Sea squirts like Ascidia belong to which chordate subphylum?',
    'exam': 'NEET, CUET',
    'expl_bn': 'অ্যাসিডিয়া (Ascidia) হলো ইউরোকর্ডাটা উপপর্বের অন্তর্ভুক্ত প্রাণী।',
    'expl_en': 'Ascidia is a classic tunicated marine invertebrate belonging to Urochordata.',
    'id': 'BIO-AK-105',
    'opts': { 'bn': ['ইউরোকর্ডাটা বা টিউনিকাটা (Urochordata)', 'সেফালোকর্ডাটা', 'ভার্টিব্রাটা', 'হெமிকর্ডাটা'],
              'en': ['Urochordata (Tunicata)', 'Cephalochordata', 'Vertebrata', 'Hemichordata']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'তিনটি প্রধান সিলোম বা দেহগহ্বরের প্রদত্ত প্রস্থচ্ছেদগুলি লক্ষ্য করো:<br><svg viewBox="0 0 520 180" '
          'width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">\n'
          '  <!-- (A) Eucoelomate (Coelomate) -->\n'
          '  <g transform="translate(10, 10)">\n'
          '    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>\n'
          '    <!-- Mesoderm lining body wall and gut with true cavity -->\n'
          '    <circle cx="80" cy="80" r="60" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <!-- Coelom cavity (white) -->\n'
          '    <circle cx="80" cy="80" r="48" fill="#ffffff" stroke="#ef4444" stroke-width="1"/>\n'
          '    <!-- Gut with mesoderm lining -->\n'
          '    <circle cx="80" cy="80" r="28" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>\n'
          '    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Gut</text>\n'
          '    <text x="80" y="48" fill="#b91c1c" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Coelom</text>\n'
          '    <text x="80" y="168" fill="#991b1b" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">A: Coelomate</text>\n'
          '  </g>\n'
          '\n'
          '  <!-- (B) Pseudocoelomate -->\n'
          '  <g transform="translate(180, 10)">\n'
          '    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>\n'
          '    <!-- Pseudocoelom cavity space -->\n'
          '    <circle cx="80" cy="80" r="60" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>\n'
          '    <!-- Scattered mesodermal pouches -->\n'
          '    <circle cx="50" cy="60" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <circle cx="110" cy="60" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <circle cx="50" cy="100" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <circle cx="110" cy="100" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <!-- Endodermal gut -->\n'
          '    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>\n'
          '    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Gut</text>\n'
          '    <text x="80" y="168" fill="#0369a1" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">B: Pseudocoelomate</text>\n'
          '  </g>\n'
          '\n'
          '  <!-- (C) Acoelomate -->\n'
          '  <g transform="translate(350, 10)">\n'
          '    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>\n'
          '    <!-- Solid mesoderm (parenchyma) without any cavity -->\n'
          '    <circle cx="80" cy="80" r="60" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <!-- Endodermal gut -->\n'
          '    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>\n'
          '    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Gut</text>\n'
          '    <text x="80" y="45" fill="#991b1b" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Parenchyma</text>\n'
          '    <text x="80" y="168" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">C: Acoelomate</text>\n'
          '  </g>\n'
          '</svg><br>নিচের কোন বিকল্পে চিত্র এবং তার প্রতিনিধি প্রাণী পর্বকে সঠিকভাবে মেলানো হয়েছে?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Examine the cross-sectional diagrams of the three coelom body plans:<br><svg viewBox="0 0 520 180" '
          'width="100%" height="180" xmlns="http://www.w3.org/2000/svg" class="select-none">\n'
          '  <!-- (A) Eucoelomate (Coelomate) -->\n'
          '  <g transform="translate(10, 10)">\n'
          '    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>\n'
          '    <!-- Mesoderm lining body wall and gut with true cavity -->\n'
          '    <circle cx="80" cy="80" r="60" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <!-- Coelom cavity (white) -->\n'
          '    <circle cx="80" cy="80" r="48" fill="#ffffff" stroke="#ef4444" stroke-width="1"/>\n'
          '    <!-- Gut with mesoderm lining -->\n'
          '    <circle cx="80" cy="80" r="28" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>\n'
          '    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Gut</text>\n'
          '    <text x="80" y="48" fill="#b91c1c" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Coelom</text>\n'
          '    <text x="80" y="168" fill="#991b1b" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">A: Coelomate</text>\n'
          '  </g>\n'
          '\n'
          '  <!-- (B) Pseudocoelomate -->\n'
          '  <g transform="translate(180, 10)">\n'
          '    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>\n'
          '    <!-- Pseudocoelom cavity space -->\n'
          '    <circle cx="80" cy="80" r="60" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>\n'
          '    <!-- Scattered mesodermal pouches -->\n'
          '    <circle cx="50" cy="60" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <circle cx="110" cy="60" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <circle cx="50" cy="100" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <circle cx="110" cy="100" r="10" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <!-- Endodermal gut -->\n'
          '    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>\n'
          '    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Gut</text>\n'
          '    <text x="80" y="168" fill="#0369a1" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">B: Pseudocoelomate</text>\n'
          '  </g>\n'
          '\n'
          '  <!-- (C) Acoelomate -->\n'
          '  <g transform="translate(350, 10)">\n'
          '    <circle cx="80" cy="80" r="70" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>\n'
          '    <!-- Solid mesoderm (parenchyma) without any cavity -->\n'
          '    <circle cx="80" cy="80" r="60" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>\n'
          '    <!-- Endodermal gut -->\n'
          '    <circle cx="80" cy="80" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>\n'
          '    <text x="80" y="85" fill="#854d0e" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Gut</text>\n'
          '    <text x="80" y="45" fill="#991b1b" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Parenchyma</text>\n'
          '    <text x="80" y="168" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">C: Acoelomate</text>\n'
          '  </g>\n'
          '</svg><br>Which of the following correctly matches the diagram with the animal phylum representing it?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'A হলো প্রকৃত সিলোমেট (দেহগহ্বর মেসোডার্ম দ্বারা আবৃত - অ্যানেলিডা থেকে কর্ডাটা); B হলো মেসোডার্মের '
               'বিক্ষিপ্ত থলিযুক্ত সিউডোসিলোমেট (অ্যাসকেলমিন্থেস); এবং C হলো সিলোমহীন অ্যাসিলোমেট (প্লাটিহেলমিন্থেস)।',
    'expl_en': 'Diagram A represents a true eucoelomate with body cavity lined completely by mesoderm peritoneum on '
               'both body wall and gut (Annelids to Chordates). Diagram B represents a pseudocoelomate with scattered '
               'mesodermal pouches (Aschelminthes). Diagram C represents an acoelomate with solid parenchyma '
               '(Platyhelminthes).',
    'id': 'BIO-AK-106',
    'opts': { 'bn': [ 'A = সিলোমেট (অ্যানেলিডা থেকে কর্ডাটা); B = সিউডোসিলোমেট (অ্যাসকেলমিন্থেস); C = অ্যাসিলোমেট '
                      '(প্লাটিহেলমিন্থেস)',
                      'A = অ্যাসিলোমেট (প্লাটিহেলমিন্থেস); B = সিলোমেট (অ্যানেলিডা); C = সিউডোসিলোমেট '
                      '(অ্যাসকেলমিন্থেস)',
                      'A = সিউডোসিলোমেট; B = সিলোমেট; C = অ্যাসিলোমেট',
                      'A = সিলোমেট (অ্যাসকেলমিন্থেস); B = সিউডোসিলোমেট (অ্যানেলিডা); C = অ্যাসিলোমেট (পরিফেরা)'],
              'en': [ 'A = Coelomate (Annelida to Chordata); B = Pseudocoelomate (Aschelminthes); C = Acoelomate '
                      '(Platyhelminthes)',
                      'A = Acoelomate (Platyhelminthes); B = Coelomate (Annelida); C = Pseudocoelomate (Aschelminthes)',
                      'A = Pseudocoelomate; B = Coelomate; C = Acoelomate',
                      'A = Coelomate (Aschelminthes); B = Pseudocoelomate (Annelida); C = Acoelomate (Porifera)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচে একটি আদর্শ কর্ডাটা প্রাণীর মৌলিক দৈহিক গঠনের রেখাচিত্র দেওয়া হলো:<br><svg viewBox="0 0 520 200" '
          'width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">\n'
          '  <!-- General chordate fish-like body outline -->\n'
          '  <path d="M 40 100 Q 150 20 400 30 Q 480 70 500 100 Q 480 130 400 170 Q 150 180 40 100 Z" fill="#f0f9ff" '
          'stroke="#0284c7" stroke-width="2.5"/>\n'
          '  \n'
          '  <!-- 1. Nerve cord (Dorsal hollow nerve cord, green, labeled A) -->\n'
          '  <path d="M 90 55 Q 250 40 450 65" fill="none" stroke="#16a34a" stroke-width="4"/>\n'
          '  <text x="250" y="45" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">A (Dorsal Hollow Nerve Cord)</text>\n'
          '  \n'
          '  <!-- 2. Notochord (Blue solid rod under nerve cord, labeled B) -->\n'
          '  <path d="M 70 75 Q 250 60 465 85" fill="none" stroke="#2563eb" stroke-width="6" stroke-linecap="round"/>\n'
          '  <text x="250" y="80" fill="#1d4ed8" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">B (Notochord)</text>\n'
          '  \n'
          '  <!-- Gut tube -->\n'
          '  <path d="M 40 100 Q 160 110 360 140" fill="none" stroke="#ca8a04" stroke-width="3"/>\n'
          '  <circle cx="360" cy="140" r="4" fill="#a16207"/>\n'
          '  <text x="360" y="158" fill="#a16207" font-size="10" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Anus</text>\n'
          '  \n'
          '  <!-- 3. Pharyngeal Gill Slits (labeled C) -->\n'
          '  <g stroke="#dc2626" stroke-width="3" stroke-linecap="round">\n'
          '    <line x1="120" y1="95" x2="120" y2="120"/>\n'
          '    <line x1="135" y1="95" x2="135" y2="120"/>\n'
          '    <line x1="150" y1="95" x2="150" y2="120"/>\n'
          '    <line x1="165" y1="95" x2="165" y2="120"/>\n'
          '  </g>\n'
          '  <text x="142" y="145" fill="#b91c1c" font-size="10" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">C (Pharyngeal Gill Slits)</text>\n'
          '  \n'
          '  <!-- 4. Post-anal tail (labeled D) -->\n'
          '  <path d="M 360 140 Q 420 160 500 100" fill="none" stroke="#7c3aed" stroke-width="2.5" '
          'stroke-dasharray="3,2"/>\n'
          '  <text x="440" y="160" fill="#6d28d9" font-size="10" font-weight="bold" font-family="system-ui">D '
          '(Post-anal tail)</text>\n'
          '</svg><br>A, B, C এবং D চিহ্নিত গঠনগুলি শনাক্ত করো:',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Given below is the schematic diagram showing the fundamental body plan of a chordate:<br><svg viewBox="0 0 '
          '520 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" class="select-none">\n'
          '  <!-- General chordate fish-like body outline -->\n'
          '  <path d="M 40 100 Q 150 20 400 30 Q 480 70 500 100 Q 480 130 400 170 Q 150 180 40 100 Z" fill="#f0f9ff" '
          'stroke="#0284c7" stroke-width="2.5"/>\n'
          '  \n'
          '  <!-- 1. Nerve cord (Dorsal hollow nerve cord, green, labeled A) -->\n'
          '  <path d="M 90 55 Q 250 40 450 65" fill="none" stroke="#16a34a" stroke-width="4"/>\n'
          '  <text x="250" y="45" fill="#15803d" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">A (Dorsal Hollow Nerve Cord)</text>\n'
          '  \n'
          '  <!-- 2. Notochord (Blue solid rod under nerve cord, labeled B) -->\n'
          '  <path d="M 70 75 Q 250 60 465 85" fill="none" stroke="#2563eb" stroke-width="6" stroke-linecap="round"/>\n'
          '  <text x="250" y="80" fill="#1d4ed8" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">B (Notochord)</text>\n'
          '  \n'
          '  <!-- Gut tube -->\n'
          '  <path d="M 40 100 Q 160 110 360 140" fill="none" stroke="#ca8a04" stroke-width="3"/>\n'
          '  <circle cx="360" cy="140" r="4" fill="#a16207"/>\n'
          '  <text x="360" y="158" fill="#a16207" font-size="10" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Anus</text>\n'
          '  \n'
          '  <!-- 3. Pharyngeal Gill Slits (labeled C) -->\n'
          '  <g stroke="#dc2626" stroke-width="3" stroke-linecap="round">\n'
          '    <line x1="120" y1="95" x2="120" y2="120"/>\n'
          '    <line x1="135" y1="95" x2="135" y2="120"/>\n'
          '    <line x1="150" y1="95" x2="150" y2="120"/>\n'
          '    <line x1="165" y1="95" x2="165" y2="120"/>\n'
          '  </g>\n'
          '  <text x="142" y="145" fill="#b91c1c" font-size="10" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">C (Pharyngeal Gill Slits)</text>\n'
          '  \n'
          '  <!-- 4. Post-anal tail (labeled D) -->\n'
          '  <path d="M 360 140 Q 420 160 500 100" fill="none" stroke="#7c3aed" stroke-width="2.5" '
          'stroke-dasharray="3,2"/>\n'
          '  <text x="440" y="160" fill="#6d28d9" font-size="10" font-weight="bold" font-family="system-ui">D '
          '(Post-anal tail)</text>\n'
          '</svg><br>Identify the labeled structures A, B, C, and D:',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'কর্ডাটার চিত্রে: A হলো পৃষ্ঠীয় ফাঁপা স্নায়ুরজ্জু (সবুজ); B হলো তার ঠিক নিচে অবস্থিত মেসোডার্মাল '
               'নোটোকর্ড (নীল); C হলো গলবিলীয় ফুলকা ছিদ্র; এবং D হলো পায়ুর পেছনের পেশিবহুল লেজ (Post-anal tail)।',
    'expl_en': 'In chordate body organization: A is the dorsal, hollow, single ectodermal nerve cord. B is the dorsal '
               'solid flexible mesodermal notochord underneath the nerve cord. C represents paired pharyngeal gill '
               'slits, and D is the muscular post-anal tail.',
    'id': 'BIO-AK-107',
    'opts': { 'bn': [ 'A = পৃষ্ঠীয় ফাঁপা স্নায়ুরজ্জু (Dorsal hollow nerve cord); B = নোটোকর্ড (Notochord); C = '
                      'গলবিলীয় ফুলকা ছিদ্র (Gill slits); D = পায়ু-পশ্চাৎ পুচ্ছ (Post-anal tail)',
                      'A = নোটোকর্ড; B = নার্ভ কর্ড; C = ফুলকা ছিদ্র; D = পুচ্ছ পাখনা',
                      'A = মেরুদণ্ড; B = সুষুম্নাকাণ্ড; C = শ্বাসনালী; D = পায়ু',
                      'A = পৃষ্ঠীয় রক্তনালী; B = অঙ্কীয় স্নায়ুরজ্জু; C = হৃদপিণ্ড; D = টেলসন'],
              'en': [ 'A = Dorsal hollow nerve cord; B = Notochord; C = Pharyngeal gill slits; D = Post-anal tail',
                      'A = Notochord; B = Nerve cord; C = Gill slits; D = Caudal fin',
                      'A = Vertebral column; B = Spinal cord; C = Trachea; D = Anus',
                      'A = Dorsal vessel; B = Ventral nerve cord; C = Heart; D = Telson']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিডারিয়া পর্বের প্রাণীদের দুটি মৌলিক দৈহিক রূপ লক্ষ্য করো:<br><svg viewBox="0 0 460 210" width="100%" '
          'height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">\n'
          '  <!-- Polyp Form (Hydra / Adamsia) -->\n'
          '  <g transform="translate(40, 20)">\n'
          '    <!-- Cylindrical stalk attached at base -->\n'
          '    <path d="M 40 160 L 40 60 Q 60 70 80 60 L 80 160 Z" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>\n'
          '    <!-- Tentacles directed upwards -->\n'
          '    <path d="M 45 60 Q 30 20 20 10 M 55 63 Q 50 15 60 5 M 65 63 Q 70 15 65 5 M 75 60 Q 90 20 100 10" '
          'fill="none" stroke="#1d4ed8" stroke-width="2.5" stroke-linecap="round"/>\n'
          '    <!-- Mouth on hypostome -->\n'
          '    <circle cx="60" cy="60" r="4" fill="#ef4444"/>\n'
          '    <text x="60" y="75" fill="#dc2626" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Mouth</text>\n'
          '    <text x="60" y="180" fill="#1e40af" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Polyp (A)</text>\n'
          '    <text x="60" y="195" fill="#3b82f6" font-size="9" font-family="system-ui" text-anchor="middle">Sessile '
          '&amp; Cylindrical</text>\n'
          '  </g>\n'
          '\n'
          '  <!-- Medusa Form (Aurelia / Jelly fish) -->\n'
          '  <g transform="translate(260, 20)">\n'
          '    <!-- Umbrella shaped bell -->\n'
          '    <path d="M 20 80 Q 80 15 140 80 Q 80 90 20 80 Z" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>\n'
          '    <!-- Mouth directed downwards on manubrium -->\n'
          '    <rect x="70" y="85" width="20" height="30" fill="#fca5a5" stroke="#b91c1c" stroke-width="1.5"/>\n'
          '    <circle cx="80" cy="115" r="4" fill="#7f1d1d"/>\n'
          '    <text x="80" y="130" fill="#991b1b" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Mouth</text>\n'
          '    <!-- Marginal tentacles hanging down -->\n'
          '    <path d="M 25 82 Q 20 130 15 160 M 45 86 Q 40 130 45 165 M 115 86 Q 120 130 115 165 M 135 82 Q 140 130 '
          '145 160" fill="none" stroke="#e11d48" stroke-width="2" stroke-linecap="round"/>\n'
          '    <text x="80" y="180" fill="#991b1b" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Medusa (B)</text>\n'
          '    <text x="80" y="195" fill="#e11d48" font-size="9" font-family="system-ui" '
          'text-anchor="middle">Free-swimming &amp; Umbrella</text>\n'
          '  </g>\n'
          '</svg><br>দেহরূপ A এবং দেহরূপ B-এর মধ্যে কোন তুলনাটি সঠিক?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Observe the two basic body forms of cnidarians depicted below:<br><svg viewBox="0 0 460 210" width="100%" '
          'height="210" xmlns="http://www.w3.org/2000/svg" class="select-none">\n'
          '  <!-- Polyp Form (Hydra / Adamsia) -->\n'
          '  <g transform="translate(40, 20)">\n'
          '    <!-- Cylindrical stalk attached at base -->\n'
          '    <path d="M 40 160 L 40 60 Q 60 70 80 60 L 80 160 Z" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>\n'
          '    <!-- Tentacles directed upwards -->\n'
          '    <path d="M 45 60 Q 30 20 20 10 M 55 63 Q 50 15 60 5 M 65 63 Q 70 15 65 5 M 75 60 Q 90 20 100 10" '
          'fill="none" stroke="#1d4ed8" stroke-width="2.5" stroke-linecap="round"/>\n'
          '    <!-- Mouth on hypostome -->\n'
          '    <circle cx="60" cy="60" r="4" fill="#ef4444"/>\n'
          '    <text x="60" y="75" fill="#dc2626" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Mouth</text>\n'
          '    <text x="60" y="180" fill="#1e40af" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Polyp (A)</text>\n'
          '    <text x="60" y="195" fill="#3b82f6" font-size="9" font-family="system-ui" text-anchor="middle">Sessile '
          '&amp; Cylindrical</text>\n'
          '  </g>\n'
          '\n'
          '  <!-- Medusa Form (Aurelia / Jelly fish) -->\n'
          '  <g transform="translate(260, 20)">\n'
          '    <!-- Umbrella shaped bell -->\n'
          '    <path d="M 20 80 Q 80 15 140 80 Q 80 90 20 80 Z" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>\n'
          '    <!-- Mouth directed downwards on manubrium -->\n'
          '    <rect x="70" y="85" width="20" height="30" fill="#fca5a5" stroke="#b91c1c" stroke-width="1.5"/>\n'
          '    <circle cx="80" cy="115" r="4" fill="#7f1d1d"/>\n'
          '    <text x="80" y="130" fill="#991b1b" font-size="9" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Mouth</text>\n'
          '    <!-- Marginal tentacles hanging down -->\n'
          '    <path d="M 25 82 Q 20 130 15 160 M 45 86 Q 40 130 45 165 M 115 86 Q 120 130 115 165 M 135 82 Q 140 130 '
          '145 160" fill="none" stroke="#e11d48" stroke-width="2" stroke-linecap="round"/>\n'
          '    <text x="80" y="180" fill="#991b1b" font-size="11" font-weight="bold" font-family="system-ui" '
          'text-anchor="middle">Medusa (B)</text>\n'
          '    <text x="80" y="195" fill="#e11d48" font-size="9" font-family="system-ui" '
          'text-anchor="middle">Free-swimming &amp; Umbrella</text>\n'
          '  </g>\n'
          '</svg><br>Which comparison between Form A and Form B is CORRECT?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'A রূপটি হলো স্থানু ও নলাকার পলিপ (Polyp); B রূপটি হলো ছাতাসদৃশ মুক্ত সাঁতারু মেদুসা (Medusa)।',
    'expl_en': 'Form A is the sessile and cylindrical Polyp with upward mouth and tentacles (Hydra, Adamsia). Form B '
               'is the free-swimming umbrella-like Medusa with downward mouth (Aurelia/Jellyfish).',
    'id': 'BIO-AK-108',
    'opts': { 'bn': [ 'A হলো নিশ্চল নলাকার পলিপ (যেমন হাইড্রা, অ্যাডামসিয়া); B হলো মুক্ত সাঁতারু ছাতার মতো মেদুসা '
                      '(যেমন অরেলিয়া বা জেলিফিশ)',
                      'A হলো মেদুসা এবং B হলো পলিপ',
                      'A যৌন জননে B তৈরি করে এবং B যৌন জননে A তৈরি করে',
                      'A ও B উভয়ই প্রবালের সচল দশা'],
              'en': [ 'Form A is a sessile, cylindrical Polyp (e.g., Hydra, Adamsia); Form B is a free-swimming, '
                      'umbrella-shaped Medusa (e.g., Aurelia)',
                      'Form A is a free-swimming Medusa; Form B is a sessile Polyp',
                      'Form A is formed sexually from Form B; Form B is formed sexually from Form A',
                      'Both Form A and Form B are motile adult stages of corals']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): পরিফেরা পর্বের স্পঞ্জে কোষীয় মাত্রার সংগঠন থাকা সত্ত্বেও এদের কোষগুলির মধ্যে চমৎকার '
          'কার্যগত সমন্বয় দেখা যায়।<br>যুক্তি (R): স্পঞ্জের ফ্ল্যাজেলাযুক্ত কোয়ানোসাইট কোষগুলি অবিরাম জলপ্রবাহ '
          'সৃষ্টি করে যা খাদ্যকণা ও অক্সিজেন ভেতরে নিয়ে আসে এবং বর্জ্য পদার্থ অসকুলাম দিয়ে বাইরে বের করে দেয়।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Sponges (Phylum Porifera) have a cellular level of organization, yet the cells demonstrate '
          'functional coordination.<br>Reason (R): In sponges, the flagellated choanocytes create continuous water '
          'currents that bring food, respiratory oxygen, and carry away metabolic wastes through the osculum.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'কলা না থাকলেও কোয়ানোসাইটের ফ্ল্যাজেলার স্পন্দনে সৃষ্ট জল সংবহন তন্ত্রই সমগ্র স্পঞ্জদেহের খাদ্য, শ্বসন '
               'ও রেচনের মৌলিক সমন্বয় সম্পন্ন করে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'Even without true tissues or nervous coordination, the physical beating of choanocyte flagella drives '
               'the hydrodynamics of the canal system, sustaining nutrition, respiration, and excretion for the entire '
               'cellular collective. (R) correctly explains (A).',
    'id': 'BIO-AK-109',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): টিনোফোরা পর্বের প্রাণীদের নিডারিয়া থেকে সম্পূর্ণ পৃথক করে একটি আলাদা পর্বের মর্যাদা '
          'দেওয়া হয়েছে।<br>যুক্তি (R): টিনোফোরায় নিডোসাইট (নেমাটোসিস্ট) একেবারেই থাকে না; তার পরিবর্তে এদের চলনের '
          'জন্য আটটি সিলিয়াযুক্ত কম্ব প্লেট এবং শিকার ধরতে আঠালো কলোব্লাস্ট কোষ থাকে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Ctenophores are considered distinct from Cnidarians and are given their own separate '
          'phylum.<br>Reason (R): Ctenophores completely lack cnidocytes (nematocysts); instead, they possess eight '
          'ciliated comb plates for locomotion and capture prey using sticky colloblast cells.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'নিডারিয়ার মূল বৈশিষ্ট্য নিডোব্লাস্ট কোষের অনুপস্থিতি এবং আটটি কম্ব প্লেট ও আঠালো কলোব্লাস্ট কোষের '
               'উপস্থিতির কারণেই টিনোফোরাকে পৃথক পর্ব করা হয়েছে। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'Because cnidarians are fundamentally defined by stinging cnidocytes, the absence of cnidocytes '
               'combined with 8 ciliated comb plates and colloblasts necessitated creating Phylum Ctenophora. (R) '
               'correctly explains (A).',
    'id': 'BIO-AK-110',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): ফিতাকৃমির (Taenia) নিজস্ব কোনো পৌষ্টিকনালী বা পরিপাকতন্ত্র থাকে না।<br>যুক্তি (R): '
          'ফিতাকৃমি হলো অন্ত্রের অন্তঃপরজীবী যা পোষকের অন্ত্র থেকে সরাসরি ত্বক ও মাইক্রোট্রিক্সের মাধ্যমে পূর্বে '
          'পরিপাক হওয়া পুষ্টিরস শোষণ করে নেয়।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Tapeworms (Taenia) lack an alimentary canal of their own.<br>Reason (R): Tapeworms are gut '
          'endoparasites whose thin body wall directly absorbs pre-digested nutrients across their microtriches from '
          "the host's intestinal lumen.",
    'exam': 'NEET, AIIMS',
    'expl_bn': 'পোষকের অন্ত্রে সর্বদা সরল পাচিত খাদ্য উপস্থিত থাকায় ফিতাকৃমির পরিপাকতন্ত্র বিলুপ্ত হয়েছে; এরা পুরো '
               'দেহত্বকের মাধ্যমে সরাসরি পুষ্টিরস শোষণ করে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'Endoparasitic flatworms like tapeworms live bathed in host digestive juices. They adaptively lost '
               'their entire gut, absorbing simple sugars and amino acids directly across their surface tegument. (R) '
               'correctly explains (A).',
    'id': 'BIO-AK-111',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): আর্থ্রোপোডা হলো পৃথিবীর সর্বাপেক্ষা সফল এবং সর্বাধিক প্রজাতিসমৃদ্ধ প্রাণী '
          'পর্ব।<br>যুক্তি (R): আর্থ্রোপোডার দেহে হালকা ও জলরোধী কাইটিনযুক্ত বহিঃকঙ্কাল, নমনীয় সন্ধিল উপাঙ্গ এবং '
          'সুবিকশিত সংবেদী অঙ্গ থাকায় এরা প্রায় প্রতিটি বাস্তুতন্ত্রে অভিযোজিত হতে পেরেছে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Arthropoda is the most taxonomically diverse and ecologically successful animal phylum on '
          'Earth.<br>Reason (R): Arthropods possess a lightweight, waterproof chitinous exoskeleton, jointed '
          'appendages, and highly developed sensory systems that enable adaptation to diverse ecological niches.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'জলরোধী কাইটিন বহিঃকঙ্কাল স্থলভাগে জলক্ষয় রোধ করে এবং সন্ধিল উপাঙ্গ ও ওড়ার ক্ষমতা এদের পৃথিবীর '
               'সর্বত্র আধিপত্য বিস্তার করতে সাহায্য করেছে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'The chitinous cuticle protects against desiccation on land, jointed appendages provide versatile '
               'locomotion, and flight in insects opened aerial niches, driving immense evolutionary radiation. (R) '
               'correctly explains (A).',
    'id': 'BIO-AK-112',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): অন্য যেকোনো নন-কর্ডাটা পর্বের তুলনায় একাইনোডার্মাটার সাথে কর্ডাটার জাতিজনি বা '
          'বিবর্তনীয় ঘনিষ্ঠতা সবচেয়ে বেশি।<br>যুক্তি (R): একাইনোডার্মাটা এবং কর্ডাটা উভয় পর্বেই ডিউটেরোস্টোম '
          '(Deuterostome) ভ্রূণ বিকাশ দেখা যায় (ব্লাস্টোপোর থেকে প্রথমে পায়ু গঠিত হয় এবং মুখ পরে তৈরি হয়)।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Echinoderms show closer phylogenetic affinity to chordates than any other non-chordate '
          'invertebrate phylum.<br>Reason (R): Both echinoderms and chordates share deuterostome embryonic development '
          '(blastopore forms the anus first; mouth develops secondarily) and enterocoelic or mesodermal coelom '
          'formation.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'ভ্রূণের ব্লাস্টোপোর থেকে পায়ু তৈরি হওয়া (Deuterostomia) এবং মেসোডার্মাল সিলোম সৃষ্টির প্রক্রিয়ায় '
               'একাইনোডার্মাটা কর্ডাটার নিকটতম আত্মীয়। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'Echinoderms, Hemichordates, and Chordates form the monophyletic clade Deuterostomia based on embryonic '
               'cleavage and blastopore fate (anus first, mouth second), linking them evolutionarily. (R) correctly '
               'explains (A).',
    'id': 'BIO-AK-113',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): অস্থিময় মাছেরা (Osteichthyes) পেশিশক্তি ব্যয় না করেই জলের নির্দিষ্ট গভীরতায় '
          'স্থিরভাবে ভেসে থাকতে পারে।<br>যুক্তি (R): অস্থিময় মাছের দেহে গ্যাসপূর্ণ পটকা বা এয়ার ব্লাডার থাকে যা এদের '
          'হাইড্রোস্ট্যাটিক প্লবতা নিখুঁতভাবে নিয়ন্ত্রণ করে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Osteichthyes (bony fishes) can stay motionless suspended at a chosen depth in water without '
          'expending muscular energy.<br>Reason (R): Osteichthyes possess a gas-filled swim bladder (air bladder) that '
          'regulates hydrostatic buoyancy.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'পটকার গ্যাসের পরিমাণ কমিয়ে-বাড়িয়ে মাছেরা জলের যেকোনো স্তরে প্লবতা বজায় রেখে অনায়াসে ভেসে থাকতে '
               'পারে। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'The air bladder secretes or absorbs gas to adjust overall density to match water density at a given '
               'depth, allowing neutral buoyancy without continuous swimming. (R) correctly explains (A).',
    'id': 'BIO-AK-114',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): আকাশে দ্রুত উড্ডয়নের সময় পাখিদের শ্বসন অত্যন্ত উচ্চক্ষমতাসম্পন্ন ও কার্যকর '
          'হয়।<br>যুক্তি (R): পাখিদের ফুসফুসের সাথে যুক্ত পাতলা প্রাচীরযুক্ত বায়ুথলি (Air sacs) শ্বাসগ্রহণ ও '
          'শ্বাসত্যাগ উভয় সময়েই ফুসফুসের ভেতর দিয়ে অবিরাম একমুখী বাতাস চলাচল নিশ্চিত করে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Respiration in birds is remarkably efficient during high-altitude flight.<br>Reason (R): '
          'Birds possess thin-walled air sacs connected to their lungs that ensure continuous unidirectional airflow '
          'across parabronchi during both inhalation and exhalation.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'পাখির অতিরিক্ত ৯টি বায়ুথলি ফুসফুসে অক্সিজেনযুক্ত বাতাসের একমুখী অবিরাম প্রবাহ বজায় রাখে যা উড্ডয়নের '
               'বিপুল শক্তির চাহিদা পূরণ করে। অতএব (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'Air sacs function as bellows, providing continuous cross-current oxygen exchange in parabronchi with '
               'no residual stagnant air, meeting the intense aerobic metabolic demand of flight. (R) correctly '
               'explains (A).',
    'id': 'BIO-AK-115',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিশ্চিত বিবৃতি (A): তিমি, ডলফিন এবং বাদুড়কে মানুষের সাথে একই শ্রেণি ম্যামালিয়া বা স্তন্যপায়ীর '
          'অন্তর্ভুক্ত করা হয়েছে।<br>যুক্তি (R): তিমি, ডলফিন এবং বাদুড় সকলের দেহেই শাবককে দুগ্ধপান করানোর '
          'স্তনগ্রন্থি, লোম এবং চার-প্রকোষ্ঠী হৃদপিণ্ড উপস্থিত থাকে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Assertion (A): Whales, dolphins, and bats are grouped alongside humans and dogs in Class '
          'Mammalia.<br>Reason (R): Whales, dolphins, and bats possess mammary glands to nourish their young with milk '
          'and have hair and a four-chambered heart.',
    'exam': 'NEET, AIIMS',
    'expl_bn': 'জলচর বা খেচর যাই হোক না কেন, স্তনগ্রন্থি এবং শাবককে দুধ খাওয়ানোর মৌলিক বৈশিষ্ট্যের কারণেই তিমি ও '
               'বাদুড়কে স্তন্যপায়ীর দলে রাখা হয়েছে। সুতরাং (R) হলো (A)-এর সঠিক ব্যাখ্যা।',
    'expl_en': 'Despite secondary adaptations for swimming (whales) and flying (bats), their core diagnostic '
               'synapomorphies (mammary glands, hair, endothermy, 4-chambered heart, vivipary) place them '
               'unequivocally in Class Mammalia. (R) correctly explains (A).',
    'id': 'BIO-AK-116',
    'opts': { 'bn': [ '(A) এবং (R) উভয়ই সত্য, এবং (R) হলো (A)-এর সঠিক ব্যাখ্যা',
                      '(A) এবং (R) উভয়ই সত্য, কিন্তু (R), (A)-এর সঠিক ব্যাখ্যা নয়',
                      '(A) সত্য, কিন্তু (R) মিথ্যা',
                      '(A) মিথ্যা, কিন্তু (R) সত্য'],
              'en': [ 'Both (A) and (R) are true, and (R) is the correct explanation of (A)',
                      'Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)',
                      '(A) is true, but (R) is false',
                      '(A) is false, but (R) is true']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'বিবৃতি I: মুক্ত সংবহনতন্ত্রে হৃদপিণ্ড থেকে রক্ত সরাসরি দেহগহ্বরে পাম্প হয় এবং কোষ ও কলা সরাসরি রক্তে '
          'নিমজ্জিত থাকে।<br>বিবৃতি II: বদ্ধ সংবহনতন্ত্রে রক্ত সর্বদা সুনির্দিষ্ট নালীজালকের (ধমনী, শিরা ও রক্তজালক) '
          'মধ্য দিয়ে প্রবাহিত হয়।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Statement I: In open circulatory systems, blood is pumped out of the heart and the cells and tissues are '
          'directly bathed in it.<br>Statement II: In closed circulatory systems, blood is circulated through a '
          'continuous circuit of vessels of varying diameters (arteries, veins and capillaries).',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'উভয় বিবৃতিই NCERT-এর রক্ত সংবহনতন্ত্রের সংজ্ঞা অনুসারে সম্পূর্ণ সঠিক।',
    'expl_en': 'Both statements are direct definitions from NCERT Section 4.1.2 on Circulatory System patterns.',
    'id': 'BIO-AK-117',
    'opts': { 'bn': [ 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল',
                      'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল',
                      'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক'],
              'en': [ 'Both Statement I and Statement II are correct',
                      'Both Statement I and Statement II are incorrect',
                      'Statement I is correct but Statement II is incorrect',
                      'Statement I is incorrect but Statement II is correct']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'বিবৃতি I: অ্যাসকেলমিন্থেস হলো সিউডোসিলোমেট কারণ এদের দেহগহ্বর মেসোডার্ম দ্বারা সম্পূর্ণ আবৃত নয়, বরং '
          'মেসোডার্মের থলি হিসেবে থাকে।<br>বিবৃতি II: অ্যানেলিডা, আর্থ্রোপোডা, মোলাস্কা, একাইনোডার্মাটা, হெமிকর্ডাটা '
          'এবং কর্ডাটা প্রত্যেকেই প্রকৃত সিলোমেট (ইউসিলোমেট)।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Statement I: Aschelminthes are pseudocoelomates because the body cavity is not lined by mesoderm, but '
          'exists as scattered pouches.<br>Statement II: Annelids, Arthropods, Molluscs, Echinoderms, Hemichordates, '
          'and Chordates are all true coelomates (eucoelomates).',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'উভয় বিবৃতিই সঠিক। অ্যাসকেলমিন্থেস একমাত্র সিউডোসিলোমেট এবং অ্যানেলিডা থেকে কর্ডাটা পর্যন্ত সকল পর্বই '
               'প্রকৃত সিলোমেট।',
    'expl_en': 'Both statements are completely correct. Aschelminthes is the only pseudocoelomate phylum; all phyla '
               'from Annelida onwards possess a true coelom.',
    'id': 'BIO-AK-118',
    'opts': { 'bn': [ 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল',
                      'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল',
                      'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক'],
              'en': [ 'Both Statement I and Statement II are correct',
                      'Both Statement I and Statement II are incorrect',
                      'Statement I is correct but Statement II is incorrect',
                      'Statement I is incorrect but Statement II is correct']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'বিবৃতি I: নেরিস হলো একটি জলজ অ্যানেলিড যা একলিঙ্গ এবং সাঁতার কাটার জন্য প্যারাপোডিয়া থাকে।<br>বিবৃতি II: '
          'কেঁচো এবং জোঁক হলো উভলিঙ্গ অ্যানেলিড যাদের কোনো প্যারাপোডিয়া থাকে না।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Statement I: Nereis is an aquatic annelid that is dioecious and possesses parapodia for '
          'swimming.<br>Statement II: Earthworms and leeches are monoecious annelids that lack parapodia.',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'উভয় বিবৃতিই সঠিক। নেরিস একলিঙ্গ ও প্যারাপোডিয়াযুক্ত; কিন্তু কেঁচো ও জোঁক উভলিঙ্গ।',
    'expl_en': 'Both statements are accurate facts from NCERT Annelida section.',
    'id': 'BIO-AK-119',
    'opts': { 'bn': [ 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল',
                      'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল',
                      'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক'],
              'en': [ 'Both Statement I and Statement II are correct',
                      'Both Statement I and Statement II are incorrect',
                      'Statement I is correct but Statement II is incorrect',
                      'Statement I is incorrect but Statement II is correct']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'বিবৃতি I: সমস্ত জীবিত সাইক্লোস্টোমদের চোয়াল এবং যুগ্ম পাখনার অভাব থাকে।<br>বিবৃতি II: সাইক্লোস্টোমদের খুলি '
          '(cranium) এবং কশেরুকা তরুণাস্থিময় কঙ্কাল দ্বারা গঠিত।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Statement I: All living cyclostomes lack jaws and paired fins.<br>Statement II: Cyclostomes have a '
          'cartilaginous cranium and vertebral column.',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'উভয় বিবৃতিই সঠিক। সাইক্লোস্টোমদের কোনো চোয়াল ও যুগ্ম পাখনা থাকে না এবং এদের খুলি ও মেরুদণ্ড '
               'তরুণাস্থিময়।',
    'expl_en': 'Both statements are exact facts from NCERT Section 4.2.11.1 (Class Cyclostomata).',
    'id': 'BIO-AK-120',
    'opts': { 'bn': [ 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল',
                      'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল',
                      'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক'],
              'en': [ 'Both Statement I and Statement II are correct',
                      'Both Statement I and Statement II are incorrect',
                      'Statement I is correct but Statement II is incorrect',
                      'Statement I is incorrect but Statement II is correct']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'বিবৃতি I: তরুণাস্থিময় মাছে (Chondrichthyes) নিষেক অভ্যন্তরীণ এবং এদের অনেকেই জরায়ুজ বা সরাসরি বাচ্চা '
          'প্রসব করে।<br>বিবৃতি II: অস্থিময় মাছে (Osteichthyes) নিষেক প্রধানত বাহ্যিক এবং এরা বেশিরভাগই ডিম্বজ বা ডিম '
          'পাড়ে।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Statement I: In Chondrichthyes, fertilization is internal and many of them are viviparous.<br>Statement II: '
          'In Osteichthyes, fertilization is usually external and they are mostly oviparous.',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'উভয় বিবৃতিই সঠিক। হাঙ্গরে অভ্যন্তরীণ নিষেক ও সন্তান প্রসব দেখা যায়; কিন্তু রুই-কাতলায় জলে বহিঃনিষেক '
               'ঘটে ও ডিম পাড়ে।',
    'expl_en': 'Both statements are correct NCERT contrasts between cartilaginous and bony fishes.',
    'id': 'BIO-AK-121',
    'opts': { 'bn': [ 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল',
                      'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল',
                      'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক'],
              'en': [ 'Both Statement I and Statement II are correct',
                      'Both Statement I and Statement II are incorrect',
                      'Statement I is correct but Statement II is incorrect',
                      'Statement I is incorrect but Statement II is correct']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'বিবৃতি I: সরীসৃপ, পাখি এবং স্তন্যপায়ী প্রাণীদের ক্ষেত্রে নিষেক সর্বদা অভ্যন্তরীণ হয়।<br>বিবৃতি II: উভচর '
          'এবং অধিকাংশ অস্থিময় মাছের ক্ষেত্রে বহিঃনিষেক জলের মধ্যে সম্পন্ন হয়।',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Statement I: In reptiles, birds, and mammals, fertilization is strictly internal.<br>Statement II: In '
          'amphibians and majority of bony fishes, fertilization is external and occurs in water.',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'উভয় বিবৃতিই সঠিক। স্থলজ উন্নত মেরুদণ্ডীদের অভ্যন্তরীণ নিষেক হয়, আর ব্যাঙ ও অস্থিময় মাছেরা জলে ডিম ও '
               'শুক্রাণু ছেড়ে বহিঃনিষেক ঘটায়।',
    'expl_en': 'Both statements are accurate. Terrestrial amniotes (Reptiles, Aves, Mammals) require internal '
               'fertilization; aquatic anamniotes (Amphibia, Osteichthyes) utilize external fertilization in water.',
    'id': 'BIO-AK-122',
    'opts': { 'bn': [ 'বিবৃতি I এবং বিবৃতি II উভয়ই সঠিক',
                      'বিবৃতি I এবং বিবৃতি II উভয়ই ভুল',
                      'বিবৃতি I সঠিক কিন্তু বিবৃতি II ভুল',
                      'বিবৃতি I ভুল কিন্তু বিবৃতি II সঠিক'],
              'en': [ 'Both Statement I and Statement II are correct',
                      'Both Statement I and Statement II are incorrect',
                      'Statement I is correct but Statement II is incorrect',
                      'Statement I is incorrect but Statement II is correct']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'কলাম-I (প্রাণী)-এর সাথে কলাম-II (রেচন অঙ্গ) মেলাও:<br>A. প্ল্যানেরিয়া<br>B. কেঁচো<br>C. চিংড়ি<br>D. '
          'আরশোলা<br>1. সবুজ গ্রন্থি (গ্রিন গ্ল্যান্ড)<br>2. শিখা কোষ (ফ্লেম সেল)<br>3. ম্যালপিজিয়ান নালিকা<br>4. '
          'নেফ্রিডিয়া',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Match Column-I (Animal) with Column-II (Excretory structure):<br>A. Planaria<br>B. Earthworm<br>C. '
          'Prawn<br>D. Cockroach<br>1. Green glands (Antennal glands)<br>2. Flame cells (Protonephridia)<br>3. '
          'Malpighian tubules<br>4. Nephridia',
    'exam': 'NEET, CUET',
    'expl_bn': 'প্ল্যানেরিয়া = শিখা কোষ (A-2); কেঁচো = নেফ্রিডিয়া (B-4); চিংড়ি = সবুজ গ্রন্থি (C-1); আরশোলা = '
               'ম্যালপিজিয়ান নালিকা (D-3)।',
    'expl_en': 'Planaria = Flame cells (A-2); Earthworm = Nephridia (B-4); Prawn = Green glands (C-1); Cockroach = '
               'Malpighian tubules (D-3).',
    'id': 'BIO-AK-123',
    'opts': { 'bn': ['A-2, B-4, C-1, D-3', 'A-4, B-2, C-1, D-3', 'A-2, B-1, C-4, D-3', 'A-3, B-4, C-1, D-2'],
              'en': ['A-2, B-4, C-1, D-3', 'A-4, B-2, C-1, D-3', 'A-2, B-1, C-4, D-3', 'A-3, B-4, C-1, D-2']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'কলাম-I (পর্ব)-এর সাথে কলাম-II (স্বতন্ত্র বৈশিষ্ট্য) মেলাও:<br>A. পরিফেরা<br>B. নিডারিয়া<br>C. '
          'টিনোফোরা<br>D. একাইনোডার্মাটা<br>1. চলনের জন্য কম্ব প্লেট ও বায়োলুমিনেসেন্স<br>2. নালিপদযুক্ত জলসংবহন '
          'তন্ত্র<br>3. ক্যানাল সিস্টেমে কোয়ানোসাইট কোষ<br>4. নেমাটোসিস্টযুক্ত নিডোসাইট',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Match Column-I (Phylum) with Column-II (Hallmark feature):<br>A. Porifera<br>B. Cnidaria<br>C. '
          'Ctenophora<br>D. Echinodermata<br>1. Comb plates for locomotion and bioluminescence<br>2. Water vascular '
          'system with tube feet<br>3. Choanocytes lining canal system<br>4. Cnidocytes containing nematocysts',
    'exam': 'NEET, CUET',
    'expl_bn': 'পরিফেরা = কোয়ানোসাইট (A-3); নিডারিয়া = নিডোসাইট (B-4); টিনোফোরা = কম্ব প্লেট (C-1); একাইনোডার্মাটা = '
               'জলসংবহন তন্ত্র (D-2)।',
    'expl_en': 'Porifera = Choanocytes (A-3); Cnidaria = Cnidocytes (B-4); Ctenophora = Comb plates (C-1); '
               'Echinodermata = Water vascular system (D-2).',
    'id': 'BIO-AK-124',
    'opts': { 'bn': ['A-3, B-4, C-1, D-2', 'A-4, B-3, C-1, D-2', 'A-3, B-1, C-4, D-2', 'A-2, B-4, C-1, D-3'],
              'en': ['A-3, B-4, C-1, D-2', 'A-4, B-3, C-1, D-2', 'A-3, B-1, C-4, D-2', 'A-2, B-4, C-1, D-3']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'কলাম-I (বৈজ্ঞানিক নাম)-এর সাথে কলাম-II (সাধারণ নাম) মেলাও:<br>A. Physalia<br>B. Pennatula<br>C. '
          'Gorgonia<br>D. Meandrina<br>1. সি-ফ্যান (Sea-fan)<br>2. ব্রেন কোরাল (Brain coral)<br>3. পর্তুগিজ '
          'ম্যান-অফ-ওয়ার<br>4. সি-পেন (Sea-pen)',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Match Column-I (Scientific name) with Column-II (Common name):<br>A. Physalia<br>B. Pennatula<br>C. '
          'Gorgonia<br>D. Meandrina<br>1. Sea-fan<br>2. Brain coral<br>3. Portuguese man-of-war<br>4. Sea-pen',
    'exam': 'NEET, CUET',
    'expl_bn': 'Physalia = পর্তুগিজ ম্যান-অফ-ওয়ার (A-3); Pennatula = সি-পেন (B-4); Gorgonia = সি-ফ্যান (C-1); '
               'Meandrina = ব্রেন কোরাল (D-2)।',
    'expl_en': 'Physalia = Portuguese man-of-war (A-3); Pennatula = Sea-pen (B-4); Gorgonia = Sea-fan (C-1); Meandrina '
               '= Brain coral (D-2).',
    'id': 'BIO-AK-125',
    'opts': { 'bn': ['A-3, B-4, C-1, D-2', 'A-3, B-1, C-4, D-2', 'A-4, B-3, C-1, D-2', 'A-2, B-4, C-1, D-3'],
              'en': ['A-3, B-4, C-1, D-2', 'A-3, B-1, C-4, D-2', 'A-4, B-3, C-1, D-2', 'A-2, B-4, C-1, D-3']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'কলাম-I (প্রাণী)-এর সাথে কলাম-II (হৃদপিণ্ডের গঠন) মেলাও:<br>A. রুই মাছ (Labeo)<br>B. ব্যাঙ (Rana)<br>C. '
          'কুমির (Crocodilus)<br>D. পায়রা (Columba)<br>1. ৩-প্রকোষ্ঠী (দুটি অলিন্দ, একটি নিলয়)<br>2. ২-প্রকোষ্ঠী '
          '(একটি অলিন্দ, একটি নিলয়)<br>3. ৪-প্রকোষ্ঠী (সরীসৃপের মধ্যে ব্যতিক্রম)<br>4. ৪-প্রকোষ্ঠী (উষ্ণশোণিত পক্ষী)',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Match Column-I (Animal) with Column-II (Heart structure):<br>A. Rohu (Labeo)<br>B. Frog (Rana)<br>C. '
          'Crocodile (Crocodilus)<br>D. Pigeon (Columba)<br>1. 3-chambered (two auricles, one ventricle)<br>2. '
          '2-chambered (one auricle, one ventricle)<br>3. 4-chambered with complete ventricular septum<br>4. '
          '4-chambered with right systemic arch',
    'exam': 'NEET, CUET',
    'expl_bn': 'মাছ = ২ প্রকোষ্ঠী (A-2); উভচর = ৩ প্রকোষ্ঠী (B-1); কুমির = ৪ প্রকোষ্ঠী (C-3); পাখি = ৪ প্রকোষ্ঠী '
               '(D-4)।',
    'expl_en': 'Fish (Rohu) = 2-chambered; Amphibian (Frog) = 3-chambered; Crocodile = 4-chambered; Bird (Pigeon) = '
               '4-chambered.',
    'id': 'BIO-AK-126',
    'opts': { 'bn': ['A-2, B-1, C-3, D-4', 'A-1, B-2, C-3, D-4', 'A-2, B-3, C-1, D-4', 'A-3, B-1, C-2, D-4'],
              'en': ['A-2, B-1, C-3, D-4', 'A-1, B-2, C-3, D-4', 'A-2, B-3, C-1, D-4', 'A-3, B-1, C-2, D-4']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের কোন প্রাণীটি শীতলশোণিত (poikilothermous), যার ত্বক শুষ্ক ও এপিডার্মাল আঁশযুক্ত এবং হৃদপিণ্ড '
          '৪-প্রকোষ্ঠ বিশিষ্ট?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Which of the following animals is cold-blooded (poikilothermous) with dry cornified skin, epidermal scales, '
          'and a 4-chambered heart?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'কুমির একটি সরীসৃপ হওয়ায় শীতলশোণিত ও আঁশযুক্ত ত্বকবিশিষ্ট, তবে ব্যতিক্রমীভাবে এর হৃদপিণ্ড '
               '৪-প্রকোষ্ঠী।',
    'expl_en': 'Crocodiles are reptiles (hence poikilothermous with dry cornified scutes), but uniquely possess a '
               '4-chambered heart.',
    'id': 'BIO-AK-127',
    'opts': { 'bn': ['কুমির (Crocodilus)', 'উটপাখি', 'প্লাটিপাস', 'সালামান্ডার'],
              'en': ['Crocodilus (Crocodile)', 'Struthio (Ostrich)', 'Ornithorhynchus', 'Salamandra']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'নিচের বক্তব্যগুলি বিবেচনা করো:<br>(i) সমস্ত মেরুদণ্ডী প্রাণীই কর্ডাট।<br>(ii) ইউরোকর্ডাটাতে নোটোকর্ড মাথা '
          'থেকে লেজ পর্যন্ত থাকে এবং সারাজীবন স্থায়ী হয়।<br>(iii) সাইক্লোস্টোমদের চোয়ালবিহীন চোষক প্রকৃতির মুখ '
          'থাকে।<br>(iv) তরুণাস্থিময় মাছে কানকো (operculum) দ্বারা ফুলকা আবৃত থাকে।<br>উপরের কোন বক্তব্যগুলি মিথ্যা '
          '(FALSE)?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Read the following statements:<br>(i) All vertebrates are chordates.<br>(ii) In Urochordates, notochord '
          'extends from head to tail and persists throughout life.<br>(iii) Cyclostomes have an unjawed circular '
          'sucking mouth.<br>(iv) Cartilaginous fishes have operculum covering their gills.<br>Which of the above '
          'statements are FALSE?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'বিবৃতি (ii) মিথ্যা কারণ এটি সেফালোকর্ডাটার বৈশিষ্ট্য; এবং বিবৃতি (iv) মিথ্যা কারণ হাঙ্গরের কোনো কানকো '
               'থাকে না। সুতরাং (ii) ও (iv) মিথ্যা।',
    'expl_en': 'Statement (ii) is false because that describes Cephalochordates (in Urochordates, notochord is only in '
               'larval tail). Statement (iv) is false because Chondrichthyes lack an operculum. Statements (i) and '
               '(iii) are true.',
    'id': 'BIO-AK-128',
    'opts': { 'bn': ['(ii) এবং (iv) মিথ্যা', '(i) এবং (iii) মিথ্যা', 'কেবল (iv) মিথ্যা', 'সবকটিই মিথ্যা'],
              'en': ['(ii) and (iv) are false', '(i) and (iii) are false', 'Only (iv) is false', 'All are false']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'প্রদত্ত প্রাণীগুলির মধ্যে কতগুলি পূর্ণাঙ্গ দশায় দ্বিপার্শ্বীয় প্রতিসাম্য (Bilateral symmetry) প্রদর্শন '
          'করে?<br>[Asterias, Adamsia, Nereis, Pila, Octopus, Pleurobrachia, Fasciola, Sycon]',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'How many of the following animals possess bilateral symmetry as adults?<br>[Asterias, Adamsia, Nereis, '
          'Pila, Octopus, Pleurobrachia, Fasciola, Sycon]',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'দ্বিপার্শ্বীয় প্রতিসম প্রাণী হলো ৪টি: Nereis, Pila, Octopus এবং Fasciola। বাকিগুলি অরীয় বা অপ্রতিসম।',
    'expl_en': 'Adult Asterias = radial; Adamsia = radial; Pleurobrachia = radial; Sycon = asymmetrical. Nereis '
               '(annelid), Pila (mollusc), Octopus (mollusc), and Fasciola (flatworm) = 4 animals with bilateral '
               'symmetry.',
    'id': 'BIO-AK-129',
    'opts': { 'bn': ['৪টি (Nereis, Pila, Octopus, Fasciola)', '৩টি', '৫টি', '৬টি'],
              'en': ['4 (Nereis, Pila, Octopus, Fasciola)', '3', '5', '6']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'প্রদত্ত গোষ্ঠীগুলির মধ্যে কোনগুলি সম্পূর্ণ বা নিরঙ্কুশভাবে সামুদ্রিক (Exclusively marine), যাদের কোনো মিষ্ট '
          'জলের প্রজাতি নেই?<br>[Porifera, Ctenophora, Echinodermata, Cnidaria, Protochordata]',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'How many of the following organisms are exclusively marine without any known freshwater '
          'representatives?<br>[Porifera, Ctenophora, Echinodermata, Cnidaria, Protochordata (Urochordata and '
          'Cephalochordata)]',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'NCERT অনুসারে Ctenophora, Echinodermata এবং Protochordata হলো নিরঙ্কুশভাবে সামুদ্রিক (exclusively '
               'marine)। স্পঞ্জিলা (স্পঞ্জ) ও হাইড্রা (নিডারিয়া) মিষ্ট জলে থাকে।',
    'expl_en': 'Porifera has Spongilla (freshwater). Cnidaria has Hydra (freshwater). Ctenophora, Echinodermata, and '
               'Protochordata are all explicitly highlighted in NCERT as exclusively marine.',
    'id': 'BIO-AK-130',
    'opts': { 'bn': [ '৩টি গোষ্ঠী: Ctenophora, Echinodermata এবং Protochordata',
                      'সবকটি ৫টি গোষ্ঠী',
                      'কেবল একাইনোডার্মাটা',
                      '২টি গোষ্ঠী: পরিফেরা ও নিডারিয়া'],
              'en': [ '3 groups: Ctenophora, Echinodermata, and Protochordata',
                      'All 5 groups',
                      'Only Echinodermata',
                      '2 groups: Porifera and Cnidaria']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'অমেরুদণ্ডী হওয়া সত্ত্বেও নিচের কোন প্রাণীর দেহে উন্নত বদ্ধ রক্ত সংবহনতন্ত্র (Closed circulatory system) '
          'বিদ্যমান?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Which of the following animals has a closed circulatory system despite lacking a vertebral column?',
    'exam': 'NEET, CUET',
    'expl_bn': 'কেঁচো এবং সেফালোপড মোলাস্কা (যেমন স্কুইড ও অক্টোপাস)-র রক্ত সংবহনতন্ত্র সম্পূর্ণ বদ্ধ প্রকৃতির।',
    'expl_en': 'Annelids (earthworm) and cephalopod molluscs (Squid, Octopus) have evolved a closed circulatory system '
               'where blood is confined to continuous vessels.',
    'id': 'BIO-AK-131',
    'opts': { 'bn': [ 'কেঁচো (Pheretima) এবং স্কুইড/অক্টোপাস (Cephalopod)',
                      'আরশোলা এবং চিংড়ি',
                      'শামুক এবং ঝিনুক',
                      'মাকড়সা এবং কাঁকড়া'],
              'en': [ 'Earthworm (Pheretima) and Squid/Octopus',
                      'Cockroach and Prawn',
                      'Snail and Clam',
                      'Spider and Crab']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'বর্তমান প্রাণীজগতের মধ্যে সবচেয়ে বৃহৎ ডিম কোন পাখিটির?',
    'correct': 0,
    'difficulty': 'Easy',
    'en': 'Which bird possesses the largest egg in the living animal kingdom?',
    'exam': 'NEET, CUET',
    'expl_bn': 'উটপাখির ডিম হলো বর্তমান জীবজগতের বৃহত্তম একক কোষ ও বৃহত্তম ডিম।',
    'expl_en': 'The ostrich egg is the largest single biological cell in the contemporary living world.',
    'id': 'BIO-AK-132',
    'opts': { 'bn': ['উটপাখি বা অস্ট্রিচ (Struthio camelus)', 'পেঙ্গুইন', 'ময়ূর', 'শকুন'],
              'en': [ 'Struthio camelus (Ostrich)',
                      'Aptenodytes (Penguin)',
                      'Pavo cristatus (Peacock)',
                      'Neophron (Vulture)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'অধিকাংশ সরীসৃপ ডিম্বজ হলেও নিচের কোনটি ব্যতিক্রমীভাবে জরায়ুজ বা বাচ্চা প্রসবকারী সরীসৃপ?',
    'correct': 0,
    'difficulty': 'Medium',
    'en': 'Which of the following represents a viviparous reptile?',
    'exam': 'NEET, CUET',
    'expl_bn': 'ভাইপার (চন্দ্রবোড়া) সাপ ডিম পাড়ে না, এটি সরাসরি জীবন্ত বাচ্চা প্রসব করে।',
    'expl_en': 'Most reptiles are oviparous, but vipers (Vipera russelli) are ovoviviparous/viviparous, retaining eggs '
               'internally and giving birth to active young ones.',
    'id': 'BIO-AK-133',
    'opts': { 'bn': ['ভাইপার বা চন্দ্রবোড়া সাপ (Vipera)', 'কুমির', 'কচ্ছপ', 'গিরগিটি'],
              'en': ['Vipera (Viper)', 'Crocodilus (Crocodile)', 'Chelone (Turtle)', 'Calotes (Garden lizard)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'প্রদত্ত চারটি প্রাণী বিবেচনা করো:<br>১. গোলকৃমি (Ascaris)<br>২. কেঁচো (Pheretima)<br>৩. কাঁকড়া '
          '(Cancer)<br>৪. তারা মাছ (Asterias)<br>এদের মধ্যে কোনটিতে প্রকৃত মেটামেরিক খণ্ডায়ন দেখা যায়?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Consider the following four animals:<br>1. Roundworm (Ascaris)<br>2. Earthworm (Pheretima)<br>3. Crab '
          '(Cancer)<br>4. Starfish (Asterias)<br>Which of these have true metameric segmentation?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'প্রকৃত মেটামেরিজম কেবলমাত্র অ্যানেলিডা (কেঁচো) এবং আর্থ্রোপোডা (কাঁকড়া)-র মধ্যে সীমাবদ্ধ।',
    'expl_en': 'True metameric segmentation is restricted to Annelida (earthworm), Arthropoda (crab), and Chordata. '
               'Roundworms and starfish lack metamerism.',
    'id': 'BIO-AK-134',
    'opts': { 'bn': ['২ এবং ৩ (কেঁচো এবং কাঁকড়া)', 'কেবল ১ ও ২', 'কেবল ৩ ও ৪', '১, ২ এবং ৩'],
              'en': ['2 and 3 (Earthworm and Crab)', '1 and 2 only', '3 and 4 only', '1, 2, and 3']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'},
  { 'bn': 'আদিম মাছ থেকে স্তন্যপায়ী পর্যন্ত মেরুদণ্ডীদের হৃদপিণ্ডের প্রকোষ্ঠের সঠিক বিবর্তনীয় ধারা কোনটি?',
    'correct': 0,
    'difficulty': 'Hard',
    'en': 'Which of the following represents the correct evolutionary sequence of heart chambers in vertebrates from '
          'ancestral fishes to mammals?',
    'exam': 'NEET, AIIMS, CUET',
    'expl_bn': 'হৃদপিণ্ডের বিবর্তন ঘটেছে মাছের ২-প্রকোষ্ঠী একক সংবহন থেকে উভচরের ৩-প্রকোষ্ঠী, সরীসৃপের আংশিক '
               '৪-প্রকোষ্ঠী এবং পাখি ও স্তন্যপায়ীর সম্পূর্ণ পৃথক ৪-প্রকোষ্ঠী দ্বৈত সংবহনতন্ত্রে।',
    'expl_en': 'Vertebrate circulatory evolution progressed from a 2-chambered single circulation heart in fishes to a '
               '3-chambered transitional heart in amphibians, transitional septation in reptiles, and completely '
               'separated 4-chambered double circulation in homeothermic birds and mammals.',
    'id': 'BIO-AK-135',
    'opts': { 'bn': [ 'মাছ (২-প্রকোষ্ঠী, একক ভেনাস সংবহন) → উভচর (৩-প্রকোষ্ঠী, ১টি নিলয়) → সরীসৃপ (অসম্পূর্ণ '
                      '৪-প্রকোষ্ঠী; কুমিরে সম্পূর্ণ ৪-প্রকোষ্ঠী) → পাখি ও স্তন্যপায়ী (সম্পূর্ণ পৃথক ৪-প্রকোষ্ঠী, '
                      'দ্বি-সংবহন)',
                      'মাছ (৩-প্রকোষ্ঠী) → উভচর (২-প্রকোষ্ঠী) → সরীসৃপ (৪-প্রকোষ্ঠী)',
                      'উভচর (২-প্রকোষ্ঠী) → সরীসৃপ (৩-প্রকোষ্ঠী) → পাখি (৪-প্রকোষ্ঠী)',
                      'মাছ (২-প্রকোষ্ঠী) → সরীসৃপ (৩-প্রকোষ্ঠী) → উভচর (৪-প্রকোষ্ঠী)'],
              'en': [ 'Fishes (2-chambered, single venous circulation) → Amphibians (3-chambered with 1 ventricle) → '
                      'Reptiles (incomplete 4-chambered; 4-chambered in crocodile) → Birds and Mammals (completely '
                      'separated 4-chambered, double circulation)',
                      'Fishes (3-chambered) → Amphibians (2-chambered) → Reptiles (4-chambered)',
                      'Amphibians (2-chambered) → Reptiles (3-chambered) → Birds (4-chambered)',
                      'Fishes (2-chambered) → Reptiles (3-chambered) → Amphibians (4-chambered)']},
    'subject': 'Biology',
    'topic': 'Animal Kingdom'}]
