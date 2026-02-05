# Write a program which contains one function that accept one number from user and returns true if 
# number is divisible by 5 otherwise return false

def CheckDivisible(Num):
      return Num % 5 == 0
      

def main():
    Number = int(input("Enter the number:"))
    print(CheckDivisible(Number))
        
if __name__ == "__main__":
    main()