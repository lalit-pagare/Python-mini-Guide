# Q.17 Write a program that prompts the user to input a character and determines the character is vowel or consonant.
vowels = ["a","e","i","o","u"]
c = str(input("Enter a character(character must be in small):"))
if c in vowels:
    print(c,"is a vowel")
else:
    print(c,"is consonant")