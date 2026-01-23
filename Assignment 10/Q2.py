# Write a program which accepts one number and prints sum of first N natural numbers
# Input: 5
# Output: 15

def SumNatural(No):
    sum = 0
    for i in range(1,No + 1):
        sum = sum + i
    return sum

def main():
    num=int(input("Enter the number:"))
    result = SumNatural(num)
    print(result)

if __name__ == "__main__":
    main()