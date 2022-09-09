#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from gestion_degat import gestion_degat 
def battle_manage(monster, perso) :
    
    while (monster[1] >= 0 and perso[1] >= 0):
        monster[1] = gestion_degat(monster[1], perso[2], monster[3])
        print(f"Le joueur {perso[0]} attaque : Il reste au monstre {monster[0]} {monster[1]} points de vie")

        if (monster[1] >= 0):
            monster[1] = gestion_degat(perso[1], monster[2], perso[3])
            print(f"{monster[0]} attaque : Il reste à {perso[0]} {perso[1]} points de vie")
    if(perso[1] > 0):
        print(f"Le joueur a vaincu le terrible {monster[0]}!")
    return perso
