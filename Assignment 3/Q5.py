# What is the difference between: print() and return. Explain with function example

# print(): it is a built in function in python. it used for displaying messages on console.
# return : it is a keyword, used for sends a value from function to caller.

print("hello")

def Multiplication(No1,No2):
    Ans=No1 * No2
    return Ans

Result = Multiplication(10,2)
print("Multiplication is:",Result)

