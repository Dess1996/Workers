from Checker import checker
from data import Workers


class Login(checker.CheckerLogin):
	def __init__(self, username):
		self.username = username

	def checkUserNameLogin(self, username):
		pass

	def create(self):
		super().checkUserNameLogin(self.username)
		Workers[self.username] = {'login': self.username}
		print(str(self) + ' создан')

	def delete(self):
		if Workers.get(self.username):
			del Workers[self.username]

		print(str(self) + ' удалён')

	def get(self):
		isUserRegestered = self.username in Workers.keys()
		if isUserRegestered:
			print('Найдены пользователи с логинами: %s' % Workers[self.username]['login'])
		else:
			print('%s не найден' % self)

	def __repr__(self):
		return 'Пользователь: %s' % (self.username)


if __name__ == '__main__':
	usr = Login('dess')
	usr.create()
