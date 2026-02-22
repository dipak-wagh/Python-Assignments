# Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file name through command line arguments and compares the contents
# of both Files.
# If both files contain the same contents, display Success
# Otherwise display Failure

# Input(Command Line)
# Demo.txt Hello.txt

# Expected Output:
# Success OR Failure

import sys

def compareFiles(file1, file2):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:
            data1 = f1.read()
            data2 = f2.read()

            if data1 == data2:
                print("Success")
            else:
                print("Failure")

    except FileNotFoundError:
        print("One or both files do not exist.")
    except Exception as e:
        print("Error:", e)


def main():
    if len(sys.argv) != 3:
        print("Usage: python scriptname.py <file1> <file2>")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    compareFiles(file1, file2)


if __name__ == "__main__":
    main()
