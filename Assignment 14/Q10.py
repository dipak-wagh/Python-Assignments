# Write a lambda function which accepts three numbers and returns largets numbers

print("Enter three numbers")
No1 = int(input())
No2 = int(input())
No3 = int(input())

LargestNumber = lambda No1,No2,No3:No1 if (No1>No2 and No1>No3) else (No2 if No2 >No3 else No3)
print("Largest Number is:",LargestNumber(No1,No2,No3))