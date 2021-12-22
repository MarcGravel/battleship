# Battleship

Command line 2 player battleship game.

Each player chooses the location of their battleship. The first
option is to choose the direction of the ship (horizontal or vertical).
Then the next options are to choose the center marker for the ship on the game board.

The ship is three spaces long, so if the center marker is placed on an edge and the ships direction is 
overflowing, you will receive and error and have to place the ship again.

Once both ships are placed, players take turns to fire a shot at the other. A shot consists of attacking
one space on the board. Each shot will be noted with a "Hit", "Miss", or "You already Hit here".

Once a player has all three positions hit on the opponents ship, they win and the game ends. 

### To use

Clone this repository is onto local system

Run:
```bash
python app.py
```

