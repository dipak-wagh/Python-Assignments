# Write a program which accepts one number and prints that many numbers starting from 1

def printNos(No):
    for i in range(1,No+1):
        print(i)

def main():
    Num = int(input("Enter the number:"))
    printNos(Num)




if __name__ == "__main__":
    main()