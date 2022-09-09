import sys
from creat_perso import create_perso
from generate_monster import generate_monst
from gestion_degat import gestion_degat
from battle_manage import battle_manage
from compteur_ennemi import compt_ennemi


nbre_ennemi = 0

if __name__ == "__main__":

    print("*"*60)
    print("Bienvenue , pret à vous ammuser ;) !!!")
    print("*"*60)
    print('1- Creation de votre personnage :')
    perso = create_perso()
    print('Creation des mostres : ')
    liste_monstres = generate_monst()
    print('Place au jeux :) ')
    
   
    degat = gestion_degat(perso[1],liste_monstres['La force du monstre'],perso[3])
  
    pv_att = liste_monstres['Le PV du monster']
    pv_deff = perso[1]
    #Appeler la fonction manage battle
    resultat = battle_manage(degat,pv_att,pv_deff)
   
    if resultat == True:
        compt_ennemi(nbre_ennemi)
        print('Le nombre de monstres tués est : ', compt_ennemi(nbre_ennemi))
        print(sys.exit())
    else:
        print('bye')
        print(sys.exit())

    
