
import random


SETTLEMENT_PREFIX = [
    "New",
    "Old",
    "Mission",
    "Ambitious",
    "Ideal",
    "Forever",
    "Eternal",
    "Impermanent",
    "Friendly",
    "Peaceful",
    "People's",
    "United",
]
SETTLEMENT_SUFFIX = [
    "Eden",
    "Hope",
    "Dreamland",
    "Paradise",
    "Utopia",
    "Haven",
    "Sanctuary",
    "Boxes",
    "Holes in the wind",
    "Artificial Illuminations",
    "Evil"
]

def settlement_name_gen():
    """ Generate a random settlement name """

    return random.choice(SETTLEMENT_PREFIX) + " " + random.choice(SETTLEMENT_SUFFIX)