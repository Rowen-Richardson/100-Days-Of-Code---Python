"""
adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)
"""

"""
#Multiplication
multi = 3.4 * 6.8
print(multi)

#division
division =  2467/4673
print(division)

#Raising numbers 
raising = 10 ** 2
print(raising)

#remainder
rem = 343 // 100
print(rem)
"""

"""
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
asnwers = round(answer,2)
print("You all owe", asnwers)
"""

print("=Lets play the billing game=")

theBill = float(input("What was your Bill? "))
billSPlit = int(input("How many people are splitting the bill? "))
tip = float(input("How much do you want to tip just number % ? "))
tipPer = (tip/100) * theBill
answer = round((theBill + tipPer) / billSPlit,2)
print("The table will cover R", answer) 