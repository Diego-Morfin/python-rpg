import attacks
class Moves:
	def __init__(self):
		# does a normal hit
		self.tackle = attacks.Attacks(40, 95, 0, 0) # 0 means no status effect
		# normal hit with fire
		self.blitz = attacks.Attacks(30, 90, 1, 30) # 1, for now, means it can cause burn
		# lower enemies accuracy no dmg
		self.smog = attacks.Attacks(0, 100, 2, 90) # 2, for now, means it can lower enemies accuracy
		# well raise selfs attack
		self.meditate = attacks.Attacks(0, 100, 3, 100) # 3, for now, means it well raise attack
		return

	def giveMoves(self, choice): # This is for when we let them choose what moves they want
		pass