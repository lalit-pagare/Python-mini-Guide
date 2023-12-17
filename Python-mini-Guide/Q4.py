#Q.4 Write a program which accept principle,rateand time from user and print the simple interest.
P = int(input("Enter the Principal:"))
R = int(input("Enter the Rate:"))
T = int(input("Enter the Time:"))
SI = (P*T*R)/100
print("Simple interest is",SI)