import sys
from hashlib import md5

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

from database import DataBase
from dialog import AboutDialog, AddUserDialog


class MainWindow(QMainWindow):
    """Главное окно"""

    def __init__(self):
        super().__init__()
        self.check_authorization()
        self.load_Ui()
        # scene = QGraphicsScene(0, 0, 400, 200)
        # scene.addPixmap(QPixmap("data/logo.jpg"))

    def load_Ui(self):
        uic.loadUi('ui/start_window.ui', self)
        self.setWindowTitle("Цифровой дневник.Desktop")
        self.set_logo()
        self.loginButton.clicked.connect(self.authorization)
        self.action_about.triggered.connect(self.about_action)

    def set_logo(self):
        self.pixmap = QPixmap('data/logo_70_70.jpeg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(70, 70)
        self.image.setPixmap(self.pixmap)

    def check_authorization(self):
        import os
        if os.path.isfile('data/login.txt'):
            with open('data/login.txt', 'r', encoding='utf-8') as f:
                try:
                    login, password = f.read().split('\n')
                    if db.user_exists(login) and db.authorize(login, password):
                        self.load_main_widget(login)
                except:
                    pass

    def add_authorization(self, login, password):
        with open('data/login.txt', 'w', encoding='utf-8') as f:
            f.write(login + '\n' + md5(bytes(password, encoding=' utf-8')).hexdigest())

    def load_main_widget(self, login):
        uic.loadUi(f'ui/main_window_{db.get_role(login)}.ui', self)
        self.greetingLabel.setText(f'Вы вошли как, {db.get_name(login)}')
        self.setWindowTitle("Цифровой дневник.Desktop")
        self.set_logo()
        self.logoutButton.clicked.connect(self.logout)
        self.addUser.clicked.connect(self.add_user)
        self.menuBar.addAction(self.action_about)
        self.action_about.triggered.connect(self.about_action)

    def add_user(self):
        dlg = AddUserDialog()
        dlg.exec()

    def logout(self):
        self.load_Ui()
        with open('data/login.txt', 'w') as f:
            f.write('')

    def about_action(self):
        '''Обработка "О программе"'''
        dlg = AboutDialog()
        dlg.exec()

    def authorization(self):
        """Авторизация"""
        login = self.loginLine.text()
        password = self.passwordLine.text()
        if db.user_exists(login):
            if db.authorize(login, md5(bytes(password, encoding=' utf-8')).hexdigest()):
                self.add_authorization(login, password)
                self.load_main_widget(login)
                # self.loginLayout.setVisible(False)

            else:
                self.passwordLine.setText('Неверный пароль')
        else:
            self.loginLine.setText('Неверный логин')
            self.passwordLine.setText('')


# class AboutDialog(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.layout = QVBoxLayout()
#         self.setWindowTitle("О программе")
#         message = QLabel("""Цифровой дневник.Desktop\n
# «Цифровой дневник. Desktop» – это электронный журнал для учителей и школьников
# с поддержкой импорта успеваемости учащихся в виде таблиц формата .csv и экспорта этих данных в форматах .csv и .xlsx.
# В программе доступны три уровня прав: ученик, учитель и администратор.""")
#         self.layout.addWidget(message)
#         self.setLayout(self.layout)

if __name__ == '__main__':
    # print(hashlib.md5(b'admin_admin').hexdigest())
    db = DataBase('data/database.sqlite')
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
    db.close()
