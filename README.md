# gym-grid2D

A simple 2D grid environment where a vehicle finds its way. The vehicle has a certain amount of energy that decreases each turn. Mushrooms boost the energy while cactuses decrese it. The vehicle can push rocks around, over mushrooms and cactuses and in the process destroying them.
The objective is to keep in life for as many turns as possible. 

### Action space
The agent may only choose to go up, down, left, or right ("N", "S", "W", "E"). If the way is blocked, it will remain at the same the location. 

### Observation space
The observation space is the (x, y) coordinate of the agent. The top left cell is (0, 0).

### Reward
A reward of 1 turn is awarded when the agent is still alive at the end of the turn.

### End condition
The number of turns when the vehicle dies. 

## Grid Versions

### Pre-generated mazes
* 3 cells x 3 cells: _GridEnvSample3x3_
* 5 cells x 5 cells: _GridEnvSample5x5_
* 10 cells x 10 cells: _GridEnvSample10x10_
* 100 cells x 100 cells: _GridEnvSample100x100_

### Randomly generated grids (same grid every epoch)
* 3 cells x 3 cells: _GridEnvRandom3x3_
* 5 cells x 5 cells: _GridEnvRandom5x5_
* 10 cells x 10 cells: _GridEnvRandom10x10_
* 100 cells x 100 cells: _GridEnvRandom100x100_

### Randomly generated grids with portals and loops
With loops, it means that there will be more than one possible path.
The agent can also teleport from a portal to another portal of the same colour. 
* 10 cells x 10 cells: _GridEnvRandom10x10Plus_
* 20 cells x 20 cells: _GridEnvRandom20x20Plus_
* 30 cells x 30 cells: _GridEnvRandom30x30Plus_

## Installation
The current version (0.1) is work in progress. At the moment only grid_view_2d 
works, the rest has not been tested, not even the tests. Use and install at 
your own risk.
It should work on Python 3.6+, maybe even lower versions. 
It requires pygame and numpy. 

```bash
cd gym-grid2D
python setup.py install
```
