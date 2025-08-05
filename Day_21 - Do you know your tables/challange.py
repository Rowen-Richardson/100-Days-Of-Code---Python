print("Lets test your tables knowledge")
print()

rules = """
Rules are simple:

Let's see if you know your tables.
1. You can choose your number.
2. The range has been set for you starting at 1 and ending at 10.
3. You will see if you know your maltiple tables 

"""

print(rules)
print()

number = int(input("Enter your number and lets see if you know your times tables: "))
print()

points = 0

for i in range(1, 11):
    result = number * i
    print(i, "x", number)
    if result == int(input("What your answer?: ")):
        print("Yes you are correct 🥳")
        points += 1
    else:
        print("Nope, the answer is", result, "😢")
print()

if points == 10:
    print("Wow you got all the answers correct! You are a times table master! 🏆")
else:
    print("You got", points, "out of 10 correct. Keep practicing and you will get there! 💪")