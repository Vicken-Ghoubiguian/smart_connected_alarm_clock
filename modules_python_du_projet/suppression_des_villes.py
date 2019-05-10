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
	import tkinter.ttk

	#
	from tkinter.messagebox import *

import horloge_monde

#Cette classe permet de définir une interface graphique pour supprimer une ville dans la base de données
class Suppression_des_Villes(Frame):

	#Définition du constructeur de la classe Suppression_des_Villes
	def __init__(self, fenetre, width_fenetre_de_conf, height_fenetre_de_conf, id_de_la_ville_courante, langue_uttilisee):

		#Appel au constructeur de la classe parente
		Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)

		#
		if langue_uttilisee == 0:

			#
			self.label_entree_de_la_ville = Label(fenetre, text = "City ​​to be deleted: ")

			#
			texte_de_description_de_l_action_du_bouton = "Validate the deletion of the selected city"

		#
		else:

			#
			self.label_entree_de_la_ville = Label(fenetre, text = "Ville à supprimer: ")

			#
			texte_de_description_de_l_action_du_bouton = "Valider la suppression de la ville séléctionnée"

		#
		self.langue_uttilisee = langue_uttilisee

		#
		self.label_entree_de_la_ville.pack()

		#
		self.liste_des_villes_avec_le_pays_correspondant = horloge_monde.retour_des_villes_enregistrees_dans_la_base(fenetre, id_de_la_ville_courante, 0, self.langue_uttilisee)

		#
		self.liste_des_villes_avec_le_pays_correspondant.pack()

		#
		self.boutton_de_validation = Button(fenetre, text = texte_de_description_de_l_action_du_bouton, command = self.validation_de_la_suppression_de_la_ville_dans_la_base)

		#
		self.boutton_de_validation.pack()

		#
		self.fenetre = fenetre

	#Cette fonction permet de valider la suppression de la ville séléctionnée dans la combobox
	def validation_de_la_suppression_de_la_ville_dans_la_base(self):

		#
		#try:

			#
			nom_de_la_ville_a_supprimer_avant_traitement_pour_extraction_de_la_combobox = self.liste_des_villes_avec_le_pays_correspondant.get()

			#
			nom_de_la_ville_a_supprimer = horloge_monde.renvoie_du_nom_de_la_ville_a_supprimer_apres_traitement_pour_extraction_de_la_combobox(nom_de_la_ville_a_supprimer_avant_traitement_pour_extraction_de_la_combobox)

			#
			horloge_monde.suppression_d_une_ville_dans_la_base(nom_de_la_ville_a_supprimer, self.langue_uttilisee)

			#
                        showinfo("Ville supprimée", "Bonne nouvelle: La ville que vous avez séléctionnée a bien été supprimée")

		#Si une erreur a été rencontrée, alors...
		#except:

			#
			#showerror("Erreur dans la suppression d'une ville", "Erreur: La suppression de la ville séléctionnée n'a pas pu se faire corretement !!!!")

		#finally:

			#
			#self.fenetre.destroy()
