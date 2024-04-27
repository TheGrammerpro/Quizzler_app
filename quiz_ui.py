from tkinter import *
from quiz_brain import QuizBrain
import data


THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.user_answer = None
        self.quiz.question_number = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=400, height=600, bg=THEME_COLOR)

        self.score_label = Label(text="score : 0", font=('Arial', 16), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=0, row=1, columnspan=2, padx=20)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="question",
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 16, 'italic'))
        self.canvas.grid(column=0, row=2, columnspan=2, padx=20, pady=20)

        right_icon = PhotoImage(file="./images/true.png")
        wrong_icon = PhotoImage(file="./images/false.png")

        self.button_r = Button(image=right_icon, width=100, height=100, command=self.true_return)
        self.button_r.grid(column=0, row=3, pady=20, padx=10)

        self.button_w = Button(image=wrong_icon, width=100, height=100, command=self.false_return)
        self.button_w.grid(column=1, row=3, pady=20, padx=10)

        self.reset_button = Button(text="New\nquiz", command=self.reset, width=12)
        self.reset_button.grid(column=0, row=0, padx=20, pady=20)
        self.reset_button["state"] = "disabled"

        self.restart_button = Button(text="Restart\nquiz", command=self.restart, width=12)
        self.restart_button.grid(column=1, row=0, padx=20, pady=20)
        self.restart_button["state"] = "disabled"

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.button_w["state"] = "active"
        self.button_r["state"] = "active"
        self.canvas.configure(bg='white')
        if self.quiz.question_number < 10:
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"The quiz is finished, "
                                                            f"your final score is {self.quiz.score} out of 10")
            self.reset_button["state"] = "active"
            self.restart_button["state"] = "active"
            self.button_w["state"] = "disabled"
            self.button_r["state"] = "disabled"

    def false_return(self):
        self.user_answer = "false"
        self.check_answer()

    def true_return(self):
        self.user_answer = "true"
        self.check_answer()

    def check_answer(self):
        self.quiz.check_answer(self.user_answer)
        self.score_label.config(text=f"score: {self.quiz.score}")
        self.button_w["state"] = "disabled"
        self.button_r["state"] = "disabled"
        if self.quiz.is_right:  # If answer is correct
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
        self.window.after(1000, self.next_question)

    def reset(self):
        """Resets the program with a new random set of questions"""
        self.window.destroy()
        quiz_ui = data.initialize()
        return quiz_ui

    def restart(self):
        """Restarts the current set of questions"""
        self.quiz.score = 0
        self.score_label.config(text=f"score: {self.quiz.score}")
        self.quiz.question_number = 0
        self.next_question()
        self.button_w["state"] = "active"
        self.button_r["state"] = "active"
