
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)


        self.score_board = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_board.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text_display =self.canvas.create_text(
            150,
            125,
            width=250,
            text=f"Some Question Text",
            fill=THEME_COLOR,
            font=("Arial",20,"italic")
        )
        self.canvas.grid(row= 1 ,column= 0, columnspan=2, pady=50)

        true_image= PhotoImage(file="images/true.png")
        self.true_button =  Button(image=true_image, highlightthickness=0, command= self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image= PhotoImage(file="images/false.png")
        self.false_button =  Button(image=false_image, highlightthickness=0, command= self.false_pressed)
        self.false_button.grid(row=2, column=1)


        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):
        quiz_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text_display, text=quiz_text)

    def true_pressed(self):
        self.quiz.check_answer("True")


    def false_pressed(self):
        self.quiz.check_answer("False")


    # def get_check_answer(self):
    #     text_answer = self.quiz.check_answer()
