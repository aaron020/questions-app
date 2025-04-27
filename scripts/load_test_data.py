import requests
from dotenv import dotenv_values

# Script to load the database with test data via API

api_url = 'https://1ujszukdof.execute-api.eu-west-1.amazonaws.com/Prod'
auth_url = 'https://cognito-idp.eu-west-1.amazonaws.com/'



print('--Preforming Authorization---')
test_account_pwd = ''
headers = {}
try:
    vars = dotenv_values('../.env')
    test_account_pwd = vars['TEST_ACCOUNT_PWD']
except Exception as e:
    print(e)
try:
    headers = {
        'Content-Type': 'application/x-amz-json-1.1',
        'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth',
        'Host': 'cognito-idp.eu-west-1.amazonaws.com'
    }
    body = {
        'AuthFlow': 'USER_PASSWORD_AUTH',
        'AuthParameters': {
            'USERNAME': 'testing_user',
            'PASSWORD': test_account_pwd
        },
        'ClientId': 'a63d0blt9et7g21sm6o0rk2sl'
    }
    response = requests.post(url=auth_url, json=body, headers=headers)
    data = response.json()
    id_token = data.get('AuthenticationResult').get('IdToken')

    headers = {
            'x-amz-docs-region': 'eu-west-1',
            'Authorization': f'Bearer {id_token}'
        }
except requests.exceptions.RequestException as e:
    print('Error:', e)


print('--Posting to Database--')

def post_topic(topic_body: dict):
    try:
        response = requests.post(
            url=f'{api_url}/topics',
            json=topic_body,
            headers=headers
        )
        assert response.status_code == 200
        bytes_string = response.content
        string_value = bytes_string.decode('utf-8')
        clean_string = string_value.strip('"')
        return clean_string
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        assert False

def post_question(question_body: dict):
    try:
        response = requests.post(
            url=f'{api_url}/topics/questions',
            json=question_body,
            headers=headers
        )
        assert response.status_code == 200
    except requests.exceptions.RequestException as e:
        print('Error:', e)

# Data
topics = [
        {
            "topic_name": "Quantum Computing",
            "description": "Exploring how quantum computers work and their potential to revolutionize computing",
            "category": "technology"
        },
        {
            "topic_name": "Renaissance Art",
            "description": "Major artists and movements of the European Renaissance period",
            "category": "art"
        },
        {
            "topic_name": "Black Holes",
            "description": "Formation, characteristics and mysteries of these cosmic phenomena",
            "category": "astronomy"
        },
        {
            "topic_name": "CRISPR",
            "description": "Gene editing technology and its implications for medicine and ethics",
            "category": "biology"
        },
        {
            "topic_name": "Startup Funding",
            "description": "How early-stage companies secure investment and grow their operations",
            "category": "business"
        },
        {
            "topic_name": "Periodic Table",
            "description": "Elements organization and properties in chemistry's fundamental framework",
            "category": "chemistry"
        },
        {
            "topic_name": "Film Noir",
            "description": "Characteristics and significance of this dark, stylized film genre",
            "category": "cinema"
        },
        {
            "topic_name": "Stand-up History",
            "description": "Evolution of stand-up comedy from vaudeville to modern streaming specials",
            "category": "comedy"
        },
        {
            "topic_name": "Inflation",
            "description": "Causes and effects of rising prices in national economies",
            "category": "economics"
        },
        {
            "topic_name": "Bridge Design",
            "description": "Principles and innovations in connecting landscapes across obstacles",
            "category": "engineering"
        },
        {
            "topic_name": "Crypto Markets",
            "description": "How cryptocurrency markets function and their investment potential",
            "category": "finance"
        },
        {
            "topic_name": "Coral Reefs",
            "description": "Formation, biodiversity, and conservation of these marine ecosystems",
            "category": "geography"
        },
        {
            "topic_name": "Ancient Rome",
            "description": "Rise and fall of the Roman Empire and its lasting legacy",
            "category": "history"
        },
        {
            "topic_name": "IP",
            "description": "Legal protections for creative works and innovations",
            "category": "law"
        },
        {
            "topic_name": "Dystopian Fiction",
            "description": "Examination of novels depicting oppressive future societies",
            "category": "literature"
        },
        {
            "topic_name": "Jazz Evolution",
            "description": "Origins and development of this influential American musical form",
            "category": "music"
        },
        {
            "topic_name": "Mindfulness",
            "description": "Practices for present-moment awareness and mental well-being",
            "category": "personal"
        },
        {
            "topic_name": "Electoral Systems",
            "description": "How different voting methods shape political representation",
            "category": "politics"
        },
        {
            "topic_name": "Climate Change",
            "description": "Causes, impacts, and solutions to global warming",
            "category": "science"
        },
        {
            "topic_name": "Content Creators",
            "description": "Rise of independent media producers on digital platforms",
            "category": "socialmedia"
        },
        {
            "topic_name": "Olympic History",
            "description": "Evolution of the international sporting competition from ancient to modern times",
            "category": "sport"
        },
        {
            "topic_name": "AI Ethics",
            "description": "Moral implications of artificial intelligence development and deployment",
            "category": "technology"
        },
        {
            "topic_name": "Gothic Architecture",
            "description": "Medieval building style featuring pointed arches and flying buttresses",
            "category": "architecture"
        },
        {
            "topic_name": "Urban Legends",
            "description": "Modern folklore and myths that spread through contemporary culture",
            "category": "other"
        }
]

questions = {
    'Quantum Computing': [
  {
    "questions": "What is superposition in quantum computing?",
    "answers": [
      {
        "answer": "When a quantum bit is spinning in multiple directions",
        "correct": False
      },
      {
        "answer": "When a quantum bit exists in multiple states simultaneously",
        "correct": True
      },
      {
        "answer": "When two quantum computers work together",
        "correct": False
      }
    ],
    "explanation": "Superposition allows qubits to exist in multiple states at once, unlike classical bits which are 0 OR 1.",
    "difficulty": 1
  },
  {
    "questions": "Which of the following is NOT a quantum computing gate?",
    "answers": [
      {
        "answer": "Hadamard gate",
        "correct": False
      },
      {
        "answer": "NAND gate",
        "correct": True
      },
      {
        "answer": "Pauli-X gate",
        "correct": False
      },
      {
        "answer": "CNOT gate",
        "correct": False
      }
    ],
    "explanation": "NAND is a classical computing gate, while Hadamard, Pauli-X and CNOT are quantum gates.",
    "difficulty": 2
  },
  {
    "questions": "What is quantum entanglement?",
    "answers": [
      {
        "answer": "When qubits become overheated during computation",
        "correct": False
      },
      {
        "answer": "When quantum computers connect to the internet",
        "correct": False
      },
      {
        "answer": "When the states of two qubits become correlated and dependent on each other",
        "correct": True
      }
    ],
    "explanation": "Entanglement creates special correlations where measuring one qubit instantly affects its entangled partner.",
    "difficulty": 1
  },
  {
    "questions": "What famous algorithm developed by Peter Shor threatens modern encryption?",
    "answers": [
      {
        "answer": "Grover's algorithm",
        "correct": False
      },
      {
        "answer": "Shor's algorithm",
        "correct": True
      },
      {
        "answer": "Deutsch-Jozsa algorithm",
        "correct": False
      },
      {
        "answer": "Simon's algorithm",
        "correct": False
      }
    ],
    "explanation": "Shor's algorithm can efficiently factor large numbers, which threatens RSA encryption used widely today.",
    "difficulty": 2
  },
  {
    "questions": "What cooling technology is typically used for superconducting quantum computers?",
    "answers": [
      {
        "answer": "Liquid helium dilution refrigeration",
        "correct": True
      },
      {
        "answer": "Standard air conditioning",
        "correct": False
      },
      {
        "answer": "Water cooling",
        "correct": False
      }
    ],
    "explanation": "Superconducting quantum computers need extremely cold temperatures near absolute zero, achieved with helium.",
    "difficulty": 2
  },
  {
    "questions": "What is 'quantum decoherence'?",
    "answers": [
      {
        "answer": "The process of quantum computers becoming obsolete",
        "correct": False
      },
      {
        "answer": "Loss of quantum information due to interaction with the environment",
        "correct": True
      },
      {
        "answer": "The process of shutting down a quantum computer",
        "correct": False
      }
    ],
    "explanation": "Decoherence is a major challenge in quantum computing where qubits lose their quantum state due to noise.",
    "difficulty": 2
  },
  {
    "questions": "What is quantum supremacy?",
    "answers": [
      {
        "answer": "When quantum computers completely replace classical computers",
        "correct": False
      },
      {
        "answer": "When a quantum computer solves a problem classical computers can't solve in reasonable time",
        "correct": True
      },
      {
        "answer": "When quantum computers reach 1 million qubits",
        "correct": False
      }
    ],
    "explanation": "Quantum supremacy is achieved when quantum computers perform a task beyond practical classical capabilities.",
    "difficulty": 1
  },
  {
    "questions": "Which company claimed to achieve quantum supremacy in 2019?",
    "answers": [
      {
        "answer": "IBM",
        "correct": False
      },
      {
        "answer": "Microsoft",
        "correct": False
      },
      {
        "answer": "Google",
        "correct": True
      },
      {
        "answer": "D-Wave",
        "correct": False
      }
    ],
    "explanation": "Google claimed quantum supremacy with their 53-qubit Sycamore processor performing a specific calculation.",
    "difficulty": 2
  },
  {
    "questions": "What is the significance of Grover's algorithm?",
    "answers": [
      {
        "answer": "It can search unsorted databases quadratically faster than classical algorithms",
        "correct": True
      },
      {
        "answer": "It can break any encryption instantly",
        "correct": False
      },
      {
        "answer": "It enables quantum teleportation",
        "correct": False
      }
    ],
    "explanation": "Grover's algorithm provides a quadratic speedup for searching unstructured databases, not exponential.",
    "difficulty": 3
  },
  {
    "questions": "What is the primary unit of information in quantum computing?",
    "answers": [
      {
        "answer": "Bit",
        "correct": False
      },
      {
        "answer": "Qubit",
        "correct": True
      },
      {
        "answer": "Byte",
        "correct": False
      },
      {
        "answer": "Qubyte",
        "correct": False
      }
    ],
    "explanation": "The qubit (quantum bit) is the fundamental unit of quantum information, analogous to classical bits.",
    "difficulty": 1
  },
  {
    "questions": "Which quantum computing approach uses trapped ions as qubits?",
    "answers": [
      {
        "answer": "Superconducting circuits",
        "correct": False
      },
      {
        "answer": "Trapped ion quantum computing",
        "correct": True
      },
      {
        "answer": "Quantum annealing",
        "correct": False
      },
      {
        "answer": "Silicon quantum dots",
        "correct": False
      }
    ],
    "explanation": "Trapped ion quantum computing uses charged atoms suspended in electromagnetic fields as qubits.",
    "difficulty": 2
  },
  {
    "questions": "What quantum error correction code uses nine qubits to encode one logical qubit?",
    "answers": [
      {
        "answer": "Shor code",
        "correct": True
      },
      {
        "answer": "Steane code",
        "correct": False
      },
      {
        "answer": "Surface code",
        "correct": False
      }
    ],
    "explanation": "The Shor code was one of the first quantum error correction codes, using 9 physical qubits for 1 logical qubit.",
    "difficulty": 3
  },
  {
    "questions": "What is the quantum no-cloning theorem?",
    "answers": [
      {
        "answer": "Quantum algorithms cannot have duplicate copies",
        "correct": False
      },
      {
        "answer": "It's impossible to create an identical copy of an unknown quantum state",
        "correct": True
      },
      {
        "answer": "Quantum computers cannot be mass-produced",
        "correct": False
      }
    ],
    "explanation": "The no-cloning theorem is fundamental to quantum mechanics and underlies quantum cryptography security.",
    "difficulty": 3
  },
  {
    "questions": "Which quantum algorithm efficiently solves linear systems of equations?",
    "answers": [
      {
        "answer": "Shor's algorithm",
        "correct": False
      },
      {
        "answer": "Grover's algorithm",
        "correct": False
      },
      {
        "answer": "HHL algorithm",
        "correct": True
      },
      {
        "answer": "Deutsch-Jozsa algorithm",
        "correct": False
      }
    ],
    "explanation": "The HHL (Harrow-Hassidim-Lloyd) algorithm can solve linear systems exponentially faster than classical methods.",
    "difficulty": 3
  },
  {
    "questions": "What does NISQ stand for in quantum computing?",
    "answers": [
      {
        "answer": "National Institute for Supercomputing Quantum-mechanics",
        "correct": False
      },
      {
        "answer": "Noisy Intermediate-Scale Quantum",
        "correct": True
      },
      {
        "answer": "New Integrated System for Quantum-computing",
        "correct": False
      }
    ],
    "explanation": "NISQ refers to current quantum computers with limited qubits and significant noise/error rates.",
    "difficulty": 2
  }
],
    'Renaissance Art': [
  {
    "questions": "Who painted the 'Mona Lisa'?",
    "answers": [
      {
        "answer": "Michelangelo",
        "correct": False
      },
      {
        "answer": "Leonardo da Vinci",
        "correct": True
      },
      {
        "answer": "Raphael",
        "correct": False
      },
      {
        "answer": "Botticelli",
        "correct": False
      }
    ],
    "explanation": "Leonardo da Vinci painted the Mona Lisa (La Gioconda) around 1503-1506, perhaps continuing until 1517.",
    "difficulty": 1
  },
  {
    "questions": "Which of these techniques, perfected during the Renaissance, creates the illusion of depth?",
    "answers": [
      {
        "answer": "Chiaroscuro",
        "correct": False
      },
      {
        "answer": "Linear perspective",
        "correct": True
      },
      {
        "answer": "Impasto",
        "correct": False
      }
    ],
    "explanation": "Linear perspective uses converging lines to create the illusion of depth and distance on a flat surface.",
    "difficulty": 2
  },
  {
    "questions": "Botticelli's 'The Birth of Venus' depicts Venus emerging from what?",
    "answers": [
      {
        "answer": "A seashell",
        "correct": True
      },
      {
        "answer": "The ocean",
        "correct": False
      },
      {
        "answer": "A cloud",
        "correct": False
      },
      {
        "answer": "A flower",
        "correct": False
      }
    ],
    "explanation": "In this famous painting, Venus stands on a giant scallop shell as she's blown to shore by Zephyr.",
    "difficulty": 1
  },
  {
    "questions": "Which Renaissance artist painted the ceiling of the Sistine Chapel?",
    "answers": [
      {
        "answer": "Leonardo da Vinci",
        "correct": False
      },
      {
        "answer": "Raphael",
        "correct": False
      },
      {
        "answer": "Michelangelo",
        "correct": True
      },
      {
        "answer": "Donatello",
        "correct": False
      }
    ],
    "explanation": "Michelangelo painted the Sistine Chapel ceiling between 1508-1512, including the famous Creation of Adam.",
    "difficulty": 1
  },
  {
    "questions": "Which artistic family dominated Florentine patronage during the early Renaissance?",
    "answers": [
      {
        "answer": "The Borgias",
        "correct": False
      },
      {
        "answer": "The Medicis",
        "correct": True
      },
      {
        "answer": "The Sforzas",
        "correct": False
      }
    ],
    "explanation": "The wealthy Medici family were major patrons of Renaissance art in Florence, supporting many famous artists.",
    "difficulty": 2
  }
],
    "Black Holes": [
    {
      "questions": "What is the 'event horizon' of a black hole?",
      "answers": [
        {
          "answer": "The center point of a black hole",
          "correct": False
        },
        {
          "answer": "The boundary beyond which nothing can escape the black hole's gravity",
          "correct": True
        },
        {
          "answer": "The area where light bends around a black hole",
          "correct": False
        }
      ],
      "explanation": "The event horizon is the point of no return, beyond which the gravitational pull is too strong for anything to escape.",
      "difficulty": 1
    },
    {
      "questions": "What is 'Hawking radiation'?",
      "answers": [
        {
          "answer": "Radiation emitted from the center of a black hole",
          "correct": False
        },
        {
          "answer": "Radiation theorized to be released by black holes due to quantum effects near the event horizon",
          "correct": True
        },
        {
          "answer": "The light that gets trapped within a black hole",
          "correct": False
        }
      ],
      "explanation": "Hawking radiation, proposed by Stephen Hawking, suggests black holes slowly emit radiation and eventually evaporate.",
      "difficulty": 2
    },
    {
      "questions": "What happens to time near a black hole?",
      "answers": [
        {
          "answer": "Time stops completely",
          "correct": False
        },
        {
          "answer": "Time flows normally",
          "correct": False
        },
        {
          "answer": "Time dilates (slows down) relative to observers farther away",
          "correct": True
        }
      ],
      "explanation": "Due to gravitational time dilation, time moves slower near massive objects like black holes compared to distant observers.",
      "difficulty": 2
    },
    {
      "questions": "What is the singularity of a black hole?",
      "answers": [
        {
          "answer": "The event horizon of a black hole",
          "correct": False
        },
        {
          "answer": "A point of infinite density at the center of a black hole",
          "correct": True
        },
        {
          "answer": "The area around a black hole where light can still escape",
          "correct": False
        }
      ],
      "explanation": "The singularity is a one-dimensional point where all the black hole's mass is concentrated, causing infinite density.",
      "difficulty": 1
    },
    {
      "questions": "What evidence confirmed the existence of a supermassive black hole at the center of our galaxy?",
      "answers": [
        {
          "answer": "Direct photographs of the black hole itself",
          "correct": False
        },
        {
          "answer": "Observations of stars orbiting around an invisible massive object",
          "correct": True
        },
        {
          "answer": "Radio signals emitted from the galactic center",
          "correct": False
        }
      ],
      "explanation": "Astronomers observed stars orbiting around Sagittarius A*, our galaxy's central supermassive black hole.",
      "difficulty": 3
    }
  ],
    "CRISPR": [
    {
      "questions": "What does CRISPR stand for?",
      "answers": [
        {
          "answer": "Cellular Replication In Specified Protein Regions",
          "correct": False
        },
        {
          "answer": "Clustered Regularly Interspaced Short Palindromic Repeats",
          "correct": True
        },
        {
          "answer": "Cytological RNA Insertion System for Precise Replication",
          "correct": False
        }
      ],
      "explanation": "CRISPR refers to repeating DNA sequences found in bacteria that form the basis of the gene-editing technology.",
      "difficulty": 2
    },
    {
      "questions": "What protein is commonly used with CRISPR for gene editing?",
      "answers": [
        {
          "answer": "Cas9",
          "correct": True
        },
        {
          "answer": "Poly1",
          "correct": False
        },
        {
          "answer": "Cre2",
          "correct": False
        },
        {
          "answer": "Ras7",
          "correct": False
        }
      ],
      "explanation": "Cas9 is an enzyme that acts like molecular scissors, cutting DNA at specific locations guided by RNA.",
      "difficulty": 1
    },
    {
      "questions": "What is the natural function of CRISPR in bacteria?",
      "answers": [
        {
          "answer": "To help bacteria reproduce faster",
          "correct": False
        },
        {
          "answer": "To allow bacteria to survive in extreme environments",
          "correct": False
        },
        {
          "answer": "To defend against viral infections by cutting up viral DNA",
          "correct": True
        }
      ],
      "explanation": "CRISPR naturally functions as an adaptive immune system in bacteria to protect against viruses.",
      "difficulty": 2
    },
    {
      "questions": "Which scientists are credited with developing CRISPR-Cas9 gene editing technology?",
      "answers": [
        {
          "answer": "Jennifer Doudna and Emmanuelle Charpentier",
          "correct": True
        },
        {
          "answer": "Francis Crick and James Watson",
          "correct": False
        },
        {
          "answer": "Craig Venter and James Collins",
          "correct": False
        }
      ],
      "explanation": "Doudna and Charpentier were awarded the 2020 Nobel Prize in Chemistry for developing CRISPR-Cas9 gene editing.",
      "difficulty": 2
    },
    {
      "questions": "What component guides the CRISPR-Cas9 system to the target DNA sequence?",
      "answers": [
        {
          "answer": "A protein marker",
          "correct": False
        },
        {
          "answer": "Guide RNA (gRNA)",
          "correct": True
        },
        {
          "answer": "A chemical attractant",
          "correct": False
        },
        {
          "answer": "Magnetic forces",
          "correct": False
        }
      ],
      "explanation": "Guide RNA (gRNA) contains sequences complementary to the target DNA, directing Cas9 where to make its cut.",
      "difficulty": 2
    }
    ],
    "Startup Funding": [
    {
      "questions": "What does 'Series A' funding typically represent?",
      "answers": [
        {
          "answer": "Initial funding from friends and family",
          "correct": False
        },
        {
          "answer": "The first significant round of venture capital funding after seed funding",
          "correct": True
        },
        {
          "answer": "Funding that comes just before an IPO",
          "correct": False
        }
      ],
      "explanation": "Series A is typically the first major VC round after seed, meant to optimize product and user base.",
      "difficulty": 1
    },
    {
      "questions": "What are angel investors?",
      "answers": [
        {
          "answer": "Institutional investors who only invest in established companies",
          "correct": False
        },
        {
          "answer": "Government agencies that provide grants to startups",
          "correct": False
        },
        {
          "answer": "Wealthy individuals who invest their own money in early-stage startups",
          "correct": True
        }
      ],
      "explanation": "Angel investors are affluent individuals who provide capital for startups, usually in exchange for equity or convertible debt.",
      "difficulty": 1
    },
    {
      "questions": "What is a 'term sheet' in startup funding?",
      "answers": [
        {
          "answer": "A legally binding contract that guarantees funding",
          "correct": False
        },
        {
          "answer": "A non-binding document outlining the terms and conditions of an investment",
          "correct": True
        },
        {
          "answer": "A list of competitors the startup promises not to work with",
          "correct": False
        },
        {
          "answer": "The startup's business plan",
          "correct": False
        }
      ],
      "explanation": "A term sheet outlines key investment terms but isn't legally binding; it serves as the basis for formal agreements.",
      "difficulty": 2
    },
    {
      "questions": "What is a 'unicorn' in startup terminology?",
      "answers": [
        {
          "answer": "A startup with a female founder",
          "correct": False
        },
        {
          "answer": "A startup valued at $1 billion or more",
          "correct": True
        },
        {
          "answer": "A startup that has been profitable from day one",
          "correct": False
        }
      ],
      "explanation": "The term unicorn refers to privately held startup companies valued at over $1 billion.",
      "difficulty": 1
    },
    {
      "questions": "What does 'bootstrapping' mean for a startup?",
      "answers": [
        {
          "answer": "Securing multiple rounds of venture capital",
          "correct": False
        },
        {
          "answer": "Building a startup with personal finances and operating revenues without external funding",
          "correct": True
        },
        {
          "answer": "Using another company's resources to build your product",
          "correct": False
        }
      ],
      "explanation": "Bootstrapping means funding growth through personal resources and revenue rather than seeking external investors.",
      "difficulty": 1
    }
    ],
    "Periodic Table": [
    {
      "questions": "Who is credited with creating the modern periodic table?",
      "answers": [
        {
          "answer": "Albert Einstein",
          "correct": False
        },
        {
          "answer": "Dmitri Mendeleev",
          "correct": True
        },
        {
          "answer": "Marie Curie",
          "correct": False
        },
        {
          "answer": "Niels Bohr",
          "correct": False
        }
      ],
      "explanation": "Mendeleev published the first recognized periodic table in 1869, arranging elements by atomic weight and properties.",
      "difficulty": 1
    },
    {
      "questions": "What do elements in the same group (column) of the periodic table have in common?",
      "answers": [
        {
          "answer": "Same number of protons",
          "correct": False
        },
        {
          "answer": "Same number of neutrons",
          "correct": False
        },
        {
          "answer": "Similar chemical properties and same number of valence electrons",
          "correct": True
        }
      ],
      "explanation": "Elements in the same group have the same number of electrons in their outer shell, giving them similar properties.",
      "difficulty": 2
    },
    {
      "questions": "What are elements in the far right column of the periodic table called?",
      "answers": [
        {
          "answer": "Alkali metals",
          "correct": False
        },
        {
          "answer": "Transition metals",
          "correct": False
        },
        {
          "answer": "Noble gases",
          "correct": True
        },
        {
          "answer": "Halogens",
          "correct": False
        }
      ],
      "explanation": "Noble gases have complete electron shells, making them highly stable and generally non-reactive.",
      "difficulty": 1
    },
    {
      "questions": "What determines an element's position in the periodic table?",
      "answers": [
        {
          "answer": "Its color and state at room temperature",
          "correct": False
        },
        {
          "answer": "Its atomic number (number of protons)",
          "correct": True
        },
        {
          "answer": "Its discovery date",
          "correct": False
        },
        {
          "answer": "Its atomic mass",
          "correct": False
        }
      ],
      "explanation": "Elements are arranged by increasing atomic number, which is the number of protons in an atom's nucleus.",
      "difficulty": 1
    },
    {
      "questions": "Elements in the 'f-block' of the periodic table are also known as?",
      "answers": [
        {
          "answer": "Transition metals",
          "correct": False
        },
        {
          "answer": "Lanthanides and actinides",
          "correct": True
        },
        {
          "answer": "Noble gases",
          "correct": False
        },
        {
          "answer": "Alkaline earth metals",
          "correct": False
        }
      ],
      "explanation": "The f-block includes lanthanides (elements 58-71) and actinides (elements 90-103), usually shown separately below.",
      "difficulty": 2
    }
    ],
    "Film Noir": [
    {
      "questions": "Which time period is most associated with classic film noir?",
      "answers": [
        {
          "answer": "1920s-1930s",
          "correct": False
        },
        {
          "answer": "1940s-1950s",
          "correct": True
        },
        {
          "answer": "1960s-1970s",
          "correct": False
        }
      ],
      "explanation": "Classic film noir flourished in American cinema primarily during the 1940s and 1950s after World War II.",
      "difficulty": 1
    },
    {
      "questions": "Which visual technique is strongly associated with film noir?",
      "answers": [
        {
          "answer": "Bright, high-key lighting",
          "correct": False
        },
        {
          "answer": "Low-key lighting with stark contrast and shadows",
          "correct": True
        },
        {
          "answer": "Soft focus and diffused lighting",
          "correct": False
        },
        {
          "answer": "Technicolor saturation",
          "correct": False
        }
      ],
      "explanation": "Film noir is known for dramatic shadows, stark contrast, and low-key lighting creating a moody, mysterious atmosphere.",
      "difficulty": 1
    },
    {
      "questions": "Which character archetype is NOT typically found in film noir?",
      "answers": [
        {
          "answer": "The femme fatale",
          "correct": False
        },
        {
          "answer": "The hard-boiled detective",
          "correct": False
        },
        {
          "answer": "The idealistic hero",
          "correct": True
        },
        {
          "answer": "The corrupt cop",
          "correct": False
        }
      ],
      "explanation": "Film noir typically features morally ambiguous characters rather than clear-cut heroes with idealistic motivations.",
      "difficulty": 2
    },
    {
      "questions": "Which film is often cited as the first True film noir?",
      "answers": [
        {
          "answer": "The Maltese Falcon (1941)",
          "correct": True
        },
        {
          "answer": "Casablanca (1942)",
          "correct": False
        },
        {
          "answer": "Citizen Kane (1941)",
          "correct": False
        },
        {
          "answer": "Double Indemnity (1944)",
          "correct": False
        }
      ],
      "explanation": "The Maltese Falcon, directed by John Huston and starring Humphrey Bogart, is widely considered the first major noir film.",
      "difficulty": 3
    },
    {
      "questions": "What term do film scholars use for modern films that adopt film noir style and themes?",
      "answers": [
        {
          "answer": "Post-noir",
          "correct": False
        },
        {
          "answer": "Neo-noir",
          "correct": True
        },
        {
          "answer": "Modern noir",
          "correct": False
        }
      ],
      "explanation": "Neo-noir refers to films made after the classic period that incorporate noir themes, styles, and motifs.",
      "difficulty": 2
    }
    ],
    "Stand-up History": [
    {
      "questions": "Which entertainment venue was crucial to early stand-up comedy in America?",
      "answers": [
        {
          "answer": "Broadway theaters",
          "correct": False
        },
        {
          "answer": "Vaudeville circuits",
          "correct": True
        },
        {
          "answer": "Television studios",
          "correct": False
        }
      ],
      "explanation": "Vaudeville circuits of the early 20th century provided the first major platform for comedic performers in America.",
      "difficulty": 2
    },
    {
      "questions": "Who is often called the 'father of modern stand-up comedy'?",
      "answers": [
        {
          "answer": "Lenny Bruce",
          "correct": True
        },
        {
          "answer": "Bob Hope",
          "correct": False
        },
        {
          "answer": "Jack Benny",
          "correct": False
        },
        {
          "answer": "Milton Berle",
          "correct": False
        }
      ],
      "explanation": "Lenny Bruce pioneered personal, controversial material and faced legal battles that changed the boundaries of comedy.",
      "difficulty": 2
    },
    {
      "questions": "Which decade saw the first major 'comedy boom' with comedy clubs opening across America?",
      "answers": [
        {
          "answer": "1960s",
          "correct": False
        },
        {
          "answer": "1970s",
          "correct": False
        },
        {
          "answer": "1980s",
          "correct": True
        },
        {
          "answer": "1990s",
          "correct": False
        }
      ],
      "explanation": "The 1980s saw an explosion of comedy clubs across America, with stand-up becoming a mainstream entertainment option.",
      "difficulty": 2
    },
    {
      "questions": "Which TV show, premiering in 1975, became a major launching pad for stand-up comedians?",
      "answers": [
        {
          "answer": "The Tonight Show",
          "correct": False
        },
        {
          "answer": "Saturday Night Live",
          "correct": True
        },
        {
          "answer": "The Ed Sullivan Show",
          "correct": False
        },
        {
          "answer": "In Living Color",
          "correct": False
        }
      ],
      "explanation": "SNL has launched numerous comedians' careers since 1975, providing a national platform for stand-up performers.",
      "difficulty": 1
    },
    {
      "questions": "What innovation has most dramatically changed stand-up comedy distribution in the 21st century?",
      "answers": [
        {
          "answer": "Cable TV specials",
          "correct": False
        },
        {
          "answer": "Streaming platforms",
          "correct": True
        },
        {
          "answer": "Radio broadcasts",
          "correct": False
        }
      ],
      "explanation": "Streaming platforms like Netflix, YouTube, and podcasts have revolutionized how comedy is distributed and consumed.",
      "difficulty": 1
    }
    ],
    "Inflation": [
    {
      "questions": "What is inflation?",
      "answers": [
        {
          "answer": "Increase in economic output",
          "correct": False
        },
        {
          "answer": "General increase in prices and fall in the purchasing value of money",
          "correct": True
        },
        {
          "answer": "Increase in unemployment",
          "correct": False
        }
      ],
      "explanation": "Inflation is the rate at which the general level of prices for goods and services rises, eroding purchasing power.",
      "difficulty": 1
    },
    {
      "questions": "Which of these is NOT a common cause of inflation?",
      "answers": [
        {
          "answer": "Increase in production costs",
          "correct": False
        },
        {
          "answer": "Excess money supply",
          "correct": False
        },
        {
          "answer": "Decrease in consumer demand",
          "correct": True
        },
        {
          "answer": "Supply chain disruptions",
          "correct": False
        }
      ],
      "explanation": "Decreased consumer demand typically causes deflation (falling prices), not inflation.",
      "difficulty": 2
    },
    {
      "questions": "What is 'hyperinflation'?",
      "answers": [
        {
          "answer": "Inflation between 10-20% annually",
          "correct": False
        },
        {
          "answer": "Extremely high and typically accelerating inflation that rapidly erodes currency value",
          "correct": True
        },
        {
          "answer": "Inflation that only affects luxury goods",
          "correct": False
        }
      ],
      "explanation": "Hyperinflation is extremely rapid inflation, usually exceeding 50% per month, causing severe economic disruption.",
      "difficulty": 1
    },
    {
      "questions": "Which economic theory suggests that inflation results primarily from increases in the money supply?",
      "answers": [
        {
          "answer": "Keynesian economics",
          "correct": False
        },
        {
          "answer": "Monetarism",
          "correct": True
        },
        {
          "answer": "Supply-side economics",
          "correct": False
        },
        {
          "answer": "Austrian economics",
          "correct": False
        }
      ],
      "explanation": "Monetarism, associated with economist Milton Friedman, holds that inflation is primarily caused by money supply growth.",
      "difficulty": 3
    },
    {
      "questions": "What is the term for inflation caused by rising production costs?",
      "answers": [
        {
          "answer": "Demand-pull inflation",
          "correct": False
        },
        {
          "answer": "Cost-push inflation",
          "correct": True
        },
        {
          "answer": "Stagflation",
          "correct": False
        },
        {
          "answer": "Hyperinflation",
          "correct": False
        }
      ],
      "explanation": "Cost-push inflation occurs when production costs increase, forcing businesses to raise prices to maintain profit margins.",
      "difficulty": 2
    }
    ],
    "Bridge Design": [
    {
      "questions": "What is the main purpose of a bridge's abutment?",
      "answers": [
        {
          "answer": "To connect bridge sections together",
          "correct": False
        },
        {
          "answer": "To support the ends of the bridge and connect it to the land",
          "correct": True
        },
        {
          "answer": "To allow for thermal expansion",
          "correct": False
        }
      ],
      "explanation": "Abutments are structures at the ends of bridges that support the superstructure and contain lateral pressures of earth.",
      "difficulty": 2
    },
    {
      "questions": "Which bridge type uses tension cables to support the deck from towers?",
      "answers": [
        {
          "answer": "Arch bridge",
          "correct": False
        },
        {
          "answer": "Suspension bridge",
          "correct": True
        },
        {
          "answer": "Beam bridge",
          "correct": False
        },
        {
          "answer": "Truss bridge",
          "correct": False
        }
      ],
      "explanation": "Suspension bridges use large main cables hung between towers, with vertical suspender cables supporting the deck.",
      "difficulty": 1
    },
    {
      "questions": "What is the primary force that an arch bridge converts to compression?",
      "answers": [
        {
          "answer": "Tension",
          "correct": True
        },
        {
          "answer": "Torsion",
          "correct": False
        },
        {
          "answer": "Shear",
          "correct": False
        }
      ],
      "explanation": "Arch bridges efficiently convert tensile forces into compression, which stone and concrete can resist well.",
      "difficulty": 2
    },
    {
      "questions": "Which bridge type is typically the most economical for short spans under 80 feet?",
      "answers": [
        {
          "answer": "Suspension bridge",
          "correct": False
        },
        {
          "answer": "Cantilever bridge",
          "correct": False
        },
        {
          "answer": "Simple beam/girder bridge",
          "correct": True
        },
        {
          "answer": "Cable-stayed bridge",
          "correct": False
        }
      ],
      "explanation": "Beam bridges are the simplest and most economical design for short spans, using horizontal beams supported by piers.",
      "difficulty": 2
    },
    {
      "questions": "What engineering challenge do engineers address with expansion joints in bridges?",
      "answers": [
        {
          "answer": "Wind resistance",
          "correct": False
        },
        {
          "answer": "Water drainage",
          "correct": False
        },
        {
          "answer": "Material expansion and contraction due to temperature changes",
          "correct": True
        }
      ],
      "explanation": "Expansion joints allow bridges to expand and contract with temperature changes without creating damaging stresses.",
      "difficulty": 2
    }
    ],
    "Crypto Markets": [
    {
      "questions": "What is a blockchain in the context of cryptocurrencies?",
      "answers": [
        {
          "answer": "A type of cryptocurrency wallet",
          "correct": False
        },
        {
          "answer": "A digital ledger of all transactions distributed across a network of computers",
          "correct": True
        },
        {
          "answer": "A government regulation on trading cryptocurrencies",
          "correct": False
        }
      ],
      "explanation": "Blockchain is a distributed, immutable ledger technology that records all transactions across many computers.",
      "difficulty": 1
    },
    {
      "questions": "What is a 'whale' in cryptocurrency markets?",
      "answers": [
        {
          "answer": "A type of cryptocurrency named after marine animals",
          "correct": False
        },
        {
          "answer": "A hacker who steals cryptocurrencies",
          "correct": False
        },
        {
          "answer": "An investor who holds a large amount of cryptocurrency",
          "correct": True
        },
        {
          "answer": "A major cryptocurrency exchange",
          "correct": False
        }
      ],
      "explanation": "Whales are individuals or entities that hold enough cryptocurrency to potentially influence market prices with their trades.",
      "difficulty": 1
    },
    {
      "questions": "What is 'mining' in the context of cryptocurrencies like Bitcoin?",
      "answers": [
        {
          "answer": "Extracting digital coins from virtual caves",
          "correct": False
        },
        {
          "answer": "The process of validating transactions and adding them to the blockchain",
          "correct": True
        },
        {
          "answer": "Converting one cryptocurrency to another",
          "correct": False
        }
      ],
      "explanation": "Mining involves solving complex mathematical problems to validate transactions and add blocks to the blockchain.",
      "difficulty": 1
    },
    {
      "questions": "What is a 'smart contract' in cryptocurrency markets?",
      "answers": [
        {
          "answer": "A legally binding agreement between cryptocurrency exchanges",
          "correct": False
        },
        {
          "answer": "Self-executing code that automatically enforces and executes agreement terms",
          "correct": True
        },
        {
          "answer": "A contract to buy cryptocurrencies at a predetermined price",
          "correct": False
        },
        {
          "answer": "An insurance policy for cryptocurrency holdings",
          "correct": False
        }
      ],
      "explanation": "Smart contracts are self-executing programs stored on a blockchain that run when predetermined conditions are met.",
      "difficulty": 2
    },
    {
      "questions": "What is 'DeFi' in cryptocurrency markets?",
      "answers": [
        {
          "answer": "Defense Finance, a security system for cryptocurrencies",
          "correct": False
        },
        {
          "answer": "Decentralized Finance, financial services without traditional intermediaries",
          "correct": True
        },
        {
          "answer": "Defined Fiat, a cryptocurrency backed by traditional currency",
          "correct": False
        }
      ],
      "explanation": "DeFi (Decentralized Finance) uses blockchain to create financial services without traditional central authorities.",
      "difficulty": 2
    }
    ],
    "Coral Reefs": [
    {
      "questions": "What organisms are primarily responsible for building coral reefs?",
      "answers": [
        {
          "answer": "Fish",
          "correct": False
        },
        {
          "answer": "Coral polyps",
          "correct": True
        },
        {
          "answer": "Algae",
          "correct": False
        },
        {
          "answer": "Sea turtles",
          "correct": False
        }
      ],
      "explanation": "Coral reefs are built by tiny animals called coral polyps that secrete calcium carbonate skeletons.",
      "difficulty": 1
    },
    {
      "questions": "What is coral bleaching?",
      "answers": [
        {
          "answer": "A natural process where corals clean themselves",
          "correct": False
        },
        {
          "answer": "The loss of colorful algae living in coral tissues due to stress, turning corals white",
          "correct": True
        },
        {
          "answer": "The application of chemicals to make coral reefs more visible to tourists",
          "correct": False
        }
      ],
      "explanation": "Bleaching occurs when stressed corals expel their symbiotic algae (zooxanthellae), losing their color and main food source.",
      "difficulty": 1
    },
    {
      "questions": "Which of these is NOT a major threat to coral reefs?",
      "answers": [
        {
          "answer": "Ocean acidification",
          "correct": False
        },
        {
          "answer": "Rising sea temperatures",
          "correct": False
        },
        {
          "answer": "Increasing sea turtle populations",
          "correct": True
        },
        {
          "answer": "Pollution runoff",
          "correct": False
        }
      ],
      "explanation": "Sea turtles are actually beneficial to reef ecosystems; they don't threaten reefs like climate change and pollution do.",
      "difficulty": 2
    },
    {
      "questions": "What percentage of marine species are estimated to depend on coral reefs?",
      "answers": [
        {
          "answer": "Less than 5%",
          "correct": False
        },
        {
          "answer": "Around 10-15%",
          "correct": False
        },
        {
          "answer": "About 25%",
          "correct": True
        },
        {
          "answer": "Over 50%",
          "correct": False
        }
      ],
      "explanation": "Though covering less than 1% of the ocean floor, coral reefs support approximately 25% of all marine species.",
      "difficulty": 2
    },
    {
      "questions": "What is the symbiotic relationship between coral and zooxanthellae?",
      "answers": [
        {
          "answer": "Zooxanthellae harm the coral but are needed for reproduction",
          "correct": False
        },
        {
          "answer": "Corals provide protection while zooxanthellae provide nutrients through photosynthesis",
          "correct": True
        },
        {
          "answer": "Zooxanthellae clean the coral of parasites",
          "correct": False
        }
      ],
      "explanation": "Corals provide zooxanthellae with shelter and compounds for photosynthesis, while receiving oxygen and nutrients in return.",
      "difficulty": 2
    }
    ],
    "Ancient Rome": [
    {
      "questions": "Who was the first Roman Emperor?",
      "answers": [
        {
          "answer": "Julius Caesar",
          "correct": False
        },
        {
          "answer": "Augustus (Octavian)",
          "correct": True
        },
        {
          "answer": "Constantine",
          "correct": False
        },
        {
          "answer": "Marcus Aurelius",
          "correct": False
        }
      ],
      "explanation": "Augustus, formerly Octavian, became the first Roman Emperor in 27 BCE after defeating Mark Antony and Cleopatra.",
      "difficulty": 1
    },
    {
      "questions": "What was the main legislative body of the Roman Republic?",
      "answers": [
        {
          "answer": "The Senate",
          "correct": True
        },
        {
          "answer": "The Consul",
          "correct": False
        },
        {
          "answer": "The Praetorian Guard",
          "correct": False
        }
      ],
      "explanation": "The Senate was the principal legislative assembly, originally representing patrician families.",
      "difficulty": 2
    },
    {
      "questions": "Which Roman structure used innovative concrete dome construction?",
      "answers": [
        {
          "answer": "The Colosseum",
          "correct": False
        },
        {
          "answer": "The Pantheon",
          "correct": True
        },
        {
          "answer": "The Forum",
          "correct": False
        },
        {
          "answer": "The Circus Maximus",
          "correct": False
        }
      ],
      "explanation": "The Pantheon features a concrete dome with an oculus, demonstrating Roman mastery of concrete architecture.",
      "difficulty": 2
    }
    ],
    "Intellectual Property": [
    {
      "questions": "What does a patent protect?",
      "answers": [
        {
          "answer": "Creative works like books and music",
          "correct": False
        },
        {
          "answer": "Inventions and new processes",
          "correct": True
        },
        {
          "answer": "Business names and logos",
          "correct": False
        }
      ],
      "explanation": "Patents protect inventions and processes, giving inventors exclusive rights for a limited time period.",
      "difficulty": 1
    },
    {
      "questions": "What is 'fair use' in copyright law?",
      "answers": [
        {
          "answer": "Using copyrighted material without permission for limited purposes like criticism or education",
          "correct": True
        },
        {
          "answer": "Using material if you give credit to the original creator",
          "correct": False
        },
        {
          "answer": "A license that allows free use of copyrighted material",
          "correct": False
        },
        {
          "answer": "Using material that has been publicly available for more than 5 years",
          "correct": False
        }
      ],
      "explanation": "Fair use allows limited use of copyrighted material without permission for purposes like commentary, criticism, or education.",
      "difficulty": 2
    },
    {
      "questions": "What is the main difference between a trademark and copyright?",
      "answers": [
        {
          "answer": "Trademarks last longer than copyrights",
          "correct": False
        },
        {
          "answer": "Trademarks protect brand identifiers while copyrights protect creative works",
          "correct": True
        },
        {
          "answer": "Trademarks are international while copyrights are national",
          "correct": False
        }
      ],
      "explanation": "Trademarks protect names, logos, and slogans that identify brands, while copyrights protect original creative expressions.",
      "difficulty": 2
    }
    ],
    "Dystopian Fiction": [
    {
      "questions": "Which novel features a society where books are banned and burned?",
      "answers": [
        {
          "answer": "1984",
          "correct": False
        },
        {
          "answer": "Fahrenheit 451",
          "correct": True
        },
        {
          "answer": "Brave New World",
          "correct": False
        },
        {
          "answer": "The Handmaid's Tale",
          "correct": False
        }
      ],
      "explanation": "Ray Bradbury's Fahrenheit 451 depicts a future where books are outlawed and 'firemen' burn any that are found.",
      "difficulty": 1
    },
    {
      "questions": "What dystopian concept is central to 'The Hunger Games'?",
      "answers": [
        {
          "answer": "Mind control through television",
          "correct": False
        },
        {
          "answer": "Forced deadly competition as entertainment and political control",
          "correct": True
        },
        {
          "answer": "Environmental collapse",
          "correct": False
        }
      ],
      "explanation": "The Hunger Games depicts a society where children fight to the death as punishment for past rebellion and entertainment.",
      "difficulty": 1
    },
    {
      "questions": "Which dystopian element appears most frequently across the genre?",
      "answers": [
        {
          "answer": "Alien invasion",
          "correct": False
        },
        {
          "answer": "Time travel disasters",
          "correct": False
        },
        {
          "answer": "Authoritarian government control and surveillance",
          "correct": True
        },
        {
          "answer": "Zombie apocalypse",
          "correct": False
        }
      ],
      "explanation": "Authoritarian control, surveillance, and restriction of individual freedoms are fundamental elements in most dystopian fiction.",
      "difficulty": 2
    }
    ],
    "Jazz Evolution": [
    {
      "questions": "Which city is considered the birthplace of jazz?",
      "answers": [
        {
          "answer": "Chicago",
          "correct": False
        },
        {
          "answer": "New York",
          "correct": False
        },
        {
          "answer": "New Orleans",
          "correct": True
        },
        {
          "answer": "Memphis",
          "correct": False
        }
      ],
      "explanation": "New Orleans is widely recognized as jazz's birthplace, emerging in the late 19th and early 20th centuries.",
      "difficulty": 1
    },
    {
      "questions": "Which jazz style emerged in the 1940s, characterized by complex harmonies and fast tempos?",
      "answers": [
        {
          "answer": "Swing",
          "correct": False
        },
        {
          "answer": "Bebop",
          "correct": True
        },
        {
          "answer": "Cool jazz",
          "correct": False
        },
        {
          "answer": "Fusion",
          "correct": False
        }
      ],
      "explanation": "Bebop, pioneered by Charlie Parker and Dizzy Gillespie, featured rapid tempos, complex chord progressions, and improvisation.",
      "difficulty": 2
    },
    {
      "questions": "Which instrument did Louis Armstrong play, becoming one of jazz's most influential figures?",
      "answers": [
        {
          "answer": "Saxophone",
          "correct": False
        },
        {
          "answer": "Piano",
          "correct": False
        },
        {
          "answer": "Trumpet",
          "correct": True
        }
      ],
      "explanation": "Louis Armstrong played the trumpet and was known for his distinctive improvisation style and scat singing.",
      "difficulty": 1
    }
    ],
    "Mindfulness": [
    {
      "questions": "What is the main focus of mindfulness practice?",
      "answers": [
        {
          "answer": "Clearing the mind of all thoughts",
          "correct": False
        },
        {
          "answer": "Awareness of present moment experiences without judgment",
          "correct": True
        },
        {
          "answer": "Achieving a state of happiness",
          "correct": False
        },
        {
          "answer": "Visualizing successful outcomes",
          "correct": False
        }
      ],
      "explanation": "Mindfulness involves paying attention to current experiences, including thoughts, feelings, and sensations, without judgment.",
      "difficulty": 1
    },
    {
      "questions": "Which tradition is most associated with the origins of mindfulness practices?",
      "answers": [
        {
          "answer": "Hinduism",
          "correct": False
        },
        {
          "answer": "Christianity",
          "correct": False
        },
        {
          "answer": "Buddhism",
          "correct": True
        },
        {
          "answer": "Taoism",
          "correct": False
        }
      ],
      "explanation": "While mindfulness exists in many traditions, it's most associated with Buddhist meditation practices, especially Vipassana.",
      "difficulty": 1
    },
    {
      "questions": "What is the term for the mental state of being fully engaged in the present moment?",
      "answers": [
        {
          "answer": "Flow",
          "correct": True
        },
        {
          "answer": "Mindlessness",
          "correct": False
        },
        {
          "answer": "Transcendence",
          "correct": False
        }
      ],
      "explanation": "Flow, described by psychologist Mihaly Csikszentmihalyi, is a state of complete immersion in a present activity.",
      "difficulty": 2
    }
    ],
    "Electoral Systems": [
    {
      "questions": "What is a 'first-past-the-post' electoral system?",
      "answers": [
        {
          "answer": "A system where voters rank candidates in order of preference",
          "correct": False
        },
        {
          "answer": "A system where the candidate with the most votes wins, even without a majority",
          "correct": True
        },
        {
          "answer": "A system where seats are allocated proportionally to votes received",
          "correct": False
        }
      ],
      "explanation": "First-past-the-post is a simple plurality system where the candidate with the most votes wins, regardless of percentage.",
      "difficulty": 1
    },
    {
      "questions": "What is proportional representation?",
      "answers": [
        {
          "answer": "A system where older voters get more voting power",
          "correct": False
        },
        {
          "answer": "A system where parties gain seats in proportion to the number of votes received",
          "correct": True
        },
        {
          "answer": "A system where each district gets representatives proportional to its population",
          "correct": False
        }
      ],
      "explanation": "Proportional representation systems allocate seats so that parties' share of seats roughly matches their share of votes.",
      "difficulty": 2
    },
    {
      "questions": "Which electoral system is used for parliamentary elections in Germany?",
      "answers": [
        {
          "answer": "First-past-the-post",
          "correct": False
        },
        {
          "answer": "Mixed-member proportional representation",
          "correct": True
        },
        {
          "answer": "Two-round system",
          "correct": False
        },
        {
          "answer": "Alternative vote",
          "correct": False
        }
      ],
      "explanation": "Germany uses mixed-member proportional representation, combining single-member districts with proportional party lists.",
      "difficulty": 3
    }
    ],
    "Climate Change": [
    {
      "questions": "Which gas is the most significant human-caused greenhouse gas?",
      "answers": [
        {
          "answer": "Oxygen",
          "correct": False
        },
        {
          "answer": "Carbon dioxide",
          "correct": True
        },
        {
          "answer": "Nitrogen",
          "correct": False
        },
        {
          "answer": "Hydrogen",
          "correct": False
        }
      ],
      "explanation": "Carbon dioxide (CO2) from burning fossil fuels is the primary greenhouse gas driving human-caused climate change.",
      "difficulty": 1
    },
    {
      "questions": "What international agreement aimed to limit global warming to well below 2°C?",
      "answers": [
        {
          "answer": "Kyoto Protocol",
          "correct": False
        },
        {
          "answer": "Montreal Protocol",
          "correct": False
        },
        {
          "answer": "Paris Agreement",
          "correct": True
        }
      ],
      "explanation": "The 2015 Paris Agreement is a landmark accord where nations committed to limiting warming to well below 2°C above pre-industrial levels.",
      "difficulty": 1
    },
    {
      "questions": "Which of these is NOT a direct effect of climate change?",
      "answers": [
        {
          "answer": "Rising sea levels",
          "correct": False
        },
        {
          "answer": "Increased frequency of extreme weather events",
          "correct": False
        },
        {
          "answer": "Depletion of the ozone layer",
          "correct": True
        },
        {
          "answer": "Changes in precipitation patterns",
          "correct": False
        }
      ],
      "explanation": "Ozone depletion is a separate environmental issue caused by CFCs, not directly by greenhouse gases causing climate change.",
      "difficulty": 2
    }
    ],
    "Content Creators": [
    {
      "questions": "What is a 'content creator'?",
      "answers": [
        {
          "answer": "A person who only works for established media companies",
          "correct": False
        },
        {
          "answer": "Someone who produces digital content like videos, blogs, podcasts, or social media posts",
          "correct": True
        },
        {
          "answer": "A software program that automatically generates online content",
          "correct": False
        }
      ],
      "explanation": "Content creators develop and share original content across various digital platforms, often building personal audiences.",
      "difficulty": 1
    },
    {
      "questions": "What is 'monetization' for content creators?",
      "answers": [
        {
          "answer": "The process of making content more engaging",
          "correct": False
        },
        {
          "answer": "Converting content to different file formats",
          "correct": False
        },
        {
          "answer": "The methods used to earn income from digital content",
          "correct": True
        }
      ],
      "explanation": "Monetization refers to various ways creators earn money from content, such as ads, sponsorships, or subscription models.",
      "difficulty": 1
    },
    {
      "questions": "Which metric is most important for determining YouTube ad revenue?",
      "answers": [
        {
          "answer": "Number of likes",
          "correct": False
        },
        {
          "answer": "Watch time",
          "correct": True
        },
        {
          "answer": "Number of comments",
          "correct": False
        },
        {
          "answer": "Video quality settings",
          "correct": False
        }
      ],
      "explanation": "Watch time (how long viewers spend watching content) is the primary metric YouTube uses for ad revenue calculation.",
      "difficulty": 2
    }
    ],
    "Olympic History": [
    {
      "questions": "Where were the first modern Olympic Games held?",
      "answers": [
        {
          "answer": "Rome, Italy",
          "correct": False
        },
        {
          "answer": "Paris, France",
          "correct": False
        },
        {
          "answer": "Athens, Greece",
          "correct": True
        },
        {
          "answer": "London, England",
          "correct": False
        }
      ],
      "explanation": "The first modern Olympic Games were held in Athens, Greece in 1896, honoring the ancient Games' birthplace.",
      "difficulty": 1
    },
    {
      "questions": "Which of these sports has featured in every modern Summer Olympics?",
      "answers": [
        {
          "answer": "Soccer (Football)",
          "correct": False
        },
        {
          "answer": "Swimming",
          "correct": False
        },
        {
          "answer": "Athletics (Track and Field)",
          "correct": True
        },
        {
          "answer": "Gymnastics",
          "correct": False
        }
      ],
      "explanation": "Athletics (track and field) has been part of every modern Summer Olympics since their inception in 1896.",
      "difficulty": 2
    },
    {
      "questions": "When were women first allowed to compete in the modern Olympic Games?",
      "answers": [
        {
          "answer": "1896 (first modern Olympics)",
          "correct": False
        },
        {
          "answer": "1900",
          "correct": True
        },
        {
          "answer": "1928",
          "correct": False
        },
        {
          "answer": "1952",
          "correct": False
        }
      ],
      "explanation": "Women first competed at the 1900 Paris Olympics in just five sports: tennis, sailing, croquet, equestrian, and golf.",
      "difficulty": 2
    }
    ],
    "AI Ethics": [
    {
      "questions": "What is algorithmic bias?",
      "answers": [
        {
          "answer": "When AI systems perform differently for different groups, often unfairly",
          "correct": True
        },
        {
          "answer": "When AI systems are programmed to favor certain political viewpoints",
          "correct": False
        },
        {
          "answer": "When AI makes deliberate choices to harm humans",
          "correct": False
        }
      ],
      "explanation": "Algorithmic bias occurs when AI systems reflect existing prejudices or create unfair outcomes for certain groups of people.",
      "difficulty": 1
    },
    {
      "questions": "What ethical principle emphasizes that AI systems should be transparent in how they make decisions?",
      "answers": [
        {
          "answer": "Beneficence",
          "correct": False
        },
        {
          "answer": "Explainability",
          "correct": True
        },
        {
          "answer": "Non-maleficence",
          "correct": False
        },
        {
          "answer": "Autonomy",
          "correct": False
        }
      ],
      "explanation": "Explainability requires that AI systems' decision-making processes can be understood and explained to affected parties.",
      "difficulty": 2
    },
    {
      "questions": "What is the 'alignment problem' in AI ethics?",
      "answers": [
        {
          "answer": "Making sure AI systems can communicate with each other",
          "correct": False
        },
        {
          "answer": "Ensuring AI goals and values align with human goals and values",
          "correct": True
        },
        {
          "answer": "Properly aligning AI hardware components",
          "correct": False
        }
      ],
      "explanation": "The alignment problem concerns ensuring AI systems pursue objectives aligned with human values, especially as they grow more capable.",
      "difficulty": 3
    }
    ],
    "Gothic Architecture": [
    {
      "questions": "What architectural feature is most characteristic of Gothic cathedrals?",
      "answers": [
        {
          "answer": "Domed roofs",
          "correct": False
        },
        {
          "answer": "Pointed arches",
          "correct": True
        },
        {
          "answer": "Columns with Corinthian capitals",
          "correct": False
        },
        {
          "answer": "Flat, undecorated facades",
          "correct": False
        }
      ],
      "explanation": "Pointed arches are a defining feature of Gothic architecture, replacing the rounded arches of Romanesque style.",
      "difficulty": 1
    },
    {
      "questions": "What is a flying buttress?",
      "answers": [
        {
          "answer": "A decorative winged statue on Gothic buildings",
          "correct": False
        },
        {
          "answer": "An arched exterior support transferring thrust from upper walls to outer supports",
          "correct": True
        },
        {
          "answer": "A type of Gothic tower design",
          "correct": False
        }
      ],
      "explanation": "Flying buttresses are external arched supports that allow Gothic walls to be taller and thinner with larger windows.",
      "difficulty": 2
    },
    {
      "questions": "In which century did Gothic architecture first develop?",
      "answers": [
        {
          "answer": "9th century",
          "correct": False
        },
        {
          "answer": "12th century",
          "correct": True
        },
        {
          "answer": "15th century",
          "correct": False
        },
        {
          "answer": "18th century",
          "correct": False
        }
      ],
      "explanation": "Gothic architecture emerged in the mid-12th century in France and spread throughout Europe over the next several centuries.",
      "difficulty": 2
    }
    ],
    "Urban Legends": [
    {
      "questions": "What defines an urban legend?",
      "answers": [
        {
          "answer": "A story that only takes place in cities",
          "correct": False
        },
        {
          "answer": "A modern folklore story of questionsable truth, usually cautionary or shocking",
          "correct": True
        },
        {
          "answer": "A True crime story from an urban area",
          "correct": False
        }
      ],
      "explanation": "Urban legends are modern folklore passed through cultures, often cautionary tales with unverified but believable elements.",
      "difficulty": 1
    },
    {
      "questions": "Which famous urban legend involves checking Halloween candy for tampering?",
      "answers": [
        {
          "answer": "The Vanishing Hitchhiker",
          "correct": False
        },
        {
          "answer": "The Hook Man",
          "correct": False
        },
        {
          "answer": "Halloween Sadism (Razor blades/poison in candy)",
          "correct": True
        },
        {
          "answer": "Bloody Mary",
          "correct": False
        }
      ],
      "explanation": "The legend of strangers tampering with Halloween candy persists despite extremely few verified incidents.",
      "difficulty": 1
    },
    {
      "questions": "What term describes when an urban legend adapts to different locations and time periods?",
      "answers": [
        {
          "answer": "Localization",
          "correct": False
        },
        {
          "answer": "Ostension",
          "correct": False
        },
        {
          "answer": "Variant",
          "correct": True
        },
        {
          "answer": "Folklorization",
          "correct": False
        }
      ],
      "explanation": "Variants occur as legends evolve across different contexts, with core elements remaining while details change to fit local concerns.",
      "difficulty": 3
    }
    ]
}


for topic in topics:
    print(f'--Created Topic {topic.get("topic_name")}--')
    topic_id = post_topic(topic)
    topic_questions = questions.get(topic.get("topic_name"), {})
    print(f'--Adding {len(topic_questions)} questions to {topic.get("topic_name")}--')
    for question_info in topic_questions:
        question_info['topic_id'] = topic_id
        post_question(question_info)


