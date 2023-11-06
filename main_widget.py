import csv

import xlsxwriter
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import QMainWindow, QLabel

import start_widget
from dialogs import AboutDialog, AddUserDialog, DelUserDialog, AddSubjDialog, DelSubjDialog


class MainWidget(QMainWindow):
    def __init__(self, login, db):
        super().__init__()
        self.db = db
        self.load_ui(login)

    def load_ui(self, login):
        uic.loadUi(f'ui/main_window_{self.db.get_role(login)}.ui', self)
        self.greetingLabel.setText(f'Вы вошли как, {self.db.get_name(login)}')
        self.setWindowTitle("Цифровой дневник.Desktop")
        self.set_logo()
        self.logoutButton.clicked.connect(self.logout)
        self.menuBar.addAction(self.action_about)
        self.action_about.triggered.connect(self.about_action)
        if self.db.get_role(login) == 3:
            self.addUser.clicked.connect(self.add_user)
            self.delUser.clicked.connect(self.del_user)
        if self.db.get_role(login) in [2, 3]:
            self.saveButton.clicked.connect(self.save_table)
            self.addSubj.clicked.connect(self.add_subj)
            self.delSubj.clicked.connect(self.del_subj)
            self.exselExport.clicked.connect(self.teacher_exsel_export)
            self.csvExport.clicked.connect(self.teacher_csv_export)
            self.teacher_table()
        if self.db.get_role(login) == 1:
            ...

    def teacher_table(self):
        logins = sorted([''.join(i) for i in self.db.get_users_login_list_from_marks()],
                        key=lambda x: self.db.get_name(x))
        marks = {}
        subj = sorted(map(lambda x: x[0], self.db.subjs_list()))
        for i in logins:
            user_marks = {}
            if self.db.get_user_marks(i) is not None:
                for s_m in self.db.get_user_marks(i)[1:-1].split(';'):
                    s, m = s_m.split(':')
                    s = s[1:-1]
                    m = list(map(str, m[1:-1].split(',')))
                    user_marks[s] = m
                marks[self.db.get_name(i)] = user_marks
            else:
                marks[self.db.get_name(i)] = {}

        self.model = QStandardItemModel(len(logins), len(subj) + 1)
        self.model.setHorizontalHeaderLabels(["Имя", *subj])

        for row in range(len(logins)):
            for column in range(len(subj) + 1):
                name = self.db.get_name(logins[row])
                if column == 0:
                    item = QStandardItem(name)
                else:
                    if subj[column - 1] in marks[name]:
                        item = QStandardItem(', '.join(marks[name][subj[column - 1]]))
                self.model.setItem(row, column, item)
        self.tableView.setModel(self.model)

    def save_table(self):
        logins = sorted([''.join(i) for i in self.db.get_users_login_list_from_marks()],
                        key=lambda x: self.db.get_name(x))
        subj = sorted(map(lambda x: x[0], self.db.subjs_list()))
        for row in range(len(logins)):
            user_marks = '{'
            user_login = self.db.get_login(self.model.index(row, 0).data())
            for column in range(1, len(subj) + 1):
                marks = self.model.index(row, column).data()
                if marks is not None:
                    user_marks += f"'{subj[column - 1]}':[{''.join(marks.split())}];"
            user_marks = user_marks[:-1] + '}'
            if len(user_marks) == 1:
                user_marks = None
            self.db.update_marks(user_login, user_marks)

    def set_logo(self):
        self.pixmap = QPixmap('data/logo_70_70.jpeg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(70, 70)
        self.image.setPixmap(self.pixmap)

    def add_user(self):
        dlg = AddUserDialog(self.db)
        dlg.exec()
        self.teacher_table()

    def add_subj(self):
        dlg = AddSubjDialog(self.db)
        dlg.exec()
        self.teacher_table()

    def del_subj(self):
        dlg = DelSubjDialog(self.db)
        dlg.exec()
        self.teacher_table()

    def del_user(self):
        dlg = DelUserDialog(self.db)
        dlg.exec()
        self.teacher_table()

    def about_action(self):
        '''Обработка "О программе"'''
        dlg = AboutDialog()
        dlg.exec()

    def teacher_exsel_export(self):
        workbook = xlsxwriter.Workbook('files/Успеваемость.xlsx')
        worksheet = workbook.add_worksheet()

        subj = sorted(map(lambda x: x[0], self.db.subjs_list()))
        logins = sorted([''.join(i) for i in self.db.get_users_login_list_from_marks()],
                        key=lambda x: self.db.get_name(x))

        for column in range(len(subj) + 1):
            if column == 0:
                worksheet.write(0, column, 'Имя')
            else:
                worksheet.write(0, column, subj[column - 1])

        for row in range(len(logins)):
            for column in range(len(subj) + 1):
                worksheet.write(row + 1, column, self.model.index(row, column).data())

        workbook.close()

    def teacher_csv_export(self):
        with open('files/Успеваемость.csv', 'w', newline='', encoding="utf8") as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            subj = sorted(map(lambda x: x[0], self.db.subjs_list()))
            logins = sorted([''.join(i) for i in self.db.get_users_login_list_from_marks()],
                            key=lambda x: self.db.get_name(x))
            writer.writerow(['Имя', *subj])
            for row in range(len(logins)):
                col = []
                for column in range(len(subj) + 1):
                    col.append(self.model.index(row, column).data())
                writer.writerow(col)

    def logout(self):
        with open('data/login.txt', 'w') as f:
            f.write('')
        self.close()
        self.start_widget = start_widget.StartWidget(self.db)
        # self.start_widget.show()
