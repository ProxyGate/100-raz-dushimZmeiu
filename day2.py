#Cуммируем первые две цифры двухзначного числа
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

print(int(two_digit_number[0]) + int(two_digit_number[1]))

####################################
#Write your code below this line 👇

# =============================================================================================================================================

# Рассчет индекса массы тела
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = int(weight) / float(height) ** 2
print("Your BMI = " + str(int(BMI)))

# =============================================================================================================================================

#Cколько тебе осталось жить
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

ULivedMonth = int(age) * 12
ULivedWeeks = int(age) * 52
ULievedDays = int(age) * 365

ULeftMonth = 90*12 - ULivedMonth
ULeftWeeks = 90*52 - ULivedWeeks
ULeftDays = 90*365 - ULievedDays

print(f"Вам осталось {ULeftDays} дней, {ULeftWeeks} недель, {ULeftMonth} месяцев жить (при расчете что вы сдохнете в 90)")

# years = 90 - int(age)
# months = years12
# weeks = years52
# days = years*365

# print (f"У тебя ещё есть {days} дней, {weeks} недель или {months} месяцев")

# =============================================================================================================================================

#Калькулятор чаевых
print("Здарова, додсы, давайте посчитаем как поделить счет поровну на всех\n")
money = float(input("Ну че, сколько там денег то?\n"))
tip = 0.01 * int(input("Сколько % хотите отстегнуть с барского плеча? (10,12,15)\n"))
people = int(input("Скок вас ваще?\n"))

MoneyPerPerson = round((money * (1+tip) / people), 2) 

print(f"Ладно, давайте каждый по {MoneyPerPerson} скидывается и небольшой расход")

# =============================================================================================================================================
