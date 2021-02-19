#guessing game
import random

NUM = random.randint(1,100)
print(NUM)
difficulty = input("I'm hinking of a number between 1 and 100. Choose 'easy' or 'hard'")
if difficulty == "easy":
    guess_count = 10
else:
    guess_count = 5
print(guess_count)

guess= int(input("I am thinking of a number between 1 and 100. What is it? "))

out_of_guesses= False

if guess == NUM:
    print("you win")
else:
    while not out_of_guesses:
        if guess > NUM:
            guess_count -= 1
            guess = int(input(f"The number is lower than your guess. You have {guess_count} more tries left "))
        elif guess < NUM:
            guess_count -= 1
            guess = int(input(f"The number is higher than your guess. You have {guess_count} more tries left "))
            if guess_count == 1:
                out_of_guesses = True
    print(f"You lose! The number was {NUM}")
