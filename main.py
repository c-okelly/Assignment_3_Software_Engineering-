# Author = Conor O'Kelly

from phraser import generate_instructions
from grid_creator_manager import create_grid, intruction_manager, count_filled_seats

# Main will run all the functions as required


def main():

    #Take input file and return instruction list
    instructions = generate_instructions("input_assign3.txt")
    print(len(instructions))

    # Generate grid
    grid = create_grid(1000,1000)

    # perform operations on grid using instruction list
    print("Starting instructions")
    intruction_manager(grid,instructions)

    # Count number of filled seats
    filled_seats = count_filled_seats(grid)
    print(filled_seats)

    return


if __name__ == '__main__':

    main()

