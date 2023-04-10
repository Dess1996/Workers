from Checker import checker
import data, salt
import bcrypt


class Password(checker.CheckerPassword):
    def __init__(self, username, password):
        self.password = password
        self.username = username

    def checkLengthPassword(self, password):
        pass

    def create(self):
        super().checkLengthPassword(self.password)
        password = str.encode(self.password)
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        data.Workers[self.username]['password'] = hashed

    def update(self, oldPassword, newPass):
        checker.CheckerPassword.checkLengthPassword(self, newPass)
        if data.Workers[self]['password'] == oldPassword:
            data.Workers[self]['password'] = newPass
            print('Пароль обновлён')
        else:
            raise AttributeError('Вы не ввели ваш старый пароль')

