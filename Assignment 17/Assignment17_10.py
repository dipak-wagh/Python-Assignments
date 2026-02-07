# Write a program which accept number from user and return addition of digits in that number.
# Input : 123   Output: 6

def main():
    Num = int(input("Enter the number:"))
    Sum = 0
    while Num != 0:
        rem = Num % 10
        Num = Num // 10
        Sum = Sum + rem
    
    print("The sum is :",Sum)

if __name__ == "__main__":
    main()