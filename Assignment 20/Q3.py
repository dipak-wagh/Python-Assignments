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




def main():
    Size = int(input("Enter the size of List: "))
    Data = list()
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("Give List Data is: ",Data)

    



if __name__ == "__main__":
    main()