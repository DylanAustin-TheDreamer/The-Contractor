import random
from Utilities.settlement_names import settlement_name_gen
from Utilities.grid_maker import start_grid_making

SETTLEMENT_TYPES = [
    "rich",
    "poor",
    "old",
    "futuristic",
]
SETTLEMENT_AREAS = [
    "street",
    "backstreet",
    "market",
    "highstreet"
]
AREA_OBJECTS = [
    "lootable_box",
    "vending_machine",
    "placeable_area",
    "interior",
]

def make_grid():
    """ Make the 2D grid for storing area objects """

    board = start_grid_making(False)
    return make_areas(board);

def make_areas(board):
    """ Make the area object with details """

    map = board["board"]
    # Iterate through the board and replace 1s with area objects
    for row_index, row in enumerate(map):
        for column_index, area in enumerate(row):
            if area == 1:
                map[row_index][column_index] = {
                    "type": random.choice(SETTLEMENT_AREAS),
                    "object": random.choice(AREA_OBJECTS)
                }

    return board

def make_settlement(planet_id, solar_id):
    """ Function for generating settlements """

    settlement = {}
    # Need a function for generating 1s on the board
    # Within those array indexes, is an object.
    # The object will contain the type of area it is,
    # what will spawn in that area and at what quantity.
    """
        example: 
            type: Backstreet,
            vending machines: 0 or 1
            LootableBox: 0 - 2,
            placeableArea: 0 - 1,
    """

    # Test everything is wired right for now
    settlementEnvironment = {
        "solar_system_id": solar_id,
        "planet_id": planet_id,
        "settlement_name": settlement_name_gen(),
        "settlement_biome": random.choice(SETTLEMENT_TYPES),
        "settlement_map": make_grid()
    }
    settlement.update({"settlement_obj": settlementEnvironment})

    return settlement