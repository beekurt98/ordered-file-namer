# Chronological File Namer
A code I wrote for my own use. 

I take many screenshots when I'm on PC, especially while watching educational videos or playing games with stories. I wrote this code to rename every file in chronological order in desired directory. 

The program asks the user for a directory, a name and a file extension. 

**For example:**
```
Please enter the directory/path of the folder:
C:\Users\user\Desktop\Python Resources\YouTube
Desired name after EVERY number (can be left empty):
freeCodeCamp
File extension to search & change the game of. For example, png, jpeg, txt, pdf, etc.:
png
From which number the naming should start? For example, 1, 5, 8. (Good for naming multiple files)
3
```

**The output will be:**
```
Filename change successful.
```

**The filenames will be:**
3 freeCodeCamp.png
4 freeCodeCamp.png
5 freeCodeCamp.png
6 freeCodeCamp.png
...

**Naming**
You don't need to put a space before the name, the program will put it for you.

**Starting Number**
This was added for the directories that have multiple types of files with different extensions and do not need to be in chronological order. 
For example, I had 12 jpg, 11 png files and named the png's starting from 13. This allowed me some order in the program. You can just type 1. 

**Warning**
I tested this on Windows & it works, but I haven't tested it on other OS, so there might be errors.
