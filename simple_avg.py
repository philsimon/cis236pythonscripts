#!
total = 0.0
number1=float(input("Enter the first number: "))
total = total + number1
number2=float(input("Enter the second number: "))
total = total + number2
number3=float(input("Enter the third number: "))
total = total + number3
average = round((total / 3),4)
print ("The average is " + str(average))

if average > 12:
    print("That's a big average.")
else:
    print("That's not so big.")

print ("zzzThe average is ", average)
