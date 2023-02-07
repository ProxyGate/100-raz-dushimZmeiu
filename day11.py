############### Blackjack Project ##################### 
def back_you_go():
    """Predlojenie perezapustit' igru + clear ruk"""
    play = input("Nu che eshe razok? y/n ") 
    P_hand.clear()
    C_hand.clear()
    return play
  
def poigraem(play): 
  # play = "y"
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
      if sum(P_hand) > 21 and 11 in P_hand:
        P_hand.remove(11)
        P_hand.append(1)
      print (f"Tvoi karti: {P_hand}, tvoi o4ki: {sum(P_hand)}")
      print (f"U dillera: {C_hand}")
      if sum(P_hand) == 21:
        hit = "n"
      elif sum(P_hand) < 21:
        hit = input("Najmite 'y' chtobi eshe ili 'n' esli sebe: ")
      elif sum(P_hand) > 21:
        hit = "net"
        print("Ha, loh 😤")
        play = back_you_go()      
      
    while hit == "n":
      if sum(C_hand) < 17:
        C_hand.append(random.choice(cards))
      if sum(C_hand) > 21 and 11 in C_hand:
        C_hand.remove(11)
        C_hand.append(1)
      if sum(C_hand) > 16:
        hit = "net"
        print (f"Tvoi karti: {P_hand}, tvoi o4ki: {sum(P_hand)}")
        print (f"U dillera: {C_hand}, o4kov: {sum(C_hand)}")
        if sum(P_hand) > sum(C_hand):
          print("Pobedil, molodets 😁")
          play = back_you_go()
        elif sum(C_hand) > 21:
          print("Pobedil, molodets 😁")
          play = back_you_go()
        elif sum(P_hand) == sum(C_hand):
          print("Ravnaya zaruba 🗿")
          play = back_you_go()
        else: 
          print("Ha, loh 😤")
          play = back_you_go()
    
from replit import clear
from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  

P_hand = []
C_hand = []

play = "y"
play = input("Budesh v bj igrat'? y/n?: ")
poigraem(play)

#===================================================================================================================================================================













































