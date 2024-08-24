import random
# program to generate random number and make user guess that number 
n = random.randint(1,100)
guess = None
attempts = 0

print("Guess the number between 1 and 100:")

while guess != n:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < n:
        print("Too low!")
    elif guess > n:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")

