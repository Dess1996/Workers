from Checker import checker1


class Password(checker1.Checker):
	def __init__(self, username, password):
		super().__init__(username, password)
		self.checkLengthPassword = self.checkLengthPassword(password)

	def checkLengthPassword(self, password):
		checker1.Checker.checkLengthPassword(self,password)
