#Ugadai melodiu
from art import logo
import random
print(logo)
print("\nDobro pojalovat'. Ugadai kakuiu melodiu ot 1 do 100 mi budem proigrivat'")
slojnost = input("Na kakoi slojnosti igraem? ('L'oh/'P'ro) ")
chislo = random.randrange(1, 101)
if slojnost == "L":
  popitki = 10
elif slojnost == "P":
  popitki = 5
else:
  print("POSHEL NAHUI")
while popitki > 0:
  guess_number = int(input(f"Ugadivay eshe {popitki} raz\n  Nu, kakoi nomer? "))
  if guess_number != chislo and popitki == 1:
    print(f"Nu ti i loshara vnature, chel\nNomer to bil, {chislo}")
    break
  if guess_number == chislo:
    print(f"Krasava, otvet - {chislo}")
    popitki = 0
  elif guess_number > chislo:
    print("Oi zamnogo\nDavai eshe")
    popitki -= 1
  elif guess_number < chislo:
    print("Oi zamalo\nDavai eshe")
    popitki -= 1
    
#=================================================================================================================================================================
