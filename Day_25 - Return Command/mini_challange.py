import random

print("Welcome to the Health Points Dice Roller! 🎲")
print()
Rules = """
Welcome to the health point chair 

There's only one Rule and that's to 
have fun! and use your name or anyones 
to see how much health they have

"""
print(Rules)
print()


sixSides = 6
eightSides = 8
playAgain = "yes"

def rollDice(sixSides,eightSides):
    userName = input("What is your name? ")
    print("Rolling the dice...")
    playerHealth = random.randint(1, sixSides) * random.randint(1, eightSides)
    print(userName,"You Rolled and your health points are", playerHealth,"HP")
    return playerHealth
while playAgain == "yes":
        rollDice(sixSides, eightSides)
        playAgain = input("Do you want to roll again? (yes/no) ")
        if playAgain.lower() != "yes":
            print("Thank you, Goodbye 🥳")
            exit()

rollDice(sixSides, eightSides)
print(rollDice(sixSides, eightSides))  # This will print the health points rolled