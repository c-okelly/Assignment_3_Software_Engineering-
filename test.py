# Author = Conor O'Kelly
import nose2

import grid_creator_manager
from phraser import *

"""
This file will contain all of the test. The goal will be to carry out a test on each of the functions.

"""

def test_create_grid():
    # Test create grid
    assert grid_creator_manager.create_grid(2,2) == [[0,0],[0,0]]

def test_occupy_seat(): # Test occupy seat

    # Create Grid
    grid = grid_creator_manager.create_grid(2,2)


    grid_creator_manager.occupy_seat(grid,1,1) # Occupy seat
    assert grid == [[0,0],[0,1]] # Test seat it occupied

def test_empty_seat(): # Test empty seat

    grid = grid_creator_manager.create_grid(2,2) # Created Grid

    grid_creator_manager.occupy_seat(grid,1,1) # occupy seat first

    grid_creator_manager.empty_seat(grid,1,1) # Empty seat

    assert grid == [[0,0],[0,0]] # Test assertion


def test_toggle_seat():
    # Test toggle seat

    grid = grid_creator_manager.create_grid(2,2) # Created Grid

    grid_creator_manager.occupy_seat(grid,1,1) # Occupy one seat first

    # Toggle two seats
    grid_creator_manager.toggle_seat(grid,0,0)  # Toggle empty seat
    grid_creator_manager.toggle_seat(grid,1,1)  # Toggle full seat

    assert grid == [[1,0],[0,0]]

def test_instruction_manager():
    # Test Instruction manager

    assert 0 == 0

    # Test generate individual instructions

    # Test count filled seats

    # Test generate instructions from file


if __name__ == '__main__':
    nose2.main()

