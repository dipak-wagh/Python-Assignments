# Write a lambda function which accepts one number and returns True if number is even otherwise False

Num = int(input("Enter the number : "))
CheckEven = lambda Num: True if Num % 2 == 0 else False
print(CheckEven(Num))