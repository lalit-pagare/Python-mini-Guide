# Q.28 Write a program to print the following:
# 1.
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# 2.
# *
# * * 
# * * *
# * * * * 
# * * * * *
# 3.
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# 4.
#     *
#    * * 
#   * * * 
#  * * * * 
# * * * * *
# 5.
#      1
#    2 2 2 
#   3 3 3 3
#  4 4 4 4 4
# 5 5 5 5 5 5
n = 5
for row in range(1,n+1):
    for col in range(1,n+1):
        print("*",end=" ")
    print()
print("--------------------------------------------------")
for row1 in range(1,n+1):
    for col1 in range(1,row1+1):
        print("*",end=" ")
    print()
print("-------------------------------------------")
for row2 in range(1,n+1):
    for sp in range(0,n-row2):
        print(" ",end=" ")
    for col2 in range(1,row2+1):
        print("*",end=" ")
    print()
print("---------------------------------------")
for row3 in range(1,n+1):
    for sp1 in range(0,n-row3):
        print(" ",end=" ")
    for col3 in range(1,row3+1):
        print(" * ",end=" ")
    print()
print("------------------------------------------------")
for row4 in range(1,n+1):
    for sp2 in range(0,n-row4):
        print(" ",end=" ")
    for col4 in range(1,2*row4):
        print(row4,end=" ")
    print()