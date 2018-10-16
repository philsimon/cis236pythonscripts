#album picker with error

import random

album_list_one = ["2112", "Hemispheres" "Moving Pictures", "Roll the Bones"]
album_list_two = ["FEAR", "Brave", "Clutching at Straws", "Marbles", "Anoraknophobia"]
album_list_three = ["The Incident", "Deadwing", "Anethsesize", "Lightbulb Sun", "Signify", "Stupid Dream"]

one_length = len(album_list_one)
two_length = len(album_list_two)
three_length = len(album_list_three)

rand1 = random.randint(0, one_length)
rand2 = random.randint(0, two_length)
rand3 = random.randint(0, three_length)

message = album_list_one[rand1] + ", " + album_list_two[rand2] + ", " + album_list_three[rand3]

print("Pick some really good albums for me: \n\t\t", message)
