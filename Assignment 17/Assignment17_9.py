# Write a program which accept number from user and return number of digits in that number.
# Input : 5187934   Output : 7

def main():
    Number = int(input("Enter the number: "))
    count = 0
    while Number != 0:
        Number = Number // 10
        count=count+1
    
    print("Count of number is: ",count)

if __name__ == "__main__":
    main()