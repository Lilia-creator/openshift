# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect

from creat_perso import create_perso
from generate_monster import generate_monst
from battle_manage import battle_manage 
from gestion_degat import gestion_degat
from compteur_ennemi import compt_ennemi

app = Flask(__name__)

import sys
import os

@app.route('/', methods=['GET', 'POST'])

def menu():
    if request.form:
        monsterkilled = 0
        liste = []
        pseudo = request.form['pseudo']

        monperso = create_perso(pseudo, 20,6,3)
        
        monster = generate_monst()
        degat = gestion_degat(monperso[1],monster['La force du monstre'],monperso[3])
            
        pv_att = monster['Le PV du monster']
        pv_deff = monperso[1]
        resultat = battle_manage(degat,pv_att,pv_deff)

        if resultat == True:
            compt_ennemi(monsterkilled)
            print('Le nombre de monstres tués est : ', compt_ennemi(monsterkilled))
            liste.append(monster[0])
            print(sys.exit())
        else:
            print('bye')
            print(sys.exit())
        return render_template('home.html', pseudo=pseudo, monsterkilled=monsterkilled, liste=liste )
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)