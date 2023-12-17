# Q.27 Write a program to find all armstrong number in the range of 0 and 999.
for num in range(10,1000):
    numstr = str(num)
    numdigits = len(numstr)
    sumdigits = 0
    for digit in numstr:
        sumdigits += int(digit)** numdigits
    if(sumdigits == num):
        print(num)