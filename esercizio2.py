import os

# Define the directory path to count files in
directory_path = '/path/to/directory'

# Initialize a dictionary to store counts for each interpreter
interpreter_counts = {}

# Iterate over each file in the directory
for filename in os.listdir(directory_path):
    # Check if the file is a script file (ends with .sh, .py, or .pl)
    if filename.endswith(('.sh', '.py', '.pl')):
        # Open the file and read the first line (the shebang line)
        with open(os.path.join(directory_path, filename), 'r') as file:
            first_line = file.readline().strip()
        # Extract the interpreter from the shebang line
        interpreter = first_line.split(' ')[0][2:]
        # Increment the count for this interpreter in the dictionary
        if interpreter in interpreter_counts:
            interpreter_counts[interpreter] += 1
        else:
            interpreter_counts[interpreter] = 1

# Print the final counts for each interpreter
for interpreter, count in interpreter_counts.items():
    print(f"{interpreter}: {count}")
