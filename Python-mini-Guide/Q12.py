# Q.12 Write a program that prompts the user to input three integers and output the largest.
A = int(input("Enter value of A:"))
B = int(input("Enter value of B:"))
C = int(input("Enter value of C:"))
if(A>B>C):
    print("A is the largest!")
elif(B>C>A):
    print("B is the largest!")
else:
    print("C is the largest!")
    
