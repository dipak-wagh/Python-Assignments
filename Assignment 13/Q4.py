# Write a program which accepts one number and print binary equivalent.

def PrintBinary(No):
    binary = ""

    if No == 0:
        return "0"
    
    while No > 0:
        binary = str(No % 2) + binary
        No = No // 2
    
    return binary

def main():
    num=int(input("Enter the number:"))
    print("Binary number is:",PrintBinary(num))


if __name__ == "__main__":
    main()