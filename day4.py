#Генератор подброса монетки
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random
print("Флип, подбрось монетку")
monetka = random.randint(1,2)
if monetka == 1:
  print("У вас орел")
elif monetka == 2:
  print("У вас решка")

#=====================================================================================================================================================================

#Кто из компании платит за счет
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
number_of_people = len(names)
kto = random.randint(1,number_of_people)
kto_na_samom_dele = kto - 1
print(f"Za s4et platit {names[kto_na_samom_dele]}")

#=====================================================================================================================================================================


