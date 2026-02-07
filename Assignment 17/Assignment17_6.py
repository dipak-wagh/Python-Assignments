# Write a program which accepts one number and display below pattern.
# Input : 5
# Output :  * * * * * 
#           * * * *
#           * * *
#           * *
#           *

def main():
    Number = 5
    for i in range(Number, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    main()



