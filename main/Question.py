#This folder is for classifying items in a list
#the 'self' part is where I put the name of the list,
#the 'prompt' part labels whatever I type next as 'prompt' and this is the same with 'answer' and 'text'.
#Here 'prompt' would be the questions, 'answer' is where the correct answers are stored, and 'test' are the wrong answers the user could choose from.
#First the quiz would show users the question, then I made it so that my quiz checks if the users answer is in 'answer', meaning it's correct. In which case score increases.
#If their answer is found in 'test', their answer is wrong and my quiz moves on to the next question.
class Question:
    def __init__(self, prompt, answer, test):
        self.prompt = prompt
        self.answer = answer
        self.test = test