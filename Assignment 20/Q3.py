# Design a Python application that creates two threads named EvenList and OddList.
# Both threads should accept a list of integers as input
# The EvenList thread should:
# Extract all even elements from the list
# Calculate and display their sum 

# The OddList thread should:
# Extract all odd elements from the list.
# Calculate and display their sum.

# Threads should run concurrently.

import threading

def EvenList(data):
    Sum = 0
    print("Even numbers are: ")
    EvenNumbers = []
    for number in data:
        if number % 2 == 0:
            EvenNumbers.append(number)
            Sum = Sum + number
    print(EvenNumbers) 
    print("Sum of Even numbers are: ",Sum)

def OddList(data):
    Sum = 0
    print("Odd numbers are: ")
    OddNumbers = []
    for number in data:
        if number % 2 != 0:
            OddNumbers.append(number)
            Sum = Sum + number
    print(OddNumbers)
    print("Sum of odd numbers are: ",Sum)


def main():
    Size = int(input("Enter the size of List: "))
    Data = list()
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("Give List Data is: ",Data)


    t1 = threading.Thread(target=EvenList,args=(Data,))
    t2 = threading.Thread(target=OddList,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()