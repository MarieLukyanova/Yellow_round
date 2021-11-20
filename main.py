import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Желтые окружности')
        self.btn = QPushButton('Новая \n окружнось', self)
        self.btn.resize(140, 60)
        self.btn.move(230, 270)
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
        rgb = [randint(0, 255) for _ in range(3)]
        rad = randint(140, 400)
        qp.setBrush(QColor(rgb[0], rgb[1], rgb[2]))
        qp.drawEllipse((600 - rad) // 2, (600 - rad) // 2, rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
