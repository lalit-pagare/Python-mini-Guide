#Q.8 Write a program that prompts the user to input the radius of the circle and output the area and circumference of the circle.
R = float(input("Enter radius of circle:"))
PI= 3.14
A = PI*(R*R)
C = 2*PI*R
print("Area of circle is:",float(A))
print("Circumference of circle is:",float(C))
