import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("UI.ui", self)
        self.button = QPushButton("Создать окружность", self)
        self.button.setGeometry(10, 10, 200, 50)
        self.button.clicked.connect(self.create_circle)
        # self.label = QLabel("Добро пожаловать!", self)
        # self.label.setGeometry(10, 70, 200, 30)
        self.circle_x = None
        self.circle_y = None
        self.circle_diameter = None

    def create_circle(self):
        self.circle_x = randint(0, self.width())
        self.circle_y = randint(0, self.height())
        self.circle_diameter = randint(10, 100)
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if (
            self.circle_x is not None
            and self.circle_y is not None
            and self.circle_diameter is not None
        ):
            qp = QPainter(self)
            qp.setBrush(QBrush(QColor(255, 255, 0)))
            qp.setRenderHint(QPainter.Antialiasing)
            qp.drawEllipse(
                self.circle_x, self.circle_y, self.circle_diameter, self.circle_diameter
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
