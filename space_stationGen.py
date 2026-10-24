import random
from Utilities.space_station_names import station_name_gen
from Utilities.grid_maker import start_grid_making

SETTLEMENT_AREAS = [
    "reactor",
    "oxygen",
    "corridor",
    "storage",
    "canteen",
    "market",
    "military",
]
AREA_OBJECTS = [
    "lootable_box",
    "vending_machine",
    "cover",
    "hazard",
]

def make_grid():
    """ Make the 2D grid for storing area objects """

    board = start_grid_making(True)
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

def make_space_station(solar_system_id):
    """ Base function for space station generation """

    spaceStation = {}

    stationEnvironment = {
        "solar_system_id": solar_system_id,
        "station_name": station_name_gen(),
        "station_map": make_grid()
    }
    spaceStation.update({"station_obj": stationEnvironment})
    
    return spaceStation