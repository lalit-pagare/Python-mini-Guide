#Q.13 Write a program that prompts the user to input a year and determine whether the year is leap year or not.
Y = int(input("Enter your year:"))
if(Y%4==0):
    print("Year is leap year!")
else:
    print("Year is not a leap year!")