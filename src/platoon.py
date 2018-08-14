from RU_infantry import *
from DE_infantry import *

class platoon:
	def __init__(self,nation):
		self.nation = nation
	name = None
	collective_health_int = None
	collective_health_str = None
	squads = None

class platoon_DE(platoon):
	name = "test"
	#TODO Add Other Platoon Roles

class platoon_RU(platoon):
	name = "test"
	#TODO Add Other Platoon Roles

def create_new_platoon_DE():
	platoon_ = platoon("Germany")
	platoon_.name = "DE PLATOON"
	platoon_.collective_health_int = 10
	platoon_.collective_health_str = "Healthy"
	platoon_.squads = [create_new_squad_DE(),create_new_squad_DE(),create_new_squad_DE()]
	return platoon_

def create_new_platoon_RU():
	platoon_list = []
	platoon_ = platoon("Russia")
	platoon_.name = "RU PLATOON"
	platoon_.collective_health_int = 10
	platoon_.collective_health_str = "Healthy"
	platoon_.squads = [create_new_squad_RU(),create_new_squad_RU(),create_new_squad_RU()]
	return platoon_

def print_platoon(platoon):
	print(platoon.name)
	print("---")
	for squad in platoon.squads:
		print_squad(squad)
		print("---")