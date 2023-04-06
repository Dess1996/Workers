import data


class Checker:
	def __init__(self, username, password):
		self.LoginChecker = self.checkUserNameLogin(username)
		self.username = username
		self.password = password

	def checkUserNameLogin(self, username):
		LoginFind = data.Workers.get(username)
		if LoginFind:
			return True

	def checkLengthPassword(self, password):
		if len(password) < 8:
			raise AttributeError('Пароль должен быть больше 8 символов')
		else:
			self.checkLenPassword = True

	def __str__(self):
		return 'Пользователь %s' % self.username
