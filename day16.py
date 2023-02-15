#coffe machine with classes
while True:
  choice = input("What do you want? latte/espresso/cappuccino/ ")
  if choice == "latte" or choice == "espresso" or choice == "cappuccino":
    if coffemaker.is_resource_sufficient(menu.find_drink(choice)):
      if money_machine.make_payment((menu.find_drink(choice)).cost):
        coffemaker.make_coffee(menu.find_drink(choice))      
  elif choice == "report":
    money_machine.report()
    coffemaker.report()
  elif choice == "off":
    break
  else:
    print(f"poshel nahui i tvoi {choice} toje")
    
    #================================================================================================================================================================
    
