def get_knowledge(leaf_type):
    """
    Returns detailed information about the selected leaf type and condition.
    """
    knowledge = {
        "Pepper__bell___Bacterial_spot": {
            "Description": "Bacterial Spot is a common bacterial disease in bell peppers caused by Xanthomonas campestris.",
            "Symptoms": [
                "Dark, water-soaked spots on leaves and fruits.",
                "Yellow halos around spots.",
                "Scabby, cracked lesions on fruits."
            ],
            "Causes": [
                "High humidity and warm temperatures (25°C–30°C).",
                "Contaminated seeds or tools.",
                "Spread by water splashes or poor air circulation."
            ],
            "Prevention": [
                "Use certified, disease-free seeds.",
                "Ensure proper spacing for air circulation.",
                "Avoid overhead watering; use drip irrigation instead."
            ],
            "Cure": [
                "Apply copper-based fungicides early.",
                "Remove and destroy infected plants.",
                "Sanitize tools to prevent disease spread."
            ]
        },
        "Pepper__bell___healthy": {
            "Description": "Healthy bell pepper plants produce high yields of vibrant, nutritious fruits.",
            "Characteristics": [
                "Dark green, shiny leaves.",
                "Sturdy stems and consistent growth.",
                "Smooth, firm, and evenly colored fruits."
            ],
            "Care": [
                "Fertilize every 2-3 weeks with balanced NPK fertilizer.",
                "Provide 6-8 hours of sunlight daily.",
                "Keep soil consistently moist but avoid waterlogging."
            ],
            "Pest_Management": [
                "Use sticky traps for whiteflies and aphids.",
                "Release beneficial insects like ladybugs."
            ],
            "Harvesting": [
                "Harvest when fruits reach full size and desired color.",
                "Use clean shears to avoid damaging the plant."
            ]
        },
        "Potato___Early_blight": {
            "Description": "Early Blight is a fungal disease caused by Alternaria solani, affecting older potato plants.",
            "Symptoms": [
                "Dark brown spots with concentric rings on older leaves.",
                "Yellow halos around the spots.",
                "Premature leaf drop and reduced yield."
            ],
            "Causes": [
                "Warm, humid conditions (24°C–29°C).",
                "Infected crop debris in the soil.",
                "Overcrowded planting and poor airflow."
            ],
            "Prevention": [
                "Use certified, disease-free seeds.",
                "Rotate crops every 2 years.",
                "Ensure proper plant spacing."
            ],
            "Cure": [
                "Apply fungicides like chlorothalonil or mancozeb.",
                "Remove and destroy infected leaves.",
                "Use organic sprays like compost tea."
            ]
        },
        "Potato___Late_blight": {
            "Description": "Late Blight is a fungal-like disease caused by Phytophthora infestans, leading to plant destruction.",
            "Symptoms": [
                "Water-soaked, dark lesions on leaves and stems.",
                "White, fuzzy growth on leaf undersides in humid conditions.",
                "Rotting tubers with foul odor."
            ],
            "Causes": [
                "Prolonged wet and cool weather (10°C–20°C).",
                "Spread through windborne spores or infected tubers.",
                "Poor drainage and overcrowded planting."
            ],
            "Prevention": [
                "Plant resistant varieties and ensure good drainage.",
                "Use certified disease-free seeds.",
                "Clean and disinfect tools regularly."
            ],
            "Cure": [
                "Apply fungicides like metalaxyl or copper sulfate.",
                "Remove and burn infected plants immediately.",
                "Use neem oil or compost tea for early-stage control."
            ]
        },
        "Potato___healthy": {
            "Description": "Healthy potato plants yield high-quality, nutritious tubers.",
            "Characteristics": [
                "Bright green, fully developed leaves with no spots.",
                "Robust and upright stems.",
                "Uniform tubers, free from cracks or scabs."
            ],
            "Care": [
                "Prepare soil with compost and maintain pH 5.0–6.0.",
                "Apply balanced fertilizers at the right stages.",
                "Keep soil moist but not waterlogged."
            ],
            "Pest_Management": [
                "Inspect regularly for pests like Colorado potato beetles.",
                "Use biological controls or neem oil sprays."
            ],
            "Harvesting": [
                "Harvest when foliage dies back naturally.",
                "Cure tubers for 1–2 weeks before storage."
            ]
        },
        "Tomato_Bacterial_spot": {
            "Description": "Bacterial disease caused by Xanthomonas campestris.",
            "Symptoms": [
                "Small, water-soaked spots on leaves and fruits.",
                "Dark, scabby patches on fruits.",
                "Leaves turn yellow and drop prematurely."
            ],
            "Causes": [
                "High humidity and temperatures.",
                "Spread through contaminated seeds or splashing water."
            ],
            "Prevention": [
                "Use certified, disease-free seeds.",
                "Water at the base to prevent leaf wetness.",
                "Rotate crops annually."
            ],
            "Cure": [
                "Apply copper-based bactericides.",
                "Remove and destroy infected plants."
            ]
        },
        "Tomato_Early_blight": {
            "Description": "Fungal disease caused by Alternaria solani.",
            "Symptoms": [
                "Target-like spots with concentric rings on lower leaves.",
                "Yellowing and premature leaf drop.",
                "Dark, sunken spots on stems and fruits."
            ],
            "Causes": [
                "Warm, humid conditions.",
                "Infected crop debris or seeds."
            ],
            "Prevention": [
                "Rotate crops every two years.",
                "Space plants for good air circulation.",
                "Mulch to prevent soil splash."
            ],
            "Cure": [
                "Apply fungicides like chlorothalonil.",
                "Remove affected leaves promptly."
            ]
        },
        "Tomato_Late_blight": {
            "Description": "Fungal-like disease caused by Phytophthora infestans.",
            "Symptoms": [
                "Water-soaked lesions on leaves and stems.",
                "White fungal growth on the underside of leaves.",
                "Brown, rotten patches on fruits."
            ],
            "Causes": [
                "Prolonged wet, cool conditions.",
                "Spread by windborne spores."
            ],
            "Prevention": [
                "Plant resistant varieties.",
                "Ensure proper drainage.",
                "Avoid overcrowding."
            ],
            "Cure": [
                "Use fungicides like metalaxyl.",
                "Destroy infected plants."
            ]
        },
        "Tomato_Leaf_Mold": {
            "Description": "Fungal disease caused by Passalora fulva.",
            "Symptoms": [
                "Yellow spots on the upper leaf surface.",
                "Olive-green to gray mold on the underside.",
                "Leaves curl, wither, and drop."
            ],
            "Causes": [
                "High humidity in greenhouses.",
                "Poor air circulation."
            ],
            "Prevention": [
                "Ventilate greenhouses and space plants adequately.",
                "Avoid overhead watering."
            ],
            "Cure": [
                "Use fungicides like copper oxychloride.",
                "Remove and destroy infected leaves."
            ]
        },
        "Tomato_Septoria_leaf_spot": {
            "Description": "Fungal disease caused by Septoria lycopersici.",
            "Symptoms": [
                "Small, circular spots with gray centers and dark edges.",
                "Leaves yellow and fall off."
            ],
            "Causes": [
                "Warm, humid conditions.",
                "Contaminated soil or debris."
            ],
            "Prevention": [
                "Remove plant debris after harvest.",
                "Use mulch to reduce soil splash."
            ],
            "Cure": [
                "Apply fungicides like mancozeb."
            ]
        },
        "Tomato_Spider_mites_Two_spotted_spider_mite": {
            "Description": "Pests that feed on plant sap, causing damage.",
            "Symptoms": [
                "Yellow stippling on leaves.",
                "Fine webbing under leaves.",
                "Leaves dry out and fall."
            ],
            "Causes": [
                "Hot, dry conditions."
            ],
            "Prevention": [
                "Spray water on leaves to dislodge mites.",
                "Introduce predatory mites (biological control)."
            ],
            "Cure": [
                "Use insecticidal soap or neem oil."
            ]
        },
        "Tomato_Target_Spot": {
            "Description": "Fungal disease caused by Corynespora cassiicola.",
            "Symptoms": [
                "Brown, concentric lesions on leaves and fruits.",
                "Premature leaf drop."
            ],
            "Causes": [
                "Warm, wet conditions."
            ],
            "Prevention": [
                "Plant disease-free seeds.",
                "Space plants adequately."
            ],
            "Cure": [
                "Apply fungicides like azoxystrobin."
            ]
        },
        "Tomato_Tomato_YellowLeaf_Curl_Virus": {
            "Description": "Viral disease spread by whiteflies.",
            "Symptoms": [
                "Curling, yellowing leaves.",
                "Stunted growth and reduced fruiting."
            ],
            "Causes": [
                "Whitefly infestations."
            ],
            "Prevention": [
                "Use insect-proof netting.",
                "Remove weeds harboring whiteflies."
            ],
            "Cure": [
                "No direct cure; control whiteflies with neem oil."
            ]
        },
        "Tomato_Tomato_mosaic_virus": {
            "Description": "Viral disease affecting leaves and fruits.",
            "Symptoms": [
                "Mosaic-like mottling of leaves.",
                "Deformed fruits with blotchy coloring."
            ],
            "Causes": [
                "Infected seeds or plant contact."
            ],
            "Prevention": [
                "Use resistant varieties.",
                "Wash hands and tools before handling plants."
            ],
            "Cure": [
                "Remove and destroy infected plants."
            ]
        },
        "Tomato_healthy": {
            "Description": "Healthy tomato plants produce high yields of firm, flavorful fruits.",
            "Characteristics": [
                "Vibrant green leaves without spots.",
                "Sturdy stems and consistent growth."
            ],
            "Care": [
                "Use balanced fertilizers.",
                "Water consistently, avoiding leaves.",
                "Prune suckers to improve airflow."
            ],
            "Harvesting": [
                "Pick fruits when fully ripened for the best flavor."
            ]
        }
    }
    return knowledge.get(leaf_type, "Information not available")
