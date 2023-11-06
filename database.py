import sqlite3


class DataBase:
    def __init__(self, db_file):
        """Инициализация"""
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def user_exists(self, login):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `login` = ?", (login,))
        return bool(len(result.fetchall()))

    def authorize(self, login, password):
        """Проверяем, пароль пользователя"""
        result = self.cursor.execute("SELECT `password` FROM `users` WHERE `login` = ?", (login,))
        return result.fetchall()[0][0] == password

    def get_role(self, login):
        '''Достаем роль пользователя'''
        result = self.cursor.execute("SELECT `role` FROM `users` WHERE `login` = ?", (login,))
        return result.fetchall()[0][0]

    def get_name(self, login):
        result = self.cursor.execute("SELECT name FROM users WHERE login = ?", (login,))
        return result.fetchall()[0][0]

    def get_login(self, name):
        result = self.cursor.execute("SELECT login FROM users WHERE name = ?", (name,))
        return result.fetchall()[0][0]

    def get_role(self, login):
        result = self.cursor.execute("SELECT `role` FROM `users` WHERE `login` = ?", (login,))
        return result.fetchall()[0][0]

    def add_user(self, login, password, name, role):
        role = self.cursor.execute("SELECT `id` FROM `roles` WHERE `name` = ?", (role,)).fetchall()[0][0]
        self.cursor.execute("INSERT INTO `users` (`login`, `password`, `name`, `role`) VALUES (?, ?, ?, ?)",
                            (login, password, name, role))
        if role == 1:
            self.cursor.execute("INSERT INTO `marks` (`login`) VALUES (?)", (login,))
        return self.conn.commit()

    def get_users_name_list(self):
        return list(self.cursor.execute("SELECT name FROM users"))

    def get_users_login_list(self):
        return list(self.cursor.execute("SELECT login FROM users"))

    def get_users_login_list_from_marks(self):
        return list(self.cursor.execute("SELECT login FROM marks"))

    def get_user_marks(self, login):
        return self.cursor.execute("SELECT marks FROM marks WHERE login = ?", (login,)).fetchall()[0][0]

    def del_user(self, name):
        login = self.cursor.execute("SELECT login FROM users WHERE name = ?", (name,)).fetchall()[0][0]
        role = self.cursor.execute("SELECT role FROM users WHERE login = ?", (login,)).fetchall()[0][0]
        self.cursor.execute("DELETE FROM users WHERE name = ?", (name,)).fetchall()
        if role == 1:
            self.cursor.execute("DELETE FROM marks WHERE login = ?", (login,)).fetchall()
        self.conn.commit()

    def subjs_list(self):
        return list(self.cursor.execute("SELECT title FROM lessons"))

    def update_marks(self, login, marks):
        self.cursor.execute("UPDATE marks SET marks = ? WHERE login = ?", (marks, login))
        self.conn.commit()

    def add_subj(self, title):
        if not self.subj_exist(title):
            self.cursor.execute("INSERT INTO lessons (title) VALUES (?)", (title,))
            return self.conn.commit()

    def subj_exist(self, title) -> bool:
        result = self.cursor.execute("SELECT id FROM lessons WHERE title = ?", (title,))
        return bool(len(result.fetchall()))

    def get_subjs_list(self):
        return list(self.cursor.execute("SELECT title FROM lessons"))

    def del_subj(self, title):
        self.cursor.execute("DELETE FROM lessons WHERE title = ?", (title,)).fetchall()
        self.conn.commit()

    def close(self):
        """Закрываем соединение с БД"""
        self.conn.close()
