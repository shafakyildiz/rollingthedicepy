# Produce the random dice numbers

from random import randrange

# Take input from the user

dice = input("If you want the roll the dice type 'dice': \n ")

while dice == "dice":

    num1 = randrange(1,7)
    num2 = randrange(1,7)
    print(num1, num2)
    dice = input("If you want the roll the dice type 'dice': \n ")

if dice != "dice":
        print("The program has been terminated!")