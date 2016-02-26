# Author = Conor O'Kelly

# This small python script will take in all the input from the user and store it.
# This will encompas a number of functions that will act toghther. Each should provide comments.


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

        # New line is everything in list bar "through"
        cleaned_line = [no_space_line[0],no_space_line[1],no_space_line[3]]
        # print(cleaned_line)


        # Add new line to list
        list_instructions.append(cleaned_line)


    return list_instructions

if __name__ == '__main__':
    print("This section is running")
    x = generate_instructions("input_assign3.txt")
    print(x)