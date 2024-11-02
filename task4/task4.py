import tkinter as tk
from tkinter import messagebox
import random
class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.user_score = 0
        self.computer_score = 0
        self.label = tk.Label(root, text="Choose: Rock, Paper, or Scissors", font=("Helvetica", 16), fg="blue")
        self.label.pack(pady=20)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)
        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play("rock"), width=10, font=("Helvetica", 14), bg="lightgray")
        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play("paper"), width=10, font=("Helvetica", 14), bg="lightgray")
        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play("scissors"), width=10, font=("Helvetica", 14), bg="lightgray")
        self.rock_button.pack(side=tk.LEFT, padx=5)
        self.paper_button.pack(side=tk.LEFT, padx=5)
        self.scissors_button.pack(side=tk.LEFT, padx=5)
        self.score_label = tk.Label(root, text="Score - You: 0, Computer: 0", font=("Helvetica", 14), fg="green")
        self.score_label.pack(pady=20)
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game, state=tk.DISABLED, bg="yellow")
        self.play_again_button.pack(pady=10)

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "You lose!"

    def play(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)

        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1

        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")
        messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")
        
        if result == "You lose!" or result == "It's a tie!":
            self.rock_button.config(state=tk.DISABLED)
            self.paper_button.config(state=tk.DISABLED)
            self.scissors_button.config(state=tk.DISABLED)
            self.play_again_button.config(state=tk.NORMAL)
        else:
            self.rock_button.config(state=tk.NORMAL)
            self.paper_button.config(state=tk.NORMAL)
            self.scissors_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score - You: 0, Computer: 0")
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="lightblue") 
    game = RockPaperScissors(root)
    root.mainloop()
