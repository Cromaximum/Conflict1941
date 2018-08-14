# coding=utf-8
from soldier_inf import *
from weapon import *

DE_first_names = ['Ernst', 'Friedrich', 'Hans', 'Heinrich', 'Hermann', 'Karl', 'Otto', 'Paul', 'Walter', 'Wilhelm', 'Gerhard', 'Günter', 'Hans', 'Heinz', 'Helmut', 'Herbert', 'Karl', 'Kurt', 'Walter', 'Werner', 'Dieter', 'Günter', 'Hans', 'Horst', 'Jürgen', 'Klaus', 'Manfred', 'Peter', 'Uwe', 'Wolfgang']

DE_last_names = ['Müller', 'Schmidt', 'Meyer', 'Schneider', 'Fischer', 'Weber', 'Becker', 'Wagner', 'Schäfer', 'Schulz', 'Hoffmann', 'Bauer', 'Koch', 'Klein', 'Schröder', 'Schwarz', 'Schwartz', 'Wolf', 'Neumann', 'Braun', 'Zimmermann', 'Huber', 'Hartmann', 'Weiss', 'Richter', 'Lange', 'Kause', 'Krauss', 'Krüger', 'Werner', 'Peters', 'Fuchs', 'Walter', 'König', 'Köhler', 'Kaiser', 'Jung', 'Keller', 'Hermann', 'Roth', 'Grün', 'Gross']

DE_inf_squad = ['Squad Leader', 'Assistant Squad Leader', 'Rifleman', 'Machine Gunner', 'Assistant Gunner', 'Ammunition Carrier']

class Squad_Leader_DE(Soldier):
    weapon = MP_41()
    rank = ""
    primary_weapon = ""
    secondary_weapon = ""
    ammo_types = []
    ammo_quantities = [128,0]

class Assistant_Squad_Leader_DE(Soldier):
    weapon = Karabiner_98K()
    rank = ""
    primary_weapon = ""
    secondary_weapon = ""
    ammo_types = []
    ammo_quantities = [40,0]

class Rifleman_DE(Soldier):
    weapon = Karabiner_98K()
    rank = ""
    primary_weapon = ""
    secondary_weapon = ""
    ammo_types = []
    ammo_quantities = [40,0]

class Machine_Gunner_DE(Soldier):
    weapon = MG_34()
    rank = ""
    primary_weapon = ""
    secondary_weapon = ""
    ammo_types = []
    ammo_quantities = [300,0]

class Assistant_Gunner_DE(Soldier):
    weapon = Walther_P38()
    rank = ""
    primary_weapon = ""
    secondary_weapon = ""
    ammo_types = []
    ammo_quantities = [40,0]

class Ammunition_Carrier_DE(Soldier):
    weapon = Karabiner_98K()
    rank = ""
    primary_weapon = ""
    secondary_weapon = ""
    ammo_types = []
    ammo_quantities = [40,0]

def create_new_Soldier_DE(role):
    de_soldier = Soldier(role)
    if(role == 'Squad Leader'):
    	de_soldier = Squad_Leader_DE(role)
    if(role == 'Assistant Squad Leader'):
    	de_soldier = Assistant_Squad_Leader_DE(role)
    if(role == 'Rifleman'):
    	de_soldier = Rifleman_DE(role)
    if(role == 'Machine Gunner'):
    	de_soldier = Machine_Gunner_DE(role)
    if(role == 'Assistant Gunner'):
    	de_soldier = Assistant_Gunner_DE(role)
    if(role == 'Ammunition Carrier'):
    	de_soldier = Ammunition_Carrier_DE(role)
    de_soldier.name = random_name(DE_first_names,DE_first_names)
    set_random_age(de_soldier, de_soldier.role)
    experience(random_experience(),de_soldier.age,de_soldier)
    set_weapon_condition(de_soldier)
    return de_soldier

#DE_inf_squad[x] refers to name of role
def create_new_squad_DE():
    squadList = []
    Squad_Leader = create_new_Soldier_DE(DE_inf_squad[0])
    Assistant_Squad_Leader = create_new_Soldier_DE(DE_inf_squad[1])
    Rifleman_1 = create_new_Soldier_DE(DE_inf_squad[2])
    Rifleman_2 = create_new_Soldier_DE(DE_inf_squad[2])
    Rifleman_3 = create_new_Soldier_DE(DE_inf_squad[2])
    Rifleman_4 = create_new_Soldier_DE(DE_inf_squad[2])
    Rifleman_5 = create_new_Soldier_DE(DE_inf_squad[2])
    Rifleman_6 = create_new_Soldier_DE(DE_inf_squad[2])
    Machine_Gunner = create_new_Soldier_DE(DE_inf_squad[3])
    Assistant_Gunner = create_new_Soldier_DE(DE_inf_squad[4])
    Ammunition_Carrier = create_new_Soldier_DE(DE_inf_squad[5])
    squadList.append(Squad_Leader)
    squadList.append(Assistant_Squad_Leader)
    squadList.append(Rifleman_1)
    squadList.append(Rifleman_2)
    squadList.append(Rifleman_3)
    squadList.append(Rifleman_4)
    squadList.append(Rifleman_5)
    squadList.append(Rifleman_6)
    squadList.append(Machine_Gunner)
    squadList.append(Assistant_Gunner)
    squadList.append(Ammunition_Carrier)
    return squadList