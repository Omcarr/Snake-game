from turtle import Screen
import Snake as body
import Snake_Score as score
import Snake_Food as food
import time

# setup of the Screen
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.title('Snake Game')
my_screen.tracer(0)

game_is_on = True
# objects
tim = body.Snake()
apple = food.Food()
board = score.ScoreBoard()
# controller
my_screen.listen()
my_screen.onkey(tim.move_up, 'Up')
my_screen.onkey(tim.move_down, 'Down')
my_screen.onkey(tim.move_left, 'Left')
my_screen.onkey(tim.move_right, 'Right')

while game_is_on:
    # makes the snake visible after each while-loop iteration
    my_screen.update()
    time.sleep(0.1)
    tim.move()
    # Detects collision with the food
    if tim.head.distance(apple) < 15:
        apple.Refresh_food()
        board.point += 1
        tim.extend()
        board.update(board.point,board.HighScore)

    # Detects collision with itself
    for seg in tim.snake_part[1:]:#slices the list to only check for distance of head from postion 1 to tail(head is position 0)
        if tim.head.distance(seg) <10:
            game_is_on = False
            board.Gameover()

    # Detects collision with the wall
    if tim.head.xcor() > 290 or tim.head.xcor() < (-290) or tim.head.ycor() > 290 or tim.head.ycor() < (-290):
        game_is_on = False
        board.Gameover()
