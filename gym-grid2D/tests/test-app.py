#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:03:29 2019

@author: arnold
"""
import numpy as np
import random

class Test():
    def __init__(self):
        self.MAZE_H = 10
        self.MAZE_W = 5
        self.maze_size = (self.MAZE_W, self.MAZE_H)
        self.STATUS = {'Wall': 1}
        
        self.maze_cells = np.zeros(self.maze_size, dtype=int)
        for x in range(self.maze_size[0]):
            self.maze_cells[x, 0] = self.STATUS["Wall"]
            self.maze_cells[x, self.MAZE_H-1] = self.STATUS["Wall"]
        for y in range(self.maze_size[1]):
            self.maze_cells[0, y] = self.STATUS["Wall"]
            self.maze_cells[self.MAZE_W-1, y] = self.STATUS["Wall"]

        cell_ids = [(x, y) for y in range(self.MAZE_H) for x in range(self.MAZE_W) if self.maze_cells[x, y] == 0]
        self.print_maze()
        
        print(cell_ids)
        
        mushroom_cell_ids = random.sample(cell_ids, 100)
        print(mushroom_cell_ids)
        

    def print_maze(self):
        cols, rows = (self.MAZE_W, self.MAZE_H)
        print(rows, cols)
        for row in range(rows):
            for col in range(cols):
                print(self.maze_cells[col, row], end=' ')
                
            print()
                
        return
    
if __name__ == "__main__":
    test = Test()