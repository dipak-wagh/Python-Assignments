# Write a program to display:
# DataTypes, Memory address, size in bytes of a variable entered by the user
import sys

def main():
    value = input("Enter any value: ")

    if value.isdigit():
        value = int(value)
    else:
        try:
            value = float(value)
        except:
            pass

    print("Value:", value)
    print("Data Type:", type(value))
    print("Memory Address:", id(value))
    print("Size in bytes:", sys.getsizeof(value))

if __name__ == "__main__":
    main()
