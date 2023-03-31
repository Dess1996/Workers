positionList = ['assistant']
loginList = []
Workers = []


class Checker:
	def __init__(self, username):
		self.username = username
		self.LoginChecker = False
		self.checkUserNameLogin()

	def checkUserNameLogin(self):
		LoginFind = list(filter(lambda user: user['login'] == self.username, Workers))
		if LoginFind:
			self.LoginChecker = True

	def __str__(self):
		return 'Пользователь %s' % self.username


class Login(Checker):
	def __init__(self, username):
		super().__init__(username)

	def create(self):
		Workers.append({'login': self.username})
		print(str(self) + ' создан')

	def delete(self):
		for i in range(len(Workers)):
			if Workers[i]['login'] == self.username:
				del Workers[i]
				break
		print(str(self) + ' удалён')

	def get(self):
		a = list(filter(lambda user: user['login'] == self.username, Workers))
		print('Найдены пользователи с логинами: %s' % ' '.join(i['login'] for i in a))


class TimerQuery(Checker):

	def __init__(self, username):
		super().__init__(username)

	def calculateTimeDuration(self):
		import time
		if self.LoginChecker:
			nowTime = time.time()
			Login(self.username).get()
			futureTime = time.time()
			print('Время поиска: %0.2f секунд' % (futureTime - nowTime))
		else:
			print('Пользователя не существует')


if __name__ == '__main__':
	import random

	b = random.randint(0, 10_000)
	for i in range(10_000):
		Login(str(i)).create()
	TimerQuery(str(b)).calculateTimeDuration()
