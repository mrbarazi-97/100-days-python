from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    answer_text = question["answer"]
    new_question = Question(q_text=question_text, q_answer=answer_text)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've compeleted the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
