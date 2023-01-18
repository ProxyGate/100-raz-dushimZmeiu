# Проверка числа на четность
# 🚨 Don't change the code below 👇
number = int(input("Какое число вы хотите проверить "))
# 🚨 Don't change the code above 👆

if number % 2 == 1:
  print ("Твое число нечетное")
else:
  print ("Твое число четное")

#===================================================================================================================================================

# Рассчет индекса массы тела
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = int(weight) / float(height) ** 2

if BMI < 18.5:
  print("Your BMI = " + str(BMI) + ", you are underweight")
elif BMI < 25:
  print("Your BMI = " + str(BMI) + ", you are normal weight")
elif BMI < 30:
  print("Your BMI = " + str(BMI) + ", you are overweight")
elif BMI < 35:
  print("Your BMI = " + str(BMI) + ", you are obese")
else:
  print("Your BMI = " + str(BMI) + ", you are clinically obese")

# =============================================================================================================================================

#Давайте поможем Даше узнать високосный ли сейчас год
# 🚨 Don't change the code below 👇
year = int(input("Какой год хотите проверить? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 != 0:
   print ("Годик то не високосный")
else:
  if year % 400 == 0:
    if year % 4 == 0:
      print ("Годик то високосный")
  else: 
    if year % 100 == 0:
      if year % 4 == 0:
        print ("Годик то не високосный")
    else:
      print ("Годик то високосный")
        
# =============================================================================================================================================

#Выбор пиццы
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "s" or size == "S":
  bill = 15
  if add_pepperoni == "y" or add_pepperoni == "Y":
    bill += 2
if size == "m" or size == "M":
  bill = 20
  if add_pepperoni == "y" or add_pepperoni == "Y":
    bill += 3
if size == "l" or size == "L":
  bill = 25
  if add_pepperoni == "y" or add_pepperoni == "Y":
    bill += 3

if extra_cheese == "y" or extra_cheese == "Y":
    bill += 1

print (f"Your total bill = {bill}")

# =============================================================================================================================================

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_count = 0
name2_count = 0

name1_low = name1.lower()
name2_low = name2.lower()
name1_count += name1_low.count("t")
name1_count += name1_low.count("r")
name1_count += name1_low.count("u")
name1_count += name1_low.count("e")

name2_count += name1_low.count("l")
name2_count += name1_low.count("o")
name2_count += name1_low.count("v")
name2_count += name1_low.count("e")

name1_count += name2_low.count("t")
name1_count += name2_low.count("r")
name1_count += name2_low.count("u")
name1_count += name2_low.count("e")

name2_count += name2_low.count("l")
name2_count += name2_low.count("o")
name2_count += name2_low.count("v")
name2_count += name2_low.count("e")

final_nubmer = int(str(name1_count) + str(name2_count))
if final_nubmer < 10 or final_nubmer > 90:
  print (f"Your score is {final_nubmer}%, you go together like coke and mentos")
elif int(final_nubmer) > 40 and int(final_nubmer) < 50:
  print (f"Your score is {final_nubmer}%, you are alright together")
else:
  print (f"Your score is {final_nubmer}%")

#   print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# name = (name1 + name2).lower()
# x = (
#   name.count("t") + 
#   name.count("r") + 
#   name.count("u") + 
#   name.count("e"))

# y = (
#   name.count("l") + 
#   name.count("o") + 
#   name.count("v") + 
#   name.count("e")
# )

# percent = int(str(x) + str(y))
# print(percent)

# if percent <= 10 or percent >= 90:
#   print (f"Ваш индекс любви составляет {percent} %, вы подходите друг другу как кола и ментос")
# elif percent >=40 and percent <= 50:
#   print (f"Ваш индекс любви составляет {percent} %, вы хорошая пара")
# else:
#   print (f"Ваш индекс любви составляет {percent} %")
  
# =============================================================================================================================================

