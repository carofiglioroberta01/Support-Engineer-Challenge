import os


def replace_string_in_files(search_string, replace_string, directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                filedata = f.read()

            # Replace the search string with the replace string in the file data
            new_filedata = filedata.replace(search_string, replace_string)

            with open(filepath, 'w') as f:
                f.write(new_filedata)


if __name__ == '__main__':
    search_string = input("Enter the string to search: ")
    replace_string = input("Enter the string to replace with: ")
    directory = input("Enter the directory name: ")
    replace_string_in_files(search_string, replace_string, directory)