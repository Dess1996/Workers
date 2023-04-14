from abc import ABCMeta, abstractmethod
from datetime import datetime


class DateTimer(metaclass=ABCMeta):
	@abstractmethod
	def setCurrentTime(self):
		nowTime = datetime.now()
		return nowTime.strftime('%d-%m-%Y')

