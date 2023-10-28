# --<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--

# Fizzbuzz is a childrens game where you count up from 1 to a number, replacing any number divisible by 3 with the word "fizz", 
# any number divisible by 5 with the word "buzz" and any number divisible by both with the word "fizzbuzz"

# --<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--

# This program will take a number from the user and play fizzbuzz up to that number

# --<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--

# It will also print "bang" for multiples of 7 (additional rule) and can be easily extended to add more rules

# --<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--

def fizz_buzz_rules():
    rules = [
        (3, "Fizz"), # divisors and their corresponding words
        (5, "Buzz"),
        (7, "Bang")  # Additional rule: print "Bang" for multiples of 7
        
        # More rules can be added as needed
    ]
    return rules

def apply_rules(number, rules):
    output = ""
    for divisor, result in rules:
        if number % divisor == 0:
            output += result
    return output if output else str(number)

def play_fizz_buzz_up_to_number(number):
    rules = fizz_buzz_rules()
    for i in range(1, number+1):
        print(apply_rules(i, rules))

if __name__ == "__main__":
    # Get the number from the user
    number = int(input("Enter a number: "))
    
    # Play FizzBuzz up to the specified number
    play_fizz_buzz_up_to_number(number)