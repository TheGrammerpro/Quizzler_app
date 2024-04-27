import requests
from question_model import Question
from quiz_brain import QuizBrain
from quiz_ui import QuizUi

parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}


def get_questions():
    question_api = requests.get("https://opentdb.com/api.php", params=parameters)
    question_api.raise_for_status()
    questions = question_api.json()
    return questions["results"]


def call_questions():
    question_data = get_questions()
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    return question_bank


def initialize():
    question_series = call_questions()
    quiz_brain = QuizBrain(question_series)
    quiz_interface = QuizUi(quiz_brain)
    return quiz_interface


