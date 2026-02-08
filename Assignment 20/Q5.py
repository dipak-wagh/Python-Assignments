# Design a Python application that creates two threads named Thread1 and Thread2
# Thread1 should display numbers from 1 to 50
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure that:
#   Thread2 starts execution only after Thread1 has completed.
# Use approximate thread Synchronization.

import threading


def DisplayOne():
    num = 50
    print("\nNumbers from 1 to 50 are: ")
    for i in range(1,num+1):
            print(i,end=" ")

def DisplayTwo():
    print("\nNumbers from 50 to 1 are: ")
    for i in range(50,0,-1):
            print(i,end=" ")

def main():

    t1 = threading.Thread(target=DisplayOne)
    t2 = threading.Thread(target=DisplayTwo)

    t1.start()
    t1.join()

    t2.start()
    t2.join()


if __name__ == "__main__":
    main()