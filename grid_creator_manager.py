# Author = Conor O'Kelly

import numpy

def create_grid(x,y):

    gird = numpy.zeros((x,y))

    return gird

# For locationg the correct set we swap the x and y order to better correlate with the graphicl illustration

# find the correct set and occupy it
def occupy_seat(x,y):
    grid[y][x] = 1

# Find correct seat and set to empty
def empty_seat(x,y):

    grid[y][x] = 0

def toggle_seat(x,y):

    #Find current status of seat
    seat = grid[y][x]

    # Set sat to opposite
    if seat == 1:
        empty_seat(x,y)
    elif seat == 0:
        occupy_seat(x,y)


def generate_coordiantes():

    return

# Will take the crated grid and instruction set and apply instruction set to grid
def intruction_manager(grid, instructioino_set):

    return

if __name__ == '__main__':
    grid = create_grid(5,5)
    print(grid)
    toggle_seat(0,1)
    toggle_seat(0,1)
    print("hello")


    print(grid[::-1])
