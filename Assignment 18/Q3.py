# Write a program which accept N numbers from user and store it into List. Return Minimum number from List

def Minimum(Arr):
    Min = Arr[0]
    for number in Arr:
        if Min > number:
            Min = number
    return Min

def main():
    Size = int(input("Enter the Size of List: "))
    print("Enter the List elements:")
    Data = list()
    for i in range(Size):
        value = int(input())
        Data.append(value)
    
    print("List of Data is : ",Data)

    print("Minimum Element from List is: ",Minimum(Data))

if __name__ == "__main__":
    main()