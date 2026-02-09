# Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.

import threading

def Prime(Data):
    print("Prime numbers are:", end=" ")
    for no in Data:
        if no <= 1:
            continue

        isPrime = True
        for i in range(2, no):
            if no % i == 0:
                isPrime = False
                break

        if isPrime:
            print(no, end=" ")
    print()


def main():
    Size = int(input("Enter the Size of List: "))
    Data = []

    print("Enter the Elements:")
    for i in range(Size):
        Data.append(int(input()))

    print("The List Data is:", Data)

    t1 = threading.Thread(target=Prime, args=(Data,))
    t1.start()
    t1.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
