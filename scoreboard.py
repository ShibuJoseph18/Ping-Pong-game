from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 50, "normal")
GAME_OVER_FONT = ("Arial", 20, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_player_score = 0
        self.right_player_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-200, y=200)
        self.write(arg=self.left_player_score, move=False, align=ALIGNMENT, font=FONT)
        self.goto(x=200, y=200)
        self.write(arg=self.right_player_score, move=False, align=ALIGNMENT, font=FONT)

    def left_player_point(self):
        self.left_player_score += 1
        self.update_scoreboard()

    def right_player_point(self):
        self.right_player_score += 1
        self.update_scoreboard()


