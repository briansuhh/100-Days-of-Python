from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    text = data["text"]
    answer = data["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print("Congratulations for completing the quiz!")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")