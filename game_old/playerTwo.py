import stats

class PlayerTwo(stats.Stats):
	def __init__(self, maxHealth, attack, defense, speed):
		stats.Stats.__init__(self, maxHealth, attack, defense, speed)
		return