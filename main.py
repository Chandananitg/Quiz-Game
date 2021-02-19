from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for qndict in question_data:
    question = Question(qndict["text"], qndict["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!\n Your final score = {quiz.score}/{quiz.question_number}")
