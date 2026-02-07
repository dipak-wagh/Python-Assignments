# Write a program which accept N numbers from user and store it into List. Return addition of all 
# prime numbers from that List. Main Python file accepts N numbers from user and pass each number
# to ChkPrime() function which is part of our user defined named as MarvellousNum. Name of the function
# from main python file should be ListPrime()

# Input : Number of elements: 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54(13 + 5 + 7 + 2 + 5)

from MarvellousNum import ChkPrime

def ListPrime(Arr):
    Sum = 0
    for num in Arr:
        if ChkPrime(num):
            Sum = Sum + num
    return Sum


def main():
    print("Enter the Size of List: ")
    Size = int(input())

    Data = list()
    print("Enter the Elements for List:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("Data is :",Data)

    Result = ListPrime(Data)
    print("Addition of Prime numbers is: ",Result)

if __name__ == "__main__":
    main()