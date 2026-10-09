import random

secret = random.randint(1, 100)
attempts = 0

print("I picked a number between 1 and 100. Guess it!")

while True:
    guess = int(input("Your guess: "))
    attempts = attempts + 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break