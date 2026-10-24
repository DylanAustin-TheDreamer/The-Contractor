import json
from map import make_map

the_great_galaxy = {}
solar_system = {}
positionX = 0
positionY = 0

# Load the map first
try:
    with open("map.json", "r") as file:
        galaxy = json.load(file)
        the_great_galaxy = galaxy
except:
    galaxy = the_great_galaxy

board = [[0 for _ in range(9)] for _ in range(9)]

for key, value in the_great_galaxy.items():
    if (
        isinstance(value, dict)
        and value.get("positionX") is not None
        and value.get("positionY") is not None
    ):
        board[value["positionY"]][value["positionX"]] = 1

game_start = True
while game_start:
    try:
        print("---------------------------------")
        print("Welcome to the Solar System Generator!")
        print(board[0])
        print(board[1])
        print(board[2])
        print(board[3])
        print(board[4])
        print(board[5])
        print(board[6])
        print(board[7])
        print(board[8])
        positionX = int(input("Enter the X coordinate (0-8): "))
        positionY = int(input("Enter the Y coordinate (0-8): "))
        if 0 <= positionX < 9 and 0 <= positionY < 9:
            if board[positionY][positionX] == 0:
                board[positionY][positionX] = 1
                make_map(solar_system, the_great_galaxy, positionX, positionY)
                print(f"Solar system generated at coordinates ({positionX}, {positionY}).")
            else:
                print("A solar system already exists at these coordinates.")
                with open("map.json", "r") as file:
                        galaxy = json.load(file)

                for key, value in galaxy.items():
                    if value["positionX"] == positionX and value["positionY"] == positionY:
                        print(f"Solar system at ({positionX}, {positionY}): {value['system_name']}")
                        print(f"Planets: {value['planets']}")
                        print(f"Asteroids: {value['Astroids']}")
                        print(f"Factions: {value['Factions']}")
                        print(f"Cargo Ships: {value['Cargo_Ships']}")
        else:
            print("Coordinates must be between 0 and 99. Please try again.")
    except ValueError:
        print("Invalid input. Please enter integer values for coordinates.")