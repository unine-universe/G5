'''
Created on Apr 6, 2014

@author: hmuriel
'''
import cherrypy
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from unipy.db import openDB

class Annonces(object):
    env = None
    
    def __init__(self):
        # Référence au dossier HTML
        self.env = Environment(loader=FileSystemLoader('html'))
        
    def annonces(self):
        # Charger et compléter le template HTML
        return self.env.get_template('afficherAnnonces.html').render()
    
    def annonce(self, a_id):
        db = openDB()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM annonce, picture WHERE id='{0}'".format(a_id))
        annonce = cursor.fetchone() # prendre une ligne. fetchall() égal à tous les lignes.
        picture = cursor.fetchone()

        
        cursor.close()
        db.close()
        if annonce:
            # Charger et compléter le template HTML
            return self.env.get_template('afficherAnnonce.html').render(image = picture[1], type = annonce[1], auteur = annonce[2], catego = annonce[3], faculty = annonce[4], titre = annonce[5],  desc = annonce[6], prix = annonce[7], prixdesc = annonce[8], datepublic = annonce[9], etat = annonce[10])
        else:
            return '<h1>Erreur, annonce inexistante</h1>'
        
        
        
#        db = openDB()
#        cursor = db.cursor()
#        cursor.execute("Select * FROM picture WHERE id='{0}'".format(a_id))
#        annonce=cursor.fetchone()
#        
#        cursor.close()
#        db.close()
#        if annonce:
#            return self.env.get_template('afficherAnnonce.html').render(image = picture[3,1])
