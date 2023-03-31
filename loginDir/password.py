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