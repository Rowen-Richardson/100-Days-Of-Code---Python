from getpass import getpass as input

print("Lets Play a game of 🪨 📰 ✂️")
print()

rules = """
1. the rules ar simple each player gets one turn
2. Players need to use the following keys for the game.

S = Scissors
P = Paper
R = Rock

3. Remember to have fun and don't smash the keys.
This is not a game of Uno
"""
print(rules)

player_1 = input("Player 1 make your choice: ")
player_2 = input("Player 2 make your choice: ")

if player_1 == "s":
  if player_2 == "p":
    print("Player 1 WINS 🍾")
  elif player_2 == "r":
    print("Player 2 WINS 🥳")
  else:
    print("It's a tie")

elif player_1 == "p":
  if player_2 == "r":
    print("Player 1 WINS 🍾")
  elif player_2 == "s":
    print("Player 2 WINS 🥳")
  else:
    print("It's a tie")

elif player_1 == "r":
  if player_2 == "s":
   print("Player 1 WINS 🍾")
  elif player_2 == "p":
    print("Player 2 WINS 🥳")
  else:
    print("It's a tie")

else:
  print("Invalid input by Player 1")