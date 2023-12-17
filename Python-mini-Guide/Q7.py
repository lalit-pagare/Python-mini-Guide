#Q.7 Write program that prompts user to enter number in two variables and swap the contents of the two variables(Do not declare extra variable).
A = int(input("Enter value of A:"))
B = int(input("Enter value of B:"))
A=A+B
B=A-B
A=A-B
print(A)
print(B)
