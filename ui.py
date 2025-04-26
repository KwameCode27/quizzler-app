
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)

        # Configure rows and columns to be responsive
        self.windows.columnconfigure(0, weight=1)
        self.windows.columnconfigure(1, weight=1)
        self.windows.rowconfigure(1, weight=1)

        self.score_board = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_board.grid(row=0, column=1, sticky="e")

        self.canvas = Canvas(bg="white")
        self.text_display = self.canvas.create_text(
            150,
            125,
            width=250,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=20)
        self.canvas.config(width=300, height=250)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed, border=0)
        self.true_button.image = true_image  # Prevent image garbage collection
        self.true_button.grid(row=2, column=0, sticky="e", padx=20, pady=10)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed, border=0)
        self.false_button.image = false_image  # Prevent image garbage collection
        self.false_button.grid(row=2, column=1, sticky="w", padx=20, pady=10)

        self.reset_button = Button(text="Start Again", command=self.reset_quiz, bg="white", fg=THEME_COLOR, font=("Arial", 12, "bold"), border=0)
        self.reset_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.reset_button.grid_remove()  # Hide it initially

        self.get_next_question()

        self.windows.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_board.config(text=f"Score: {self.quiz.score}")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_display, text=quiz_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.text_display, text= f"You've completed the quiz\n\nYour final Score : {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.reset_button.grid()


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.windows.after(1000, self.get_next_question)

    def reset_quiz(self):
        self.quiz.reset()  # Call the reset method in QuizBrain (you'll add it next)
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        self.reset_button.grid_remove()
        self.get_next_question()



