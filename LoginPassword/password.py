from Checker import checker
import data
import bcrypt


class Password(checker.CheckerPassword):
	def __init__(self, username, password):
		self.password = password
		self.username = username

	def checkLengthPassword(self, password):
		pass

	def checkEncription(self, password, employmentPassword):
		pass

	def checkOnNumbers(self, password):
		pass

	def checkOnUppers(self, password):
		pass

	def create(self):
		super().checkLengthPassword(self.password)
		super().checkOnNumbers(self.password)
		super().checkOnUppers(self.password)

		password = str.encode(self.password)
		hashed = bcrypt.hashpw(password, bcrypt.gensalt())
		data.Workers[self.username]['password'] = hashed

	def update(self, oldPassword, newPass):
		emplPassword = data.Workers[self]['password']
		checker.CheckerPassword.checkEncription(self, oldPassword, emplPassword)
		Password(self, newPass).create()
		print('Пароль обновлён')
