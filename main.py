import os
import glob

"""
A code by Bee Kurt
https://github.com/beekurt98/ordered-file-namer
"""

path = input(r"Please enter the directory/path of the folder:" + "\n")  # Gets the file path
name = input("Desired name after EVERY number. Can be left empty:\n")  # Gets the name
file_ext = input("File extension to search & change the name of. For example, png, jpeg, txt, pdf, etc.:\n")  # The file extension

if name != " " or name != "":  # Checks if the name is empty. If not, adds a space before the name.
    name = " " + name

files = glob.glob(f"{path}\\*.{file_ext}")
files.sort(key=os.path.getmtime)  # Sorts the files by date

if len(files) == 0:  # Checks if there are any files with the file extension the user gave
    print(f"There aren't any files with '.{file_ext}' extension.")
else:
    for i in range(len(files)):
        file = files[i]
        os.rename(file, f'{path}\\{i + 1}{name}.{file_ext}')
    print("Filename change successful.")
