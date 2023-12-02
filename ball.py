from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        x_coordinate = self.xcor() + self.x_move
        y_coordinate = self.ycor() + self.y_move
        self.goto(x_coordinate, y_coordinate)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reverse_position(self):
        self.goto(0,0)
        self.bounce_x()
