# Write a lambda function which accepts one number and returns cube of that number.

Num = int(input("Enter the number : "))
Cube = lambda Num:Num*Num*Num
print(f"Cube of",Num,"is",Cube(Num))