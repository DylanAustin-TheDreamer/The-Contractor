import random
import json

BIOMES = [
    "lush",
    "scorched",
    "barren",
    "frozen",
    "ocean"
]

def generate_planet_art():
    """ Function for generating biomes and art for planets """
    art = {}
    biome = random.choice(BIOMES)
    art.update({
        "biome": biome,
        "art": f"{biome}_{random.randint(1, 10)}.png"
    })
    return art