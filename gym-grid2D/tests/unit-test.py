import time
import pygame
import unittest
import gym_maze.envs.maze_view_2d as m2d

# Test the musicfiles class
class TestGridUtilities(unittest.TestCase):
    def setUp(self):
        self.init_pos = (4, 3)
        self.maze = m2d.MazeView2D(screen_size=(500, 500), maze_size=(6, 7), 
                          res_path='/media/i/home/arnold/development/python/machine_learning/gym/gym-maze', 
                          n_mushrooms=0, n_cactuses=0, n_rocks=0,
                          init_pos=self.init_pos)
    
        self.maze.update()
        
        return
    
    def teardown(self):
        pygame.quit()
        
        return
    
    def test_insert_thing(self):
        # Test vwhether insert_thing inserts a thing at the expected location
        pos = (2, 2)
        thing = self.maze.maze.insert_thing(m2d.Mushroom, pos)
        loc = thing.location
        exp_loc = pos
        self.assertEqual(loc, exp_loc, 'Incorrect location')
        
        # Test whether thing_by_id contains the inserted vehicle
        thing_id = thing.id
        inserted_thing = self.maze.maze.things_by_id[thing_id]
        self.assertEqual(thing, inserted_thing, 'Incorrect references: thing and inserted_thing')
        
        # Test whether thing is inserted in maze
        thing_type = thing.category
        idx = self.maze.maze.maze_cells[loc]
        self.assertEqual(idx, thing_type, 'thing_if not correctly inserted in maze_cells')
        
        return
    
    def test_find_by_loc(self):
        # Test the find_thing_by_loc function
        pos = (2, 2)
        thing = self.maze.maze.insert_thing(m2d.Mushroom, pos)
        loc = thing.location
        found_thing = self.maze.maze.find_thing_by_loc(loc)
        self.assertEqual(thing, found_thing, 'Incorrect location')
        
        return
        
    def test_move_over_field(self):
        #cols, rows = self.maze.maze.maze_size
        #print(self.maze.maze.print_maze())

        direction = "W"
        robot = self.maze.robot
        start_energy = robot.energy
        self.maze.robot.move(self.maze.maze, direction)
        exp_loc = (self.init_pos[0] + m2d.COMPASS[direction][0], self.init_pos[1] + m2d.COMPASS[direction][1])
        loc = robot.location
        cost, _ = robot.cost(self.maze.maze, direction)
        thing_energy = m2d.COST['Field']
        exp_energy = start_energy + thing_energy
        energy = robot.energy
        
        self.assertEqual(loc, exp_loc, 'Incorrect location')
        self.assertEqual(energy, exp_energy, 'Incorrect energy')
        
        return

    def test_move_against_wall(self):
        direction = "E"
        robot = self.maze.robot
        start_energy = robot.energy
        self.maze.robot.move(self.maze.maze, direction)
        exp_loc = self.init_pos
        loc = robot.location
        cost, _ = robot.cost(self.maze.maze, direction)
        thing_energy = m2d.COST['Wall']
        exp_energy = start_energy + thing_energy
        energy = robot.energy
        
        self.assertEqual(loc, exp_loc, 'Incorrect location')
        self.assertEqual(energy, exp_energy, 'Incorrect energy')
        
        return

    def test_move_over_mushroom(self):
        direction = "W"
        thing = self.maze.maze.insert_thing(m2d.Mushroom, (3, 3))
        
        robot = self.maze.robot
        start_energy = robot.energy
        self.maze.robot.move(self.maze.maze, direction)
        exp_loc = self.init_pos
        loc = robot.location
        thing_energy = thing.energy
        exp_energy = start_energy + thing_energy
        energy = robot.energy
        
        self.assertEqual(loc, exp_loc, 'Incorrect location')
        self.assertEqual(energy, exp_energy, 'Incorrect energy')
        
        return
    
    def test_move_over_cactus(self):
        direction = "W"
        thing = self.maze.maze.insert_thing(m2d.Cactus, (3, 3))

        robot = self.maze.robot
        start_energy = robot.energy
        self.maze.robot.move(self.maze.maze, direction)
        exp_loc = self.init_pos
        loc = robot.location
        thing_energy = thing.energy
        exp_energy = start_energy + thing_energy
        energy = robot.energy
        
        #print(loc, exp_loc)
        #print(energy, exp_energy, thing_energy)
        self.assertEqual(loc, exp_loc, 'Incorrect location')
        self.assertEqual(energy, exp_energy, 'Incorrect energy')
        
        return

    def test_move_rock(self):
        direction = "W"
        thing1 = self.maze.maze.insert_thing(m2d.Rock, (3, 3))
        thing2 = self.maze.maze.insert_thing(m2d.Rock, (2, 3))
        thing3 = self.maze.maze.insert_thing(m2d.Rock, (1, 3))

        robot = self.maze.robot
        start_energy = robot.energy
        self.maze.robot.move(self.maze.maze, direction)
        exp_loc = self.init_pos#(self.init_pos[0] + m2d.COMPASS[direction][0], self.init_pos[1] + m2d.COMPASS[direction][1])
        loc = robot.location
        thing_energy = thing1.energy + thing2.energy + thing3.energy
        exp_energy = start_energy + thing_energy
        energy = robot.energy
        
        #print(loc, exp_loc)
        #print(energy, exp_energy, thing_energy)
        self.assertEqual(loc, exp_loc, 'Incorrect location')
        self.assertEqual(energy, exp_energy, 'Incorrect energy')
        
        return
    
if __name__ == '__main__':
    unittest.main()
