# Count Lines in a File 
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the 
# current directory or not.

# Input:
# Demo.txt

# Expected Output:
# Display whether Demo.txt existsor not.

def countLines(filename):
    try:
        with open(filename, "r") as file:
            count = 0
            for line in file:
                count += 1

        print(f"Total number of lines in {filename}: {count}")

    except FileNotFoundError:
        print(f"{filename} does not exist in the current directory.")
    except Exception as e:
        print("Error:", e)


def main():
    fileName = input("Enter file name: ")
    countLines(fileName)


if __name__ == "__main__":
    main()
