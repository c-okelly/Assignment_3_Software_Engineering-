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


# Will now also generate the instructions then execut them to reduce runtime

def intruction_manager(grid, instruction):

    # Determine the type of instruction and carry out corresponding action
    for instruction in instruction_set:

        if instruction[0] == "empty":
            empty_seat(grid,instruction[1],instruction[2])

        elif instruction[0] == "occupy":
            occupy_seat(grid,instruction[1],instruction[2])

        elif instruction[0] == "toggle":
            toggle_seat(grid,instruction[1],instruction[2])

    return grid

# Take instruction list of ranges and break it down into idiviudal instruction and return list
# This will generate a list of indiviudal instruction for each coordiante

def generate_indiviudal_instructions_and_run(grid,instruction_set):


    for instruction in instruction_set:
        # print(instruction)

        instruc_type = instruction[0]
        start_x = int(instruction[1])
        start_y = int(instruction[2])
        finish_x = int(instruction[3])
        finish_y = int(instruction[4])

        # For loops to iterate over x and y ranges
        for x in range(start_x,(finish_x+1)):
            for y in range(start_y,(finish_y+1)):

                # Create specific instruction and append to main list
                specific_instruc = [instruc_type, x, y]
                #print(specific_instruc)


                #Execute required instruction

                if specific_instruc[0] == "empty":
                    empty_seat(grid,specific_instruc[1],specific_instruc[2])

                elif specific_instruc[0] == "occupy":
                    occupy_seat(grid,specific_instruc[1],specific_instruc[2])

                elif specific_instruc[0] == "toggle":
                    toggle_seat(grid,specific_instruc[1],specific_instruc[2])


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


