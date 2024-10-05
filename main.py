import os
import glob

"""
A code by Bee Kurt
https://github.com/beekurt98/ordered-file-namer
"""

exit_program = False

while not exit_program:

    path = input(r"Please enter the directory/path of the folder:" + "\n")  # Gets the file path
    name = input("Desired name after EVERY number. Can be left empty:\n")  # Gets the name
    file_ext = input("File extension to search & change the name of. For example, png, jpeg, txt, pdf, etc.:\n")  # The file extensions
    starting_number = int(input("From which number the naming should start? For example, 1, 5, 8. "
                                "(Good for naming multiple file extension types)\n"))-1

    if name != " " or name != "":  # Checks if the name is empty. If not, adds a space before the name.
        name = " " + name

    files = glob.glob(f"{path}\\*.{file_ext}")
    files.sort(key=os.path.getmtime)  # Sorts the files by date

    if len(files) == 0:  # Checks if there are any files with the file extension the user gave
        print(f"There aren't any files with '.{file_ext}' extension.")
    else:
        for i in range(len(files)):
            file = files[i]
            os.rename(file, f'{path}\\{i+starting_number + 1}{name}.{file_ext}')
        print("Filename change successful.")
    cont = input("Continue? Y/n\n")
    if cont == "Y" or cont == "y":
        pass
    else:
        print("Exiting the program...")
        exit_program = True
