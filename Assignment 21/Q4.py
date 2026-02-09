import threading

def SumElement(Data):
    Sum = 0
    for number in Data:
        Sum = Sum + number
    print("Sum of List Elements is: ",Sum)

def ProductElement(Data):
    Product = 1
    for number in Data:
        Product = Product * number
    print("Product of List is: ",Product)

        
def main():
    Size = int(input("Enter the Size of List: "))
    Data = []

    print("Enter the Elements:")
    for i in range(Size):
        Data.append(int(input()))

    print("The List Data is:", Data)

    t1 = threading.Thread(target=SumElement(Data))
    t2 = threading.Thread(target=ProductElement(Data))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()