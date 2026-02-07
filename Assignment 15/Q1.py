# Write a lambda function using map() which accepts a list of numbers and returns a list of 
# squares of each numbers


Squares = lambda No:No*No

def main():
    Size = int(input("Enter the size of list:"))
    Data = []

    for i in range(Size):
        value = int(input())
        Data.append(value)

    print("Actual list is:",Data)

    MData = list(map(Squares,Data))
    print("Squares of list Data is:",MData)


if __name__ == "__main__":
    main()