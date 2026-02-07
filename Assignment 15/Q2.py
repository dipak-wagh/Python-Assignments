# Write a lambda function using filter() which accepts a list of numbers and returns a list of 
# even nos.

CheckEven = lambda No:(No % 2 == 0)

def main():
    size = int(input("Enter the size of list:"))
    Data = []

    for i in range(size):
        value = int(input())
        Data.append(value)

    print("list is:",Data)

    FilterData = list(filter(CheckEven,Data))
    print("Data After Filter is : ",FilterData)


if __name__ == "__main__":
    main()