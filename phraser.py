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

    # First version way of executing. Changes so instructions are generated and executed at same time
    # # Make instructions individual
    # individual_intructions = generate_indiviudal_instructions(list_instructions)

    return list_instructions


if __name__ == '__main__':
    print("This section is running")
    x = generate_instructions("input_assign3.txt")
    print(x)
