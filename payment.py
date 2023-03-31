import warnings

# TODO: Если человек женщина, возможно потребуется изменение фамилии
profDict = {'assistant': 270}

emplist = [{'login': 'emp1', 'name': 'Mikhail', 'lastName': 'Ivashkin', 'position': 'assistant', 'pairs': 10},
		   {'login': 'emp2', 'name': 'Mike', 'lastName': 'Ivanov', 'position': 'assistant', 'pairs': 5, }]


class Profession:
	onePair = 2

	def __init__(self, name, LastName, position):
		self.name = name
		self.LastName = LastName
		self.position = position
		self.positionFind = self.ifFindPosition()
		self.pairs = 0
		self.salary = 0

	def ifFindPosition(self):
		return self.position in profDict

	def setPairs(self, numberPairs):
		if self.positionFind:
			self.pairs = numberPairs
		else:
			raise Exception('Позиция %s обнаружена не была' % self.position)

	def calculateSalary(self):
		if self.positionFind and self.pairs > 0:
			self.salary = profDict[self.position] * Profession.onePair * self.pairs

	def __str__(self):
		return 'к выплате: %d рублей' % self.salary



for i in emplist:
	i['login'] = Profession(i['name'], i['lastName'], i['position'])
	pairs = i['pairs']
	if pairs == 0:
		warnings.warn('%s: Количество пар  равно 0' % i['lastName'])
	i['login'].setPairs(pairs)
	i["login"].calculateSalary()
	print('%s: %s' % (i['lastName'], i['login']))
