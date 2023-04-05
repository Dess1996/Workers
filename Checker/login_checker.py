from Checker import checker1


class Login(checker1.Checker):
	def __init__(self, login, password=None):
		super().__init__(login, password)
		self.checkUserNameLogin = self.checkUserNameLogin(login)

	def checkUserNameLogin(self, login):
		checker1.Checker.checkUserNameLogin(self,login)



