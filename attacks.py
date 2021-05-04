import playerOne, playerTwo
import random

class Attacks:
	def __init__(self, dmg, acc, effect, effectChance):
		self.mDamage = dmg
		self.mAccuracy = acc
		self.mEffChance = effectChance
		return

	def dealAttack(self, person):
		missChance = random.randint(0, 100)
		if self.mAccuracy >= missChance:
			print("\nHit")
			health = person.getMaxHP()
			health -= self.mDamage # <- we'll probably put our algorithem here or a function calling it
			person.setMaxHP(health)
			#self.dealEffect(person)
			print("Enemies HP: ", person.getMaxHP())
		else:
			print("\nAttack Missed")
		return