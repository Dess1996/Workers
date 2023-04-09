import data
from abc import ABCMeta, abstractmethod


class CheckerLogin(metaclass=ABCMeta):
	@abstractmethod
	def checkUserNameLogin(self, username):
		LoginFind = data.Workers.get(username)
		if LoginFind:
			assert False, 'Пользователь не найден'


class CheckerPassword(metaclass=ABCMeta):
	@abstractmethod
	def checkLengthPassword(self, password):
		if len(password) < 8:
			assert False, 'Пароль должен быть больше 8 символов'
