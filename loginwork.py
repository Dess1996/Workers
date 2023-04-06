from LoginPassword.login import Login
from LoginPassword.password import Password
import data


class Credentials(Login, Password):
	def __init__(self, username, password):
		super().__init__(username, password)
		Login(username, password).create()
		Password(username, password).create()

	def LoginGet(self, user):
		Login(user).get()

	def LoginDelete(self, user):
		Login(user).delete()

	def PasswordUpdate(self, oldPassword, newpassWord):
		Password.update(self.username, oldPassword, newpassWord)


if __name__ == '__main__':
	usr = Credentials(username='dess', password='1hrtyt222333')
	usr2 = Credentials(username='sue', password='1hrtyt23333')
	usr.LoginGet('dess')
	usr.LoginGet('sue')
	usr.LoginGet('mama')
	usr.PasswordUpdate('1hrtyt', 'dess')
	usr.LoginDelete('dess')
	print(data.Workers)
