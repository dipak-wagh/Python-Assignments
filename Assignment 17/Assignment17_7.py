# Write a program which accept one number and display below patterns
# Input : 5
# Output : 1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5



def main():
    Num = 5
    for i in range(1,Num+1):
        for i in range(1,Num+1):
            print(i,end=" ")
        print()

if __name__ == "__main__":
    main()