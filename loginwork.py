from loginDir.login import Login
from loginDir.password import Password
import data


class Credentials(Login, Password):
	def __init__(self, username, password):
		super().__init__(username)
		Login(username).create()
		Password(username=username, password=password).create()
		self.password = password

	def LoginGet(self, user):
		Login(user).get()

	def LoginDelete(self, user):
		Login(user).delete()

	def PasswordUpdate(self, oldPassword, newpassWord):
		Password.update(self.username, oldPassword, newpassWord)


if __name__ == '__main__':
	usr = Credentials('dess', '1hrtyt')
	usr.LoginGet('dess')
	usr.PasswordUpdate('1hrtyt','dess')
	usr.LoginDelete('dess')

	print(data.Workers)
