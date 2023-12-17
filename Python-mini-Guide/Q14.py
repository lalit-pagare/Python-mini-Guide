#Q.14 Write a program that prompts the user to input numbers of calls and calculate the monthly telephone bills as per the following rule:
# Minimum Rs. 200 for upto 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.

calls = int(input("Enter number of calls in this month:"))
if(calls <= 100):
    print("Your total telephone bill of this month is Rs. 200")
elif(calls <=150):
    print("Your total telephone bill of this month is Rs.",calls*0.60)
elif(calls <= 200):
    print("Your totla telephone bill of this month is Rs.",calls*0.50)
else:
    print("Your total telephone bill of this month is Rs.",calls*0.40)