# Write a program which contains one lambda function which accepts two parameters and return its multiplication

Multiplication = lambda A, B: (A * B)

def main():
    Num1 = int(input("Enter the first number: "))
    Num2 = int(input("Enter the second number: "))

    print("Multiplication is :",Multiplication(Num1,Num2))


if __name__ == "__main__":
    main()