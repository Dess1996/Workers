import data


class Checker:
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def checkUserNameLogin(self, username):
		LoginFind = data.Workers.get(self.username)
		if LoginFind:
			self.LoginChecker = True

	def checkLengthPassword(self, password):
		if len(password) < 8:
			raise AttributeError('Пароль должен быть больше 8 символов')

	def __str__(self):
		return 'Пользователь %s' % self.username
