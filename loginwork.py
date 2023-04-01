from loginDir.login import Login
from loginDir.password import Password


class Credentials(Login, Password):
	def __init__(self, username, password):
		super().__init__(username)
		Login(username).create()
		Password(username=username, password=password).create()

	def LoginGet(self, user):
		Login(user).get()

	def PasswordUpdate(self, newpassWord):
		Password.update(self.password, newpassWord)


if __name__ == '__main__':
	usr = Credentials('dess', '1hrtyt')
	usr.LoginGet('dess')
	usr.PasswordUpdate('4e1d07') #TODO: ошибка
