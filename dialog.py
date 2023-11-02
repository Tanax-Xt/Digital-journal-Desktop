from hashlib import md5
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


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Добавить пользователя")
        Dialog.resize(381, 313)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 260, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 331, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавить пользователя"))
        self.pushButton.setText(_translate("Dialog", "Создать"))
        self.label.setText(_translate("Dialog", "Логин"))
        self.label_3.setText(_translate("Dialog", "Пароль"))
        self.label_4.setText(_translate("Dialog", "ФИО"))
        self.label_2.setText(_translate("Dialog", "Роль"))


class AddUserDialog(QDialog, Ui_Dialog):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setupUi(self)
        roles = ["Ученик", "Учитель", "Администратор"]
        self.comboBox.addItems(roles)
        self.pushButton.clicked.connect(self.add_user)

    def add_user(self):
        login = self.lineEdit.text()
        password = md5(bytes(self.lineEdit_2.text(), encoding='utf-8')).hexdigest()
        name = self.lineEdit_3.text()
        role = self.comboBox.currentText()
        self.db.add_user(login, password, name, role)
        self.close()



class Ui_Dialog_2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 120, 181, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(50, 20, 311, 71))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Удалить пользователя"))
        self.checkBox.setText(_translate("Dialog", "Подтверждаю"))
        self.pushButton.setText(_translate("Dialog", "Удалить"))


class DelUser(QDialog, Ui_Dialog_2):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setupUi(self)
        names = [''.join(i) for i in db.get_users_name_list()]
        print(db.get_users_login_list())
        self.comboBox.addItems(names)
        self.pushButton.clicked.connect(self.del_user)

    def del_user(self):
        if self.checkBox.isChecked():
            name = self.comboBox.currentText()
            self.db.del_user(name)
            self.close()