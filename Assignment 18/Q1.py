# Write a program which accept N numbers from user and store it into List. Return addition of 
# all elements from that list

# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4  56
# Output : 130


def main():
    Size = int(input("Enter the Size of list:"))
    Data = list()

    print("Enter the Elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    
    print("List Elements are:",Data)

    Sum = 0
    for i in range(Size):
        Sum = Sum + Data[i]
    print("Sum of list is :",Sum)



if __name__ == "__main__":
    main()