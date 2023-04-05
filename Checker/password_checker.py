from Checker import checker


class Password(checker.Checker):
	def __init__(self, username, password):
		super().__init__(username, password)
		self.checkLengthPassword = self.checkLengthPassword(password)

	def checkLengthPassword(self, password):
		checker.Checker.checkLengthPassword(self,password)
