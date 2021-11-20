import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_round(qp)
            qp.end()

    def draw_round(self, qp):
        qp.setBrush(QColor(227, 220, 30))
        r = randint(140, 400)
        qp.drawEllipse((600 - r) // 2, (600 - r) // 2, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
