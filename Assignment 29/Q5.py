# Frequency of a String  in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency
# (Count of occurrences) of that string in the file. 

# Input:
# Demo.txt Marvellous

# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt

def countFrequency(filename, searchString):
    try:
        with open(filename, "r") as file:
            data = file.read()

            count = data.count(searchString)

            print(f'"{searchString}" appears {count} times in {filename}')

    except FileNotFoundError:
        print("File does not exist.")
    except Exception as e:
        print("Error:", e)


def main():
    fileName = input("Enter file name: ")
    searchString = input("Enter string to search: ")

    countFrequency(fileName, searchString)


if __name__ == "__main__":
    main()
