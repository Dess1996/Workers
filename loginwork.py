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
	if bcrypt.checkpw(b'1hrtyt222333', b'$2b$12$ClxMi2.XMye.wMe2T6g8QuDeOJH/JVzhNGdmvuCvdz90uS4/e6rRy'):
		print('Correct')
