
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import QMainWindow, QLabel

from dialogs import AboutDialog, AddUserDialog, DelUser
import start_widget

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
            self.teacher_table()

    def teacher_table(self):
        logins = [''.join(i) for i in self.db.get_users_login_list_from_marks()]
        marks = {}
        subj = []
        for i in logins:
            user_marks = {}
            if self.db.get_user_marks(i) is not None:
                for s_m in self.db.get_user_marks(i)[1:-1].split(';'):
                    s, m = s_m.split(':')
                    s = s[1:-1]
                    m = list(map(str, m[1:-1].split(',')))
                    user_marks[s] = m
                marks[self.db.get_name(i)] = user_marks
                subj.extend(list(user_marks.keys()))
            else:
                marks[self.db.get_name(i)] = {}
        subj = list(set(subj))
        subj.sort()
        logins.sort(key=lambda x: self.db.get_name(x))

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
        ...

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

    def del_user(self):
        dlg = DelUser(self.db)
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
        self.start_widget = start_widget.StartWidget(self.db)
        # self.start_widget.show()
