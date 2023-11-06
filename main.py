import sys

from PyQt6.QtWidgets import QApplication

import start_widget
from database import DataBase

if __name__ == '__main__':
    db = DataBase('data/database.sqlite')
    app = QApplication(sys.argv)
    ex = start_widget.StartWidget(db)
    sys.exit(app.exec())
    db.close()
