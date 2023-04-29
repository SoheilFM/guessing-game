import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Keep track of the number of guesses
guesses = 0

# Loop until the player guesses the correct number
while True:
    # Get a guess from the player
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1
    
    # Check if the guess is correct
    if guess == number:
        print("Congratulations, you guessed the number in", guesses, "guesses!")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")