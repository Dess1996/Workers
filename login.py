positionList = ['assistant']
loginList = []
Workers = {}


class Checker:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.LoginChecker = False
		self.PasswordChecker = False
		self.checkUserNameLogin()
		self.checkPassword()


	def checkUserNameLogin(self):
		LoginFind = Workers.get(self.username)
		if LoginFind:
			self.LoginChecker = True

	def checkPassword(self):
		if self.password:
			if 'password' in Workers[self.username] and Workers[self.username]['password'] == self.password:
					self.PasswordChecker = True
	def __str__(self):
		return 'Пользователь %s' % self.username


class Login(Checker):
	def __init__(self, username):
		super().__init__(username, password=None)

	def create(self):
		Workers[self.username] = {'login': self.username}
		print(str(self) + ' создан')

	def delete(self):
		if Workers.get(self.username):
			del Workers[self.username]

		print(str(self) + ' удалён')

	def get(self):
		a = Workers.get(self.username)
		print('Найдены пользователи с логинами: %s' % a)


class Password(Checker):
	def __init__(self, username, password):
		super().__init__(username, password)
		self.passwd = password

	def create(self):
		if self.LoginChecker:
			Workers[self.username]['password'] = self.passwd
			print(str(self) + ' создал пароль')

	def update(self, newPass):
		if self.PasswordChecker:
			Workers[self.username][self.passwd] = newPass
			print('Пароль обновлён')


class TimerQuery(Checker):

	def __init__(self, username):
		super().__init__(username, password=None)

	def calculateTimeDuration(self):
		import time
		if self.LoginChecker:
			nowTime = time.time()
			Login(self.username).get()
			futureTime = time.time()
			print('Время поиска: %0.2f секунд' % (futureTime - nowTime))
		else:
			print('Пользователя не существует')


if __name__ == '__main__':
	Login('usr').create()
	Password(username='usr', password='passwd').create()
	Password(username='usr', password='passwd').update('pass')
