class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        cur_q = self.question_number
        q_text = self.question_list[cur_q].text
        q_ans = self.question_list[cur_q].answer
        self.question_number += 1
        # print(f"\t*** PSST. The answer is {q_ans}")
        user_ans = input(f"Q.{cur_q + 1}: {q_text} (True/False):  ").lower()
        self.check_answer(user_ans, q_ans)

    def check_answer(self, user, correct):
        if user == correct.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's incorrect.")
        print(f"The correct answer was: {correct}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

