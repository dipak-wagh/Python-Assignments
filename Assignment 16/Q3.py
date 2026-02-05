# Write a program which contains one function named as Add() which accepts two numbers from user and 
# return addition of that two numbers.

def Add(Num1,Num2):
    return Num1 + Num2

def main():
    Num1 = int(input("Enter first number : "))
    Num2 = int(input("Enter second number :"))

    Result = Add(Num1,Num2)
  # print(f"Addition of {Num1} and {Num2} is : ",Result)
    print("Addition is:",Result)

if __name__ == "__main__":
    main()