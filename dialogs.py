from hashlib import md5

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QGraphicsScene

from chart import Chart


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


class Ui_Dialog_3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(582, 444)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 280, 241, 141))
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 50, 481, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.subjTitle = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.subjTitle.setObjectName("subjTitle")
        self.horizontalLayout.addWidget(self.subjTitle)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавить предмет"))
        self.checkBox.setText(_translate("Dialog", "Подтверждаю"))
        self.pushButton.setText(_translate("Dialog", "Добавить"))
        self.label.setText(_translate("Dialog", "Название предмета"))


class Ui_Dialog_4(object):
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
        Dialog.setWindowTitle(_translate("Dialog", "Удалить предмет"))
        self.checkBox.setText(_translate("Dialog", "Подтверждаю"))
        self.pushButton.setText(_translate("Dialog", "Удалить"))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(661, 519)
        self.graphicsView = QtWidgets.QGraphicsView(parent=Form)
        self.graphicsView.setGeometry(QtCore.QRect(40, 40, 581, 381))
        self.graphicsView.setObjectName("graphicsView")
        self.closeButton = QtWidgets.QPushButton(parent=Form)
        self.closeButton.setGeometry(QtCore.QRect(270, 450, 113, 32))
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Успеваемость"))
        self.closeButton.setText(_translate("Form", "Закрыть"))


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


class DelUserDialog(QDialog, Ui_Dialog_2):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setupUi(self)
        names = [''.join(i) for i in db.get_users_name_list()]
        self.comboBox.addItems(sorted(names))
        self.pushButton.clicked.connect(self.del_user)

    def del_user(self):
        if self.checkBox.isChecked():
            name = self.comboBox.currentText()
            self.db.del_user(name)
            self.close()


class AddSubjDialog(QDialog, Ui_Dialog_3):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_subj)

    def add_subj(self):
        title = self.subjTitle.text()
        self.db.add_subj(title)
        self.close()


class DelSubjDialog(QDialog, Ui_Dialog_4):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setupUi(self)
        subjs = [''.join(i) for i in db.get_subjs_list()]
        self.comboBox.addItems(sorted(subjs))
        self.pushButton.clicked.connect(self.del_subj)

    def del_subj(self):
        if self.checkBox.isChecked():
            subj = self.comboBox.currentText()
            self.db.del_subj(subj)
            self.close()


class ChartDialog(QDialog, Ui_Form):
    def __init__(self, model, db):
        super().__init__()
        self.setupUi(self)
        chart = Chart(model, db)
        chart.marks()
        scene = QGraphicsScene()
        scene.addWidget(chart)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()

        self.closeButton.clicked.connect(self.close_chart)

    def close_chart(self):
        self.close()
