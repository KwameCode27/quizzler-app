from tkinter import *
from tkinter import ttk
from quiz_brain import QuizBrain
import time


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Color scheme
        self.primary_color = "#2C3E50"  # Dark blue-gray
        self.secondary_color = "#3498DB"  # Bright blue
        self.accent_color = "#E74C3C"  # Red accent
        self.text_color = "#ECF0F1"  # Off-white
        self.correct_color = "#2ECC71"  # Green
        self.incorrect_color = "#E74C3C"  # Red
        self.neutral_color = "#F5F5F5"  # Light gray

        # Set up window
        self.window = Tk()
        self.window.title("Quizzler Pro")
        self.window.geometry("600x650")
        self.window.config(padx=40, pady=40, bg=self.primary_color)
        self.window.minsize(400, 550)  # Set minimum window size

        # Custom font styles
        self.title_font = ("Helvetica", 22, "bold")
        self.heading_font = ("Helvetica", 18, "bold")
        self.body_font = ("Helvetica", 14)
        self.button_font = ("Helvetica", 12, "bold")

        # Configure rows and columns for responsive layout
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(1, weight=1)  # Question frame should expand

        # Header with app title and score
        self.header_frame = Frame(self.window, bg=self.primary_color)
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 20))
        self.header_frame.columnconfigure(0, weight=2)  # Title gets more space
        self.header_frame.columnconfigure(1, weight=1)  # Score gets less space

        self.app_title = Label(
            self.header_frame,
            text="QUIZZLER PRO",
            fg=self.secondary_color,
            bg=self.primary_color,
            font=self.title_font
        )
        self.app_title.grid(row=0, column=0, sticky="w")

        self.score_frame = Frame(self.header_frame, bg=self.secondary_color, padx=15, pady=5)
        self.score_frame.grid(row=0, column=1, sticky="e")

        self.score_label = Label(
            self.score_frame,
            text="Score:",
            fg=self.text_color,
            bg=self.secondary_color,
            font=self.body_font
        )
        self.score_label.grid(row=0, column=0, padx=(0, 8))

        self.score_value = Label(
            self.score_frame,
            text="0",
            fg=self.text_color,
            bg=self.secondary_color,
            font=self.heading_font
        )
        self.score_value.grid(row=0, column=1)

        # Question area - now with responsive Text widget instead of Label
        self.question_frame = Frame(
            self.window,
            bg=self.neutral_color,
            highlightbackground=self.secondary_color,
            highlightthickness=2,
            padx=20,
            pady=20
        )
        self.question_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=20)
        self.question_frame.columnconfigure(0, weight=1)  # Make inner column expand
        self.question_frame.rowconfigure(1, weight=1)  # Make question row expand

        self.question_number = Label(
            self.question_frame,
            text="Question 1/10",
            fg=self.primary_color,
            bg=self.neutral_color,
            font=self.body_font,
            anchor="w"
        )
        self.question_number.grid(row=0, column=0, sticky="ew", pady=(0, 15))

        # Using Text widget for better text wrapping and responsiveness
        self.question_text = Text(
            self.question_frame,
            fg=self.primary_color,
            bg=self.neutral_color,
            font=self.heading_font,
            wrap=WORD,  # Wrap by word
            height=6,
            width=30,  # Width in characters, will expand with window
            relief=FLAT,
            padx=10,
            pady=10
        )
        self.question_text.grid(row=1, column=0, sticky="nsew")
        self.question_text.insert(END, "Question text will appear here")
        self.question_text.config(state=DISABLED)  # Make it read-only

        # Add a scrollbar that appears only when needed
        self.scrollbar = ttk.Scrollbar(self.question_frame, orient=VERTICAL, command=self.question_text.yview)
        self.question_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=1, sticky="ns")

        # Progress bar
        self.progress_frame = Frame(self.window, bg=self.primary_color)
        self.progress_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 20))
        self.progress_frame.columnconfigure(0, weight=1)  # Make progress bar expand

        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure(
            "custom.Horizontal.TProgressbar",
            troughcolor=self.neutral_color,
            background=self.secondary_color,
            thickness=10
        )

        self.progress = ttk.Progressbar(
            self.progress_frame,
            style="custom.Horizontal.TProgressbar",
            orient="horizontal",
            mode="determinate"
        )
        self.progress.grid(row=0, column=0, sticky="ew", pady=10)

        # Button area
        self.button_frame = Frame(self.window, bg=self.primary_color)
        self.button_frame.grid(row=3, column=0, columnspan=2, sticky="ew")
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)

        # True button
        self.true_frame = Frame(self.button_frame, bg=self.primary_color)
        self.true_frame.grid(row=0, column=0, padx=10, pady=10)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            self.true_frame,
            image=true_image,
            bg=self.primary_color,
            activebackground=self.primary_color,
            bd=0,
            highlightthickness=0,
            cursor="hand2",
            command=self.true_pressed
        )
        self.true_button.image = true_image  # Prevent image garbage collection
        self.true_button.pack()

        self.true_label = Label(
            self.true_frame,
            text="TRUE",
            fg=self.correct_color,
            bg=self.primary_color,
            font=self.button_font
        )
        self.true_label.pack(pady=(5, 0))

        # False button
        self.false_frame = Frame(self.button_frame, bg=self.primary_color)
        self.false_frame.grid(row=0, column=1, padx=10, pady=10)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            self.false_frame,
            image=false_image,
            bg=self.primary_color,
            activebackground=self.primary_color,
            bd=0,
            highlightthickness=0,
            cursor="hand2",
            command=self.false_pressed
        )
        self.false_button.image = false_image  # Prevent image garbage collection
        self.false_button.pack()

        self.false_label = Label(
            self.false_frame,
            text="FALSE",
            fg=self.incorrect_color,
            bg=self.primary_color,
            font=self.button_font
        )
        self.false_label.pack(pady=(5, 0))

        # Reset button
        self.reset_frame = Frame(self.window, bg=self.primary_color)
        self.reset_frame.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(20, 0))
        self.reset_frame.columnconfigure(0, weight=1)

        self.reset_button = Button(
            self.reset_frame,
            text="Play Again",
            font=self.button_font,
            bg=self.secondary_color,
            fg=self.text_color,
            activebackground=self.secondary_color,
            activeforeground=self.text_color,
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            border=0,
            command=self.reset_quiz
        )
        self.reset_button.grid(row=0, column=0)
        self.reset_button.grid_remove()  # Hide initially

        # Timer animation vars
        self.feedback_duration = 800  # ms

        # Bind resize event to update layout
        self.window.bind("<Configure>", self.on_window_resize)

        # Start the quiz
        self.get_next_question()

        self.window.mainloop()

    def on_window_resize(self, event):
        """Handle window resize events"""
        # Only respond to actual window resizes, not widget resizes
        if event.widget == self.window:
            # Dynamically adjust question text font size based on window width
            window_width = self.window.winfo_width()
            if window_width < 500:
                new_font = ("Helvetica", 14, "bold")
            elif window_width < 700:
                new_font = ("Helvetica", 16, "bold")
            else:
                new_font = ("Helvetica", 18, "bold")

            # Update font for question text
            self.question_text.config(font=new_font)

            # Also adjust progress bar size to match window width
            self.progress.config(length=window_width - 100)

            # Make scrollbar visible only when needed
            if float(self.question_text.yview()[1]) < 1.0:
                self.scrollbar.grid(row=1, column=1, sticky="ns")
            else:
                self.scrollbar.grid_remove()

    def update_progress(self):
        """Update the progress bar based on current question number"""
        if self.quiz.question_number == 0:
            progress_value = 0
        else:
            total_questions = len(self.quiz.question_list)
            progress_value = (self.quiz.question_number / total_questions) * 100
        self.progress["value"] = progress_value

    def get_next_question(self):
        """Display the next question or end screen"""
        self.question_frame.config(bg=self.neutral_color)
        self.question_text.config(bg=self.neutral_color)
        self.question_number.config(bg=self.neutral_color)

        if self.quiz.still_has_questions():
            # Update score and question number
            self.score_value.config(text=f"{self.quiz.score}")
            total_questions = len(self.quiz.question_list)
            self.question_number.config(text=f"Question {self.quiz.question_number + 1}/{total_questions}")

            # Get next question
            quiz_text = self.quiz.next_question()

            # Update question text with Text widget
            self.question_text.config(state=NORMAL)
            self.question_text.delete(1.0, END)
            self.question_text.insert(END, quiz_text)
            self.question_text.config(state=DISABLED)

            # Check if scrollbar is needed
            self.window.update_idletasks()  # Force geometry update
            if float(self.question_text.yview()[1]) < 1.0:
                self.scrollbar.grid(row=1, column=1, sticky="ns")
            else:
                self.scrollbar.grid_remove()

            # Update progress bar
            self.update_progress()

            # Ensure buttons are enabled
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
        else:
            # Quiz completed
            self.update_progress()
            final_score = self.quiz.score
            total_questions = len(self.quiz.question_list)
            percentage = int((final_score / total_questions) * 100)

            # Display results with appropriate feedback
            if percentage >= 80:
                result_text = f"Excellent!\n\nYour final score: {final_score}/{total_questions} ({percentage}%)"
                color = self.correct_color
            elif percentage >= 60:
                result_text = f"Good job!\n\nYour final score: {final_score}/{total_questions} ({percentage}%)"
                color = self.secondary_color
            else:
                result_text = f"Keep practicing!\n\nYour final score: {final_score}/{total_questions} ({percentage}%)"
                color = self.incorrect_color

            # Update question text with Text widget
            self.question_frame.config(bg=self.neutral_color)
            self.question_number.config(text="Quiz Complete", bg=self.neutral_color)

            self.question_text.config(state=NORMAL)
            self.question_text.delete(1.0, END)
            self.question_text.insert(END, result_text)
            self.question_text.config(state=DISABLED)

            # Disable answer buttons and show reset button
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.reset_button.grid()

    def true_pressed(self):
        """Handle True button press"""
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        """Handle False button press"""
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Show visual feedback for correct/incorrect answers"""
        # Disable buttons while showing feedback
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        # Change background color based on answer
        if is_right:
            color = self.correct_color
        else:
            color = self.incorrect_color

        self.question_frame.config(bg=color)
        self.question_text.config(bg=color)
        self.question_number.config(bg=color)

        # Schedule next question after feedback duration
        self.window.after(self.feedback_duration, self.get_next_question)

    def reset_quiz(self):
        """Reset the quiz to start again"""
        self.quiz.reset()  # Reset quiz brain
        self.update_progress()  # Reset progress bar
        self.reset_button.grid_remove()  # Hide reset button
        self.true_button.config(state="normal")  # Enable buttons
        self.false_button.config(state="normal")
        self.get_next_question()  # Get first question