# Author = Conor O'Kelly

"""
This small python script will take in all the input from the user file and store it.
It will then convert the instruction set into individual instructions

"""

# Take in file, read line, clean line and instruction list

def generate_instructions(file_name):

    file = open(file_name, "r", encoding="utf-8")

    # Instruction list in raw format
    list_instructions = []

    for line in file:
        #Remove the new line formatting
        new_line = line.replace("\n","")

        # Split line on space
        no_space_line = new_line.split(" ")

        # Split cordinates on comma
        start = no_space_line[1].split(",")
        finish = no_space_line[3].split(",")

         # New line is everything in list bar "through"
        cleaned_line = [no_space_line[0],start[0],start[1],finish[0],finish[1]]

        # Add new line to list
        list_instructions.append(cleaned_line)


    return list_instructions

# Take instruction list of ranges and break it down into idiviudal instruction and return list
# This will generate a list of indiviudal instruction for each coordiante

def generate_coordiantes(instruction_set):

    master_instructions = []

    for instruction in instruction_set:

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
                print(specific_instruc)
                master_instructions.append(specific_instruc)

        # Two for loops to generate instruction for range of coordiantes

    return



if __name__ == '__main__':
    print("This section is running")
    x = generate_instructions("input_assign3.txt")
    print(x)