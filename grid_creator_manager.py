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

# This will generate a list of indiviudal instruction for each coordiante
def generate_coordiantes(instruction):

    instruc_type = instruction[0]
    start_x = int(instruction[1])
    start_y = int(instruction[2])
    finish_x = int(instruction[3])
    finish_y = int(instruction[4])

    finished_instruction_list = []

    for x in range(start_x,(finish_x+1)):
        print(x)

    # Two for loops to generate instruction for range of coordiantes

    return

# Will take the crated grid and instruction set and apply instruction set to grid
def intruction_manager(grid, instructioino_set):

    return


# Count number of filled seats in the gird

if __name__ == '__main__':
    grid = create_grid(5,5)
    print(grid)
    toggle_seat(0,1)
    toggle_seat(0,1)
    print("hello")

    # Print out grid bottom up so it make sense like a graph would
    print(grid[::-1])


    generate_coordiantes(['empty', '660', '55', '665', '197'])

