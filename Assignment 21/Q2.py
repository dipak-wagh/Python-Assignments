# Design a Python application that creates two threads.
# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading

def MaxElement(Data):
    max = Data[0]

    for number in Data:
        if number > max:
            max = number
    return max

def main():
    Size = int(input("Enter the Size of List: "))
    Data = []

    print("Enter the Elements:")
    for i in range(Size):
        Data.append(int(input()))

    print("The List Data is:", Data)

    print("Maximum element is: ",MaxElement(Data))

if __name__ == "__main__":
    main()