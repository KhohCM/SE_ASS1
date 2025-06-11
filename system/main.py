import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.config(bg="#222222")

# Scores
player_score = 0
ai_score = 0

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Functions
def ai_move():
    return random.choice(choices)

def decide_winner(player, ai):
    global player_score, ai_score
    if player == ai:
        result_label.config(text="It's a draw!")
    elif (player == "Rock" and ai == "Scissors") or \
         (player == "Paper" and ai == "Rock") or \
         (player == "Scissors" and ai == "Paper"):
        result_label.config(text="You win this round!")
        player_score += 1
    else:
        result_label.config(text="AI wins this round!")
        ai_score += 1
    update_score()

def play(player_choice):
    ai_choice = ai_move()
    player_label.config(text=f"You chose: {player_choice}")
    ai_label.config(text=f"AI chose: {ai_choice}")
    decide_winner(player_choice, ai_choice)

def update_score():
    score_label.config(text=f"Score → You: {player_score} | AI: {ai_score}")

def reset_game():
    global player_score, ai_score
    player_score = 0
    ai_score = 0
    update_score()
    result_label.config(text="")
    player_label.config(text="")
    ai_label.config(text="")

# Widgets
title = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 20, "bold"), bg="#222222", fg="white")
title.pack(pady=10)

score_label = tk.Label(root, text="Score → You: 0 | AI: 0", font=("Helvetica", 14), bg="#222222", fg="white")
score_label.pack()

player_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#222222", fg="white")
player_label.pack()

ai_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#222222", fg="white")
ai_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#222222", fg="gold")
result_label.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#222222")
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

reset_btn = tk.Button(root, text="Reset Game", width=15, command=reset_game, bg="darkred", fg="white")
reset_btn.pack(pady=10)

# Start the GUI loop
root.mainloop()
