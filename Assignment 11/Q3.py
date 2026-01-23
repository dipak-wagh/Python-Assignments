# Write a program which accepts one number and prints sum of digits
# Input: 123
# Output: 6

def SumOfDigit(No):
    sum = 0

    while No> 0:
        digit = No % 10
        sum = sum + digit
        No = No // 10
    
    return sum

def main():
    num = int(input("Enter the number:"))
    print("Sum of digit is:",SumOfDigit(num))


if __name__ == "__main__":
    main()