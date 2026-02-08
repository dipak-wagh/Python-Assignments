import threading 

def EvenFactors(no):
    Sum = 0
    print("Even Factors are: ")
    for i in range(1,no+1):
        if no % i == 0 and i % 2 == 0:
            print(i,end=" ")
            Sum = Sum + i
            print(i,end=" ")

    print("\nEven Factors Sum is: ",Sum)

def OddFactors(no):
    Sum = 0
    print("Odd factors are: ")
    for i in range(1,no+1):
        if no % i == 0 and i % 2 != 0:
            print(i,end=" ")
            Sum =Sum + i
    print("\nOdd Numbers Sum is: ",Sum)


def main():
    Number = int(input("Enter the number: "))

    t1 = threading.Thread(target=EvenFactors(Number))
    t2 = threading.Thread(target=OddFactors(Number))

    t1.start()
    t2.start()

    t1.join()
    t2.join()



if __name__ == "__main__":
    main()