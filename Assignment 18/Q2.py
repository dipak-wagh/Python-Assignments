# Write a program which accepts N numbers from user and store it into List. Return Maximum number 
# from that list

# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56


def Maximum(Arr):
    max = Arr[0]

    for number in Arr :
        if number > max:
            max = number
    return max


def main():
    print("Enter the size of list:")
    Size = int(input())
    Data = list()

    print("Enter the Elements of list: ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    print("List is :",Data)

    result = Maximum(Data)
    print("Maximum Number is :",result)

if __name__ == "__main__":
    main()