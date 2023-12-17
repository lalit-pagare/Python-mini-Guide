# Q.21 Write a program that prompts the user to input a number and print its factorial.
n = int(input("Enter a number:"))
i = 1
fact = 1
for i in range(1,n+1):
    fact*=i
print(fact)