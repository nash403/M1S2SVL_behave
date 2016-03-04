# -*- coding: utf-8 -*-
"""
SVL 2015-2016
TP poids ideal
Authors: Honore Nintunze, Antonin Durey
"""

import cherrypy


PAGE_INDEX="""
<!DOCTYPE html>
<html>
    <head>
        <title>Calcul poids idéal</title>
    </head>
    <body>
        <h1>Calculez votre poids idéal</h1>
        <form action="/calcul" method="post">
            <div>Sexe :
                <span>
                    <input id="homme" type="radio" value="h" name="sexe"/>
                    <label for="homme">Homme</label>
                    <input id="femme" type="radio" value="f" name="sexe"/>
                    <label for="femme">Femme</label>
                </span>
            </div>
            <input type="number" id="taille" name="taille"/>
        </form>
    </body>
</html>
"""

PAGE_INDEX_ERREUR="""
<!DOCTYPE html>
<html>
    <head>
        <title>Calcul poids idéal</title>
    </head>
    <body>
        <h1>Calculez votre poids idéal</h1>
        <form action="/calcul" method="post">
            <div>Sexe :
                <span>
                    <input id="homme" type="radio" value="h" name="sexe"/>
                    <label for="homme">Homme</label>
                    <input id="femme" type="radio" value="f" name="sexe"/>
                    <label for="femme">Femme</label>
                </span>
            </div>
            <input type="number" id="taille" name="taille"/><br/>
            <span id="mess_err" style="color:red;">Le poids doit être positif</span>
        </form>
    </body>
</html>
"""

def PAGE_INDEX_RESULTAT(poids):
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Calcul poids idéal</title>
    </head>
    <body>
        <h1>Calculez votre poids idéal</h1>
        <form action="/calcul" method="post">
            <div>Sexe :
                <span>
                    <input id="homme" type="radio" value="h" name="sexe"/>
                    <label for="homme">Homme</label>
                    <input id="femme" type="radio" value="f" name="sexe"/>
                    <label for="femme">Femme</label>
                </span>
            </div>
            <input type="number" id="taille" name="taille"/>
        </form>
        <br/>
        <span id="mess_result">Votre poids idéal est : """ + str(poids) + """ kg</span>
    </body>
</html>
"""

class AppliCalculPoidsIdeal:

    def __init__(self,factoryCalculateur):
        self.calculateur = factoryCalculateur

    @cherrypy.expose
    def index(self):
        return PAGE_INDEX

    @cherrypy.expose
    def calcul(self,taille=None,sexe=None):
        print('---------')
        if taille == None:
            return PAGE_INDEX
        elif int(taille) < 0:
            return PAGE_INDEX_ERREUR
        else:

            return PAGE_INDEX_RESULTAT(self.calculateur.create().calcule(int(taille),sexe))

class FactoryCalculateur:

    def create(self):
        return Calculateur()

class Calculateur:

    def calcule(self, taille, sexe):
        if taille < 0:
            raise ValueError()
        if sexe == "h":
            return taille - 100 - (taille -150) / 4
        elif sexe == "f":
            return taille - 100 - (taille -150) / 2.5
        else:
            return taille - 100 - (taille -150) / 4


if __name__ == '__main__':
    cherrypy.quickstart(AppliCalculPoidsIdeal(FactoryCalculateur()))
