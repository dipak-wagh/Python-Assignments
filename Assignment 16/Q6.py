# Write a program which accept number from user and check whether that number is positive or 
# negative or zero

# Input : 11   Output : Positive Number
# Input : -8   Output : Negative Number
# Input :  0   Output : Zero


def main():
    Number = int(input("Enter the number: "))
    if Number>0:
        print("Positive")
    elif Number<0:
        print("Negative")
    else:
        print("Zero")

if __name__ == "__main__":
    main()