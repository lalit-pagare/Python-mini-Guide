# Q.20 Write a program that prompts the user to input a number and prints its multiplication table.
n = int(input("Enter a number:"))
i=0
sum=0
for i in range(1,11):
    sum=n*i
    print("2 x",i,"=",sum)