import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.is_right = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.question_number < 10:
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = html.unescape(self.current_question.text)
            return f"Q.{self.question_number}: {q_text} (True/False): "
        else:
            return f"Quiz is over. Your score is {self.score} out of 10."
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.is_right = True
            return self.is_right
        else:
            self.is_right = False
            return self.is_right

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")

    def refresh_questions(self, q_list):
        self.question_list = q_list
