from Checker import password_checker
import data


class Password(password_checker.Password):
    def __init__(self, username, password):
        super().__init__(username, password)

    def create(self):
        data.Workers[self.username]['password'] = self.password
        print(str(self) + ' создал пароль')

    def update(self, oldPassword, newPass):
        if data.Workers[self]['password'] == oldPassword:
            data.Workers[self]['password'] = newPass
        print('Пароль обновлён')

