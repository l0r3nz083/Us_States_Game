from turtle import Turtle

FONT = ("Courier", 6, "bold")


class Poster(Turtle):

    def __init__(self, state, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.cor = (x, y)
        self.speed("slowest")
        self.positioning()
        self.write(state, align="center", font=FONT)

    def positioning(self):
        self.setpos(self.cor)
