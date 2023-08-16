class QuizBrain:
    def __init__(self,question_list):
        self.question_number =0
        self.questions_list = question_list
        self.score =0
        
    def still_has_question(self):
        if len(self.questions_list) == self.question_number:
            return False
        else: return True
         
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(choice,current_question.answer)
        
    def check_answer(self,useranswer,correctanswer):
        if useranswer.lower()  == correctanswer.lower():
            self.score += 1
            print("You Got The Right Answer")
        else:
            print("You Got The Wrong Answer")
        print(f"The Right Answer is: {correctanswer}")   
        print(f"Your Correct Score is: {self.score}")
        print("\n")
        
        
        
        
            
   
    
            
    
    