# Q.24 Write a program that ask the user to input a positive integer. Your program should find and display the sum of digits of number.
n = int(input("Enter a positive number:"))
sum=0
while n>0:
    sum+=n%10
    n/=10
print("The sum of its digits is:",int(sum))