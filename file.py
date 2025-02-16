def modify_content(content):
    return content.upper()

def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        modified_content = modify_content(content)
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print(f"Error: An error occurred while reading or writing the file.")

# Example usage
input_filename = 'web.txt'
output_filename = 'web_out.txt'
read_and_write_file(input_filename, output_filename)
