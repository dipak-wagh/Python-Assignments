# Write a program which accept number from user and print that number of "*" on Screen.
# Input : 5      Output : * * * * *

def main():
    Number = int(input("Enter the number: "))
    
    for i in range(Number):
        print("*",end = " ")

if __name__ =="__main__":
    main()