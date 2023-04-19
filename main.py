import random
from art import lose
def easy():
    game_over = False
    computer_guess = random.randint(1, 101)
    attempts = 10
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        if player_guess == computer_guess:
            print("You guessed correctly, You Win.")
            game_over = True
        elif player_guess > computer_guess:
            attempts -= 1
            print("Too High.")
        else:
            attempts -= 1
            print("Too Low.")
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        game_over = True

def hard():
    game_over = False
    computer_guess = random.randint(1, 101)
    attempts = 5
    while not game_over:
        if attempts == 0:
            print(f"You've run out of guesses, you lose.")
            game_over = True
            break
        print(f"You have {attempts} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        if player_guess == computer_guess:
            print("You guessed correctly, You Win.")
            game_over = True
            break
        elif player_guess > computer_guess:
            attempts -= 1
            print("Too High.")
        else:
            attempts -= 1
            print("Too Low.")
            
        
def play():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    choice = input("Chose a difficulty. Type 'easy' or 'hard':") 
    if choice == "easy":
        easy()
    elif choice == "hard":
        hard()
    else:
        print("Please provide a valid answer.")

play()