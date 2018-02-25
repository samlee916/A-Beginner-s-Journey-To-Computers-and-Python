#Python Example 2

#conditional statements
favoritelanguage = "python"

if favoritelanguage == "python":
    print("Yes it is.")
else:
    print("No it isn't.")

#else if statement
favoriteanimal = "tiger"
if favoriteanimal == "lion":
    print("Lions are not my favorite animal.")
elif favoriteanimal == "snake":
    print("Snakes are not my favorite animal.")
else:
    print("Tigers are my favorite animal.")

#more if, else, and else if statements
if 10 < 15:
    print("True.")
elif 10 == 15:
    print("False.")
elif 10 != 15:
    print("True.")

#nested conditionals
100 != 100
if 100 != 100:
    print("False.")
else:
    if 100 == 100:
        print("True.")
    else:
        print("False.")

for i in range(10):
    print("i is now", i)

#for loops
for birthdaycard in ["Anna", "Hanna", "Sanna"]:
    birthdaycard = "Hello " + birthdaycard + ", I wish you a happy birthday."
    print(birthdaycard)

for trainticket in ["$8.50", "$10.50", "$12.50", "$14.50", "$16.10"]:
    trainticket = "That will cost you " + trainticket + " Ma'am/Sir."
    print(trainticket)

for p in range (0,5):
    print("Politics is boring.", p)

for a in range(0,10):
    print("Don't steal my food!!!", a)

for d in range(20):
    print(1, "\t", 5)

for w in range(10):
    print(w, "\t", 2**w)

#while loops
#number = 0;
#question = "What is my name? "

#while 0 != 1:
#    number = input(question)

#a small guessing game
import random

integer = random.randint(1,30)
amountofguesses = 0

while amountofguesses < 5:
    print("Guess a number between 1 and 30:")
    guess = input()
    guess = int(guess)
    amountofguesses += 1

    if guess < integer:
          print("Unfortunately, you are wrong")
    if guess > integer:
          print("Unfortunately, you are wrong")
    if guess == integer:
          break
    if guess == integer:
          print("You guessed the number in " + str(amountoftries) + "tries.")
    else:
        print("What a bummer! The correct number was " + str(integer))
          



          
        
    










    
