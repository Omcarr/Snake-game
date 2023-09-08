from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    def __init__(self):
        self. snake_part = []
        self.create_snake()
        self.head = self.snake_part[0]

    # makes 3 turtles & sends them to the starting postion
    def create_snake(self):
        for i in START_POSITION:
            self.add_part(i)

    # snake is ready at the initial poistion now
    def move(self):
        for i in range((len(self.snake_part)-1), 0, -1):
            # 3 goes to the position of 2 to that of 1......
            new_x = self.snake_part[i-1].xcor()
            new_y = self.snake_part[i-1].ycor()
            self.snake_part[i].goto(new_x, new_y)
        # head will always move forward according to the heading
        self.head.forward(MOVE_DISTANCE)

    def add_part(self, postion):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(postion)
        self.snake_part.append(new_segment)
    # extends the tail by 1

    def extend(self):
        self.add_part(self.snake_part[-1].position())
    # Controller

    def move_left(self):
        if self.head.heading()!= RIGHT:
         self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading()!= LEFT:
         self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)
