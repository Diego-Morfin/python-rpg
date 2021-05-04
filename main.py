from game import Game
import random

def playersSetup(game):
	p1HP = 1000
	p1ATT = 100
	p1DEF = 100
	p1SPEED = 150
	game.setPlayerOneStats(p1HP, p1ATT, p1DEF, p1SPEED)
	p2HP = 1000
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