import sys
from hashlib import md5

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

from database import DataBase
from dialog import AboutDialog, AddUserDialog, DelUser


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(1440, 780)
        StartWindow.setMinimumSize(QtCore.QSize(1440, 780))
        StartWindow.setMaximumSize(QtCore.QSize(1440, 780))
        self.centralwidget = QtWidgets.QWidget(parent=StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(590, 250, 291, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.loginLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.loginLayout.setContentsMargins(0, 0, 0, 0)
        self.loginLayout.setObjectName("loginLayout")
        self.loginButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.loginButton.setMaximumSize(QtCore.QSize(175, 35))
        self.loginButton.setObjectName("loginButton")
        self.loginLayout.addWidget(self.loginButton, 4, 0, 1, 1)
        self.passwordLine = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.passwordLine.setMaximumSize(QtCore.QSize(170, 25))
        self.passwordLine.setObjectName("passwordLine")
        self.loginLayout.addWidget(self.passwordLine, 3, 0, 1, 1)
        self.loginLine = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.loginLine.setMaximumSize(QtCore.QSize(170, 25))
        self.loginLine.setObjectName("loginLine")
        self.loginLayout.addWidget(self.loginLine, 1, 0, 1, 1)
        self.loginText = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.loginText.setMinimumSize(QtCore.QSize(170, 25))
        self.loginText.setMaximumSize(QtCore.QSize(170, 25))
        self.loginText.setObjectName("loginText")
        self.loginLayout.addWidget(self.loginText, 0, 0, 1, 1)
        self.passwordText = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.passwordText.setMinimumSize(QtCore.QSize(170, 25))
        self.passwordText.setMaximumSize(QtCore.QSize(170, 25))
        self.passwordText.setObjectName("passwordText")
        self.loginLayout.addWidget(self.passwordText, 2, 0, 1, 1)
        StartWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(parent=StartWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1440, 24))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(parent=self.menuBar)
        self.menu.setObjectName("menu")
        StartWindow.setMenuBar(self.menuBar)
        self.actionkvf = QtGui.QAction(parent=StartWindow)
        self.actionkvf.setObjectName("actionkvf")
        self.action_about = QtGui.QAction(parent=StartWindow)
        self.action_about.setObjectName("action_about")
        self.action_quit = QtGui.QAction(parent=StartWindow)
        self.action_quit.setObjectName("action_quit")
        self.menu.addAction(self.action_about)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "MainWindow"))
        self.loginButton.setText(_translate("StartWindow", "Войти"))
        self.passwordLine.setText(_translate("StartWindow", "password"))
        self.loginLine.setText(_translate("StartWindow", "login"))
        self.loginText.setText(_translate("StartWindow", "Login:"))
        self.passwordText.setText(_translate("StartWindow", "Password:"))
        self.menu.setTitle(_translate("StartWindow", "Цифровой дневник"))
        self.actionkvf.setText(_translate("StartWindow", "kvf"))
        self.action_about.setText(_translate("StartWindow", "О программе"))
        self.action_quit.setText(_translate("StartWindow", "Закрыть"))


class StartWidget(QMainWindow, Ui_StartWindow):
    """Стартовое окно"""

    def __init__(self):
        super().__init__()
        self.load_Ui()
        self.check_authorization()

    def load_Ui(self):
        self.setupUi(self)
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
            self.teacher_table()
        if db.get_role(login) == 2:
            self.teacher_table()

    def teacher_table(self):
        logins = [''.join(i) for i in db.get_users_login_list_from_marks()]
        marks = {}
        subj = []
        for i in logins:
            user_marks = {}
            if db.get_user_marks(i) is not None:
                for s_m in db.get_user_marks(i)[1:-1].split(';'):
                    s, m = s_m.split(':')
                    s = s[1:-1]
                    m = list(map(str, m[1:-1].split(',')))
                    user_marks[s] = m
                marks[db.get_name(i)] = user_marks
                subj.extend(list(user_marks.keys()))
            else:
                marks[db.get_name(i)] = {}
        subj = list(set(subj))
        subj.sort()
        logins.sort(key=lambda x: db.get_name(x))

        self.model = QStandardItemModel(len(logins), len(subj) + 1)
        self.model.setHorizontalHeaderLabels(["Имя", *subj])

        for row in range(len(logins)):
            for column in range(len(subj) + 1):
                name = db.get_name(logins[row])
                if column == 0:
                    item = QStandardItem(name)
                else:
                    if subj[column - 1] in marks[name]:
                        item = QStandardItem(', '.join(marks[name][subj[column - 1]]))
                self.model.setItem(row, column, item)
        self.tableView.setModel(self.model)

    def set_logo(self):
        self.pixmap = QPixmap('data/logo_70_70.jpeg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(70, 70)
        self.image.setPixmap(self.pixmap)

    def add_user(self):
        dlg = AddUserDialog(db)
        dlg.exec()
        self.teacher_table()

    def del_user(self):
        dlg = DelUser(db)
        dlg.exec()
        self.teacher_table()

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
