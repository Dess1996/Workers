import data
from abc import ABCMeta, abstractmethod
import bcrypt


class CheckerLogin(metaclass=ABCMeta):
	@abstractmethod
	def checkUserNameLogin(self, username):
		LoginFind = data.Workers.get(username)
		if LoginFind:
			assert False, 'Пользователь существует'


class CheckerPassword(metaclass=ABCMeta):
	@abstractmethod
	def checkLengthPassword(self, password):
		if len(password) < 8:
			assert False, 'Пароль должен быть больше 8 символов'

	@abstractmethod
	def checkEncription(self, password):
		pass
