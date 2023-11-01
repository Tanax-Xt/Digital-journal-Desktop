from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setWindowTitle("О программе")
        message = QLabel("""Цифровой дневник.Desktop\n
«Цифровой дневник. Desktop» – это электронный журнал для учителей и школьников
с поддержкой импорта успеваемости учащихся в виде таблиц формата .csv и экспорта этих данных в форматах .csv и .xlsx. 
В программе доступны три уровня прав: ученик, учитель и администратор.""")
        self.layout.addWidget(message)
        self.setLayout(self.layout)


class AddUserDialog(QDialog):
    def __init__(self):
        super().__init__()
        # self.layout = QVBoxLayout()
        uic.loadUi('ui/reg_new_user.ui')
        self.setWindowTitle("Добавить пользователя")
        # message = QLabel("Введите данные:")
        # message.setFixedWidth(250)
        # self.layout.addWidget(message)
        #
        # self.setLayout(self.layout)
