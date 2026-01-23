# Write a program which accepts one number and checks whether it is perfect number or not.

def CheckPerfect(No):
    sum = 0
    end = No//2
    for i in range(1,end+1):
        if No % i == 0:
          sum = sum + i
    if No == sum:
            print("Perfect Number")
    else:
           print("Not Perfect Number")


def main():
    num = int(input("Enter the number:"))
    CheckPerfect(num)


if __name__ == "__main__":
    main()