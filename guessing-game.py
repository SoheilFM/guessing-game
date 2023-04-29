import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Set the maximum number of guesses
max_guesses = 10

# Keep track of the number of guesses
guesses = 0

# Loop until the player guesses the correct number or runs out of guesses
while guesses < max_guesses:
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

# If the player runs out of guesses, display the correct number
if guesses == max_guesses:
    print("Sorry, you ran out of guesses. The number was", number)