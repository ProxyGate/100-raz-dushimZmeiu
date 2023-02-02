#Menyaem bukvi na zaglavnyu 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

imya = input("Nazovi svoe imya, stalker ").lower()
familiya = input("familiya bistro ").lower()

def imya_familiya (a, b): 
  dfamil=""
  c=""
  ename=""
  for i in letters:    
    if a[0] == letters[letters.index(i)]:
      c = letters.index(i)
      ename = a.replace(a[0], letters[c+26])      
  for i in letters:    
    if b[0] == letters[letters.index(i)]:
      c = letters.index(i)
      dfamil = b.replace(b[0], letters[c+26])    
      fullname = ename + " " + dfamil
  return fullname
                      
print(imya_familiya (imya, familiya))

#====================================================================================================================================================================

#Количество дней в году
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return("Leap year.")
      else:
        return("Not leap year.")
    else:
      return("Leap year.")
  else:
    return("Not leap year.")

def days_in_month(year, month):  
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year) == "Leap year.":
    return(29)
  return(month_days[month-1])
    
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

#====================================================================================================================================================================












