# -*- coding: utf-8 -*

#
try:

	#
	import ttk

	#
	from tkMessageBox import *

#
except ImportError:

	#
	import tkinter.ttk as ttk

	#
	from tkinter.messagebox import *

import datetime
import os
import pytz
import sqlite3
import time
import subprocess
import situation_de_la_meteo
import interface_graphique

#
def renvoie_de_l_id_du_timezone_correspondant_a_l_id_de_la_ville_courante(indice_de_la_ville_courante):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

        #
        curseur.execute("SELECT ville.timezone FROM ville WHERE ville.id = ?", (indice_de_la_ville_courante,))

	#
	resultat_de_la_requete_de_recuperation_de_l_id_de_la_timezone_de_la_ville_dont_id_est_en_parametre = curseur.fetchone()

        #
        connecteur.close()

	#
	return(resultat_de_la_requete_de_recuperation_de_l_id_de_la_timezone_de_la_ville_dont_id_est_en_parametre[0])

#
def renvoie_de_l_id_de_la_ville_pour_les_mises_a_jour():

        #Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

        #
        curseur.execute("SELECT ville.id FROM ville INNER JOIN Mise_a_jour ON Mise_a_jour.ville = ville.id")

        #
        resultat_de_la_requete_de_recuperation_de_l_id_de_la_ville_pour_les_mises_a_jour = curseur.fetchone()

        #
        connecteur.close()

        #
        return int(resultat_de_la_requete_de_recuperation_de_l_id_de_la_ville_pour_les_mises_a_jour[0])

#
def renvoie_de_l_heure_de_la_minute_de_la_seconde_et_de_la_timezone_pour_les_mises_a_jour():

        #Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

        #
        curseur.execute("SELECT Mise_a_jour.heure, Mise_a_jour.minute, Mise_a_jour.seconde, Mise_a_jour.timezone FROM Mise_a_jour")

        #
        resultat_de_la_requete_de_recuperation_de_l_heure_de_la_minute_de_la_seconde_et_de_la_timezone_pour_les_mises_a_jour = curseur.fetchone()

        #
        connecteur.close()

        #
        return resultat_de_la_requete_de_recuperation_de_l_heure_de_la_minute_de_la_seconde_et_de_la_timezone_pour_les_mises_a_jour

#
def renvoie_de_l_id_de_la_ville_pour_faire_sonner_le_reveil():

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#
	curseur.execute("SELECT ville.id FROM ville INNER JOIN Reveil ON Reveil.ville = ville.id")

	#
	resultat_de_la_requete_de_recuperation_de_l_id_de_la_ville_pour_faire_sonner_le_reveil = curseur.fetchone()

	#
        connecteur.close()

	#
	return int(resultat_de_la_requete_de_recuperation_de_l_id_de_la_ville_pour_faire_sonner_le_reveil[0])

#
def renvoie_de_la_frequence_de_la_sonnerie_du_reveil():

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#
	curseur.execute("SELECT Reveil.frequence FROM Reveil")

	#
	resultat_de_la_requete_de_recuperation_de_la_frequence_de_la_sonnerie_du_reveil = curseur.fetchone()

	#
        connecteur.close()

	#
	return int(resultat_de_la_requete_de_recuperation_de_la_frequence_de_la_sonnerie_du_reveil[0])

#
def renvoie_de_l_id_du_single_enregistre_pour_faire_sonner_le_reveil():

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#
	curseur.execute("SELECT Single.id FROM Single INNER JOIN Reveil ON Reveil.single_choisi = Single.id")

	#
	resultat_de_la_requete_de_recuperation_de_l_id_du_single_a_faire_jouer_quand_le_reveil_sonne = curseur.fetchone()

	#
        connecteur.close()

	#
	return resultat_de_la_requete_de_recuperation_de_l_id_du_single_a_faire_jouer_quand_le_reveil_sonne[0]

#
def renvoie_de_l_heure_de_la_minute_de_la_seconde_et_de_la_timezone_pour_faire_sonner_le_reveil():

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

        #
        curseur.execute("SELECT Reveil.heure, Reveil.minute, Reveil.seconde, Reveil.timezone FROM Reveil")

	#
	resultat_de_la_requete_de_recuperation_de_l_heure_de_la_minute_de_la_seconde_et_de_la_timezone_pour_faire_sonner_le_reveil = curseur.fetchone()

	#
        connecteur.close()

	#
	return resultat_de_la_requete_de_recuperation_de_l_heure_de_la_minute_de_la_seconde_et_de_la_timezone_pour_faire_sonner_le_reveil

#
def mise_a_jour_des_modules_python_necessaires_pour_le_reveil():

	#
        heure_et_date_du_systeme = time.strftime("%a %d %b %Y - %H:%M:%S")

        #
      	descripteur_du_fichier_de_logs_pour_la_mise_a_jour_des_modules = os.open("logs/logs_mise_a_jour_des_modules", os.O_WRONLY | os.O_CREAT | os.O_APPEND)

	#
	os.write(descripteur_du_fichier_de_logs_pour_la_mise_a_jour_des_modules, "{heure_et_date_de_lancement_des_mises_a_jour}".format(heure_et_date_de_lancement_des_mises_a_jour = heure_et_date_du_systeme))

	#
	os.write(descripteur_du_fichier_de_logs_pour_la_mise_a_jour_des_modules, "\n\n\n")

	#
	liste_de_tous_les_packets_python_instales = ["pytube", "pytz", "pyowm", "datetime", "pygame", "SpeechRecognition", "Pillow", "PyAudio", "geojson", "chardet", "certifi", "idna", "urllib3", "requests"]

	#
	for packet in liste_de_tous_les_packets_python_instales:

        	#
        	subprocess.call(["sudo", "-H", "pip", "install", "--upgrade", packet], stdout = descripteur_du_fichier_de_logs_pour_la_mise_a_jour_des_modules)

	#
	os.write(descripteur_du_fichier_de_logs_pour_la_mise_a_jour_des_modules, "-----------------------------------------------------------------------------------------------------\n")

	#
	os.close(descripteur_du_fichier_de_logs_pour_la_mise_a_jour_des_modules)

#
def verification_d_appartenance_de_la_chaine_a_un_nom_d_une_ville_inscrite_dans_la_base(mot_dont_l_appartenance_a_un_nom_de_ville_doit_etre_verifie, langue_uttilisee):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#
        if langue_uttilisee == 0:

		#
		requete_a_executer = "SELECT ville.ville_en_en FROM ville WHERE ville.ville_en_en LIKE '%{0}%'".format(mot_dont_l_appartenance_a_un_nom_de_ville_doit_etre_verifie)

		#
		curseur.execute(requete_a_executer)

        #
        if langue_uttilisee == 1:

		#
                requete_a_executer = "SELECT ville.ville_en_fr FROM ville WHERE ville.ville_en_fr LIKE '%{0}%'".format(mot_dont_l_appartenance_a_un_nom_de_ville_doit_etre_verifie)

                #
                curseur.execute(requete_a_executer)

        #
        tableau_des_resultats = curseur.fetchall()

	#
	connecteur.close()

	#
	if len(tableau_des_resultats) == 0:

		#
		return False;

	#
	else:

		#
		return True

#
def contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre(element_a_trouver, tableau_passe_en_parametre):

	#
	contient_l_element_dans_le_tableau_passe_en_parametre = False

	#
	for element_courant in tableau_passe_en_parametre:

		#
		if element_courant == element_a_trouver:

			#
			contient_l_element_dans_le_tableau_passe_en_parametre = True

			#
			break

	#
	return contient_l_element_dans_le_tableau_passe_en_parametre

#
def renvoi_de_l_id_d_une_ville_a_partir_de_son_nom(ville_dont_on_recherche_l_id, langue_uttilisee):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

        #Dans le cas ou la langue uttilisée est l'anglais
        if langue_uttilisee == 0:

                #
                curseur.execute("SELECT ville.id FROM ville WHERE ville.ville_en_en = ?", (ville_dont_on_recherche_l_id,))

        #Sinon...
        if langue_uttilisee == 1:

                #
                curseur.execute("SELECT ville.id FROM ville WHERE ville.ville_en_fr = ?", (ville_dont_on_recherche_l_id,))

        #
        resultat_de_la_requete_de_recuperation_de_l_id_d_une_ville_passee_en_parametre = curseur.fetchone()

        #Férmeture du connecteur grace à la fonction close() appliquée ce premier
        connecteur.close()

	#
	return int(resultat_de_la_requete_de_recuperation_de_l_id_d_une_ville_passee_en_parametre[0])

#
def verification_d_une_correspondance_avec_le_nom_d_une_ville_inscrite_dans_la_base(mot_dont_fait_objet_la_verification_avec_une_ville, langue_uttilisee):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#Dans le cas ou la langue uttilisée est l'anglais
	if langue_uttilisee == 0:

		#
		curseur.execute("SELECT COUNT(ville.ville_en_en) FROM ville WHERE ville.ville_en_en = ?", (mot_dont_fait_objet_la_verification_avec_une_ville,))

	#Sinon...
	else:

		#
		curseur.execute("SELECT COUNT(ville.ville_en_fr) FROM ville WHERE ville.ville_en_fr = ?", (mot_dont_fait_objet_la_verification_avec_une_ville,))

        #
        resultat_de_la_requete_de_verification_d_une_correspondance_du_mot_passe_en_parametre_avec_une_ville = curseur.fetchone()

        #Férmeture du connecteur grace à la fonction close() appliquée ce premier
        connecteur.close()

	#
	if int(resultat_de_la_requete_de_verification_d_une_correspondance_du_mot_passe_en_parametre_avec_une_ville[0]) == 1:

		#
		variable_de_confirmation_de_correspondance = True

	#
	else:

		#
		variable_de_confirmation_de_correspondance = False

	#
	return variable_de_confirmation_de_correspondance

#
def uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, identifiant_en_lettres_de_la_langue_uttilisee):

	#
	subprocess.call(["espeak", "-v" + identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", texte_a_dire_par_eSpeak])

def conversion_du_fichier_audio_extrait_depuis_YouTube_en_wav(nom_du_fichier_audio_extrait_depuis_YouTube):

	#
	subprocess.call(["ffmpeg", "-loglevel", "quiet", "./media/" + nom_du_fichier_audio_extrait_depuis_YouTube + ".wav", "-i", "./media/" + nom_du_fichier_audio_extrait_depuis_YouTube + ".mp4"], shell = False)

#
def filtre_de_la_commande_vocale_de_l_uttilisateur(commande_vocale_de_l_uttilisateur_sous_forme_d_un_string, langue_uttilisee):

	#
	tableau_de_tous_les_mots_contenus_dans_l_interface_vocale = commande_vocale_de_l_uttilisateur_sous_forme_d_un_string.split(" ")

	#
	tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes = []

	#
	nom_de_la_ville_demandee = ""

	#
	incrementeur = 0

	#
	for mot in tableau_de_tous_les_mots_contenus_dans_l_interface_vocale:

		#
		if langue_uttilisee == 0:

			#
			if mot == "delete" or mot == "Delete":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("DELETE")

			#
			if mot == "french" or mot == "French":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("FRENCH")

			#
                        elif mot == "celsius" or mot == "Celsius":

                                #
                                tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("CELSIUS")

                	#
                        elif mot == "fahrenheit" or mot == "Fahrenheit":

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("FAHRENHEIT")

			#
                        elif mot == "show" or mot == "Show":

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("SHOW")

                        #
                        elif mot == "weather" or mot == "Weather":

                                #
                                tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("WEATHER")

                        #
			elif mot == "single" or mot == "Single":

				#
                                tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("SINGLE")

			#
                        elif mot == "configure" or mot == "Configure":

                                #
                                tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("CONFIGURE")

                        #
                        elif mot == "alarm" or mot == "Alarm":

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("ALARM")

                        #
                        elif mot == "included" or mot == "inclusion" or mot == "Inclusion" or mot == "Included" or mot == "added" or mot == "Added" or mot == "adding" or mot == "Adding" or mot == "add" or mot == "Add" or mot == "Download" or mot == "download":

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("INCLUDE")

                        #
                        elif mot == "city" or mot == "City":

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("CITY")

                        #
                        elif mot == "remove" or mot == "Remove" or mot == "delete" or mot == "Delete":

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("REMOVE")

			#
			elif mot == "player" or mot == "Player" or mot == "play" or mot == "Play":

				 #
				 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("READER")

			#
                        elif mot == "single" or mot == "YouTube" or mot == "fichier":

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("YOUTUBE")

			#
			elif mot == "voice" or mot == "Voice":

				#
                                tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("VOICE")

			#
                        elif mot == "Maximum" or mot == "maximum":

                               #
                               tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("MAXIMUM")

                        #
                        elif mot == "Minimum" or mot == "minimum":

                               #
                               tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("MINIMUM")

			#
			elif mot == "consult" or mot == "Consult" or mot == "consultation" or mot == "Consultation":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("CONSULT")

			#
			elif mot == "temperature" or mot == "Temperature":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("TEMPERATURE")

			#
			elif mot == "Sunrise" or mot == "sunrise":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("SUNRISE")

			#
			elif mot == "Sunset" or mot == "sunset":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("SUNSET")

			#
			elif mot == "What" or mot == "what":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("WHAT")

			#
			elif mot == "time" or mot == "Time":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("TIME")

			#
			elif mot == "date" or mot == "Date":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("DATE")

			#
			elif mot == "is" or mot == "Is" or mot == "are" or mot == "Are":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("IS")

			#
			elif mot == "log" or mot == "Log" or mot == "logs" or mot == "Logs":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("LOG")

			#
			elif mot == "Disable" or mot == "disable":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("DISABLE")

			#
			elif mot == "Activate" or mot == "activate":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("ACTIVATE")

			#
			elif mot == "settings" or mot == "Settings" or mot == "setting" or mot == "Setting":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("SETTINGS")

			#
			elif mot == "about" or mot == "About":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("ABOUT")

			#
			elif mot == "updates" or mot == "Updates" or mot == "Update" or mot == "update":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("UPDATES")

			#
                        elif mot == "previous" or mot == "Previous":

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("PREVIOUS")

                        #
                        elif mot == "next" or mot == "Next":

                                 #
                         	 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("NEXT")

		  	#
			elif verification_d_une_correspondance_avec_le_nom_d_une_ville_inscrite_dans_la_base(mot, langue_uttilisee) == True:

				 #
				 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append(mot)

			#
			elif contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("'", mot) == False:

				#
				if verification_d_appartenance_de_la_chaine_a_un_nom_d_une_ville_inscrite_dans_la_base(mot, 0) == True:

				 	#
				 	if nom_de_la_ville_demandee == "":

				 		#
				 		nom_de_la_ville_demandee = nom_de_la_ville_demandee + mot

				 	#
				 	else:

						#
						nom_de_la_ville_demandee = nom_de_la_ville_demandee + " " + mot

		#
		else:

			 #
			 if mot == "supprimer" or mot == "Supprimer" or mot == "suppression" or mot == "Suppression":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("SUPPRESSION")

			 #
			 if mot == "anglais" or mot == "Anglais":

				 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("ANGLAIS")

			 #
			 elif mot == "celsius" or mot == "Celsius":

				 #
				 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("CELSIUS")

			 #
                         elif mot == "fahrenheit" or mot == "Fahrenheit":

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("FAHRENHEIT")

			 #
			 elif mot == "affiche" or mot == "Afficher" or mot == "afficher" or mot == "Affiche":

				 #
				 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("AFFICHER")

			 #
			 elif mot == "météo" or mot == "Météo":

				 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("METEO")

			 #
                         elif mot == "température" or mot == "Température":

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("TEMPERATURE")

			 #
			 elif mot == "Couché" or mot == "couché" or mot == "Couche" or mot == "couche" or mot == "Coucher" or mot == "coucher":

				 #
				 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("COUCHER")

			 #
			 elif mot == "Quelle" or mot == "quelle" or mot == "quelles" or mot == "Quelles" or mot == "quel" or mot == "Quel" or mot == "Quels" or mot == "quels":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("QUELLE")

			 #
			 elif mot == "Heure" or mot == "heure" or mot == "l'heure" or mot == "L'heure":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("HEURE")

			 #
			 elif mot == "Date" or mot == "date":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("DATE")

			 #
			 elif mot == "est-il" or mot == "est" or mot == "Est" or mot == "sont" or mot == "Sont":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("EST")

			 #
			 elif mot == "Levé" or mot == "levé" or mot == "Léve" or mot == "léve" or mot == "Lever" or mot == "lever":

				 #
				 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("LEVER")

			 #
			 elif mot == "configure" or mot == "configurer" or mot == "Configure" or mot == "Configurer":

				 #
				 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("CONFIGURER")

			 #
			 elif mot == "réveil" or mot == "Révéil":

				 #
                               	 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("REVEIL")

			 #
			 elif mot == "inclus" or mot == "Inclus" or mot == "Inclure" or mot == "inclure" or mot == "Inclusion" or mot == "inclusion" or mot == "ajoute" or mot == "Ajoute" or mot == "ajout" or mot == "Ajout" or mot == "télécharger" or mot == "Télécharger":

				 #
				 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("INCLURE")

			 #
			 elif mot == "single" or mot == "Single":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("SINGLE")

			 #
                         elif mot == "Désactiver" or mot == "désactiver":

                                #
                                tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("DESACTIVER")

                         #
                         elif mot == "Activer" or mot == "activer":

                                #
                                tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("ACTIVER")

			 #
			 elif mot == "Paramètres" or mot == "paramètres" or mot == "paramètre" or mot == "Paramètre":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("PARAMETRES")

			 #
			 elif mot == "voix" or mot == "Voix" or mot == "Vocale" or mot == "vocale" or mot == "vocales" or mot == "Vocales":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("VOIX")

			 #
			 elif mot == "maximale" or mot == "Maximale" or mot == "Maximum" or mot == "maximum":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("MAXIMALE")

			 #
			 elif mot == "minimale" or mot == "Minimale" or mot == "Minimum" or mot == "minimum":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("MINIMALE")

			 #
                         elif mot == "consulter" or mot == "Consulter" or mot == "consultation" or mot == "Consultation":

                                #
                                tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("CONSULTER")

			 #
			 elif mot == "mise" or mot == "Mise" or mot == "jour" or mot == "Jour":

				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("MAJ")

			 #
                         elif mot == "log" or mot == "Log" or mot == "logs" or mot == "Logs":

                                #
                                tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("LOG")

			 #
			 elif mot == "ville" or mot == "Ville":

				#
				tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("VILLE")

			 #
			 elif mot == "suppression" or mot == "Suppression" or mot == "supprime" or mot == "Supprime" or mot == "supprimer" or mot == "Supprimer":

				#
                                tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("SUPPRIMER")

			 #
                         elif mot == "lecteur" or mot == "Lecteur" or mot == "jouer" or mot == "Jouer" or mot == "joue" or mot == "Joue" or mot == "lire" or mot == "Lire":

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("LECTEUR")

			 #
			 elif mot == "single" or mot == "YouTube" or mot == "fichier":

				 #
				 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("YOUTUBE")

			 #
			 elif mot == "propos" or mot == "Propos":

				 #
				 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("PROPOS")

			 #
			 elif mot == "précédente" or mot == "Précédente":

				 #
				 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("PRECEDENT")

			 #
			 elif mot == "Soleil" or mot == "soleil":

				 #
				 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("SOLEIL")

			 #
                         elif mot == "suivante" or mot == "Suivante":

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append("SUIVANT")

			 #
                         elif verification_d_une_correspondance_avec_le_nom_d_une_ville_inscrite_dans_la_base(mot, langue_uttilisee) == True:

                                 #
                                 tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append(mot)

			 #
			 elif contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("'", mot) == False:

				  #
				  if verification_d_appartenance_de_la_chaine_a_un_nom_d_une_ville_inscrite_dans_la_base(mot, 0) == True:

                                   	#
                                   	if nom_de_la_ville_demandee == "":

                                        	#
                                        	nom_de_la_ville_demandee = nom_de_la_ville_demandee + mot

                                   	#
                                   	else:

                                        	#
                                        	nom_de_la_ville_demandee = nom_de_la_ville_demandee + " " + mot

		#
		if incrementeur + 1 == len(tableau_de_tous_les_mots_contenus_dans_l_interface_vocale):

			#
			tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes.append(nom_de_la_ville_demandee)

		#
		incrementeur = incrementeur + 1

	#
	return tableau_des_mots_cles_a_retourner_pour_le_declenchement_des_commandes

#Cette fonction renvoie un objet de type datetime correspondant à l'horaire courant du fuseau horaire passé en paramétre
def renvoi_de_la_date_et_de_l_heure(zone_temporelle):

	#
	#
	return datetime.datetime.now(pytz.timezone(zone_temporelle))

#Cette fonction permet de convertir un objet de type datetime passé en paramétre en un objet timestamp (nombre de secondes écoulée depuis le 1er janvier 1970 à minuit)
def conversion_de_date_et_heure_en_timestamp(horaire):

	#
	#
	return time.mktime(horaire.timetuple())

#Cette fonction renvoie une chaine de caractere correspondant à l'horaire courant passé en parametre dans le format passé en paramétre
def renvoi_de_la_date_et_de_l_heure_dans_un_format_donee(horaire, format):

	#
	#
	return horaire.strftime(format)

#Cette fonction renvoie le nombre de villes enregistrées dans la table ville (et donc, le nombre de ville qui est traités)
def initialisation_du_nombre_total_de_villes():

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#Execution de la requête renvoyant le nombre total d'éléments dans la table ville
	curseur.execute("""SELECT COUNT(ville.id) FROM ville""")

	#
	nb_total_de_villes_enregistrees = curseur.fetchone()

	#Férmeture du connecteur grace à la fonction close() appliquée ce premier
        connecteur.close()

	#
	return int(nb_total_de_villes_enregistrees[0])

#Cette fonction renvoie une chaine de caracteres correspondant à l'horaire courant passé en paramétre dans le format determiné dans le language passé en paramétre
def renvoi_de_la_date_et_de_l_heure_pour_l_interface_graphique(datetime_courant, language, format_de_date_choisi):

	#Définition des deux tableaux pour les jours de la semaine, tant en français qu'en anglais
	jour_de_la_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
	days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

	#Définition des deux tableaux pour les mois de l'année, tant en français qu'en anglais
	mois_de_l_annee = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
	months_in_the_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

	#
	if datetime_courant.second < 10:

		#
		seconde = "0" + str(datetime_courant.second)

	else:
		#
		seconde = str(datetime_courant.second)

	#
	if datetime_courant.minute < 10:

		#
		minute = "0" + str(datetime_courant.minute)

	else:
		#
		minute = str(datetime_courant.minute)

	#
	if datetime_courant.hour < 10:

		#
		heure = "0" + str(datetime_courant.hour)

	else:
		#
		heure = str(datetime_courant.hour)


	#
	if datetime_courant.day < 10:

		#
		day = "0" + str(datetime_courant.day)

	else:
		#
		day = str(datetime_courant.day)

	#
	if language == 0:

		#
		jour_courant_dans_la_semaine = days_of_the_week[datetime_courant.weekday()]

		#
		mois_courant_dans_l_annee = months_in_the_year[datetime_courant.month - 1]

	#
	else:

		#
                jour_courant_dans_la_semaine = jour_de_la_semaine[datetime_courant.weekday()]

                #
                mois_courant_dans_l_annee = mois_de_l_annee[datetime_courant.month - 1]

	#
	if format_de_date_choisi == 0:

		#
		return jour_courant_dans_la_semaine + " " + mois_courant_dans_l_annee + " " + day + " " + str(datetime_courant.year) + " " + heure + ":" + minute + ":" + seconde

	#
	elif format_de_date_choisi == 1:

		#
		return jour_courant_dans_la_semaine + " " + day + " " + mois_courant_dans_l_annee + " " + str(datetime_courant.year) + " " + heure + ":" + minute + ":" + seconde

	#
	elif format_de_date_choisi == 2:

		#
		return jour_courant_dans_la_semaine + " " + str(datetime_courant.year) + " " + mois_courant_dans_l_annee + " " + day + " " + heure + ":" + minute + ":" + seconde

	#
	else:

		#
		return jour_courant_dans_la_semaine + " " + str(datetime_courant.year) + " " + day + " " + mois_courant_dans_l_annee + " " + heure + ":" + minute + ":" + seconde

#Cette fonction permet d'afficher le nom de la ville, le pays et la date et l'heure dans celui-ci
def affichage_de_la_date_et_de_l_heure_dans_une_ville_et_un_pays_donne(ville, pays, timezone):
	#
	print(ville + " (" + pays + "): " + renvoi_de_la_date_et_de_l_heure_dans_un_format_donee(renvoi_de_la_date_et_de_l_heure(timezone), "%Y-%m-%d %H:%M:%S %Z%z") + ".")

#
def initialisation_du_tableau_des_villes(language):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
	connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

	#instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#
	if language == 0:

		#
		curseur.execute("""SELECT ville.ville_en_en FROM ville""")

	#
	if language == 1:

		#
		curseur.execute("""SELECT ville.ville_en_fr FROM ville""")

	#
	tableau_des_resultats = curseur.fetchall()

	#Déclaration d'un tableau tableau_des_villes qui contiendra toutes les villes retournées par la précédente requête SQL
	tableau_des_villes = []

	#Déclaration d'une variable incrementeur qui permet d'insérer un élément du résultat de la requête précédente à l'emplacement donné
	incrementeur = 0

	#
	for ville in tableau_des_resultats:

		#La ville courante est insérée dans le tableau tableau_des_villes à l'indice incrementeur
		tableau_des_villes.insert(incrementeur, ville[0])

		#La valeur contenue dans la variable incrementeur est additionée à 1
		incrementeur = incrementeur + 1

	#Fermeture du connecteur après uttilisation de la base de données registre_des_timezones_des_villes_et_des_pays
	connecteur.close()

	#Le tableau des villes est ensuite retournée
	return tableau_des_villes

#
def retour_des_villes_enregistrees_dans_la_base(fenetre, id_de_la_premiere_ville_a_ne_pas_prendre_en_compte, id_de_la_seconde_ville_a_ne_pas_prendre_en_compte, indice_a_mettre_en_place, langue_uttilisee):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#
	if langue_uttilisee == 0:

		#Execution de la requette qui permet de récupérer l'id de la ville passée en paramétre et l'id du timezone correspondant
		curseur.execute("SELECT ville.id, ville.ville_en_en, ville.pays FROM ville WHERE ville.id != ? AND ville.id != ?", (id_de_la_premiere_ville_a_ne_pas_prendre_en_compte, id_de_la_seconde_ville_a_ne_pas_prendre_en_compte))

	#
	else:

        	#Execution de la requette qui permet de récupérer l'id de la ville passée en paramétre et l'id du timezone correspondant
        	curseur.execute("SELECT ville.id, ville.ville_en_fr, ville.pays FROM ville WHERE ville.id != ? AND ville.id != ?", (id_de_la_premiere_ville_a_ne_pas_prendre_en_compte, id_de_la_seconde_ville_a_ne_pas_prendre_en_compte))

	#
	tableau_des_resultats = curseur.fetchall()

	#Déclaration d'un tableau tableau_des_villes qui contiendra toutes les villes retournées par la précédente requette SQL
	tableau_des_villes = []

	#Déclaration d'une variable incrementeur qui permettra d'insérer l'element dans le tableau tableau_des_villes
	incrementeur = 0

	#
	for ville in tableau_des_resultats:

		#
		if langue_uttilisee == 0:

			curseur.execute("SELECT pays.pays_en_en FROM pays WHERE pays.id = ?", (ville[2],))

		#
		else:

			curseur.execute("SELECT pays.pays_en_fr FROM pays WHERE pays.id = ?", (ville[2],))

		#
		resultat_de_la_requete_de_la_requete_de_renvoi_du_nom_du_pays_correspondant_a_la_ville = curseur.fetchone()

		#
		nom_du_pays_correspondant = resultat_de_la_requete_de_la_requete_de_renvoi_du_nom_du_pays_correspondant_a_la_ville[0]

		#L'enregistrement courant est inséré à l'indice incrementeur
		tableau_des_villes.insert(incrementeur, ville[1] + " (" + nom_du_pays_correspondant  + ")")

		#La valeur contenue dans la variable incrementeur est additionée à 1
		incrementeur = incrementeur + 1

	#Férmeture du connecteur grace à la fonction close() appliquée ce premier
	connecteur.close()

	#Initialisation d'une Combobox avec comme paramétre
        combobox_a_retourner = ttk.Combobox(fenetre, state = "readonly", values = tableau_des_villes, width = 45)

	#
	combobox_a_retourner.current(indice_a_mettre_en_place)

	#La combobox remplie précédement du nom des villes en français et des identifiants est retournée
	return combobox_a_retourner

#
def retour_des_timezones_enregistrees_dans_la_base(fenetre, id_du_pays_a_prendre_en_compte):

	#
	indice_a_mettre_en_place = 0

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

        #Execution de la requette qui permet de récupérer l'id de la ville passée en paramétre et l'id du timezone correspondant
	if id_du_pays_a_prendre_en_compte <= 0:

		#
		curseur.execute("SELECT timezone.timezone FROM timezone")

	#
	else:

		#
		curseur.execute("SELECT timezone.timezone FROM timezone WHERE timezone.pays = ?", (id_du_pays_a_prendre_en_compte,))

	#
	tableau_des_resultats = curseur.fetchall()

	#Déclaration d'un tableau tableau_des_villes qui contiendra toutes les villes retournées par la précédente requette SQL
	tableau_des_timezones = []

	#Déclaration d'une variable incrementeur qui permettra d'insérer l'element dans le tableau tableau_des_villes
	incrementeur = 0

	#
	for timezone in tableau_des_resultats:

		#L'enregistrement courant est inséré à l'indice incrementeur
		tableau_des_timezones.insert(incrementeur, timezone[0])

		#La valeur contenue dans la variable incrementeur est additionée à 1
		incrementeur = incrementeur + 1

	#Férmeture du connecteur grace à la fonction close() appliquée ce premier
	connecteur.close()

	#Initialisation d'une Combobox avec comme paramétre
        combobox_a_retourner = ttk.Combobox(fenetre, values = tableau_des_timezones, state = "readonly", width = 50)

	#
	combobox_a_retourner.current(indice_a_mettre_en_place)

	#La combobox remplie précédement du nom des villes en français et des identifiants est retournée
	return combobox_a_retourner

#
def retour_des_pays_enregistres_dans_la_base(fenetre, language, etat):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
	connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

	#instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#
	if language == 0:

		#Execution de la requette qui permet de récupérer l'id du pays passé en paramétre et l'id du timezone correspondant
		curseur.execute("SELECT pays.id, pays.pays_en_en FROM pays WHERE pays.id != 1")

	#Sinon...
	else:

		#Execution de la requette qui permet de récupérer l'id du pays passé en paramétre et l'id du timezone correspondant
        	curseur.execute("SELECT pays.id, pays.pays_en_fr FROM pays WHERE pays.id != 1")

	#
	tableau_des_resultats = curseur.fetchall()

	#Férmeture du connecteur grace à la fonction close() appliquée ce premier
	connecteur.close()

	#Déclaration d'un tableau tableau_des_pays qui contiendra toutes les pays retournés par la précédente requette SQL
	tableau_des_pays = []

	#Déclaration d'une variable incrementeur qui permettra d'insérer l'element dans le tableau tableau_des_pays
        incrementeur = 0

	#
	for pays in tableau_des_resultats:

                #L'enregistrement courant est inséré à l'indice incrementeur
                tableau_des_pays.insert(incrementeur, pays[1])

                #La valeur contenue dans la variable incrementeur est additionée à 1
                incrementeur = incrementeur + 1

	#Initialisation d'une Combobox avec comme paramétre
        combobox_a_retourner = ttk.Combobox(fenetre, state = etat, values = tableau_des_pays, width = 50)

        #
        combobox_a_retourner.current(0)

        #La combobox remplie précédement du nom des villes en français et des identifiants est retournée
        return combobox_a_retourner

#Cette fonction permet de renvoyer l'état du reveil (activé ou désactivé) sous forme d'un booléen (True si le reveil est activé, False dans le cas contraire)
def renvoi_de_l_etat_du_reveil():

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

        #
        curseur.execute("SELECT Reveil.est_active FROM Reveil")

	#
	resultat_de_la_requete_precedente = curseur.fetchone()

	#Férmeture du connecteur grace à la fonction close() appliquée ce premier
        connecteur.close()

	#
	resultat_de_la_requete_precedente_sous_forme_de_int = int(resultat_de_la_requete_precedente[0])

        #
	resultat_de_la_requete_precedente_sous_forme_de_bool = bool(resultat_de_la_requete_precedente_sous_forme_de_int)

	#
	return resultat_de_la_requete_precedente_sous_forme_de_bool

#Cette fonction s'enclenche dés que l'heure (heure, minute, et seconde) passée en paramétre dans la ville passée en paramétre correspond à l'heure incrite pour sonner
def reveil():

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#
	curseur.execute("SELECT Reveil.heure, Reveil.minute, Reveil.seconde, Reveil.frequence FROM Reveil")

	#
	heure_donnee_dans_le_reveil = curseur.fetchone()

	#
	heure_du_reveil = int(heure_donnee_dans_le_reveil[0])
	minute_du_reveil = int(heure_donnee_dans_le_reveil[1])
	seconde_du_reveil = int(heure_donnee_dans_le_reveil[2])
	frequence_du_reveil = int(heure_donnee_dans_le_reveil[3])

	#
	est_active = renvoi_de_l_etat_du_reveil()

	#
	curseur.execute("SELECT timezone.timezone FROM timezone INNER JOIN Reveil ON Reveil.timezone = timezone.id")

	#
	timezone_donnee_dans_le_reveil = curseur.fetchone()

	#
	timezone = timezone_donnee_dans_le_reveil[0]

	#
	horaire = renvoi_de_la_date_et_de_l_heure(timezone)

	#Férmeture du connecteur grace à la fonction close() appliquée ce premier
        connecteur.close()

	#Déclaration de la variable confirmation qui permet de confirmer si il est temps de sonner le reveil ou non
        confirmation = False

	#Dans le cas où la frequence du reveil n'est pas égale à 7 (donc, dans le cas où le reveil n'est pas programé pour sonner tous les jours)
	if not(frequence_du_reveil == 7):

		#Si l'heure courante, la minute courante, la seconde courante, que le jour courant de la ssemaine en cours de la timezone, et que le reveil est active...
		if horaire.hour == heure_du_reveil and horaire.minute == minute_du_reveil and horaire.second == seconde_du_reveil and horaire.weekday() == frequence_du_reveil and est_active == True:

			#
			confirmation = True

	#Dans le cas contraire (donc, dans le cas où la frequence du reveil est programmée pour sonner un des jours de la semaine spécifiée directement)
	else:

		#Si l'heure courante, la minute courante, et la seconde courante de la timezone renseignée sont égales à celle renseignée dans la table Reveil, et que le Reveil lui-même est active alors...
		if horaire.hour == heure_du_reveil and horaire.minute == minute_du_reveil and horaire.second == seconde_du_reveil and est_active == True:

			#
			confirmation = True

	#
	return confirmation

#
def mise_a_jour():

	#
	connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

	#
	curseur = connecteur.cursor()

	#
	curseur.execute("SELECT Mise_a_jour.heure, Mise_a_jour.minute, Mise_a_jour.seconde FROM Mise_a_jour")

	#
	heure_quotidienne_pour_les_mises_a_jour = curseur.fetchone()

	#
	heure_des_mises_a_jour = int(heure_quotidienne_pour_les_mises_a_jour[0])

	#
	minute_des_mises_a_jour = int(heure_quotidienne_pour_les_mises_a_jour[1])

	#
	seconde_des_mises_a_jour = int(heure_quotidienne_pour_les_mises_a_jour[2])

	#
	curseur.execute("SELECT timezone.timezone FROM timezone INNER JOIN Mise_a_jour ON Mise_a_jour.timezone = timezone.id")

	#
	timezone_donnee_pour_les_mises_a_jour = curseur.fetchone()

	#
	timezone = timezone_donnee_pour_les_mises_a_jour[0]

	#
	horaire = renvoi_de_la_date_et_de_l_heure(timezone)

	#
	connecteur.close()

	#
	confirmation = False

	#
	if horaire.hour == heure_des_mises_a_jour and horaire.minute == minute_des_mises_a_jour and horaire.second == seconde_des_mises_a_jour:

		#
		confirmation = True

	#
	return confirmation

#Cette fonction permet de mettre à jour la table reveil grace à l'heure, la minute, la seconde, la frequence et la ville passées en paramétre
def mise_a_jour_de_la_table_reveil(heure, minute, seconde, frequence, id_de_la_ville_selectionnee, id_single_a_jouer):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
	connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

	#instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#Execution de la requette qui permet de récupérer l'id de la ville passée en paramétre et l'id du timezone correspondant
	curseur.execute("SELECT ville.timezone FROM ville WHERE ville.id = ?", (id_de_la_ville_selectionnee,))

	#Récupération de l'id de la ville passée en paramétre et l'id du timezone correspondant dans la variable resultat_de_la_requette
	resultat_de_la_requette = curseur.fetchone()

	#Afféctation de leurs variables respectives dans les variables id_ville et id_timezone
	id_timezone = resultat_de_la_requette[0]

	#
	etat_du_reveil = renvoi_de_l_etat_du_reveil()

	#Suppression de toutes les données contenues dans la table Reveil
	curseur.execute("DELETE FROM Reveil")

	#Préparation de la commande SQL d'insertion de toutes les données passées en paramétre dans la table Reveil
	curseur.execute("INSERT INTO Reveil(heure, minute, seconde, frequence, timezone, ville, single_choisi, est_active) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (heure, minute, seconde, frequence, id_timezone, id_de_la_ville_selectionnee, id_single_a_jouer, etat_du_reveil))

	#Execution de la requette préparée précédement (pour les requettes SELECT uniquement)
	connecteur.commit()

	#
        connecteur.close()

#
def mise_a_jour_de_la_table_Mise_a_jour(heure, minute, seconde, id_de_la_ville):

	#
	connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

	#
	curseur = connecteur.cursor()

	#
	curseur.execute("SELECT ville.timezone FROM ville WHERE ville.id = ?", (id_de_la_ville,))

	#
	resultat_de_la_requette_de_recuperation_du_timezone = curseur.fetchone()

	#
	id_timezone = resultat_de_la_requette_de_recuperation_du_timezone[0]

	#
	curseur.execute("DELETE FROM Mise_a_jour")

	#
	curseur.execute("INSERT INTO Mise_a_jour(heure, minute, seconde, ville, timezone) VALUES(?, ?, ?, ?, ?)", (heure, minute, seconde, id_de_la_ville, id_timezone))

	#
	connecteur.commit()

	#
	connecteur.close()

#Cette fonction affiche la date et l'heure de la ville passée en paramétre
def affichage_de_la_date_et_de_l_heure_passee_en_parametre(ville, language):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

        #Execution de la requette qui permet de récuperer l'id du timezone et l'id du pays correspondants à la ville passée en paramétre
        curseur.execute("SELECT ville.pays, ville.timezone FROM ville WHERE ville.ville_en_fr = ?", (ville,))

        #Affectation du resultat dans la variable resultat_ville grace à la fonction fetchone
        resultat_ville = curseur.fetchone()

	#
	if language == 0:

		#Execution de la requette qui permet de récuperer le nom du pays (sous forme d'une chaine de caractéres) à partir de l'id de celui-ci récupéré grace à la précéden$
        	curseur.execute("SELECT pays.pays_en_en FROM pays WHERE pays.id = ?", (resultat_ville[0],))

	if language == 1:

		#Execution de la requette qui permet de récuperer le nom du pays (sous forme d'une chaine de caractéres) à partir de l'id de celui-ci récupéré grace à la $
                curseur.execute("SELECT pays.pays_en_fr FROM pays WHERE pays.id = ?", (resultat_ville[0],))

	#Affectation du resultat dans la variable pays grace à la fonction fetchone
	pays = curseur.fetchone()

	#Execution de la requette qui permet de récuperer le timezone (sous forme d'une chaine de caractéres) à partir de l'id de celui-ci récupéré grace à l'avant-derniére requette
	curseur.execute("SELECT timezone.timezone FROM timezone WHERE timezone.id = ?", (resultat_ville[1],));

	#Affectation du resultat dans la variable timezone grace à la fonction fetchone
	timezone = curseur.fetchone()

	#
        connecteur.close()

	#Execution de la fonction affichage_de_la_date_et_de_l_heure_dans_une_ville_et_un_pays_donne()
	affichage_de_la_date_et_de_l_heure_dans_une_ville_et_un_pays_donne(ville, pays[0], timezone[0])

#Cette fonction renvoi la date et l'heure de la ville passée en paramétre
def retour_de_la_date_et_de_l_heure_sous_forme_de_string(id_de_la_ville_correspondante, language, format_de_date_choisi):

        #Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#
	if language == 0:

        	#Execution de la requette qui permet de récuperer l'id du timezone et l'id du pays correspondants à la ville passée en paramétre
        	curseur.execute("SELECT ville.pays, ville.timezone, ville.ville_en_en FROM ville WHERE ville.id = ?", (id_de_la_ville_correspondante,))

	#
	if language == 1:
		#Execution de la requette qui permet de récuperer l'id du timezone et l'id du pays correspondants à la ville passée en paramétre
                curseur.execute("SELECT ville.pays, ville.timezone, ville.ville_en_fr FROM ville WHERE ville.id = ?", (id_de_la_ville_correspondante,))

        #Affectation du resultat dans la variable resultat_ville grace à la fonction fetchone
        resultat_ville = curseur.fetchone()

	#
	if language == 0:

        	#Execution de la requette qui permet de récuperer le nom du pays (sous forme d'une chaine de caractéres) à partir de l'id de celui-ci récupéré grace à la précédente requette
        	curseur.execute("SELECT pays.pays_en_en FROM pays WHERE pays.id = ?", (resultat_ville[0],))
	#
	if language == 1:
		#
		curseur.execute("SELECT pays.pays_en_fr FROM pays WHERE pays.id = ?", (resultat_ville[0],))

        #Affectation du resultat dans la variable pays grace à la fonction fetchone
        pays = curseur.fetchone()

        #Execution de la requette qui permet de récuperer le timezone (sous forme d'une chaine de caractéres) à partir de l'id de celui-ci récupéré grace à l'avant-derniére requette
        curseur.execute("SELECT timezone.timezone FROM timezone WHERE timezone.id = ?", (resultat_ville[1],));

        #Affectation du resultat dans la variable timezone grace à la fonction fetchone
        timezone = curseur.fetchone()

	#Férmeture du connecteur grace à la fonction close() appliquée ce premier
        connecteur.close()

	#Retour du resultat sous forme de la chaine de caractéres suivante:
	return str(resultat_ville[2]) + " (" + str(pays[0]) + "): " + renvoi_de_la_date_et_de_l_heure_pour_l_interface_graphique(renvoi_de_la_date_et_de_l_heure(timezone[0]), language, format_de_date_choisi) + " "

#
def retour_de_la_date_et_de_l_heure_passee_en_parametre_sous_forme_de_timestamp(id_de_la_ville_correspondante):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

        #Execution de la requette qui permet de récuperer l'id du timezone et l'id du pays correspondants à la ville passée en paramétre
        curseur.execute("SELECT ville.timezone FROM ville WHERE ville.id = ?", (id_de_la_ville_correspondante,))

        #Affectation du resultat dans la variable resultat_ville grace à la fonction fetchone
        resultat_ville = curseur.fetchone()

        #Execution de la requette qui permet de récuperer le timezone (sous forme d'une chaine de caractéres) à partir de l'id de celui-ci récupéré grace à l'avant-derniére requette
        curseur.execute("SELECT timezone.timezone FROM timezone WHERE timezone.id = ?", (resultat_ville[0],));

        #Affectation du resultat dans la variable timezone grace à la fonction fetchone
        timezone = curseur.fetchone()

	#
        connecteur.close()

	#La date est calculée puis renvoyée sous forme d'un datetime grace à la fonction renvoi_de_la_date_et_de_l_heure
	heure_et_date_en_datetime = renvoi_de_la_date_et_de_l_heure(timezone[0])

        #Retour du resultat sous forme d'un timestamp
        return conversion_de_date_et_heure_en_timestamp(heure_et_date_en_datetime)

#Cette fonction permet de verifier la pertinance des données insérées dans la table timezone
def verification_des_timezones():

	#Définition d'un incrementeur pour le numéro de la ligne:
	incrementeur = 1

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
	connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

	#instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
	curseur = connecteur.cursor()

	#Execution de la requette "SELECT timezone FROM timezone"
	curseur.execute("""SELECT timezone.timezone FROM timezone""")

	#Affectation du resultat dans la variable result_rows grace à la fonction fetchall
	result_rows = curseur.fetchall()

	#Parcours de tous les résulats de la requette precedente executée
	for ligne in result_rows:

		#Inclusion dans un bloc try...except pour tester les données incluses dans la couche de persistance (table timezone)
		try:
			#Affichage de l'heure et de la date sur la timezone indiquée par la variable ligne[0] sous le format %Y-%m-%d %H:%M:%S %Z%z
			temps_maintenant = renvoi_de_la_date_et_de_l_heure(str(ligne[0]))
        		print("numéro " + str(incrementeur) + " - " + str(ligne[0]) + ": " + renvoi_de_la_date_et_de_l_heure_dans_un_format_donee(temps_maintenant, "%Y-%m-%d %H:%M:%S %Z%z"))
		except:
			#Dans le cas ou une erreur se déclanche...
			print("Erreur sur cette timezone-ci: " + str(incrementeur) + " " + str(ligne[0]) +  ".\n");
		finally:
			incrementeur = incrementeur + 1

	#
	connecteur.close()

#Cette fonction permet de verifier la pertinance des données insérées dans la table pays
def verification_des_pays(language):

        #Définition d'un incrementeur pour le numéro de la ligne:
        incrementeur = 1

        #Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les données de la table
        curseur = connecteur.cursor()

	#
	if language == 0:

        	#Execution de la requette "SELECT pays FROM pays"
        	curseur.execute("""SELECT pays.pays_en_fr FROM pays""")

	if language == 1:

		#Execution de la requette "SELECT pays FROM pays"
                curseur.execute("""SELECT pays.pays_en_en FROM pays""")

        #Affectation du resultat dans la variable result_rows grace à la fonction fetchall
        result_rows = curseur.fetchall()

        #Parcours de tous les résulats de la requette précédement executée
        for pays in result_rows:

                #Inclusion dans un bloc try...except pour tester les données incluses dans la couche de persistance (table timezone)
                try:
                        #Affichage de l'heure et de la date sur la timezone indiquée par la variable pays[0]
                        print("numéro " + str(incrementeur) + " - " + str(pays[0]))
                except:
                        #Dans le cas ou une erreur se déclanche...
                        print("Erreur sur ce pays-ci: " + str(incrementeur) + ".\n");
                finally:
                        incrementeur = incrementeur + 1

	#Férmeture du connecteur grace à la fonction close() appliquée ce premier
        connecteur.close()

#Cette fonction permet de vérifier que tous les pays enregistrés dans la base ont le nombre exacte de timezones
def verification_du_nb_de_timezones_par_pays(language):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#Dans le cas où le language choisi est le Français (la variable language est égale à 0)
	if language == 0:

		#
		curseur.execute("""SELECT pays.id, pays.pays_en_fr FROM pays""")

	#Dans le cas où le language choisi est l'Anglais (la variable language est égale à 1)
	if language == 1:

		#
		curseur.execute("""SELECT pays.id, pays.pays_en_en FROM pays""")

	#Affectation du résultat dans la variable resultat_de_la_selection_de_tous_les_pays grace à la fonction fetchall
	resultat_de_la_selection_de_tous_les_pays = curseur.fetchall()

	#Parcours de tous les résultats de la requette précédement executée
	for pays in resultat_de_la_selection_de_tous_les_pays:

		#
		curseur.execute("SELECT count(timezone.id) FROM timezone INNER JOIN pays ON pays.id = timezone.pays WHERE pays.id = ?", (pays[0],))

		#
		nb_de_timezones = curseur.fetchone()

		#
		if language == 0:

			#
			print("Le pays nommé " + str(pays[1]) + " posséde " + str(nb_de_timezones[0]) + " timezones.")

		#
		if language == 1:

			#
			print("The named country " + str(pays[1]) + " have " + str(nb_de_timezones[0]) + " timezones.")

	#Férmeture du connecteur grace à la fonction close() appliquée ce premier
        connecteur.close()

#Cette fonction permet de vérifier le pays auquel est affecté chaque timezone
def verification_de_chaque_timezone_par_pays(language):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
	curseur.execute("""SELECT timezone.timezone FROM timezone""")

	#
	resultat_de_la_selection_de_tous_les_timezones = curseur.fetchall()

	#
	for timezone_courant in resultat_de_la_selection_de_tous_les_timezones:

		#
		if language == 0:

			#
			curseur.execute("SELECT pays.pays_en_fr FROM pays INNER JOIN timezone ON timezone.pays = pays.id WHERE timezone = ?", (timezone_courant[0],))

		#
		if language == 1:

			#
			curseur.execute("SELECT pays.pays_en_en FROM pays INNER JOIN timezone ON timezone.pays = pays.id WHERE timezone = ?", (timezone_courant[0],))

		#
		pays = curseur.fetchone()

		#
		if language == 0:

			#
			print("Le timezone courant " + str(timezone_courant[0]) + " est affecté au pays nommé " + str(pays[0]) + ".")

		#
		if language == 1:

			#
			print("The current timezone " + str(timezone_courant[0]) + " is affected to the named country " + str(pays[0]) + ".")

	#Férmeture du connecteur grace à la fonction close() appliquée ce premier
        connecteur.close()

#Cette fonction permet de déterminer le nombre de timezones d'un pays donné passé en paramétre
def determination_du_nb_de_timezone_d_un_pays_donne(pays):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
        curseur.execute("SELECT count(timezone.id) FROM timezone INNER JOIN pays ON pays.id = timezone.pays WHERE pays.id = ?", (pays,))

	#
	resultat_de_la_requete_renvoyant_le_nb_de_timezone = curseur.fetchone()

	#Le connecteur à la base de données SQLITE est fermé
	connecteur.close()

	#
	return int(resultat_de_la_requete_renvoyant_le_nb_de_timezone[0])

#
def mise_en_forme_de_la_ville_passee_en_parametre(nom_de_la_ville):

	#Définition d'une variable nom_de_la_ville_mis_en_forme correspondant à une chaine de caractére contenant le nom de la ville mis en forme pour vérification dans la base de données
        nom_de_la_ville_mis_en_forme = ""

	#
	incrementeur = 0

        #Le nom de la ville est parcourus grace à une boucle tant que avec pour condition que la valeur de l'incrementeur est strictement inferieur au nombre de caractéres que comprend le nom de la ville
        while(incrementeur < len(nom_de_la_ville)):

                #
                if incrementeur == 0 or nom_de_la_ville[incrementeur - 1] == " ":

                        #
                        nom_de_la_ville_mis_en_forme = nom_de_la_ville_mis_en_forme + nom_de_la_ville[incrementeur].upper()

                #
                else:

                        #
                        nom_de_la_ville_mis_en_forme = nom_de_la_ville_mis_en_forme + nom_de_la_ville[incrementeur]

		#
		incrementeur = incrementeur + 1

	#
	return nom_de_la_ville_mis_en_forme

#Cette fonction permet la suppression d'une ville dans la table ville
def suppression_d_une_ville_dans_la_base(fenetre_courante_de_l_horloge, nom_de_la_ville):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
	fenetre_courante_de_l_horloge.destroy()

	#
	curseur.execute("DELETE FROM ville WHERE ville.ville_en_fr = ?", (nom_de_la_ville,))

	#
	connecteur.commit()

	#Le connecteur de la base de données SQLITE est fermé
	connecteur.close()

	#
	fenetre_courante_de_l_horloge.destroy()

	#
	remise_en_etat_de_tous_les_ids_de_la_table_Ville()

	#
	interface_graphique.initialisation_et_affichage_de_l_horloge()

#Cette fonction permet de déterminer si le nom de la ville passé en paramétre (variable nom_de_la_ville) est valide
def est_valide_comme_nom_de_ville(nom_de_la_ville):

	#Définition de la variable est_valide qui permettra d'indiquer si le nom de la ville passée en paramétre est valide
	est_valide = True

	#Si le nom de la ville nom_de_la_ville passé en paramétre de la fonction est vide...
	if not(nom_de_la_ville.strip()):

		est_valide = False

	#Sinon...
	else:

		#On parcours la chaine de caractéres nom_de_la_ville caractére par caractére
		for caractere in nom_de_la_ville:

			#Dans le cas ou le caractere courant n'est ni une lettre de l'alphabet, ni un apostrophe, ni un espace, ni un tiret, alors...
			if not(caractere.isalpha() == True or caractere == "'" or caractere == " " or caractere == "-"):

				#Le caractere en question est définis comme n'étant pas valide
				est_valide = False

				#On sort de la boucle sans attendre qu'elle atteint le dernier caractére
				break

	#On retourne la valeur contenue dans la variable est_valide
	return est_valide

#Cette fonction permet de déterminer si le nom de la ville (en anglais et en français) correspondant au pays (tous trois passés en paramétres) n'est pas déjà inscrite dans la table ville
def est_presente_dans_la_table_ville(nom_de_la_ville_en_fr, nom_de_la_ville_en_en, id_du_pays_selectionne):

	#Définition d'une variable nom_de_la_ville_mis_en_forme correspondant à une chaine de caractére contenant le nom de la ville mis en forme grace à la fonction mise_en_forme_de_la_ville_passee_en_parametre pour vérification dans la base de données
	nom_de_la_ville_en_fr_mis_en_forme = mise_en_forme_de_la_ville_passee_en_parametre(nom_de_la_ville_en_fr)
	nom_de_la_ville_en_en_mis_en_forme = mise_en_forme_de_la_ville_passee_en_parametre(nom_de_la_ville_en_en)

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
	curseur.execute("SELECT ville.id FROM ville WHERE ville.ville_en_fr = ? AND ville.ville_en_en = ? AND ville.pays = ?", (nom_de_la_ville_en_fr_mis_en_forme, nom_de_la_ville_en_en_mis_en_forme, id_du_pays_selectionne))

	#
	resultats_de_la_selection = curseur.fetchall()

	#
	if not(len(resultats_de_la_selection) ==  0):

		#
		return True

	else:

		#
		return False

#Cette fonction permet de renvoyer le nombre de villes enregistrées dans la base
def renvoi_du_nb_de_villes_enregistrees_dans_la_base():

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

        #
	curseur.execute("SELECT count(ville.id) FROM ville")

	#
	nb_de_villes_enregistrees_dans_la_base = curseur.fetchone()

	#
	connecteur.close()

	#Le nombre de villes enregistrées dans la base (correspondant au résultat de la requête précédente convertit en entier) est retourné
	return int(nb_de_villes_enregistrees_dans_la_base[0])

#Cette fonction permet de déterminer si une ville est valide ou non pour être insérée dans la table ville
def verification_de_la_validite_de_la_ville(nom_de_la_ville_en_fr, nom_de_la_ville_en_en, id_du_pays_selectione):

	#Définition de la variable est_valide qui permettra d'indiquer si le nom de la ville passée en paramétre est valide
	est_valide = True

	#
        if est_valide_comme_nom_de_ville(nom_de_la_ville_en_fr) == False or est_valide_comme_nom_de_ville(nom_de_la_ville_en_en) == False:

		#On affecte la valeur False à la variable est_valide (signe que le nom de la ville n'est pas valide pour insertion)
                est_valide = False

	#Sinon...
	else:

		#Si le nom de la ville passée en paramétre corréspondant au pays séléctionné (également passé en paramétre) est déjà présente dans la table ville, alors...
		if est_presente_dans_la_table_ville(nom_de_la_ville_en_fr, nom_de_la_ville_en_en, id_du_pays_selectione) == True:

			#On affecte la valeur False à la variable est_valide (signe que le nom de la ville n'est pas valide pour insertion)
                	est_valide = False

	#La valeur contenue dans la variable est_valide est retournée
	return est_valide

#Cette fonction met à jour la table ville en recopiant toutes les données conservées dans la table ville (excepté les id) pour les remettres dans la table après suppression de toutes les données présentes
def mise_a_jour_de_la_table_ville():

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#Execution de la requête qui permet de recueillir toutes les données relatives aux villes enregistrées dnas la base
	curseur.execute("""SELECT ville.ville_en_fr, ville.ville_en_en, ville.pays, ville.timezone FROM ville""")

	#
	tableau_des_villes_retournees = curseur.fetchall()

	#Execution de la requête qui permet de supprimer toutes les données enregistrées dans la base
        curseur.execute("DELETE FROM ville")

	#
	connecteur.commit()

	#Execution de la requête qui permet de mettre à jour l'id (autoincrémentée) de la table ville
	curseur.execute("""UPDATE sqlite_sequence SET seq = 0 WHERE name = 'ville'""")

        #
        connecteur.commit()

	#Parcours du tableau tableau_des_villes contenant tous les enregistrements de la table ville
	for ville in tableau_des_villes_retournees:

		#Insertion de l'enregistrement courant dans la table ville
		curseur.execute("INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES(?, ?, ?, ?)", (ville[0], ville[1], ville[2], ville[3]))

		#
		connecteur.commit()

	#Le connecteur à la base de données SQLITE est fermé
        connecteur.close()

#Cette fonction permet de remplacer les caractéres espaces par des underscores à partir d'une chaine passée en paramétre
def remplacement_des_espaces_par_des_underscores(chaine_de_caracteres_initiale):

	#Initialisation de la variable chaine_de_caracteres_retournee qui servira à retourner le résultat final de la fonction
	chaine_de_caracteres_retournee = ""

        #
        for caractere in chaine_de_caracteres_initiale:

                #
                if caractere == " ":

                        #
                        chaine_de_caracteres_retournee = chaine_de_caracteres_retournee + "_"

                #
                else:

                        #
                        chaine_de_caracteres_retournee = chaine_de_caracteres_retournee + caractere

        #Le résultat final est retournée
        return chaine_de_caracteres_retournee

#
def verification_de_la_validite_d_une_chaine_de_caracteres_passee_en_parametre(chaine_de_caracteres_initiale):

	#Initialisation de la variable chaine_de_caracteres_retournee qui servira à retourner le résultat final de la fonction
        chaine_de_caracteres_retournee = ""

	#Définition de la variable est_valide_comme_chaine_de_caractere est initialisation de sa valeur à True
	est_valide_comme_chaine_de_caractere = True

        #
        for caractere in chaine_de_caracteres_initiale:

		#Si le caractère courant n'est pas un caractère alphanumérique, n'est pas un espace, un tiret, ou encore un underscore: Alors...
		if caractere.isalnum() == False and not(caractere == " ") and not(caractere == "-") and not(caractere == "_"):

			#
			est_valide_comme_chaine_de_caractere = False

			#Puis, on quitte définitivement la boucle
			break

	#
	return est_valide_comme_chaine_de_caractere

#Cette fonction permet d'insérer une nouvelle ville dans la base dans le cas ou le nom de celui-ci est équivalent au nom de son timezone correspondant
def insertion_d_une_ville_dans_la_base_concernant_les_pays_a_plusieurs_timezones_dans_le_cas_d_equivalence_entre_nom_de_la_ville_et_nom_du_timezone(ville_en_fr, ville_en_en, pays_selectionne):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#Execution de la requête qui permet de récupérer l'id et le nom de tous les timezones concernant le pays dont l'id est passé en paramétre
	curseur.execute("SELECT timezone.id, timezone.timezone FROM timezone INNER JOIN pays ON pays.id = timezone.pays WHERE pays.id = ?", (pays_selectionne,))

	#Récupération des résultats de la requête précédente dans le tableau resultat_de_la_requete_de_selection_des_timezones
	resultat_de_la_requete_de_selection_des_timezones = curseur.fetchall()

	#Le connecteur à la base de données SQLITE est fermé
        connecteur.close()

	#
	nom_de_la_ville_mis_en_forme = mise_en_forme_de_la_ville_passee_en_parametre(ville_en_en)

	#Seconde phase de la mise en forme du nom de la ville en anglais: Les espaces sont remplacés par des underscores (_)
	nom_de_la_ville_mis_en_forme = remplacement_des_espaces_par_des_underscores(nom_de_la_ville_mis_en_forme)

	#On parcours tous les résultats de la requête précédente (stockés dans le tableau resultat_de_la_requete_de_selection_des_timezones) grace à une variable timezone_courant
	for timezone_courant in resultat_de_la_requete_de_selection_des_timezones:

		#
		decoupage_du_nom_du_timezone_en_deux_parties = str(timezone_courant[1]).split("/")

		#
		dernier_indice_du_tableau = len(decoupage_du_nom_du_timezone_en_deux_parties) - 1

		#
		nom_de_la_ville_contenu_dans_le_nom_du_timezone = decoupage_du_nom_du_timezone_en_deux_parties[dernier_indice_du_tableau]

		#
		id_du_timezone_courant = timezone_courant[0]

		#Dans le cas ou le nom de la ville passée en paramétre et mis en forme est égal au nom de la ville contenu dans le nom du timezone courant...
		if nom_de_la_ville_mis_en_forme == nom_de_la_ville_contenu_dans_le_nom_du_timezone:

			#
			#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        		connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        		#instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        		curseur = connecteur.cursor()

        		#Execution de la requête qui permet de récupérer l'id et le nom de tous les timezones concernant le pays dont l'id est passé en paramétre
        		curseur.execute("INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES (?, ?, ?, ?)", (mise_en_forme_de_la_ville_passee_en_parametre(ville_en_fr), mise_en_forme_de_la_ville_passee_en_parametre(ville_en_en), pays_selectionne, id_du_timezone_courant))

			#
			connecteur.commit()

			#Le connecteur à la base de données SQLITE est fermé
        		connecteur.close()

			#
			break

#
def insertion_d_une_ville_dans_la_base(nom_de_la_ville_en_fr, nom_de_la_ville_en_en, id_du_timezone_correspondant, id_du_pays_correspondant):


	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
	nom_de_la_ville_en_fr = mise_en_forme_de_la_ville_passee_en_parametre(nom_de_la_ville_en_fr)

	#
	nom_de_la_ville_en_en = mise_en_forme_de_la_ville_passee_en_parametre(nom_de_la_ville_en_en)

	#Execution de la requête d'insertion de la ville entrée en paramétre (sous son nom français et anglais) dans la table ville
	curseur.execute("INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES (?, ?, ?, ?)", (nom_de_la_ville_en_fr, nom_de_la_ville_en_en, id_du_pays_correspondant, id_du_timezone_correspondant))

	#
        connecteur.commit()

        #Le connecteur à la base de données SQLITE est fermé
        connecteur.close()

#
def verification_de_l_existence_d_une_equivalence_avec_un_nom_de_timezone(nom_de_la_ville_en_en, indice_du_pays_selectionne):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
	curseur.execute("SELECT timezone.timezone FROM timezone WHERE timezone.pays = ?", (indice_du_pays_selectionne,))

	#Récupération des résultats de la requête précédente dans le tableau resultat_de_la_requete_de_selection_des_timezones
        resultat_de_la_requete_de_selection_des_timezones = curseur.fetchall()

	#
	connecteur.close()

	#
	variable_de_determination_d_une_equivalence_entre_nom_de_la_ville_en_en_et_le_nom_du_timezone = False

	#
        nom_de_la_ville_en_en_apres_une_premiere_mise_en_forme = mise_en_forme_de_la_ville_passee_en_parametre(nom_de_la_ville_en_en)

        #
        nom_de_la_ville_en_en_totalement_mis_en_forme = remplacement_des_espaces_par_des_underscores(nom_de_la_ville_en_en_apres_une_premiere_mise_en_forme)

	#
	possede_une_equivalence_avec_un_nom_de_timezone = False

	#On parcours tous les résultats de la requête précédente (stockés dans le tableau resultat_de_la_requete_de_selection_des_timezones) grace à une variable timezone_courant
        for timezone_courant in resultat_de_la_requete_de_selection_des_timezones:

        	#
               	decoupage_du_nom_du_timezone_en_deux_parties = str(timezone_courant[0]).split("/")

		#
		dernier_indice_du_tableau = len(decoupage_du_nom_du_timezone_en_deux_parties) - 1

                #
                nom_de_la_ville_contenu_dans_le_nom_du_timezone = decoupage_du_nom_du_timezone_en_deux_parties[dernier_indice_du_tableau]

                #Dans le cas ou le nom de la ville passée en paramétre et mis en forme est égal au nom de la ville contenu dans le nom du timezone courant...
                if nom_de_la_ville_en_en_totalement_mis_en_forme == nom_de_la_ville_contenu_dans_le_nom_du_timezone:

			variable_de_determination_d_une_equivalence_entre_nom_de_la_ville_en_en_et_le_nom_du_timezone = True
	#
	return variable_de_determination_d_une_equivalence_entre_nom_de_la_ville_en_en_et_le_nom_du_timezone

#
def verification_de_la_pertinance_de_la_correspondance_entre_le_pays_et_le_timezone_selectionnes(indice_du_pays_selectionne, indice_du_timezone_selectionne):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

        #
        curseur.execute("SELECT * FROM timezone WHERE timezone.pays = ? AND timezone.id = ?", (indice_du_pays_selectionne, indice_du_timezone_selectionne))

        #Récupération des résultats de la requête précédente dans le tableau resultat_de_la_requete_de_selection_des_timezones
        resultat_de_la_requete_de_selection_des_timezones = curseur.fetchall()

        #
        connecteur.close()

	#
	if len(resultat_de_la_requete_de_selection_des_timezones) == 0:

		return False

	#Sinon...
	else:

		return True

#
def renvoi_du_single_utilise_pour_le_reveil():

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

        #
        curseur.execute("""SELECT Single.chemin_d_accee FROM Single INNER JOIN Reveil ON Reveil.single_choisi = Single.id""")

	#Récupération des résultats de la requête précédente dans le tableau resultat_de_la_requete_de_selection_des_timezones
        resultat_de_la_requete_de_recuperation_du_chemin_d_accee_du_fichier_audio_a_jouer_pour_le_reveil = curseur.fetchall()

        #
        connecteur.close()

	#
	return resultat_de_la_requete_de_recuperation_du_chemin_d_accee_du_fichier_audio_a_jouer_pour_le_reveil[0][0]

#
def retour_des_singles_enregistres_dans_la_base(fenetre, indice_a_mettre_en_place):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

        #
	curseur.execute("""SELECT Single.nom_du_single, Single.nom_de_l_auteur FROM Single""")

	#
	resultat_de_la_requete_de_recuperation_des_noms_des_singles_et_de_leurs_auteurs = curseur.fetchall()

	#
	connecteur.close()

	#
	tableau_des_singles = []

	#
	incrementeur = 0

	#
	for enregistrement in resultat_de_la_requete_de_recuperation_des_noms_des_singles_et_de_leurs_auteurs:

		#
		tableau_des_singles.insert(incrementeur, enregistrement[0] + "-" + enregistrement[1])

		#
		incrementeur = incrementeur + 1

	#Initialisation d'une Combobox avec comme paramétre
        combobox_a_retourner = ttk.Combobox(fenetre, values = tableau_des_singles, state = "readonly", width = 50)

        #
        combobox_a_retourner.current(indice_a_mettre_en_place)

        #La combobox remplie précédement du nom des singles et de leurs artistes est retournée
        return combobox_a_retourner

#
def renvoi_du_titre_du_single_a_ecouter(id_du_single_choisi_a_ecouter):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

        #
        curseur.execute("SELECT Single.nom_du_single FROM Single WHERE Single.id = ?", (id_du_single_choisi_a_ecouter,))

	#
	resultat_de_la_requete_de_renvoi_du_titre_du_single_a_ecouter = curseur.fetchall()

	#
        connecteur.close()

	#
	return resultat_de_la_requete_de_renvoi_du_titre_du_single_a_ecouter[0][0]

#
def renvoi_de_l_auteur_du_single_a_ecouter(id_du_single_choisi_a_ecouter):

        #Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

        #
        curseur.execute("SELECT Single.nom_de_l_auteur FROM Single WHERE Single.id = ?", (id_du_single_choisi_a_ecouter,))

        #
        resultat_de_la_requete_de_renvoi_de_l_auteur_du_single_a_ecouter = curseur.fetchall()

	#
        connecteur.close()

        #
        return resultat_de_la_requete_de_renvoi_de_l_auteur_du_single_a_ecouter[0][0]

#
def renvoi_du_nom_du_pays_d_origine_du_single_a_ecouter(id_du_single_choisi_a_ecouter, language):

        #Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
	if language == 0:

		#
		curseur.execute("SELECT pays.pays_en_en FROM pays INNER JOIN Single ON pays.id = Single.pays WHERE Single.id = ?", (id_du_single_choisi_a_ecouter,))

	#
	if language == 1:

        	#
        	curseur.execute("SELECT pays.pays_en_fr FROM pays INNER JOIN Single ON pays.id = Single.pays WHERE Single.id = ?", (id_du_single_choisi_a_ecouter,))

        #
        resultat_de_la_requete_de_renvoi_du_nom_du_pays_d_origine_du_single_a_ecouter = curseur.fetchall()

	#
        connecteur.close()

        #
        return resultat_de_la_requete_de_renvoi_du_nom_du_pays_d_origine_du_single_a_ecouter[0][0]

#
def renvoi_du_fichier_audio_selectionne_pour_etre_joue(id_du_single_choisi_pour_etre_ecoute):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

        #
        curseur.execute("SELECT Single.chemin_d_accee FROM Single WHERE Single.id = ?", (id_du_single_choisi_pour_etre_ecoute,))

	#
        resultat_de_la_requete_de_renvoi_du_chemin_du_single_a_ecouter = curseur.fetchall()

	#
        connecteur.close()

        #
        return resultat_de_la_requete_de_renvoi_du_chemin_du_single_a_ecouter[0][0]

#Cette fonction permet de vérifier si le fichier audio à extraire depuis la vidéo YouTube dont l'identifiant YouTube est passé en paramétre n'est pas déjà enregistré dans la base de données
def verification_de_l_existance_d_un_titre_de_single_similaire_dans_la_base(identifiant_de_la_video_YouTube):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
        curseur.execute("SELECT count(*) FROM Single WHERE Single.identifiant_YouTube_de_la_video_d_origine = ?", (identifiant_de_la_video_YouTube,))

	#
        resultat_de_la_requete_de_renvoi_du_nombre_de_single_extraits_depuis_la_video_YouTube_dont_l_identifiant_est_passe_en_parametre = curseur.fetchall()

        #Fermeture du connecteur après interrogation de la base de données
        connecteur.close()

	#
	nombre_de_single_extraits_depuis_la_video_YouTube_dont_l_identifiant_est_passe_en_parametre = int(resultat_de_la_requete_de_renvoi_du_nombre_de_single_extraits_depuis_la_video_YouTube_dont_l_identifiant_est_passe_en_parametre[0][0])

	#Si le nombre de singles extraits depuis la même vidéo YouTube est strictement supérieur à 0, alors...
	if nombre_de_single_extraits_depuis_la_video_YouTube_dont_l_identifiant_est_passe_en_parametre > 0:

		#Retourner True (Il existe bel et bien 1 single extrait depuis la video Youtube dont l'identifiant YouTube est passé en paramétre)
		return True

	#Sinon...
	else:

		#
		return False

#
def enregistrement_du_fichier_audio_extrait_depuis_la_video_YouTube_renseignee_dans_la_base(nom_du_single, nom_de_l_auteur, pays, nom_du_fichier_audio_extrait_depuis_YouTube, identifiant_YouTube_de_la_video_d_origine):

	#
	nom_et_chemin_relatif_du_fichier_audio = "./media/" + nom_du_fichier_audio_extrait_depuis_YouTube

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
	curseur.execute("INSERT INTO Single(nom_du_single, nom_de_l_auteur, chemin_d_accee, pays, identifiant_YouTube_de_la_video_d_origine) VALUES (?, ?, ?, ?, ?)", (nom_du_single, nom_de_l_auteur, nom_et_chemin_relatif_du_fichier_audio, pays, identifiant_YouTube_de_la_video_d_origine))

	#
        connecteur.commit()

        #Le connecteur à la base de données SQLITE est fermé
        connecteur.close()

#
def changement_d_etat_du_reveil(valeur_de_l_etat_du_reveil_pour_modification, langue_uttilisee, identifiant_en_lettres_de_la_langue_uttilisee):

	#
	try:

		#
		if langue_uttilisee == 0:

			#
                        if valeur_de_l_etat_du_reveil_pour_modification == 1:

				#
				contenu_du_texte_a_dire_en_cas_de_reussite = "The alarm has been activated successfully"

			#
			else:

				#
				contenu_du_texte_a_dire_en_cas_de_reussite = "the alarm has been successfully deactivated"

			#
			contenu_du_texte_a_dire_en_cas_d_echec = "Error: An error occurred in the wakeup state change (on / off)"

		#
		else:

			#
			if valeur_de_l_etat_du_reveil_pour_modification == 1:

				#
				contenu_du_texte_a_dire_en_cas_de_reussite = "Le reveil a été activé avec succès"
			#
			else:

				#
				contenu_du_texte_a_dire_en_cas_de_reussite = "Le reveil a été désactivé avec succès"

			#
			contenu_du_texte_a_dire_en_cas_d_echec = "Erreur: Une erreur est survenue dans le changement d'état du reveil (activation / désactivation)"

		#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        	connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        	#instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        	curseur = connecteur.cursor()

		#
		curseur.execute("UPDATE Reveil SET est_active = ?", (valeur_de_l_etat_du_reveil_pour_modification,))

		#
		connecteur.commit()

		#Le connecteur à la base de données SQLITE est fermé
        	connecteur.close()

		#
		if valeur_de_l_etat_du_reveil_pour_modification == 1:

			#
			uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(contenu_du_texte_a_dire_en_cas_de_reussite, identifiant_en_lettres_de_la_langue_uttilisee)

		#
		else:

			#
			uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(contenu_du_texte_a_dire_en_cas_de_reussite, identifiant_en_lettres_de_la_langue_uttilisee)

	#
	except:

		#
		uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(contenu_du_texte_a_dire_en_cas_d_erreur, identifiant_en_lettres_de_la_langue_uttilisee)

#
def renvoi_du_code_du_pays_ou_de_la_zone_correspondant(id_correspondant_a_la_ville_courante):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
	curseur.execute("SELECT ville.timezone FROM Ville WHERE ville.id = ?", (id_correspondant_a_la_ville_courante,))

	#
	resultat_de_la_requete_de_selection_de_la_timezone_correspondant_au_nom_de_la_ville_passee_en_paramettre = curseur.fetchone()

	#
	id_de_la_timezone_correspondante_de_la_ville_passee_en_parametre = int(resultat_de_la_requete_de_selection_de_la_timezone_correspondant_au_nom_de_la_ville_passee_en_paramettre[0])

	#
	curseur.execute("SELECT timezone.code_du_pays_ou_de_la_region FROM timezone WHERE timezone.id = ?", (id_de_la_timezone_correspondante_de_la_ville_passee_en_parametre,))

	#
	resultat_de_la_requete_de_selection_du_code_du_pays_ou_de_la_region_correspondant_a_la_ville_passee_en_parametre = curseur.fetchone()

	#Le connecteur à la base de données SQLITE est fermé
        connecteur.close()

	#
	return resultat_de_la_requete_de_selection_du_code_du_pays_ou_de_la_region_correspondant_a_la_ville_passee_en_parametre[0]

#
def renvoi_du_nom_du_pays_correspondant_a_l_id_de_la_ville_passe_en_parametre(id_de_la_ville_courante, language):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
	curseur.execute("SELECT ville.pays FROM Ville WHERE ville.id = ?", (id_de_la_ville_courante,))

	#
	resultat_de_la_requete_de_selection_de_l_id_de_la_ville_correspondant_a_l_id_de_la_ville = curseur.fetchone()

	#
	id_du_pays_correspondant_a_la_ville_dont_l_id_est_passe_en_parametre = int(resultat_de_la_requete_de_selection_de_l_id_de_la_ville_correspondant_a_l_id_de_la_ville[0])

	#
	if language == 0:

		#
		curseur.execute("SELECT pays.pays_en_en FROM Pays WHERE pays.id = ?", (id_du_pays_correspondant_a_la_ville_dont_l_id_est_passe_en_parametre,))

	#
	else:

		#
		curseur.execute("SELECT pays.pays_en_fr FROM Pays WHERE pays.id = ?", (id_du_pays_correspondant_a_la_ville_dont_l_id_est_passe_en_parametre,))

	#
	resultat_de_la_requete_de_selection_du_nom_du_pays_dans_la_langue_choisie_correspondant_a_la_ville_demandee = curseur.fetchone()

	#Le connecteur à la base de données SQLITE est fermé
        connecteur.close()

	#
	return resultat_de_la_requete_de_selection_du_nom_du_pays_dans_la_langue_choisie_correspondant_a_la_ville_demandee[0]

#
def renvoi_du_nom_de_la_ville_courante_pour_la_meteo_a_partir_de_son_id(id_de_la_ville_courante):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
	curseur.execute("SELECT ville.ville_en_en FROM Ville WHERE ville.id = ?", (id_de_la_ville_courante,))

	#
	resultat_de_la_requete_de_selection_du_nom_de_la_ville_courante_en_anglais_a_partir_de_son_id = curseur.fetchone()

	#Le connecteur à la base de données SQLITE est fermé
        connecteur.close()

	#
	return resultat_de_la_requete_de_selection_du_nom_de_la_ville_courante_en_anglais_a_partir_de_son_id[0]

#
def renvoi_du_timezone_correspondant_a_l_id_de_la_ville_passe_en_parametre(id_de_la_ville_courante):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
	curseur.execute("SELECT ville.timezone FROM Ville WHERE ville.id = ?", (id_de_la_ville_courante,))

	#
	resultat_de_la_requete_de_renvoi_de_l_id_du_timezone_correspondant_a_la_ville_courante = curseur.fetchone()

	#
	id_du_timezone_correspondant_a_la_ville_courante = int(resultat_de_la_requete_de_renvoi_de_l_id_du_timezone_correspondant_a_la_ville_courante[0])

	#
	curseur.execute("SELECT timezone.timezone FROM timezone WHERE timezone.id = ?", (id_du_timezone_correspondant_a_la_ville_courante,))

	#
	resultat_de_la_requete_de_renvoi_du_nom_du_timezone_correspondant_a_la_ville_courante = curseur.fetchone()

	#Le connecteur à la base de données SQLITE est fermé
        connecteur.close()

	#
	return resultat_de_la_requete_de_renvoi_du_nom_du_timezone_correspondant_a_la_ville_courante[0]

#
def renvoi_de_la_ville_parametree_pour_faire_sonner_le_reveil(langue_uttilise):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

	#
	if langue_uttilise == 0:

		#
		curseur.execute("SELECT Ville.ville_en_en FROM Ville INNER JOIN Reveil ON Reveil.ville WHERE Reveil.ville = Ville.id")

	#
	else:

		#
		curseur.execute("SELECT Ville.ville_en_fr FROM Ville INNER JOIN Reveil ON Reveil.ville WHERE Reveil.ville = Ville.id")

	#
	resultat_de_la_requete_de_renvoi_de_la_ville_parametree_pour_faire_sonner_le_reveil = curseur.fetchone()

	#Le connecteur à la base de données SQLITE est fermé
        connecteur.close()

	#
	return resultat_de_la_requete_de_renvoi_de_la_ville_parametree_pour_faire_sonner_le_reveil[0]

#
def renvoi_du_nom_du_pays_correspondant_au_timezone_renseignee_pour_faire_sonner_le_reveil(langue_uttilisee):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

        #
        if langue_uttilisee == 0:

                #
                curseur.execute("SELECT pays.pays_en_en FROM pays INNER JOIN timezone ON timezone.pays = pays.id WHERE timezone.id = (SELECT Reveil.timezone FROM Reveil)")

        #
        else:

                #
                curseur.execute("SELECT pays.pays_en_fr FROM pays INNER JOIN timezone ON timezone.pays = pays.id WHERE timezone.id = (SELECT Reveil.timezone FROM Reveil)")

        #
        resultat_de_renvoi_du_pays_parametre_pour_faire_sonner_le_reveil = curseur.fetchone()

        #Le connecteur à la base de données SQLITE est fermé
        connecteur.close()

	#
	return resultat_de_renvoi_du_pays_parametre_pour_faire_sonner_le_reveil[0]

#
def renvoi_du_nom_de_la_ville_courante_dans_le_language_passe_en_parametre(id_de_la_ville_courante, langue_courante):

	#Connection à la base de données registre_des_timezones_des_villes_et_des_pays
        connecteur = sqlite3.connect('registre_des_timezones_des_villes_et_des_pays.db')

        #instanciation d'une variable curseur (de type cursor) qui va permettre de parcourir les don$
        curseur = connecteur.cursor()

        #
        if langue_courante == 0:

                #
		curseur.execute("SELECT ville.ville_en_en FROM Ville WHERE ville.id = ?", (id_de_la_ville_courante,))

        #
        else:

                #
		curseur.execute("SELECT ville.ville_en_fr FROM Ville WHERE ville.id = ?", (id_de_la_ville_courante,))

        #
        resultat_de_renvoi_du_nom_de_la_ville_courante_dans_la_langue_uttilisee = curseur.fetchone()

        #Le connecteur à la base de données SQLITE est fermé
        connecteur.close()

        #
        return resultat_de_renvoi_du_nom_de_la_ville_courante_dans_la_langue_uttilisee[0]

#
def renvoi_des_donnees_concernant_le_single_enregistre_pour_le_reveil(langue_uttilisee):

	#
	tableau_des_donnees_concernant_le_single_enregistre_pour_le_reveil = []

	#
	id_du_single_enregistre_pour_faire_sonner_le_reveil = renvoie_de_l_id_du_single_enregistre_pour_faire_sonner_le_reveil()

	#
	titre_du_single_enregistre_pour_le_reveil = renvoi_du_titre_du_single_a_ecouter(id_du_single_enregistre_pour_faire_sonner_le_reveil)

	#
	tableau_des_donnees_concernant_le_single_enregistre_pour_le_reveil.append(titre_du_single_enregistre_pour_le_reveil)

	#
	auteur_du_single_enregistre_pour_faire_sonner_le_reveil = renvoi_de_l_auteur_du_single_a_ecouter(id_du_single_enregistre_pour_faire_sonner_le_reveil)

	#
	tableau_des_donnees_concernant_le_single_enregistre_pour_le_reveil.append(auteur_du_single_enregistre_pour_faire_sonner_le_reveil)

	#
	pays_d_origine_du_single_enregistre_pour_faire_sonner_le_reveil = renvoi_du_nom_du_pays_d_origine_du_single_a_ecouter(id_du_single_enregistre_pour_faire_sonner_le_reveil, langue_uttilisee)

	#
	tableau_des_donnees_concernant_le_single_enregistre_pour_le_reveil.append(pays_d_origine_du_single_enregistre_pour_faire_sonner_le_reveil)

	#
	return tableau_des_donnees_concernant_le_single_enregistre_pour_le_reveil

#
def renvoi_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil(langue_uttilisee):

	#
	tableau_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil = []

	#
	heure_minute_seconde_et_timezone_pour_faire_sonner_le_reveil = renvoie_de_l_heure_de_la_minute_de_la_seconde_et_de_la_timezone_pour_faire_sonner_le_reveil()

	#
	tableau_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil.append(heure_minute_seconde_et_timezone_pour_faire_sonner_le_reveil[0])

	#
	tableau_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil.append(heure_minute_seconde_et_timezone_pour_faire_sonner_le_reveil[1])

	#
	tableau_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil.append(heure_minute_seconde_et_timezone_pour_faire_sonner_le_reveil[2])

	#
	pays_correspondant_au_timezone_renseignee_dans_les_parametres_du_reveil = renvoi_du_nom_du_pays_correspondant_au_timezone_renseignee_pour_faire_sonner_le_reveil(langue_uttilisee)

	#
	tableau_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil.append(pays_correspondant_au_timezone_renseignee_dans_les_parametres_du_reveil)

	#
	nom_de_la_ville_parametree_pour_faire_sonner_le_reveil = renvoi_de_la_ville_parametree_pour_faire_sonner_le_reveil(langue_uttilisee)

	#
	tableau_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil.append(nom_de_la_ville_parametree_pour_faire_sonner_le_reveil)

	#
	frequence_pour_faire_sonner_le_reveil = renvoie_de_la_frequence_de_la_sonnerie_du_reveil()

	#
	tableau_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil.append(frequence_pour_faire_sonner_le_reveil)

	#
	return tableau_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil

#
def expression_de_donnees_meteo_par_la_commande_vocale(tableau_des_donnees_meteo_demandees, id_de_la_ville_courante, cle_de_l_API, unite_de_mesure_en_chiffre_de_la_temperature, langue_uttilisee):

	#
	texte_a_dire_par_eSpeak = ""

	#
	code_du_pays_ou_de_la_zone_correspondant = renvoi_du_code_du_pays_ou_de_la_zone_correspondant(id_de_la_ville_courante)

	#
	nom_de_la_ville_courante_a_uttiliser_pour_la_situation_de_la_meteo = renvoi_du_nom_de_la_ville_courante_pour_la_meteo_a_partir_de_son_id(id_de_la_ville_courante)

	#
	nom_de_la_ville_courante_a_uttiliser_pour_eSpeak = renvoi_du_nom_de_la_ville_courante_dans_le_language_passe_en_parametre(id_de_la_ville_courante, langue_uttilisee)

	#
	tz_name = renvoi_du_timezone_correspondant_a_l_id_de_la_ville_passe_en_parametre(id_de_la_ville_courante)

	#
        nom_du_pays = renvoi_du_nom_du_pays_correspondant_a_l_id_de_la_ville_passe_en_parametre(id_de_la_ville_courante, langue_uttilisee)

	#
	instance_de_la_situation_de_la_meteo_dans_la_ville_passee_en_parametre = situation_de_la_meteo.Situation_de_la_Meteo(nom_de_la_ville_courante_a_uttiliser_pour_la_situation_de_la_meteo, code_du_pays_ou_de_la_zone_correspondant, cle_de_l_API, unite_de_mesure_en_chiffre_de_la_temperature, langue_uttilisee)

	#
	if langue_uttilisee == 0:

		#
		identifiant_en_lettres_de_la_langue_uttilisee = 'en'

	#
	else:

		#
		identifiant_en_lettres_de_la_langue_uttilisee = 'fr'

	#
	if unite_de_mesure_en_chiffre_de_la_temperature == 0:

		#
		unite_de_mesure_en_lettres_de_la_temperature = "Celsius"

	#
	else:

		#
		unite_de_mesure_en_lettres_de_la_temperature = "Fahrenheit"

	#
	if len(tableau_des_donnees_meteo_demandees) < 2:

		#
		if langue_uttilisee == 0:

			#
			if tableau_des_donnees_meteo_demandees[0] == "TEMPERATURE":

				#
				texte_a_dire_par_eSpeak = "Observed temperature in the city " + nom_de_la_ville_courante_a_uttiliser_pour_eSpeak + " located in the country " + nom_du_pays + ": " + str(instance_de_la_situation_de_la_meteo_dans_la_ville_passee_en_parametre.temperature_dans_la_ville_donnee) + " degrees " + unite_de_mesure_en_lettres_de_la_temperature

			#
			elif tableau_des_donnees_meteo_demandees[0] == "SUNRISE":

				#
				affichage_de_la_date_et_de_l_heure_du_leve_de_soleil = datetime.datetime.fromtimestamp(instance_de_la_situation_de_la_meteo_dans_la_ville_passee_en_parametre.heure_du_leve_de_soleil_pour_la_date_courante_sous_forme_de_timestamp, tz = pytz.timezone(tz_name))

				#
				heure_correspondant_a_l_heure_du_leve_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.hour)

				#
				minute_correspondant_a_l_heure_du_leve_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.minute)

				#
				seconde_correspondant_a_l_heure_du_leve_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.second)

				#
				texte_a_dire_par_eSpeak = "The sun rises at " + heure_correspondant_a_l_heure_du_leve_de_soleil + " hours " + minute_correspondant_a_l_heure_du_leve_de_soleil + " minutes and " + seconde_correspondant_a_l_heure_du_leve_de_soleil + " seconds AM"

			#
			elif tableau_des_donnees_meteo_demandees[0] == "SUNSET":

				#
				affichage_de_la_date_et_de_l_heure_du_couche_de_soleil = datetime.datetime.fromtimestamp(instance_de_la_situation_de_la_meteo_dans_la_ville_passee_en_parametre.heure_du_couche_de_soleil_pour_la_date_courante_sous_forme_de_timestamp, tz = pytz.timezone(tz_name))

				#
				heure_correspondant_a_l_heure_du_couche_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.hour % 12)

				#
				minute_correspondant_a_l_heure_du_couche_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.minute)

				#
				seconde_correspondant_a_l_heure_du_couche_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.second)

				#
				texte_a_dire_par_eSpeak = "The sun sets at " + heure_correspondant_a_l_heure_du_couche_de_soleil + " hours " + minute_correspondant_a_l_heure_du_couche_de_soleil + " minutes and " + seconde_correspondant_a_l_heure_du_couche_de_soleil + " seconds PM"

		#
		else:

			#
                        if tableau_des_donnees_meteo_demandees[0] == "TEMPERATURE":

                                #
                                texte_a_dire_par_eSpeak = "Température observée dans la ville " + nom_de_la_ville_courante_a_uttiliser_pour_eSpeak + " située dans le pays " + nom_du_pays + ": " + str(instance_de_la_situation_de_la_meteo_dans_la_ville_passee_en_parametre.temperature_dans_la_ville_donnee) + " degrès " + unite_de_mesure_en_lettres_de_la_temperature

                        #
                        elif tableau_des_donnees_meteo_demandees[0] == "LEVER":

                                #
				affichage_de_la_date_et_de_l_heure_du_leve_de_soleil = datetime.datetime.fromtimestamp(instance_de_la_situation_de_la_meteo_dans_la_ville_passee_en_parametre.heure_du_leve_de_soleil_pour_la_date_courante_sous_forme_de_timestamp, tz = pytz.timezone(tz_name))

				#
				heure_correspondant_a_l_heure_du_leve_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.hour)

				#
				minute_correspondant_a_l_heure_du_leve_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.minute)

				#
				seconde_correspondant_a_l_heure_du_leve_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_leve_de_soleil.second)

				#
				texte_a_dire_par_eSpeak = "Le soleil se lève à " + heure_correspondant_a_l_heure_du_leve_de_soleil + " heures " + minute_correspondant_a_l_heure_du_leve_de_soleil + " minutes et " + seconde_correspondant_a_l_heure_du_leve_de_soleil + "secondes"

                        #
                        elif tableau_des_donnees_meteo_demandees[0] == "COUCHER":

				#
				affichage_de_la_date_et_de_l_heure_du_couche_de_soleil = datetime.datetime.fromtimestamp(instance_de_la_situation_de_la_meteo_dans_la_ville_passee_en_parametre.heure_du_couche_de_soleil_pour_la_date_courante_sous_forme_de_timestamp, tz = pytz.timezone(tz_name))

				#
				heure_correspondant_a_l_heure_du_couche_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.hour)

				#
				minute_correspondant_a_l_heure_du_couche_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.minute)

				#
				seconde_correspondant_a_l_heure_du_couche_de_soleil = str(affichage_de_la_date_et_de_l_heure_du_couche_de_soleil.second)

				#
				texte_a_dire_par_eSpeak = "Le soleil se couche à "+ heure_correspondant_a_l_heure_du_couche_de_soleil + " heures " + minute_correspondant_a_l_heure_du_couche_de_soleil + " minutes et " + seconde_correspondant_a_l_heure_du_couche_de_soleil + " secondes"

	#
	else:

		#
		if langue_uttilisee == 0:

			#
			if tableau_des_donnees_meteo_demandees[0] == "TEMPERATURE" and tableau_des_donnees_meteo_demandees[1] == "MAXIMUM":

				#
				texte_a_dire_par_eSpeak = "Maximum temperature expected in the city " + nom_de_la_ville_courante_a_uttiliser_pour_eSpeak + " located in the country " + nom_du_pays + ": " + str(instance_de_la_situation_de_la_meteo_dans_la_ville_passee_en_parametre.prevision_de_la_temperature_la_plus_haute_pour_la_ville_donnee) + " degrees " + unite_de_mesure_en_lettres_de_la_temperature

			#
			elif tableau_des_donnees_meteo_demandees[0] == "TEMPERATURE" and tableau_des_donnees_meteo_demandees[1] == "MINIMUM":

				#
				texte_a_dire_par_eSpeak = "Minimum temperature expected in the city " + nom_de_la_ville_courante_a_uttiliser_pour_eSpeak + " located in the country " + nom_du_pays + ": " + str(instance_de_la_situation_de_la_meteo_dans_la_ville_passee_en_parametre.prevision_de_la_temperature_la_plus_basse_pour_la_ville_donnee) + " degrees " + unite_de_mesure_en_lettres_de_la_temperature

		#
		else:

			#
			if tableau_des_donnees_meteo_demandees[0] == "TEMPERATURE" and tableau_des_donnees_meteo_demandees[1] == "MAXIMALE":

                                #
                                texte_a_dire_par_eSpeak = "Température maximale prévue dans la ville " + nom_de_la_ville_courante_a_uttiliser_pour_eSpeak + " située dans le pays " + nom_du_pays + ": " + str(instance_de_la_situation_de_la_meteo_dans_la_ville_passee_en_parametre.prevision_de_la_temperature_la_plus_haute_pour_la_ville_donnee) + " degrès " + unite_de_mesure_en_lettres_de_la_temperature

                        #
                        elif tableau_des_donnees_meteo_demandees[0] == "TEMPERATURE" and tableau_des_donnees_meteo_demandees[1] == "MINIMALE":

                                #
                                texte_a_dire_par_eSpeak = "Température minimale prévue dans la ville " + nom_de_la_ville_courante_a_uttiliser_pour_eSpeak + " située dans le pays " + nom_du_pays + ": " + str(instance_de_la_situation_de_la_meteo_dans_la_ville_passee_en_parametre.prevision_de_la_temperature_la_plus_basse_pour_la_ville_donnee) + " degrès " + unite_de_mesure_en_lettres_de_la_temperature

	#
	uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, identifiant_en_lettres_de_la_langue_uttilisee)

#Les lignes de code suivants permettent de tester si toutes les fonctionnalités du module sont au point
if __name__ == '__main__':

	#Sauts de ligne pour la lecture du resultat
	print("\n")

	#Verification de tous les timezones inclus dans la table timezone
	verification_des_timezones()

	#Saut de deux lignes (pour la lisibilité du résultat final)
	print("\n\n");

	#Verification de tous les pays (leurs noms en français) inclus dans la table pays
	verification_des_pays(0)

	#Saut de deux lignes (pour la lisibilité du résultat final)
	print("\n\n")

	#Vérification de tous les pays (leurs noms en anglais) inclus dans la table pays
	verification_des_pays(1)

	#Saut de deux lignes (pour la lisibilité du résultat final)
	print("\n\n")

	#
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Perpignan", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Los Angeles", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Ottawa", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("New York City", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Phoenix", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Moscou", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Vladivostok", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Seoul", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Tokyo", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Pekin", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Londres", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Canberra", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Wellington", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Santiago du Chili", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Johannesburg", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Windhoek", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Antananarivo", 0)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Lima", 0)

	#Saut de deux lignes (pour la lisibilité du résultat final)
	print("\n\n")

	#
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Perpignan", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Los Angeles", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Ottawa", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("New York City", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Phoenix", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Moscou", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Vladivostok", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Seoul", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Tokyo", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Pekin", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Londres", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Canberra", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Wellington", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Santiago du Chili", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Johannesburg", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Windhoek", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Antananarivo", 1)
	affichage_de_la_date_et_de_l_heure_passee_en_parametre("Lima", 1)

	#Saut de deux lignes (pour la lisibilité du résultat final)
	print("\n\n")

	#
	verification_du_nb_de_timezones_par_pays(0)

	#Saut de deux lignes (pour la lisibilité du résultat final)
        print("\n\n")

	#
	verification_de_chaque_timezone_par_pays(0)

	#Saut de deux lignes (pour la lisibilité du rtésultat final)
	print("\n\n")

	#Saut de deux lignes (pour la lisibilité du résultat final)
        print("\n\n")

        #
        verification_du_nb_de_timezones_par_pays(0)

        #Saut de deux lignes (pour la lisibilité du résultat final)
        print("\n\n")

        #
        verification_de_chaque_timezone_par_pays(1)

        #Saut de deux lignes (pour la lisibilité du rtésultat final)
        print("\n\n")

	#Test de la fonction de remplacement des espaces par des underscores
	print(remplacement_des_espaces_par_des_underscores("Ceci est un test !!!!"))
