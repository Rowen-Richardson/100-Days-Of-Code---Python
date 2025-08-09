import random

print("Welcome to the infinty Dice Roller! 🎲")

sides = int(input("How many sides does your dice have? "))
playAgain = "yes"

def rollDice(sides):
    print("Rolling the dice...")
    print("You rolled a", random.randint(1, sides))
    
while playAgain == "yes":
        rollDice(sides)
        playAgain = input("Do you want to roll again? (yes/no) ")
        if playAgain.lower() != "yes":
            print("Thank you, Goodbye 🥳")
            exit()

rollDice(sides)
