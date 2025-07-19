print("""=  Welcome to The wacky Jedi Story  =
where every question matters and the wacker the answer
the better the story""") 
print()

name = input("Welcome Jedi could you tell me your name:  ")
house = input("What is your favourit household iteam? ")
dislike = input("Whats the one thing or person you don't like? ")
pet = input("what kind of pet or pets do you have? ")
transport = input("""Whats your favoirt mode of transport be specific 
i.e if its a car you'll say Honda Acord: """)
planet = input("Give us a name of a family memeber, friend or person: ")
food = input("What's your favourite food? ")
activity = input("What activity or chore do you dislike? ")
print()

print("""Welcome to the wacky but mazing world of""", "\033[32m",activity, planet, food,"\033[0m" ,"where you my young Jedi", "\033[34m",name,"\033[0m")
print("shall be fighting in the great","\033[31m",planet, food,"\033[0m","war which has lasted for ages")
print("You as our new Jedi shall arive in your new spaceship called", "\033[33m",transport,"\033[0m")
print("with your trusted sidekick","\033[35m" ,pet, dislike, "\033[0m","and your strange but useful","\033[30m",house,"\033[0m","light saber")