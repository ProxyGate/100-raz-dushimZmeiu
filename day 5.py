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
