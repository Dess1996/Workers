class Login(Checker):
	def __init__(self, username):
		super().__init__(username, password=None)

	def create(self):
		Workers[self.username] = {'login': self.username}
		print(str(self) + ' создан')

	def delete(self):
		if Workers.get(self.username):
			del Workers[self.username]

		print(str(self) + ' удалён')

	def get(self):
		a = Workers.get(self.username)
		print('Найдены пользователи с логинами: %s' % a)
