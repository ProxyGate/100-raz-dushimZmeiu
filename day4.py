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

#Камень ножницы бумага
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

#kamanoja = [rock, paper, scissors]

igrok = int(input("Ну что, сыграем в камень(1) ножницы(2) бумага(3), выбирай цифру\n"))

if igrok == 1:
  print(rock)
elif igrok == 2:
  print(paper)
elif igrok == 3:
  print(scissors)
else:
  print("Такого нет варианта, дружок")
  
ai = random.randint(1, 3)

if ai == 1:
  print(f"ИИ выбирает: \n {rock}")
elif ai == 2:
  print(f"ИИ выбирает: \n {paper}")
elif ai == 3:
  print(f"ИИ выбирает: \n {scissors}")

if ai == igrok:
  print("\n Ничья")
elif ai == 1 and igrok == 2:
  print("\n Победа твоя")
elif ai == 3 and igrok == 1:
  print("\n Победа твоя")
elif ai == 2 and igrok == 3:
  print("\n Победа твоя")
elif igrok == 1 and ai == 2:
  print("\n Попробуй снова")
elif igrok == 3 and ai == 1:
  print("\n Попробуй снова")
elif igrok == 2 and ai == 3:
  print("\n Попробуй снова")

#=====================================================================================================================================================================

