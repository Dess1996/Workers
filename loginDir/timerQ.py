from . import checker
import time


class TimerQuery(checker.Checker):

	def __init__(self, username):
		super().__init__(username, password=None)

	def calculateTimeDuration(self):

		if self.LoginChecker:
			nowTime = time.time()
			Login(self.username).get()
			futureTime = time.time()
			print('Время поиска: %0.2f секунд' % (futureTime - nowTime))
		else:
			print('Пользователя не существует')
