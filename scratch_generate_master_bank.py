import json
import csv

master_questions = [
    # =========================================================================
    # PHYSICS - MECHANICS & PROPERTIES OF MATTER
    # =========================================================================
    {
        "id": "PHY-001", "exam": "NEET", "subject": "Physics", "topic": "Units and Measurement", "difficulty": "Easy",
        "en": "In a Vernier callipers, 20 Vernier Scale Divisions (VSD) coincide with 16 Main Scale Divisions (MSD). If each MSD is 1 mm, the least count of the Vernier callipers is:",
        "bn": "একটি ভার্নিয়ার ক্যালিপার্সে, ২০টি ভার্নিয়ার স্কেল ঘর (VSD) ১৬টি মূল স্কেল ঘরের (MSD) সাথে মিলে যায়। মূল স্কেলের প্রতিটি ঘর ১ মিমি হলে ভার্নিয়ার ধ্রুবক (Least Count) কত?",
        "opts": {"en": ["0.02 cm", "0.01 cm", "0.2 mm", "0.02 mm"], "bn": ["0.02 cm", "0.01 cm", "0.2 mm", "0.02 mm"]},
        "correct": 0,
        "expl_en": "1 VSD = (16/20) MSD = 0.8 mm. Least Count LC = 1 MSD - 1 VSD = 1 mm - 0.8 mm = 0.2 mm = 0.02 cm.",
        "expl_bn": "১ VSD = (১৬/২০) MSD = ০.৮ মিমি। ভার্নিয়ার ধ্রুবক LC = ১ MSD - ১ VSD = ১ - ০.৮ = ০.২ মিমি = ০.০২ সেমি।"
    },
    {
        "id": "PHY-002", "exam": "JEE", "subject": "Physics", "topic": "Units and Measurement", "difficulty": "Easy",
        "en": "The speed of light in vacuum is taken as unity (c = 1 unit). If light takes 6 minutes and 40 seconds to reach the Earth from the Sun, the distance between the Sun and Earth in this new system of units is:",
        "bn": "শূন্য মাধ্যমে আলোর দ্রুতিকে একক (c = 1 unit) ধরা হলো। সূর্য থেকে পৃথিবীতে আলো পৌঁছাতে ৬ মিনিট ৪০ সেকেন্ড সময় লাগলে, এই নতুন একক পদ্ধতিতে সূর্য ও পৃথিবীর দূরত্ব কত?",
        "opts": {"en": ["400 units", "500 units", "3 × 10⁸ units", "3 × 10¹⁰ units"], "bn": ["400 units", "500 units", "3 × 10⁸ units", "3 × 10¹⁰ units"]},
        "correct": 0,
        "expl_en": "Time t = 6 min 40 s = (6 × 60) + 40 = 400 s. Distance d = c × t = 1 unit/s × 400 s = 400 units.",
        "expl_bn": "সময় t = ৬ মিনিট ৪০ সেকেন্ড = ৪০০ সেকেন্ড। দূরত্ব d = c × t = ১ × ৪০০ = ৪০০ units।"
    },
    {
        "id": "PHY-003", "exam": "WBJEE", "subject": "Physics", "topic": "Units and Measurement", "difficulty": "Medium",
        "en": "The percentage errors in the measurement of mass (m) and speed (v) of a body are 2% and 3% respectively. The maximum percentage error in the estimation of its kinetic energy (E = ½mv²) is:",
        "bn": "একটি বস্তুর ভর (m) এবং দ্রুতি (v) পরিমাপে শতকরা ত্রুটি যথাক্রমে ২% এবং ৩%। বস্তুটির গতিশক্তি (E = ½mv²) গণনায় সর্বোচ্চ শতকরা ত্রুটি কত?",
        "opts": {"en": ["8%", "5%", "11%", "7%"], "bn": ["8%", "5%", "11%", "7%"]},
        "correct": 0,
        "expl_en": "Kinetic Energy E = ½mv² => (ΔE/E) × 100 = (Δm/m) × 100 + 2 × (Δv/v) × 100 = 2% + 2(3%) = 8%.",
        "expl_bn": "গতিশক্তি E = ½mv² => শতকরা ত্রুটি = ২% + ২ × ৩% = ৮%।"
    },
    {
        "id": "PHY-004", "exam": "NEET", "subject": "Physics", "topic": "Kinematics", "difficulty": "Medium",
        "en": "A body of mass 5 kg is acted upon by two mutually perpendicular forces of 8 N and 6 N. The magnitude and direction of the acceleration produced in the body are respectively:",
        "bn": "৫ কেজি ভরের একটি বস্তুর ওপর পরস্পরের সাথে লম্বভাবে ৮ N এবং ৬ N মানের দুটি বল প্রযুক্ত হলো। বস্তুতে উৎপন্ন ত্বরণের মান ও অভিমুখ যথাক্রমে:",
        "opts": {
            "en": ["2 m/s² ; tan⁻¹(3/4) with the 8 N force", "2 m/s² ; tan⁻¹(4/3) with the 8 N force", "2 m/s² ; tan⁻¹(3/4) with the 6 N force", "10 m/s² ; tan⁻¹(4/3) with the 6 N force"],
            "bn": ["2 m/s² ; ৮ N বলের সাথে tan⁻¹(3/4)", "2 m/s² ; ৮ N বলের সাথে tan⁻¹(4/3)", "2 m/s² ; ৬ N বলের সাথে tan⁻¹(3/4)", "10 m/s² ; ৬ N বলের সাথে tan⁻¹(4/3)"]
        },
        "correct": 0,
        "expl_en": "Net resultant force F = √(8² + 6²) = 10 N. Acceleration a = F/m = 10 N / 5 kg = 2 m/s². tan θ = 6/8 = 3/4.",
        "expl_bn": "লব্ধি বল F = √(৮² + ৬²) = ১০ N। ত্বরণ a = ১০/৫ = ২ m/s²। কোণ θ = tan⁻¹(৩/৪)।"
    },
    {
        "id": "PHY-005", "exam": "JEE", "subject": "Physics", "topic": "Kinematics", "difficulty": "Medium",
        "en": "A projectile is thrown with an initial velocity of u = (6i + 8j) m/s. The horizontal range of the projectile is (take g = 10 m/s²):",
        "bn": "একটি প্রক্ষেপ্যকে (6i + 8j) m/s প্রারম্ভিক বেগে নিক্ষেপ করা হলো। প্রক্ষেপ্যটির অনুভূমিক সীমা (Range) কত? (g = 10 m/s²):",
        "opts": {"en": ["9.6 m", "4.8 m", "12.8 m", "19.2 m"], "bn": ["9.6 m", "4.8 m", "12.8 m", "19.2 m"]},
        "correct": 0,
        "expl_en": "u_x = 6 m/s, u_y = 8 m/s. Time of flight T = 2 u_y / g = 2(8)/10 = 1.6 s. Range R = u_x × T = 6 × 1.6 = 9.6 m.",
        "expl_bn": "u_x = ৬ m/s, u_y = ৮ m/s। উড্ডয়ন কাল T = ২(৮)/১০ = ১.৬ সেকেন্ড। অনুভূমিক সীমা R = ৬ × ১.৬ = ৯.৬ মিটার।"
    },
    {
        "id": "PHY-006", "exam": "CUET", "subject": "Physics", "topic": "Kinematics", "difficulty": "Easy",
        "en": "A ball is thrown vertically upward with speed u = 30 m/s. The ratio of distances travelled in the 1st second and 2nd second of its upward journey is (take g = 10 m/s²):",
        "bn": "একটি বলকে ৩০ m/s বেগে খাড়া ওপরের দিকে ছোঁড়া হলো। ওপরের দিকে যাত্রাকালে ১ম ও ২য় সেকেন্ডে অতিক্রান্ত দূরত্বের অনুপাত কত? (g = 10 m/s²):",
        "opts": {"en": ["5 : 3", "3 : 1", "7 : 5", "4 : 3"], "bn": ["5 : 3", "3 : 1", "7 : 5", "4 : 3"]},
        "correct": 0,
        "expl_en": "Distance in nth second: s_n = u - g/2(2n - 1). s₁ = 30 - 5 = 25 m. s₂ = 30 - 15 = 15 m. Ratio = 25 : 15 = 5 : 3.",
        "expl_bn": "১ম সেকেন্ডে s₁ = ২৫ মি, ২য় সেকেন্ডে s₂ = ১৫ মি। অনুপাত = ৫ : ৩।"
    },
    {
        "id": "PHY-007", "exam": "WBJEE", "subject": "Physics", "topic": "Work, Energy and Power", "difficulty": "Easy",
        "en": "A crane lifts a load of mass 1000 kg vertically to a height of 20 m in 10 seconds with uniform velocity. The average power output of the crane is (take g = 9.8 m/s²):",
        "bn": "একটি ক্রেন ১০০০ কেজি ভরের একটি বস্তুকে ১০ সেকেন্ডে সমবেগে ২০ মিটার উচ্চতায় তোলে। ক্রেনটির গড় ক্ষমতা কত? (g = 9.8 m/s²):",
        "opts": {"en": ["19.6 kW", "39.2 kW", "19.6 W", "9.8 kW"], "bn": ["19.6 kW", "39.2 kW", "19.6 W", "9.8 kW"]},
        "correct": 0,
        "expl_en": "Work done W = mgh = 1000 × 9.8 × 20 = 196,000 J. Power P = W / t = 196,000 / 10 = 19.6 kW.",
        "expl_bn": "কৃতকার্য W = ১৯৬,০০০ J। গড় ক্ষমতা P = ১৯৬,০০০ / ১০ = ১৯.৬ kW।"
    },
    {
        "id": "PHY-008", "exam": "JEE", "subject": "Physics", "topic": "Laws of Motion", "difficulty": "Hard",
        "en": "A block of mass m = 2 kg rests on a rough horizontal surface with coefficient of static friction μ_s = 0.5. A force of F = 6 N is applied horizontally on the block. The frictional force acting on the block is (take g = 10 m/s²):",
        "bn": "২ কেজি ভরের একটি ব্লক অনুভূমিক অমসৃণ তলে স্থির আছে (স্থৈতিক ঘর্ষণ গুণাঙ্ক μ_s = 0.5)। ব্লকের ওপর ৬ N অনুভূমিক বল প্রযুক্ত হলে কার্যকর ঘর্ষণ বল কত? (g = 10 m/s²):",
        "opts": {"en": ["6 N", "10 N", "5 N", "0 N"], "bn": ["6 N", "10 N", "5 N", "0 N"]},
        "correct": 0,
        "expl_en": "Maximum static friction f_max = μ_s × N = 0.5 × 20 = 10 N. Since applied force (6 N) < f_max (10 N), static friction exactly balances applied force: f = 6 N.",
        "expl_bn": "সীমাস্ত ঘর্ষণ f_max = ১০ N। প্রযুক্ত বল (৬ N) কম হওয়ায় কার্যকর ঘর্ষণ বল = ৬ N।"
    },
    {
        "id": "PHY-009", "exam": "NEET", "subject": "Physics", "topic": "Rotational Motion", "difficulty": "Medium",
        "en": "A solid sphere and a hollow sphere of equal mass M and equal radius R roll down the same inclined plane without slipping from rest. The ratio of their translational accelerations (a_solid : a_hollow) is:",
        "bn": "সমান ভর (M) ও সমান ব্যাসার্ধের (R) একটি নিরেট গোলক ও একটি ফাঁপা গোলক একই আনত তল বেয়ে পিছলে না গিয়ে গড়িয়ে নামে। তাদের রৈখিক ত্বরণের অনুপাত (a_নিরেট : a_ফাঁপা) কত?",
        "opts": {"en": ["25 : 21", "15 : 14", "7 : 5", "5 : 3"], "bn": ["25 : 21", "15 : 14", "7 : 5", "5 : 3"]},
        "correct": 0,
        "expl_en": "a = (g sin θ) / (1 + I/MR²). a_solid = 5/7 g sin θ. a_hollow = 3/5 g sin θ. Ratio = (5/7) / (3/5) = 25/21.",
        "expl_bn": "নিরেট গোলক a = ৫/৭ g sin θ, ফাঁপা গোলক a = ৩/৫ g sin θ। অনুপাত = ২৫ : ২১।"
    },
    {
        "id": "PHY-010", "exam": "JEE", "subject": "Physics", "topic": "Gravitation", "difficulty": "Medium",
        "en": "If the radius of the Earth were to shrink by 1% while its mass remains constant, the acceleration due to gravity on the Earth's surface would:",
        "bn": "পৃথিবীর ভর অপরিবর্তিত রেখে যদি এর ব্যাসার্ধ ১% সংকুচিত হয়, তবে ভূপৃষ্ঠে অভিকর্ষজ ত্বরণ (g) এর কী পরিবর্তন হবে?",
        "opts": {"en": ["Increase by 2%", "Decrease by 2%", "Increase by 1%", "Decrease by 1%"], "bn": ["২% বৃদ্ধি পাবে", "২% হ্রাস পাবে", "১% বৃদ্ধি পাবে", "১% হ্রাস পাবে"]},
        "correct": 0,
        "expl_en": "g = GM/R² => Δg/g ≈ -2(ΔR/R) = -2(-1%) = +2% increase.",
        "expl_bn": "g = GM/R² => ব্যাসার্ধ ১% সংকুচিত হলে অভিকর্ষজ ত্বরণ ২% বৃদ্ধি পায়।"
    },
    {
        "id": "PHY-011", "exam": "JEE", "subject": "Physics", "topic": "Thermodynamics", "difficulty": "Medium",
        "en": "A Carnot engine absorbs 1000 J of heat from a heat reservoir at 500 K and rejects heat to a sink at 300 K. The work done per cycle and heat rejected to sink are respectively:",
        "bn": "একটি কারনট ইঞ্জিন ৫০০ K তাপমাত্রার উৎস থেকে ১০০০ J তাপ গ্রহণ করে এবং ৩০০ K তাপমাত্রার গ্রাহকে তাপ বর্জন করে। প্রতি চক্রে কৃতকার্য ও বর্জিত তাপ যথাক্রমে:",
        "opts": {"en": ["400 J, 600 J", "600 J, 400 J", "500 J, 500 J", "200 J, 800 J"], "bn": ["400 J, 600 J", "600 J, 400 J", "500 J, 500 J", "200 J, 800 J"]},
        "correct": 0,
        "expl_en": "Efficiency η = 1 - 300/500 = 0.40. Work W = 0.40 × 1000 = 400 J. Q₂ = 1000 - 400 = 600 J.",
        "expl_bn": "কর্মদক্ষতা η = ০.৪০। কৃতকার্য W = ৪০০ J। বর্জিত তাপ Q₂ = ৬০০ J।"
    },
    {
        "id": "PHY-012", "exam": "NEET", "subject": "Physics", "topic": "Kinetic Theory of Gases", "difficulty": "Easy",
        "en": "The average translational kinetic energy of an ideal gas molecule at absolute temperature T is given by (k_B = Boltzmann constant):",
        "bn": "T পরম তাপমাত্রায় একটি আদর্শ গ্যাসের অণুর গড় রৈখিক গতিশক্তি (Translational Kinetic Energy) কত? (k_B = বোল্টজম্যান ধ্রুবক):",
        "opts": {"en": ["(3/2) k_B T", "(1/2) k_B T", "(5/2) k_B T", "3 k_B T"], "bn": ["(3/2) k_B T", "(1/2) k_B T", "(5/2) k_B T", "3 k_B T"]},
        "correct": 0,
        "expl_en": "By equipartition of energy theorem: Total average translational KE across 3 dimensions = (3/2) k_B T.",
        "expl_bn": "শক্তির সমবণ্টন নীতি অনুযায়ী ৩টি মাত্রায় মোট গতিশক্তি = (৩/২) k_B T।"
    },
    {
        "id": "PHY-013", "exam": "WBJEE", "subject": "Physics", "topic": "Oscillations and Waves", "difficulty": "Medium",
        "en": "A particle executes Simple Harmonic Motion (SHM) with an amplitude A. At what displacement from the mean position is its kinetic energy equal to its potential energy?",
        "bn": "একটি কণা A বিস্তারে সরল দোলগতি (SHM) সম্পন্ন করছে। সাম্যাবস্থান থেকে কত সরণে কণাটির গতিশক্তি ও স্থিতিশক্তি সমান হবে?",
        "opts": {"en": ["A / √2", "A / 2", "A / √3", "A √3 / 2"], "bn": ["A / √2", "A / 2", "A / √3", "A √3 / 2"]},
        "correct": 0,
        "expl_en": "KE = PE => A² - x² = x² => 2x² = A² => x = A / √2.",
        "expl_bn": "গতিশক্তি = স্থিতিশক্তি => ২x² = A² => x = A / √২।"
    },
    {
        "id": "PHY-014", "exam": "NEET", "subject": "Physics", "topic": "Electrostatics", "difficulty": "Hard",
        "en": "Five capacitors of capacitance C₁ = C₂ = C₃ = C₄ = 10 μF and C₅ = 2.5 μF are arranged in a balanced bridge network connected across a 50 V battery. The equivalent capacitance of the network is:",
        "bn": "C₁ = C₂ = C₃ = C₄ = ১০ μF এবং C₅ = ২.৫ μF ধারকত্বের পাঁচটি ধারক একটি প্রতিসম ব্রিজ সমবায়ে ৫০ V ব্যাটারির সাথে যুক্ত। সমবায়টির তুল্য ধারকত্ব কত?",
        "opts": {"en": ["10 μF", "5 μF", "2.5 μF", "20 μF"], "bn": ["10 μF", "5 μF", "2.5 μF", "20 μF"]},
        "correct": 0,
        "expl_en": "Balanced bridge eliminates middle capacitor C₅. Top branch = 5 μF, Bottom branch = 5 μF. Total C_eq = 5 + 5 = 10 μF.",
        "expl_bn": "প্রতিসম ব্রিজে C₅ নিষ্ক্রিয়। তুল্য ধারকত্ব = ৫ + ৫ = ১০ μF।"
    },
    {
        "id": "PHY-015", "exam": "JEE", "subject": "Physics", "topic": "Electrostatics", "difficulty": "Medium",
        "en": "An electric dipole of dipole moment p = 4 × 10⁻⁹ C·m is aligned at 30° with the direction of a uniform electric field of magnitude 5 × 10⁴ N/C. The torque acting on the dipole is:",
        "bn": "p = ৪ × ১০⁻⁹ C·m দ্বিমেরু ভ্রামকবিশিষ্ট একটি তড়িৎ দ্বিমেরু ৫ × ১০⁴ N/C মানের সুষম তড়িৎক্ষেত্রের সাথে ৩০° কোণে স্থাপিত। দ্বিমেরুর ওপর প্রযুক্ত টর্কের মান:",
        "opts": {"en": ["1.0 × 10⁻⁴ N·m", "2.0 × 10⁻⁴ N·m", "1.73 × 10⁻⁴ N·m", "0.5 × 10⁻⁴ N·m"], "bn": ["1.0 × 10⁻⁴ N·m", "2.0 × 10⁻⁴ N·m", "1.73 × 10⁻⁴ N·m", "0.5 × 10⁻⁴ N·m"]},
        "correct": 0,
        "expl_en": "τ = p E sin 30° = (4 × 10⁻⁹) × (5 × 10⁴) × 0.5 = 1.0 × 10⁻⁴ N·m.",
        "expl_bn": "টর্ক τ = p E sin ৩০° = ১.০ × ১০⁻⁴ N·m।"
    },
    {
        "id": "PHY-016", "exam": "NEET", "subject": "Physics", "topic": "Current Electricity", "difficulty": "Medium",
        "en": "A galvanometer of resistance 100 Ω gives full-scale deflection for a current of 1 mA. To convert it into an ammeter of range 0 – 10 A, the required shunt resistance is:",
        "bn": "১০০ Ω রোধের একটি গ্যালভানোমিটার ১ mA প্রবাহে পূর্ণ স্কেল বিক্ষেপ দেয়। এটিকে ০ - ১০ A পাল্লার অ্যামিটারে রূপান্তরিত করতে প্রয়োজনীয় শান্ট রোধ কত?",
        "opts": {"en": ["0.01 Ω", "0.1 Ω", "0.001 Ω", "1.0 Ω"], "bn": ["0.01 Ω", "0.1 Ω", "0.001 Ω", "1.0 Ω"]},
        "correct": 0,
        "expl_en": "Shunt S = (I_g × G) / (I - I_g) = (0.001 × 100) / (10 - 0.001) ≈ 0.01 Ω.",
        "expl_bn": "শান্ট S = (০.০০১ × ১০০) / ১০ = ০.০১ Ω।"
    },
    {
        "id": "PHY-017", "exam": "WBJEE", "subject": "Physics", "topic": "Current Electricity", "difficulty": "Easy",
        "en": "In a metre bridge experiment, the null point is found at a distance of 40 cm from the left end when a known resistance of 12 Ω is connected in the right gap. The unknown resistance in the left gap is:",
        "bn": "মিটার ব্রিজ পরীক্ষায় ডান প্রান্তের ফাঁকে ১২ Ω রোধ যুক্ত থাকলে বাম প্রান্ত থেকে ৪০ সেমি দূরত্বে নিস্পন্দ বিন্দু পাওয়া যায়। বাম ফাঁকের অজানা রোধের মান কত?",
        "opts": {"en": ["8 Ω", "18 Ω", "6 Ω", "12 Ω"], "bn": ["8 Ω", "18 Ω", "6 Ω", "12 Ω"]},
        "correct": 0,
        "expl_en": "R / 12 = 40 / 60 = 2/3 => R = 12 × (2/3) = 8 Ω.",
        "expl_bn": "মিটার ব্রিজ নীতি: R / ১২ = ৪০ / ৬০ => R = ৮ Ω।"
    },
    {
        "id": "PHY-018", "exam": "NEET", "subject": "Physics", "topic": "Magnetic Effects of Current", "difficulty": "Medium",
        "en": "A 100-turn circular coil of radius 5 cm carries a current producing a magnetic field of 3.14 × 10⁻³ T at its centre. The current flowing through the coil and its magnetic dipole moment are respectively (take μ₀ = 4π × 10⁻⁷ T·m/A):",
        "bn": "৫ সেমি ব্যাসার্ধের এবং ১০০ পাকের একটি বৃত্তাকার কুন্ডলীর কেন্দ্রে চৌম্বক ক্ষেত্র ৩.১৪ × ১০⁻³ T। কুন্ডলীর মধ্য দিয়ে তড়িৎপ্রবাহ এবং কুন্ডলীটির চৌম্বক দ্বিমেরু ভ্রামক যথাক্রমে:",
        "opts": {"en": ["2.5 A, 2.0 A·m²", "2.5 A, 20 A·m²", "2.0 A, 4.0 A·m²", "5.0 A, 1.0 A·m²"], "bn": ["2.5 A, 2.0 A·m²", "2.5 A, 20 A·m²", "2.0 A, 4.0 A·m²", "5.0 A, 1.0 A·m²"]},
        "correct": 0,
        "expl_en": "B = (μ₀ N I)/(2 R) => I = 2.5 A. M = N I A ≈ 2.0 A·m².",
        "expl_bn": "কেন্দ্রে B = (μ₀ N I)/(২ R) => I = ২.৫ A। চৌম্বক ভ্রামক M ≈ ২.০ A·m²।"
    },
    {
        "id": "PHY-019", "exam": "NEET", "subject": "Physics", "topic": "Alternating Current", "difficulty": "Medium",
        "en": "A series AC circuit contains a resistance R = 1 kΩ, a capacitor C = 0.1 μF, and an inductor L = 1 mH. The resonant frequency of this series LCR circuit is approximately:",
        "bn": "একটি শ্রেণি LCR বর্তনীতে রোধ R = ১ kΩ, ধারক C = ০.১ μF এবং আবেশক L = ১ mH যুক্ত আছে। বর্তনীটির অনুনাদী কম্পাঙ্ক (Resonant Frequency) প্রায়:",
        "opts": {"en": ["15.9 kHz", "10.1 kHz", "20.7 kHz", "13.5 kHz"], "bn": ["15.9 kHz", "10.1 kHz", "20.7 kHz", "13.5 kHz"]},
        "correct": 0,
        "expl_en": "f_r = 1 / (2π√(LC)) = 1 / (2π√(10⁻³ × 10⁻⁷)) ≈ 15.9 kHz.",
        "expl_bn": "অনুনাদী কম্পাঙ্ক f_r = ১ / (২π√(LC)) ≈ ১৫.৯ kHz।"
    },
    {
        "id": "PHY-020", "exam": "JEE", "subject": "Physics", "topic": "Electromagnetic Induction", "difficulty": "Medium",
        "en": "A rectangular loop of dimensions 8 cm × 3 cm with a small cut is moving with velocity 2 cm/s out of a uniform magnetic field B = 0.3 T perpendicular to the loop, in a direction normal to its shorter side. The induced EMF across the cut is:",
        "bn": "৮ সেমি × ৩ সেমি পরিমাপের একটি ছোট কাটাযুক্ত আয়তাকার লুপ ০.৩ T সুষম চৌম্বক ক্ষেত্র থেকে ক্ষুদ্রতম বাহুর লম্ব বরাবর ২ সেমি/সেকেন্ড বেগে বেরিয়ে আসছে। কাটা প্রান্তে আবিষ্ট তড়িচ্চালক বলের মান:",
        "opts": {"en": ["4.8 × 10⁻⁴ V", "1.8 × 10⁻⁴ V", "1.2 × 10⁻⁴ V", "2.4 × 10⁻⁴ V"], "bn": ["4.8 × 10⁻⁴ V", "1.8 × 10⁻⁴ V", "1.2 × 10⁻⁴ V", "2.4 × 10⁻⁴ V"]},
        "correct": 0,
        "expl_en": "Induced emf ε = B·L·v = 0.3 × 0.08 × 0.02 = 4.8 × 10⁻⁴ V.",
        "expl_bn": "আবিষ্ট তড়িচ্চালক বল ε = B L v = ৪.৮ × ১০⁻⁴ V।"
    },
    {
        "id": "PHY-021", "exam": "NEET", "subject": "Physics", "topic": "Wave Optics", "difficulty": "Hard",
        "en": "In Young's double-slit experiment using monochromatic light of wavelength λ, the intensity at a point where the path difference is λ is K units. The intensity at a point where the path difference is λ/3 will be:",
        "bn": "λ তরঙ্গদৈর্ঘ্যের আলো ব্যবহার করে ইয়ং-এর দ্বি-রেখাছিদ্র পরীক্ষায় যে বিন্দুতে পথপার্থক্য λ, সেখানে তীব্রতা K। যে বিন্দুতে পথপার্থক্য λ/৩, সেখানে তীব্রতা কত হবে?",
        "opts": {"en": ["K / 4", "K / 2", "K", "3K / 4"], "bn": ["K / 4", "K / 2", "K", "3K / 4"]},
        "correct": 0,
        "expl_en": "Phase diff for Δx = λ/3 is φ = 2π/3. Intensity I = K cos²(φ/2) = K cos²(π/3) = K/4.",
        "expl_bn": "পথপার্থক্য λ/৩ হলে তীব্রতা I = K cos²(π/৩) = K/৪।"
    },
    {
        "id": "PHY-022", "exam": "JEE", "subject": "Physics", "topic": "Ray Optics", "difficulty": "Medium",
        "en": "An equilateral glass prism has a refractive index of μ = √3. The angle of minimum deviation for this prism is:",
        "bn": "একটি সমবাহু কাচ প্রিজমের প্রতিসরাঙ্ক √3। প্রিজমটির ন্যূনতম চ্যুতি কোণ (Angle of Minimum Deviation) কত?",
        "opts": {"en": ["60°", "30°", "45°", "90°"], "bn": ["60°", "30°", "45°", "90°"]},
        "correct": 0,
        "expl_en": "sin((60° + δ_m)/2) = √3 × sin 30° = √3/2 => (60° + δ_m)/2 = 60° => δ_m = 60°.",
        "expl_bn": "ন্যূনতম চ্যুতি কোণ δ_m = ৬০°।"
    },
    {
        "id": "PHY-023", "exam": "CUET", "subject": "Physics", "topic": "Ray Optics", "difficulty": "Easy",
        "en": "A convex lens of focal length f₁ = +20 cm is placed in contact with a concave lens of focal length f₂ = -30 cm. The focal length and power of the combination are respectively:",
        "bn": "+২০ সেমি ফোকাস দৈর্ঘ্যের একটি উত্তল লেন্স -৩০ সেমি ফোকাস দৈর্ঘ্যের একটি অবতল লেন্সের সংস্পর্শে রাখা হলো। সমবায়টির ফোকাস দৈর্ঘ্য ও ক্ষমতা যথাক্রমে:",
        "opts": {"en": ["+60 cm, +1.67 D", "-60 cm, -1.67 D", "+12 cm, +8.33 D", "+50 cm, +2.0 D"], "bn": ["+60 cm, +1.67 D", "-60 cm, -1.67 D", "+12 cm, +8.33 D", "+50 cm, +2.0 D"]},
        "correct": 0,
        "expl_en": "1/F = 1/20 - 1/30 = 1/60 => F = +60 cm. Power P = 100/60 = +1.67 D.",
        "expl_bn": "১/F = ১/২০ - ১/৩০ = ১/৬০ => F = +৬০ সেমি। ক্ষমতা P = +১.৬৭ ডায়প্টার।"
    },
    {
        "id": "PHY-024", "exam": "NEET", "subject": "Physics", "topic": "Dual Nature of Matter", "difficulty": "Easy",
        "en": "Match the following physical phenomena with their correct theoretical explanations:\n(A) E = hν — (I) de Broglie Wavelength\n(B) Diffraction & Interference — (II) Particle Nature of Light\n(C) λ = h/p — (III) Wave Nature of Light\n(D) Compton Effect — (IV) Energy of Photon",
        "bn": "নিচের ভৌত ঘটনাগুলির সাথে সংশ্লিষ্ট সঠিক তত্ত্বগুলি মেলান:\n(A) E = hν — (I) ডি ব্রগলি তরঙ্গদৈর্ঘ্য\n(B) অপবর্তন ও ব্যতিচার — (II) আলোর কণা ধর্ম\n(C) λ = h/p — (III) আলোর তরঙ্গ ধর্ম\n(D) কম্পটন ক্রিয়া — (IV) ফোটনের শক্তি",
        "opts": {"en": ["A-IV, B-III, C-I, D-II", "A-I, B-IV, C-III, D-II", "A-IV, B-I, C-II, D-III", "A-III, B-II, C-I, D-IV"], "bn": ["A-IV, B-III, C-I, D-II", "A-I, B-IV, C-III, D-II", "A-IV, B-I, C-II, D-III", "A-III, B-II, C-I, D-IV"]},
        "correct": 0,
        "expl_en": "E=hν is photon energy (IV). Diffraction proves wave nature (III). λ=h/p is de Broglie wavelength (I). Compton effect proves particle nature (II).",
        "expl_bn": "E = hν ফোটনের শক্তি (IV)। অপবর্তন তরঙ্গ ধর্ম (III)। λ = h/p ডি ব্রগলি (I)। কম্পটন কণা ধর্ম (II)।"
    },
    {
        "id": "PHY-025", "exam": "JEE", "subject": "Physics", "topic": "Nuclear Physics", "difficulty": "Medium",
        "en": "A radioactive nucleus undergoes alpha decay according to the equation ₉₂U²³⁸ → ₉₀Th²³⁴ + ₂He⁴. If the mass defect is 0.0045 amu, the total Q-value of the reaction is approximately (1 amu = 931.5 MeV):",
        "bn": "একটি তেজস্ক্রিয় নিউক্লিয়াস ₉₂U²³⁸ → ₉₀Th²³⁴ + ₂He⁴ সমীকরণ অনুযায়ী আলফা ক্ষয়প্রাপ্ত হয়। ভর ত্রুটি ০.০০৪৫ amu হলে বিক্রিয়ায় মুক্ত শক্তি (Q-value) প্রায়:",
        "opts": {"en": ["4.19 MeV", "2.25 MeV", "9.31 MeV", "18.6 MeV"], "bn": ["4.19 MeV", "2.25 MeV", "9.31 MeV", "18.6 MeV"]},
        "correct": 0,
        "expl_en": "Q = 0.0045 amu × 931.5 MeV/amu ≈ 4.19 MeV.",
        "expl_bn": "মুক্ত শক্তি Q = ০.০০৪৫ × ৯৩১.৫ = ৪.১৯ MeV।"
    },
    {
        "id": "PHY-026", "exam": "CUET", "subject": "Physics", "topic": "Semiconductor Electronics", "difficulty": "Easy",
        "en": "In a p-n junction diode under forward bias, the barrier potential across the depletion layer:",
        "bn": "সম্মুখ বায়াসে (Forward Bias) থাকা একটি p-n সংযোগ ডায়োডে নিঃশেষিত স্তরের (Depletion layer) বিভব প্রাচীর:",
        "opts": {"en": ["Decreases", "Increases", "Remains unchanged", "Becomes zero immediately"], "bn": ["হ্রাস পায়", "বৃদ্ধি পায়", "অপরিবর্তিত থাকে", "তৎক্ষণাৎ শূন্য হয়ে যায়"]},
        "correct": 0,
        "expl_en": "External forward bias reduces the barrier potential and depletion layer width.",
        "expl_bn": "সম্মুখ বায়াস অভ্যন্তরীণ বিভব প্রাচীর হ্রাস করে।"
    },

    # =========================================================================
    # CHEMISTRY - INORGANIC, ORGANIC, PHYSICAL
    # =========================================================================
    {
        "id": "CHEM-001", "exam": "JEE", "subject": "Chemistry", "topic": "Chemical Bonding", "difficulty": "Easy",
        "en": "According to Molecular Orbital Theory (MOT), which of the following species is diamagnetic and has a bond order of 3?",
        "bn": "আণবিক কক্ষক তত্ত্ব (MOT) অনুসারে, নিচের কোন প্রজাতিটি তিরশ্চৌম্বকীয় (diamagnetic) এবং এর বন্ধন ক্রম 3?",
        "opts": {"en": ["N₂", "O₂", "NO", "C₂⁺"], "bn": ["N₂", "O₂", "NO", "C₂⁺"]},
        "correct": 0,
        "expl_en": "N₂ has 14 electrons: Bond Order = (10 - 4)/2 = 3. All electrons are paired, making N₂ diamagnetic.",
        "expl_bn": "N₂ অণুতে ১৪টি ইলেকট্রন রয়েছে। বন্ধন ক্রম = ৩। কোনো বিজোড় ইলেকট্রন নেই, তাই তিরশ্চৌম্বকীয়।"
    },
    {
        "id": "CHEM-002", "exam": "NEET", "subject": "Chemistry", "topic": "Electrochemistry", "difficulty": "Medium",
        "en": "The standard electrode potential for Zn²⁺/Zn is -0.76 V and for Cu²⁺/Cu is +0.34 V. The standard EMF of the cell Zn | Zn²⁺ || Cu²⁺ | Cu is:",
        "bn": "Zn²⁺/Zn এর প্রমাণ তড়িৎদ্বার বিভব -0.76 V এবং Cu²⁺/Cu এর +0.34 V। Zn | Zn²⁺ || Cu²⁺ | Cu কোষের প্রমাণ তড়িচ্চালক বল কত?",
        "opts": {"en": ["+1.10 V", "-1.10 V", "+0.42 V", "-0.42 V"], "bn": ["+1.10 V", "-1.10 V", "+0.42 V", "-0.42 V"]},
        "correct": 0,
        "expl_en": "E°_cell = E°_cathode - E°_anode = +0.34 V - (-0.76 V) = +1.10 V.",
        "expl_bn": "E°_cell = E°_ক্যাথোড - E°_অ্যানোড = ০.৩৪ - (-০.৭৬) = +১.১০ V।"
    },
    {
        "id": "CHEM-003", "exam": "NEET", "subject": "Chemistry", "topic": "Organic Chemistry", "difficulty": "Medium",
        "en": "Which of the following compounds gives a positive Iodoform test upon reaction with I₂/NaOH?",
        "bn": "নিচের কোন যৌগটি I₂/NaOH সহযোগে বিক্রিয়ায় আয়োডোফর্ম পরীক্ষা দেয়?",
        "opts": {"en": ["Ethanol (CH₃CH₂OH)", "Methanol (CH₃OH)", "Benzophenone (C₆H₅COC₆H₅)", "Diethyl ether (C₂H₅OC₂H₅)"], "bn": ["ইথানল (CH₃CH₂OH)", "মিথানল (CH₃OH)", "বেনজোফেনন", "ডাইইথাইল ইথার"]},
        "correct": 0,
        "expl_en": "Compounds containing CH₃-CH(OH)- or CH₃-C=O group undergo iodoform reaction. Ethanol oxidizes to ethanal (CH₃CHO) which gives yellow CHI₃ precipitate.",
        "expl_bn": "যেসব যৌগে CH₃-CH(OH)- বা CH₃-C=O গ্রুপ থাকে তারা আয়োডোফর্ম বিক্রিয়া দেয়। ইথানল জারিত হয়ে CH₃CHO গঠন করে ও হলুদ CHI₃ অধঃক্ষেপ ফেলে।"
    },
    {
        "id": "CHEM-004", "exam": "JEE", "subject": "Chemistry", "topic": "Coordination Compounds", "difficulty": "Hard",
        "en": "The hybridization and magnetic character of the complex [Fe(CN)₆]³⁻ are respectively (Fe atomic number = 26):",
        "bn": "[Fe(CN)₆]³⁻ জটিল আয়নের সংকরায়ণ (Hybridization) এবং চৌম্বক প্রকৃতি যথাক্রমে:",
        "opts": {"en": ["d²sp³, Paramagnetic (1 unpaired electron)", "sp³d², Paramagnetic (5 unpaired electrons)", "d²sp³, Diamagnetic", "sp³d², Diamagnetic"], "bn": ["d²sp³, পরাচৌম্বকীয় (১টি বিজোড় ইলেকট্রন)", "sp³d², পরাচৌম্বকীয় (৫টি বিজোড় ইলেকট্রন)", "d²sp³, তিরশ্চৌম্বকীয়", "sp³d², তিরশ্চৌম্বকীয়"]},
        "correct": 0,
        "expl_en": "Fe³⁺ has 3d⁵ configuration. CN⁻ is a strong field ligand causing pairing of electrons: t_2g⁵ e_g⁰ (1 unpaired electron). Inner orbital complex d²sp³, paramagnetic.",
        "expl_bn": "Fe³⁺ এর 3d⁵ বিন্যাস। CN⁻ তীব্র লিগ্যান্ড হওয়ায় ইলেকট্রন জোর বাঁধে: t_2g⁵ e_g⁰। সংকরায়ণ d²sp³, ১টি বিজোড় ইলেকট্রন থাকায় পরাচৌম্বকীয়।"
    },
    {
        "id": "CHEM-005", "exam": "WBJEE", "subject": "Chemistry", "topic": "Chemical Kinetics", "difficulty": "Easy",
        "en": "For a first-order chemical reaction, the half-life period (t_1/2) is related to the rate constant (k) by:",
        "bn": "প্রথম ক্রমের রাসায়নিক বিক্রিয়ার ক্ষেত্রে অর্ধায়ু (t_1/2) এবং হার ধ্রুবক (k) এর সম্পর্ক:",
        "opts": {"en": ["t_1/2 = 0.693 / k", "t_1/2 = 1 / (k [A]₀)", "t_1/2 = [A]₀ / (2k)", "t_1/2 = 2.303 / k"], "bn": ["t_1/2 = 0.693 / k", "t_1/2 = 1 / (k [A]₀)", "t_1/2 = [A]₀ / (2k)", "t_1/2 = 2.303 / k"]},
        "correct": 0,
        "expl_en": "For first order reaction: k = (2.303 / t) log(1 / 0.5) = 0.693 / t_1/2 => t_1/2 = 0.693 / k.",
        "expl_bn": "প্রথম ক্রম বিক্রিয়ায় অর্ধায়ু t_1/2 = ০.৬৯৩ / k, যা প্রারম্ভিক ঘনমাত্রার ওপর নির্ভর করে না।"
    },

    # =========================================================================
    # MATHEMATICS - CALCULUS, ALGEBRA, COORDINATE GEOMETRY
    # =========================================================================
    {
        "id": "MATH-001", "exam": "JEE", "subject": "Mathematics", "topic": "Definite Integrals", "difficulty": "Medium",
        "en": "The value of the definite integral ∫[0 to π/2] (sin x) / (sin x + cos x) dx is:",
        "bn": "নির্দিষ্ট সমাকলনের মান নির্ণয় করো: ∫[0 থেকে π/2] (sin x) / (sin x + cos x) dx:",
        "opts": {"en": ["π/4", "π/2", "π", "1"], "bn": ["π/4", "π/2", "π", "1"]},
        "correct": 0,
        "expl_en": "Using King's rule ∫[0 to a] f(x)dx = ∫[0 to a] f(a-x)dx: 2I = ∫[0 to π/2] 1 dx = π/2 => I = π/4.",
        "expl_bn": "∫[0 to a] f(x)dx = ∫[0 to a] f(a-x)dx সূত্র প্রয়োগ করে: 2I = π/২ => I = π/৪।"
    },
    {
        "id": "MATH-002", "exam": "WBJEE", "subject": "Mathematics", "topic": "Matrices & Determinants", "difficulty": "Easy",
        "en": "If A is a 3 × 3 non-singular square matrix such that |A| = 4, then the determinant of its adjoint |adj(A)| is equal to:",
        "bn": "যদি A একটি ৩ × ৩ বর্গ ম্যাট্রিক্স হয় এবং |A| = ৪ হয়, তবে |adj(A)| এর মান কত?",
        "opts": {"en": ["16", "64", "4", "12"], "bn": ["16", "64", "4", "12"]},
        "correct": 0,
        "expl_en": "|adj(A)| = |A|^(n-1). For n = 3: |adj(A)| = |A|^(3-1) = |A|² = 4² = 16.",
        "expl_bn": "|adj(A)| = |A|^(n-১)। এখানে n = ৩ হওয়ায়: |adj(A)| = ৪² = ১৬।"
    },
    {
        "id": "MATH-003", "exam": "JEE", "subject": "Mathematics", "topic": "Coordinate Geometry", "difficulty": "Medium",
        "en": "The equation of the tangent to the parabola y² = 8x at the point (2, 4) is:",
        "bn": "y² = 8x অধিবৃত্তের (২, ৪) বিন্দুতে স্পর্শকের সমীকরণ হলো:",
        "opts": {"en": ["x - y + 2 = 0", "x + y - 6 = 0", "2x - y = 0", "x - 2y + 6 = 0"], "bn": ["x - y + 2 = 0", "x + y - 6 = 0", "2x - y = 0", "x - 2y + 6 = 0"]},
        "correct": 0,
        "expl_en": "Tangent at (x₁, y₁): y y₁ = 2a(x + x₁). Here 4a = 8 => 2a = 4. y(4) = 4(x + 2) => 4y = 4x + 8 => x - y + 2 = 0.",
        "expl_bn": "স্পর্শক সমীকরণ: y y₁ = 2a(x + x₁)। y(৪) = ৪(x + ২) => ৪y = ৪x + ৮ => x - y + ২ = ০।"
    },
    {
        "id": "MATH-004", "exam": "CUET", "subject": "Mathematics", "topic": "Probability", "difficulty": "Easy",
        "en": "Two fair dice are thrown simultaneously. The probability of obtaining a total sum of 8 is:",
        "bn": "দুটি নিরপেক্ষ ছক্কা একসাথে গড়িয়ে দিলে মোট সমষ্টি ৮ হওয়ার সম্ভাবনা কত?",
        "opts": {"en": ["5 / 36", "1 / 6", "7 / 36", "1 / 9"], "bn": ["5 / 36", "1 / 6", "7 / 36", "1 / 9"]},
        "correct": 0,
        "expl_en": "Favourable outcomes for sum = 8: (2,6), (3,5), (4,4), (5,3), (6,2) => 5 outcomes out of 36 total. P = 5/36.",
        "expl_bn": "সমষ্টি ৮ হওয়ার অনুকূল ঘটনা: (২,৬), (৩,৫), (৪,৪), (৫,৩), (৬,২) = ৫টি। মোট ফলাফল = ৩৬। সম্ভাবনা = ৫/৩৬।"
    },

    # =========================================================================
    # BIOLOGY - BOTANY & ZOOLOGY
    # =========================================================================
    {
        "id": "BIO-001", "exam": "NEET", "subject": "Biology", "topic": "Genetics & Molecular Biology", "difficulty": "Easy",
        "en": "Which of the following enzymes synthesizes short RNA primers required for DNA replication?",
        "bn": "কোন উৎসেচকটি ডিএনএ রেপ্লিকেশনের জন্য প্রয়োজনীয় ক্ষণস্থায়ী আরএনএ প্রাইমার তৈরি করে?",
        "opts": {"en": ["RNA Primase", "DNA Ligase", "DNA Polymerase I", "Helicase"], "bn": ["আরএনএ প্রাইমেজ", "ডিএনএ লাইগেজ", "ডিএনএ পলিমারেজ I", "হেলিকোজ"]},
        "correct": 0,
        "expl_en": "RNA Primase synthesizes short RNA primers providing free 3'-OH group for DNA polymerase to initiate replication.",
        "expl_bn": "আরএনএ প্রাইমেজ আরএনএ প্রাইমার তৈরি করে যা ডিএনএ পলিমারেজকে রেপ্লিকেশন শুরু করতে 3'-OH প্রান্ত দেয়।"
    },
    {
        "id": "BIO-002", "exam": "NEET", "subject": "Biology", "topic": "Human Physiology", "difficulty": "Medium",
        "en": "In the human nephron, maximum reabsorption of water, glucose, and essential electrolytes takes place in:",
        "bn": "মানুষের নেফ্রনে সর্বাধিক পরিমাণ জল, গ্লুকোজ ও প্রয়োজনীয় ইলেক্ট্রোলাইট পুনঃশোষিত হয় কোথায়?",
        "opts": {"en": ["Proximal Convoluted Tubule (PCT)", "Loop of Henle", "Distal Convoluted Tubule (DCT)", "Collecting Duct"], "bn": ["নিকটবর্তী সংবর্ত নালিকা (PCT)", "হেনলির লুপ", "দূরবর্তী সংবর্ত নালিকা (DCT)", "সংগ্রাহী নালিকা"]},
        "correct": 0,
        "expl_en": "PCT is lined by simple cuboidal brush border epithelium which reabsorbs nearly 70-80% of electrolytes and 100% of filtered glucose.",
        "expl_bn": "PCT-তে ব্রাশ বর্ডার এপিথেলিয়াম থাকে এবং এখানেই গ্লুকোজ ও ৭০-৮০% ইলেক্ট্রোলাইটের সর্বাধিক পুনঃশোষণ ঘটে।"
    },
    {
        "id": "BIO-003", "exam": "NEET", "subject": "Biology", "topic": "Plant Physiology", "difficulty": "Medium",
        "en": "In C₄ plants, the primary carbon dioxide (CO₂) acceptor and the primary carboxylation enzyme are respectively:",
        "bn": "C₄ উদ্ভিদে প্রাথমিক CO₂ গ্রাহক এবং প্রাথমিক কার্বক্সিলেশন উৎসেচক যথাক্রমে:",
        "opts": {"en": ["Phosphoenolpyruvate (PEP) & PEP Carboxylase", "RuBP & RuBisCO", "PGA & PEP Carboxylase", "Oxaloacetic Acid & RuBisCO"], "bn": ["ফসফোএনলপাইরুভেট (PEP) ও PEP কার্বক্সিলেজ", "RuBP ও রুবিস্কো", "PGA ও PEP কার্বক্সিলেজ", "অক্সালোঅ্যাসিটিক অ্যাসিড ও রুবিস্কো"]},
        "correct": 0,
        "expl_en": "In C₄ mesophyll cells, PEP (3C) accepts CO₂ via PEP Carboxylase (PEPcase) to form Oxaloacetic acid (4C).",
        "expl_bn": "C₄ উদ্ভিদের মেসোফিল কোষে PEP কার্বক্সিলেজের উপস্থিতিতে PEP প্রাথমিক CO₂ গ্রহণ করে ৪-কার্বন যুক্ত OAA তৈরি করে।"
    },
    {
        "id": "BIO-004", "exam": "NEET", "subject": "Biology", "topic": "Ecology & Environment", "difficulty": "Easy",
        "en": "The pyramid of energy in any terrestrial or aquatic ecological food chain is always:",
        "bn": "যেকোনো স্থলজ বা জলজ বাস্তুতন্ত্রের শক্তির পিরামিড সর্বদা কীরূপ হয়?",
        "opts": {"en": ["Always Upright", "Always Inverted", "Spindle shaped", "Inverted in aquatic and upright in grassland"], "bn": ["সর্বদা খাড়া (Upright)", "সর্বদা উল্টানো (Inverted)", "মাকু আকৃতির", "জলে উল্টানো ও ভূমিতে খাড়া"]},
        "correct": 0,
        "expl_en": "According to Lindeman's 10% law, energy decreases at each successive trophic level due to heat loss, so energy pyramids are strictly always upright.",
        "expl_bn": "লিন্ডেম্যানের ১০% নিয়ম অনুসারে এক পুষ্টিস্তর থেকে অন্য পুষ্টিস্তরে শক্তির অপচয় ঘটে, তাই শক্তির পিরামিড সর্বদা খাড়া থাকে।"
    }
]

# Write to JSON
with open(r'c:\AVAI_PREP\data\physics_questions.json', 'w', encoding='utf-8') as f:
    json.dump(master_questions, f, indent=2, ensure_ascii=False)

# Write to JS
with open(r'c:\AVAI_PREP\data\physics_questions.js', 'w', encoding='utf-8') as f:
    f.write('// Auto-generated Master Questions Dataset for AVAI Prep\n')
    f.write('window.PHYSICS_QUESTIONS_DATA = ' + json.dumps(master_questions, indent=2, ensure_ascii=False) + ';\n')

# Write to CSV
fields = [
    'Exam', 'Subject', 'Topic', 'Difficulty',
    'Question_EN', 'Question_BN',
    'Opt1_EN', 'Opt2_EN', 'Opt3_EN', 'Opt4_EN',
    'Opt1_BN', 'Opt2_BN', 'Opt3_BN', 'Opt4_BN',
    'Correct', 'Expl_EN', 'Expl_BN'
]

csv_path = r'c:\AVAI_PREP\data\physics_for_you_master_questions.csv'
with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    for q in master_questions:
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
            q.get('en', ''),
            q.get('bn', ''),
            opts_en[0], opts_en[1], opts_en[2], opts_en[3],
            opts_bn[0], opts_bn[1], opts_bn[2], opts_bn[3],
            corr,
            q.get('expl_en', ''),
            q.get('expl_bn', '')
        ])

# Write to TSV for instant clipboard copy paste
tsv_path = r'c:\AVAI_PREP\data\master_questions_copy_paste.tsv'
with open(tsv_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(fields)
    for q in master_questions:
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
            q.get('en', ''),
            q.get('bn', ''),
            opts_en[0], opts_en[1], opts_en[2], opts_en[3],
            opts_bn[0], opts_bn[1], opts_bn[2], opts_bn[3],
            corr,
            q.get('expl_en', ''),
            q.get('expl_bn', '')
        ])

print(f"Generated {len(master_questions)} questions in JSON, JS, CSV, and TSV!")
