import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x300")

        self.player_score = 0
        self.computer_score = 0

        self.player_label = tk.Label(self.root, text="Your Score: 0", font=("Arial", 14))
        self.player_label.grid(row=0, column=0, padx=10, pady=10)

        self.computer_label = tk.Label(self.root, text="Computer Score: 0", font=("Arial", 14))
        self.computer_label.grid(row=0, column=2, padx=10, pady=10)

        self.choice_label = tk.Label(self.root, text="", font=("Arial", 18))
        self.choice_label.grid(row=1, column=1, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 20))
        self.result_label.grid(row=2, column=1, padx=10, pady=10)

        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.make_choice("Rock"), font=("Arial", 12))
        self.rock_button.grid(row=3, column=0, padx=10, pady=10)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.make_choice("Paper"), font=("Arial", 12))
        self.paper_button.grid(row=3, column=1, padx=10, pady=10)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.make_choice("Scissors"), font=("Arial", 12))
        self.scissors_button.grid(row=3, column=2, padx=10, pady=10)

        self.root.mainloop()

    def make_choice(self, player_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        self.choice_label.config(text=f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            self.result_label.config(text="It's a tie!")
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            self.player_score += 1
            self.player_label.config(text=f"Your Score: {self.player_score}")
            self.result_label.config(text="You win!")
        else:
            self.computer_score += 1
            self.computer_label.config(text=f"Computer Score: {self.computer_score}")
            self.result_label.config(text="Computer wins!")

if __name__ == "__main__":
    game = RockPaperScissors()