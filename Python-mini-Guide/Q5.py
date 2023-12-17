#Q.5 Write a program that accept seconds from keyboard as integer. Your program should convert seconds in hours,minutes and seconds. Your output should like this:
# Enter seconds: 13400
# Hours: 3
# Minues: 43
# Seconds: 20
S = int(input("Enter time in seconds:"))
h = S/3600
m = S%3600/60
se = S%60

print("Hours:",int(h))
print("Minutes:",int(m))
print("Seconds:",int(se))