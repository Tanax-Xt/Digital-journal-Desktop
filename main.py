import sys
from hashlib import md5

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

from database import DataBase
from dialog import AboutDialog, AddUserDialog, DelUser


class StartWidget(QMainWindow):
    """Стартовое окно"""

    def __init__(self):
        super().__init__()
        self.load_Ui()
        self.check_authorization()



        # scene = QGraphicsScene(0, 0, 400, 200)
        # scene.addPixmap(QPixmap("data/logo.jpg"))

    def load_Ui(self):
        uic.loadUi('ui/start_window.ui', self)
        self.setWindowTitle("Цифровой дневник.Desktop")
        self.set_logo()
        self.show()
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
        self.main_widget = MainWidget(login)
        self.close()
        self.main_widget.show()

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


class MainWidget(QMainWindow):
    def __init__(self, login):
        super().__init__()
        self.load_ui(login)

    def load_ui(self, login):
        uic.loadUi(f'ui/main_window_{db.get_role(login)}.ui', self)
        self.greetingLabel.setText(f'Вы вошли как, {db.get_name(login)}')
        self.setWindowTitle("Цифровой дневник.Desktop")
        self.set_logo()
        self.logoutButton.clicked.connect(self.logout)
        self.menuBar.addAction(self.action_about)
        self.action_about.triggered.connect(self.about_action)
        if db.get_role(login) == 3:
            self.addUser.clicked.connect(self.add_user)
            self.delUser.clicked.connect(self.del_user)

    def set_logo(self):
        self.pixmap = QPixmap('data/logo_70_70.jpeg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(70, 70)
        self.image.setPixmap(self.pixmap)

    def add_user(self):
        dlg = AddUserDialog(db)
        dlg.exec()

    def del_user(self):
        dlg = DelUser(db)
        dlg.exec()

    def about_action(self):
        '''Обработка "О программе"'''
        dlg = AboutDialog()
        dlg.exec()

    def logout(self):
        with open('data/login.txt', 'w') as f:
            f.write('')
        self.close()
        self.start_widget = StartWidget()
        # self.start_widget.show()


if __name__ == '__main__':
    # print(md5(b'admin').hexdigest())
    db = DataBase('data/database.sqlite')
    app = QApplication(sys.argv)
    ex = StartWidget()
    # ex.show()
    sys.exit(app.exec())
    db.close()
