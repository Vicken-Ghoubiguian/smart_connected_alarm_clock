# -*- coding: utf-8 -*

#
try:

        #
        from Tkinter import *

#
except ImportError:

        #
        from tkinter import *

import os

#
class Affichage_du_contenu_des_fichiers_de_logs(Frame):

        #
        def __init__(self, fenetre, width_fenetre_d_affichage, height_fenetre_d_affichage, langue_uttilisee, fichier_dont_le_contenu_doit_etre_affiche):

                #Appel au constructeur de la classe parente
                Frame.__init__(self, fenetre, width = width_fenetre_d_affichage, height = height_fenetre_d_affichage)

		#
		texte_de_presentation_du_fichier = ""

		#
		self.fenetre = fenetre

		#
		if fichier_dont_le_contenu_doit_etre_affiche == "logs/logs_commande_vocale":

			#
			if langue_uttilisee == 0:

				#
				texte_de_presentation_du_fichier = "Display of the voice command log file for consultation: "

			#
			if langue_uttilisee == 1:

				#
				texte_de_presentation_du_fichier = "Affichage du fichier de logs de la commande vocale pour consultation: "

			#
                        self.label_de_presentation_du_fichier = Label(fenetre, text = texte_de_presentation_du_fichier)

                        #
                        self.label_de_presentation_du_fichier.pack()

		#
		if fichier_dont_le_contenu_doit_etre_affiche == "logs/logs_mise_a_jour_des_modules":

			#
			if langue_uttilisee == 0:

				#
				texte_de_presentation_du_fichier = "Display the updates log file for consultation: "

			#
			if langue_uttilisee == 1:

				#
				texte_de_presentation_du_fichier = "Affichage du fichier de logs des mises à jour pour consultation: "

			#
			self.label_de_presentation_du_fichier = Label(fenetre, text = texte_de_presentation_du_fichier)

			#
			self.label_de_presentation_du_fichier.pack()

		#
		taille_en_bytes_du_fichier_dont_le_contenu_doit_etre_affiche = os.path.getsize(fichier_dont_le_contenu_doit_etre_affiche)

		#
		descripteur_du_fichier_dont_le_contenu_doit_etre_affiche = os.open(fichier_dont_le_contenu_doit_etre_affiche, os.O_RDONLY)

		#
		variable_contenant_le_contenu_du_fichier_log_passe_en_parametre = os.read(descripteur_du_fichier_dont_le_contenu_doit_etre_affiche, taille_en_bytes_du_fichier_dont_le_contenu_doit_etre_affiche)

		#
                os.close(descripteur_du_fichier_dont_le_contenu_doit_etre_affiche)

		#
		yscrollbar = Scrollbar(self.fenetre, orient = VERTICAL)

		#
		yscrollbar.pack(side=RIGHT, fill=Y)

		#
		self.widget_d_affichage_du_contenu_du_fichier_de_logs = Text(self.fenetre, yscrollcommand = yscrollbar.set)

		#
		self.widget_d_affichage_du_contenu_du_fichier_de_logs.insert(INSERT, variable_contenant_le_contenu_du_fichier_log_passe_en_parametre)

		#
		self.widget_d_affichage_du_contenu_du_fichier_de_logs.config(state = DISABLED)

		#
		self.widget_d_affichage_du_contenu_du_fichier_de_logs.pack()
