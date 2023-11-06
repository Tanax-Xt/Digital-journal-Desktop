from hashlib import md5

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QLabel

from dialogs import AboutDialog
from main_widget import MainWidget


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
    def __init__(self, db):
        super().__init__()
        self.db = db
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
                    if self.db.user_exists(login) and self.db.authorize(login, password):
                        self.load_main_widget(login)
                except:
                    pass

    def add_authorization(self, login, password):
        with open('data/login.txt', 'w', encoding='utf-8') as f:
            f.write(login + '\n' + md5(bytes(password, encoding=' utf-8')).hexdigest())

    def load_main_widget(self, login):
        self.main_widget = MainWidget(login, self.db)
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
        if self.db.user_exists(login):
            if self.db.authorize(login, md5(bytes(password, encoding=' utf-8')).hexdigest()):
                self.add_authorization(login, password)
                self.load_main_widget(login)
                # self.loginLayout.setVisible(False)
            else:
                self.passwordLine.setText('Неверный пароль')
        else:
            self.loginLine.setText('Неверный логин')
            self.passwordLine.setText('')