
def gestion_degat(pv_deffenseur,force_attaquant,armure_defonseur):
    if (force_attaquant > armure_defonseur) :
        deg= force_attaquant-armure_defonseur
        degat = pv_deffenseur - deg
    else : 
        return pv_deffenseur -1
     