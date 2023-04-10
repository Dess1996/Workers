from LoginPassword.login import Login
from LoginPassword.password import Password
from Checker import checker
from data import Workers



class Credentials(Login, Password):
	def __init__(self, username, password):
		super().__init__(username)
		Login(username).create()
		Password(username, password).create()

	def LoginGet(self, user):
		Login(user).get()

	def LoginDelete(self, user):
		Login(user).delete()

	def PasswordUpdate(self, OldPassword, newpassWord):
		Password.update(self.username, OldPassword, newpassWord)


if __name__ == '__main__':
	usr = Credentials(username='dess', password='1hrtyt222333')
	usr.LoginGet('dess')
	usr.LoginGet('sue')
	usr.LoginGet('mama')
	usr.PasswordUpdate('1hrtyt222333', '4e1d072006')
	print(Workers) # Output: {'dess': {'login': 'dess', 'password': # b'$2b$12$mX65cK73RNhQHVb.cj8lPOn4Um0LHMRN/e88vPozQXqafHvVk8zY.'}}
