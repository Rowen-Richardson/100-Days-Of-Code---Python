print("Lets find out how many minutes in a year")
print()

year_we_have = int(input("""Is it a Leap Year [366] or A Normal Year [365]? 
Please answer in number values: """))

year_in_months = 12
days_in_months = 31
hours_in_day = 24
min_in_hours = 60
sec_in_min = 60

year_min = year_we_have * hours_in_day * min_in_hours
print()

if year_we_have == 365:
  print("We have a total of",year_min,"minutes in a year. Its just a normal year😔😭")
elif year_we_have == 366:
  print("We have a total of",year_min,"minutes in a year which means we have a Leap year 🥳🎇🍾")
else:
  print("""Are you normal or are we going crazy?
  Please do try again""")