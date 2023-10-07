import random

class NumberGuessingGame:
    def __init__(self, low, high, max_attempts):
        self.low = low # lowest number of your choice
        self.high = high # highest number of your choice
        self.max_attempts = max_attempts # maximum number of attempts
        self.number_to_guess = random.randint(low, high) # random number between low and high
        self.attempts = 0 # number of attempts

    def guess(self, user_guess):
        self.attempts += 1 # increment number of attempts

        if user_guess == self.number_to_guess: # if user guess is correct
            return f"Congratulations! You guessed the correct number {self.number_to_guess} in {self.attempts} attempts." # return this message
        elif user_guess < self.number_to_guess: # if user guess is lower than the number to guess
            return "Too low. Try again." # return this message
        else: # if user guess is higher than the number to guess
            return "Too high. Try again." # return this message
        

    def play(self): # play function
        print("Welcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between {self.low} and {self.high}.")
        print(f"Can you guess what it is in {self.max_attempts} attempts?") 

        while self.attempts < self.max_attempts:
            try:
                print(f"Guess number {self.attempts + 1}")
                if self.attempts + 1 == self.max_attempts:
                    print("This is your last attempt.")
                user_input = int(input("Enter your guess: "))
                result = self.guess(user_input)
                print(result)
                print("\n")

                if user_input == self.number_to_guess:
                    break

            except ValueError:
                print("Invalid input. Please enter a number.")

        if self.attempts == self.max_attempts and user_input != self.number_to_guess:
            print(f"Sorry, you've run out of attempts. The correct number was {self.number_to_guess}.")

if __name__ == "__main__":
    game = NumberGuessingGame(low=1, high=100, max_attempts=7)
    game.play()