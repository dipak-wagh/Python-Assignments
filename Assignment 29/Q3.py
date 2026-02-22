# Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments. creates a new file 
# named Demo.txt and copies all contents from the given file into Demo.txt

# Input (Command Line)
# ABC.txt

# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt

import sys

def copyFile(sourceFile):
    try:
        # Open source file in read mode
        with open(sourceFile, "r") as src:
            data = src.read()

        # Create Demo.txt and write data into it
        with open("Demo.txt", "w") as dest:
            dest.write(data)

        print("Contents copied successfully into Demo.txt")

    except FileNotFoundError:
        print("Source file does not exist.")
    except Exception as e:
        print("Error:", e)


def main():
    if len(sys.argv) != 2:
        print("Usage: python scriptname.py <filename>")
        return

    sourceFile = sys.argv[1]
    copyFile(sourceFile)


if __name__ == "__main__":
    main()
