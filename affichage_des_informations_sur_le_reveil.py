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
class Affichage_des_informations_sur_le_reveil(Frame):

	#
	def __init__(self, fenetre, width_fenetre_de_conf, height_fenetre_de_conf, language):

		#Appel au constructeur de la classe parente
                Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)

		#
		texte_du_label_d_affichage_du_nom_du_projet = ""

		#
		texte_de_presentation_du_nom_du_concepteur = ""

		#
		texte_de_presentation_du_nom_du_produit = ""

		#
		texte_de_presentation_de_l_adresse_email_du_concepteur = ""

		#
		texte_de_presentation_du_nom_de_l_entreprise = ""

		#
		texte_de_presentation_du_titre_de_la_licence = ""

		#
		texte_de_presentation_du_numero_de_version = ""

		#
		if language == 0:

			#
			texte_de_presentation_du_nom_du_produit = "Name of the project: "

			#
			texte_de_presentation_du_numero_de_version = "Number of the current version: "

			#
			texte_de_presentation_du_nom_de_l_entreprise = "Company: "

			#
			texte_de_presentation_du_titre_de_la_licence = "Project licence: "

			#
			texte_du_label_d_affichage_du_nom_du_projet = "Smart connected alarm clock: "

			#
			texte_de_presentation_de_l_adresse_email_du_concepteur = "Email address of the designer: "

			#
			texte_de_presentation_du_nom_du_concepteur = "Designer's name: "

		#
		if language == 1:

			#
                        texte_de_presentation_du_nom_du_produit = "Nom du projet: "

			#
			texte_de_presentation_du_numero_de_version = "Numéro de la version courante: "

			#
			texte_de_presentation_du_nom_de_l_entreprise = "Entreprise: "

			#
			texte_de_presentation_du_titre_de_la_licence = "Licence du projet: "

			#
			texte_du_label_d_affichage_du_nom_du_projet = "Réveil intelligent et connecté: "

			#
			texte_de_presentation_de_l_adresse_email_du_concepteur = "Adresse email du concepteur: "

			#
			texte_de_presentation_du_nom_du_concepteur = "Nom du concepteur: "

		#
		texte_du_label_d_affichage_du_numero_de_la_version_du_projet = "1.0"

		#
		texte_du_label_du_nom_de_la_licence_du_projet = "MIT"

		#
		texte_du_label_d_affichage_du_nom_de_la_societe = "SquaregoLab"

		#
		texte_du_label_d_affichage_du_concepteur = "Eric Steve Vicken Ghoubiguian"

		#
		texte_du_label_d_affichage_de_l_adresse_email = "ericghoubiguian@live.fr"

		#
		self.label_d_affichage_du_nom_du_projet = Label(fenetre, text = texte_du_label_d_affichage_du_nom_du_projet + texte_du_label_d_affichage_du_nom_du_projet)

		#
		self.label_d_affichage_du_nom_du_projet.pack()

		#
		self.label_d_affichage_du_numero_de_la_version_du_projet = Label(fenetre, text = texte_de_presentation_du_numero_de_version + texte_du_label_d_affichage_du_numero_de_la_version_du_projet)

		#
		self.label_d_affichage_du_numero_de_la_version_du_projet.pack()

		#
		self.label_d_affichage_du_concepteur = Label(fenetre, text = texte_de_presentation_du_nom_du_concepteur + texte_du_label_d_affichage_du_concepteur)

		#
		self.label_d_affichage_du_concepteur.pack()

		#
		self.label_d_affichage_du_nom_de_la_societe = Label(fenetre, text = texte_de_presentation_du_nom_de_l_entreprise + texte_du_label_d_affichage_du_nom_de_la_societe)

		#
		self.label_d_affichage_du_nom_de_la_societe.pack()

		#
		self.label_d_affichage_de_l_adresse_email = Label(fenetre, text = texte_de_presentation_de_l_adresse_email_du_concepteur + texte_du_label_d_affichage_de_l_adresse_email)

		#
		self.label_d_affichage_de_l_adresse_email.pack()

		#
		self.label_du_nom_de_la_licence_du_projet = Label(fenetre, text = texte_de_presentation_du_titre_de_la_licence + texte_du_label_du_nom_de_la_licence_du_projet)

		#
		self.label_du_nom_de_la_licence_du_projet.pack()
