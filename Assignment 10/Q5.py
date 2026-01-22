# Write a program which accepts one number and prints all odd numbers till that number

def OddNum(Num):
    for i in range(1,Num+1):
        if not i % 2 ==0:
            print(i)

def main():
    num=int(input("Enter the number:"))
    OddNum(num)

if __name__ == "__main__":
    main()