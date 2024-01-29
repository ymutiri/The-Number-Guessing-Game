"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""


import random
# Import the random module.

# Create the start_game function.
# Write your code inside this function.


#This Function used to generate two numbers to be used with random.randint method
def get_random_numbers():
    pass



def start_game():
    print("#####################################")
    print("#                                   #")
    print("# Welcome to a number guessing game #")
    print("#                                   #")
    print("#####################################")
    random_number = random.randint(1, 10)
    user_guess = None
    tries = 0
    guesses = 5
    while True:
        #Generat a random number from 1 to 10, and store the return of randint in random_number variable

        #Get the user input as integer
        try:
            user_guess = int(input("Guess the number > "))
            if user_guess < 0 or user_guess > 10:
                print("Input number is out of range!!!")
        except ValueError as err:
            print(f"Integer is the only allowed input!!!!")
            continue
        if user_guess > random_number:
            print("Too High")
            tries += 1
        elif user_guess < random_number:
            print("To Low")
            tries += 1
        elif user_guess == random_number:
            print("You guessed {}".format(user_guess))
            print(f"You've guessed the number {random_number} after {tries} attempts")

            user_input = input("Would you like to play again ? (y/n) ")
            if user_input.lower() == 'y':
                random_number = random.randint(1, 10)
                user_guess = None
                tries = 0
                continue
            else:
                print("GAME OVER...")
                break







start_game()
#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
