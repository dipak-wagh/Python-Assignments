# Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input
# The small thread should count and display the number of lowercase characters.
# The capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display:
#    Thread ID
#    Thread Name

import threading
import os

def Small(name):
    count = 0
    print("\nThread ID:",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
    print("Small Characters is: ")
    for char in name:
        if char.islower():
            print(char,end=" ")
            count = count + 1
    print("\nSmall Charcater count is: ",count)
    print()
    

def Capital(name):
    count = 0
    print("\nThread ID:",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
    print("Capital Charcaters is: ")
    for char in name:
        if char.isupper():
            print(char,end=" ")
            count = count + 1
    print("\ncapital character count is: ",count)
    print()

def Digits(name):
    count = 0
    print("\nThread ID:",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
    print("Digits is: ")
    for num in name:
        if num.isdigit():
            print(num,end=" ")
            count = count + 1
    print("\n Digits is: ",count)
    print()
    

def main():
    name = input("Enter the input string: ")

    t1 = threading.Thread(target=Small,args=(name,),name="Small")
    t2 = threading.Thread(target=Capital,args=(name,),name="Capital")
    t3 = threading.Thread(target=Digits,args=(name,),name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()