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
