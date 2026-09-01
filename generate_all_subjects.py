import json
import csv

all_subjects_questions = [
    # =========================================================================
    # 1. PHYSICS (NEET, JEE, WBJEE, CUET, NDA)
    # =========================================================================
    {
        "id": "PHY-001", "exam": "NEET", "subject": "Physics", "topic": "Units and Measurement", "difficulty": "Easy", "year": "2024",
        "en": "In a Vernier callipers, 20 Vernier Scale Divisions (VSD) coincide with 16 Main Scale Divisions (MSD). If each MSD is 1 mm, the least count of the Vernier callipers is:",
        "bn": "একটি ভার্নিয়ার ক্যালিপার্সে, ২০টি ভার্নিয়ার স্কেল ঘর (VSD) ১৬টি মূল স্কেল ঘরের (MSD) সাথে মিলে যায়। মূল স্কেলের প্রতিটি ঘর ১ মিমি হলে ভার্নিয়ার ধ্রুবক (Least Count) কত?",
        "opts": {"en": ["0.02 cm", "0.01 cm", "0.2 mm", "0.02 mm"], "bn": ["0.02 cm", "0.01 cm", "0.2 mm", "0.02 mm"]},
        "correct": 0,
        "expl_en": "1 VSD = (16/20) MSD = 0.8 mm. Least Count LC = 1 MSD - 1 VSD = 1 mm - 0.8 mm = 0.2 mm = 0.02 cm.",
        "expl_bn": "১ VSD = (১৬/২০) MSD = ০.৮ মিমি। ভার্নিয়ার ধ্রুবক LC = ১ MSD - ১ VSD = ১ - ০.৮ = ০.২ মিমি = ০.০২ সেমি।"
    },
    {
        "id": "PHY-002", "exam": "JEE", "subject": "Physics", "topic": "Units and Measurement", "difficulty": "Easy", "year": "2023",
        "en": "The speed of light in vacuum is taken as unity (c = 1 unit). If light takes 6 minutes and 40 seconds to reach the Earth from the Sun, the distance between the Sun and Earth in this new system of units is:",
        "bn": "শূন্য মাধ্যমে আলোর দ্রুতিকে একক (c = 1 unit) ধরা হলো। সূর্য থেকে পৃথিবীতে আলো পৌঁছাতে ৬ মিনিট ৪০ সেকেন্ড সময় লাগলে, এই নতুন একক পদ্ধতিতে সূর্য ও পৃথিবীর দূরত্ব কত?",
        "opts": {"en": ["400 units", "500 units", "3 × 10⁸ units", "3 × 10¹⁰ units"], "bn": ["400 units", "500 units", "3 × 10⁸ units", "3 × 10¹⁰ units"]},
        "correct": 0,
        "expl_en": "Time t = 6 min 40 s = (6 × 60) + 40 = 400 s. Distance d = c × t = 1 unit/s × 400 s = 400 units.",
        "expl_bn": "সময় t = ৬ মিনিট ৪০ সেকেন্ড = ৪০০ সেকেন্ড। দূরত্ব d = c × t = ১ × ৪০০ = ৪০০ units।"
    },
    {
        "id": "PHY-003", "exam": "WBJEE", "subject": "Physics", "topic": "Units and Measurement", "difficulty": "Medium", "year": "2023",
        "en": "The percentage errors in the measurement of mass (m) and speed (v) of a body are 2% and 3% respectively. The maximum percentage error in the estimation of its kinetic energy (E = ½mv²) is:",
        "bn": "একটি বস্তুর ভর (m) এবং দ্রুতি (v) পরিমাপে শতকরা ত্রুটি যথাক্রমে ২% এবং ৩%। বস্তুটির গতিশক্তি (E = ½mv²) গণনায় সর্বোচ্চ শতকরা ত্রুটি কত?",
        "opts": {"en": ["8%", "5%", "11%", "7%"], "bn": ["8%", "5%", "11%", "7%"]},
        "correct": 0,
        "expl_en": "Kinetic Energy E = ½mv² => (ΔE/E) × 100 = (Δm/m) × 100 + 2 × (Δv/v) × 100 = 2% + 2(3%) = 8%.",
        "expl_bn": "গতিশক্তি E = ½mv² => শতকরা ত্রুটি = ২% + ২ × ৩% = ৮%।"
    },
    {
        "id": "PHY-004", "exam": "NEET", "subject": "Physics", "topic": "Kinematics", "difficulty": "Medium", "year": "2024",
        "en": "A body of mass 5 kg is acted upon by two mutually perpendicular forces of 8 N and 6 N. The magnitude and direction of the acceleration produced in the body are respectively:",
        "bn": "৫ কেজি ভরের একটি বস্তুর ওপর পরস্পরের সাথে লম্বভাবে ৮ N এবং ৬ N মানের দুটি বল প্রযুক্ত হলো। বস্তুতে উৎপন্ন ত্বরণের মান ও অভিমুখ যথাক্রমে:",
        "opts": {
            "en": ["2 m/s² ; tan⁻¹(3/4) with the 8 N force", "2 m/s² ; tan⁻¹(4/3) with the 8 N force", "2 m/s² ; tan⁻¹(3/4) with the 6 N force", "10 m/s² ; tan⁻¹(4/3) with the 6 N force"],
            "bn": ["2 m/s² ; ৮ N বলের সাথে tan⁻¹(3/4)", "2 m/s² ; ৮ N বলের সাথে tan⁻¹(4/3)", "2 m/s² ; ৬ N বলের সাথে tan⁻¹(3/4)", "10 m/s² ; ৬ N বলের সাথে tan⁻¹(4/3)"]
        },
        "correct": 0,
        "expl_en": "Net resultant force F = √(8² + 6²) = 10 N. Acceleration a = F/m = 10 N / 5 kg = 2 m/s². Direction with 8 N force: tan θ = 6/8 = 3/4.",
        "expl_bn": "লব্ধি বল F = √(৮² + ৬²) = ১০ N। ত্বরণ a = ১০/৫ = ২ m/s²। কোণ θ = tan⁻¹(৩/৪)।"
    },
    {
        "id": "PHY-005", "exam": "JEE", "subject": "Physics", "topic": "Kinematics", "difficulty": "Medium", "year": "2023",
        "en": "A projectile is thrown with an initial velocity of u = (6i + 8j) m/s. The horizontal range of the projectile is (take g = 10 m/s²):",
        "bn": "একটি প্রক্ষেপ্যকে (6i + 8j) m/s প্রারম্ভিক বেগে নিক্ষেপ করা হলো। প্রক্ষেপ্যটির অনুভূমিক সীমা (Range) কত? (g = 10 m/s²):",
        "opts": {"en": ["9.6 m", "4.8 m", "12.8 m", "19.2 m"], "bn": ["9.6 m", "4.8 m", "12.8 m", "19.2 m"]},
        "correct": 0,
        "expl_en": "u_x = 6 m/s, u_y = 8 m/s. Time of flight T = 2(8)/10 = 1.6 s. Horizontal Range R = u_x × T = 6 × 1.6 = 9.6 m.",
        "expl_bn": "u_x = ৬ m/s, u_y = ৮ m/s। উড্ডয়ন কাল T = ১.৬ সেকেন্ড। অনুভূমিক সীমা R = ৬ × ১.৬ = ৯.৬ মিটার।"
    },
    {
        "id": "PHY-006", "exam": "NEET", "subject": "Physics", "topic": "Electrostatics", "difficulty": "Hard", "year": "2022",
        "en": "Five capacitors of capacitance C₁ = C₂ = C₃ = C₄ = 10 μF and C₅ = 2.5 μF are arranged in a balanced bridge network across 50 V. The equivalent capacitance is:",
        "bn": "C₁ = C₂ = C₃ = C₄ = ১০ μF এবং C₅ = ২.৫ μF ধারকত্বের পাঁচটি ধারক একটি প্রতিসম ব্রিজ সমবায়ে ৫০ V ব্যাটারির সাথে যুক্ত। সমবায়টির তুল্য ধারকত্ব কত?",
        "opts": {"en": ["10 μF", "5 μF", "2.5 μF", "20 μF"], "bn": ["10 μF", "5 μF", "2.5 μF", "20 μF"]},
        "correct": 0,
        "expl_en": "Balanced bridge eliminates middle capacitor C₅. Top branch = 5 μF, Bottom branch = 5 μF. Total C_eq = 5 + 5 = 10 μF.",
        "expl_bn": "প্রতিসম ব্রিজে C₅ নিষ্ক্রিয়। তুল্য ধারকত্ব = ৫ + ৫ = ১০ μF।"
    },

    # =========================================================================
    # 2. CHEMISTRY (NEET, JEE, WBJEE, CUET)
    # =========================================================================
    {
        "id": "CHEM-001", "exam": "JEE", "subject": "Chemistry", "topic": "Chemical Bonding", "difficulty": "Easy", "year": "2024",
        "en": "According to Molecular Orbital Theory (MOT), which of the following species is diamagnetic and has a bond order of 3?",
        "bn": "আণবিক কক্ষক তত্ত্ব (MOT) অনুসারে, নিচের কোন প্রজাতিটি তিরশ্চৌম্বকীয় (diamagnetic) এবং এর বন্ধন ক্রম 3?",
        "opts": {"en": ["N₂", "O₂", "NO", "C₂⁺"], "bn": ["N₂", "O₂", "NO", "C₂⁺"]},
        "correct": 0,
        "expl_en": "N₂ has 14 electrons: Bond Order = (10 - 4)/2 = 3. All electrons are paired, making N₂ diamagnetic.",
        "expl_bn": "N₂ অণুতে ১৪টি ইলেকট্রন রয়েছে। বন্ধন ক্রম = ৩। কোনো বিজোড় ইলেকট্রন নেই, তাই তিরশ্চৌম্বকীয়।"
    },
    {
        "id": "CHEM-002", "exam": "NEET", "subject": "Chemistry", "topic": "Electrochemistry", "difficulty": "Medium", "year": "2023",
        "en": "The standard electrode potential for Zn²⁺/Zn is -0.76 V and for Cu²⁺/Cu is +0.34 V. The standard EMF of the cell Zn | Zn²⁺ || Cu²⁺ | Cu is:",
        "bn": "Zn²⁺/Zn এর প্রমাণ তড়িৎদ্বার বিভব -0.76 V এবং Cu²⁺/Cu এর +0.34 V। Zn | Zn²⁺ || Cu²⁺ | Cu কোষের প্রমাণ তড়িচ্চালক বল কত?",
        "opts": {"en": ["+1.10 V", "-1.10 V", "+0.42 V", "-0.42 V"], "bn": ["+1.10 V", "-1.10 V", "+0.42 V", "-0.42 V"]},
        "correct": 0,
        "expl_en": "E°_cell = E°_cathode - E°_anode = +0.34 V - (-0.76 V) = +1.10 V.",
        "expl_bn": "E°_cell = E°_ক্যাথোড - E°_অ্যানোড = ০.৩৪ - (-০.৭৬) = +১.১০ V।"
    },
    {
        "id": "CHEM-003", "exam": "NEET", "subject": "Chemistry", "topic": "Organic Chemistry", "difficulty": "Medium", "year": "2024",
        "en": "Which of the following compounds gives a positive Iodoform test upon reaction with I₂/NaOH?",
        "bn": "নিচের কোন যৌগটি I₂/NaOH সহযোগে বিক্রিয়ায় আয়োডোফর্ম পরীক্ষা দেয়?",
        "opts": {"en": ["Ethanol (CH₃CH₂OH)", "Methanol (CH₃OH)", "Benzophenone (C₆H₅COC₆H₅)", "Diethyl ether (C₂H₅OC₂H₅)"], "bn": ["ইথানল (CH₃CH₂OH)", "মিথানল (CH₃OH)", "বেনজোফেনন", "ডাইইথাইল ইথার"]},
        "correct": 0,
        "expl_en": "Ethanol is oxidized to ethanal (CH₃CHO) containing CH₃-C=O group which yields yellow CHI₃ precipitate.",
        "expl_bn": "ইথানল জারিত হয়ে CH₃CHO গঠন করে ও হলুদ CHI₃ অধঃক্ষেপ ফেলে।"
    },
    {
        "id": "CHEM-004", "exam": "JEE", "subject": "Chemistry", "topic": "Coordination Chemistry", "difficulty": "Hard", "year": "2022",
        "en": "The hybridization and magnetic character of the complex [Fe(CN)₆]³⁻ are respectively (Fe atomic number = 26):",
        "bn": "[Fe(CN)₆]³⁻ জটিল আয়নের সংকরায়ণ (Hybridization) এবং চৌম্বক প্রকৃতি যথাক্রমে:",
        "opts": {"en": ["d²sp³, Paramagnetic (1 unpaired electron)", "sp³d², Paramagnetic (5 unpaired electrons)", "d²sp³, Diamagnetic", "sp³d², Diamagnetic"], "bn": ["d²sp³, পরাচৌম্বকীয় (১টি বিজোড় ইলেকট্রন)", "sp³d², পরাচৌম্বকীয় (৫টি বিজোড় ইলেকট্রন)", "d²sp³, তিরশ্চৌম্বকীয়", "sp³d², তিরশ্চৌম্বকীয়"]},
        "correct": 0,
        "expl_en": "Fe³⁺ has 3d⁵. Strong field ligand CN⁻ causes pairing leaving 1 unpaired electron in inner d orbitals -> d²sp³ hybridization.",
        "expl_bn": "তীব্র লিগ্যান্ড CN⁻ এর উপস্থিতিতে ইলেকট্রন জোড় বাঁধে এবং ১টি বিজোড় ইলেকট্রন অবশিষ্ট থাকে -> d²sp³ সংকরায়ণ।"
    },

    # =========================================================================
    # 3. BIOLOGY (NEET, CUET)
    # =========================================================================
    {
        "id": "BIO-001", "exam": "NEET", "subject": "Biology", "topic": "Cell Biology", "difficulty": "Easy", "year": "2024",
        "en": "Which of the following cell organelles is responsible for the initiation of the intrinsic pathway of apoptosis?",
        "bn": "নিচের কোন কোষীয় অঙ্গাণুটি অ্যাপোপটোসিস (Apoptosis)-এর অভ্যন্তরীণ পথ সূচনার জন্য দায়ী?",
        "opts": {"en": ["Mitochondria", "Golgi Apparatus", "Lysosome", "Peroxisome"], "bn": ["মাইটোকনড্রিয়া", "গলগি বডি", "লাইসোজোম", "পারঅক্সিজোম"]},
        "correct": 0,
        "expl_en": "Mitochondria release Cytochrome c into the cytosol which activates caspases and initiates apoptosis.",
        "expl_bn": "মাইটোকনড্রিয়া থেকে সাইটোক্রোম সি নির্গত হয়ে ক্যাসপেজ সক্রিয় করে অ্যাপোপটোসিস ঘটায়।"
    },
    {
        "id": "BIO-002", "exam": "NEET", "subject": "Biology", "topic": "Genetics & Evolution", "difficulty": "Medium", "year": "2023",
        "en": "If a double-stranded DNA molecule contains 20% Cytosine, what will be the percentage of Adenine according to Chargaff's rule?",
        "bn": "একটি দ্বিতন্ত্রী DNA অণুতে ২০% সাইটোসিন থাকলে চারগাফের সূত্র অনুযায়ী অ্যাডেনিনের শতকরা পরিমাণ কত হবে?",
        "opts": {"en": ["30%", "20%", "40%", "60%"], "bn": ["30%", "20%", "40%", "60%"]},
        "correct": 0,
        "expl_en": "C = 20% => G = 20%. Total C + G = 40%. Therefore, A + T = 60%, so A = 30%.",
        "expl_bn": "C = ২০% হলে G = ২০%। মোট C+G = ৪০%। অতএব A+T = ৬০%, অর্থাৎ A = ৩০%।"
    },
    {
        "id": "BIO-003", "exam": "NEET", "subject": "Biology", "topic": "Human Physiology", "difficulty": "Medium", "year": "2024",
        "en": "Juxtaglomerular apparatus (JGA) releases renin in response to:",
        "bn": "জাক্সটাগ্লোমেরুলার অ্যাপারেটাস (JGA) কার প্রতিক্রিয়ায় রেনিন ক্ষরণ করে?",
        "opts": {"en": ["Fall in Glomerular Blood Pressure / GFR", "Rise in Blood Pressure", "High blood sodium level", "Atrial Natriuretic Peptide release"], "bn": ["গ্লোমেরুলার রক্তচাপ / GFR হ্রাস পেলে", "রক্তচাপ বৃদ্ধি পেলে", "রক্তে উচ্চ সোডিয়াম মাত্রা", "ANP ক্ষরণ হলে"]},
        "correct": 0,
        "expl_en": "A fall in glomerular blood flow/pressure stimulates JG cells to secrete Renin, activating the RAAS pathway.",
        "expl_bn": "গ্লোমেরুলার রক্তচাপ কমে গেলে JG কোষ রেনিন নিঃসরণ করে RAAS পথ চালু করে।"
    },

    # =========================================================================
    # 4. MATHEMATICS (JEE, WBJEE, NDA, CUET)
    # =========================================================================
    {
        "id": "MATH-001", "exam": "JEE", "subject": "Mathematics", "topic": "Calculus", "difficulty": "Easy", "year": "2024",
        "en": "The value of limit lim(x -> 0) [sin(5x) / tan(2x)] is:",
        "bn": "lim(x -> 0) [sin(5x) / tan(2x)] এর মান কত?",
        "opts": {"en": ["5/2", "2/5", "1", "0"], "bn": ["5/2", "2/5", "1", "0"]},
        "correct": 0,
        "expl_en": "lim [sin(5x)/5x × 5] / [tan(2x)/2x × 2] = (1 × 5) / (1 × 2) = 5/2.",
        "expl_bn": "lim [sin(5x)/5x × 5] / [tan(2x)/2x × 2] = ৫/২।"
    },
    {
        "id": "MATH-002", "exam": "WBJEE", "subject": "Mathematics", "topic": "Calculus", "difficulty": "Medium", "year": "2023",
        "en": "The integral ∫ [1 / (x² + 4)] dx is equal to:",
        "bn": "∫ [1 / (x² + 4)] dx সমাকলনের মান কত?",
        "opts": {"en": ["(1/2) tan⁻¹(x/2) + C", "tan⁻¹(x/2) + C", "(1/4) tan⁻¹(x/4) + C", "ln(x² + 4) + C"], "bn": ["(1/2) tan⁻¹(x/2) + C", "tan⁻¹(x/2) + C", "(1/4) tan⁻¹(x/4) + C", "ln(x² + 4) + C"]},
        "correct": 0,
        "expl_en": "Standard formula: ∫ dx/(x² + a²) = (1/a) tan⁻¹(x/a) + C. Here a = 2.",
        "expl_bn": "প্রমাণ সূত্র: ∫ dx/(x² + a²) = (1/a) tan⁻¹(x/a) + C। এখানে a = ২।"
    },
    {
        "id": "MATH-003", "exam": "NDA", "subject": "Mathematics", "topic": "Matrices & Determinants", "difficulty": "Medium", "year": "2023",
        "en": "If A is an invertible 3 × 3 matrix such that det(A) = 4, then det(adj A) is equal to:",
        "bn": "A একটি ৩ × ৩ ইনভার্টেবল ম্যাট্রিক্স এবং det(A) = ৪ হলে, det(adj A) এর মান কত?",
        "opts": {"en": ["16", "4", "64", "1/4"], "bn": ["16", "4", "64", "1/4"]},
        "correct": 0,
        "expl_en": "For an n × n matrix, det(adj A) = (det A)^(n - 1) = 4^(3 - 1) = 4² = 16.",
        "expl_bn": "n × n ম্যাট্রিক্সের ক্ষেত্রে det(adj A) = (det A)^(n-1) = ৪² = ১৬।"
    },

    # =========================================================================
    # 5. GENERAL KNOWLEDGE & CURRENT AFFAIRS (UPSC, SSC, CUET, NDA)
    # =========================================================================
    {
        "id": "GK-001", "exam": "UPSC", "subject": "General Knowledge", "topic": "International Affairs", "difficulty": "Easy", "year": "2024",
        "en": "The permanent secretariat of the South Asian Association for Regional Cooperation (SAARC) is located in:",
        "bn": "সার্ক (SAARC)-এর স্থায়ী সচিবালয় কোথায় অবস্থিত?",
        "opts": {"en": ["Kathmandu, Nepal", "New Delhi, India", "Dhaka, Bangladesh", "Colombo, Sri Lanka"], "bn": ["কাঠমান্ডু, নেপাল", "নয়াদিল্লি, ভারত", "ঢাকা, বাংলাদেশ", "কলম্বো, শ্রীলঙ্কা"]},
        "correct": 0,
        "expl_en": "The SAARC Secretariat was established in Kathmandu, Nepal on 16 January 1987.",
        "expl_bn": "সার্ক সচিবালয় ১৯৮৭ সালে নেপালের কাঠমান্ডুতে প্রতিষ্ঠিত হয়।"
    },
    {
        "id": "GK-002", "exam": "SSC", "subject": "General Knowledge", "topic": "Awards & Honors", "difficulty": "Easy", "year": "2023",
        "en": "Who was the first Indian citizen to be awarded the prestigious Nobel Prize?",
        "bn": "কোন ভারতীয় নাগরিক প্রথম মর্যাদাপূর্ণ নোবেল পুরস্কার লাভ করেন?",
        "opts": {"en": ["Rabindranath Tagore (1913)", "C. V. Raman (1930)", "Mother Teresa (1979)", "Amartya Sen (1998)"], "bn": ["রবীন্দ্রনাথ ঠাকুর (১৯১৩)", "সি. ভি. রমন (১৯৩০)", "মাদার তেরেসা (১৯৭৯)", "অমর্ত্য সেন (১৯৯৮)"]},
        "correct": 0,
        "expl_en": "Rabindranath Tagore received the Nobel Prize in Literature in 1913 for 'Gitanjali'.",
        "expl_bn": "রবীন্দ্রনাথ ঠাকুর ১৯১৩ সালে 'গীতাঞ্জলি' কাব্যের জন্য সাহিত্যে নোবেল পান।"
    },

    # =========================================================================
    # 6. GENERAL SCIENCE (UPSC, SSC, NDA, CUET)
    # =========================================================================
    {
        "id": "GS-001", "exam": "SSC", "subject": "General Science", "topic": "Optics & Physics in Daily Life", "difficulty": "Easy", "year": "2024",
        "en": "Which optical phenomenon is primarily responsible for the brilliant sparkle and glittering of diamonds?",
        "bn": "হীরার উজ্জ্বল দ্যুতির জন্য মূলত কোন আলোকীয় ঘটনাটি দায়ী?",
        "opts": {"en": ["Total Internal Reflection (TIR)", "Refraction only", "Scattering of light", "Diffraction"], "bn": ["অভ্যন্তরীণ পূর্ণ প্রতিফলন (TIR)", "কেবল প্রতিসরণ", "আলোর বিচ্ছুরণ", "অপবর্তন"]},
        "correct": 0,
        "expl_en": "Diamonds have a high refractive index (~2.42) and small critical angle (~24.4°), trapping light by Total Internal Reflection.",
        "expl_bn": "হীরকের সংকট কোণ কম (২৪.৪°) হওয়ায় আলোক রশ্মি অভ্যন্তরে বারবার পূর্ণ প্রতিফলিত হয়।"
    },

    # =========================================================================
    # 7. HISTORY (UPSC, SSC)
    # =========================================================================
    {
        "id": "HIST-001", "exam": "UPSC", "subject": "History", "topic": "Modern Indian History", "difficulty": "Medium", "year": "2023",
        "en": "The historic Lahore Session of the Indian National Congress (1929) is memorable because:",
        "bn": "ভারতীয় জাতীয় কংগ্রেসের ১৯২৯ সালের ঐতিহাসিক লাহোর অধিবেশন কী কারণে স্মরণীয়?",
        "opts": {"en": ["Resolution of 'Poorna Swaraj' (Complete Independence) was passed", "Non-Cooperation Movement was launched", "Quit India Resolution was adopted", "Gandhi-Irwin Pact was signed"], "bn": ["'পূর্ণ স্বরাজ' প্রস্তাব গৃহীত হয়", "অসহযোগ আন্দোলন শুরু হয়", "ভারত ছাড়ো প্রস্তাব গৃহীত হয়", "গান্ধী-আরউইন চুক্তি স্বাক্ষরিত হয়"]},
        "correct": 0,
        "expl_en": "Presided over by Jawaharlal Nehru, the Congress declared 'Poorna Swaraj' as its ultimate goal on 31 Dec 1929.",
        "expl_bn": "জওহরলাল নেহরুর সভাপতিত্বে লাহোর অধিবেশনে 'পূর্ণ স্বরাজ' দাবি আনুষ্ঠানিকভাবে গৃহীত হয়।"
    },

    # =========================================================================
    # 8. GEOGRAPHY (UPSC, SSC)
    # =========================================================================
    {
        "id": "GEOG-001", "exam": "UPSC", "subject": "Geography", "topic": "Indian Geography", "difficulty": "Medium", "year": "2024",
        "en": "The 'Ten Degree Channel' separates which of the following geographical island groups?",
        "bn": "'টেন ডিগ্রি চ্যানেল' নিচের কোন দ্বীপপুঞ্জ দুটিকে পৃথক করেছে?",
        "opts": {"en": ["Andaman Islands and Nicobar Islands", "Lakshadweep and Maldives", "South Andaman and Little Andaman", "Minicoy and Maldives"], "bn": ["আন্দামান এবং নিকোবর দ্বীপপুঞ্জ", "লাক্ষাদ্বীপ এবং মালদ্বীপ", "দক্ষিণ আন্দামান এবং লিটল আন্দামান", "মিনিকয় এবং মালদ্বীপ"]},
        "correct": 0,
        "expl_en": "The 10-degree latitude line (Ten Degree Channel) separates Andaman Islands to the north from Nicobar Islands to the south.",
        "expl_bn": "১০ ডিগ্রি উত্তর সমঅক্ষরেখা আন্দামান দ্বীপপুঞ্জকে নিকোবর দ্বীপপুঞ্জ থেকে পৃথক করেছে।"
    },

    # =========================================================================
    # 9. POLITICAL SCIENCE & POLITY (UPSC, SSC)
    # =========================================================================
    {
        "id": "POL-001", "exam": "UPSC", "subject": "Political Science", "topic": "Indian Constitution", "difficulty": "Easy", "year": "2024",
        "en": "Which Article of the Indian Constitution is termed as the 'Heart and Soul of the Constitution' by Dr. B.R. Ambedkar?",
        "bn": "ভারতীয় সংবিধানের কোন অনুচ্ছেদটিকে ড. বি. আর. আম্বেদকর 'সংবিধানের হৃদয় ও আত্মা' বলে অভিহিত করেছিলেন?",
        "opts": {"en": ["Article 32 (Right to Constitutional Remedies)", "Article 21 (Right to Life)", "Article 14 (Equality before Law)", "Article 19 (Freedom of Speech)"], "bn": ["অনুচ্ছেদ ৩২ (সাংবিধানিক প্রতিকারের অধিকার)", "অনুচ্ছেদ ২১ (জীবনের অধিকার)", "অনুচ্ছেদ ১৪ (আইনের দৃষ্টিতে সমতা)", "অনুচ্ছেদ ১৯ (বাকস্বাধীনতা)"]},
        "correct": 0,
        "expl_en": "Article 32 empowers citizens to move the Supreme Court directly via writs (Habeas Corpus, Mandamus, etc.) to enforce Fundamental Rights.",
        "expl_bn": "অনুচ্ছেদ ৩২ মৌলিক অধিকার রক্ষার জন্য সরাসরি সুপ্রিম কোর্টে রিট জারির ক্ষমতা প্রদান করে।"
    },

    # =========================================================================
    # 10. REASONING & APTITUDE (SSC, CUET)
    # =========================================================================
    {
        "id": "REAS-001", "exam": "SSC", "subject": "Reasoning", "topic": "Number Series", "difficulty": "Easy", "year": "2023",
        "en": "Find the missing term in the sequence: 2, 6, 12, 20, 30, 42, ?",
        "bn": "সংখ্যা ক্রমের পরবর্তী পদটি নির্ণয় করো: ২, ৬, ১২, ২০, ৩০, ৪২, ?",
        "opts": {"en": ["56", "54", "50", "48"], "bn": ["56", "54", "50", "48"]},
        "correct": 0,
        "expl_en": "Differences are +4, +6, +8, +10, +12, so next is +14 => 42 + 14 = 56 (or n² + n for n = 7 => 49 + 7 = 56).",
        "expl_bn": "পার্থক্য ক্রম: +৪, +৬, +৮, +১০, +১২, পরবর্তী পদ +১৪ => ৪২ + ১৪ = ৫৬।"
    },

    # =========================================================================
    # 11. ENGLISH LANGUAGE (SSC, CUET, NDA)
    # =========================================================================
    {
        "id": "ENG-001", "exam": "SSC", "subject": "English", "topic": "Subject-Verb Agreement", "difficulty": "Medium", "year": "2024",
        "en": "Choose the grammatically correct option: 'Neither the teacher nor the students ______ present in the auditorium.'",
        "bn": "সঠিক বিকল্পটি নির্বাচন করো: 'Neither the teacher nor the students ______ present in the auditorium.'",
        "opts": {"en": ["were", "was", "is", "has been"], "bn": ["were", "was", "is", "has been"]},
        "correct": 0,
        "expl_en": "With 'Neither...nor', the verb agrees with the closer subject ('the students' -> plural -> 'were').",
        "expl_bn": "'Neither...nor' গঠনে verb নিকটতম subject অনুসারে হয়। 'students' বহুবচন হওয়ায় 'were' সঠিক।"
    }
]

# Write to JSON
with open(r'c:\AVAI_PREP\data\physics_questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_subjects_questions, f, indent=2, ensure_ascii=False)

# Write to JS
with open(r'c:\AVAI_PREP\data\physics_questions.js', 'w', encoding='utf-8') as f:
    f.write('// Comprehensive Master Question Bank for AVAI Prep\n')
    f.write('window.PHYSICS_QUESTIONS_DATA = ' + json.dumps(all_subjects_questions, indent=2, ensure_ascii=False) + ';\n')

# Write to CSV
fields = [
    'Exam', 'Subject', 'Topic', 'Difficulty', 'Year',
    'Question_EN', 'Question_BN',
    'Opt1_EN', 'Opt2_EN', 'Opt3_EN', 'Opt4_EN',
    'Opt1_BN', 'Opt2_BN', 'Opt3_BN', 'Opt4_BN',
    'Correct', 'Expl_EN', 'Expl_BN'
]

csv_path = r'c:\AVAI_PREP\data\physics_for_you_master_questions.csv'
with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    for q in all_subjects_questions:
        opts_en = q.get('opts', {}).get('en', ['', '', '', ''])
        opts_bn = q.get('opts', {}).get('bn', opts_en)
        while len(opts_en) < 4: opts_en.append('')
        while len(opts_bn) < 4: opts_bn.append('')
        corr = q.get('correct', 0) + 1
        writer.writerow([
            q.get('exam', 'ALL'),
            q.get('subject', 'Physics'),
            q.get('topic', 'General'),
            q.get('difficulty', 'Medium'),
            q.get('year', ''),
            q.get('en', ''),
            q.get('bn', ''),
            opts_en[0], opts_en[1], opts_en[2], opts_en[3],
            opts_bn[0], opts_bn[1], opts_bn[2], opts_bn[3],
            corr,
            q.get('expl_en', ''),
            q.get('expl_bn', '')
        ])

# Write to TSV for instant clipboard copy-paste
tsv_path = r'c:\AVAI_PREP\data\master_questions_copy_paste.tsv'
with open(tsv_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(fields)
    for q in all_subjects_questions:
        opts_en = q.get('opts', {}).get('en', ['', '', '', ''])
        opts_bn = q.get('opts', {}).get('bn', opts_en)
        while len(opts_en) < 4: opts_en.append('')
        while len(opts_bn) < 4: opts_bn.append('')
        corr = q.get('correct', 0) + 1
        writer.writerow([
            q.get('exam', 'ALL'),
            q.get('subject', 'Physics'),
            q.get('topic', 'General'),
            q.get('difficulty', 'Medium'),
            q.get('year', ''),
            q.get('en', ''),
            q.get('bn', ''),
            opts_en[0], opts_en[1], opts_en[2], opts_en[3],
            opts_bn[0], opts_bn[1], opts_bn[2], opts_bn[3],
            corr,
            q.get('expl_en', ''),
            q.get('expl_bn', '')
        ])

print(f"Master bank updated with {len(all_subjects_questions)} questions with PYQ Year tags across all subjects!")
