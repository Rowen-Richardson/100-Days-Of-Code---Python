def print My Name(): #This line would cause a syntax error as you cannot have spaces in function names or use the print statement in this way.
  print("My Name is David")

print My Name() # This line would also cause a syntax error for the same reason as above.

def countToFive: #missing parentheses would cause a syntax error.
    for i in range(1, 6):
        print(i)

countToFive()

def countToFive():
  for i in range(1, 6):
    print(i)

  countToFive() # This line would cause an indentation error as it is incorrectly indented.