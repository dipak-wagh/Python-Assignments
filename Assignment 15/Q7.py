# Write a lambda function using filter() which accepts list of strings and returns a list of strings 
# having length greater than 5

GreaterString = lambda s: len(s) > 5

def main():
    Size = int(input("Enter the No of strings:"))
    Data = []

    for i in range(Size):
        Value = str(input("Enter a string:  "))
        Data.append(Value)
    print("List is : ",Data)

    FData = list(filter(GreaterString,Data))
    print("List of Strings Whose Length Greater than 5 : ",FData)


if __name__ == "__main__":
    main()