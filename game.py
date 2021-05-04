import playerOne, playerTwo, attacks, moves
import random

class Game(moves.Moves):
	def __init__(self):
		self.mPlayerOne = playerOne.PlayerOne(100, 100, 100, 100)
		self.mPlayerTwo = playerTwo.PlayerTwo(100, 100, 100, 100)
		moves.Moves.__init__(self)
		return

	def setPlayerOneStats(self, health, speed, attack, defense):
		self.mPlayerOne.setMaxHP(health)
		self.mPlayerOne.setSpeed(speed)
		self.mPlayerOne.setAttack(attack)
		self.mPlayerOne.setDefense(defense)
		return

	def setPlayerTwoStats(self, health, speed, attack, defense):
		self.mPlayerTwo.setMaxHP(health)
		self.mPlayerTwo.setSpeed(speed)
		self.mPlayerTwo.setAttack(attack)
		self.mPlayerTwo.setDefense(defense)
		return

	def getPlayerOneStats(self):
		print(self.mPlayerOne.getMaxHP())
		print(self.mPlayerOne.getSpeed())
		print(self.mPlayerOne.getAttack())
		print(self.mPlayerOne.getDefense())
		return

	def getPlayerTwoStats(self):
		print(self.mPlayerTwo.getMaxHP())
		print(self.mPlayerTwo.getSpeed())
		print(self.mPlayerTwo.getAttack())
		print(self.mPlayerTwo.getDefense())
		return

	def displayStats(self):
		print("")
		print("Player One stats:")
		self.getPlayerOneStats()
		print("Player Two stats:")
		self.getPlayerTwoStats()
		return

	def battle(self, userChoice):
		if self.mPlayerOne.getSpeed() > self.mPlayerTwo.getSpeed():
			self.castAttack(userChoice)
			self.cpuAttack()
		elif self.mPlayerOne.getSpeed() < self.mPlayerTwo.getSpeed():
			self.cpuAttack()
			self.castAttack(userChoice)
		else:
			coin = random.randint(0,1)
			if coin:
				self.castAttack(userChoice)
				self.cpuAttack()
			else:
				self.cpuAttack()
				self.castAttack(userChoice)

		flag = self.checkWinner()
		return flag

	def castAttack(self, userChoice):
		if userChoice == 'a':
			self.tackle.dealAttack(self.mPlayerTwo)
		elif userChoice == 'b':
			self.blitz.dealAttack(self.mPlayerTwo) #there's a big problem with status effects
		elif userChoice == 'c':
			self.smog.dealAttack(self.mPlayerTwo)
		elif userChoice == 'd':
			self.meditate.dealAttack(self.mPlayerOne) # can't have it be playerOne in the future
		return

	def cpuAttack(self):
		print("test")
		return

	def checkWinner(self):
		if self.mPlayerOne.getMaxHP() <= 0:
			return False
		if self.mPlayerTwo.getMaxHP() <= 0:
			return False
		return True