# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Betty Liu
# runmengl@uci.edu
# 12306049

from pathlib import Path
import shlex

# C - Create a new file in the specified directory.
def handle_create(tokens):
    if len(tokens) != 4:
        print("ERROR")
        return

    if tokens[2] != "-n":
        print("ERROR")
        return

    directory = Path(tokens[1])
    filename = tokens[3]
    new_file = directory / f"{filename}.dsu"

    if not directory.exists() or not directory.is_dir():
        print("ERROR")
        return

    if new_file.exists():
        print("ERROR")
        return

    try:
        new_file.touch()
        print(new_file)
    except Exception:
        print("ERROR")

# D - Delete the file
def handle_delete(tokens):
    if len(tokens) != 2:
        print("ERROR")
        return

    file_path = Path(tokens[1])

    if not file_path.exists() or not file_path.is_file() or file_path.suffix != ".dsu":
        print("ERROR")
        return

    try:
        file_path.unlink()
        print(f"{file_path} DELETED")
    except Exception:
        print("ERROR")

# R - Read the contents of a file.
def handle_read(tokens):
    if len(tokens) != 2:
        print("ERROR")
        return

    file_path = Path(tokens[1])

    if not file_path.exists() or not file_path.is_file() or file_path.suffix != ".dsu":
        print("ERROR")
        return

    try:
        content = file_path.read_text()
        if content == "":
            print("EMPTY")
        else:
            print(content)
    except Exception:
        print("ERROR")

# run the command and catch exceptions
def process_command(user_input):
    """
    Returns False when user wants to quit, otherwise True.
    """
    try:
        tokens = shlex.split(user_input)
    except Exception:
        print("ERROR")
        return True

    if len(tokens) == 0:
        print("ERROR")
        return True

    command = tokens[0]

    if command == "Q":
        if len(tokens) == 1:
            return False
        print("ERROR")
        return True

    if command == "C":
        handle_create(tokens)
    elif command == "D":
        handle_delete(tokens)
    elif command == "R":
        handle_read(tokens)
    else:
        print("ERROR")

    return True

# main
def main():
    running = True
    while running:
        user_input = input()
        running = process_command(user_input)


if __name__ == "__main__":
    main()
