# Q.26 Write a program that prompts the user to input two numbers and display its H.C.F.
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
if(n1 < n2):
    smaller = n1
else:
    smaller = n2
hcf = 1

for i in range(1, smaller+1):
    if(n1 % i == 0) and (n2%i == 0):
        hcf = i
print("The hcf of",n1,"and",n2,"is",hcf)