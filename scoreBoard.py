#------------------------------------------------
#------------------ ScoreBoard ------------------
#------------------------------------------------
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout, QLCDNumber,QLabel
class Scoreboard(QWidget):
    def __init__(self, score=0):
        super().__init__()
        self.score = int(score)
        self.play_time = None

    def reset_score(self):
        self.score = 0

    def update_score(self, value=0):
        raise NotImplementedError("to be useed in Subclasses")


class LCDScoreboard(Scoreboard):
    def __init__(self, start_text = "Score Secured : " ,display_digits = 4,initial_score = 0 ):
        super().__init__(initial_score)
        self.lcd = QLCDNumber()
        self.label_name = QLabel()
        self.label_name.setText(start_text)
        self.lcd.setDigitCount(display_digits)
        self.lcd.display(f"{initial_score}")
        Hbox = QHBoxLayout()
        Hbox.addWidget(self.label_name)
        Hbox.addWidget(self.lcd)
        layout = QVBoxLayout()
        layout.addLayout(Hbox)
        self.setLayout(layout)

    def update_score(self, value = 0):
        self.score += value
        self.lcd.display(self.score)

class LabelScoreBoard(Scoreboard):
    def __init__(self,start_text = "Score Secured : " ,initial_score = 0):
        super().__init__(initial_score)
        self.label_name = QLabel()
        self.label_name.setText(start_text)
        self.label = QLabel("<b>Score:</b> <span style='color:green'>100</span>")
        self.label.setText(f"{initial_score}")
        Hbox = QHBoxLayout()
        Hbox.addWidget(self.label_name)
        Hbox.addWidget(self.label)
        layout = QVBoxLayout()
        layout.addLayout(Hbox)
        self.setLayout(layout)

    def update_score(self, value = 0):
        self.score += value
        self.label.setText(str(self.score))

