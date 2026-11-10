"""Build web/static/catalog.json & web/static/catalog.js with trilingual value-focused descriptions."""

import json
from pathlib import Path

with open("data/marketplace_catalog.json", "r", encoding="utf-8") as f:
    items = json.load(f)

CATEGORY_MAP = {
    "supervivencia-es": "Supervivència i Resiliència",
    "control-de-plagas": "Supervivència i Resiliència",
    "cultiu-interior-hidroponia": "Supervivència i Resiliència",
    "jardineria-horticultura-urbana": "Supervivència i Resiliència",
    "compostatge-fertilitat-sol": "Supervivència i Resiliència",
    "permacultura-agroecologia": "Supervivència i Resiliència",
    "agricultura-general-i-sostenible": "Supervivència i Resiliència",
    "gutenberg-health-medicine": "Supervivència i Resiliència",
    "gutenberg-earth-agricultural-sciences": "Supervivència i Resiliència",
    "gutenberg-practical-manuals-how-to": "Supervivència i Resiliència",
    "gutenberg-physics": "Ciència i Coneixement Humà",
    "gutenberg-chemistry-biochemistry": "Ciència i Coneixement Humà",
    "gutenberg-mathematics": "Ciència i Coneixement Humà",
    "gutenberg-engineering-technology": "Ciència i Coneixement Humà",
    "gutenberg-economics": "Ciència i Coneixement Humà",
    "gutenberg-research-methods-information-systems": "Ciència i Coneixement Humà",
    "ciencias-de-la-tierra": "Ciència i Coneixement Humà",
    "ciencias-aplicadas": "Ciència i Coneixement Humà",
    "ciencias-naturales": "Ciència i Coneixement Humà",
    "ciencias-sociales": "Ciència i Coneixement Humà",
    "textos-info-ciencia": "Ciència i Coneixement Humà",
    "textos-info-historia": "Ciència i Coneixement Humà",
    "textos-info-ensayo": "Ciència i Coneixement Humà",
    "textos-info-tratado": "Ciència i Coneixement Humà",
    "planetalibro-ciencia": "Ciència i Coneixement Humà",
    "planetalibro-historia": "Ciència i Coneixement Humà",
    "planetalibro-ensayo": "Ciència i Coneixement Humà",
    "planetalibro-economia": "Ciència i Coneixement Humà",
    "textos-info-filosofia": "Filosofia i Pensament",
    "textos-info-politica": "Filosofia i Pensament",
    "planetalibro-filosofia": "Filosofia i Pensament",
    "planetalibro-politica": "Filosofia i Pensament",
    "planetalibro-estrategia": "Filosofia i Pensament",
}

# Trilingual names & practical value descriptions (zero style tags)
PACK_COPY = {
    "agricultura-general-i-sostenible": {
        "names": {
            "ca": "Agricultura General i Bones Pràctiques",
            "es": "Agricultura General y Buenas Prácticas",
            "en": "General & Sustainable Agriculture",
        },
        "descriptions": {
            "ca": "Guies agronòmiques essencials (FAO i IICA) per planificar cultius, gestionar el reg, protegir collites i assegurar l'autosuficiència alimentària sense dependre de cadenes de subministrament externes.",
            "es": "Guías agronómicas esenciales (FAO e IICA) para planificar cultivos, gestionar el riego, proteger cosechas y asegurar la autosuficiencia alimentaria sin depender de cadenas externas.",
            "en": "Essential agronomy manuals (FAO & IICA) to plan crops, manage irrigation, safeguard yields, and achieve food self-reliance without external supply chains.",
        },
    },
    "jardineria-horticultura-urbana": {
        "names": {
            "ca": "Jardineria i Horticultura Urbana",
            "es": "Jardinería y Horticultura Urbana",
            "en": "Urban Gardening & Horticulture",
        },
        "descriptions": {
            "ca": "Tècniques pràctiques per cultivar hortalisses en espais reduïts, patis, balcons i jardins exteriors, incloent propagació per esqueixos, calendaris de sembra i cures estacionals.",
            "es": "Técnicas prácticas para cultivar hortalizas en espacios reducidos, patios, balcones y huertos exteriores, incluyendo propagación, calendarios de siembra y cuidados estacionales.",
            "en": "Practical techniques for growing vegetables in small spaces, balconies, and outdoor plots, covering propagation, planting calendars, and seasonal care.",
        },
    },
    "compostatge-fertilitat-sol": {
        "names": {
            "ca": "Compostatge i Fertilitat del Sòl",
            "es": "Compostaje y Fertilidad del Suelo",
            "en": "Composting & Soil Fertility",
        },
        "descriptions": {
            "ca": "Aprèn a transformar residus orgànics en adob fèrtil, equilibrar la relació carboni-nitrogen i regenerar sòls degradats mitjançant microbiologia natural sense fertilitzants sintètics.",
            "es": "Aprende a transformar residuos orgánicos en abono fértil, equilibrar la relación carbono-nitrógeno y regenerar suelos sin fertilizantes sintéticos.",
            "en": "Learn how to turn organic waste into fertile compost, balance carbon-to-nitrogen ratios, and regenerate soil biology without synthetic fertilizers.",
        },
    },
    "cultiu-interior-hidroponia": {
        "names": {
            "ca": "Cultiu en Interior i Hidroponia",
            "es": "Cultivo en Interior e Hidroponía",
            "en": "Indoor Farming & Hydroponics",
        },
        "descriptions": {
            "ca": "Manuals detallats per muntar sistemes hidropònics (NFT, arrel flotant, substrat inert), formular solucions nutritives minerals i produir aliment en interiors tot l'any amb mínim consum d'aigua.",
            "es": "Manuales detallados para montar sistemas hidropónicos (NFT, raíz flotante, sustrato), formular soluciones nutritivas y producir alimentos en interior con mínimo consumo de agua.",
            "en": "Detailed guides to building hydroponic systems (NFT, deep water culture, substrate), mixing nutrient formulas, and growing year-round indoors with minimal water.",
        },
    },
    "permacultura-agroecologia": {
        "names": {
            "ca": "Permacultura i Agroecologia",
            "es": "Permacultura y Agroecología",
            "en": "Permaculture & Agroecology",
        },
        "descriptions": {
            "ca": "Disseny d'ecosistemes productius resilients inspirats en la natura (Fukuoka, Mollison): captació d'aigua de pluja, boscos comestibles i cultiu regeneratiu de baix manteniment.",
            "es": "Diseño de ecosistemas productivos resilientes inspirados en la naturaleza (Fukuoka, Mollison): captación de agua de lluvia, bosques comestibles y cultivo regenerativo.",
            "en": "Resilient ecological design inspired by nature (Fukuoka, Mollison): rainwater harvesting, food forests, and low-maintenance regenerative cultivation.",
        },
    },
    "control-de-plagas": {
        "names": {
            "ca": "Control de Plagues i Sanitat Vegetal",
            "es": "Control de Plagas y Sanidad Vegetal",
            "en": "Pest Control & Plant Health",
        },
        "descriptions": {
            "ca": "Protocols de Maneig Integrat de Plagues (MIP), preparats botànics casolans i control biològic amb depredadors naturals per protegir collites i llars de manera segura i sense químics tòxics.",
            "es": "Protocolos de Manejo Integrado de Plagas (MIP), preparados botánicos caseros y control biológico para proteger cultivos y hogares de forma segura sin químicos tóxicos.",
            "en": "Integrated Pest Management (IPM) protocols, botanical remedies, and biological controls to protect crops and homes safely without toxic chemicals.",
        },
    },
    "gutenberg-earth-agricultural-sciences": {
        "names": {
            "ca": "Ciències de la Terra i Agronomia Clàssica",
            "es": "Ciencias de la Tierra y Agronomía Clásica",
            "en": "Earth & Agricultural Sciences",
        },
        "descriptions": {
            "ca": "Obres fundacionals sobre geologia, mineralogia, formació de sòls i aprofitament de recursos naturals (Darwin, Agricola, Leith) útils per entendre el territori i l'extracció sostenible.",
            "es": "Obras fundacionales sobre geología, mineralogía, suelos y aprovechamiento de recursos naturales (Darwin, Agricola, Leith) útiles para comprender el terreno.",
            "en": "Foundational treatises on geology, mineralogy, soil formation, and natural resource management (Darwin, Agricola, Leith) for understanding terrain and sustainability.",
        },
    },
    "gutenberg-health-medicine": {
        "names": {
            "ca": "Salut, Medicina Pràctica i Cures",
            "es": "Salud, Medicina Práctica y Cuidados",
            "en": "Health, Medicine & Field Care",
        },
        "descriptions": {
            "ca": "Tractats clàssics d'anatomia, cures d'infermeria, higiene preventiva, herbolària medicinal i salut pública (Nightingale, Culpeper) essencials quan manquen serveis sanitaris.",
            "es": "Tratados clásicos de anatomía, cuidados de enfermería, higiene preventiva, herbolaria medicinal y salud pública (Nightingale, Culpeper) esenciales en emergencias.",
            "en": "Classic reference works on anatomy, nursing care, preventive hygiene, herbal pharmacology, and public health (Nightingale, Culpeper) for off-grid medical resilience.",
        },
    },
    "gutenberg-practical-manuals-how-to": {
        "names": {
            "ca": "Manuals Pràctics d'Oficis i Taller",
            "es": "Manuales Prácticos de Oficios y Taller",
            "en": "Practical Manuals & Workshop Skills",
        },
        "descriptions": {
            "ca": "Guies d'oficis tradicionals, mecànica bàsica, fusteria, treball del metall i resolució pràctica de problemes tècnics sense eines industrials complexes.",
            "es": "Guías de oficios tradicionales, mecánica básica, carpintería, metalurgia y resolución práctica de problemas técnicos sin equipamiento industrial complejo.",
            "en": "Hands-on trade manuals covering basic mechanics, carpentry, metalworking, and practical problem-solving without complex industrial machinery.",
        },
    },
    "ciencias-sociales": {
        "names": {
            "ca": "Ciències Socials i Organització Civil",
            "es": "Ciencias Sociales y Organización Civil",
            "en": "Social Sciences & Civic Organization",
        },
        "descriptions": {
            "ca": "Fonaments d'organització comunitària, dret, educació cívica i anàlisi social per sostenir estructures de cooperació i governança local en escenaris d'aïllament.",
            "es": "Fundamentos de organización comunitaria, derecho, educación cívica y análisis social para sostener estructuras de cooperación y gobernanza local.",
            "en": "Foundations of community organization, law, civic education, and social analysis to sustain local cooperation and governance during crises.",
        },
    },
    "ciencias-naturales": {
        "names": {
            "ca": "Ciències Naturals i Biologia",
            "es": "Ciencias Naturales y Biología",
            "en": "Natural Sciences & Biology",
        },
        "descriptions": {
            "ca": "Compendi de botànica, ecologia, zoologia i fisiologia que ajuda a identificar espècies útils, comprendre els cicles biològics i gestionar ecosistemes locals.",
            "es": "Compendio de botánica, ecología, zoología y fisiología útil para identificar especies, comprender ciclos biológicos y gestionar ecosistemas locales.",
            "en": "Compendium of botany, ecology, zoology, and physiology to identify useful species, understand biological cycles, and manage local ecosystems.",
        },
    },
    "ciencias-de-la-tierra": {
        "names": {
            "ca": "Ciències de la Terra, Clima i Aigua",
            "es": "Ciencias de la Tierra, Clima y Agua",
            "en": "Earth Sciences, Climate & Hydrology",
        },
        "descriptions": {
            "ca": "Manuals d'hidrologia, meteorologia, geografia física i sismologia per localitzar fonts d'aigua, interpretar fenòmens climàtics i avaluar riscos naturals sobre el terreny.",
            "es": "Manuales de hidrología, meteorología, geografía física y sismología para localizar fuentes de agua, interpretar el clima y evaluar riesgos naturales.",
            "en": "Manuals on hydrology, meteorology, physical geography, and seismology to locate water sources, read weather patterns, and assess terrain hazards.",
        },
    },
    "ciencias-aplicadas": {
        "names": {
            "ca": "Ciències Aplicades i Tecnologia",
            "es": "Ciencias Aplicadas y Tecnología",
            "en": "Applied Sciences & Technology",
        },
        "descriptions": {
            "ca": "Principis pràctics de mecànica, termodinàmica, energia i processos industrials aplicats al manteniment d'infraestructures i solucions d'enginyeria domèstica.",
            "es": "Principios prácticos de mecánica, termodinámica, energía y procesos industriales aplicados al mantenimiento de infraestructuras y soluciones de ingeniería.",
            "en": "Practical mechanics, thermodynamics, energy systems, and industrial fundamentals for maintaining infrastructure and building field engineering solutions.",
        },
    },
    "planetalibro-historia": {
        "names": {
            "ca": "Història i Lliçons de Civilització",
            "es": "Historia y Lecciones de Civilización",
            "en": "World History & Civilizational Turning Points",
        },
        "descriptions": {
            "ca": "Cròniques i anàlisis històriques sobre com diverses societats han afrontat crisis, reconstruït infraestructures i preservat el coneixement col·lectiu.",
            "es": "Crónicas y análisis históricos sobre cómo distintas sociedades han afrontado crisis, reconstruido infraestructuras y preservado el saber colectivo.",
            "en": "Historical chronicles and analyses of how societies navigated systemic crises, rebuilt infrastructure, and preserved collective knowledge.",
        },
    },
    "textos-info-ensayo": {
        "names": {
            "ca": "Assaig Científic i Humanista",
            "es": "Ensayo Científico y Humanista",
            "en": "Scientific & Humanist Essays",
        },
        "descriptions": {
            "ca": "Obres analítiques sobre ciència, pensament crític i cultura humana pensades per fomentar la comprensió profunda i el criteri autònom.",
            "es": "Obras analíticas sobre ciencia, pensamiento crítico y cultura humana orientadas a fomentar la comprensión profunda y el criterio autónomo.",
            "en": "Analytical essays spanning science, critical inquiry, and human culture designed to strengthen independent reasoning.",
        },
    },
    "planetalibro-ciencia": {
        "names": {
            "ca": "Ciències i Filosofia Natural",
            "es": "Ciencias y Filosofía Natural",
            "en": "Science & Natural Philosophy",
        },
        "descriptions": {
            "ca": "Obres divulgatives i tractats clàssics sobre el mètode científic, la psicologia, la natura i l'observació empírica de l'entorn.",
            "es": "Obras divulgativas y tratados clásicos sobre el método científico, la observación empírica de la naturaleza y los fundamentos del conocimiento.",
            "en": "Classic works on the scientific method, empirical observation of nature, psychology, and foundational laws.",
        },
    },
    "planetalibro-ensayo": {
        "names": {
            "ca": "Assaigs de Pensament Crític",
            "es": "Ensayos de Pensamiento Crítico",
            "en": "Critical Thought Essays",
        },
        "descriptions": {
            "ca": "Selecció d'assaigs fonamentals sobre societat, ètica pràctica i resolució racional de problemes complexos.",
            "es": "Selección de ensayos fundamentales sobre sociedad, ética práctica y resolución racional de problemas complejos.",
            "en": "Curated collection of foundational essays on society, practical ethics, and rational problem-solving.",
        },
    },
    "planetalibro-economia": {
        "names": {
            "ca": "Economia Política i Gestió de Recursos",
            "es": "Economía Política y Gestión de Recursos",
            "en": "Political Economy & Resource Management",
        },
        "descriptions": {
            "ca": "Principis sobre valor, producció, intercanvi just i administració eficient de recursos escassos en comunitats resilients.",
            "es": "Principios sobre valor, producción, intercambio y administración eficiente de recursos escasos en comunidades resilientes.",
            "en": "Core principles of value, production, trade, and efficient allocation of scarce resources for resilient communities.",
        },
    },
    "gutenberg-chemistry-biochemistry": {
        "names": {
            "ca": "Química i Bioquímica Aplicada",
            "es": "Química y Bioquímica Aplicada",
            "en": "Chemistry & Biochemistry",
        },
        "descriptions": {
            "ca": "Tractats clàssics de química orgànica, anàlisi de substàncies, reaccions redox, elaboració de sabons, desinfectants i processos bioquímics fonamentals (Faraday, Lavoisier).",
            "es": "Tratados clásicos de química orgánica, análisis de sustancias, reacciones redox, desinfectantes y procesos bioquímicos esenciales (Faraday, Lavoisier).",
            "en": "Classic treatises on organic chemistry, chemical analysis, redox reactions, sanitation agents, and biochemical fundamentals (Faraday, Lavoisier).",
        },
    },
    "gutenberg-economics": {
        "names": {
            "ca": "Economia, Comerç i Teoria Monetària",
            "es": "Economía, Comercio y Teoría Monetaria",
            "en": "Economics & Resource Systems",
        },
        "descriptions": {
            "ca": "Textos clàssics d'economia política i sistemes de mercat (Adam Smith, Marx, Sun Yat-sen) per entendre els cicles econòmics i les crisis financeres.",
            "es": "Textos clásicos de economía política y sistemas de mercado (Adam Smith, Marx, Sun Yat-sen) para comprender ciclos económicos y crisis.",
            "en": "Landmark treatises on political economy, trade, and monetary systems (Adam Smith, Marx, Sun Yat-sen) to understand resource cycles.",
        },
    },
    "gutenberg-mathematics": {
        "names": {
            "ca": "Matemàtiques Pures i Aplicades",
            "es": "Matemáticas Puras y Aplicadas",
            "en": "Pure & Applied Mathematics",
        },
        "descriptions": {
            "ca": "Càlcul diferencial, geometria pràctica, àlgebra i probabilitat (Newton, Poincaré, Dudeney) indispensables per a topografia, càlcul estructural i criptografia.",
            "es": "Cálculo diferencial, geometría práctica, álgebra y probabilidad (Newton, Poincaré, Dudeney) indispensables para topografía, estructuras y criptografía.",
            "en": "Calculus, practical geometry, algebra, and probability (Newton, Poincaré, Dudeney) essential for surveying, structural math, and engineering.",
        },
    },
    "gutenberg-physics": {
        "names": {
            "ca": "Física, Mecànica i Electromagnetisme",
            "es": "Física, Mecánica y Electromagnetismo",
            "en": "Physics, Mechanics & Electromagnetism",
        },
        "descriptions": {
            "ca": "Lleis del moviment, òptica, termodinàmica i electricitat (Einstein, Newton, Leonardo da Vinci, Bacon) per dissenyar màquines simples, generadors i sistemes solars.",
            "es": "Leyes del movimiento, óptica, termodinámica y electricidad (Einstein, Newton, Da Vinci, Bacon) para diseñar máquinas simples, dinamos y sistemas térmicos.",
            "en": "Laws of motion, optics, thermodynamics, and electricity (Einstein, Newton, Da Vinci, Bacon) for designing simple machines, generators, and thermal systems.",
        },
    },
    "gutenberg-research-methods-information-systems": {
        "names": {
            "ca": "Mètodes d'Investigació i Sistemes d'Informació",
            "es": "Métodos de Investigación y Sistemas de Información",
            "en": "Research Methods & Information Systems",
        },
        "descriptions": {
            "ca": "Lògica científica, estadística experimental i metodologia rigorosa (Ramón y Cajal, John Venn, Galton) per validar hipòtesis i organitzar coneixement fiable.",
            "es": "Lógica científica, estadística experimental y metodología rigurosa (Ramón y Cajal, John Venn, Galton) para validar hipótesis y estructurar conocimiento.",
            "en": "Scientific logic, experimental statistics, and rigorous methodology (Ramón y Cajal, John Venn, Galton) for validating empirical evidence.",
        },
    },
    "textos-info-ciencia": {
        "names": {
            "ca": "Ciència i Epistemologia Històrica",
            "es": "Ciencia y Epistemología Histórica",
            "en": "Science & Historical Epistemology",
        },
        "descriptions": {
            "ca": "Obres clàssiques en espanyol sobre l'observació natural, els fonaments de la física i el desenvolupament del pensament científic.",
            "es": "Obras clásicas en español sobre la observación natural, los fundamentos de la física y el desarrollo del pensamiento científico.",
            "en": "Classic Spanish-language works on natural observation, physics foundations, and the evolution of scientific thought.",
        },
    },
    "textos-info-historia": {
        "names": {
            "ca": "Història i Cròniques Primàries",
            "es": "Historia y Crónicas Primarias",
            "en": "History & Primary Chronicles",
        },
        "descriptions": {
            "ca": "Fonts primàries i cròniques històriques fonamentals per preservar la memòria documental sense censura ni alteracions.",
            "es": "Fuentes primarias y crónicas históricas fundamentales para preservar la memoria documental sin censura ni alteraciones.",
            "en": "Primary historical chronicles and archival sources preserved offline to safeguard unedited human memory.",
        },
    },
    "gutenberg-engineering-technology": {
        "names": {
            "ca": "Enginyeria Mecànica i Tecnologia Industrial",
            "es": "Ingeniería Mecánica y Tecnología Industrial",
            "en": "Engineering & Industrial Technology",
        },
        "descriptions": {
            "ca": "Tractats clàssics d'enginyeria mecànica, motors, metal·lúrgia, energia hidràulica i manufactura (Da Vinci, Zerbe, Ford) per reparar i fabricar maquinària essencial.",
            "es": "Tratados clásicos de ingeniería mecánica, motores, metalurgia, energía hidráulica y manufactura (Da Vinci, Zerbe, Ford) para reparar y fabricar maquinaria.",
            "en": "Classic engineering references on mechanics, engines, metallurgy, hydraulics, and manufacturing (Da Vinci, Zerbe, Ford) for repairing and building equipment.",
        },
    },
    "textos-info-tratado": {
        "names": {
            "ca": "Tractats Tècnics i Metodologia",
            "es": "Tratados Técnicos y Metodología",
            "en": "Technical Treatises & Methodology",
        },
        "descriptions": {
            "ca": "Compendis sistemàtics de regles pràctiques, organització lògica i mètodes aplicats a diverses disciplines del saber.",
            "es": "Compendios sistemáticos de reglas prácticas, organización lógica y métodos aplicados a diversas disciplinas del saber.",
            "en": "Systematic compendiums of practical rules, logical structure, and proven methods across technical disciplines.",
        },
    },
    "textos-info-politica": {
        "names": {
            "ca": "Teoria Política, Dret i Societat",
            "es": "Teoría Política, Derecho y Sociedad",
            "en": "Political Theory & Civic Order",
        },
        "descriptions": {
            "ca": "Textos clàssics sobre contracte social, drets civils, separació de poders i organització comunitària justa.",
            "es": "Textos clásicos sobre contrato social, derechos civiles, separación de poderes y organización comunitaria justa.",
            "en": "Classic texts on the social contract, civil liberties, separation of powers, and fair community governance.",
        },
    },
    "planetalibro-politica": {
        "names": {
            "ca": "Doctrina Política i Governança",
            "es": "Doctrina Política y Gobernanza",
            "en": "Political Doctrine & Governance",
        },
        "descriptions": {
            "ca": "Obres de referència sobre lideratge institucional, negociació, lleis fonamentals i resolució de conflictes socials.",
            "es": "Obras de referencia sobre liderazgo institucional, negociación, leyes fundamentales y resolución de conflictos sociales.",
            "en": "Reference works on institutional leadership, negotiation, foundational law, and conflict resolution.",
        },
    },
    "planetalibro-estrategia": {
        "names": {
            "ca": "Estratègia, Logística i Tàctica",
            "es": "Estrategia, Logística y Táctica",
            "en": "Strategy, Logistics & Coordination",
        },
        "descriptions": {
            "ca": "Tractats clàssics (Sun Tzu, Maquiavel) enfocats en la presa de decisions sota pressió, planificació logística i coordinació d'equips en crisi.",
            "es": "Tratados clásicos (Sun Tzu, Maquiavelo) enfocados en la toma de decisiones bajo presión, planificación logística y coordinación de equipos en crisis.",
            "en": "Classic strategic treatises (Sun Tzu, Machiavelli) focused on decision-making under pressure, logistics planning, and team coordination.",
        },
    },
    "planetalibro-filosofia": {
        "names": {
            "ca": "Filosofia Pràctica i Estoïcisme",
            "es": "Filosofía Práctica y Estoicismo",
            "en": "Practical Philosophy & Stoicism",
        },
        "descriptions": {
            "ca": "Manuals de resiliència mental, ètica i serenitat en moments d'adversitat (Marc Aureli, Sèneca, Epictet) per mantenir la claredat en emergències.",
            "es": "Manuales de resiliencia mental, ética y serenidad ante la adversidad (Marco Aurelio, Séneca, Epicteto) para mantener la claridad en emergencias.",
            "en": "Handbooks on mental resilience, ethics, and calm under adversity (Marcus Aurelius, Seneca, Epictetus) for crisis clarity.",
        },
    },
    "textos-info-filosofia": {
        "names": {
            "ca": "Filosofia Clàssica i Lògica",
            "es": "Filosofía Clásica y Lógica",
            "en": "Classical Philosophy & Logic",
        },
        "descriptions": {
            "ca": "Diàlegs i tractats d'Aristòtil, Plató, Ramon Llull i John Locke sobre ètica, lògica formal i convivència racional.",
            "es": "Diálogos y tratados de Aristóteles, Platón, Ramon Llull y John Locke sobre ética, lógica formal y convivencia racional.",
            "en": "Core dialogues and treatises by Aristotle, Plato, Ramon Llull, and John Locke on ethics, formal logic, and rational coexistence.",
        },
    },
    "cloud-computing": {
        "names": {
            "ca": "Infraestructures de Núvol i Contenidors",
            "es": "Infraestructuras Cloud y Contenedores",
            "en": "Cloud Infrastructure & Containers",
        },
        "descriptions": {
            "ca": "Manuals d'arquitectura de servidors, Docker, Kubernetes i virtualització útils per desplegar clústers locals privats en xarxes comunitàries aïllades.",
            "es": "Manuales de arquitectura de servidores, Docker, Kubernetes y virtualización útiles para desplegar clústeres locales privados en redes aisladas.",
            "en": "Server architecture, Docker, Kubernetes, and virtualization manuals valuable for running private local clusters on isolated community networks.",
        },
    },
    "computacion-cuantica": {
        "names": {
            "ca": "Computació Quàntica i Criptografia Postquàntica",
            "es": "Computación Cuántica y Criptografía Postcuántica",
            "en": "Quantum Computing & Post-Quantum Crypto",
        },
        "descriptions": {
            "ca": "Fonaments de qubits, algorismes quàntics i esquemes criptogràfics resistents per comprendre la propera generació de càlcul i seguretat.",
            "es": "Fundamentos de cúbits, algoritmos cuánticos y esquemas criptográficos resistentes para comprender la próxima generación de cómputo y seguridad.",
            "en": "Fundamentals of qubits, quantum algorithms, and post-quantum cryptography to understand next-generation computation and security.",
        },
    },
    "machine-learning": {
        "names": {
            "ca": "Aprenentatge Automàtic (Machine Learning)",
            "es": "Aprendizaje Automático (Machine Learning)",
            "en": "Machine Learning",
        },
        "descriptions": {
            "ca": "Guies tècniques d'estadística predictiva, models classificadors, arbres de decisió i entrenament eficient en maquinari local sense dependre de serveis al núvol.",
            "es": "Guías técnicas de estadística predictiva, clasificadores, árboles de decisión y entrenamiento eficiente en hardware local sin depender de la nube.",
            "en": "Technical guides to predictive modeling, classifiers, decision trees, and efficient local model training without cloud dependency.",
        },
    },
    "computacion": {
        "names": {
            "ca": "Fonaments de la Computació i Sistemes",
            "es": "Fundamentos de la Computación y Sistemas",
            "en": "Computer Science & Systems",
        },
        "descriptions": {
            "ca": "Arquitectura de computadors, sistemes operatius, compiladors i lògica digital per mantenir, programar i recuperar equips informàtics en local.",
            "es": "Arquitectura de computadores, sistemas operativos, compiladores y lógica digital para mantener, programar y recuperar equipos informáticos.",
            "en": "Computer architecture, operating systems, compilers, and digital logic for maintaining, programming, and recovering hardware locally.",
        },
    },
    "comercio-electronico": {
        "names": {
            "ca": "Comerç Digital i Sistemes d'Intercanvi",
            "es": "Comercio Digital y Sistemas de Intercambio",
            "en": "Digital Commerce & Exchange Systems",
        },
        "descriptions": {
            "ca": "Disseny de plataformes d'intercanvi, gestió d'inventaris, seguretat transaccional i protecció de dades aplicables a mercats locals.",
            "es": "Diseño de plataformas de intercambio, gestión de inventarios, seguridad transaccional y protección de datos aplicables a mercados locales.",
            "en": "Design of exchange platforms, inventory tracking, transaction security, and data protection applicable to local marketplaces.",
        },
    },
    "seguridad-informatica": {
        "names": {
            "ca": "Seguretat Informàtica i Ciberdefensa",
            "es": "Seguridad Informática y Ciberdefensa",
            "en": "Cybersecurity & System Hardening",
        },
        "descriptions": {
            "ca": "Enduriment de sistemes Linux/xarxa, auditoria de vulnerabilitats, protecció de comunicacions i resposta davant incidents per blindar nodes autònoms.",
            "es": "Bastionado de sistemas Linux y redes, auditoría de vulnerabilidades, protección de comunicaciones y respuesta a incidentes para proteger nodos locales.",
            "en": "Linux and network hardening, vulnerability auditing, communications defense, and incident response to secure autonomous nodes.",
        },
    },
    "inteligencia-artificial": {
        "names": {
            "ca": "Intel·ligència Artificial i Xarxes Neuronals",
            "es": "Inteligencia Artificial y Redes Neuronales",
            "en": "Artificial Intelligence & Neural Networks",
        },
        "descriptions": {
            "ca": "Models lingüístics, raonament automatitzat i arquitectures de xarxes neuronals orientades a executar assistents intel·ligents directament a la teva màquina.",
            "es": "Modelos de lenguaje, razonamiento automatizado y arquitecturas neuronales orientadas a ejecutar asistentes inteligentes directamente en tu equipo.",
            "en": "Language models, automated reasoning, and neural architectures tailored for running intelligent assistants locally on your own machine.",
        },
    },
    "bases-de-datos": {
        "names": {
            "ca": "Bases de Dades i Estructuració d'Informació",
            "es": "Bases de Datos y Estructuración de Datos",
            "en": "Databases & Data Storage",
        },
        "descriptions": {
            "ca": "Modelatge relacional, SQL, indexació ràpida (SQLite/FTS5) i integritat de transaccions per emmagatzemar registres mèdics, censos i arxius de coneixement.",
            "es": "Modelado relacional, SQL, indexación rápida (SQLite/FTS5) e integridad transaccional para almacenar historiales, censos y archivos de conocimiento.",
            "en": "Relational modeling, SQL, fast indexing (SQLite/FTS5), and transactional integrity for storing medical records, registries, and archives.",
        },
    },
    "blockchain": {
        "names": {
            "ca": "Registres Distribuïts i Consens P2P",
            "es": "Registros Distribuidos y Consenso P2P",
            "en": "Distributed Ledgers & P2P Consensus",
        },
        "descriptions": {
            "ca": "Estructures criptogràfiques immutables i mecanismes de consens sense autoritat central útils per a verificació d'identitat i traçabilitat en xarxes desconnectades.",
            "es": "Estructuras criptográficas inmutables y mecanismos de consenso sin autoridad central para verificación de identidad y trazabilidad descentralizada.",
            "en": "Tamper-evident cryptographic ledgers and leaderless consensus mechanisms for identity verification and decentralized trust.",
        },
    },
    "diseno-grafico": {
        "names": {
            "ca": "Disseny Gràfic i Comunicació Visual",
            "es": "Diseño Gráfico y Comunicación Visual",
            "en": "Graphic Design & Visual Communication",
        },
        "descriptions": {
            "ca": "Tipografia, maquetació de manuals impresos, senyalètica d'emergència i composició visual clara per transmetre instruccions crítiques sense ambigüitats.",
            "es": "Tipografía, maquetación de manuales impresos, señalética de emergencia y composición visual clara para comunicar instrucciones críticas.",
            "en": "Typography, print manual layout, emergency signage, and clear visual communication for conveying critical field instructions.",
        },
    },
    "diseno-web": {
        "names": {
            "ca": "Disseny Web, Usabilitat i Accessibilitat",
            "es": "Diseño Web, Usabilidad y Accesibilidad",
            "en": "Web Design, Usability & Accessibility",
        },
        "descriptions": {
            "ca": "Arquitectura d'informació, interfícies intuïtives i accessibilitat universal per construir portals locals fàcils d'usar per qualsevol persona en crisi.",
            "es": "Arquitectura de información, interfaces intuitivas y accesibilidad universal para construir portales locales fáciles de usar por cualquier persona.",
            "en": "Information architecture, intuitive UI, and universal accessibility for building local web portals usable by anyone in emergencies.",
        },
    },
    "redes-informaticas": {
        "names": {
            "ca": "Xarxes Informàtiques, Ràdio i Enrutament",
            "es": "Redes Informáticas, Radio y Enrutamiento",
            "en": "Computer Networks & Mesh Routing",
        },
        "descriptions": {
            "ca": "Protocols TCP/IP, xarxes locals autònomes, enrutament sense fil i topologies *mesh* imprescindibles per muntar intranets de barri o poble sense operadors.",
            "es": "Protocolos TCP/IP, redes locales autónomas, enrutamiento inalámbrico y topologías *mesh* imprescindibles para montar intranets vecinales sin operadores.",
            "en": "TCP/IP protocols, autonomous LANs, wireless routing, and mesh topologies essential for standing up neighborhood intranets without ISPs.",
        },
    },
    "analisis-de-datos": {
        "names": {
            "ca": "Anàlisi de Dades i Estadística Aplicada",
            "es": "Análisis de Datos y Estadística Aplicada",
            "en": "Data Analysis & Applied Statistics",
        },
        "descriptions": {
            "ca": "Eines quantitatives per analitzar consums d'aigua, estocs alimentaris, dades epidemiològiques i tendències ambientals sobre fulls locals.",
            "es": "Herramientas cuantitativas para analizar consumos de agua, reservas de alimentos, datos epidemiológicos y variables ambientales localmente.",
            "en": "Quantitative methods for analyzing water usage, food reserves, epidemiological tracking, and environmental readings locally.",
        },
    },
    "criptografia": {
        "names": {
            "ca": "Criptografia Aplicada i Privacitat",
            "es": "Criptografía Aplicada y Privacidad",
            "en": "Applied Cryptography & Privacy",
        },
        "descriptions": {
            "ca": "Algorismes de xifratge simètric, signatures digitals Ed25519 i funcions hash per autenticar missatges i verificar paquets descarregats sense connexió.",
            "es": "Algoritmos de cifrado simétrico, firmas digitales Ed25519 y funciones hash para autenticar mensajes y verificar paquetes sin conexión.",
            "en": "Symmetric encryption, Ed25519 digital signatures, and cryptographic hashing to authenticate messages and verify offline packages.",
        },
    },
    "algoritmo": {
        "names": {
            "ca": "Algorísmica i Optimització Computacional",
            "es": "Algoritmia y Optimización Computacional",
            "en": "Algorithms & Computational Optimization",
        },
        "descriptions": {
            "ca": "Estructures de dades, cerca eficient, grafs d'enrutament i resolució òptima de rutes o assignació de recursos en dispositius de baixa potència.",
            "es": "Estructuras de datos, búsqueda eficiente, grafos de enrutamiento y optimización de rutas o recursos en hardware de bajo consumo.",
            "en": "Data structures, fast search algorithms, graph routing, and resource optimization techniques suited for low-power edge hardware.",
        },
    },
    "automatizacion": {
        "names": {
            "ca": "Automatització, Sensors i Control",
            "es": "Automatización, Sensores y Control",
            "en": "Automation, Sensors & Control",
        },
        "descriptions": {
            "ca": "Disseny de sistemes automàtics per a reg per degoteig, control tèrmic d'hivernacles, relés solars i monitoratge autònom amb microcontroladors.",
            "es": "Diseño de sistemas automáticos para riego por goteo, control térmico en invernaderos, relés solares y monitorización con microcontroladores.",
            "en": "Design of automated drip irrigation, greenhouse climate control, solar relays, and autonomous sensing with microcontrollers.",
        },
    },
    "big-data": {
        "names": {
            "ca": "Processament Massiu de Dades",
            "es": "Procesamiento Masivo de Datos",
            "en": "Large-Scale Data Engineering",
        },
        "descriptions": {
            "ca": "Tècniques de particionament, compressió i indexació distribuïda per gestionar grans arxius documentals i científics en emmagatzematge limitat.",
            "es": "Técnicas de particionado, compresión e indexación distribuida para gestionar grandes archivos documentales en almacenamiento limitado.",
            "en": "Partitioning, compression, and distributed indexing techniques for managing large scientific document archives on constrained storage.",
        },
    },
    "desarrollo-web": {
        "names": {
            "ca": "Desenvolupament d'Aplicacions Web Locals",
            "es": "Desarrollo de Aplicaciones Web Locales",
            "en": "Local Web Application Development",
        },
        "descriptions": {
            "ca": "Creació de portals, aplicacions progressives offline-first (PWA) i serveis lleugers perquè tota la comunitat accedeixi al node des de qualsevol navegador.",
            "es": "Creación de portales, aplicaciones offline-first (PWA) y servicios ligeros para que cualquier vecino acceda al nodo desde su navegador.",
            "en": "Building portals, offline-first progressive web apps (PWAs), and lightweight local services accessible from any device browser.",
        },
    },
}

enriched = []
for it in items:
    cid = it["id"]
    cat = CATEGORY_MAP.get(cid, "Tecnologia i Informàtica")
    is_survival = (
        cat == "Supervivència i Resiliència"
        or "supervivencia" in cid
        or "plaga" in cid
        or "cultiu" in cid
        or "agri" in cid
        or "health" in cid
    )

    copy_entry = PACK_COPY.get(cid, {})
    names = copy_entry.get("names", {"ca": it["name"], "es": it["name"], "en": it["name"]})
    descriptions = copy_entry.get("descriptions", {
        "ca": it.get("description", ""),
        "es": it.get("description", ""),
        "en": it.get("description", ""),
    })

    enriched.append({
        **it,
        "name": names["ca"],
        "description": descriptions["ca"],
        "names": names,
        "descriptions": descriptions,
        "portal_category": cat,
        "is_survival": is_survival,
        "install_command": f"smart-local import-pack {it['file']}",
        "rag_id": cid,
        "cover_image": f"static/covers/{cid}.jpg",
        "release_url": f"https://github.com/resettingworld/catalogo/releases/download/v1.0.0/{it['file']}",
        "catalogo_path": f"https://github.com/resettingworld/catalogo/tree/main/catalogs/{cid}",
    })

enriched.sort(key=lambda x: (not x["is_survival"], x["portal_category"], -x["books_count"]))

with open("web/static/catalog.json", "w", encoding="utf-8") as f:
    json.dump(enriched, f, indent=2, ensure_ascii=False)

with open("web/static/catalog.js", "w", encoding="utf-8") as f:
    f.write("window.RW_CATALOG = " + json.dumps(enriched, ensure_ascii=False) + ";\n")

print(f"Generated trilingual value catalog with {len(enriched)} packs.")
