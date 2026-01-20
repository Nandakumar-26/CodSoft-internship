
# Task 4: Rock Paper Scissors Game

import random

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- ROCK PAPER SCISSORS ---")
        print("Choices:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_choice = input("Enter your choice (1-3): ")

        if user_choice not in ["1", "2", "3"]:
            print("Invalid choice. Try again.")
            continue

        choices = ["Rock", "Paper", "Scissors"]
        user = choices[int(user_choice) - 1]
        computer = random.choice(choices)

        print("You chose:", user)
        print("Computer chose:", computer)

        if user == computer:
            print("Result: It's a Tie!")

        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Scissors" and computer == "Paper") or \
             (user == "Paper" and computer == "Rock"):
            print("Result: You Win!")
            user_score += 1

        else:
            print("Result: You Lose!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

play_game()
