from Checker import login_checker
from data import Workers


class Login(login_checker.Login):
    def __init__(self, username, password=None):
        super().__init__(username, password)

    def create(self):
        Workers[self.username] = {'login': self.username}
        print(str(self) + ' создан')

    def delete(self):
        if Workers.get(self.username):
            del Workers[self.username]

        print(str(self) + ' удалён')

    def get(self):
        a = self.username in Workers.keys()
        if a:
            print('Найдены пользователи с логинами: %s' % Workers[self.username]['login'])
        else:
            print('%s не найден' % self)

