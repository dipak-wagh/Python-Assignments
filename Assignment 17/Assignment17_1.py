# Create on module named as Arithmetic which contains 4 functions as Add() for addition
# Sub() for subtraction,Mult() for multiplication and Div() for division. All functions accepts two 
# parameters as number and perform the operation. Write on python program which call all the functtions
# from Arithmetic module by accepting the parameters from user


from Arithmetic import Add, Sub, Mult, Div



def main():
    No1 = int(input("Enter the first number :"))
    No2 = int(input("Enter the second number :"))

    Addition = Add(No1,No2)
    print("Addition is :",Addition)

    Subtraction = Sub(No1,No2)
    print("Subtraction is :",Subtraction)

    Multiplication = Mult(No1,No2)
    print("Multiplication is :",Multiplication)

    Division = Div(No1,No2)
    print("Division is:",Division)

if __name__ == "__main__":
    main()