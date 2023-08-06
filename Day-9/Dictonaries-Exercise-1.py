student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key,values in student_scores.items():
    if(values >= 91 and values <=100):
        student_grades[key] = "Outstanding"
    elif(values >= 81 and values <=90):
        student_grades[key] = "Exceeds Expectations"
    elif(values >= 71 and values <=80):
        student_grades[key] =  "Acceptable"
    else:
        student_grades[key] =  "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)