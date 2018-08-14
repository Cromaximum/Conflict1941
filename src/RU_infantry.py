# coding=utf-8
from soldier_inf import *
from weapon import *

RU_first_names = ['Abram','Alexander','Alexei','Albert','Anatoly','Andrei','Anton','Arkady','Arseny','Artyom','Artur','Afanasy','Bogdan','Boris','Vadim','Valentin','Valery','Vasily','Veniamin','Viktor','Vitaly','Vlad','Vladimir','Vladislav','Vsevolod','Vyacheslav','Gavriil','Garry','Gennady','Georgy','Gerasim','German','Gleb','Grigory','David','Daniil','Denis','Dimitry','Evgeny','Yegor','Yefim','Zakhar','Ivan','Ignat','Ignaty','Igor','Illarion','Ilia','Immanuil','Iosif','Kirill','Konstantin','Lev','Leo','Leonid','Makar','Maxim','Marat','Mark','Matvei','Mikhail','Nestor','Nikita','Nikolay','Oleg','Pavel','Pyotr','Peter','Robert','Rodion','Roman','Rostislav','Ruslan','Semyon','Sergei','Spartak','Stanislav','Stepan','Taras','Timofei','Timur','Trofim','Eduard','Erik','Yulian','Yury','Yarkov','Yaroslav']

RU_last_names = ['Ivanov','Smirnov','Kuznetsov','Popov','Vasiliev','Petrov','Sokolov','Mkhailov','Fedorov','Morozov','Volkov','Alexeev','Lebedev','Semenov','Egorov','Pavlov','Kozlov','Stepanov','Kikolaev','Orlov']

RU_inf_squad = ['Squad Leader','Sub-machine Gunner','Rifleman','Machine Gunner','Assistant Gunner']

class Squad_Leader_RU(Soldier):
    weapon = PPSh_41()
    rank = ""
    primary_weapon = ""
    secondary_weapon = ""
    ammo_types = []
    ammo_quantities = [128,0]

class Sub_machine_Gunner_RU(Soldier):
    weapon = PPSh_41()
    rank = ""
    primary_weapon = ""
    secondary_weapon = ""
    ammo_types = []
    ammo_quantities = [128,0]

class Rifleman_RU(Soldier):
    weapon = Mosin_Nagant_M1891_30()
    rank = ""
    primary_weapon = ""
    secondary_weapon = ""
    ammo_types = []
    ammo_quantities = [40,0]

class Machine_Gunner_RU(Soldier):
    weapon = DP_27()
    rank = ""
    primary_weapon = ""
    secondary_weapon = ""
    ammo_types = []
    ammo_quantities = [141,0]

class Assistant_Gunner_RU(Soldier):
    weapon = Tokarev_TT_33()
    rank = ""
    primary_weapon = ""
    secondary_weapon = ""
    ammo_types = []
    ammo_quantities = [40,0]

def create_new_Soldier_RU(role):
	ru_soldier = Soldier(role)
	if(role == 'Squad Leader'):
		ru_soldier = Squad_Leader_RU(role)
	if(role == 'Sub-machine Gunner'):
		ru_soldier = Sub_machine_Gunner_RU(role)
	if(role == 'Rifleman'):
		ru_soldier = Rifleman_RU(role)
	if(role == 'Machine Gunner'):
		ru_soldier = Machine_Gunner_RU(role)
	if(role == 'Assistant Gunner'):
		ru_soldier = Assistant_Gunner_RU(role)
	ru_soldier.name = random_name(RU_first_names,RU_last_names)
	set_random_age(ru_soldier,ru_soldier.role)
	experience(random_experience(),ru_soldier.age,ru_soldier)
	set_weapon_condition(ru_soldier)
	return ru_soldier

def create_new_squad_RU():
	squadList = []
	Squad_Leader = create_new_Soldier_RU(RU_inf_squad[0])
	Sub_machine_gunner_1 = create_new_Soldier_RU(RU_inf_squad[1])
	Sub_machine_gunner_2 = create_new_Soldier_RU(RU_inf_squad[1])
	Rifleman_1 = create_new_Soldier_RU(RU_inf_squad[2])
	Rifleman_2 = create_new_Soldier_RU(RU_inf_squad[2])
	Rifleman_3 = create_new_Soldier_RU(RU_inf_squad[2])
	Rifleman_4 = create_new_Soldier_RU(RU_inf_squad[2])
	Rifleman_5 = create_new_Soldier_RU(RU_inf_squad[2])
	Rifleman_6 = create_new_Soldier_RU(RU_inf_squad[2])
	Machine_Gunner = create_new_Soldier_RU(RU_inf_squad[3])
	Assistant_Gunner = create_new_Soldier_RU(RU_inf_squad[4])
	squadList.append(Squad_Leader)
	squadList.append(Sub_machine_gunner_1)
	squadList.append(Sub_machine_gunner_2)
	squadList.append(Rifleman_1)
	squadList.append(Rifleman_2)
	squadList.append(Rifleman_3)
	squadList.append(Rifleman_4)
	squadList.append(Rifleman_5)
	squadList.append(Rifleman_6)
	squadList.append(Machine_Gunner)
	squadList.append(Assistant_Gunner)
	return squadList