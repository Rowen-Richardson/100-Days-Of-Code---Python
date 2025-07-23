print("=Welcome to your daily Affirmations=")
print()

name = input("Hi what should we call you today? ")
dayWeek = input("Do you mind telling me the day of the week? ")
song = input("Who are we listening to today? ")
colour = input("What's your favourite colour or what are we into today? ")
feeling = input("How are you feeling today? ")
Monday = "I am allowed to ask for what I want and what I need."
Tuesday = "I am content and free from pain."
Wednesday = "I am doing the work that works for me."
Thursday = "I am doing the work that works for me."
Friday = " I am listening and open to the messages the universe has to offer today."
Saturday = "I am loved and worthy."
Sunday = "I am more than my circumstances dictate."

print()

if dayWeek == "Monday" or dayWeek == "monday":
  print("Good day", name, "we wanted to start your", dayWeek, "with a amazing affermation")
  if feeling == "blue" or feeling == "Blue":
    print("Todays Affirmation is: ",Monday)
  elif feeling == "happy" or feeling == "Happy":
    print("Your", dayWeek,"is better than a blue", dayWeek)
  else:
    print("No matter how you're feeling, you showed up. That's enough.")
  
if dayWeek == "Tuesday" or dayWeek == "tuesday":
  print("Good day", name, "we wanted to start your", dayWeek, "with a amazing affermation")
  if feeling == "sad" or feeling == "Sad":
    print("Todays Affirmation is: ",Tuesday)
  elif feeling == "great" or feeling == "Great":
    print("Your", dayWeek,"is better than a your enemies", dayWeek)
  else:
    print("No matter how you're feeling, you showed up. with your jam and we hope", song, "is keeping you motivated")

if dayWeek == "Wednesday" or dayWeek == "wednesday":
  print("Good day", name, "we wanted to start your", dayWeek, "with a amazing affermation")
  if feeling == "tired" or feeling == "Tired":
    print("Todays Affirmation is: ",Tuesday)
  elif feeling == "happy" or feeling == "Happy":
    print("Your", dayWeek,"is better than a some other peopl's ", dayWeek)
  else:
    print("No matter how you're feeling, you showed up. with your jam and we hope", song, "is keeping you motivated and that colour", colour, "sounds amazing")

else:
    print("Good day", name, "we wanted to start your", dayWeek," by telling you that you'd look good in",colour, "and keep that jam on today its",song,"day and nothing can go wrong")

