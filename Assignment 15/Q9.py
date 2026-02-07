# Write a lambda function using reduce() which accepts a list of numbers and returns the product
# of all elements

from functools import reduce


ProductElements = lambda A,B: A+B

def main():
    Size = int(input("Enter the Size of list :"))
    Data = []

    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    
    print("The given List is : ",Data)

    RData = reduce(ProductElements,Data)
    print("Data After Reduce is : ",RData)

if __name__ == "__main__":
    main()