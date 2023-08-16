from data import question_data



for i in range(0,len(question_data)):
    del question_data[i]["category"]
    del question_data[i]["type"]
    del question_data[i]["difficulty"]
    del question_data[i]["incorrect_answers"]
    question_data[i]["text"] = question_data[i]["question"]
    del question_data[i]["question"]
    question_data[i]["answer"] = question_data[i]["correct_answer"]
    del question_data[i]["correct_answer"]
    
for i in range(0,len(question_data)):
    print(question_data[i])
    print("\n")
