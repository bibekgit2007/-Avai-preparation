/**
 * AVAI Preparation Platform - Official Examination Syllabus Registry
 * Contains hierarchical Unit -> Chapter -> Topic mapping based on official NTA/NMC NEET (UG) & Competitive Exam frameworks.
 */

(function(window) {
    'use strict';

    const EXAM_SYLLABUS_REGISTRY = {
        'NEET': {
            'Biology': [
                {
                    unitId: 'BIO_UNIT_01',
                    unitNo: 1,
                    unitTitle: 'Diversity in Living World',
                    icon: '🌿',
                    classLevel: 'Class 11',
                    chapters: [
                        {
                            id: 'BIO_CH_01',
                            title: 'The Living World',
                            keywords: ['living world', 'taxonomic', 'binomial nomenclature', 'systematics', 'hierarchy', 'species', 'herbarium', 'botanical garden']
                        },
                        {
                            id: 'BIO_CH_02',
                            title: 'Biological Classification',
                            keywords: ['biological classification', 'monera', 'protista', 'fungi', 'archae', 'methanogen', 'lichens', 'viruses', 'viroids', 'dikaryophase']
                        },
                        {
                            id: 'BIO_CH_03',
                            title: 'Plant Kingdom',
                            keywords: ['plant kingdom', 'algae', 'bryophytes', 'pteridophytes', 'gymnosperms', 'angiosperms', 'rhodophyceae', 'floridean', 'cycas', 'coralloid']
                        },
                        {
                            id: 'BIO_CH_04',
                            title: 'Animal Kingdom',
                            keywords: ['animal kingdom', 'porifera', 'coelenterata', 'annelida', 'arthropoda', 'mollusca', 'echinodermata', 'chordata', 'symmetry', 'coelom', 'malpighian']
                        }
                    ]
                },
                {
                    unitId: 'BIO_UNIT_02',
                    unitNo: 2,
                    unitTitle: 'Structural Organisation in Animals and Plants',
                    icon: '🔬',
                    classLevel: 'Class 11',
                    chapters: [
                        {
                            id: 'BIO_CH_05',
                            title: 'Morphology of Flowering Plants',
                            keywords: ['morphology of flowering plants', 'root', 'stem', 'leaf', 'inflorescence', 'flower', 'fruit', 'seed', 'placentation', 'pneumatophores', 'dianthus']
                        },
                        {
                            id: 'BIO_CH_06',
                            title: 'Anatomy of Flowering Plants',
                            keywords: ['anatomy of flowering plants', 'casparian', 'endodermis', 'xylem', 'phloem', 'vascular bundle', 'heartwood', 'sapwood', 'secondary growth', 'meristem']
                        },
                        {
                            id: 'BIO_CH_07',
                            title: 'Structural Organisation in Animals',
                            keywords: ['structural organisation in animals', 'epithelial', 'connective', 'cockroach', 'frog', 'anal styles', 'ciliated', 'tissue']
                        }
                    ]
                },
                {
                    unitId: 'BIO_UNIT_03',
                    unitNo: 3,
                    unitTitle: 'Cell Structure and Function',
                    icon: '🧬',
                    classLevel: 'Class 11',
                    chapters: [
                        {
                            id: 'BIO_CH_08',
                            title: 'Cell: The Unit of Life',
                            keywords: ['cell: the unit of life', 'cell biology', 'organelle', 'mitochondria', 'chloroplast', 'ribosome', 'endomembrane', 'golgi', 'lysosome', 'nuclear pore', 'nucleus', 'fluid mosaic']
                        },
                        {
                            id: 'BIO_CH_09',
                            title: 'Biomolecules',
                            keywords: ['biomolecules', 'enzyme', 'michaelis', 'km', 'vmax', 'competitive inhibition', 'protein', 'carbohydrate', 'chargaff', 'nucleic acid']
                        },
                        {
                            id: 'BIO_CH_10',
                            title: 'Cell Cycle and Cell Division',
                            keywords: ['cell cycle', 'cell division', 'mitosis', 'meiosis', 'prophase', 'pachytene', 'crossing over', 'recombinase', 's phase', 'interphase', 'metaphase']
                        }
                    ]
                },
                {
                    unitId: 'BIO_UNIT_04',
                    unitNo: 4,
                    unitTitle: 'Plant Physiology',
                    icon: '🌱',
                    classLevel: 'Class 11',
                    chapters: [
                        {
                            id: 'BIO_CH_11',
                            title: 'Photosynthesis in Higher Plants',
                            keywords: ['photosynthesis', 'rubisco', 'pep carboxylase', 'c3', 'c4', 'kranz', 'light reaction', 'photolysis', 'photophosphorylation', 'chemiosmosis', 'photorespiration']
                        },
                        {
                            id: 'BIO_CH_12',
                            title: 'Respiration in Plants',
                            keywords: ['respiration in plants', 'glycolysis', 'krebs', 'tca', 'electron transport', 'succinate', 'fumarate', 'atp', 'fermentation', 'respiratory quotient']
                        },
                        {
                            id: 'BIO_CH_13',
                            title: 'Plant Growth and Development',
                            keywords: ['plant growth', 'auxin', 'gibberellin', 'cytokinin', 'abscisic acid', 'ethylene', 'stress hormone', 'differentiation', 'photoperiodism']
                        },
                        {
                            id: 'BIO_CH_14',
                            title: 'Water & Mineral Nutrition in Plants',
                            keywords: ['water potential', 'mineral nutrition', 'manganese', 'osmosis', 'transpiration', 'nitrogen fixation']
                        }
                    ]
                },
                {
                    unitId: 'BIO_UNIT_05',
                    unitNo: 5,
                    unitTitle: 'Human Physiology',
                    icon: '🫀',
                    classLevel: 'Class 11',
                    chapters: [
                        {
                            id: 'BIO_CH_15',
                            title: 'Digestion and Absorption',
                            keywords: ['digestion', 'absorption', 'parietal', 'oxyntic', 'castle', 'intrinsic factor', 'pepsin', 'stomach', 'gastric']
                        },
                        {
                            id: 'BIO_CH_16',
                            title: 'Breathing and Exchange of Gases',
                            keywords: ['breathing', 'exchange of gases', 'respiratory', 'bicarbonate', 'chloride shift', 'alveoli', 'haemoglobin', 'asthma', 'emphysema']
                        },
                        {
                            id: 'BIO_CH_17',
                            title: 'Body Fluids and Circulation',
                            keywords: ['body fluids', 'circulation', 'heart', 'san', 'sino-atrial', 'cardiac cycle', 'ecg', 'blood pressure', 'pacemaker']
                        },
                        {
                            id: 'BIO_CH_18',
                            title: 'Excretory Products and Their Elimination',
                            keywords: ['excretory', 'nephron', 'henle', 'counter-current', 'osmolarity', 'vasa recta', 'kidney', 'dialysis', 'urea', 'urine']
                        },
                        {
                            id: 'BIO_CH_19',
                            title: 'Locomotion and Movement',
                            keywords: ['locomotion', 'movement', 'sarcomere', 'sliding filament', 'actin', 'myosin', 'h zone', 'muscle', 'skeletal', 'joints']
                        },
                        {
                            id: 'BIO_CH_20',
                            title: 'Neural Control and Coordination',
                            keywords: ['neural', 'neuron', 'action potential', 'resting membrane', 'sodium-potassium', 'synapse', 'brain', 'reflex']
                        },
                        {
                            id: 'BIO_CH_21',
                            title: 'Chemical Coordination and Integration',
                            keywords: ['chemical coordination', 'endocrine', 'hormone', 'thyrocalcitonin', 'adrenaline', 'pituitary', 'thyroid', 'adrenal', 'insulin']
                        }
                    ]
                },
                {
                    unitId: 'BIO_UNIT_06',
                    unitNo: 6,
                    unitTitle: 'Reproduction',
                    icon: '🌸',
                    classLevel: 'Class 12',
                    chapters: [
                        {
                            id: 'BIO_CH_22',
                            title: 'Sexual Reproduction in Flowering Plants',
                            keywords: ['flowering plants', 'pollen', 'sporopollenin', 'embryo sac', 'double fertilization', 'triple fusion', 'endosperm', 'apomixis']
                        },
                        {
                            id: 'BIO_CH_23',
                            title: 'Human Reproduction',
                            keywords: ['human reproduction', 'leydig', 'spermatogenesis', 'oogenesis', 'menstrual', 'ovulation', 'lh surge', 'fertilization', 'placenta']
                        },
                        {
                            id: 'BIO_CH_24',
                            title: 'Reproductive Health',
                            keywords: ['reproductive health', 'contraception', 'iud', 'cut', 'zift', 'iut', 'gift', 'art', 'infertility', 'amniocentesis']
                        }
                    ]
                },
                {
                    unitId: 'BIO_UNIT_07',
                    unitNo: 7,
                    unitTitle: 'Genetics and Evolution',
                    icon: '🧬',
                    classLevel: 'Class 12',
                    chapters: [
                        {
                            id: 'BIO_CH_25',
                            title: 'Principles of Inheritance and Variation',
                            keywords: ['principles of inheritance', 'incomplete dominance', 'klinefelter', 'sickle-cell', 'mendel', 'linkage', 'down syndrome', 'turner', 'morgan']
                        },
                        {
                            id: 'BIO_CH_26',
                            title: 'Molecular Basis of Inheritance',
                            keywords: ['molecular basis of inheritance', 'dna', 'griffith', 'genetic code', 'aug', 'lac operon', 'allolactose', 'transcription', 'translation', 'hgp', 'replication']
                        },
                        {
                            id: 'BIO_CH_27',
                            title: 'Evolution',
                            keywords: ['evolution', 'miller', 'origin of life', 'homologous', 'bougainvillea', 'hardy-weinberg', 'analogous', 'natural selection', 'darwin']
                        }
                    ]
                },
                {
                    unitId: 'BIO_UNIT_08',
                    unitNo: 8,
                    unitTitle: 'Biology and Human Welfare',
                    icon: '🏥',
                    classLevel: 'Class 12',
                    chapters: [
                        {
                            id: 'BIO_CH_28',
                            title: 'Human Health and Disease',
                            keywords: ['human health and disease', 'malaria', 'sporozoite', 'plasmodium', 'immunity', 'colostrum', 'iga', 'antibody', 'aids', 'cancer']
                        },
                        {
                            id: 'BIO_CH_29',
                            title: 'Microbes in Human Welfare',
                            keywords: ['microbes in human welfare', 'statins', 'monascus', 'cyclosporin', 'trichoderma', 'biogas', 'sewage', 'biofertilizer', 'antibiotics']
                        }
                    ]
                },
                {
                    unitId: 'BIO_UNIT_09',
                    unitNo: 9,
                    unitTitle: 'Biotechnology and Its Applications',
                    icon: '🧪',
                    classLevel: 'Class 12',
                    chapters: [
                        {
                            id: 'BIO_CH_30',
                            title: 'Biotechnology: Principles and Processes',
                            keywords: ['biotechnology: principles', 'restriction endonuclease', 'ecori', 'palindromic', 'taq polymerase', 'pcr', 'electrophoresis', 'plasmid', 'gel']
                        },
                        {
                            id: 'BIO_CH_31',
                            title: 'Biotechnology and Its Applications',
                            keywords: ['biotechnology and its applications', 'bt cotton', 'protoxin', 'gene therapy', 'ada deficiency', 'scid', 'transgenic', 'rnai']
                        }
                    ]
                },
                {
                    unitId: 'BIO_UNIT_10',
                    unitNo: 10,
                    unitTitle: 'Ecology and Environment',
                    icon: '🌍',
                    classLevel: 'Class 12',
                    chapters: [
                        {
                            id: 'BIO_CH_32',
                            title: 'Organisms and Populations',
                            keywords: ['organisms and populations', 'allen', 'adaptations', 'logistic growth', 'carrying capacity', 'population']
                        },
                        {
                            id: 'BIO_CH_33',
                            title: 'Ecosystem',
                            keywords: ['ecosystem', 'pyramid of energy', 'productivity', 'secondary productivity', 'trophic', 'decomposition']
                        },
                        {
                            id: 'BIO_CH_34',
                            title: 'Biodiversity and Conservation',
                            keywords: ['biodiversity and conservation', 'evil quartet', 'habitat loss', 'ex-situ', 'botanical garden', 'humboldt', 'species-area']
                        },
                        {
                            id: 'BIO_CH_35',
                            title: 'Environmental Issues',
                            keywords: ['environmental issues', 'biomagnification', 'ddt', 'montreal protocol', 'ozone', 'pollution']
                        }
                    ]
                }
            ],
            'Physics': [
                {
                    unitId: 'PHY_UNIT_01',
                    unitNo: 1,
                    unitTitle: 'Physics and Measurement',
                    icon: '📏',
                    chapters: [
                        { id: 'PHY_CH_01', title: 'Units, Dimensions & Errors', keywords: ['measurement', 'dimensions', 'screw gauge', 'least count', 'vernier', 'errors'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_02',
                    unitNo: 2,
                    unitTitle: 'Kinematics',
                    icon: '🏎️',
                    chapters: [
                        { id: 'PHY_CH_02', title: 'Motion in a Straight Line & Plane', keywords: ['kinematics', 'straight line', 'projectile', 'relative velocity', 'instantaneous'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_03',
                    unitNo: 3,
                    unitTitle: 'Laws of Motion',
                    icon: '⚖️',
                    chapters: [
                        { id: 'PHY_CH_03', title: 'Newton Laws of Motion & Friction', keywords: ['laws of motion', 'equilibrium', 'friction', 'circular motion', 'banking'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_04',
                    unitNo: 4,
                    unitTitle: 'Work, Energy, and Power',
                    icon: '⚡',
                    chapters: [
                        { id: 'PHY_CH_04', title: 'Work, Energy, Power & Collisions', keywords: ['work', 'energy', 'power', 'collision', 'conservative', 'spring'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_05',
                    unitNo: 5,
                    unitTitle: 'Rotational Motion',
                    icon: '🎡',
                    chapters: [
                        { id: 'PHY_CH_05', title: 'Centre of Mass & Rotational Dynamics', keywords: ['rotational', 'centre of mass', 'moment of inertia', 'torque', 'angular momentum', 'rolling'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_06',
                    unitNo: 6,
                    unitTitle: 'Gravitation',
                    icon: '🪐',
                    chapters: [
                        { id: 'PHY_CH_06', title: 'Gravitation & Satellites', keywords: ['gravitation', 'kepler', 'escape velocity', 'orbital', 'acceleration due to gravity'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_07',
                    unitNo: 7,
                    unitTitle: 'Properties of Solids and Liquids',
                    icon: '💧',
                    chapters: [
                        { id: 'PHY_CH_07', title: 'Elasticity, Viscosity & Fluid Mechanics', keywords: ['solids and liquids', 'elasticity', 'hooke', 'bernoulli', 'surface tension', 'viscosity', 'stokes'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_08',
                    unitNo: 8,
                    unitTitle: 'Thermodynamics & KTG',
                    icon: '🔥',
                    chapters: [
                        { id: 'PHY_CH_08', title: 'Thermodynamic Laws & Heat Engines', keywords: ['thermodynamics', 'carnot', 'isothermal', 'adiabatic', 'entropy', 'first law'] },
                        { id: 'PHY_CH_09', title: 'Kinetic Theory of Gases', keywords: ['kinetic theory', 'rms speed', 'mean free path', 'degrees of freedom'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_09',
                    unitNo: 9,
                    unitTitle: 'Oscillations and Waves',
                    icon: '〰️',
                    chapters: [
                        { id: 'PHY_CH_10', title: 'Simple Harmonic Motion (SHM)', keywords: ['oscillations', 'shm', 'pendulum', 'frequency', 'resonance'] },
                        { id: 'PHY_CH_11', title: 'Waves & Sound', keywords: ['waves', 'doppler', 'standing waves', 'beats', 'sound speed'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_10',
                    unitNo: 10,
                    unitTitle: 'Electrostatics',
                    icon: '⚡',
                    chapters: [
                        { id: 'PHY_CH_12', title: 'Electric Charges, Field & Gauss Law', keywords: ['electrostatics', 'coulomb', 'gauss', 'electric field', 'dipole', 'flux', 'sphere cavity'] },
                        { id: 'PHY_CH_13', title: 'Electric Potential & Capacitors', keywords: ['potential', 'capacitor', 'dielectric', 'capacitance', 'stored energy'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_11',
                    unitNo: 11,
                    unitTitle: 'Current Electricity',
                    icon: '💡',
                    chapters: [
                        { id: 'PHY_CH_14', title: 'Current Electricity & Circuit Laws', keywords: ['current electricity', 'ohm', 'kirchhoff', 'wheatstone', 'potentiometer', 'meter bridge', 'two conductors'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_12',
                    unitNo: 12,
                    unitTitle: 'Magnetic Effects of Current & Magnetism',
                    icon: '🧲',
                    chapters: [
                        { id: 'PHY_CH_15', title: 'Magnetic Field & Ampere Law', keywords: ['magnetic effects', 'biot-savart', 'ampere', 'lorentz', 'cyclotron', 'solenoid'] },
                        { id: 'PHY_CH_16', title: 'Magnetism & Matter', keywords: ['magnetism', 'magnetic moment', 'hysteresis', 'dia', 'para', 'ferro', 'coil'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_13',
                    unitNo: 13,
                    unitTitle: 'Electromagnetic Induction & Alternating Currents',
                    icon: '🔌',
                    chapters: [
                        { id: 'PHY_CH_17', title: 'Electromagnetic Induction (EMI)', keywords: ['electromagnetic induction', 'faraday', 'lenz', 'self induction', 'mutual induction'] },
                        { id: 'PHY_CH_18', title: 'Alternating Currents & LCR Circuits', keywords: ['alternating currents', 'lcr', 'resonance', 'power factor', 'transformer', 'impedance'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_14',
                    unitNo: 14,
                    unitTitle: 'Electromagnetic Waves',
                    icon: '📡',
                    chapters: [
                        { id: 'PHY_CH_19', title: 'Electromagnetic Waves & Spectrum', keywords: ['electromagnetic waves', 'displacement current', 'spectrum', 'maxwell'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_15',
                    unitNo: 15,
                    unitTitle: 'Optics',
                    icon: '🔭',
                    chapters: [
                        { id: 'PHY_CH_20', title: 'Ray Optics & Optical Instruments', keywords: ['optics', 'ray optics', 'prism', 'tir', 'total internal reflection', 'lens', 'mirror', 'microscope', 'telescope'] },
                        { id: 'PHY_CH_21', title: 'Wave Optics & Interference', keywords: ['wave optics', 'interference', 'diffraction', 'polarization', 'young', 'fringe', 'brewster'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_16',
                    unitNo: 16,
                    unitTitle: 'Modern Physics',
                    icon: '⚛️',
                    chapters: [
                        { id: 'PHY_CH_22', title: 'Dual Nature of Radiation & Matter', keywords: ['dual nature', 'photoelectric', 'work function', 'de broglie', 'stopping potential'] },
                        { id: 'PHY_CH_23', title: 'Atoms and Nuclei', keywords: ['atoms', 'nuclei', 'bohr', 'hydrogen spectrum', 'binding energy', 'radioactivity', 'decay', 'half life'] },
                        { id: 'PHY_CH_24', title: 'Electronic Devices (Semiconductors)', keywords: ['electronic devices', 'semiconductor', 'p-n junction', 'diode', 'zener', 'logic gates', 'solar cell'] }
                    ]
                },
                {
                    unitId: 'PHY_UNIT_17',
                    unitNo: 17,
                    unitTitle: 'Experimental Skills',
                    icon: '📐',
                    chapters: [
                        { id: 'PHY_CH_25', title: 'Practical Skills & Lab Instruments', keywords: ['experimental skills', 'metre bridge', 'screw gauge', 'travelling microscope', 'potentiometer experiment'] }
                    ]
                }
            ],
            'Chemistry': [
                {
                    unitId: 'CHEM_UNIT_01',
                    unitNo: 1,
                    unitTitle: 'Physical Chemistry',
                    icon: '⚗️',
                    chapters: [
                        { id: 'CHEM_CH_01', title: 'Some Basic Concepts of Chemistry (Mole Concept)', keywords: ['basic concepts', 'mole concept', 'molarity', 'stoichiometry', 'empirical formula', 'avogadro'] },
                        { id: 'CHEM_CH_02', title: 'Structure of Atom', keywords: ['structure of atom', 'bohr', 'quantum numbers', 'heisenberg', 'de broglie', 'electronic configuration'] },
                        { id: 'CHEM_CH_03', title: 'Chemical Bonding and Molecular Structure', keywords: ['chemical bonding', 'vsepr', 'hybridization', 'dipole moment', 'molecular orbital', 'hydrogen bond'] },
                        { id: 'CHEM_CH_04', title: 'Chemical Thermodynamics', keywords: ['chemical thermodynamics', 'enthalpy', 'entropy', 'gibbs', 'first law', 'hess law', 'spontaneity'] },
                        { id: 'CHEM_CH_05', title: 'Solutions', keywords: ['solutions', 'colligative', 'raoult', 'van t hoff', 'osmotic pressure', 'depression in freezing'] },
                        { id: 'CHEM_CH_06', title: 'Equilibrium (Chemical & Ionic)', keywords: ['equilibrium', 'le chatelier', 'ph', 'buffer', 'solubility product', 'hydrolysis', 'kp', 'kc'] },
                        { id: 'CHEM_CH_07', title: 'Redox Reactions and Electrochemistry', keywords: ['redox', 'electrochemistry', 'nernst', 'galvanic', 'kohlrausch', 'electrolysis', 'faraday', 'emf'] },
                        { id: 'CHEM_CH_08', title: 'Chemical Kinetics', keywords: ['chemical kinetics', 'rate law', 'arrhenius', 'order of reaction', 'activation energy', 'half life'] }
                    ]
                },
                {
                    unitId: 'CHEM_UNIT_02',
                    unitNo: 2,
                    unitTitle: 'Inorganic Chemistry',
                    icon: '🧱',
                    chapters: [
                        { id: 'CHEM_CH_09', title: 'Classification of Elements & Periodicity', keywords: ['classification of elements', 'periodicity', 'electron gain enthalpy', 'ionization enthalpy', 'atomic radii'] },
                        { id: 'CHEM_CH_10', title: 'p-Block Elements', keywords: ['p-block', 'group 13', 'group 14', 'group 15', 'group 16', 'group 17', 'group 18', 'noble gases'] },
                        { id: 'CHEM_CH_11', title: 'd- and f-Block Elements', keywords: ['d- and f-block', 'transition elements', 'lanthanoid', 'actinoid', 'oxidation states', 'magnetic properties'] },
                        { id: 'CHEM_CH_12', title: 'Coordination Compounds', keywords: ['coordination compounds', 'cft', 'crystal field', 'splitting', 'werner', 'isomerism', 'iupac', 'spectrochemical'] }
                    ]
                },
                {
                    unitId: 'CHEM_UNIT_03',
                    unitNo: 3,
                    unitTitle: 'Organic Chemistry',
                    icon: '🧪',
                    chapters: [
                        { id: 'CHEM_CH_13', title: 'Purification & Basic Principles (GOC)', keywords: ['basic principles of organic', 'goc', 'inductive', 'resonance', 'hyperconjugation', 'iupac', 'electrophile'] },
                        { id: 'CHEM_CH_14', title: 'Hydrocarbons', keywords: ['hydrocarbons', 'alkane', 'alkene', 'alkyne', 'aromatic', 'benzene', 'markovnikov', 'ozonolysis'] },
                        { id: 'CHEM_CH_15', title: 'Haloalkanes and Haloarenes', keywords: ['halogens', 'haloalkanes', 'haloarenes', 'sn1', 'sn2', 'grignard'] },
                        { id: 'CHEM_CH_16', title: 'Alcohols, Phenols and Ethers', keywords: ['alcohols', 'phenols', 'ethers', 'reimer-tiemann', 'kolbe', 'lucas', 'williamson'] },
                        { id: 'CHEM_CH_17', title: 'Aldehydes, Ketones and Carboxylic Acids', keywords: ['aldehydes', 'ketones', 'carboxylic', 'cannizzaro', 'aldol', 'clemmensen', 'tollens', 'fehling'] },
                        { id: 'CHEM_CH_18', title: 'Organic Compounds Containing Nitrogen (Amines)', keywords: ['nitrogen', 'amines', 'diazonium', 'hoffmann', 'carbylamine', 'gabriel'] },
                        { id: 'CHEM_CH_19', title: 'Biomolecules & Polymers', keywords: ['biomolecules', 'sucrose', 'glucose', 'uracil', 'proteins', 'amino acids', 'bakelite', 'polymers'] },
                        { id: 'CHEM_CH_20', title: 'Principles of Practical Chemistry & Environmental', keywords: ['practical chemistry', 'environmental chemistry', 'salt analysis', 'titration', 'functional groups'] }
                    ]
                }
            ]
        }
    };

    /**
     * Map a single question to its syllabus Unit and Chapter
     */
    function mapQuestionToSyllabus(question, exam) {
        const targetExam = exam || 'NEET';
        const examSyllabus = EXAM_SYLLABUS_REGISTRY[targetExam] || EXAM_SYLLABUS_REGISTRY['NEET'];
        const subjectList = examSyllabus[question.subject] || [];

        const qTopic = (question.topic || '').toLowerCase();
        const qEn = (question.en || '').toLowerCase();
        const combinedText = qTopic + ' ' + qEn;

        // Try to match best chapter by keyword score
        let bestMatch = null;
        let highestScore = 0;

        for (const unit of subjectList) {
            for (const ch of unit.chapters) {
                let score = 0;
                for (const kw of ch.keywords) {
                    if (qTopic.includes(kw)) score += 5;
                    else if (combinedText.includes(kw)) score += 2;
                }
                if (score > highestScore) {
                    highestScore = score;
                    bestMatch = {
                        unitId: unit.unitId,
                        unitNo: unit.unitNo,
                        unitTitle: unit.unitTitle,
                        unitName: unit.unitTitle,
                        unitIcon: unit.icon,
                        chapterId: ch.id,
                        chapterTitle: ch.title,
                        chapterName: ch.title
                    };
                }
            }
        }

        // Fallback to first unit/chapter or topic if no match
        if (!bestMatch && subjectList.length > 0) {
            const firstUnit = subjectList[0];
            const firstCh = firstUnit.chapters[0];
            bestMatch = {
                unitId: firstUnit.unitId,
                unitNo: firstUnit.unitNo,
                unitTitle: firstUnit.unitTitle,
                unitName: firstUnit.unitTitle,
                unitIcon: firstUnit.icon,
                chapterId: firstCh.id,
                chapterTitle: question.topic || firstCh.title,
                chapterName: question.topic || firstCh.title
            };
        }

        return bestMatch || {
            unitId: 'GEN_UNIT',
            unitNo: 1,
            unitTitle: question.topic || 'General Practice',
            unitName: question.topic || 'General Practice',
            unitIcon: '📚',
            chapterId: 'GEN_CH',
            chapterTitle: question.topic || 'Core Concept',
            chapterName: question.topic || 'Core Concept'
        };
    }

    /**
     * Calculate per-chapter question stats
     */
    function getChapterQuestionStats(questions, exam, subject, userResponses) {
        const stats = {};
        const responses = userResponses || [];

        questions.forEach((q, idx) => {
            if (subject && subject !== 'ALL' && q.subject !== subject) return;
            const mapping = mapQuestionToSyllabus(q, exam);
            const chId = mapping.chapterId;

            if (!stats[chId]) {
                stats[chId] = {
                    chapterId: chId,
                    chapterTitle: mapping.chapterTitle,
                    unitId: mapping.unitId,
                    unitTitle: mapping.unitTitle,
                    unitIcon: mapping.unitIcon,
                    total: 0,
                    solved: 0,
                    correct: 0,
                    easy: 0,
                    medium: 0,
                    hard: 0,
                    questionIndices: []
                };
            }

            stats[chId].total += 1;
            stats[chId].questionIndices.push(idx);

            const diff = (q.difficulty || 'medium').toLowerCase();
            if (diff === 'easy') stats[chId].easy += 1;
            else if (diff === 'hard') stats[chId].hard += 1;
            else stats[chId].medium += 1;

            if (responses[idx] !== null && responses[idx] !== undefined) {
                stats[chId].solved += 1;
                if (responses[idx] === q.correct) {
                    stats[chId].correct += 1;
                }
            }
        });

        return stats;
    }

    /**
     * Retrieve syllabus units and chapters for a specific exam and subject
     */
    function getExamSyllabus(exam, subject) {
        const targetExam = (exam && EXAM_SYLLABUS_REGISTRY[exam]) ? exam : 'NEET';
        const examRegistry = EXAM_SYLLABUS_REGISTRY[targetExam] || EXAM_SYLLABUS_REGISTRY['NEET'];
        if (!examRegistry) return [];

        const units = examRegistry[subject] || [];
        return units.map(u => ({
            id: u.unitId || u.id,
            unitId: u.unitId || u.id,
            unitNo: u.unitNo,
            unitTitle: u.unitTitle,
            icon: u.icon,
            classLevel: u.classLevel,
            name: {
                en: u.unitTitle || (u.name && u.name.en) || 'Unit',
                bn: u.unitTitleBn || (u.name && u.name.bn) || u.unitTitle || 'অধ্যায়'
            },
            chapters: (u.chapters || []).map(ch => ({
                id: ch.id,
                title: ch.title,
                name: {
                    en: ch.title || (ch.name && ch.name.en) || 'Chapter',
                    bn: ch.titleBn || (ch.name && ch.name.bn) || ch.title || 'অনুচ্ছেদ'
                },
                keywords: ch.keywords || []
            }))
        }));
    }

    // Expose to window
    const AVAI_SYLLABUS = {
        NEET_SYLLABUS: EXAM_SYLLABUS_REGISTRY['NEET'],
        EXAM_SYLLABUS_REGISTRY,
        getExamSyllabus,
        mapQuestionToSyllabus,
        getChapterQuestionStats
    };

    window.AVAI_SYLLABUS = AVAI_SYLLABUS;
    window.EXAM_SYLLABUS_REGISTRY = EXAM_SYLLABUS_REGISTRY;
    window.getExamSyllabus = getExamSyllabus;
    window.mapQuestionToSyllabus = mapQuestionToSyllabus;
    window.getChapterQuestionStats = getChapterQuestionStats;

})(typeof window !== 'undefined' ? window : this);
