#Q.9 Write a program that prompts the user to input the length and Width of the rectangle and outputs the area and circumference of the rectangle.
L = int(input("Enter the length:"))
W = int(input("Enter the width:"))
A = L*W
P = 2*(L+W)
print("Area of rectangle is:",A)
print("Perimeter of rectangle is:",P)

# Circumference if a unit of circle so that's why it is not applicable in the case of rectangle.So we use perimeter in rectangle..