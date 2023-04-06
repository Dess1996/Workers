from Checker import checker


class Login(checker.Checker):
	def __init__(self, login, password=None):
		super().__init__(login, password)
		self.checkUserNameLogin = self.checkUserNameLogin(login)

	def checkUserNameLogin(self, login):
		checker.Checker.checkUserNameLogin(self,login)



