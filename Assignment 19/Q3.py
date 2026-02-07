# Write a program which contains filter(), map() and reduce() in it. Python application which contains
# one list of numbers. List contains the numbers which are accepted from user. Filter should filter
# out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function 
# will increase each number by 10. Reduce will return product of all that numbers

from functools import reduce

Greater = lambda No: (No >= 70 and No<= 90)

IncreaseNumber = lambda No: No + 10

Addition = lambda A, B: (A * B)

def main():
    Size = int(input("Enter the size of List:"))
    Data = list()

    print("Enter the List elements: ")
    
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("Data of List is:",Data)

    FData = list(filter(Greater,Data))
    print("Data after Filter is: ",FData)

    MData = list(map(IncreaseNumber,FData))
    print("Data After Map is: ",MData)

    RData = reduce(Addition,MData)
    print("Data after Reduce is: ",RData)



if __name__ == "__main__":
    main()