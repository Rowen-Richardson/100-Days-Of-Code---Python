print("Lets play the guessing game")
print() 

myNumber = 777
tries = 0

while True: 

  guess = int(input("Guess the Number form 0 - 1 000 000?: "))
  
  if guess < 0:
    print("That's not a guess game over")
    exit()
    
  elif guess < myNumber:
    print("try again your guess is to low")
    tries += 1
    print()

  elif guess > myNumber: 
    print("You're geuss is to high")
    tries += 1
    print()
  
  else:
    if guess == myNumber:
      print("YOU HAVE WON THE GAME 🥳")
      break

  if tries == 5:
    print("You've ran out of tries")
    print()
    exit()
  else:
    print("you have used, ",tries, "out of 5 guesses")
    print()
    continue