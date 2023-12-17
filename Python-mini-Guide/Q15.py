# Q.15 The marks obtained by a student in 3 diffrent subjects are input by the user. Your program should calculte the average of subjects and display the grade. The student gets a grade as per the following rules.
# Average        Grade
# 90-100           A
# 80-89            B
# 70-79            C
# 60-69            D
# 0-59             F

M = int(input("Enter marks obtained in Mathamatics:"))
S = int(input("Enter marks obtained in Science:"))
E = int(input("Enter marks obtained in English:"))
Avg = M+S+E/3
if(Avg <= 59):
    print("Sorry bro your grade is: F")
elif(Avg <= 69):
    print("Your grade is 'D'")
elif(Avg <= 79):
    print("Your grade is 'C'")
elif(Avg <= 89):
    print("Your grade is 'B'")
else:
    print("Congratulations! Your grade is 'A'")