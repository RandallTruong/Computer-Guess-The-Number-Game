import random

def main():
   play_again = ""
   # While loop until the user does not want to play anymore
   while play_again != "n":
      # Call the check number function
      number = check_number()
      # Call the play game function and pass the number variable
      play_game(number)
      # Call the check play again function to see if user would like to play again
      play_again = check_play_again()
   # End of game
   print("Thanks for playing")

# Function checks if user would like to play again and validates input
def check_play_again():
    while True:
        options = ["y", "n"]
        play_again = input("Would you like to play again...Y or N: ").lower()
        if play_again in options:
            return play_again
        else:
            print("Invalid entry please try again")

# Function checks if input is a number and between 1 - 100
def check_number():
    while True:
        number = input("Please provide a number between 1 and 100: ")
        if number.isdigit():
            number = int(number)
        else:
            print("Invalid entry please try again")
            continue
        if 1<= number <= 100:
            return number
        else:
            print("Invalid entry please try again")

# Function plays the game
def play_game(number):
    game = True
    min_number = 1
    max_number = 100
    guess = generate_random_number(min_number, max_number)
    attempts = 1
    # If computer guessed incorrectly, randomly guess again
    while game:
        # If computer guess is above, then adjust the next guess to be lower
        if guess > number:
            print(f"The computer guess {guess} and it was above.")
            max_number = guess - 1
            guess = generate_random_number(min_number, max_number)
            attempts += 1

        # If computer is below, then adjust the next guess to be higher
        elif guess < number:
            print(f"The computer guess {guess} and it was below")
            min_number = guess + 1
            guess = generate_random_number(min_number, max_number)
            attempts += 1

        # If computer guessed correctly, they win, print number of attempts, end the game
        else:
            print(f"The computer guess {guess} and it was correct")
            print(f"It took {attempts} attempts")
            game = False

# Function generates a random number and then returns the number
def generate_random_number(min_number, max_number):
    random_number = random.randint(min_number, max_number)
    return random_number

if __name__ == "__main__":
    main()