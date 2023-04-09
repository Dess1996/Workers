from Checker import checker
import data


class Password(checker.CheckerPassword):
    def __init__(self, username, password):
        self.password = password
        self.username = username


    def checkLengthPassword(self, password):
        pass

    def create(self):
        super().checkLengthPassword(self.password)
        data.Workers[self.username]['password'] = self.password

    def update(self, oldPassword, newPass):
#        super().checkLengthPassword(self.password) TODO: почему так не работает?
        checker.CheckerPassword.checkLengthPassword(self, newPass)
        if data.Workers[self]['password'] == oldPassword:
            data.Workers[self]['password'] = newPass
            print('Пароль обновлён')
        else:
            raise AttributeError('Вы не ввели старый пароль')



