# Write a program which contains filter(), map() and reduce() in it.Python application which contains 
# one list of numbers. List contains the numbers which are accepted from user.Filter should filter out
# all prime numbers.Map function will multiply each number by 2. Reduce will return Maximum number from
# that numbers.

# Input List: [2,70,11,10,17,23,31,77]
# List After filter = [2,11,17,23,31]
# List after map = [4,22,34,46,62]
# Output of reduce = 62

def Prime(No):
    if No <= 1:
        return False
    
    for i in range(2,No):
        if No % i == 0:
            return False
    return True
            

def main():
    print("Enter the Size of list: ")
    Size = int(input())
    Data = list()
    print("Enter the List Elements: ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    print("List Data is: ",Data)

    FData = list(filter(Prime,Data))
    print("Data after Filter is: ",FData)


if __name__ == "__main__":
    main()