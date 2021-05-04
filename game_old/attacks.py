import playerOne, playerTwo, attacks
import random

class Attacks:
	def __init__(self, dmg, acc, effect, effectChance):
		self.mDamage = dmg
		self.mAccuracy = acc
		self.mEffect = effect
		self.mEffectChance = effectChance

		self.mEffectFlag = False
		self.mChance = 0
		self.mCount = 0
		return

	def dealAttack(self, person):
		missChance = random.randint(0, 100)
		if self.mAccuracy >= missChance:
			print("\nHit")
			health = person.getMaxHP()
			health -= self.mDamage # <- we'll probably put our algorithem here or a function calling it
			person.setMaxHP(health)
			self.dealEffect(person)
			print("Enemies HP: ", person.getMaxHP()) #we wont be able to use this for when enemie can start attacking us
			if person.getMaxHP() > 0:
				return True
			else:
				return False
		else:
			print("\nAttack Missed")
			return True

	def dealEffect(self, person):
		if self.mEffect != 0: 
			if not self.mEffectFlag:
				self.mCount = 0
				self.mChance = random.randint(0, 100)
				self.checkEffect(person)
			else:
				self.checkEffect(person)

	def checkEffect(self, person):
		if self.mEffect == 1:
			self.fireEffect(person)
		elif self.mEffect == 2:
			self.lowerAccuracy(person) #we'll change these later for now we only have 4 moves
		elif self.mEffect == 3:
			self.raiseAttack(person)
		return

	def fireEffect(self, person):
		if self.mChance <= self.mEffectChance:
			if self.mCount <= 3:
				health = person.getMaxHP()
				health -= 10
				person.setMaxHP(health)
				self.mCount += 1
				self.mEffectFlag = True
				print("\nDamaged by fire")
				return
			else:
				print("\nNo longer on fire")
				self.mEffectFlag = False
		return

	def lowerAccuracy(self, person):
		print("not made yet")
		return

	def raiseAttack(self, person):
		print("not made yet")
		return

	def otherEffect(self, person):
		if self.mChance <= self.mEffectChance:
			if self.mCount <= 5: #change this for a different effect
				health = person.getMaxHP()
				health -= 10 #change this for a different effect
				person.setMaxHP(health)
				self.mCount += 1
				self.mEffectFlag = True
				print("\nDamaged by")
				return
			else:
				self.mEffectFlag = False
		return


