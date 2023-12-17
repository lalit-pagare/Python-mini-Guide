# Q.29 Write a program that accept a list from user and print the alternate element of list.
lst = input("Enter a list of elements saparated by space:").split()
for i in range(0,len(lst),2):
    print(lst[i])