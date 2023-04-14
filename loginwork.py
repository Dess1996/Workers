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
	usr = Credentials(username='dess', password='Qwertyiop1234')
	usr.LoginGet('dess')
	usr.LoginGet('sue')
	usr.LoginGet('mama')
	usr.PasswordUpdate('Qwertyiop1234', '4E1d072006')
	print(
		Workers)  # {'dess': {'login': 'dess', 'DateOfCreation': '14-04-2023', 'password': b'$2b$12$5h8OFsPViHT.nKtTYw/RJ.bo7.cT2KtwX4KiUuMmOWCKKqW/w2VD2'}}
