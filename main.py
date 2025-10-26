from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette,QColor
import Board
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.commitDataRequest
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("white"))
    app.setPalette(palette)
    demo = Board.Board()
    demo.show()
    sys.exit(app.exec())
