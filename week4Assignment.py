# Function to modify the first line of a file and write the result to another file
def modify_first_line():
    try:
        # Open the input file in read mode and the output file in write mode
        with open("input.txt", "r", encoding="utf-8") as infile, open("output.txt", "w", encoding="utf-8") as outfile:
            # Read all lines from the input file
            lines = infile.readlines()
            
            # Modify the first line if the file is not empty
            if lines:
                lines[1] = "Kancane kancane xyz.\n"
            
            # Write the modified lines to the output file
            outfile.writelines(lines)
    except FileNotFoundError:
        # Handle the error if the input file does not exist
        print("The input file does not exist.")

# Function to read a file specified by the user
def read_file():
    while True:
        try:
            # Ask the user for a filename to read from
            filename = input("Enter the filename: ")
            
            # Attempt to open the file in read mode
            with open(filename, "r", encoding="utf-8") as file:
                # Read the file content
                content = file.read()
                print("File content successfully read.")
                print(content)  # Display the content to the user
                break  # Exit the loop after successfully reading the file
        except FileNotFoundError:
            # Handle the error if the file does not exist
            print("Error: File not found. Please try again.")
        except IOError:
            # Handle errors related to file permissions or other input/output issues
            print("Error: File cannot be read. Please check permissions.")

# Call the functions to execute the tasks
modify_first_line()
read_file()