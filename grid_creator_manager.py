# Author = Conor O'Kelly

import numpy

def create_grid(x,y):

    gird = numpy.zeros((x,y))

    return gird

# For locationg the correct set we swap the x and y order to better correlate with the graphicl illustration

# find the correct set and occupy it
def occupy_seat(grid,x,y):
    grid[y][x] = 1

# Find correct seat and set to empty
def empty_seat(grid,x,y):

    grid[y][x] = 0

def toggle_seat(grid,x,y):

    # Find current status of seat
    seat = grid[y][x]

    # Set sat to opposite
    if seat == 1:
        empty_seat(grid,x,y)
    elif seat == 0:
        occupy_seat(grid,x,y)


# Will take the crated grid and instruction set and apply instruction set to grid
def intruction_manager(grid, instruction_set):

    # Determine the type of instruction and carry out corresponding action
    for instruction in instruction_set:

        if instruction[0] == "empty":
            empty_seat(grid,instruction[1],instruction[2])

        elif instruction[0] == "occupy":
            occupy_seat(grid,instruction[1],instruction[2])

        elif instruction[0] == "toggle":
            toggle_seat(grid,instruction[1],instruction[2])

    return grid

# Function to count the number of occupied seat in the grid

def count_filled_seats(grid):

    # set filled seat to zero and thne count number of seat in each row from top down
    filled_seats = 0

    for row in grid:
        for seat in row:
            if seat == 1:
                filled_seats += 1

    return filled_seats


# Count number of filled seats in the gird

if __name__ == '__main__':
    grid_1 = create_grid(5,5)
    print(grid_1)
    instruction_set = [["occupy",1,1],["occupy",1,2],["occupy",1,0],["occupy",1,3],["empty",1,1]]
    print("gap")
    intruction_manager(grid_1,instruction_set)

    # Print out grid bottom up so it make sense like a graph would
    print(grid_1[::-1])

    print(count_filled_seats(grid_1))


