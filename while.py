#! number guessing game

num1 = 6
num2 = int(input("Enter a number between one and six. "))
while(num2!=num1):
    print("Nope, that's not it.\n")
    num2 = int(input("Please enter a number."))

print("That's right.")
