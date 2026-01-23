# Write a program which accepts one number and prints count of digits in that number:
# Input: 7521
# Output: 4

def CountDigit(No): # 12
    count = 0     # 0
    if No == 0: 
        return 1
    
    while No > 0:  # 12>0 1>0 0>0
        count += 1 # count=1 2
        No = No //10 # 12//10=1 1//10=0

    return count


def main(): 
    num=int(input("Enter the number:")) # 12
    print("Number of digits:",CountDigit(num)) 

if __name__ == "__main__":
    main()