# Write a lambda function which accepts one number and returns True if divisible by 5.

Num = int(input("Enter the Number:"))
CheckDivisible = lambda Num:Num%5==0 
print(CheckDivisible(Num))