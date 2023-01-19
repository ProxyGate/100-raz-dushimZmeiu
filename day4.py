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

#Карта сокровищ
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
stolbets = int(position[0]) - 1
stroka = int(position[1]) - 1

if stroka == 0:
  row1.insert(stolbets, "x ") 
  row1.pop(stolbets+1)
elif stroka == 1:
  row2.insert(stolbets, "x ") 
  row2.pop(stolbets+1)
elif stroka == 2:
  row3.insert(stolbets, "x ") 
  row3.pop(stolbets+1)
else:
  print("Incorrect number")

# row = locals()["row" + position[1]]     #определяем строку
# row[int(position[0])-1] = 'X'         #заменяем позицию в строке
# # print (row[int(position[0])-1])       #определяем и печатаем позицию в строке 

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

#=====================================================================================================================================================================
