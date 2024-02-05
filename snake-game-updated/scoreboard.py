from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')
#DATA_FILE_PATH = "Day24\snake-game-updated\data.txt" #The file link must contain full path from the work environment
DATA_FILE_PATH = "/Users/Owner/Desktop/data.txt"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()  

    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
    
    def add_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def get_high_score(self):
        with open(DATA_FILE_PATH) as file:
            return int(file.read())
            
            
    def update_high_score(self):
        with open(DATA_FILE_PATH, mode = "w") as file:
            file.write(str(self.high_score))