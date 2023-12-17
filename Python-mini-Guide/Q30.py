# Q.30 Write a program that accept a list from user. Your program should reverse the content of list and display it. Do not use reverse()
lst = input("Enter a list of elements saparated by space:").split()
rev =[]
for i in range(len(lst)-1,-1,-1):
    rev.append(lst[i])
print("Reversed list looks like:",rev)