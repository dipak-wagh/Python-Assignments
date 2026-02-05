# Write a program which contains one function named as ChkNum() which accept one parameter as number
# if number is even then it should display "Even number" otherwise display "Odd number" on console

def ChkNum(Num):
    # if Num % 2 ==0:
    #     return True
    # else:
    #     return False

    return Num % 2 == 0


def main():
    Number = int(input("Enter the number: "))
    Result = ChkNum(Number)
    if Result == True:
        print("Even number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()