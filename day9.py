#Рейтинги Гарри Потного (словарь)

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
  
student_grades = {}
for i in student_scores:  
  if student_scores[i] < 71:
    student_grades[i] = "fail"
  elif student_scores[i] < 81:
    student_grades[i] = "acceptable"
  elif student_scores[i] < 91:
    student_grades[i] = "exceeds Expectations"
  elif student_scores[i] <= 100:
    student_grades[i] = "outstanding"
  # print(i)
  # print (student_scores[i])

print(student_grades)

#=====================================================================================================================================================================



