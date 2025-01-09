import tkinter as tk
import random

# Flashcard data
flashcards = {
    "あ": "a",
    "い": "i",
    "う": "u",
    "え": "e",
    "お": "o",
    "か": "ka",
    "き": "ki",
    "く": "ku",
    "け": "ke",
    "こ": "ko",
}

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz")

        self.flashcards = list(flashcards.items())
        self.current_card = None

        self.question_label = tk.Label(root, text="", font=("Arial", 24))
        self.question_label.pack(pady=20)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        self.buttons = []
        for i in range(6):
            button = tk.Button(self.buttons_frame, text="", font=("Arial", 16), width=10, command=lambda b=i: self.check_answer(b))
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.result_label.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", font=("Arial", 16), command=self.next_card)
        self.next_button.pack(pady=10)

        self.next_card()

    def next_card(self):
        self.result_label.config(text="")
        self.current_card = random.choice(self.flashcards)
        self.question_label.config(text=self.current_card[0])

        # Shuffle options and add the correct answer
        options = [self.current_card[1]]
        while len(options) < 6:
            option = random.choice(list(flashcards.values()))
            if option not in options:
                options.append(option)

        random.shuffle(options)

        # Update button texts
        for i, option in enumerate(options):
            self.buttons[i].config(text=option, state=tk.NORMAL)

        self.correct_answer = self.current_card[1]

    def check_answer(self, button_index):
        selected_answer = self.buttons[button_index].cget("text")
        if selected_answer == self.correct_answer:
            self.result_label.config(text="Correct!", fg="green")
            for button in self.buttons:
                button.config(state=tk.DISABLED)
        else:
            self.result_label.config(text="Incorrect, try again!", fg="red")

# Create the app
root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()
