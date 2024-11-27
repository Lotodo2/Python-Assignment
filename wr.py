import os

def write_happy_hour():
    try:
        # Ask the user for the name of the file to read
        input_file = input("Enter the name of the file to read (or create): ")

        # Check if the file exists; if not, create it with default content
        if not os.path.exists(input_file):
            print(f"File '{input_file}' does not exist. Creating it...")
            with open(input_file, 'w') as file:
                file.write("This is the default content.\n")

        # Read the content of the file
        with open(input_file, 'r') as file:
            content = file.read()
            print(f"Original content of '{input_file}':")
            print(content)

        # Write the phrase "HAPPY HOUR" to a new file
        output_file = input("Enter the name of the file to write 'HAPPY HOUR' to: ")
        with open(output_file, 'w') as file:
            file.write("HAPPY HOUR\n")

        print(f"'HAPPY HOUR' has been written to '{output_file}'.")

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except PermissionError:
        print("Error: You don't have permission to access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
write_happy_hour()
