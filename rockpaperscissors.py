"""
Rock-Paper-Scissors 
-----------------------------
Play against the computer, keep score, and see stats at the end.
"""

import random
from collections import Counter

# Function to decide who wins the round
def who_wins(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

# Function to show stats at the end
def show_stats(total_games, p_score, c_score, draws, player_moves):
    print("\n=== Game Stats ===")
    print(f"Total games: {total_games}")
    print(f"You won: {p_score} | Computer won: {c_score} | Draws: {draws}")
    if player_moves:
        most_move = Counter(player_moves).most_common(1)[0][0]
        print(f"Your most used move: {most_move.capitalize()}")
    print("=================\n")

# Main game function
def play_rps():
    moves = ["rock", "paper", "scissors"]
    p_score = 0
    c_score = 0
    draws = 0
    total = 0
    player_history = []

    print(" Welcome to Rock-Paper-Scissors ")
    print("Type 'quit' anytime to leave the game.\n")

    while True:
        player = input("Your move (rock/paper/scissors): ").lower().strip()

        if player == "quit":
            print("\nThanks for playing! Bye ")
            show_stats(total, p_score, c_score, draws, player_history)
            break

        if player not in moves:
            print("Oops, invalid move. Try again.")
            continue

        computer = random.choice(moves)
        print(f"Computer chose: {computer}")

        player_history.append(player)
        total += 1

        winner = who_wins(player, computer)

        if winner == "draw":
            print(" It's a draw!")
            draws += 1
        elif winner == "player":
            print(" You win this round! Nice!")
            p_score += 1
        else:
            print(" Computer wins this round!")
            c_score += 1

        print(f"Score -> You: {p_score} | Comp: {c_score} | Draws: {draws}\n")

        # Ask if player wants another round
        again = input("Play another round? (yes/no): ").lower().strip()
        if again != "yes":
            print("\nThanks for playing! Bye ")
            show_stats(total, p_score, c_score, draws, player_history)
            break

# Run the game
if __name__ == "__main__":
    play_rps()
