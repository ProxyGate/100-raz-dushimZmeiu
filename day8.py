#Количество банок краски
#Write your code below this line 👇

import math

def paint_calc(height, width, cover):
  itogo = math.ceil((height * width) / cover )

  print (f"banok {itogo}")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#==================================================================================================================================================================

#Provekra na prostoe chislo
#Write your code below this line 👇

def prime_checker (number):
  if n>0:
    if n % 5 != 0 or n == 5:
      if n % 3 != 0 or n == 3:
        if n % 2 != 0 or n == 2:    
          print("tvoe chislo prostoe")
        else:
          print("tvoe chislo sostavnoe")
      else:
        print("tvoe chislo sostavnoe")    
    else:
      print("tvoe chislo sostavnoe")
  else:
    print("idi naher da s takimi prikolami")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

#==================================================================================================================================================================


