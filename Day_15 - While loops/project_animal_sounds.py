exit = ""

while exit != "yes":
  animal = input("What animal would you like to hear? ")
  if animal == "cow":
    print("Well a Cow goes Mooo.")
  else:
    if animal == "dog":
      print("A dog goes woof woof.")
    elif animal == "cat":
      print("Do cats even make a sound? I guess cats go meaow")
    elif animal == "lesser spotted lemur":
        print("This is a funny one cause the Lesser Spotted Lemur goes awooga")
    else:
      print("That's not an animal silly")
  exit = input("Would you like to EXIT?: ")