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

		#
		self.label_de_presentation_des_commandes_vocales_en_anglais = Label(fenetre, text = "Voice commands in english: ", underline = True)

		#
		self.label_de_presentation_des_commandes_vocales_en_anglais.pack()

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_City = Label(fenetre, text = "City: ", underline = True)

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_City.pack()

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Weather = Label(fenetre, text = "Weather: ", underline = True)

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Weather.pack()

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Alarm = Label(fenetre, text = "Alarm: ", underline = True)

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Alarm.pack()

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Updates = Label(fenetre, text = "Updates", underline = True)

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Updates.pack()

		#
                self.label_de_presentation_des_commandes_vocales_de_la_section_Languages_and_Formats = Label(fenetre, text = "Languages & formats: ", underline = True)

                #
                self.label_de_presentation_des_commandes_vocales_de_la_section_Languages_and_Formats.pack()

                #
                self.label_de_presentation_des_commandes_vocales_de_la_section_YouTube_en_en = Label(fenetre, text = "YouTube: ", underline = True)

                #
                self.label_de_presentation_des_commandes_vocales_de_la_section_YouTube_en_en.pack()

                #
                self.label_de_presentation_des_commandes_vocales_de_la_section_Logs_en_en = Label(fenetre, text = "Logs: ", underline = True)

                #
                self.label_de_presentation_des_commandes_vocales_de_la_section_Logs_en_en.pack()

                #
                self.label_de_presentation_des_commandes_vocales_de_la_section_About = Label(fenetre, text = "About: ", underline = True)

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_About.pack()

		#
		self.label_de_presentation_des_commandes_vocales_en_francais = Label(fenetre, text = "Commandes vocales en français: ", underline = True)

		#
		self.label_de_presentation_des_commandes_vocales_en_francais.pack()

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Ville = Label(fenetre, text = "Ville: ", underline = True)

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Ville.pack()

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Meteo = Label(fenetre, text = "Météo: ", underline = True)

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Meteo.pack()

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Reveil = Label(fenetre, text = "Réveil: ", underline = True)

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Reveil.pack()

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Mises_a_jour = Label(fenetre, text = "Mises à jour", underline = True)

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_Mises_a_jour.pack()

		#
                self.label_de_presentation_des_commandes_vocales_de_la_section_Languages_and_Formats = Label(fenetre, text = "Langues & formats: ", underline = True)

                #
                self.label_de_presentation_des_commandes_vocales_de_la_section_Languages_and_Formats.pack()

                #
                self.label_de_presentation_des_commandes_vocales_de_la_section_YouTube_en_fr = Label(fenetre, text = "YouTube: ", underline = True)

                #
                self.label_de_presentation_des_commandes_vocales_de_la_section_YouTube_en_fr.pack()

                #
                self.label_de_presentation_des_commandes_vocales_de_la_section_Logs_en_fr = Label(fenetre, text = "Logs: ", underline = True)

                #
                self.label_de_presentation_des_commandes_vocales_de_la_section_Logs_en_fr.pack()

                #
                self.label_de_presentation_des_commandes_vocales_de_la_section_A_Propos = Label(fenetre, text = "A propos: ", underline = True)

		#
		self.label_de_presentation_des_commandes_vocales_de_la_section_A_Propos.pack()
