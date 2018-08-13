from DE_infantry import *
from RU_infantry import *

#False = squad2 starts
#True = squad1 starts
def initiative(squad1,squad2):
	exp1 = squad1[0].experience_int
	exp2 = squad2[0].experience_int
	print(get_squad_leader(squad1) + " Experience: " + get_experience_str(squad1[0]))
	print(get_squad_leader(squad2) + " Experience: " + get_experience_str(squad2[0]))
	if exp1 == exp2:
		return_val = bool(random.getrandbits(1))
	else:
		return_val = exp1 > exp2
	if return_val:
		print(get_squad_leader(squad1) + " gets the initiative!")
	else:
		print(get_squad_leader(squad2) + " gets the initiative!")
	return return_val

def is_squad_dead(squad):
	return_val = True
	for Soldier_inf in squad:
		if not Soldier_inf.dead:
			return_val = False

def is_soldier_dead(Soldier_inf):
	return Soldier_inf.dead


def is_mg_alive(squad):
	return_val = False
	for Soldier_inf in squad:
		if Soldier_inf.role == "Machine Gunner" and not is_soldier_dead(Soldier_inf):
			return_val = True



def attacking(squad1, squad2):
	#Spotting
	#Firing
	#Reloading
	pass

def defending(squad1,squad2):
	#Spotting
	#Reaction to attack
	pass

def combat(squad1, squad2, date):
	init_val = initiative(squad1,squad2)
	if init_val:
		starting_squad = squad1
		ending_squad = squad2
		print("")
		cool_text("The Wehrmacht will begin combat")
	else:
		starting_squad = squad2
		ending_squad = squad1
		print("")
		cool_text("The Red Army will begin combat")
	print("")

	#TODO MAKE CLASS FOR SQUADS AND DYNAMIC DIVISION NAMES

	print("")
	print("THE GERMANS")
	print("-----------")
	print_squad(squad1)
	print("")
	print("THE SOVIETS")
	print("-----------")
	print_squad(squad2)
	print("")
	print_date_c(date)
	print("")
	sleep_seconds(1)

	count = 0

	while not is_squad_dead(squad1) and not is_squad_dead(squad2):
		if count % 2 == 0:
			attacking(starting_squad,ending_squad)
			count += 1
		else:
			attacking(ending_squad,starting_squad)
			count += 1
		sleep_seconds(1)
