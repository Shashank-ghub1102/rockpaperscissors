# rockpaperscissorsimport random

def rock_paper_scissors():
    print("✊✋✌ Welcome to Rock, Paper, Scissors!")
    options = ["rock", "paper", "scissors"]
    
    player_score = 0
    computer_score = 0
    
    while True:
        player = input("Choose Rock, Paper, or Scissors (or type 'quit' to stop): ").lower()
        
        if player == "quit":
            print(" Thanks for playing!")
            print(f"Final Score → You: {player_score}, Computer: {computer_score}")
            break
        
        if player not in options:
            print("⚠ Invalid choice. Try again.")
            continue
        
        computer = random.choice(options)
        print(f"Computer chose: {computer}")
        
        if player == computer:
            print("It's a draw!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "scissors" and computer == "paper") or \
             (player == "paper" and computer == "rock"):
            print(" You win this round!")
            player_score += 1
        else:
            print(" Computer wins this round!")
            computer_score += 1
        
        print(f"Score → You: {player_score}, Computer: {computer_score}\n")

# Run the game
rock_paper_scissors()
