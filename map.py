import json
import uuid
import random
from Utilities.solar_system_nameGen import generate_name_solar
from Utilities.planet_nameGen import generate_name_planet
from Utilities.planet_artGen import generate_planet_art
from settlementGen import make_settlement
from space_stationGen import make_space_station

def make_map(solar_system, the_great_galaxy, positionX, positionY):
    """ This function will generate a map """

    settlementObjects = {}
    spaceStationObjects = {}
    solar_system = {}
    solar_system.update({"id": generate_obj_id()})
    solar_system.update({"system_name": generate_name_solar()})
    solar_system.update({"positionX": positionX})
    solar_system.update({"positionY": positionY})
    solar_system.update({"wanted_level": 0})
    solar_system.update({"planets": random.randint(1, 4)})
    solar_system.update({"astroids": random.randint(100, 1000)})
    solar_system.update({"space_stations": random.randint(1, 4)})
    solar_system.update({"cargos_ships": random.randint(40, 80)})

    # for planets and settlements
    settlement_counter = 1
    for i in range(0, solar_system["planets"]):
        settlements = random.randint(0,4)
        planet_name = generate_name_planet()
        planet_id = generate_obj_id()
        solar_system.update({f"planet{i + 1}": {
            "id": planet_id,
            "name": planet_name,
            "solar_system_id": solar_system["id"],
            "art": generate_planet_art()
        }})
        if settlements != 0:
            for _ in range(0, settlements):
                settlementObjects.update({
                    f"settlement{settlement_counter}":
                    make_settlement(planet_id, solar_system["id"])
                    })
                settlement_counter += 1
    solar_system.update({"settlements": settlementObjects})

    # for generating space stations
    station_quantity = 0
    space_station_count = 1
    while station_quantity != solar_system["space_stations"]:
        counter = 1
        spaceStationObjects.update({
            f"space_stations{space_station_count}": make_space_station(solar_system["id"])
        })
        station_quantity += 1
        space_station_count += 1
    solar_system.update({
        "stations": spaceStationObjects
    })

    count = 1
    difficulty_level = 1
    while f"solar_system{count}" in the_great_galaxy:
        count += 1
        difficulty_level += 1
    solar_system.update({"difficulty_level": difficulty_level})
    the_great_galaxy[f"solar_system{count}"] = solar_system

    json_str = json.dumps(the_great_galaxy, indent=4)
    with open("map.json", "w") as file:
        file.write(json_str)
        print("Map has been made successfully!")

def generate_obj_id():
    """ Function for giving out Ids """
    obj_uuid = uuid.uuid4()
    return str(obj_uuid)