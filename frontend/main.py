import tkinter as tk
from tkinter import messagebox
from backend.database import Database
from backend.game_logic import GameLogic
from frontend.drag_drop import DragDrop
from config.settings import (
    BG_COLOR, ADJ_COLOR, NOUN_COLOR, WORD_BG_COLOR, 
    WINDOW_WIDTH, WINDOW_HEIGHT
)

class WordGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Classification Game")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.config(bg=BG_COLOR)

        # Initialize Database and Game Logic
        self.db = Database()
        self.game_logic = GameLogic()
        
        self.username = None
        self.current_level = 1

        self.setup_login_screen()

    def setup_login_screen(self):
        """Create a simple login screen to enter username."""
        self.clear_screen()

        tk.Label(self.root, text="Enter Username:", font=("Arial", 14), bg=BG_COLOR).pack(pady=10)
        self.username_entry = tk.Entry(self.root, font=("Arial", 14))
        self.username_entry.pack(pady=5)
        tk.Button(self.root, text="Start Game", font=("Arial", 12), command=self.login).pack(pady=10)

    def login(self):
        """Logs in the user and initializes the game screen."""
        username = self.username_entry.get()
        if not username:
            messagebox.showerror("Error", "Username cannot be empty")
            return
        
        self.db.add_user(username)
        self.username = username
        self.current_level = self.db.get_progress(username)
        self.setup_game_screen()

    def setup_game_screen(self):
        """Sets up the main game interface."""
        self.clear_screen()

        tk.Label(self.root, text=f"Welcome, {self.username}!", font=("Arial", 16), bg=BG_COLOR).pack(pady=10)
        tk.Label(self.root, text="Select Level:", font=("Arial", 14), bg=BG_COLOR).pack(pady=10)

        # Create Level Selection Buttons
        for i in range(1, 7):
            state = "normal" if i <= self.current_level else "disabled"
            tk.Button(self.root, text=f"Level {i}", font=("Arial", 12), 
                      state=state, command=lambda l=i: self.load_level(l)).pack(pady=5)

    def load_level(self, level):
        """Loads the selected level with words and drag-drop mechanics."""
        self.clear_screen()
        self.current_level = level

        tk.Label(self.root, text=f"Level {level}", font=("Arial", 16), bg=BG_COLOR).pack(pady=10)

        # Display Hen Image
        self.hen_image = tk.PhotoImage(file="frontend/assets/hen.png")
        tk.Label(self.root, image=self.hen_image, bg=BG_COLOR).pack(pady=10)

        # Fetch Words for Current Level
        words = self.game_logic.words_data[str(level)]
        self.word_buttons = {}
        
        # Display Jumbled Words
        word_frame = tk.Frame(self.root, bg=BG_COLOR)
        word_frame.pack(pady=10)
        
        for word in words["adjective"] + words["noun"]:
            btn = tk.Button(word_frame, text=word, relief="raised", bg=WORD_BG_COLOR, font=("Arial", 12))
            btn.pack(side="left", padx=5)
            self.word_buttons[word] = btn

        # Adjective Box
        self.adj_frame = tk.Frame(self.root, bg=ADJ_COLOR, width=200, height=100)
        self.adj_frame.pack(pady=10)
        tk.Label(self.adj_frame, text="Adjective Box", bg=ADJ_COLOR, font=("Arial", 12)).pack()

        # Noun Box
        self.noun_frame = tk.Frame(self.root, bg=NOUN_COLOR, width=200, height=100)
        self.noun_frame.pack(pady=10)
        tk.Label(self.noun_frame, text="Noun Box", bg=NOUN_COLOR, font=("Arial", 12)).pack()

        # Initialize Drag & Drop
        self.drag_drop = DragDrop(self.root, self.word_buttons, self.adj_frame, self.noun_frame)

        tk.Button(self.root, text="Check Answers", font=("Arial", 12), command=self.check_answers).pack(pady=10)

    def check_answers(self):
        """Checks if the words are placed correctly."""
        user_answers = {"adjective": [], "noun": []}
        
        # Identify the words in each category based on placement
        for word, btn in self.word_buttons.items():
            if btn.winfo_ismapped():  # If the button is still visible (not inside a frame)
                continue
            elif btn.winfo_parent() == str(self.adj_frame):
                user_answers["adjective"].append(word)
            elif btn.winfo_parent() == str(self.noun_frame):
                user_answers["noun"].append(word)

        if self.game_logic.check_answers(self.current_level, user_answers):
            messagebox.showinfo("Success", f"Level {self.current_level} Completed!")
            self.db.update_progress(self.username, self.current_level + 1)
            self.setup_game_screen()
        else:
            messagebox.showerror("Error", "Try Again!")

    def clear_screen(self):
        """Clears all widgets from the current screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordGameApp(root)
    root.mainloop()
