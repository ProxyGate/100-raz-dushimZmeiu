############### Blackjack Project #####################

def poigraem():  
  play = "y"
  while play == "y":
    clear()
    print(logo)
    P_hand.append(random.choice(cards))
    P_hand.append(random.choice(cards))
    print (f"Tvoi karti: {P_hand}, tvoi o4ki: {sum(P_hand)}")
    C_hand.append(random.choice(cards))
    print (f"U dillera: {C_hand}")
    hit = "n"
    hit = input("Najmite 'y' chtobi eshe ili 'n' esli sebe: ") 
    while hit == "y":
      P_hand.append(random.choice(cards))
      print (f"Tvoi karti: {P_hand}, tvoi o4ki: {sum(P_hand)}")
      print (f"U dillera: {C_hand}")
      hit = input("Najmite 'y' chtobi eshe ili 'n' esli sebe: ")
    
    while hit == "n":
      if sum(C_hand) < 17:
        C_hand.append(random.choice(cards))
      if sum(C_hand) > 16:
        hit = "net"
        print (f"Tvoi karti: {P_hand}, tvoi o4ki: {sum(P_hand)}")
        print (f"U dillera: {C_hand}, o4kov: {sum(C_hand)}")
        if sum(P_hand) > sum(C_hand):
          print("Pobedil, molodets 😁")
          play = input("Nu che eshe razok? y/n ") 
          P_hand.clear()
          C_hand.clear()
        elif sum(C_hand) > 21:
          print("Pobedil, molodets 😁")
          play = input("Nu che eshe razok? y/n ") 
          P_hand.clear()
          C_hand.clear()
        elif sum(P_hand) == sum(C_hand):
          print("Ravnaya zaruba 🗿")
          play = input("Nu che eshe razok? y/n ") 
          P_hand.clear()
          C_hand.clear()
        else: 
          print("Ha, loh 😤")
          play = input("Nu che eshe razok? y/n ") 
          P_hand.clear()
          C_hand.clear()
    

from replit import clear
from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  

P_hand = []
C_hand = []
# play = input("Budesh v bj igrat'? 'y', 'n'? :")
play = "y"

poigraem()

#===================================================================================================================================================================













































