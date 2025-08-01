import random

print("Hi ! Welcome to Number Guessing Game.\nYou have 7 chances to guess the number. Let's start !")

low = int(input("Enter the Lower Limit: "))
high = int(input("Enter the Upper Limit: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Lets start !")

number = random.randint(low, high)
chances = 7
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    guess = int(input('Enter your guess: '))

    if guess == number:
        print(f'Correct! The number is {number}. You guessed it in {guess_counter} attempts.')
        break
    elif guess_counter >= chances and guess != number:
        print(f'Sorry! The number is {number}. Better luck next time!')
    elif guess > number:
        print('Too high ! Try lowering your guess.')
    elif guess < number:
        print('Too low ! Try upping your guess.')
