# Write a program which accepts one number and prints cube of that number:

def CubeNo(No):
    return No*No*No

def main():
    No = int(input("Enter the number:"))
    Result = CubeNo(No)
    print("Cube of",No, "is:",Result)

if __name__ == "__main__":
    main()