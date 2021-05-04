import stats

class PlayerOne(stats.Stats):
	def __init__(self, maxHealth, attack, defense, speed):
		stats.Stats.__init__(self, maxHealth, attack, defense, speed)
		return

	