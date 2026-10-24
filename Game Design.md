# The Contractor - Game Design Concepts

## Core Gameplay

---

## Procedural Generation

Procrdural Generation in game design or computer concept alone, is not possible without boundries - according to my tutor Richard, procedural generation takes the form of what he called more 'pseudo procedural generation'. The example that he used for describing this pseudo generation is style, was minecraft and how minecraft worlds are built. It starts with the design of a huge box that contains the game world, and the envrionmental generation takes places within those boundaries. The possibilities for formations is not unlimited, and the formations that are possible in minecraft are down to 'seeds'. Although my knowledge of seeds is hardly vague nevermind knowledgeable, I understand that the seed is the data stored for a possible procedurally generated formation. There is a limited number of seeds.

Now, in my game 'The Contractor', I have conceived a suitable stylistic approach to pseudo procedural generation. I have decided that in my galaxy, the only real substantial area that can be given a name and concept - is a solar system. The solar system is not just a star, but the planets close enough to orbit that star. Therefore, in an empty galaxy, I could say the next tangible concept within the galaxy, is a solar system and its subjects. 

Therefore, I have decided that my only boundry here is memory, and the ability to store a solar system object to file or data structure within memory bounds. This way, solar system objects can be randomly generated instantly when needed. Within the solar system object, are planets and settlements associated with those planets. Within the solar system object we also store an amount of astroids it may have, travelling marchents mouching about, and how many space stations if any. Within those properties of the solar system, resides their own properties such as their explorable gridmap of areas within settlements and space stations, unique id's, and anything else I can think of that could be a subject of a solar system (maybe something to do with the center star and even moons and the planets they are associated with)

## How to render the map

This section is about how to render my map information (solar system objects) within a game engine using graphics and world space to interpret locations. Here I will state some concepts and themes that may be good to explore.

### The 4 state system

For the 4 state system / algorithm to work in my game, I need to code this on the game engine side as a form of game mechanic. There will be many game design mechanics coded on the engine side as opposed to the code that handles procedural generation of map, saving to, and reading from map file. 

The idea with the 4 state system, is that the most zoomed out aspect of the game possible, is the map of all accessible solar systems. This can be considered a 'state' of game. This state of game is the simplest concept to begin with, where each solar system generated has co-ordinates for the x and y axis of a two dimentional grid data-structure, read from file, then to have a 2D grid read those co-ordinates and state at which co-ordinate of this 2D grid has a solar system. In the game engine, we can display graphics in a form of grid map that reads from that 2D grid that shows us solar systems discovered and their properties.

The second state of game, is the level after the solar map state. This will literally be the area within the solar system. The solar system itself has lots of initial properties that needs to representated in graphics within the game engine. On a 2D plane, we can display how many planets there are in the solar system, their graphics properties, and sufficient distance between those physically perceivable objects. Within this state, we also have access to loose properties such as the amount of astroids we can spawn in from a pool of astroids, cargo merchants and so on. There may also be space stations that need to be positioned on the 2D plane, and represented with graphics.

The third state of game is activated when having gone close enough to a planet to enter it. There, we pass the information of that planet alongside activating this state, and represent the graphics of its properties such as the settlements on the planet, and their locations in order to travel towards them. The third state literally represents the planet environment.

The fourth state of game, is when you have entered a settlement or interior with a map such as a spacestation. Same principle - we activate state and pass relevent information about the properties that need to be rendered by graphics, located, and spaced accordingly.

This is the first game design mechanic regarding world building - switching between each state depending on player actions and ability, in order to change those game states. This way, we don't have to position the player, or have the player travel to co-ordinates. Thus, the locations can always be reset to (x = 0, y = 0, z = 0), and the graphics and relevent data around the player is what changes.

---