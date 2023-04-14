import data
from abc import ABCMeta, abstractmethod
import bcrypt
import re


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
	def checkEncription(self, password, employmentPassword):
		passwd = str(password).encode()
		if bcrypt.checkpw(passwd, employmentPassword):
			print('Пароль пользователя %s корректный' % self)
		else:
			assert False, 'Пароли не совпадают'

	@abstractmethod
	def checkOnNumbers(self, password):
		pattern = re.compile(r'[0-9]+')
		NumbersInPassword = re.findall(pattern, password)
		if not NumbersInPassword:
			assert False, 'Пароль не содержит цифр'

	@abstractmethod
	def checkOnUppers(self, password):
		pattern = re.compile(r'[A-Z]+')
		UpperCasesInLetters = re.findall(pattern, password)
		if not UpperCasesInLetters:
			assert False, 'Пароль не содержит заглавных символов'
