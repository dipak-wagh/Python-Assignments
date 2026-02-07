# Write a lambda function using filter() which accepts list of numbers and returns a list of odd nos

CheckOdd = lambda No:(No%2 != 0)

def main():
    Size = int(input("Enter the size of the list:"))
    Data = []

    for i in range(Size):
        value = int(input())
        Data.append(value)

    print("List is : ",Data)

    FilterData = list(filter(CheckOdd,Data))
    print("List After Filter Data is:",FilterData)



if __name__ == "__main__":
    main()