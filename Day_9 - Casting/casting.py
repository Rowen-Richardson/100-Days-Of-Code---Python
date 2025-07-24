#Broken code ints
"""
myScore = input("Your score: ")
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
"""
#Fixed code int
"""
myScore = int(input("Your score: "))
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
"""

#Working with Floats
"""
myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")
"""
#Code Challenge fix the bugs
"""
score = input("What was your score on the test?"))
if score >= 80
  print("Not too shabby")
elif score > "70":
  print("Acceptable.")
else:
print("Dude, you need to study more!")
"""

#Fixing the bugs
"""
score = int(input("What was your score on the test?"))
if score >= 80:
  print("Not too shabby")
elif score > 70:
  print("Acceptable.")
else:
  print("Dude, you need to study more!")
"""

#Generation Generator
print("Find out your Generations name")
print()

name = input ("Hi what should we call you [Name]? ")
genName = int(input("""Type in the year you where born and we'll tell you which generation you belong to!!! """))
print()

if genName >= 1925:
  print("You're a Traditionalist", name)
elif genName >= 1947 and genName <= 1964:
  print("Welcome Baby Boomer", name)
elif genName >= 1965 and genName <= 1981:
  print("Gen X marks the spot for you",name)
elif genName >= 1982 and genName <= 1995:
  print("Another Millenial gracesses us. Welcome", name)
elif genName >= 1996 and genName <= 2015:
  print("Welcome you finally made it you're a Gen Z baby", name)
else:
  print("We haven't found your generation yet please try again😭")