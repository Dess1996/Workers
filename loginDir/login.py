from . import checker
import data



class Login(checker.Checker):
	def __init__(self, username):
		super().__init__(username, password=None)

	def create(self):
		data.Workers[self.username] = {'login': self.username}
		print(str(self) + ' создан')

	def delete(self):
		if data.Workers.get(self.username):
			del Workers[self.username]

		print(str(self) + ' удалён')

	def get(self):
		a = data.Workers.get(self.username)
		print('Найдены пользователи с логинами: %s' % a)

print('Hello world')