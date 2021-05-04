import playerOne, playerTwo, attacks
import random

class Game: #could use a better name
	def __init__(self):
		self.mPlayerOne = playerOne.PlayerOne(100, 100, 100, 100)
		self.mPlayerTwo = playerTwo.PlayerTwo(100, 100, 100, 100)
		return

#useful for when we want more then one enemy etc.
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

	def displayStats(self): # we can split this to be for a single person only
		print("")
		print("Player One stats:")
		self.getPlayerOneStats()
		print("Player Two stats:")
		self.getPlayerTwoStats()
		return

	def createAttacks(self):
		# does a normal hit
		self.tackle = attacks.Attacks(40, 95, 0, 0) # 0 means no status effect
		# normal hit with fire
		self.blitz = attacks.Attacks(30, 90, 1, 30) # 1, for now, means it can cause burn
		# lower enemies accuracy no dmg
		self.smog = attacks.Attacks(0, 100, 2, 90) # 2, for now, means it can lower enemies accuracy
		# well raise selfs attack
		self.meditate = attacks.Attacks(0, 100, 3, 100) # 3, for now, means it well raise attack

	def battle(self, userChoice):
		if userChoice == 'a':
			flag = self.tackle.dealAttack(self.mPlayerTwo)
		elif userChoice == 'b':
			flag = self.blitz.dealAttack(self.mPlayerTwo) #there's a big problem with status effects
		elif userChoice == 'c':
			flag = self.smog.dealAttack(self.mPlayerTwo)
		elif userChoice == 'd':
			flag = self.meditate.dealAttack(self.mPlayerOne) # can't have it be playerOne in the future
		return flag


def playersSetup(game):
	p1HP = 1000 #random.randint(180,220)
	p1ATT = 100
	p1DEF = 100
	p1SPEED = 150
	game.setPlayerOneStats(p1HP, p1ATT, p1DEF, p1SPEED)
	p2HP = 1000 #change back
	p2ATT = 100
	p2DEF = 100
	p2SPEED = 100
	game.setPlayerTwoStats(p2HP, p2ATT, p2DEF, p2SPEED)
	return


def getUserChoice():
	while True:
		choice = input("choice? ")
		if choice == 'a' or choice == 'b' or choice == 'c' or choice == 'd':
			break
		else:
			print("please pick a valid option")
	return choice

def battleMenu(game):
	flag = True
	game.createAttacks()
	while flag:
		print("\nChoose an attack...")
		print("[a-Tackle]", end="")
		print("%11s" % ("[b-Blitz]"), end="\n")
		print("[c-Smog]", end="")
		print("%16s" % ("[d-Meditate]"), end="\n")
		userChoice = getUserChoice()
		flag = game.battle(userChoice)
	return


def menu(game):
	print("%25s" % ("Welcome to UNKNOWN"), end="")
	options = ["\n\nPick an option...", "[a] - stats", "[b] - start a battle", "[c] - custom battle", "[d] - quit"]
	while 1:
		for option in options:
			print(option)
		userChoice = getUserChoice()
		if userChoice == 'a':
			game.displayStats()
		elif userChoice == 'b': # initiate battle
			battleMenu(game)
		elif userChoice == 'c': # make function to allow user to set stats
			print("\nnot yet completed")
		else:
			print("\nGoodbye")
			return

def main():
	game = Game()
	playersSetup(game)
	menu(game)
	return

if __name__ == '__main__':
	main()


	# def battle(self, userChoice): this was your code but we'll ignore for now
	# 	if playerOne.getSpeed() > playerTwo.getSpeed():
	#		playerOne.castAttack(userChoice)
	#		playerTwo.castAttack()
	# 		return flag
	# 	elif playerOne.getSpeed() < playerTwo.getSpeed():
	#		playerTwo.castAttack(userChoice)
	#		playerOne.castAttack()
	# 		return flag
	# 	else:
	# 		coin = random.randint(0,1)
	# 		if coin:
	#		playerOne.castAttack(userChoice)
	#		playerTwo.castAttack()
	# 			return flag
	# 		else:
	#		playerTwo.castAttack(userChoice)
	#		playerOne.castAttack()
	# 			return flag