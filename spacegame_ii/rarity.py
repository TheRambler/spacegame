import random

class Rarity:
	def __init__(self, json):
		self.default=int(json["default"])
		self.factions=json["factions"]
	def get_for(self, faction_key):
		for i in self.factions:
			if i["faction"]==faction_key:
				return int(i["rarity"])
		return self.default
	def should_have(self, faction_key):
		if random.randint(0,99) < self.get_for(faction_key):
			return True
		return False
	def __str__(self, *args, **kwargs):
		r="DEFAULT[]: "+str(self.default)
		for i in self.factions:
			r+="\n-FACTION["+str(i["faction"])+"]:"+str(i["rarity"])
		return r