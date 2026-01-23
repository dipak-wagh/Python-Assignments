# Write a program which accepts two numbers and prints addition,subtraction,multiplication 
# and division


def main():
    Num1=int(input("Enter the first number:"))
    Num2=int(input("Enter the second number:"))

    Addition=Num1+Num2
    Subtraction=Num1-Num2
    Multiplication=Num1*Num2
    Division=Num1/Num2

    print("Addition is:",Addition)
    print("Subtraction is:",Subtraction)
    print("Multiplication is:",Multiplication)
    print("Division is:",Division)

if __name__ == "__main__":
    main()