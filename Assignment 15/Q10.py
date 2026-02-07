# Write a lambda function using filter() which accepts a list of numbers and returns the count of 
# even numbers

CountEven = lambda No:No % 2 == 0

def main():
    Size = int(input("Enter the number of List : "))
    Data = []

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("The given list is : ",Data)

    EvenCount = len(list(filter(CountEven,Data)))
    print("Count of even numbers from list is : ",EvenCount)

if __name__ == "__main__":
    main()