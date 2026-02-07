# Write a program which accept one number and display below pattern
# Input : 5
# Output :  * * * * *
#           * * * * * 
#           * * * * *
#           * * * * *
#           * * * * * 
  
def main():
    Number = int(input("Enter the number: "))

    for i in range(Number):
        for j in range(Number):
            print("*",end=" ")
        print()

if __name__ == "__main__":
    main()