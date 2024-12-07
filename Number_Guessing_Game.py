import random
import time
import json
import os

LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return {}
    with open(LEADERBOARD_FILE, "r") as file:
        return json.load(file)

def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file)

def display_leaderboard(leaderboard):
    if not leaderboard:
        print("\nNo leaderboard data yet. Be the first to play!")
        return
    print("\n--- Leaderboard ---")
    sorted_scores = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for rank, (player, score) in enumerate(sorted_scores, start=1):
        print(f"{rank}. {player}: {score} points")
    print("--------------------")

def start_game():
    leaderboard = load_leaderboard()

    print("Welcome to the Advanced Number Guessing Game!")
    player_name = input("Enter your name: ").strip()
    if not player_name:
        print("Name cannot be empty. Using 'Player1' as default.")
        player_name = "Player1"

    print("1. Easy (1-50)  \n2. Medium (1-100) \n3. Hard (1-200)")
    difficulty = int(input("Select difficulty (1/2/3): "))

    max_number = {1: 50, 2: 100, 3: 200}[difficulty]
    target = random.randint(1, max_number)
    attempts = 0
    streak = 0
    hint_points = 3
    max_time = 30 if difficulty > 1 else 60

    print(f"\nGuess a number between 1 and {max_number}. You have {max_time} seconds!")
    print(f"You start with {hint_points} hint points.\n")

    start_time = time.time()
    score = 0

    while True:
        if time.time() - start_time > max_time:
            print("\n⏰ Time's up! You couldn't guess the number in time!")
            break

        guess = input(f"Enter your guess (or type 'hint' to use hint points): ").strip()

        if guess.lower() == 'hint':
            if hint_points > 0:
                hint_points -= 1
                difference = abs(target - random.randint(1, max_number))
                print(f"Hint: The target number is within ±{difference} of your guess. Hint points left: {hint_points}.")
            else:
                print("No hint points left!")
            continue

        if not guess.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == target:
            streak += 1
            points_earned = max(10 - attempts, 1) * difficulty * 10
            score += points_earned
            print(f"🎉 Correct! You guessed it in {attempts} attempts. Streak: {streak}. Points this round: {points_earned}")
            break
        else:
            if guess > target:
                print("Too high!")
            else:
                print("Too low!")

            # Provide periodic clues
            if attempts % 3 == 0:
                if target % 2 == 0:
                    print("Clue: The number is even.")
                else:
                    print("Clue: The number is odd.")
                if target % 5 == 0:
                    print("Clue: The number is divisible by 5.")
                else:
                    print("Clue: The number is not divisible by 5.")

    # Update leaderboard
    leaderboard[player_name] = leaderboard.get(player_name, 0) + score
    save_leaderboard(leaderboard)

    print("\nGame Over!")
    print(f"Your final score: {score}")
    print(f"Your total score: {leaderboard[player_name]}")
    display_leaderboard(leaderboard)

if __name__ == "__main__":
    start_game()
