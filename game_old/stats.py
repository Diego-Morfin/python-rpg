class Stats:
	def __init__(self, maxHealth, attack, defense, speed):
		self.mMaxHP = maxHealth
		self.mAttack = attack
		self.mDefense = defense
		self.mSpeed = speed
		self.mCurrentHP = self.mMaxHP
		return

	def getMaxHP(self):
		return self.mMaxHP

	def getAttack(self):
		return self.mAttack

	def getDefense(self):
		return self.mDefense

	def getSpeed(self):
		return self.mSpeed
		
	def setMaxHP(self, health):
		self.mMaxHP = health
		return

	def setAttack(self, attack):
		self.mAttack = attack
		return

	def setDefense(self, defense):
		self.mDefense = defense
		return

	def setSpeed(self, speed):
		self.mSpeed = speed
		return