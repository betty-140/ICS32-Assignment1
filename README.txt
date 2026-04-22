# ICS32-Assignment1

In this assignment, I wrote an interactive file explorer in Python, which allows the user to create, read, or delete files with .dsu extension. The user are supposed to enter commands in a shell-like format, such as "D not_a_real_file.dsu". This program keeps accepting user input until the user enters the Q command to quit.

This program implements the Path dictionary in pathlib to work with file paths; and shlex to parse user input, including paths with spaces. The program is also able to handle exceptions, like invalid commands and file operation errors, by printing ERROR.