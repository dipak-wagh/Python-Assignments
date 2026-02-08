# Design a Python application that creates two separate threads named Even and Odd
# The Even thread should display first 10 even numbers
# The Odd thread should display the first 100 odd numbers.
# Both threads should execute independently using threading module.
# Ensure proper thread creation and execution.

import threading

def DisplayEven():
    print("Even numbers:")
    for i in range(2,22,2):
        print(i,end=" ")
    print()


def DisplayOdd():
    print("Odd numbers: ")
    for i in range(1,200,2):
        print(i,end=" ")
    print()


def main():
    Even = threading.Thread(target=DisplayEven)
    Odd = threading.Thread(target=DisplayOdd)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

    print("Both threads Execution Complete")

if __name__ == "__main__":
    main()