# Write a lambda function using reduce() which accepts a list of numbers and returns the 
# minimum element

from functools import reduce

Minimum = lambda a,b:a if a<b else b

def main():
    Size = int(input("Enter the Size:"))
    Data = []

    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    print("List is : ",Data)

    RData = reduce(Minimum,Data)
    print("Data After Reduce is : ",RData)
    

if __name__ == "__main__":
    main()