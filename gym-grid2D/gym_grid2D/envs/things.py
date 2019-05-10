#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 07:58:39 2019

@author: arnold
"""

class Thing():
    Seq = 0
    
    def __init__(self, location=(1, 1)):
        Thing.Seq += 1

        self.id = Thing.Seq
        self.location = location
        self.type = 'Field'
        self.category = STATUS[self.type]
        self.energy = 0
        self.deleted = False
        self.color = (255, 0, 0)
        
        return
    
    def cost(self, maze, direction):
        ''' Computes the cost of a move in a certain direction
        
        A rock may move when it is pushed by a vehicle, depending on the 
        field lying before it. There is always a cost involved, even when 
        the rock cannot move. When a rock is pushed against a wall but the
        cost that is transmitted to the vehicle is the energy of the rock
        plus the nerge of the wall. For a cactus the same type of cost 
        is computed, but the rock will move over the cactus and the cactus
        will disappear. Thus this is a save way to get rid of cactuses.
        
        Cost is always negative.

        Args:
            maze (np.arry): maze on which to perform the move
            direction (char): direction in which to move
            
        Returns:
            The cost of the move when it should be effected (float)
        '''
        potential_pos = (self.location[0] + COMPASS[direction][0], self.location[1] + COMPASS[direction][1])
        idx = maze.maze_cells[potential_pos]
        cost = 0
        may_move = False
        
        if idx == STATUS['Field']:
            cost = COST['Field']
            may_move = True
        elif idx == STATUS['Wall']:
            cost = COST['Wall']
            may_move = False
        elif idx == STATUS['Vehicle']:
            thing = maze.find_thing_by_loc(potential_pos)
            cost = thing.energy
            may_move = False
        elif idx == STATUS['Mushroom'] :
            thing = maze.find_thing_by_loc(potential_pos)
            cost = thing.energy
            may_move = False
        elif idx == STATUS['Cactus']:
            thing = maze.find_thing_by_loc(potential_pos)
            cost = thing.energy
            may_move = False
        elif idx == STATUS['Rock']:
            thing = maze.find_thing_by_loc(potential_pos)
            cost, may_move = thing.cost(maze, direction)
            cost = -abs(cost) + thing.energy
        else:
            raise ValueError('*** Unknown field code in Rock.move:', idx)
            
        return cost, may_move
    
    def move(self, maze, direction=None):
        return
    
## Class: Thing ##

class Vehicle(Thing):
    def __init__(self, location=(1, 1)):
        super().__init__(location)
        
        self.type = 'Vehicle'
        self.category = INFO[self.type][0]
        self.energy = INFO[self.type][1]
        self.color = INFO[self.type][2]
        
        return
    
    def move(self, maze, direction=None):
        if direction is None:
            direction = random.sample(['N', 'E', 'S', 'W'], 1)[0]
            
        potential_loc = (self.location[0] + COMPASS[direction][0], self.location[1] + COMPASS[direction][1])
        idx = maze.maze_cells[potential_loc]
        cost, may_move = self.cost(maze, direction)
        
        # Vehicle may move over the field
        if idx == STATUS['Field']:
            new_loc = potential_loc
            
        # Vehicle may not move thru a wall
        elif idx == STATUS['Wall']:
            new_loc = self.location
            
        # Rock cannot be pushed thru a Vehicle
        elif idx == STATUS['Vehicle']:
            thing = maze.find_thing_by_loc(potential_loc)
            new_loc = self.location
            
        # Cannot move over a mushroom which is lost
        elif idx == STATUS['Mushroom'] :
            thing = maze.find_thing_by_loc(potential_loc)
            thing.deleted = True
            new_loc = self.location
            print('Vehicle energy from Mushroom:', cost)
            
        # Cannot be moved over a cactus which remainslost
        elif idx == STATUS['Cactus']:
            thing = maze.find_thing_by_loc(potential_loc)
            new_loc = self.location
            print('Vehicle cost from Cactus:', cost)
            
        # Rock can move, depending on the object before it
        elif idx == STATUS['Rock']:
            new_loc = self.location
            if may_move:
                thing = maze.find_thing_by_loc(potential_loc)
                thing.move(maze, direction)
                new_loc = potential_loc

            print('Vehicle cost from Rock:', cost)

        else:
            raise ValueError('*** Unknown field code in Rock.move:', idx)
                
        # if
    
        self.energy += cost
        maze.maze_cells[self.location] = STATUS['Field']
        self.location = new_loc
        maze.maze_cells[self.location] = STATUS['Vehicle']
        
        return cost, self.location
            
## Class: Vehicle ##

class Mushroom(Thing):
    def __init__(self, location):
        super().__init__(location)

        self.type = 'Mushroom'
        self.category = INFO[self.type][0]
        self.energy = INFO[self.type][1]
        self.color = INFO[self.type][2]
        
        return

## Class: Mushroom ##

class Cactus(Thing):
    def __init__(self, location):
        super().__init__(location)

        self.type = 'Cactus'
        self.category = INFO[self.type][0]
        self.energy = INFO[self.type][1]
        self.color = INFO[self.type][2]
        
        return

## Class: Mushroom ##

class Rock(Thing):
    def __init__(self, location):
        super().__init__(location)

        self.type = 'Rock'
        self.category = INFO[self.type][0]
        self.energy = INFO[self.type][1]
        self.color = INFO[self.type][2]
        
        return

    def move(self, maze, direction=None):
        # When direction is None this function is called to move itself, 
        # not from vehicle move (pushing the rock). In that case it returns
        # immediately as it does not spontaneously move
        if direction is None:
            return
            
        # Compute a move based on the push of a vehicle
        potential_loc = (self.location[0] + COMPASS[direction][0], self.location[1] + COMPASS[direction][1])
        idx = maze.maze_cells[potential_loc]
        cost, new_loc = self.cost(maze, direction)
        thing = None
        
        # Rock may move of the field
        if idx == STATUS['Field']:
            new_loc = potential_loc
            
        # Rock may not move thru a wall
        elif idx == STATUS['Wall']:
            new_loc = self.location
            
        # Rock cannot be pushed thru a wall
        elif idx == STATUS['Vehicle']:
            thing = maze.find_thing_by_loc(potential_loc)
            new_loc = self.location
            
        # Can be pushed over a mushroom which is lost
        elif idx == STATUS['Mushroom']:
            thing = maze.find_thing_by_loc(potential_loc)
            thing.deleted = True
            new_loc = potential_loc
            
        # Can be pushed over a cactus which is lost
        elif idx == STATUS['Cactus']:
            thing = maze.find_thing_by_loc(potential_loc)
            thing.deleted = True
            new_loc = potential_loc
            
        # Rock can move, depending on the object before it
        elif idx == STATUS['Rock']:
            thing = maze.find_thing_by_loc(potential_loc)
            thing.move(maze, direction)
            new_loc = potential_loc
        else:
            raise ValueError('*** Unknown field code in Rock.move:', idx)
            
        # if
        if not thing is None:
            print('Rock added cost from', thing.type, 'cost =', cost)
    
        maze.maze_cells[self.location] = STATUS['Field']
        self.location = new_loc
        maze.maze_cells[self.location] = STATUS['Rock']
            
        return cost, self.location
            
## Class: Rock ##
    