#Step 1 
# import random

# word_list = ["aardvark", "baboon", "camel"]

# randw = random.choice(word_list)

# randl = input("Угадайте какая буква есть в слове\n").lower()

# for i in range (0, len(randw)):
#   if randl == randw[i]:
#     print ("Ugadal")
#   else:
#     print("Neugadal")

import random
import os

word_list = ["aardvark", "baboon", "camel"]
randw = random.choice(word_list)
print(f'The solution is {randw}.')
display = ["_"] * len(randw)

while (display) != (randw):
  randl = input("Угадывай какая буква есть в слове: ").lower()
  for i in range (0, len(randw)):
    if randl == randw[i]:
      print ("Ugadal")
      display[i] += randw[i]
      print(display)  
    else:
      display[i] = "_"
      print(display)  
  print(display)   

# if display[i] not in display:
#   print("lol")
  
# while (display) != (randw):
# randl = input("Угадывай какая буква есть в слове: ").lower()
# for i in range (0, len(randw)):
#   if randl == randw[i]:
#     print ("Ugadal")
#     display.append(randw[i])
#     print(display)  
#   else:
#     display.append("_")
#     print(display)  
# print(display) 

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
