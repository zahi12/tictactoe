# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:28:10 2019

@author: pierr
"""

class Game ():
    def __init__(self):
        pass
    
    def start(self):
        self.board = Board()
    
    def get_board(self):
        return self.board
        
        
class Board():
    def __init__(self):
        self.grids = []
        for i in range(9):
            self.grids.append(Grid())
            
    def get_grid(self, x, y):
        return self.grids[]
            
class Grid()
