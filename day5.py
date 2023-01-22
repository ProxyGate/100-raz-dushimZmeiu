# Средняя высота учащихся
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

total_height = 0
total_PEPOL = 0

for a in student_heights:
  total_height += a
  total_PEPOL += 1
avg_height = round(total_height/total_PEPOL)
print(f"Average student height = {avg_height}")

#=======================================================================================================================================================================

#Воспроизведение МАКС фунции
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_number = 0
for a in student_scores:
  if a > max_number:
    max_number = a

print(f"Max number = :{max_number}")

#=======================================================================================================================================================================

#Сумма всех четных до ста включая 1
#Write your code below this row 👇
b = 1
for a in range (2, 101, 2):
   b += a
print(f"Total number is {b}")

#=======================================================================================================================================================================

#Детская игра FizzBuzz 
#Write your code below this row 👇
for a in range(1,101):
  if a % 3 == 0 and a % 5 == 0:
    a = "fizz buzz"
  elif a % 3 == 0:
    a = "fizz"
  elif a % 5 == 0:
    a = "buzz"
  print (a)

#=======================================================================================================================================================================

#Генератор паролей (рандомный(совсем))
#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
a = 0
b = []
c = ""
d = ""
for a in range(0, nr_letters): 
  r_letter = random.choice(letters)
  b += r_letter
for a in range(0, nr_numbers): 
  r_number = random.choice(numbers)
  b += r_number
for a in range(0, nr_symbols): 
  r_symbol = random.choice(symbols)
  b += r_symbol

for a in range(0, len(b)):
  r_string = random.choice(b)
  d += r_string
  b.remove(r_string)

c = ''.join(map(str, d))
print(f"Your password: \n{c}\n(Dont trust password generators st00pid!)")

#=======================================================================================================================================================================
#EBANINA
# #Password Generator Project
# import random

# letters = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
#     'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
#     'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
# ]
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# passw = str()
# pass_len = nr_letters + nr_symbols + nr_numbers
# lc = 0
# sc = 0
# nc = 0

# currlen = 0
# for i in  range(0, pass_len):
#     x = random.randint(1, 3)
#     if ((x == 1) or ((nc == nr_numbers) and (sc == nr_symbols))) and (lc < nr_letters):
#       l = random.randint(0, len(letters) - 1)
#       passw = passw + letters[l]
#       print(f"x - {x}; lc - {lc}; l - {l}")
#       lc += 1
#     elif ((x <= 2) or (sc == nr_symbols)) and (nc < nr_numbers):
#       n = random.randint(0, len(numbers) - 1)
#       passw = passw + numbers[n]
#       print(f"x - {x}; nc - {nc}; n - {n}")
#       nc += 1
#     elif (x <= 3) and (sc < nr_symbols):
#       s = random.randint(0, len(symbols) - 1)
#       passw = passw + symbols[s]
#       print(f"x - {x}; sc - {sc}; s - {s}")
#       sc += 1
#    # currlen = lc + nc + sc


# print(f"len - {pass_len}; len(p) - {len(passw)}")
# print(f"Parol - {passw}") 

#=======================================================================================================================================================================

