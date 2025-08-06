"""
import random

myNumber = randint(1, 100) it needs the random module to be imported inline of the code
print(myNumber)

"""
"""
import random

myNumber = random.randint(1, 100)
for i in range(10): #this prints 10 times the same random number
  print(myNumber)
  
"""

import random

myNumber = random.randint(1, 100)
for i in range(10):
  ran = myNumber + i
  print(ran)  # This will print a different number each time, incrementing by i