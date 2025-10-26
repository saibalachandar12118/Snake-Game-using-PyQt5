from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout,QHBoxLayout,QVBoxLayout,QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt ,QUrl
from PyQt5.QtMultimedia import QSoundEffect
import scoreBoard
import snake
import random
import Food
from PyQt5.QtCore import QTimer

class Board(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snake Game 2.0")
        self.setWindowIcon(QIcon("Icon/snake_window_title_image.png"))
        self.resize(600,650)
        self.board_dim = 20 
        self.Board_core = [[QPushButton() for i in range(self.board_dim)] for j in range (self.board_dim) ]
        self.grid = QGridLayout()
        self.grid.setSpacing(1)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.ScoreBoard_instance = scoreBoard.LCDScoreboard()
        self.SnakeObj = snake.Snake()
        self.foodObj = Food.food_items
        self.relaunch_btn = QPushButton("Re - Launch")
        self.relaunch_btn.clicked.connect(self.relaunch_game)
        self.btn  = QHBoxLayout()
        self.btn.addStretch()
        self.btn.addWidget(self.relaunch_btn)
        self.grid_widget = QWidget()
        self.grid_widget.setLayout(self.grid)
        self.VFrame = QVBoxLayout()
        self.VFrame.addWidget(self.ScoreBoard_instance)
        self.VFrame.addWidget(self.grid_widget)
        self.VFrame.addLayout(self.btn)
        self.setLayout(self.VFrame)
        self.startup()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_snake)  # function to move snake each step
        self.timer.start(150)  # interval in ms (snake speed)
        self.setup_sounds()

    def relaunch_game(self):
        self.relaunch_game_sound.play()
        for i_index in self.Board_core:
            for j_buttons in i_index:
                try:
                    j_buttons.setIcon(QIcon("Icon/white.png"))
                except:
                    pass
        self.SnakeObj.snake_array = self.SnakeObj.Intial_snake[:]
        self.SnakeObj._direction = self.SnakeObj.reset_direction[:]
        self.place_food()
        self.ScoreBoard_instance.reset_score()
        self.ScoreBoard_instance.update_score()
        self.draw_snake()
        self.update()  
        self.timer.start(150)
        
    def startup(self):
        for row in (self.Board_core) :
            for col in (row):
                col.setIcon(QIcon("Icon/white.png"))
                self.grid.addWidget(col,self.Board_core.index(row),row.index(col))
        self.place_food()
        self.draw_snake()

    def color_setter(self,index,args):
        for i,j in index :
            if args == "board":
                self.Board_core[i][j].setIcon(QIcon("Icon/white.png"))
                self.Board_core[i][j].update()
            elif args == "snake":
                self.Board_core[i][j].setIcon(QIcon(f"Icon/{self.SnakeObj.get_snake_color}"))
                self.Board_core[i][j].update()

    def draw_snake(self):
        for items in self.SnakeObj.snake_array:
            self.color_setter([items],"snake") 

    def keyPressEvent(self, event):
        key = event.key()
        tempdir = self.SnakeObj.get_direction
        if key == Qt.Key_W and tempdir[0] != 1:
            self.SnakeObj.set_direction([-1, 0])
        elif key == Qt.Key_S and tempdir[0] !=-1 :
            self.SnakeObj.set_direction([1, 0])
        elif key == Qt.Key_A and tempdir[1] != 1 :
            self.SnakeObj.set_direction([0,-1])
        elif key == Qt.Key_D and tempdir[1] != -1 :
            self.SnakeObj.set_direction([0,1])

    def move_snake(self,new_posx):
        temp_var1 = self.SnakeObj.snake_array.pop()
        self.Board_core[temp_var1[0]][temp_var1[1]].setIcon(QIcon("Icon/white.png"))
        self.color_setter([temp_var1],"board")
        self.color_setter([new_posx],"snake")
        self.SnakeObj.snake_array.insert(0,new_posx)
        
    def place_food(self):
        while True:
            i = random.randint(0, self.board_dim - 1)
            j = random.randint(0, self.board_dim - 1)
            if [i, j] not in (self.SnakeObj.snake_array):
                break
        self.placeFood  = random.choice(self.foodObj)
        self.placeFood.location = [i,j]
        self.Board_core[i][j].setIcon(QIcon(f"Icon/{self.placeFood.food_getter()}"))
        self.Board_core[i][j].update()

    def update_snake(self):
        head = self.SnakeObj.snake_array[0]
        direction = self.SnakeObj.get_direction
        new_head = [head[0] + direction[0], head[1] + direction[1]]
        new_head[0] = new_head[0] % self.board_dim
        new_head[1] = new_head[1] % self.board_dim

        # Check self collision
        if new_head in self.SnakeObj.snake_array:
            self.timer.stop()
            self.sound_gameover.play()
            self.fill_board_with_bomb_effect()

            print("Game Over: Hit itself")
            return

        # Check food
        if new_head == self.placeFood.location:
            self.sound_eat.play()
            self.SnakeObj.snake_array.insert(0, new_head)  # grow snake
            self.ScoreBoard_instance.update_score(self.placeFood.score_getter)
            self.color_setter([new_head],"snake")
            self.place_food()
            self.place_food_sound.play()

        else:
            self.move_snake(new_head)

    def setup_sounds(self):
        # Food / eat sound (.wav)
        self.sound_eat = QSoundEffect()
        self.sound_eat.setSource(QUrl.fromLocalFile("./sounds/eat.wav"))
        self.sound_eat.setVolume(1)

        # Game-over sound (.wav)
        self.sound_gameover = QSoundEffect()
        self.sound_gameover.setSource(QUrl.fromLocalFile("./sounds/GameOver.wav"))
        self.sound_gameover.setVolume(1)

        #sound for foodplacement
        self.place_food_sound = QSoundEffect()
        self.place_food_sound.setSource(QUrl.fromLocalFile("./sounds/Placefood.wav"))
        self.place_food_sound.setVolume(1)

        #re-Launch 
        self.relaunch_game_sound = QSoundEffect()
        self.relaunch_game_sound.setSource(QUrl.fromLocalFile("./sounds/Restart.wav"))
        self.relaunch_game_sound.setVolume(0.5)

    def fill_board_with_bomb_effect(self, delay=30):
        bomb_icon = QIcon("Icon/bomb.png")
        total_rows = len(self.Board_core)

        def fill_row(row_index):
            if row_index >= total_rows:
                return
            for btn in self.Board_core[row_index]:
                btn.setIcon(bomb_icon)
            QApplication.processEvents()  # update UI instantly
            QTimer.singleShot(delay, lambda: fill_row(row_index + 1))

        fill_row(0)










