#!
#program that asks for threshold
#calculates average value for three numbers
#then compares the two
total = 0.0
thresh = int(input("What is your threshold? "))
number1 = float(input("Enter the first number: "))
total = total + number1
number2 = float(input("Enter the second number: "))
total = total + number2
number3 = float(input("Enter the third number: "))
total = total + number3
average = round((total / 3),1)
print ("The average is " + str(average))

if average > thresh:
    print("That number is greater than your threshold.")
else:
    print("That number is less than your threshold.")
