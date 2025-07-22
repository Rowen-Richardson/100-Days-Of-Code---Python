#Testing code
"""
tvShow = input("What is your favorite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
  else:
    print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
"""

#Changing Tested code 

"""
tvShow = input("What is your favorite tv show? ")
if tvShow == "Rick and Morty":
  print("Ugh, why?")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter == "Grandpa Rick":
    print("Right answer")
  else:
    print("Nah,Rick's the greatest")
elif tvShow == "Eureka":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
"""

#Broken code 
"""
tvShow = input("What is your favourite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favourite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
else:
  print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
"""

#Fixing the code
"""
tvShow = input("What is your favourite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favourite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
  else:
    print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
"""

#broken code
"""
order = input(What would you like to order: pizza or hamburger? ")
if order = "hamburger":
print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
  print("You got it.")
else: 
    print("No cheese it is.")
elif order == pizza:
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings = "yes"
    print("We will add pepperoni.")
else:
  print"Your pizza will not have pepperoni.")
"""

#Fixing the code
"""
order = input("What would you like to order: pizza or hamburger?")
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")
  else: 
    print("No cheese it is.")
elif order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")
  else:
    print("Your pizza will not have pepperoni.")
"""

#True Fans

print("Are you a true Star Wars fan")

tvShow = input("Whats your favourite Star Wars show? ")

if tvShow == "bad batch":
  print("You maybe on the right track")
  favouriteCharacter = input("And who's your favourit character? ")
  if favouriteCharacter == "Echo":
    print("We have a true fan")
  elif favouriteCharacter == "Omega":
    print("Are you a clone or something")
  else:
    print("They are also cool but Echo's the best...")

elif tvShow == "rebels":
  print("You've made the right choice Jedi")
  favouriteCharacter2 = input("And don't cheat who's your all time favourit character? ")
  if favouriteCharacter2 == "ezra":
    print("You are a Jedi after my heart")
  else:
    print("What do you possible see in them...")

else:
  print("Above all shows you choose that one I can't belive you")