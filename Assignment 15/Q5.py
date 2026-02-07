# Write a lambda function using reduce() which accepts list of numbers and returns the maximum 
# element

from functools import reduce

Maximum = lambda a,b:a if a>b else b

def main():
    Size = int(input("Enter the size of list"))
    Data = []

    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("List is:",Data)

    RData = reduce(Maximum,Data)
    print("Data After Reduce is :",RData)

if __name__ == "__main__":
    main()