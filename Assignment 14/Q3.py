# Write a lambda function which accepts two numbers and returns maximum number

No1 = int(input("Enter the first number : "))
No2 = int(input("Enter the second number : "))

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2
print("Maximum number is : ",Maximum(No1,No2))