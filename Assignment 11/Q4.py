# Write a program which accepts one number and prints reverse of that number:
# Input: 123
# Output: 321

def ReverseNumber(No):
    reverse=0
    while No>0:
        digit=No%10
        reverse=(reverse*10) + digit
        No = No//10
    return reverse
        

def main():
    num=int(input("Enter the number:"))
    print("Reverse no. is:",ReverseNumber(num))

if __name__ == "__main__":
    main()