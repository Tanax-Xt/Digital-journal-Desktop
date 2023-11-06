import sys
from hashlib import md5

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

from database import DataBase
from dialogs import AboutDialog, AddUserDialog, DelUser
import start_widget

if __name__ == '__main__':
    # print(md5(b'admin').hexdigest())
    db = DataBase('data/database.sqlite')
    app = QApplication(sys.argv)
    ex = start_widget.StartWidget(db)
    # ex.show()
    sys.exit(app.exec())
    db.close()
