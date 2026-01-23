# Write a program which accepts one character and checks whether it is vowel or consonant
# Input: a
# Output: Vowel

def checkVowel(ch):
    vowels="aeiouAEIOU"

    if ch in vowels:
        return True
    else:
        return False
    
def main():
    ch=input("Enter a character:")

    if checkVowel(ch):
        print("Vowel")
    else:
        print("Consonant")


if __name__ == "__main__":
    main()