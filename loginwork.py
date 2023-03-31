from loginDir.login import Login
from loginDir.password import Password

positionList = ['assistant']
loginList = []

if __name__ == '__main__':
	Login('usr').create()
	Password(username='usr', password='passwd').create()
	Password(username='usr', password='passwd').update('pass')
