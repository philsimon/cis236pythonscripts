#say_my_name. 
counter = 1 #this is the counter that I metnioned before
guess = input("Say my name. ")
name = "Heisenberg"
while (guess != name):
    guess = input("Try again. ")
    counter = counter + 1 
if counter == 1: #note the double == here.
    print("\nYou are *!##%! right.", "It took you", counter, "try.")
elif counter in [2, 3, 4, 5]:
    print("\nYou are *!##%! right.", "It took you", counter, "tries.")
else: 
    print("\n\tSeriously? You don't watch this show at all.")
