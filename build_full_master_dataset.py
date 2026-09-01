import json
import csv
import os

all_questions = [
    # =========================================================================
    # 1. MATHEMATICS (JEE Main 2025 Authentic Magazine Practice Paper Q1-Q25)
    # =========================================================================
    {
        "id": "MATH-001",
        "exam": "JEE",
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
        "exam": "JEE",
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
        "exam": "JEE",
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
        "exam": "JEE",
        "subject": "Mathematics",
        "topic": "Trigonometric Inequations",
        "difficulty": "Medium",
        "en": "The number of solutions of the inequation 2 sin²(x) - sin(x) - 1 ≤ 0 in the interval [0, 2π] is given by the length of the interval of solution, which is:",
        "bn": "[0, 2π] ব্যবধিতে 2 sin²(x) - sin(x) - 1 ≤ 0 অসমীকরণটির সমাধান অঞ্চলের মোট বিস্তার (দৈর্ঘ্য) কত?",
        "opts": {
            "en": ["4π/3", "π", "5π/6", "3π/2"],
            "bn": ["4π/3", "π", "5π/6", "3π/2"]
        },
        "correct": 0,
        "expl_en": "Factorizing: (2 sin x + 1)(sin x - 1) ≤ 0. Since (sin x - 1) ≤ 0 for all real x, the inequality holds when 2 sin x + 1 ≥ 0, which means sin x ≥ -1/2. In [0, 2π], sin x ≥ -1/2 on [0, 7π/6] ∪ [11π/6, 2π]. Total length = (7π/6 - 0) + (2π - 11π/6) = 7π/6 + π/6 = 8π/6 = 4π/3.",
        "expl_bn": "(2 sin x + 1)(sin x - 1) ≤ 0। যেহেতু sin x - 1 সর্বদাই ≤ 0, তাই 2 sin x + 1 ≥ 0 হতে হবে অর্থাৎ sin x ≥ -1/2। [0, 2π] ব্যবধিতে এর দৈর্ঘ্য = ৭π/৬ + π/৬ = ৮π/৬ = ৪π/৩।"
    },
    {
        "id": "MATH-005",
        "exam": "JEE",
        "subject": "Mathematics",
        "topic": "Definite Integrals & Properties",
        "difficulty": "Hard",
        "en": "The value of the definite integral I = ∫₀^{π/2} (sin³ x)/(sin³ x + cos³ x) dx is:",
        "bn": "I = ∫₀^{π/2} (sin³ x)/(sin³ x + cos³ x) dx নির্দিষ্ট সমাকলটির মান কত?",
        "opts": {
            "en": ["π/4", "π/2", "π", "0"],
            "bn": ["π/4", "π/2", "π", "0"]
        },
        "correct": 0,
        "expl_en": "Using King's property ∫₀ᵃ f(x) dx = ∫₀ᵃ f(a - x) dx: I = ∫₀^{π/2} (cos³ x)/(cos³ x + sin³ x) dx. Adding the two equations: 2I = ∫₀^{π/2} 1 dx = [x]₀^{π/2} = π/2 => I = π/4.",
        "expl_bn": "King's property ব্যবহার করে: 2I = ∫₀^{π/2} 1 dx = π/2 => I = π/4।"
    },
    {
        "id": "MATH-006",
        "exam": "JEE",
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
        "id": "MATH-007",
        "exam": "JEE",
        "subject": "Mathematics",
        "topic": "Probability",
        "difficulty": "Medium",
        "en": "Two fair dice are thrown simultaneously. The conditional probability that the sum of the numbers is 8, given that the sum is an even number, is:",
        "bn": "দুটি নিরপেক্ষ ছক্কা একসাথে ছোড়া হলো। প্রাপ্ত সংখ্যা দুটির যোগফল জোড় সংখ্যা হওয়ার শর্তে যোগফল ৮ হওয়ার শর্তাধীন সম্ভাবনা (Conditional Probability) কত?",
        "opts": {
            "en": ["5/18", "5/36", "1/6", "1/4"],
            "bn": ["5/18", "5/36", "1/6", "1/4"]
        },
        "correct": 0,
        "expl_en": "Total outcomes with an even sum = 18 (sums 2, 4, 6, 8, 10, 12). Outcomes giving sum 8: {(2,6), (3,5), (4,4), (5,3), (6,2)} = 5 outcomes. Hence P(Sum=8 | Even Sum) = 5/18.",
        "expl_bn": "জোড় যোগফলের মোট ঘটনা = ১৮। ৮ যোগফল আসার অনুকূল ঘটনা = ৫টি {(২,৬), (৩,৫), (৪,৪), (৫,৩), (৬,২)}। অতএব নির্ণেয় সম্ভাবনা = ৫/১৮।"
    },

    # =========================================================================
    # 2. CHEMISTRY (JEE Main 2025 Authentic Magazine Practice Paper Q1-Q25)
    # =========================================================================
    {
        "id": "CHEM-001",
        "exam": "JEE",
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
        "exam": "JEE",
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
        "exam": "JEE",
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
        "exam": "JEE",
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
        "exam": "JEE",
        "subject": "Chemistry",
        "topic": "Atomic Structure & Quantum Numbers",
        "difficulty": "Medium",
        "en": "For a 3d orbital, the number of radial nodes and angular nodes are respectively:",
        "bn": "একটি 3d কক্ষকের জন্য রেডিয়াল নোড (Radial Nodes) এবং কৌণিক নোডের (Angular Nodes) সংখ্যা যথাক্রমে:",
        "opts": {
            "en": ["0 and 2", "1 and 2", "2 and 1", "0 and 1"],
            "bn": ["0 এবং 2", "1 এবং 2", "2 এবং 1", "0 এবং 1"]
        },
        "correct": 0,
        "expl_en": "For a 3d orbital: principal quantum number n = 3, azimuthal quantum number l = 2. Radial nodes = n - l - 1 = 3 - 2 - 1 = 0. Angular nodes = l = 2.",
        "expl_bn": "3d কক্ষকের জন্য n = ৩, l = ২। রেডিয়াল নোড = n - l - ১ = ৩ - ২ - ১ = ০। কৌণিক নোড = l = ২।"
    },
    {
        "id": "CHEM-006",
        "exam": "JEE",
        "subject": "Chemistry",
        "topic": "Coordination Compounds",
        "difficulty": "Medium",
        "en": "The intense bright red colour of the nickel dimethylglyoxime complex [Ni(dmg)₂] is stabilized by how many intramolecular hydrogen bonds?",
        "bn": "নিকেল ডাইমিথাইলগ্লাইঅক্সিম জটিল যৌগে [Ni(dmg)₂] কয়টি অন্তঃআণবিক হাইড্রোজেন বন্ধন উপস্থিত থাকে?",
        "opts": {
            "en": ["2", "4", "1", "0"],
            "bn": ["2", "4", "1", "0"]
        },
        "correct": 0,
        "expl_en": "In the square planar [Ni(dmg)₂] complex, the two dimethylglyoximate bidentate ligands are joined through two O-H···O symmetrical intramolecular hydrogen bonds, creating extra six-membered chelate rings.",
        "expl_bn": "[Ni(dmg)₂] জটিল যৌগে দুটি লিগ্যান্ডের মধ্যে ২টি O-H···O অন্তঃআণবিক হাইড্রোজেন বন্ধন থাকে।"
    },
    {
        "id": "CHEM-007",
        "exam": "JEE",
        "subject": "Chemistry",
        "topic": "Solutions & Colligative Properties",
        "difficulty": "Hard",
        "en": "A salt MX₂ dissociates into M²⁺ and 2X⁻ ions in water with degree of dissociation α = 0.5. The van 't Hoff factor (i) for this electrolyte is:",
        "bn": "MX₂ লবণটি পানিতে M²⁺ ও 2X⁻ আয়নে বিয়োজিত হয় যার বিয়োজন মাত্রা α = ০.৫। এই দ্রবণটির ভ্যান্ট হফ গুণক (i) কত?",
        "opts": {
            "en": ["2.0", "2.5", "1.5", "3.0"],
            "bn": ["2.0", "2.5", "1.5", "3.0"]
        },
        "correct": 0,
        "expl_en": "MX₂ -> M²⁺ + 2X⁻ (n = 3 ions per formula unit). Van 't Hoff factor i = 1 + (n - 1)α = 1 + (3 - 1)(0.5) = 1 + 2(0.5) = 1 + 1 = 2.0.",
        "expl_bn": "MX₂ বিয়োজনে ৩টি আয়ন উৎপন্ন হয় (n = ৩)। ভ্যান্ট হফ গুণক i = ১ + (n - ১)α = ১ + ২(০.৫) = ২.০।"
    },

    # =========================================================================
    # 3. PHYSICS (High-Yield Practice Sets for NEET, JEE, WBJEE)
    # =========================================================================
    {
        "id": "PHY-001",
        "exam": "NEET",
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
        "exam": "JEE",
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
        "exam": "WBJEE",
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
        "exam": "NEET",
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
        "exam": "JEE",
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

    # =========================================================================
    # 4. BIOLOGY (NEET Standard High-Yield Practice Questions)
    # =========================================================================
    {
        "id": "BIO-001",
        "exam": "NEET",
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
        "exam": "NEET",
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
        "exam": "NEET",
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
        "exam": "NEET",
        "subject": "Biology",
        "topic": "Biotechnology",
        "difficulty": "Medium",
        "en": "EcoRI restriction endonuclease recognizes and cleaves which specific palindromic nucleotide sequence in double-stranded DNA?",
        "bn": "EcoRI রেস্ট্রিকশন এন্ডোনিউক্লিয়েজ দ্বিসূত্রক ডিএনএ-র কোন নির্দিষ্ট প্যালিনড্রোমিক ক্ষারীয় অনুক্রমকে শনাক্ত ও কর্তন করে?",
        "opts": {
            "en": ["5'-GAATTC-3'", "5'-GGATCC-3'", "5'-AAGCTT-3'", "5'-CTGCAG-3'"],
            "bn": ["5'-GAATTC-3'", "5'-GGATCC-3'", "5'-AAGCTT-3'", "5'-CTGCAG-3'"]
        },
        "correct": 0,
        "expl_en": "EcoRI cuts specifically between G and A in the 5'-GAATTC-3' palindromic sequence, producing 5' cohesive sticky ends.",
        "expl_bn": "EcoRI উৎসেচকটি 5'-GAATTC-3' সিকোয়েন্সে G ও A এর মধ্যবর্তী ফসফোডাইএস্টার বন্ধন ছিন্ন করে।"
    },

    # =========================================================================
    # 5. GENERAL SCIENCE & GENERAL KNOWLEDGE (UPSC, SSC, NDA, CUET)
    # =========================================================================
    {
        "id": "GK-001",
        "exam": "UPSC",
        "subject": "General Science",
        "topic": "Space & Defense Technology",
        "difficulty": "Medium",
        "en": "In satellite communication, the standard geostationary orbit (GEO) is located at an altitude of approximately how many kilometers above Earth's equator?",
        "bn": "উপগ্রহীয় যোগাযোগ ব্যবস্থায় আদর্শ ভূ-স্থির কক্ষপথ (Geostationary Orbit) পৃথিবীর বিষুবরেখা থেকে আনুমানিক কত কিলোমিটার উচ্চতায় অবস্থিত?",
        "opts": {
            "en": ["35,786 km", "400 km", "20,200 km", "1,000 km"],
            "bn": ["৩৫,৭৮৬ কিমি", "৪০০ কিমি", "২০,২০০ কিমি", "১,০০০ কিমি"]
        },
        "correct": 0,
        "expl_en": "A circular geosynchronous orbit positioned exactly over the equator at ~35,786 km (22,236 miles) has an orbital period matching Earth's rotation (23h 56m 4s), appearing stationary relative to ground antennas.",
        "expl_bn": "ভূ-স্থির উপগ্রহ বিষুবরেখার ঠিক ওপরে ৩৫,৭৮৬ কিমি উচ্চতায় পৃথিবীকে ২৪ ঘণ্টায় একবার প্রদক্ষিণ করে।"
    },
    {
        "id": "GK-002",
        "exam": "SSC",
        "subject": "General Knowledge",
        "topic": "Indian Polity & Constitution",
        "difficulty": "Easy",
        "en": "Under which Article of the Constitution of India is the Right to Equality guaranteed to all citizens?",
        "bn": "ভারতের সংবিধানের কোন অনুচ্ছেদের অধীনে সকল নাগরিকের জন্য সাম্যের অধিকার (Right to Equality) সুরক্ষিত?",
        "opts": {
            "en": ["Articles 14 to 18", "Articles 19 to 22", "Articles 25 to 28", "Articles 32 to 35"],
            "bn": ["অনুচ্ছেদ ১৪ থেকে ১৮", "অনুচ্ছেদ ১৯ থেকে ২২", "অনুচ্ছেদ ২৫ থেকে ২৮", "অনুচ্ছেদ ৩২ থেকে ৩৫"]
        },
        "correct": 0,
        "expl_en": "Articles 14 through 18 of Part III of the Indian Constitution guarantee Fundamental Rights to Equality before law and equal protection of laws.",
        "expl_bn": "সংবিধানের তৃতীয় অংশের অনুচ্ছেদ ১৪ থেকে ১৮ নাগরিকদের সাম্যের মৌলিক অধিকার প্রদান করে।"
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
