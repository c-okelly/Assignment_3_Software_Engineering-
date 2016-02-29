# Author = Conor O'Kelly
import nose2

import grid_creator_manager
import phraser

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


def test_generate_individual_instructions():
    # Test generate individual instructions

    grid = grid_creator_manager.create_grid(4,2) # Create grid

    # Set instructions one of each type
    instructions_set = [["occupy","0","0","3","1"],["empty","0","0","3","0"],["toggle","2","0","3","1"]]

    grid = grid_creator_manager.generate_indiviudal_instructions_and_run(grid,instructions_set) # Run instructions

    assert grid == [[0, 0, 1, 1], [1, 1, 0, 0]]


def test_count_filled_seats():
    # Test count filled seats

    grid = [[0, 0, 1, 1], [1, 1, 0, 0]] # Set grid

    result = grid_creator_manager.count_filled_seats(grid)

    assert result == 4


def test_generate_instructions_from_file():
    # Test generate instructions from file

    input_text = "input_assign3.txt"

    output = phraser.generate_instructions(input_text)
    first_three_items = output[:3]

    assert first_three_items == [['empty', '660', '55', '986', '197'], ['empty', '341', '304', '638', '850'], ['empty', '199', '133', '461', '193']]

if __name__ == '__main__':
    nose2.main()


