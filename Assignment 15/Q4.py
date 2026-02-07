# Write a lambda function using reduce() which accepts a list of numbers and returns the addition
# of all elements.
from functools import reduce

Addition = lambda A,B: A+B

def main():
    Size = int(input("Enter the size of list:"))
    Data = []

    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("List is : ",Data)

    RData = reduce(Addition,Data)
    print("Data After Reduce is:",RData)

if __name__ == "__main__":
    main()