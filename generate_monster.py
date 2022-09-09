
# -*- coding: utf-8 -*-

import random
from create_monster import create_monster as cm

def generate_monst():

    mon_dico = {}

    pv = random.randint(5,20)
    force = random.randint(3, 8)
    armure = random.randint(0, 5)

    mon_dico = {'Le pseudo du monstre': cm(), 'Le PV du monster' : pv, 'La force du monstre': force, 'Armure du monstre ': armure}
    print(mon_dico)
    return mon_dico

