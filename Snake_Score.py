from turtle import Turtle
import pygame
FONT=('Courier', 16, 'bold')
ALIGNMENT ='center'
pygame.mixer.init()
sound = pygame.mixer.Sound("Dead_Mario.mp3")

class ScoreBoard(Turtle):   
    point=0
    file=open('highscore.txt')
    HighScore=file.read()
    file.close()
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.update(self.point,self.HighScore)

    def display(self):
        self.speed('fastest')
        self.penup()
        self.color('white')
    
    def update(self,point,HighScore):
        self.clear()
        self.display()
        self.goto(-200,270)
        self.write(f'Score:{point}', align=ALIGNMENT, font=FONT)
        self.goto(180,270)
        self.write(f'Highscore:{HighScore}', align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if int(self.HighScore)<self.point:
            self.HighScore=self.point
            file=open('Snake Game\highscore.txt',mode='w')
            file.write(f'{self.HighScore}')
            file.close()
            self.display()
            self.update(self.point,self.HighScore)
            self.goto(0,0)
            self.write(f'New Highscore', align=ALIGNMENT, font=FONT)
         

    def Gameover(self):
        self.display()
        self.goto(0,0)
        self.write(f'GAME OVER!', align=ALIGNMENT, font=FONT)
        self.reset()
        sound.play()
        self.point=0
        #pygame.time.wait() pauses the execution of the programme for specified time and the audio is played
        pygame.time.wait(int(sound.get_length() * 1000))
        pygame.quit()
