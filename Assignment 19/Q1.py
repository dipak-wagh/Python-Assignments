# Write a program which contains one lambda function which accepts one parameter and return power of two
# Input : 4   Output: 16
# Input : 6   Output: 64


def main():
    Num = int(input("Enter the Number: "))

    Power = lambda No: 2**No
    print("Power of number is: ",Power(Num))

if __name__ == "__main__":
    main()