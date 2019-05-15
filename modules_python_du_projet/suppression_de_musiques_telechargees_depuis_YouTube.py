# -*- coding: utf-8 -*

#
try:

	#
	from Tkinter import *

	#
	import ttk

	#
	from tkMessageBox import *

#
except ImportError:

	#
	from tkinter import *

	#
	import tkinter.ttk as ttk

	#
	from tkinter.messagebox import *

import os
import pytube
import horloge_monde
from PIL import ImageTk, Image
import requests
import subprocess
from io import BytesIO

#Cette classe permet de définir une interface graphique pour choisir un fichier audio téléchargé depuis YouTube pour suppréssion
class Suppression_de_musiques_telechargees_depuis_YouTube(Frame):

        #Définition du constructeur de la classe Extracteur_de_fichiers_audio_depuis_YouTube
        def __init__(self, fenetre, langue_utilisee, width_fenetre_de_conf, height_fenetre_de_conf):

                #Appel au constructeur de la classe parente
                Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)

		#
		if langue_utilisee == 0:

			#
			self.label_entree_du_single = Label(fenetre, text = "Single to be deleted: ")

			#
			self.identifiant_en_lettres_de_la_langue_utilisee = "en"

			#
			texte_de_description_de_l_action_du_bouton = "Validate the deletion of the selected single"

		#
		else:

			#
			self.label_entree_du_single = Label(fenetre, text = "Single à supprimer: ")

			#
			self.identifiant_en_lettres_de_la_langue_utilisee = "fr"

			#
			texte_de_description_de_l_action_du_bouton = "Valider la suppression du single séléctionné"

		#
		self.langue_utilisee = langue_utilisee

		#
		self.label_entree_du_single.pack()

		#
		indice_du_single_courant_a_jouer_en_cas_de_sonnerie_du_reveil = horloge_monde.renvoie_de_l_id_du_single_enregistre_pour_faire_sonner_le_reveil()

		#
		self.liste_des_singles = horloge_monde.retour_des_singles_enregistres_dans_la_base(fenetre, 0, indice_du_single_courant_a_jouer_en_cas_de_sonnerie_du_reveil)

		#
		self.liste_des_singles.pack()

		#
		self.boutton_de_validation = Button(fenetre, text = texte_de_description_de_l_action_du_bouton, command = self.validation_de_la_suppression_d_un_single_dans_la_base)

		#
		self.boutton_de_validation.pack()

		#
		self.fenetre = fenetre

	#
	def validation_de_la_suppression_d_un_single_dans_la_base(self):

		#
		try:

			#
			if self.langue_utilisee == 0:

				#
				texte_a_dire_par_eSpeak = "Single deleted succesfully"

			#
			else:

				#
				texte_a_dire_par_eSpeak = "Single supprimé avec succès"

			#
			subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_utilisee, "-s", "20", texte_a_dire_par_eSpeak])

		#
		except:

			#
			if self.langue_utilisee == 0:

				#
				texte_a_dire_par_eSpeak = "Error deleting single"

			#
			else:

				#
				texte_a_dire_par_eSpeak = "Erreur lors de la suppression d'un single"

			#
			subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_utilisee, "-s", "20", texte_a_dire_par_eSpeak])

		#
		finally:

			#
			self.fenetre.destroy()
