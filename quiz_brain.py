class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        q_n_a = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Qn{self.question_number}. {q_n_a.text} (True/False) ? : ")
        self.check_answer(guess,q_n_a.answer)

    def check_answer(self,guess,answer):
        if guess.lower() == answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"Wrong answer.")
        print(f"The correct answer is: {answer}")
        print(f"Current Score = {self.score}/{self.question_number}\n")


    def still_has_questions(self):
        number_of_questions = len(self.question_list)
        if self.question_number <= number_of_questions - 1:
            return True
        else:
            return False

    # def still_has_questions(self):
    #     number_of_questions = len(self.question_list)
    #     return self.question_number <= number_of_questions - 1
