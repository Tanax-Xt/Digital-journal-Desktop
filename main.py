import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/start_window.ui', self)  # Загружаем дизайн
        scene = QGraphicsScene(0, 0, 400, 200)
        scene.addPixmap(QPixmap("data/logo.jpg"))

        # self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.label.setText("OK")
        # Имя элемента совпадает с objectName в QTDesigner

import hashlib

if __name__ == '__main__':
    # print(hashlib.md5(b'admin_admin').hexdigest())
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())


print(hashlib.md5(bytes(input(), encoding=' utf-8')).hexdigest())

