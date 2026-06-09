import random

def Guesses_Game():

    attempts = 10
    number = random.randint(1, 100)
    used_numbers = set()

    print("Guess a number between 1 and 100")

    while attempts > 0:

        guess = input(f"\nEnter your guess (Remaining attempts: {attempts}): ")

        if not guess.isdigit():
            print("Invalid input, please enter a number.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("Not allowed! number must be between 1 and 100")
            continue  

        if guess in used_numbers:
            print("You already entered this number!")
            continue  

        used_numbers.add(guess)

        if guess == number:
            print("Congratulations! You guessed it right!")
            print("A new number will be generated...\n")
            number = random.randint(1, 100)
            used_numbers.clear()
            continue

        if guess < number:
            print("Too small!")
        else:
            print("Too big!")

        attempts -= 1

    print("\nYou finished all attempts!")

    again = input("Do you want to play again? (y/n): ")

    if again.lower() == "y":
        Guesses_Game()
    else:
        print("Thanks for playing!")

Guesses_Game()