# Design a Python application that creates two threads named EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter.

# The EvenFactor thread should:
# Identify all even factors of the given number.
# Calculate and display the sum of even factors

# The OddFactor thread should:
# Identify all odd factors of the given number.
# Calculate and display the sum of odd factors

# After both threads complete execution, the main thread should display the message:"Exit from main"

# import threading

# def Even(no):
#     print("Even numbers: ")
#     for i in range(1,no+1):
#         if no%i == 0:
#             if i%2 == 0:
#                 print(i,end=" ")


# def Odd(no):
#     print("Odd numbers: ")
#     for i in range(1,no+1,2):
#         if no%i == 0:
#             print(i,end=" ")


# def main():
#     Number = int(input("Enter the number: "))
#     EvenFactor = threading.Thread(target=Even(Number))
#     OddFactor = threading.Thread(target=Odd(Number))

#     EvenFactor.start()
#     OddFactor.start()

#     EvenFactor.join()
#     OddFactor.join()

#     print("Exit from the main:")

# if __name__ == "__main__":
#     main()


import threading

def Even(no):
    Sum = 0
    print("Even factors are:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i, end=" ")
            Sum = Sum + i
    print("\nSum of even factors is:", Sum)


def Odd(no):
    Sum = 0
    print("Odd factors are:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i, end=" ")
            Sum = Sum + i
    print("\nSum of odd factors is:", Sum)


def main():
    Number = int(input("Enter the number: "))

    EvenFactor = threading.Thread(target=Even, args=(Number,), name="EvenFactor")
    OddFactor = threading.Thread(target=Odd, args=(Number,), name="OddFactor")

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
