#Exercise
"""
while True:
  print("This program is running")
print("Aww, I was having a good time 😭")
"""
"""
while True:
  print("This program is running")
  goAgain = input("Go again?: ")
  if goAgain == "no":
    break
print("Aww, I was having a good time 😭")
"""

#Common errors
"""
counter = 0
while true: #the error is the T in True it needs to be a capitall
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")
"""
"""
counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
addAnother = input("Add another? ") # a portion of the code was outside of the loop
if addAnother == "no":
  break
print("Bye!")
"""

#Broken Code
"""
while true:
  color = input("Enter a color: ")
  if color = "red":
  break
  else:
    print("Cool color!")
print("I don't like red")
"""

#my fix
"""
while True:
  color = input("Enter a color: ")
  if color == "red":
    break
  else:
    print("Cool color!")
print("I don't like red")

"""