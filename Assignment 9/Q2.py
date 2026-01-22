# Write a Program which contains one function ChkGreater() that accepts two numbers and prints the 
# greater number

def ChkGreater(No1,No2):
    if No1 > No2:
        return No1
    else:
        return No2
    

def main():
    Result = ChkGreater(10,20)
    print(Result,"is Greater")

if __name__ == "__main__":
    main()