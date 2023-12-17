#Q.6 Write a program that prompts the user to enter number in two variables and swap the contents of the variables.
A = int(input("Enter value of A:"))
B = int(input("Enter value of B:"))
swap=A
A=B
B=swap
print("Value of A is",A)
print("Value of B is",B)