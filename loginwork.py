positionList = ['assistant']
loginList = []
Workers = {}


class TimerQuery(Checker):

	def __init__(self, username):
		super().__init__(username, password=None)

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
	Login('usr').create()
	Password(username='usr', password='passwd').create()
	Password(username='usr', password='passwd').update('pass')
