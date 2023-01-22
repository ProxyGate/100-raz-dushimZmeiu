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


