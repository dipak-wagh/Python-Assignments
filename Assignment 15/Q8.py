# Write a lambda function using filter() which accepts a list of numbers and returns a list of 
# numbers divisible by both 3 and 5.

CheckDivisible = lambda No:(No % 3 == 0 and No % 5 == 0)

def main():
    Size = int(input("Enter the Size of list : "))
    Data = []

    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    print("The Given List Data is : ",Data)

    FData = list(filter(CheckDivisible,Data))
    print("Data After Filter is : ",FData)



if __name__ == "__main__":
    main()