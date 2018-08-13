from util import *
from DE_infantry import *
from RU_infantry import *
from combat import *

squad1 = create_new_squad_DE()
squad2 = create_new_squad_RU()
Date = date()
random_starting_date(Date)
print("")
cool_text("Squad Combat 1941")
print("")
cool_text("-----------------")
print("")

combat(squad1,squad2,Date)