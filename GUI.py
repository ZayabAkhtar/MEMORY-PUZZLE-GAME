import tkinter as tk
from tkinter import messagebox
import random
import time

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Puzzle Game")
        
        self.size = 4  # 4x4 board
        self.card_values = list(range(1, (self.size * self.size) // 2 + 1)) * 2
        random.shuffle(self.card_values)
        
        self.buttons = []
        self.revealed = [False] * (self.size * self.size)
        self.first_pick = None
        self.second_pick = None
        self.attempts = 0
        
        self.create_widgets()
        
        self.start_time = time.time()
        self.time_limit = 60  # 60 seconds

    def create_widgets(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                btn = tk.Button(self.master, text="*", width=5, height=2,
                                command=lambda x=i, y=j: self.on_button_click(x, y))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    def on_button_click(self, x, y):
        index = x * self.size + y
        if not self.revealed[index]:
            self.revealed[index] = True
            self.buttons[x][y].config(text=str(self.card_values[index]))

            if self.first_pick is None:
                self.first_pick = index
            else:
                self.second_pick = index
                self.master.after(1000, self.check_match)

    def check_match(self):
        if self.card_values[self.first_pick] != self.card_values[self.second_pick]:
            self.buttons[self.first_pick // self.size][self.first_pick % self.size].config(text="*")
            self.buttons[self.second_pick // self.size][self.second_pick % self.size].config(text="*")
            self.revealed[self.first_pick] = False
            self.revealed[self.second_pick] = False
        else:
            self.attempts += 1
            if all(self.revealed):
                messagebox.showinfo("Congratulations!", f"You've matched all pairs in {self.attempts} attempts!")
                self.master.quit()

        self.first_pick = None
        self.second_pick = None

        if time.time() - self.start_time > self.time_limit:
            messagebox.showwarning("Time's up!", "Game Over!")
            self.master.quit()
        
        self.update_timer()

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        time_left = self.time_limit - int(elapsed_time)
        if time_left >= 0:
            self.master.title(f"Memory Puzzle Game - Time left: {time_left} seconds")
            self.master.after(1000, self.update_timer)
        else:
            messagebox.showwarning("Time's up!", "Game Over!")
            self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()