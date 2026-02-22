# Display File Contents
# Problem Statements:
# Write a program which accepts a file name from the user, opens that file, and displays the entire 
# contents on the console.

# Input:
# Demo.txt

# Expected Output:
# Display contents of Demo.txt on console

def displayFileContents(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            print("\nFile Contents:\n")
            print(data)
    except FileNotFoundError:
        print(f"{filename} does not exist in the current directory.")
    except Exception as e:
        print("Error:", e)

def main():
    fileName = input("Enter file name: ")
    displayFileContents(fileName)

if __name__ == "__main__":
    main()
