import random


def generate_sun_art(type):
    """ Function for generating suns and art for suns """
    art = {}
    art.update({
        "sun": type,
        "art": f"{type}_{random.randint(1, 10)}.png"
    })
    return art