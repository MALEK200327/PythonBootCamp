from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questionBank=[]
for question in question_data:
    questions = Question(question["text"],question["answer"])
    questionBank.append(questions)


quiz = QuizBrain(questionBank)
while quiz.still_has_question() :
    quiz.next_question()


print(f"you have completed the quiz with a score of {quiz.score}/ {len(questionBank)}")