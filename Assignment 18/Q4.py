# Write a program which accept N numbers from user and store it into List. Accept one another number 
# from user and return frequency of that number from List

# Input : Number of elements : 5
# Input Elements: 10 20 10 30 40
# Element to search: 10
# Output : 3
def CheckFrequency(Arr, SearchNum):
    Count = 0
    for number in Arr:
        if number == SearchNum:
            Count = Count + 1
    return Count


def main():
    Size = int(input("Enter the size of List: "))

    Data = []
    print("Enter the elements of List:")
    for i in range(Size):
        value = int(input())
        Data.append(value)

    Search = int(input("Enter the Number to check its Frequency: "))

    Result = CheckFrequency(Data, Search)
    print("Frequency is:", Result)

    print("List Data is:", Data)


if __name__ == "__main__":
    main()
