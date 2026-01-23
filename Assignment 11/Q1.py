# Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number

def CheckPrime(No):
    if No <= 1:
        return False
    
    for i in range(2,No):
        if No%i == 0:
            return False
    return True


def main():
    num=int(input("Enter number:"))

    if CheckPrime(num):
        print(num,"is a Prime Number")
    else:
        print(num,"is not a Prime Number")

if __name__ == "__main__":
    main()