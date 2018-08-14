from weapon import *
import random

class Soldier:
    def __init__(self,role):
        self.role = role
    name = ""
    age = ""
    rank = ""
    weapon = weapon()
    fatigue = 100
    fatigue_gain_rate = 1
    health = 10
    experience_str = ""
    experience_int = 0
    condition_str = ""
    condition_int = 0
    dead = False

def random_name(list1,list2):
	return random.choice(list1) + " " + random.choice(list2)

def print_soldier(Soldier_inf):
    print("-----")
    print("Name: " + Soldier_inf.name)
    print("Age: " + str(Soldier_inf.age) + " Born: " + str(1941 - Soldier_inf.age))
    print("Squad Role: " + Soldier_inf.role)
    print("Weapon: " + Soldier_inf.weapon.name + " Condition: " + Soldier_inf.condition_str)
    print("Ammo : " + str(Soldier_inf.ammo_quantities[0]))
    print("Experience : " + Soldier_inf.experience_str)
    if Soldier_inf.health > 7:
    	print("Status: Healthy")
    elif Soldier_inf.health > 4:
    	print("Status: Moderate")
    else:
    	print("Status: Poor")
    print("-----")
    print("")

def print_squad_v(squad):
    for Soldier_inf in squad:
        print_soldier(Soldier_inf)
        sleep_seconds(.1)

def print_squad(squad):
    for Soldier_inf in squad:
        print(Soldier_inf.name + " - " + Soldier_inf.role + " - " + Soldier_inf.weapon.name + " [" +  str(Soldier_inf.experience_int) + "]")

def print_squad_leader(squadList):
    print("Officer: " + squadList[0].name)

def get_squad_leader(squadList):
    return squadList[0].name

def get_experience_int(Soldier_inf):
    return Soldier_inf.experience_int

def get_experience_str(Soldier_inf):
    return Soldier_inf.experience_str

def random_experience():
    return random.randint(30,100)

def experience(factor, age, Soldier_inf):
    if age > 25:
        factor += 25
    if Soldier_inf.role == "Rifleman":
        factor -= 20
    if Soldier_inf.role == "Squad Leader":
        factor += 35 
    if Soldier_inf.role == "Assistant Squad Leader":
        factor += 30
    if Soldier_inf.role == "Ammunition Carrier" or "Assistant Gunner":
        factor -= 30
    if factor < 0:
        factor = 0
    if factor > 100:
        factor = 100
    if factor >= 80 and age >= 25:
       Soldier_inf.experience_int = factor
       Soldier_inf.experience_str = "Veteran [" + str(factor) + "]"
    elif factor >= 70 and age >= 22:
        Soldier_inf.experience_int = factor
        Soldier_inf.experience_str = "Seasoned [" + str(factor) + "]"
    elif factor >= 50 and age >= 18:
        Soldier_inf.experience_int = factor
        Soldier_inf.experience_str = "Regular [" + str(factor) + "]"
    elif factor >= 40 and age >= 17:
        Soldier_inf.experience_int = factor
        Soldier_inf.experience_str = "Trained [" + str(factor) + "]"
    else:
        Soldier_inf.experience_int = factor
        Soldier_inf.experience_str = "Green/Fresh [" + str(factor) + "]"

def set_weapon_condition(Soldier_inf):
    var = random.randint(0,100)
    if var > 50:
        Soldier_inf.condition_str = "New [" + str(var) + "]"
    elif var > 30:
        Soldier_inf.condition_str = "Used [" + str(var) + "]"
    else:
       Soldier_inf.condition_str = "Old [" + str(var) + "]"
    Soldier_inf.condition_int = var

def set_random_age(Soldier_inf,role):
    age = random.randint(18,35)
    if role == "Squad Leader":
        age+=10
        if age > 35:
            age = 35
    if role == "Rifleman":
        age -= 5
        if age < 18:
            age = 18
    Soldier_inf.age = age