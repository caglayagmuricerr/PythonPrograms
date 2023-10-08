import random

def roll_dice():
    return random.randint(1, 6) # Return a random integer between 1 and 6 to simulate a dice roll

def higher_or_lower_game():
    print("\t\t\t\t\tWelcome to the Higher or Lower Dice Game!") # Print a welcome message
    print("=================================================================================================================================")
    print('''The rules are simple: I will roll a dice and you have to guess if the next roll will be higher or lower than the current roll. 
          If you guess correctly, you get a point. If you guess wrong, the game ends. Let's begin!''')
    print("=================================================================================================================================")

    score = 0

    while True:
        current_roll = roll_dice()
        print(f"Current roll: {current_roll}")

        user_guess = input("Will the next roll be higher or lower? (h/l): ").lower()

        if user_guess not in ['h', 'l']:
            print("Invalid input. Please enter 'h' for higher or 'l' for lower.")
            continue

        next_roll = roll_dice()
        print(f"Next roll: {next_roll}")

        if next_roll == current_roll:
            print("It's the same number. Roll again.")
            continue

        if (user_guess == 'h' and next_roll > current_roll) or (user_guess == 'l' and next_roll < current_roll):
            print("Correct! You guessed it right.")
            print("\n")
            score += 1
        else:
            print(f"Wrong guess. Game over! You guessed right {score} times!")
            break

        current_roll = next_roll

        while True:
            play_again = input("Do you want to continue playing? (yes/no): ").lower()
            if play_again == 'yes':
                print("\n")
                break
            elif play_again == 'no':
                print(f"Thank you for playing! You guessed right {score} times!")
                return  # Exit the function to end the game
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    higher_or_lower_game()
