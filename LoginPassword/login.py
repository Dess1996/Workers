from Checker import checker
from data import Workers


class Login(checker.Checker):
	def __init__(self, username, password=None):
		super().__init__(username, password)

	def create(self):
		if self.LoginChecker:
			raise AttributeError('Пользователь уже существует')
		Workers[self.username] = {'login': self.username}
		print(str(self) + ' создан')

	def delete(self):
		if Workers.get(self.username):
			del Workers[self.username]

		print(str(self) + ' удалён')

	def get(self):
		if self.LoginChecker:
			a = self.username in Workers.keys()
			if a:
				print('Найдены пользователи с логинами: %s' % Workers[self.username]['login'])
			else:
				print('%s не найден' % self)


if __name__ == '__main__':
	usr = Login('dess', '1hrtyt1996')
