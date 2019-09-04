# DungeonCrawler
A simple dungeon game I made to practice Python 3 syntax since learning through tutorials is kinda boring.

Game is played on a board of 9x9 squares. Top left corner is labled as square 11, top right as 19, bottom left as 91, bottom right as 99.

Players start at square 11, and the goal is to defeat the monster in square 99 to exit the dungeon and win the game.

Each time you enter a room, there will be a monster (except for the starting room 11). Winning against the monster earns you the randomly generated loot in that room. 

Alternatively, the player can choose to not fight and simply leave the room via a door. Not fighting means you do not earn the loot in that room. But you can always come back later to fight the monster and earn the loot in that room (loot and monster stats stay constant in each iteration of the game, and only changes after the game is closed and restarted).

Losing a fight loses 1 health. 3 health total upon game start. 0 health = death = game over.

Doors are present in all rooms, and each room has a door that leads to each adjacent room (diagonally adjacent does not count).

Currently attack and defense are not really implemented and are simply added together into a holistic "power score". Future iterations might see a proper combat system where attack and defense balance is more important, and monsters will be updated to fit the same system.

Literally no one is gonna read this so I am not gonna bother writing more lmao.
