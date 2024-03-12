afflictions_library = {
        "allergies_medicated": {
            "name": "allergies_medicated",
            "cost": 30,
        },
        "allergies_unchecked": {
            "name": "allergies_unchecked",
            "health": -1,
            "happiness": -1,
        },
        "fleas": {
            "name": "fleas",
            "duration": float("inf"),
            "max_health": -1,
            "health": -2,
            "happiness": -5,
        },
        "obesity": {
            "name": "obesity",
            "duration": float("inf"),
        },
        "heartworm_unchecked": {
            "name": "heartworm_unchecked",
            "duration": 1,
            "health": -100,
        },
        "heartworm_medicated": {
            "name": "heartworm_medicated",
            "duration": 3,
            "time": 10,
            "cost": lambda dog : 800 + dog.weight * 10
        },
        "cancer_unchecked": {
            "name": "cancer",
            "duration": float("inf"),
            "max_health": -10,
            "health": -10,
            "time": 10,
            "happiness": -5,
        },
        "cancer_medicated": {
            "name": "cancer_medicated",
            "duration": 4,
            "cost": 600,
            "time": 10,
            "happiness": -5,
        },
    }
