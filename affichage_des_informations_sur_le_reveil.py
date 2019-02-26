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
from PIL import Image, ImageTk

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
		texte_de_presentation_des_remerciements = ""

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
			texte_du_label_d_affichage_du_nom_du_projet = "Smart connected alarm clock"

			#
			texte_de_presentation_de_l_adresse_email_du_concepteur = "Email address of the designer: "

			#
			texte_de_presentation_du_nom_du_concepteur = "Designer's name: "

			#
			texte_de_presentation_des_remerciements = "Thanks: "

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
			texte_du_label_d_affichage_du_nom_du_projet = "Réveil intelligent et connecté"

			#
			texte_de_presentation_de_l_adresse_email_du_concepteur = "Adresse email du concepteur: "

			#
			texte_de_presentation_du_nom_du_concepteur = "Nom du concepteur: "

			#
			texte_de_presentation_des_remerciements = "Remerciements: "

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
		self.label_d_affichage_du_nom_du_projet = Label(fenetre, text = texte_de_presentation_du_nom_du_produit + texte_du_label_d_affichage_du_nom_du_projet)

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

		#
		self.label_de_presentation_des_remerciements = Label(fenetre, text = texte_de_presentation_des_remerciements)

		#
		self.label_de_presentation_des_remerciements.pack()

		#
		image1 = Image.open("images/imerir_logo.png")

		#
		photo1 = ImageTk.PhotoImage(image1)

		#
		image2 = Image.open("images/squaregolab_logo.png")

		#
		photo2 = ImageTk.PhotoImage(image2)

		#
		self.canvas_d_affichage_du_logo_imerir = Canvas(fenetre, width = image1.size[0], height = image1.size[1])

		#
		self.canvas_d_affichage_du_logo_imerir.create_image(0,0, anchor = NW, image=photo1)

		#
		self.canvas_d_affichage_du_logo_imerir.pack()

		#
		self.canvas_d_affichage_du_logo_du_squaregolab = Canvas(fenetre, width = image2.size[0], height = image2.size[1])

		#
		self.canvas_d_affichage_du_logo_du_squaregolab.create_image(0,0, anchor = NW, image=photo2)

		#
		self.canvas_d_affichage_du_logo_du_squaregolab.pack()
