# Write a lambda function which accepts two numbers and returns minimum number:

No1 = int(input("Enter the first number : "))
No2 = int(input("Enter the second number : "))

Minimum = lambda No1, No2 : No1 if No1 < No2 else No2
print("Minimum number is : ",Minimum(No1,No2))
