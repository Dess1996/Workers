from . import checker
import data


class Password(checker.Checker):
	def __init__(self, username, password):
		super().__init__(username, password)
		self.passwd = password

	def create(self):
		if self.LoginChecker:
			data.Workers[self.username]['password'] = self.passwd
			print(str(self) + ' создал пароль')

	def update(self, newPass):
		print(self.PasswordChecker)
		if self.PasswordChecker:
			data.Workers[self.username][self.passwd] = newPass
			print('Пароль обновлён')
