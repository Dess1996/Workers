import data


class Checker:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.LoginChecker = False
		self.PasswordChecker = False
		self.checkUserNameLogin()
		self.checkPassword()

	def checkUserNameLogin(self):
		LoginFind = data.Workers.get(self.username)
		if LoginFind:
			self.LoginChecker = True

	def checkPassword(self):
		if self.password:
			if 'password' in data.Workers[self.username] and data.Workers[self.username]['password'] == self.password:
				self.PasswordChecker = True

	def __str__(self):
		return 'Пользователь %s' % self.username
