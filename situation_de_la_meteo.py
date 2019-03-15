# -*- coding: utf-8 -*

#
import pyowm

#Cette classe permet de déterminer la situation météorologique d'une ville passée en paramétre du constructeur dans une unité de mesure des températures passée en paramétre
class Situation_de_la_Meteo():

	#Constructeur de la classe Situation_de_la_Meteo prenant comme paramétres le nom de la  ville, le code du pays correspondant (enregistré dans la table timezone), la clé de l'API et l'unité de mesure de la température (Celsius ou Fahrenheit)
	def __init__(self, ville, code_du_pays_correspondant, cle_de_l_API, unite_de_mesure_de_la_temperature, language):

		#
		self.owm = pyowm.OWM(cle_de_l_API)

		#Récupération des données météorologiques de la ville passée en paramétre grâce à la méthode de la classe OWM  weather_at_place et affectation de celui-ci dans la variable observations
		observations = self.owm.weather_at_place(ville + "," + code_du_pays_correspondant)

		#
		temps_meteorologique = observations.get_weather()

		#
		self.situation_meteorologique_dans_la_ville_donnee = temps_meteorologique.get_status()

		#
		self.url_de_l_icone_de_la_meteo_de_la_ville_courante = "http://openweathermap.org/img/w/" + str(temps_meteorologique.get_weather_icon_name()) + ".png"

		#
		donnees_relatives_a_la_pression_atmospherique = temps_meteorologique.get_pressure()

		#
		self.pression_atmospherique_dans_la_ville_donnee = donnees_relatives_a_la_pression_atmospherique['press']

		#Si l'unité de mesure de la température passée au constructeur est égale à 0, alors...
		if unite_de_mesure_de_la_temperature == 0:

			#L'unité de mesure de la température est fixée à Celsius pour la récupération des données relatives à la température grâce à la fonction get_temperature
			donnees_relatives_a_la_temperature = temps_meteorologique.get_temperature('celsius')

		#Sinon (dans le cas ou celui-ci est égale à 1) alors...
		else:

			#L'unité de mesure de la température est fixée à Fahrenheit pour la récupération des données relatives à la température grâce à la fonction get_temperature
			donnees_relatives_a_la_temperature = temps_meteorologique.get_temperature('fahrenheit')

		#
		self.temperature_dans_la_ville_donnee = donnees_relatives_a_la_temperature['temp']

		#
		self.prevision_de_la_temperature_la_plus_haute_pour_la_ville_donnee = donnees_relatives_a_la_temperature['temp_max']

		#
		self.prevision_de_la_temperature_la_plus_basse_pour_la_ville_donnee = donnees_relatives_a_la_temperature['temp_min']

		#
		donnees_relatives_au_vent = temps_meteorologique.get_wind()

		#Récupération de la vitesse du vent et affectation à l'attribut de la classe Situation_de_la_Meteo vitesse_du_vent
		self.vitesse_du_vent = donnees_relatives_au_vent['speed']

		#Récupération de la valeur de l'Humidité et affectation à l'attribut de la classe Situation_de_la_Meteo humidite_dans_la_ville_donnee
		self.humidite_dans_la_ville_donnee = temps_meteorologique.get_humidity()

		#
		localisation_de_la_ville_donnee = observations.get_location()

		#
		latitude_de_la_ville_donnee = localisation_de_la_ville_donnee.get_lat()

		#
		longitude_de_la_ville_donnee = localisation_de_la_ville_donnee.get_lon()

		#
		donnees_relatives_aux_UV_dans_la_ville_courante = self.owm.uvindex_around_coords(latitude_de_la_ville_donnee, longitude_de_la_ville_donnee)

		#
		self.valeur_de_l_intensite_des_UV_dans_la_ville_donnee = donnees_relatives_aux_UV_dans_la_ville_courante.get_value()

		#
		if language == 0:

			#
			self.appreciation_du_risque_d_exposition_aux_UV_dans_la_ville_donnee = donnees_relatives_aux_UV_dans_la_ville_courante.get_exposure_risk()

		#
		else:

			#
			if donnees_relatives_aux_UV_dans_la_ville_courante.get_exposure_risk() == 'low':

				#
				self.appreciation_du_risque_d_exposition_aux_UV_dans_la_ville_donnee = 'faible'

			#
			elif donnees_relatives_aux_UV_dans_la_ville_courante.get_exposure_risk() == 'moderate':

				#
				self.appreciation_du_risque_d_exposition_aux_UV_dans_la_ville_donnee = 'modéré'

			#
			elif donnees_relatives_aux_UV_dans_la_ville_courante.get_exposure_risk() == 'high':

				#
				self.appreciation_du_risque_d_exposition_aux_UV_dans_la_ville_donnee = 'élevé'

			#
			elif donnees_relatives_aux_UV_dans_la_ville_courante.get_exposure_risk() == 'extreme':

				#
				self.appreciation_du_risque_d_exposition_aux_UV_dans_la_ville_donnee = 'extrême'

			#
			else:

				#
				self.appreciation_du_risque_d_exposition_aux_UV_dans_la_ville_donnee = 'très élevé'

		#Récupération de l'heure du levé de soleil sous forme de timestamp et afféctation à l'attribut de la classe Situation_de_la_Meteo heure_du_leve_de_soleil_pour_la_date_courante_sous_forme_de_timestamp
		self.heure_du_leve_de_soleil_pour_la_date_courante_sous_forme_de_timestamp = temps_meteorologique.get_sunrise_time('unix')

		#Récupération de l'heure du couché de soleil sous forme de timestamp et afféctation à l'attribut de la classe Situation_de_la_Meteo heure_du_couche_de_soleil_pour_la_date_courante_sous_forme_de_timestamp
		self.heure_du_couche_de_soleil_pour_la_date_courante_sous_forme_de_timestamp = temps_meteorologique.get_sunset_time('unix')
