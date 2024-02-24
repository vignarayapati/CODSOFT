import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("300x200")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.label = tk.Label(root, text="Choose: Rock, Paper, or Scissors", font=("Helvetica", 12))
        self.label.pack(pady=10)
        
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()
        
        self.rock_button = tk.Button(self.buttons_frame, text="Rock", command=lambda: self.check_winner("rock"))
        self.rock_button.grid(row=0, column=0, padx=5)
        
        self.paper_button = tk.Button(self.buttons_frame, text="Paper", command=lambda: self.check_winner("paper"))
        self.paper_button.grid(row=0, column=1, padx=5)
        
        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", command=lambda: self.check_winner("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=5)
        
        self.score_label = tk.Label(root, text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")
        self.score_label.pack(pady=5)
        
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=5)
        
    def check_winner(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1
        
        messagebox.showinfo("Result", f"User's choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")
        self.update_score_label()
        
    def update_score_label(self):
        self.score_label.config(text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")
        
    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.update_score_label()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
