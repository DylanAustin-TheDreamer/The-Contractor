import random


STATION_PREFIXES = [
    "Station",
    "Port",
    "Haven",
    "Relay",
    "Outpost",
    "Terminal",
    "Spindle",
    "Citadel",
]

PHONETIC_ONSETS = [
    "",
    "b",
    "br",
    "c",
    "d",
    "dr",
    "f",
    "g",
    "gr",
    "h",
    "j",
    "k",
    "kr",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "sh",
    "sk",
    "t",
    "th",
    "tr",
    "v",
    "w",
    "x",
    "z",
]

PHONETIC_NUCLEI = [
    "a",
    "ae",
    "ai",
    "e",
    "ei",
    "i",
    "ia",
    "o",
    "oi",
    "u",
    "ua",
    "y",
]

PHONETIC_CODAS = [
    "",
    "k",
    "l",
    "m",
    "n",
    "r",
    "s",
    "t",
    "th",
    "x",
    "z",
]

STATION_DESCRIPTORS = [
    "Anchor",
    "Array",
    "Bastion",
    "Crown",
    "Drift",
    "Exchange",
    "Forge",
    "Gate",
    "Halo",
    "Junction",
    "Lattice",
    "Market",
    "Nexus",
    "Reach",
    "Ring",
    "Spire",
    "Watch",
    "Yard",
]

STATION_CALLSIGNS = [
    "Alpha",
    "Bravo",
    "Echo",
    "Foxtrot",
    "Hotel",
    "Kilo",
    "Lima",
    "November",
    "Oscar",
    "Quebec",
    "Romeo",
    "Sierra",
    "Tango",
    "Victor",
    "Whiskey",
    "X-ray",
]


def _phonetic_name():
    """Build a pronounceable two- or three-syllable station name."""

    syllable_count = random.choice((2, 2, 3))
    syllables = []
    for _ in range(syllable_count):
        syllables.append(
            random.choice(PHONETIC_ONSETS)
            + random.choice(PHONETIC_NUCLEI)
            + random.choice(PHONETIC_CODAS)
        )

    return "".join(syllables).capitalize()


def station_name_gen():
    """Generate a random, readable name for a space station."""

    name = _phonetic_name()
    style = random.randrange(4)

    if style == 0:
        return f"{random.choice(STATION_PREFIXES)}-{name}-{random.randint(1, 99)}"
    if style == 1:
        return f"{name} {random.choice(STATION_DESCRIPTORS)}"
    if style == 2:
        return f"{random.choice(STATION_PREFIXES)} {name}"
    return f"{name} {random.choice(STATION_CALLSIGNS)}"
