# -*- coding: utf-8 -*

from Tkinter import *
import ttk
from tkMessageBox import *
import horloge_monde

#Cette classe permet de définir une interface graphique pour supprimer une ville dans la base de données
class Suppression_des_Villes(Frame):

	#Définition du constructeur de la classe Suppression_des_Villes
	def __init__(self, fenetre, width_fenetre_de_conf, height_fenetre_de_conf, id_de_la_ville_courante):

		#Appel au constructeur de la classe parente
		Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)

		#
		self.label_entree_de_la_ville = Label(fenetre, text = "Ville à supprimer: ")

		#
		self.label_entree_de_la_ville.pack()

		#
		self.liste_des_villes_avec_le_pays_correspondant = horloge_monde.retour_des_villes_enregistrees_dans_la_base(fenetre, id_de_la_ville_courante, 1, 1)

		#
		self.liste_des_villes_avec_le_pays_correspondant.pack()

		#
		self.boutton_de_validation = Button(fenetre, text = "Valider la suppression de la ville séléctionnée", command = self.validation_de_la_suppression_de_la_ville_dans_la_base)

		#
		self.boutton_de_validation.pack()

		#
		self.fenetre = fenetre

	#Cette fonction permet de valider la suppression de la ville séléctionnée dans la combobox
	def validation_de_la_suppression_de_la_ville_dans_la_base(self):

		#
		try:

			#
			nom_de_la_ville_a_supprimer = self.liste_des_villes_avec_le_pays_correspondant.get()

			#
			horloge_monde.suppression_d_une_ville_dans_la_base(nom_de_la_ville_a_supprimer)

			#
                        showinfo("Ville supprimée", "Bonne nouvelle: La ville que vous avez séléctionnée a bien été supprimée")

		#Si une erreur a été rencontrée, alors...
		except:

			#
			showerror("Erreur dans la suppression d'une ville", "Erreur: La suppression de la ville séléctionnée n'a pas pu se faire corretement !!!!")

		finally:

			#
			self.fenetre.destroy()
