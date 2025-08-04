print("Lets play a game called 'What's the range?'")
print()

print("In this game you would be given a set of 3 inputs and a range of numbers will be generated based on those inputs.")
print()

rules = """
The rules are simple:

1. You will choose a number to start with.
2. You'll choose a number to end with.
3. Finally, you'll choose a step value to determine the increment or decrement.
4. The program will generate a range of numbers based on your inputs.
5. If the start number is greater than the end number, the program will count down.
6. If the start number is less than the end number, the program will count up.
7. If the start number is equal to the end number, the program will print that number only. 
8. The step value determines how much to increment or decrement the numbers.
"""

print(rules)
print()

s = int(input("What number do you want to start with?: "))
e = int(input("What number do you want to end with?: "))
st = int(input("What step value do you want to use?: "))

for i in range(s, e, st):
    print(i)

print()