def rollDice():
    import random
    dice = random.randint(1,6)
    print("Your dice roll is:",dice)

rollDice()

for i in range(100):
  rollDice()