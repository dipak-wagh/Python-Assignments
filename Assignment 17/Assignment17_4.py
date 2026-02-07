# Write a program which accept one number from user and return addition of its factors.
# Input : 12       Output : 16    (1+2+3+4+5+6)

def Addition_factors(No):
    Sum = 0
    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i
    return Sum    
  

def main():
    Number = int(input("Enter the number: "))
    Result = Addition_factors(Number)
    print("Addition of factors is:",Result)

if __name__ == "__main__":
    main()

