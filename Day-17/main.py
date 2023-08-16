from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


for i in range(0,len(question_data)):
    del question_data[i]["category"]
    del question_data[i]["type"]
    del question_data[i]["difficulty"]
    del question_data[i]["incorrect_answers"]
    question_data[i]["text"] = question_data[i]["question"]
    del question_data[i]["question"]
    question_data[i]["answer"] = question_data[i]["correct_answer"]
    del question_data[i]["correct_answer"]
    



for i in range(0, len(question_data)):
    question_bank.append(Question (text=question_data[i]['text'],answer=question_data[i]['answer']))
    


quizbrain = QuizBrain(question_list=question_bank)
print(quizbrain.still_has_question())
while quizbrain.still_has_question():
    quizbrain.next_question()

print("youve completed the quiz ")
print(f"Your FInal Score is {quizbrain.score}")