# File Handling and Exception Handling Assignment

def modify_content(text):
    """
    Simple modifier function:
    Converts text to uppercase.
    (You can customize this later if you want.)
    """
    return text.upper()

# Ask user for filename
filename = input("Enter the name of the file to read: ")

try:
    # Try to open and read the file
    with open(filename, "r") as file:
        content = file.read()

    # Modify content
    modified_content = modify_content(content)

    # Write to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"File processed successfully! Modified content saved in '{new_filename}'.")

except FileNotFoundError:
    print("Error: The file you entered does not exist. Please try again.")
except PermissionError:
    print("Error: Permission denied. You cannot access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
