from hero import *

#=================MAIN=======================

myhero1 = Hero("Dagora", 60, 'Orc')
myhero2 = Hero("Alexandr", 4, 'Human')


myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.level_up()
myhero1.show_hero()
myhero2.show_hero()

myhero2.set_health(10)
myhero2.show_hero()
