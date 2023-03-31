from login import Login
from database import databaseWorkers


class User:
	def __init__(self, loginname, name, lastName, gender):
		databaseWorkers[-1]['name'] = name
		databaseWorkers[-1]['lastname'] = lastName
		databaseWorkers[-1]['gender'] = gender


if __name__ == '__main__':
	usr = Login.createLogin()
