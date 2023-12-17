# Q.16 Write a program that prompts the user to input a number. Program should display the corresponding days to the number.
days = {}
days[1]="Monday"
days[2]="Tuesday"
days[3]="Wednesday"
days[4]="Thursday"
days[5]="Friday"
days[6]="Saturday"
days[7]="Sunday"
D = int(input("Enter a number(between 1-7):"))
if D in days:
    print(days[D])
    # print("The day is:",days)
else:
    print("Please give a number between 1-7")