# -*- coding: utf-8 -*

#
try:

	#
	from Tkinter import *

	#
	from urllib2 import urlopen

#
except ImportError:

	#
	from tkinter import *

	#
	from urllib.request import urlopen

import situation_de_la_meteo
import horloge_monde
import datetime
import pytz
from PIL import ImageTk, Image
import requests
import io
import base64

#Cette classe permet de définir une interface graphique pour afficher la météo d'une ville enregistrée dans la base de données
class Affichage_de_la_Meteo(Frame):

	#Définition du constructeur de la classe Affichage_de_la_Meteo
	def __init__(self, fenetre, width_fenetre_de_conf, height_fenetre_de_conf, id_de_la_ville_courante, cle_de_l_API, unite_de_mesure_de_la_temperature_en_chiffre, language):

		#Appel au constructeur de la classe parente
		Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)

		#
		code_du_pays_ou_de_la_zone_correspondant = horloge_monde.renvoi_du_code_du_pays_ou_de_la_zone_correspondant(id_de_la_ville_courante)

		#
		nom_de_la_ville_courante = horloge_monde.renvoi_du_nom_de_la_ville_courante_pour_la_meteo_a_partir_de_son_id(id_de_la_ville_courante)

		#
		nom_de_la_ville_courante_dans_la_langue_courante = horloge_monde.renvoi_du_nom_de_la_ville_courante_dans_le_language_passe_en_parametre(id_de_la_ville_courante, language)

		#
		nom_du_pays_correspondant_a_la_ville_courante = horloge_monde.renvoi_du_nom_du_pays_correspondant_a_l_id_de_la_ville_passe_en_parametre(id_de_la_ville_courante, language)

		#
		timezone_correspondant_a_la_ville_courante = horloge_monde.renvoi_du_timezone_correspondant_a_l_id_de_la_ville_passe_en_parametre(id_de_la_ville_courante)

		#
		if unite_de_mesure_de_la_temperature_en_chiffre == 0:

			#
			unite_de_mesure_de_la_temperature_en_lettres = "Celsius"

		#
		else:

			#
			unite_de_mesure_de_la_temperature_en_lettres = "Fahrenheit"

		#
		self.situation_de_la_meteo_dans_la_ville_donnee = situation_de_la_meteo.Situation_de_la_Meteo(nom_de_la_ville_courante, code_du_pays_ou_de_la_zone_correspondant, cle_de_l_API, unite_de_mesure_de_la_temperature_en_chiffre, language)

		#
                if language == 0:

                        #
                        texte_du_label_d_affichage_des_donnees_generales = "Temperature: " + str(self.situation_de_la_meteo_dans_la_ville_donnee.temperature_dans_la_ville_donnee) + " degrees " + unite_de_mesure_de_la_temperature_en_lettres + ".\nHighest temperature expected: " + str(self.situation_de_la_meteo_dans_la_ville_donnee.prevision_de_la_temperature_la_plus_haute_pour_la_ville_donnee) + " degrees " + unite_de_mesure_de_la_temperature_en_lettres + ".\nLowest temperature expected: " + str(self.situation_de_la_meteo_dans_la_ville_donnee.prevision_de_la_temperature_la_plus_basse_pour_la_ville_donnee) + " degrees " + unite_de_mesure_de_la_temperature_en_lettres+ ".\nHumidity: " + str(self.situation_de_la_meteo_dans_la_ville_donnee.humidite_dans_la_ville_donnee)  + "%.\nAtmospheric pressure: " + str(self.situation_de_la_meteo_dans_la_ville_donnee.pression_atmospherique_dans_la_ville_donnee) + " hpa"

			#
			texte_du_label_d_affichage_de_l_indice_UV_de_la_ville_courante = "UV index: "

			#
			texte_du_label_d_affichage_du_risque_evalue_que_represente_les_UV = "Risk of exposure: "

			#
			texte_du_label_d_affichage_de_presentation_de_l_heure_du_lever_de_soleil = "Sunrise time: "

			#
			texte_du_label_d_affichage_de_presentation_de_l_heure_du_coucher_de_soleil = "Sunset time: "

                #
                else:

                        #
                        texte_du_label_d_affichage_des_donnees_generales = "Température: " + str(self.situation_de_la_meteo_dans_la_ville_donnee.temperature_dans_la_ville_donnee) + " degrés " + unite_de_mesure_de_la_temperature_en_lettres + ".\nTempérature la plus haute attendue: " + str(self.situation_de_la_meteo_dans_la_ville_donnee.prevision_de_la_temperature_la_plus_haute_pour_la_ville_donnee) + " degrés " + unite_de_mesure_de_la_temperature_en_lettres + ".\nTempérature la plus basse attendue: " + str(self.situation_de_la_meteo_dans_la_ville_donnee.prevision_de_la_temperature_la_plus_basse_pour_la_ville_donnee) + " degrés " + unite_de_mesure_de_la_temperature_en_lettres+ ".\nHumidité: " + str(self.situation_de_la_meteo_dans_la_ville_donnee.humidite_dans_la_ville_donnee)  + "%.\nPression atmosphérique: " + str(self.situation_de_la_meteo_dans_la_ville_donnee.pression_atmospherique_dans_la_ville_donnee) + " hpa"

			#
			texte_du_label_d_affichage_de_l_indice_UV_de_la_ville_courante = "Indice UV: "

			#
			texte_du_label_d_affichage_du_risque_evalue_que_represente_les_UV = "Risque d'exposition: "

			#
			texte_du_label_d_affichage_de_presentation_de_l_heure_du_lever_de_soleil = "Heure du lever de soleil: "

			#
			texte_du_label_d_affichage_de_presentation_de_l_heure_du_coucher_de_soleil = "Heure du coucher de soleil: "

		#
		self.label_d_affichage_du_nom_de_la_ville_concernee = Label(fenetre, text = nom_de_la_ville_courante_dans_la_langue_courante+ " ( " + nom_du_pays_correspondant_a_la_ville_courante + " ): ")

		#
		self.label_d_affichage_du_nom_de_la_ville_concernee.pack()

		#
		image_byt = urlopen(self.situation_de_la_meteo_dans_la_ville_donnee.url_de_l_icone_de_la_meteo_de_la_ville_courante).read()

		#
		image_b64 = base64.encodestring(image_byt)

		#
		image_prete_a_l_affichage = PhotoImage(data = image_b64)

		#
		self.canvas_d_affichage_de_l_image_de_presentation_de_la_situation_meteorologique = Label(fenetre, image = image_prete_a_l_affichage)

		#
		self.canvas_d_affichage_de_l_image_de_presentation_de_la_situation_meteorologique.pack()

		#
		self.label_d_affichage_des_donnees_generales = Label(fenetre, text = texte_du_label_d_affichage_des_donnees_generales)

		#
		self.label_d_affichage_des_donnees_generales.pack()

		#
		self.label_d_affichage_des_donnees_UV = Label(fenetre, text = texte_du_label_d_affichage_de_l_indice_UV_de_la_ville_courante + str(self.situation_de_la_meteo_dans_la_ville_donnee.valeur_de_l_intensite_des_UV_dans_la_ville_donnee) + ".\n" + texte_du_label_d_affichage_du_risque_evalue_que_represente_les_UV + self.situation_de_la_meteo_dans_la_ville_donnee.appreciation_du_risque_d_exposition_aux_UV_dans_la_ville_donnee)

		#
		self.label_d_affichage_des_donnees_UV.pack()

		#
		affichage_de_la_date_et_de_l_heure_du_leve_de_soleil = datetime.datetime.fromtimestamp(self.situation_de_la_meteo_dans_la_ville_donnee.heure_du_leve_de_soleil_pour_la_date_courante_sous_forme_de_timestamp, tz = pytz.timezone(timezone_correspondant_a_la_ville_courante))

		#
		affichage_de_la_date_et_de_l_heure_du_couche_de_soleil = datetime.datetime.fromtimestamp(self.situation_de_la_meteo_dans_la_ville_donnee.heure_du_couche_de_soleil_pour_la_date_courante_sous_forme_de_timestamp, tz = pytz.timezone(timezone_correspondant_a_la_ville_courante))

		#
		if affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.hour < 10:

			#
			heure_correspondant_a_l_heure_du_leve_de_soleil = "0" + str(affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.hour)

		#
		else:

			#
			heure_correspondant_a_l_heure_du_leve_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.hour)

		#
		if affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.minute < 10:

			#
			minute_correspondant_a_l_heure_du_leve_de_soleil = "0" + str(affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.minute)

		#
		else:

			#
			minute_correspondant_a_l_heure_du_leve_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.minute)

		#
		if affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.second < 10:

			#
			seconde_correspondant_a_l_heure_du_leve_de_soleil = "0" + str(affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.second)

		#
		else:

			#
			seconde_correspondant_a_l_heure_du_leve_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.second)

		#
		if affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.hour < 10:

                       	#
                       	heure_correspondant_a_l_heure_du_couche_de_soleil = "0" + str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.hour)

               	#
               	else:

			#
			if affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.hour > 12:

				#
				if language == 0:

					#
					if affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.hour % 12 < 10:

						#
						heure_correspondant_a_l_heure_du_couche_de_soleil = "0" + str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.hour % 12)

					#
					else:

						#
						heure_correspondant_a_l_heure_du_couche_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.hour % 12)

				#
				else:

					#
					heure_correspondant_a_l_heure_du_couche_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.hour)

			#
			else:

                      		#
                      		heure_correspondant_a_l_heure_du_couche_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.hour)

                #
                if affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.minute < 10:

                        #
                        minute_correspondant_a_l_heure_du_couche_de_soleil = "0" + str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.minute)

                #
                else:

                        #
                        minute_correspondant_a_l_heure_du_couche_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.minute)

                #
               	if affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.second < 10:

                        #
                        seconde_correspondant_a_l_heure_du_couche_de_soleil = "0" + str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.second)

                #
                else:

                        #
                        seconde_correspondant_a_l_heure_du_couche_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.second)

		#
		if language == 0:

			#
			indication_avant_midi = " AM"

			#
			indication_apres_midi = " PM"

		#
		else:

			#
			indication_avant_midi = ""

			#
			indication_apres_midi = ""

		#
		self.label_d_affichage_des_donnees_astronomiques = Label(fenetre, text = texte_du_label_d_affichage_de_presentation_de_l_heure_du_lever_de_soleil + heure_correspondant_a_l_heure_du_leve_de_soleil + ":" + minute_correspondant_a_l_heure_du_leve_de_soleil + ":" + seconde_correspondant_a_l_heure_du_leve_de_soleil + indication_avant_midi + ".\n" + texte_du_label_d_affichage_de_presentation_de_l_heure_du_coucher_de_soleil + heure_correspondant_a_l_heure_du_couche_de_soleil + ":" + minute_correspondant_a_l_heure_du_couche_de_soleil + ":" + seconde_correspondant_a_l_heure_du_couche_de_soleil  + indication_apres_midi + ".")

		#
		self.label_d_affichage_des_donnees_astronomiques.pack()
