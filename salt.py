import bcrypt
if __name__ == '__main__':
	salt = bcrypt.gensalt()
	print(salt)
