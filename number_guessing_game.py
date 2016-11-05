import sys
from random import randint

print "Welcome to the number guessing game!"

target_number = randint(1, 10)
print "I have my number..."

number_guessed = 0
number_of_guesses = 0

while (number_guessed != target_number):
    number_of_guesses += 1
    
    number_guessed = int(raw_input("What is your guess [1-10]?"))

    if number_guessed > target_number:
        print "That's too high. Try again!"
    elif number_guessed < target_number:
        print "That's too low. Try again!"

    if number_of_guesses == 5:
        print "You've ran out of guesses. Tough luck! Better luck next time..."
        sys.exit()
 
print "You got it! Thanks for playing! Number of guesses: {}".format(number_of_guesses)

"""
"""