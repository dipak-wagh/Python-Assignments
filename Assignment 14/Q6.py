# Write a lambda function which accepts one number and return True if number is Odd otherwise False

Num = int(input("Enter the number : "))
CheckOdd = lambda Num: True if Num%2 != 0 else False
print(CheckOdd(Num))