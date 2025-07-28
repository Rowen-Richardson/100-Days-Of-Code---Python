print("Lets see your Grade")
print()

name = input("Hi please tell us your name? ")
gradeMark = 70
score = int(input("What grade did you get? "))
total_per_mark = (score/gradeMark) * 100
total_grade_percentage = round(total_per_mark,2)

if total_grade_percentage < 50:
  print("Hi",name, "you're percentage score was", total_grade_percentage, "meaning you've recieved the following grade")
  print("U")

elif total_grade_percentage < 60:
  print("Hi",name, "you're percentage score was", total_grade_percentage, "meaning you've recieved the following grade")
  print("D")

elif total_grade_percentage < 70:
  print("Hi",name, "you're percentage score was", total_grade_percentage, "meaning you've recieved the following grade")
  print("C")

elif total_grade_percentage < 80:
  print("Hi",name, "you're percentage score was", total_grade_percentage, "meaning you've recieved the following grade")
  print("B")

elif total_grade_percentage < 90:
  print("Hi",name, "you're percentage score was", total_grade_percentage, "meaning you've recieved the following grade")
  print("A")

elif total_grade_percentage <= 100:
  print("Hi",name, "you're percentage score was", total_grade_percentage, "meaning you've recieved the following grade")
  print("A+")

else:
  print("that is not a grade score, Please try Again")
  