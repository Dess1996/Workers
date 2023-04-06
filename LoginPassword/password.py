from Checker import checker
import data


class Password(checker.Checker):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.chPass = self.checkLengthPassword(password)


    def create(self):
        data.Workers[self.username]['password'] = self.password
        print(str(self) + ' создал пароль')

    def update(self, oldPassword, newPass):
        if data.Workers[self]['password'] == oldPassword:
            data.Workers[self]['password'] = newPass
            print('Пароль обновлён')
        else:
            raise AttributeError('Вы не ввели старый пароль')



if __name__ == '__main__':
    usr = Password('dess', '1hrtyt1996')