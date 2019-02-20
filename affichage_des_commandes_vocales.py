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
class Affichage_des_commandes_vocales(Frame):

	#
	def __init__(self, fenetre, width_fenetre_de_conf, height_fenetre_de_conf, language):

                #Appel au constructeur de la classe parente
                Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)

		
