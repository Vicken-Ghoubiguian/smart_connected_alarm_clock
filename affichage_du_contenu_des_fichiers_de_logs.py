# -*- coding: utf-8 -*

#
try:

        #
        from Tkinter import *

#
except ImportError:

        #
        from tkinter import *

#
class Affichage_du_contenu_des_fichiers_de_logs(Frame):

        #
        def __init__(self, fenetre, width_fenetre_de_conf, height_fenetre_de_conf, fichier_dont_le_contenu_doit_etre_affiche, language):

                #Appel au constructeur de la classe parente
                Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)
