import random

def get_user_choice():
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("Q. Quit")

    choice = input("Your choice: ").lower()
    return choice

def get_ai_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, ai):
    if player == ai:
        return "draw"
    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        return "player"
    else:
        return "ai"

player_score = 0
ai_score = 0

while True:
    user_input = get_user_choice()

    if user_input == 'q':
        print("Thanks for playing!")
        break

    if user_input not in ['1', '2', '3']:
        print("Invalid input! Please try again.")
        continue

    user_move = {"1": "rock", "2": "paper", "3": "scissors"}[user_input]
    ai_move = get_ai_choice()

    print(f"\nYou chose {user_move}")
    print(f"AI chose {ai_move}")

    result = determine_winner(user_move, ai_move)
    if result == "draw":
        print("It's a draw!")
    elif result == "player":
        print("You win this round!")
        player_score += 1
    else:
        print("AI wins this round!")
        ai_score += 1

    print(f"Score → You: {player_score} | AI: {ai_score}")

## version 1