import sys
from hashlib import md5

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QWidget

from database import DataBase


class MainWindow(QMainWindow):
    """Главное окно"""

    def __init__(self):
        super().__init__()
        uic.loadUi('ui/start_window.ui', self)  # Загружаем дизайн
        self.setWindowTitle("Цифровой дневник.Desktop")
        # scene = QGraphicsScene(0, 0, 400, 200)
        # scene.addPixmap(QPixmap("data/logo.jpg"))
        self.loginButton.clicked.connect(self.login)
        self.action_about.triggered.connect(self.about_action)

    def about_action(self):
        '''Обработка "О программе"'''
        dlg = AboutDialog()
        dlg.exec()

    def login(self):
        """Авторизация"""
        login = self.loginLine.text()
        password = self.passwordLine.text()
        if db.user_exists(login):
            if db.authorize(login, md5(bytes(password, encoding=' utf-8')).hexdigest()):
                print('ok')
                # self.loginLayout.setVisible(False)
                self.loginLine.setVisible(False)
                self.passwordLine.setVisible(False)
                self.loginText.setVisible(False)
                self.passwordText.setVisible(False)
                self.loginButton.setVisible(False)
                uic.loadUi(f'ui/main_window_{db.get_role(login)}.ui', self)
                self.setWindowTitle("Цифровой дневник.Desktop")
            else:
                self.passwordLine.setText('Неверный пароль')
        else:
            self.loginLine.setText('Неверный логин')
            self.passwordLine.setText('')


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("О программе")
        self.layout = QVBoxLayout()
        message = QLabel("""Цифровой дневник.Desktop\n
«Цифровой дневник. Desktop» – это электронный журнал для учителей и школьников
с поддержкой импорта успеваемости учащихся в виде таблиц формата .csv и экспорта этих данных в форматах .csv и .xlsx. 
В программе доступны три уровня прав: ученик, учитель и администратор.""")
        self.layout.addWidget(message)
        self.setLayout(self.layout)


if __name__ == '__main__':
    # print(hashlib.md5(b'admin_admin').hexdigest())
    db = DataBase('data/database.sqlite')
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

print(md5(bytes(input(), encoding=' utf-8')).hexdigest())
