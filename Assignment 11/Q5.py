# Write a program which accepts one number and checks whether it is palindrome or not
# Input: 121
# Output: Palindrome

def CheckPalindrome(No):
    temp=No
    reverse = 0

    while No > 0:
        digit = No % 10
        reverse = (reverse*10)+digit
        No=No//10

    return temp == reverse

def main():
    num=int(input("Enter the number:"))
    if CheckPalindrome(num):
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()