#RPS Game Update 

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


player_1_score = 0
player_2_score = 0

while True:
  player_1 = input("Player 1 make your choice: ").lower()
  player_2 = input("Player 2 make your choice: ").lower()
  
  if player_1 == "s":
    if player_2 == "p":
     print("Player 1 WINS 🍾")
     player_1_score += 1
     print("Here are your new scores\n",player_1_score,"Player 1's Score""\n",player_2_score,"Player 2's Score")
    elif player_2 == "r":
      print("Player 2 WINS 🥳")
      player_2_score += 1
      print("Here are your new scores\n",player_1_score,"Player 1's Score""\n",player_2_score,"Player 2's Score")
    else:
      print("It's a tie")
      print("Here are your new scores\n",player_1_score,"Player 1's Score""\n",player_2_score,"Player 2's Score")
      continue
  
  elif player_1 == "p":
    if player_2 == "r":
      print("Player 1 WINS 🍾")
      player_1_score += 1 
      print("Here are your new scores\n",player_1_score,"Player 1's Score""\n",player_2_score,"Player 2's Score")
    elif player_2 == "s":
      print("Player 2 WINS 🥳")
      player_2_score += 1 
      print("Here are your new scores\n",player_1_score,"Player 1's Score""\n",player_2_score,"Player 2's Score")
    else:
      print("It's a tie")
      print("Here are your new scores\n",player_1_score,"Player 1's Score""\n",player_2_score,"Player 2's Score")
      continue

  elif player_1 == "r":
    if player_2 == "s":
      print("Player 1 WINS 🍾")
      player_1_score += 1
      print("Here are your new scores\n",player_1_score,"Player 1's Score""\n",player_2_score,"Player 2's Score")
    elif player_2 == "p":
      print("Player 2 WINS 🥳")
      player_2_score += 1
      print("Here are your new scores\n",player_1_score,"Player 1's Score""\n",player_2_score,"Player 2's Score")
    else:
      print("It's a tie")
      print("Here are your new scores\n",player_1_score,"Player 1's Score""\n",player_2_score,"Player 2's Score")
      continue
      
  else:
    print("Invalid input by Player 1")
    continue

  if player_1_score == 3:
    if player_2_score <= 3:
      print("The Game Ends Here player 1 wins")
      print("Here are your final scores\n",player_1_score,"Player 1's Score""\n",player_2_score,"Player 2's Score")
      break

  if player_2_score == 3:
    if player_1_score <= 3:
      print("The Game Ends Here player 2 wins")
      print("Here are your final scores\n",player_1_score,"Player 1's Score""\n",player_2_score,"Player 2's Score")
      exit()

