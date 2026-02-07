# Write a program which contains filter(), map() and reduce() in it. Python application which contains
# one list of numbers.List contains the numbers which are accepted from user.Filter should filter out
# all such numbers which are even. Map function will calculate its square. Reduce will return addition 
# of all that numbers

# Input List = [5,2,3,4,3,4,1,2,8,10]
# List after filter = [2,4,4,2,8,10]
# List after map = [4,16,16,4,64,100]
# Output of reduce = 204

from functools import reduce

EvenNumbers = lambda No: No % 2 == 0

SquareNumber = lambda No: No * No

AdditionNumbers = lambda A,B: A + B

def main():
    print("Enter the Size of list")
    Size = int(input())

    print("Enter the List elements: ")
    Data = list()
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("List Data is: ",Data)

    FData = list(filter(EvenNumbers,Data))
    print("Data after Filter is :",FData)

    MData = list(map(SquareNumber,FData))
    print("Data after Map is: ",MData)

    RData = reduce(AdditionNumbers,MData)
    print("Data after Reduce is: ",RData)



if __name__ == "__main__":
    main()