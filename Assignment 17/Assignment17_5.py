# Write a program which accept one number for user and check whether number is prime or not
# Input : 5   Output : It is Prime Number

def CheckPrime(No):
    Count = 0
    for i in range(2,No):
        if No % i == 0:
            Count = Count + 1
    return Count


def main():
    Number = int(input("Enter the number: "))
    Result = CheckPrime(Number)
    if Result == 0:
        print("Prime Number:")
    else:
        print("Not Prime:")

if __name__ == "__main__":
    main()