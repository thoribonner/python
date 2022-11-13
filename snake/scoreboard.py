import random
from turtle import Turtle, Screen
import json
import datetime

TOP = (0, 270)
ABOVE_CENTER = (0, 50)
CENTER = (0, 0)
HIGH_SCORES = "high_scores.json"
ALIGNMENT = "center"
SCORE_FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 98, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_scores = self._load_scores()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(TOP)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(ABOVE_CENTER)
        self.color("pink")
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        if self._is_high_score():
            self._set_high_score(Screen().textinput(title="🏆 join the leader board 🏆", prompt="enter your name:  "))
        self._display_high_scores()

    def _load_scores(self):
        with open(HIGH_SCORES, "r") as file:
            saved_scores = json.load(file)
            return saved_scores

    def _is_high_score(self):
        lowest_high_score = int(self.high_scores["5"]['score'])
        return lowest_high_score <= self.score

    def _set_high_score(self, player_name):
        score_saved = False
        new_high_score = {"score": str(self.score), "name": player_name, "date": str(datetime.date.today())}
        next_score = {}
        for key in self.high_scores:
            check_score = int(self.high_scores[key]['score'])
            if not self.high_scores[key]['score']:
                self.high_scores[key] = new_high_score
                break
            elif self.score >= check_score and not score_saved:
                next_score = self.high_scores[key]
                self.high_scores[key] = new_high_score
                score_saved = True
            elif score_saved:
                temp = next_score
                next_score = self.high_scores[key]
                self.high_scores[key] = temp

        self._save_high_scores(self.high_scores)
        self.high_scores = self._load_scores()
        self.score = 0

    def _save_high_scores(self, scores_to_save):
        with open(HIGH_SCORES, "w") as file:
            json.dump(scores_to_save, file)

    def _display_high_scores(self):
        self.penup()
        self.color("lime")
        x_value, y_value = CENTER
        for key, value in self.high_scores.items():
            if int(value['score']) > 0:
                self.goto(x_value, y_value)
                self.write(f"{value['score']} --- {value['name']}", align=ALIGNMENT, font=SCORE_FONT)
                y_value -= 30
