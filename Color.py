import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QMainWindow


class Example(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.picture_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_flag(qp)
        # Завершаем рисование
        qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        r = random.randint(1, 250)
        x = self.frameGeometry().width() // 2 - r
        y = self.frameGeometry().height() // 2 - r
        color_1 = random.randint(1, 255)
        color_2 = random.randint(1, 255)
        color_3 = random.randint(1, 255)
        qp.setBrush(QColor(color_1, color_2, color_3))
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())