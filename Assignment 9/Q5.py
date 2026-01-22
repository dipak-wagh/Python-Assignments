# Write a program which accepts one number and checks whether it is divisible by 3 and 5
# Input: 15
# Output: Divisible by 3 and 5

def CheckDivisible(No):
    if No%3==0 and No%5==0:
        return True
    else:
        return False

def main():
    Num=int(input("Enter Number:"))
    Result = CheckDivisible(Num)
    
    if Result:
        print(Num,"is divisible by 3 and 5")
    else:
        print(Num,"is Not divisible by 3 and 5")

if __name__ == "__main__":
    main()