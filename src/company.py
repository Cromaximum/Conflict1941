from platoon import *

class company:
	def __init__(self,nation):
		self.nation = nation
	name = None
	collective_health_int = None
	collective_health_str = None
	platoons = None

class company_DE(company):
	pass

class company_RU(company):
	pass

def create_new_company_DE():
	company_ = company("Germany")
	company_.name = "----- DE COMPANY -----"
	company_.collective_health_int = 10
	company_.collective_health_str = "Healthy"
	company_.platoons = [create_new_platoon_DE(),create_new_platoon_DE()]
	return company_

def create_new_company_RU():
	company_ = company("Russia")
	company_.name = "----- RU COMPANY -----"
	company_.collective_health_int = 10
	company_.collective_health_str = "Healthy"
	company_.platoons = [create_new_platoon_RU(),create_new_platoon_RU()]
	return company_

def print_company(company):
	print(company.name)
	for platoon in company.platoons:
		print_platoon(platoon)