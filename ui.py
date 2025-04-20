
from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.geometry("400x500")  # Starting size
        self.windows.minsize(300, 400)
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)


        self.score_board = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_board.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=500, bg="white")
        self.text_display =self.canvas.create_text(text="Some of the Question",)
        self.canvas.grid()








        self.windows.mainloop()