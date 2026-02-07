# Write a program which accept one number from user and return its factorial.
# Input : 5              Output : 120

def factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    return fact
        


def main():
    Number = int(input("Enter the number:"))
    Result = factorial(Number)
    print("Factorial is:",Result)


if __name__ == "__main__":
    main()