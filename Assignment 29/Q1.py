# Check file Exists in Current Directory
# Problem Statement: Write a program which accepts a file name from the user and checks whether that 
# file exists in the current directory or not.

# Input: 
# Demo.txt

# Expected Output: 
# Display whether Demo.txt exists or not

import os

def checkFileExists(filename):
    if os.path.isfile(filename):
        print(f"{filename} exists in the current directory.")
    else:
        print(f"{filename} does not exist in the current directory.")

def main():
    fileName = input("Enter file name: ")
    checkFileExists(fileName)

if __name__ == "__main__":
    main()
