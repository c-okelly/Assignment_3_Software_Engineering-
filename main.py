# Author = Conor O'Kelly

from phraser import generate_instructions
from grid_creator_manager import create_grid, generate_indiviudal_instructions_and_run, count_filled_seats
import time

# Main will run all the functions as required


def main():

    curent_time = time.time()

    #Take input file and return instruction list
    instructions = generate_instructions("input_assign3.txt")
    print(len(instructions))

    # Generate grid
    grid = create_grid(1000,1000)

    # perform operations on grid using instruction list
    print("Starting instructions")

    generate_indiviudal_instructions_and_run(grid,instructions)

    # Count number of filled seats
    filled_seats = count_filled_seats(grid)
    print(filled_seats)

    # Print out run time
    finish_time = time.time()
    print("Run time was ",finish_time-curent_time)

    return grid


if __name__ == '__main__':

    main()

