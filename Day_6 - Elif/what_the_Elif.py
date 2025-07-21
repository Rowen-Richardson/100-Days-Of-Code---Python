#Adding Elif to the code below 
"""
print("SECURE LOGIN")
username = input("Username > ")
if username == "mark":
  print("Welcome Mark!")
else:
  print("Go away!")
"""

#Added the Elif
"""
print("SECURE LOGIN")
username = input("Username > ")
if username == "mark":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
  print("Go away!")
"""

#Given Code

"""
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "password":
 print("Welcome Mark!")
elif username == "suzanne":
 print("Hey there Suzanne!")
else:
 print("Go away!")
"""

#My updates 

"""
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "password":
 print("Welcome Mark!")
elif username == "suzanne" and password == "Su74nne":
 print("Hey there Suzanne!")
else:
 print("Go away!") 
"""

#Code Errors 

"""
season = input(what is your favorite season?)
if season = "spring"
  print("Ah! The birds are chirping and flowers blooming.")
  elif season == summer:
  print("Catch some sun and cool off with a lemonade.")
elif season == autumn
print("The leaves are changing and the air is crisp. Enjoy!)
      elif season = winter:
      print("Stay warm by the fire and watch the snow fall.")
else: 
print("I don't know that season. Please try again.")
"""

#Fixing the errors 

"""
season = input("what is your favorite season? ")

if season == "spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
  print("Stay warm by the fire and watch the snow fall.")
else: 
  print("I don't know that season. Please try again.") 
"""

#Challange 

print("===Welcome Jedi to the temple===")
print()
print("""In order to access the temple we need a few things""")

print()
userName = input("What is the Jedi's name entering: ")
passWord = input("Enter your secret key [password]: ")

print()
if userName == "luke" and passWord == "Luk3":
  print("Welcome master Luke")
elif userName == "laya" and passWord == "S0l0":
  print("Welcome princess Laya, we are pleased to have you")
elif userName == "hanse solo" and passWord == "S0l4ya":
  print("Welcome you dirty dog, where are my credits")
else:
  print("The seith are not allowed here")