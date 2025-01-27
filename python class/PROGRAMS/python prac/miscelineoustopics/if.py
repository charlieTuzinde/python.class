# from random import randint
# num = randint(1,10)
# guess = eval(input('Enter your guess: '))
# if guess == num:
#   print ('You got it!')
import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Ask the user for input
user_input = input("Guess a number between 1 and 10: ")

try:
    # Convert user input to an integer
    user_guess = int(user_input)

    # Check if the user's guess matches the random number
    if 1 <= user_guess <= 10:
        if user_guess == random_number:
            print(f"Congratulations! You guessed it. The number was {random_number}.")
        else:
            print(f"Sorry, the correct number was {random_number}.")
    else:
        print("Please enter a number between 1 and 10.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
