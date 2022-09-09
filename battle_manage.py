#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 13:16:27 2022

@author: chef
"""
import sys



def battle_manage(degat, pv_attaquant, pv_deffenseur) :
    
    while (pv_attaquant > 0 and pv_deffenseur > 0):
    
        pv_deffenseur = pv_deffenseur - degat
       
        
        pv_attaquant = pv_attaquant - degat
      
      
        if ( pv_deffenseur <= 0 and pv_attaquant > 0):
            
            print ('Game over, le diffenseur ne peut plus comabattre, le PV est :', pv_deffenseur)
            return False
            print(sys.exit())
        
        elif ( pv_attaquant <= 0 and pv_deffenseur > 0): 
            
            print ('Bravo le personnage a gagné, le pv du monstre est :', pv_attaquant, 'le joueur il lui reste encore', pv_deffenseur, 'PV')
            return True
        
            print(sys.exit())
    return pv_deffenseur
        
