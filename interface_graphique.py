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

import horloge_monde
import time
import os
import extracteur_de_fichiers_audio_depuis_des_videos_YouTube
import configuration_du_reveil
import pygame
import pygame.mixer
import affichage_de_la_meteo
import insertion_des_villes
import suppression_des_villes
import lecteur_de_musiques_telechargees_depuis_YouTube
import suppression_de_musiques_telechargees_depuis_YouTube
import speech_recognition
import configuration_des_mises_a_jour
import affichage_des_informations_sur_le_reveil
import affichage_du_contenu_des_fichiers_de_logs
import affichage_des_commandes_vocales

#
class Horloge(Frame):

	#Définition du constructeur de la classe Horloge
	def __init__(self, fenetre, titre, width_fenetre, height_fenetre):

		#Appel au constructeur de la classe parente
		Frame.__init__(self, fenetre, width = width_fenetre, height = height_fenetre)

		#
		self.langue_selectionnee = IntVar()

		#
		self.langue_uttilisee = 0

		#
		self.langue_selectionnee.set(0)

		#
		self.identifiant_en_lettres_de_la_langue_uttilisee = 'en'

		#
		self.format_de_date_selectionne = IntVar()

		#
		self.format_de_date_uttilisee = 0

		#
		self.format_de_date_selectionne.set(0)

		#
		self.pack(fill = BOTH)

		#
		self.afficheur = Label(self, font = ('times', 20, 'bold'), fg = 'yellow', bg = 'blue')

		#
		self.afficheur.pack()

		#
		self.cle_de_l_API_pour_uttilisation_des_fonctionnalites_d_OpenWeather = "adf02119ee79c20ceea9e04073a15bc2"

		#
		self.bouton_avant = Button(self, text = "Next city", command = self.suivant)

		#
		self.bouton_de_declenchement_de_la_commande_vocale = Button(self, text = "Tap here, then talk", bg = "blue", fg = "white", command = self.commande_vocale_du_reveil)

		#
		self.bouton_arriere = Button(self, text = "Previous city", command = self.precedent)

		#
		self.bouton_arriere.pack(side = "left")

		#
		self.bouton_de_declenchement_de_la_commande_vocale.pack(side = "left")

		#
		self.bouton_avant.pack(side = "right")

		#
		barre_de_menu_du_reveil = Menu(fenetre)

		#
		self.menu_des_villes = Menu(barre_de_menu_du_reveil, tearoff = 0)

		#
		self.menu_des_villes.add_command(label = "Inclusion of a new city", command = self.insertion_d_une_nouvelle_ville)

		#
		self.menu_des_villes.add_command(label = "Deleting a city", command = self.suppression_d_une_ville)

		#
		self.est_active_reveil = BooleanVar()

		#
		self.etat_du_reveil = horloge_monde.renvoi_de_l_etat_du_reveil()

		#
		self.est_active_reveil.set(self.etat_du_reveil)

		#
		barre_de_menu_du_reveil.add_cascade(label = "Villes", menu = self.menu_des_villes)

		#
		self.menu_du_reveil = Menu(barre_de_menu_du_reveil, tearoff = 0)

		#
		self.menu_du_reveil.add_command(label = "Alarm clock configuration", command = self.configuration_du_reveil)

		#
		self.menu_du_reveil.add_checkbutton(label = "Is activated", variable = self.est_active_reveil, command = self.changement_de_l_etat_du_reveil_a_l_aide_de_la_case_a_cocher)

		#
		barre_de_menu_du_reveil.add_cascade(label = "Réveil", menu = self.menu_du_reveil)

		#
		self.menu_de_configuration_des_mises_a_jour = Menu(barre_de_menu_du_reveil, tearoff = 0)

		#
		self.menu_de_configuration_des_mises_a_jour.add_command(label = "Configuring the moment to update", command = self.configuration_des_mises_a_jour)

		#
		barre_de_menu_du_reveil.add_cascade(label = "Configuration des mises à jour", menu = self.menu_de_configuration_des_mises_a_jour)

		#
		self.menu_des_langues_et_des_formats = Menu(barre_de_menu_du_reveil, tearoff = 0)

		#
		self.menu_des_langues_et_des_formats.add_radiobutton(label = "English", variable = self.langue_selectionnee, command = self.choix_de_la_langue, value = 0)

		#
		self.menu_des_langues_et_des_formats.add_radiobutton(label = "Français", variable = self.langue_selectionnee, command = self.choix_de_la_langue, value = 1)

		#
		self.menu_des_langues_et_des_formats.add_separator()

		#
		self.menu_des_langues_et_des_formats.add_radiobutton(label = "MDY", variable = self.format_de_date_selectionne, command = self.choix_du_format_de_date, value = 0)

		#
		self.menu_des_langues_et_des_formats.add_radiobutton(label = "DMY", variable = self.format_de_date_selectionne, command = self.choix_du_format_de_date, value = 1)

		#
		self.menu_des_langues_et_des_formats.add_radiobutton(label = "YMD", variable = self.format_de_date_selectionne, command = self.choix_du_format_de_date, value = 2)

		#
		self.menu_des_langues_et_des_formats.add_radiobutton(label = "YDM", variable = self.format_de_date_selectionne, command = self.choix_du_format_de_date, value = 3)

		#
		barre_de_menu_du_reveil.add_cascade(label = "Langues et formats", menu = self.menu_des_langues_et_des_formats)

		#Cette variable permet de déterminer si la boite de configuration du reveil est ouverte ou pas (elle est définie par défaut comme pas ouverte)
		self.est_ouverte_boite_de_configuration_du_reveil = False

		#Cette variable permet de déterminer si la boite d'insertion de nouvelles villes est ouverte ou pas (elle est définie par défaut comme pas ouverte)
		self.est_ouverte_boite_d_insertion_des_villes = False

		#Cette variable permet de déterminer si la boite de suppression des villes est ouverte ou pas (elle est définie par défaut comme pas ouverte)
		self.est_ouverte_boite_de_suppression_des_villes = False

		#
		self.unite_de_mesure_selectionnee_pour_la_temperature = IntVar()

		#
		self.unite_de_mesure_selectionnee_pour_la_temperature.set(0)

		#
		self.unite_de_mesure_de_la_temperature = 0

		#
		self.menu_de_la_meteo = Menu(barre_de_menu_du_reveil, tearoff = 0)

		#
		self.menu_de_la_meteo.add_command(label = "Weather data display", command = self.affichage_des_donnees_meteo_de_la_ville_courante)

		#
		self.menu_de_la_meteo.add_separator()

		#
		self.menu_de_la_meteo.add_radiobutton(label = "° Celsius", variable = self.unite_de_mesure_selectionnee_pour_la_temperature, command = self.choix_de_l_unite_de_mesure_selectionnee_pour_la_temperature, value = 0)

		#
		self.menu_de_la_meteo.add_radiobutton(label = "° Fahrenheit", variable = self.unite_de_mesure_selectionnee_pour_la_temperature, command = self.choix_de_l_unite_de_mesure_selectionnee_pour_la_temperature, value = 1)

		#
		barre_de_menu_du_reveil.add_cascade(label = "Météo", menu = self.menu_de_la_meteo)

		#
		self.est_ouverte_boite_d_affichage_des_donnees_meteo = False

		#
		self.menu_de_YouTube = Menu(barre_de_menu_du_reveil, tearoff = 0)

		#
		self.menu_de_YouTube.add_command(label = "Playing singles downloaded from YouTube", command = self.lecture_de_fichiers_audio_telecharges_depuis_YouTube)

		#
		self.menu_de_YouTube.add_command(label = "Extraction and download of singles from YouTube", command = self.telechargement_et_extraction_d_un_single_depuis_YouTube)

		#
		self.menu_de_YouTube.add_command(label = "Deleting a single download from YouTube", command = self.suppression_d_un_single_telecharge_depuis_YouTube)

		#
		barre_de_menu_du_reveil.add_cascade(label = "YouTube", menu = self.menu_de_YouTube)

		#
		self.menu_d_aide = Menu(barre_de_menu_du_reveil, tearoff = 0)

		#
		self.menu_d_aide.add_command(label = "Voice commands...", command = self.affichage_des_commandes_vocales)

		#
		self.menu_d_aide.add_command(label = "Showing the contents of the voice command log file...", command = self.affichage_du_contenu_du_fichier_de_log_de_la_commande_vocale_dans_une_fenetre)

		#
		self.menu_d_aide.add_command(label = "Showing the contents of the updates log file...", command = self.affichage_du_contenu_du_fichier_de_log_des_mises_a_jour_dans_une_fenetre)

		#
		self.menu_d_aide.add_command(label = "About...", command = self.affichage_des_informations_sur_le_reveil_intelligent_et_connecte)

		#
		#self.menu_d_aide.add_command(label = "update logs", command = self.affichage_du_contenu_des_logs_des_mises_a_jour)

		#
		#self.menu_d_aide.add_command(label = "voice command logs", command = self.affichage_du_contenu_des_logs_de_la_commande_vocale)

		#
		barre_de_menu_du_reveil.add_cascade(label = "Aide", menu = self.menu_d_aide)

		#
		self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube = False

		#
		self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube = False

		#
		self.frame_courant_de_lecteur_de_fichiers_audio_telecharges_depuis_YouTube = None

		#
		self.fenetre_courante_pour_la_lecteure_de_fichiers_audio_telecharges_depuis_YouTube = None

		#
		self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube = False

		#
		self.est_ouverte_boite_de_configuration_des_mises_a_jour = False

		#
		self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil = False

		#
		self.est_ouverte_boite_d_affichage_des_commandes_vocales = False

		#
		self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour = False

		#
		self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale = False

		#
		self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour = False

		#
		self.time1 = 0

		#
		self.time1_str = ''

		#Initialisation du tableau tableau_des_villes grâce à la fonction initialisation_du_tableau_des_villes du module horloge_monde
		self.array_of_cities = horloge_monde.initialisation_du_tableau_des_villes(0)

		#Initialisation du tableau array_of_cities grâce à la fonction initialisation_du_tableau_des_villes du module horloge_monde
		self.tableau_des_villes = horloge_monde.initialisation_du_tableau_des_villes(1)

		#Initialisation du nombre total de villes traité par le reveil
		self.maximum_de_l_incrementeur = horloge_monde.initialisation_du_nombre_total_de_villes() - 1

		#
		self.incrementeur = 0

		#
		pygame.mixer.init(44100, -16, 2, 2048)

		#
		self.single_utilise_pour_le_reveil = horloge_monde.renvoi_du_single_utilise_pour_le_reveil()

		#
		self.sonnerie = pygame.mixer.Sound(self.single_utilise_pour_le_reveil)

		#
		self.est_en_train_de_sonner_reveil = False

		#
		fenetre.config(menu = barre_de_menu_du_reveil)

		#
                self.texte_d_indication_du_demarrage_des_mises_a_jour_a_dire_par_eSpeak = "Now, updates will be made"

	#Définition d'une fonction choix_de_l_unite_de_mesure_selectionnee_pour_la_temperature() qui permet de choisir l'unité de mesure de la température entre degrés Celsius et degrés Fahrenheit
	def choix_de_l_unite_de_mesure_selectionnee_pour_la_temperature(self):

		#Dans le cas ou la musique du reveil joue, alors...
		if self.est_en_train_de_sonner_reveil == True:

                	#On arrete de la jouer
                	self.sonnerie.stop()

			#
		 	self.est_en_train_de_sonner_reveil = False

			#
			if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

				#
				self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

		#
		else:

			#Si la variable self.est_ouverte_boite_d_insertion_des_villes est à False (donc, si la fenetre d'insertion de nouvelles villes n'est pas ouverte) alors...
			if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#
				numero_de_l_unite_de_mesure_choisie_pour_la_temperature = self.unite_de_mesure_selectionnee_pour_la_temperature.get()

				#
				self.unite_de_mesure_de_la_temperature = numero_de_l_unite_de_mesure_choisie_pour_la_temperature

				#
                        	if self.langue_uttilisee == 0:

					#
					if self.unite_de_mesure_de_la_temperature == 0:

                                		#
                                		texte_a_dire_par_eSpeak = "Now, temperature in celsius."

					#
					else:

						#
						texte_a_dire_par_eSpeak = "Now, temperature in fahrenheit."

                        	#
                        	else:

					#
					if self.unite_de_mesure_de_la_temperature == 0:

                                		#
                                		texte_a_dire_par_eSpeak = "Maintenant, température en celsius."

					#
					else:

						#
                                        	texte_a_dire_par_eSpeak = "Maintenant, température en fahrenheit."

                        	#
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#Sinon...
                	else:

				#
				self.unite_de_mesure_selectionnee_pour_la_temperature.set(self.unite_de_mesure_de_la_temperature)

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: Window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def lecture_de_fichiers_audio_telecharges_depuis_YouTube(self):

		#Dans le cas ou la musique du reveil joue, alors...
		if self.est_en_train_de_sonner_reveil == True:

			#On arrete de la jouer
			self.sonnerie.stop()

			#
			self.est_en_train_de_sonner_reveil = False

			#
			if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

				#
				self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

		#
		else:

			#Si la variable self.est_ouverte_boite_d_insertion_des_villes est à False (donc, si la fenetre d'insertion de nouvelles villes n'est pas ouverte) alors...
			if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#
				self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube = True

				#
        			fenetre_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube = Toplevel()

        			#
        			fenetre_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube.title("Lecteur de musiques téléchargées depuis YouTube")

				#
				fenetre_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube.resizable(False, False)

				#
				fenetre_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube.protocol("WM_DELETE_WINDOW", self.verification_pour_savoir_si_le_lecteur_de_fichiers_audio_telecharges_depuis_YouTube_peut_etre_ferme_ou_pas)

				#
				fenetre_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube.bind("<Destroy>", self.rendre_possible_l_ouverture_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube)

				#
				self.fenetre_courante_pour_la_lecteure_de_fichiers_audio_telecharges_depuis_YouTube = fenetre_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube

        			#
        			lecteur_de_fichiers_audio_telechargees_depuis_YouTube = lecteur_de_musiques_telechargees_depuis_YouTube.Lecteur_de_musiques_telechargees_depuis_YouTube(fenetre_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube, self.langue_uttilisee, 500, 700)

				#
				lecteur_de_fichiers_audio_telechargees_depuis_YouTube.mise_a_jour_de_la_position_de_lecture()

				#
				self.frame_courant_de_lecteur_courant_de_fichiers_audio_telecharges_depuis_YouTube = lecteur_de_fichiers_audio_telechargees_depuis_YouTube

        			#
        			lecteur_de_fichiers_audio_telechargees_depuis_YouTube.mainloop()

			#Sinon...
                	else:

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: Window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def verification_pour_savoir_si_le_lecteur_de_fichiers_audio_telecharges_depuis_YouTube_peut_etre_ferme_ou_pas(self):

		#
		if self.frame_courant_de_lecteur_courant_de_fichiers_audio_telecharges_depuis_YouTube.est_stoppe == False:

			#
			showerror("Erreur par rapport à la fermeture de la fenêtre","Erreur: Il est interdit de fermer le lecteur de fichiers audio téléchargés depuis YouTube pendant que celui-ci joue !!!!")

		#Sinon...
		else:

			#
			self.fenetre_courante_pour_la_lecteure_de_fichiers_audio_telecharges_depuis_YouTube.destroy()

	#
	def rendre_possible_l_ouverture_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube(self, event):

		#La boite de lecture de fichiers audio téléchargés depuis YouTube est fermée, donc False est affectée comme valeur à la variable self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube, donc il est possible de l'ouvrir
		self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube = False

		#
		self.frame_courant_de_lecteur_courant_de_fichiers_audio_telecharges_depuis_YouTube.est_stoppe = None

		#
		self.fenetre_courante_pour_la_lecteure_de_fichiers_audio_telecharges_depuis_YouTube = None

	#
	def affichage_du_contenu_du_fichier_de_log_de_la_commande_vocale_dans_une_fenetre(self):

		#
		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

                        #
                        self.est_en_train_de_sonner_reveil = False

                        #
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

                #
                else:

			#
			if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#
				if os.path.isfile("logs/logs_commande_vocale"):

					#
					fenetre_d_affichage_du_contenu_du_fichier_de_log_de_la_commande_vocale = Toplevel()

					#
					fenetre_d_affichage_du_contenu_du_fichier_de_log_de_la_commande_vocale.title("Affichage du contenu du fichier de log de la commande vocale")

					#
					fenetre_d_affichage_du_contenu_du_fichier_de_log_de_la_commande_vocale.resizable(False, False)

					#
					affichage_du_contenu = affichage_du_contenu_des_fichiers_de_logs.Affichage_du_contenu_des_fichiers_de_logs(fenetre_d_affichage_du_contenu_du_fichier_de_log_de_la_commande_vocale, 500, 700, self.langue_uttilisee, "logs/logs_commande_vocale")

					#
					self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale = True

					#
					fenetre_d_affichage_du_contenu_du_fichier_de_log_de_la_commande_vocale.bind("<Destroy>", self.rendre_possible_l_ouverture_de_la_fenetre_d_affichage_du_fichier_de_log_de_la_commande_vocale)

					#
					fenetre_d_affichage_du_contenu_du_fichier_de_log_de_la_commande_vocale.mainloop()

				#
				else:

					#
					if self.langue_uttilisee == 0:

						#
						texte_a_dire_par_eSpeak_en_cas_de_non_disponibilite_du_fichier = "The requested file is unfortunately not available"

					#
					else:

						#
						texte_a_dire_par_eSpeak_en_cas_de_non_disponibilite_du_fichier = "Le fichier demandée n'est malheureusement pas disponible"

					#
					horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#Sinon...
                        else:

                                #
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: Window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def rendre_possible_l_ouverture_de_la_fenetre_d_affichage_du_fichier_de_log_de_la_commande_vocale(self, event):

		#
		self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale = False

	#
	def affichage_du_contenu_du_fichier_de_log_des_mises_a_jour_dans_une_fenetre(self):

		#
		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

                        #
                        self.est_en_train_de_sonner_reveil = False

                        #
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

                #
                else:

			#
			if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#
				if os.path.isfile("logs/logs_mise_a_jour_des_modules"):

					#
					fenetre_d_affichage_du_contenu_du_fichier_de_log_des_mises_a_jour = Toplevel()

					#
					fenetre_d_affichage_du_contenu_du_fichier_de_log_des_mises_a_jour.title("Affichage du contenu du fichier de log des mises à jour")

					#
					fenetre_d_affichage_du_contenu_du_fichier_de_log_des_mises_a_jour.resizable(False, False)

					#
					affichage_du_contenu = affichage_du_contenu_des_fichiers_de_logs.Affichage_du_contenu_des_fichiers_de_logs(fenetre_d_affichage_du_contenu_du_fichier_de_log_des_mises_a_jour, 1500, 1700, self.langue_uttilisee, "logs/logs_mise_a_jour_des_modules")

					#
					self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour = True

					#
					fenetre_d_affichage_du_contenu_du_fichier_de_log_des_mises_a_jour.bind("<Destroy>", self.rendre_possible_l_ouverture_de_la_fenetre_d_affichage_du_fichier_de_log_des_mises_a_jour)

					#
					fenetre_d_affichage_du_contenu_du_fichier_de_log_des_mises_a_jour.mainloop()

				#
				else:

					#
					if self.langue_uttilisee == 0:

						#
						texte_a_dire_par_eSpeak_en_cas_de_non_disponibilite_du_fichier = "The requested file is unfortunately not available"

					#
					else:

						#
						texte_a_dire_par_eSpeak_en_cas_de_non_disponibilite_du_fichier = "Le fichier demandée n'est malheureusement pas disponible"

					#
					horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#Sinon...
                        else:

                                #
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: Window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def rendre_possible_l_ouverture_de_la_fenetre_d_affichage_du_fichier_de_log_des_mises_a_jour(self, event):

		#
		self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour = False

	#
	def affichage_des_donnees_meteo_de_la_ville_courante(self):

		#Dans le cas ou la musique du reveil joue, alors...
		if self.est_en_train_de_sonner_reveil == True:

			#On arrete de la jouer
			self.sonnerie.stop()

			#
			self.est_en_train_de_sonner_reveil = False

			#
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

		#
		else:

			#Si la variable self.est_ouverte_boite_d_insertion_des_villes est à False (donc, si la fenetre d'insertion de nouvelles villes n'est pas ouverte) alors...
			if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#
                                fenetre_d_affichage_des_donnees_meteo = Toplevel()

                                #
                                fenetre_d_affichage_des_donnees_meteo.title("Affichage des données meteo de la ville courante")

                                #
                                fenetre_d_affichage_des_donnees_meteo.resizable(False, False)

				#
				try:

					#
					affichage_des_donnees_meteorologiques_relatives_a_la_ville_courante = affichage_de_la_meteo.Affichage_de_la_Meteo(fenetre_d_affichage_des_donnees_meteo, 500, 700, self.incrementeur + 1, self.cle_de_l_API_pour_uttilisation_des_fonctionnalites_d_OpenWeather, self.unite_de_mesure_de_la_temperature, self.langue_uttilisee)

					#On affecte True à la variable self.est_ouverte_boite_d_insertion_des_villes, donc la fenetre d'insertion de nouvelles villes est ouverte, donc il est impossible d$
                                	self.est_ouverte_boite_d_affichage_des_donnees_meteo = True

					#Dans le cas ou la fenetre est détruite (événement <Destroy>), alors on appelle la fonction rendre_possible_l_ouverture_de_l_insertion_des_villes
					fenetre_d_affichage_des_donnees_meteo.bind("<Destroy>", self.rendre_possible_l_ouverture_de_l_affichage_des_donnees_meteo_des_villes)

					#
					affichage_des_donnees_meteorologiques_relatives_a_la_ville_courante.mainloop()

				#
				except:

					#
                        		if self.langue_uttilisee == 0:

                                		#
                                		texte_a_dire_par_eSpeak_en_cas_d_erreur = "Error: City does not exist or is misspelled city"

                        		#
                        		else:

                                		#
						texte_a_dire_par_eSpeak_en_cas_d_erreur = "Erreur: La ville n'existe pas ou est mal orthographiée"

					#
					fenetre_d_affichage_des_donnees_meteo.destroy()

                			#
					horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak_en_cas_d_erreur, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#Sinon...
			else:

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: Window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def rendre_possible_l_ouverture_de_l_affichage_des_donnees_meteo_des_villes(self, event):

		#La boite d'affichage des données météo des villes est fermée, donc False est affectée comme valeur à la variable self.est_ouverte_boite_d_affichage_des_donnees_meteo, donc il est possible de l'ouvrir
		self.est_ouverte_boite_d_affichage_des_donnees_meteo = False

	#
	def suppression_d_une_ville(self):

		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

			#
			self.est_en_train_de_sonner_reveil = False

			#
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

		#
		else:

			#Si le nombre de villes enregistrées dans la table ville est strictement supérieur à 1 alors...
			if horloge_monde.renvoi_du_nb_de_villes_enregistrees_dans_la_base() > 2:

                		#Si la variable self.est_ouverte_boite_d_insertion_des_villes est à False (donc, si la fenetre d'insertion de nouvelles villes n'est pas ouverte) alors...
                		if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

					#On affecte True à la variable self.est_ouverte_boite_de_suppression_des_villes, donc la fenetre de suppression des villes est ouverte, donc il est impossible d'en ouvrir une autre
					self.est_ouverte_boite_de_suppression_des_villes = True

					#
					fenetre_de_suppression = Toplevel()

					#
					fenetre_de_suppression.title("Suppression de villes")

					#
					fenetre_de_suppression.resizable(False, False)

					#
					suppression_d_une_ville = suppression_des_villes.Suppression_des_Villes(fenetre_de_suppression, 500, 700, self.incrementeur + 1)

					#Dans le cas ou la fenetre est détruite (événement <Destroy>), alors on appelle la fonction rendre_possible_l_ouverture_de_la_suppression_des_villes
					fenetre_de_suppression.bind("<Destroy>", self.rendre_possible_l_ouverture_de_la_suppression_des_villes)

					#
					suppression_d_une_ville.mainloop()

				#Sinon...
                		else:

					#
                                	if self.langue_uttilisee == 0:

                                        	#
                                        	texte_a_dire_par_eSpeak = "Error: Window already open"

                                	#
                                	else:

                                        	#
                                        	texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                	#
					horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#Sinon...
			else:

				#Une boite de dialogue de type affichage d'erreur (showerror) s'ouvre et indique qu'il est impossible d'ouvrir une autre fenetre de ce type
                        	showerror("Erreur dans l'ouverture de la fenetre d'insertion de nouvelles villes", "Erreur: Il n'y a plus que deux villes dans le tableau, il est donc impossible de supprimer des villes !!!!")

	#
	def rendre_possible_l_ouverture_de_la_suppression_des_villes(self, event):

		#La boite d'insertion de nouvelles villes est fermée, donc False est affectée comme valeur à la variable self.est_ouverte_boite_d_insertion_des_villes, donc il est possible de l'ouvrir
                self.est_ouverte_boite_de_suppression_des_villes = False

		horloge_monde.mise_a_jour_de_la_table_ville()
		#horloge_monde.mise_a_jour_de_l_identifiant_de_la_table_ville()

                #Modification du tableau tableau_des_villes grâce à la fonction initialisation_du_tableau_des_villes du module horloge_monde
                self.array_of_cities = horloge_monde.initialisation_du_tableau_des_villes(0)

                #Modification du tableau array_of_cities grâce à la fonction initialisation_du_tableau_des_villes du module horloge_monde
                self.tableau_des_villes = horloge_monde.initialisation_du_tableau_des_villes(1)

                #Modification du nombre total de villes traité par le reveil
                self.maximum_de_l_incrementeur = horloge_monde.initialisation_du_nombre_total_de_villes() - 1

	#Cette fonction permet de créer une nouvelle instance de Tkinter pour l'insertion de nouvelles villes dna sle reveil
	def insertion_d_une_nouvelle_ville(self):

		#Dans le cas ou la musique du reveil joue, alors...
		if self.est_en_train_de_sonner_reveil == True:

			#On arrete de la jouer
			self.sonnerie.stop()

			#
			self.est_en_train_de_sonner_reveil = False

			#
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

		#
		else:

			#Si la variable self.est_ouverte_boite_d_insertion_des_villes est à False (donc, si la fenetre d'insertion de nouvelles villes n'est pas ouverte) alors...
			if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#On affecte True à la variable self.est_ouverte_boite_d_insertion_des_villes, donc la fenetre d'insertion de nouvelles villes est ouverte, donc il est impossible d'en ouvrir une autre
				self.est_ouverte_boite_d_insertion_des_villes = True

				#
				fenetre_d_insertion = Toplevel()

				#
				if self.langue_uttilisee == 0:

					#
					fenetre_d_insertion.title("Insertion of new cities")

				#
				else:

					#
					fenetre_d_insertion.title("Insertion de nouvelles villes")

				#
				fenetre_d_insertion.resizable(False, False)

				#
				insertion_d_une_ville = insertion_des_villes.Insertion_des_Villes(fenetre_d_insertion, self.langue_uttilisee, 500, 700)

				#Dans le cas ou la fenetre est détruite (événement <Destroy>), alors on appelle la fonction rendre_possible_l_ouverture_de_l_insertion_des_villes
				fenetre_d_insertion.bind("<Destroy>", self.rendre_possible_l_ouverture_de_l_insertion_des_villes)

				#
				insertion_d_une_ville.mainloop()

			#Sinon...
			else:

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: Window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def rendre_possible_l_ouverture_de_l_insertion_des_villes(self, event):

		#La boite d'insertion de nouvelles villes est fermée, donc False est affectée comme valeur à la variable self.est_ouverte_boite_d_insertion_des_villes, donc il est possible de l'ouvrir
		self.est_ouverte_boite_d_insertion_des_villes = False

		#Modification du tableau tableau_des_villes grâce à la fonction initialisation_du_tableau_des_villes du module horloge_monde
                self.array_of_cities = horloge_monde.initialisation_du_tableau_des_villes(0)

                #Modification du tableau array_of_cities grâce à la fonction initialisation_du_tableau_des_villes du module horloge_monde
                self.tableau_des_villes = horloge_monde.initialisation_du_tableau_des_villes(1)

                #Modification du nombre total de villes traité par le reveil
                self.maximum_de_l_incrementeur = horloge_monde.initialisation_du_nombre_total_de_villes() - 1

	#Cette fonction permet de créer une nouvelle instance de Tkinter pour configurer le reveil
	def configuration_du_reveil(self):

		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

			#
			self.est_en_train_de_sonner_reveil = False

			#
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

		#
		else:

			#Si la variable self.est_ouverte_boite_de_configuration_du_reveil est à False (donc, si la fenetre de configuration du reveil n'est pas ouverte) alors...
			if self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#On affecte True à la variable self.est_ouverte_boite_de_configuration_du_reveil, donc la fenetre de configuration du reveil est ouverte, donc il est impossible d'en ouvrir une autre
				self.est_ouverte_boite_de_configuration_du_reveil = True

				#Cette fonction permet de créer une nouvelle instance de la classe Tkinter enfant de la fenetre d'affichage de l'horloge
				fenetre_de_configuration = Toplevel()

				#Définition du titre de cette seconde fenetre
				fenetre_de_configuration.title("Configuration du reveil")

				#
				fenetre_de_configuration.resizable(False, False)

				#
				configuration_du_reveil_pour_l_horloge_courante = configuration_du_reveil.Configuration_du_Reveil(fenetre_de_configuration, self.langue_uttilisee, 500, 700)

				#Dans le cas ou la fenetre est détruite (événement <Destroy>), alors on appelle la fonction rendre_possible_l_ouverture_de_la_configuration_du_reveil
				fenetre_de_configuration.bind("<Destroy>", self.rendre_possible_l_ouverture_de_la_configuration_du_reveil)

				#
				configuration_du_reveil_pour_l_horloge_courante.mainloop()

			#Sinon...
			else:

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: A window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Une fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#Cette fonction a pour finalité de rendre possible l'ouverture de la fenetre de la configuration du reveil
        def rendre_possible_l_ouverture_de_la_configuration_du_reveil(self, event):

                #La boite de configuration du reveil est fermée, donc False est affectée comme valeur à la variable self.est_ouverte_boite_de_configuration_du_reveil, donc il est possible de l'ouvrir
                self.est_ouverte_boite_de_configuration_du_reveil = False

	#Cette fonction permet de créer une nouvelle instance de Tkinter pour le téléchargement et l'extraction d'un nouveau single depuis YouTube
	def telechargement_et_extraction_d_un_single_depuis_YouTube(self):

		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

			#
			self.est_en_train_de_sonner_reveil = False

			#
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()
		#
		else:

			#Si la variable self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube est à False (donc, si la fenetre d'extraction et de téléchargement de singles depuis YouTube n'est pas ouverte) alors...
                	if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#
				self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube = True

				#
				fenetre_d_extraction_et_de_telechargement_depuis_YouTube = Toplevel()

				#
				fenetre_d_extraction_et_de_telechargement_depuis_YouTube.title("Extraction et téléchargement depuis des vidéos YouTube")

				#
				fenetre_d_extraction_et_de_telechargement_depuis_YouTube.resizable(False, False)

				#
				extracteur_et_telechargeur_de_singles_depuis_YouTube = extracteur_de_fichiers_audio_depuis_des_videos_YouTube.Extracteur_de_fichiers_audio_depuis_YouTube(fenetre_d_extraction_et_de_telechargement_depuis_YouTube, self.langue_uttilisee, 500, 700)

				#Dans le cas ou la fenetre est détruite (événement <Destroy>), alors on appelle la fonction rendre_possible_l_ouverture_de_l_extraction_et_du_telechargement_de_single_depuis_YouTube
				fenetre_d_extraction_et_de_telechargement_depuis_YouTube.bind("<Destroy>", self.rendre_possible_l_ouverture_de_l_extraction_et_du_telechargement_de_single_depuis_YouTube)

				#
				fenetre_d_extraction_et_de_telechargement_depuis_YouTube.mainloop()

			#
			else:

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: Window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#Cette fonction a pour finalité de rendre possible l'ouverture de la fenetre d'extraction et de téléchargement de single depuis YouTube
	def rendre_possible_l_ouverture_de_l_extraction_et_du_telechargement_de_single_depuis_YouTube(self, event):

		#
		self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube = False

	#
	def suppression_d_un_single_telecharge_depuis_YouTube(self):

		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

			#
			self.est_en_train_de_sonner_reveil = False

			#
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()
		#
		else:

			#Si la variable self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube est à False (donc, si la fenetre d'extraction et de téléchargement de singles depuis YouTube n'est pas ouverte) alors...
                	if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#
				self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube = True

				#
				fenetre_de_suppression_d_un_single_telecharge_depuis_YouTube = Toplevel()

				#
				fenetre_de_suppression_d_un_single_telecharge_depuis_YouTube.title("Suppression d'un single téléchargé depuis YouTube")

				#
				fenetre_de_suppression_d_un_single_telecharge_depuis_YouTube.resizable(False, False)

				#
				suppression_de_fichiers_audio_telecharges_depuis_YouTube = suppression_de_musiques_telechargees_depuis_YouTube.Suppression_de_musiques_telechargees_depuis_YouTube(fenetre_de_suppression_d_un_single_telecharge_depuis_YouTube, self.langue_uttilisee, 500, 700)

				#Dans le cas ou la fenetre est détruite (événement <Destroy>), alors on appelle la fonction rendre_possible_l_ouverture_de_l_extraction_et_du_telechargement_de_single_depuis_YouTube
				fenetre_de_suppression_d_un_single_telecharge_depuis_YouTube.bind("<Destroy>", self.rendre_possible_l_ouverture_de_la_suppression_d_un_single_telecharge_depuis_YouTube)

				#
				fenetre_de_suppression_d_un_single_telecharge_depuis_YouTube.mainloop()

			#
			else:

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: Window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def rendre_possible_l_ouverture_de_la_suppression_d_un_single_telecharge_depuis_YouTube(self, event):

		#
		self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube = False

	#
	def affichage_des_informations_sur_le_reveil_intelligent_et_connecte(self):

		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

                        #
                        self.est_en_train_de_sonner_reveil = False

                        #
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()
                #
                else:

                        #Si la variable self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube est à False (donc, si la fenetre d'extraction et de téléchargement de singles depuis$
                        if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

                                #
                                self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil = True

                                #
                                fenetre_d_affichage_des_informations_sur_le_reveil = Toplevel()

                                #
                                fenetre_d_affichage_des_informations_sur_le_reveil.title("A propos...")

                                #
                                fenetre_d_affichage_des_informations_sur_le_reveil.resizable(False, False)

				#
				affichage_des_informations_sur_le_reveil.Affichage_des_informations_sur_le_reveil(fenetre_d_affichage_des_informations_sur_le_reveil, 500, 700, self.langue_uttilisee)

				#
                                fenetre_d_affichage_des_informations_sur_le_reveil.bind("<Destroy>", self.rendre_possible_l_ouverture_de_l_affichage_des_informations_sur_le_reveil_intelligent_et_connecte)

                                #
                                fenetre_d_affichage_des_informations_sur_le_reveil.mainloop()

                        #
                        else:

                                #
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: Window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def rendre_possible_l_ouverture_de_l_affichage_des_informations_sur_le_reveil_intelligent_et_connecte(self, event):

		#
		self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil = False

	#
	def affichage_des_commandes_vocales(self):

		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

                        #
                        self.est_en_train_de_sonner_reveil = False

                        #
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()
                #
                else:

                        #Si la variable self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube est à False (donc, si la fenetre d'extraction et de téléchargement de singles depuis$
                        if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

                                #
                                self.est_ouverte_boite_d_affichage_des_commandes_vocales = True

                                #
                                fenetre_d_affichage_des_commandes_vocales = Toplevel()

                                #
                                fenetre_d_affichage_des_commandes_vocales.title("Affichage des commandes vocales")

                                #
                                fenetre_d_affichage_des_commandes_vocales.resizable(False, False)

				#
				affichage_des_commandes_vocales.Affichage_des_commandes_vocales(fenetre_d_affichage_des_commandes_vocales, 500, 700, self.langue_uttilisee)

				#
                                fenetre_d_affichage_des_commandes_vocales.bind("<Destroy>", self.rendre_possible_l_ouverture_de_l_affichage_des_commandes_vocales)

                                #
                                fenetre_d_affichage_des_commandes_vocales.mainloop()

                        #
                        else:

                                #
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: Window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def rendre_possible_l_ouverture_de_l_affichage_des_commandes_vocales(self, event):

		#
		self.est_ouverte_boite_d_affichage_des_commandes_vocales = False

	#
	def configuration_des_mises_a_jour(self):

		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

                        #
                        self.est_en_train_de_sonner_reveil = False

                        #
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()
                #
                else:

                        #Si la variable self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube est à False (donc, si la fenetre d'extraction et de téléchargement de singles depuis$
                        if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

                                #
                                self.est_ouverte_boite_de_configuration_des_mises_a_jour = True

                                #
                                fenetre_de_configuration_des_mises_a_jour = Toplevel()

                                #
                                fenetre_de_configuration_des_mises_a_jour.title("Configuration des mises à jour")

                                #
                                fenetre_de_configuration_des_mises_a_jour.resizable(False, False)

				#
				c = configuration_des_mises_a_jour.Configuration_des_mises_a_jour(fenetre_de_configuration_des_mises_a_jour, self.langue_uttilisee, 500, 700)

				#
                                fenetre_de_configuration_des_mises_a_jour.bind("<Destroy>", self.rendre_possible_l_ouverture_de_la_configuration_des_mises_a_jour)

                                #
                                fenetre_de_configuration_des_mises_a_jour.mainloop()

                        #
                        else:

                                #
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: Window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def rendre_possible_l_ouverture_de_la_configuration_des_mises_a_jour(self, event):

		#
		self.est_ouverte_boite_de_configuration_des_mises_a_jour = False

	#Cette fonction permet d'afficher l'heure et la date de la ville suivante (dans le tableau)
	def suivant(self):

		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

			#
			self.est_en_train_de_sonner_reveil = False

			#
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

		#
		else:

			#Si la variable self.est_ouverte_boite_d_insertion_des_villes est à False (donc, si la fenetre d'insertion de nouvelles villes n'est pas ouverte) alors...
                	if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#Si la somme de la valeur contenue dans incrementeur avec 1 est strictement supérieur au maximum de l'incrémenteur, alors...
				if self.incrementeur + 1 > self.maximum_de_l_incrementeur:

					#La valeur 0 est affectée à la variable incrementeur
					self.incrementeur = 0

				#Dans le cas contraire...
				else:

					#La valeur contenue dans la variable incrementeur correspond à la somme entre cette meme valeur et 1
					self.incrementeur = self.incrementeur + 1

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Next city: " + self.array_of_cities[self.incrementeur]

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Ville suivante: " + self.tableau_des_villes[self.incrementeur]

				#
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#Sinon...
			else:

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: A window is open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Une fenetre est ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#Cette fonction permet d'afficher l'heure et la date de la ville précédente (dans le tableau)
	def precedent(self):

		#Dans le cas ou la musique du reveil joue, alors...
		if self.est_en_train_de_sonner_reveil == True:

			#On arrete de la jouer
			self.sonnerie.stop()

			#
			self.est_en_train_de_sonner_reveil = False

			#
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

		#
		else:

			#Si la variable self.est_ouverte_boite_d_insertion_des_villes est à False (donc, si la fenetre d'insertion de nouvelles villes n'est pas ouverte) alors...
                	if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#Si la différence de la valeur contenue dans incrementeur avec 1 est strictement inférieur à 0, alors...
				if self.incrementeur - 1 < 0:

					#La valeur du maximum de l'incrementeur (valeur de la variable self.maximum_de_l_incrementeur) est affectée à la variable incrementeur
					self.incrementeur = self.maximum_de_l_incrementeur

				#Dans le cas contraire...
				else:

					#La valeur contenue dans la variable incrementeur correspond à la difference entre cette meme valeur et 1
					self.incrementeur = self.incrementeur - 1

				#
				if self.langue_uttilisee == 0:

					#
					texte_a_dire_par_eSpeak = "Previous city: " + self.array_of_cities[self.incrementeur]

				#
				else:

					#
					texte_a_dire_par_eSpeak = "Ville précédente: " + self.tableau_des_villes[self.incrementeur]

				#
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#Sinon...
                	else:

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: A window is open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Une fenetre est ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def choix_du_format_de_date(self):

		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

			#
			self.est_en_train_de_sonner_reveil = False

			#
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

                #Sinon...
                else:

			#Si la variable self.est_ouverte_boite_d_insertion_des_villes est à False (donc, si la fenetre d'insertion de nouvelles villes n'est pas ouverte) alors...
			if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#
				numero_du_format_de_date_choisi = self.format_de_date_selectionne.get()

				#
				self.format_de_date_uttilisee = numero_du_format_de_date_choisi

				#
                        	if self.langue_uttilisee == 0:

					#
					if self.format_de_date_uttilisee == 0:

                                		#
                                		texte_a_dire_par_eSpeak = "Date format in effect: Month Day Year"

					#
					elif self.format_de_date_uttilisee == 1:

						#
                                        	texte_a_dire_par_eSpeak = "Date format in effect: Day Month Year"

					#
					elif self.format_de_date_uttilisee == 2:

						#
						texte_a_dire_par_eSpeak = "Date format in effect: Year Month Day"

					#
					else:

						#
                                        	texte_a_dire_par_eSpeak = "Date format in effect: Year Day Month"

                        	#
                        	else:

                                	#
                                	if self.format_de_date_uttilisee == 0:

                                        	#
                                        	texte_a_dire_par_eSpeak = "Format de date en vigueur: Mois Jour Année"

                                	#
                                	elif self.format_de_date_uttilisee == 1:

                                        	#
                                        	texte_a_dire_par_eSpeak = "Format de date en vigueur: Jour Mois Année"

                                	#
                                	elif self.format_de_date_uttilisee == 2:

                                        	#
                                        	texte_a_dire_par_eSpeak = "Format de date en vigueur: Année Mois Jour"

                                	#
                                	else:

                                        	#
                                        	texte_a_dire_par_eSpeak = "Format de date en vigueur: Année Jour Mois"

                        	#
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#Sinon...
                	else:

				#
				self.format_de_date_selectionne.set(self.format_de_date_uttilisee)

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: A window is open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Une fenetre est ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#Définition d'une fonction choix_langue() qui met à jour l'heure pour afficher l'heure soit en format français, soit en format anglo-saxon
	def choix_de_la_langue(self):

		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

			#
			self.est_en_train_de_sonner_reveil = False

			#
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

		#Sinon...
		else:

			#Si la variable self.est_ouverte_boite_d_insertion_des_villes est à False (donc, si la fenetre d'insertion de nouvelles villes n'est pas ouverte) alors...
			if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#
				numero_de_la_langue_choisie = self.langue_selectionnee.get()

				#
				self.langue_uttilisee = numero_de_la_langue_choisie

				#
				if self.langue_uttilisee == 0:

					#
					self.identifiant_en_lettres_de_la_langue_uttilisee = 'en'

					#
					self.bouton_avant.config(text = "Next city")

					#
					self.bouton_arriere.config(text = "Previous city")

					#
					self.bouton_de_declenchement_de_la_commande_vocale.config(text = "Tap here, then talk")

					#
                                	self.menu_des_villes.entryconfig(0, label = "Inclusion of a new city")

                                	#
                                	self.menu_des_villes.entryconfig(1, label = "Deleting a city")

					#
					self.menu_du_reveil.entryconfig(0, label = "Alarm clock configuration")

					#
					self.menu_du_reveil.entryconfig(1, label = "Is activated")

					#
					self.menu_de_configuration_des_mises_a_jour.entryconfig(0, label = "Configuring the moment to update")

					#
					self.menu_de_la_meteo.entryconfig(0, label = "Weather data display")

					#
					self.menu_de_YouTube.entryconfig(0, label = "Playing singles downloaded from YouTube")

					#
					self.menu_de_YouTube.entryconfig(1, label = "Extraction and download of singles from YouTube")

					#
					self.menu_de_YouTube.entryconfig(2, label = "Deleting a single download from YouTube")

					#
					self.menu_d_aide.entryconfig(0, label = "Voice commands...")

					#
					self.menu_d_aide.entryconfig(1, label = "Showing the contents of the voice command log file...")

					#
					self.menu_d_aide.entryconfig(2, label = "Showing the contents of the updates log file...")

					#
					self.menu_d_aide.entryconfig(3, label = "About...")

					#
					self.texte_d_indication_du_demarrage_des_mises_a_jour_a_dire_par_eSpeak = "Now, updates will be made"

				#
				else:

					#
					self.identifiant_en_lettres_de_la_langue_uttilisee = 'fr'

					#
					self.bouton_avant.config(text = "Ville suivante")

					#
					self.bouton_arriere.config(text = "Ville précédente")

					#
                                	self.bouton_de_declenchement_de_la_commande_vocale.config(text = "Appuyez ici, puis parlez")

					#
					self.menu_des_villes.entryconfig(0, label = "Inclusion d'une nouvelle ville")

					#
					self.menu_des_villes.entryconfig(1, label = "Suppression d'une ville")

					#
                                	self.menu_du_reveil.entryconfig(0, label = "Configuration du réveil")

					#
					self.menu_du_reveil.entryconfig(1, label = "Est activé")

					#
					self.menu_de_configuration_des_mises_a_jour.entryconfig(0, label = "Configuration du moment pour effectuer les mises à jour")

					#
					self.menu_de_la_meteo.entryconfig(0, label = "Affichage des données météo")

					#
					self.menu_de_YouTube.entryconfig(0, label = "Lecture de singles téléchargés depuis YouTube")

					#
					self.menu_de_YouTube.entryconfig(1, label = "Extraction et téléchargement de singles depuis YouTube")

					#
					self.menu_de_YouTube.entryconfig(2, label = "Suppression d'un single télécharger depuis YouTube")

					#
					self.menu_d_aide.entryconfig(0, label = "Commandes vocales...")

					#
					self.menu_d_aide.entryconfig(1, label = "Affichage du contenu du fichier log de la commande vocale...")

					#
					self.menu_d_aide.entryconfig(2, label = "Affichage du contenu du fichier log des mises à jour...")

					#
                                        self.menu_d_aide.entryconfig(3, label = "A propos...")

					#
                                	self.texte_d_indication_du_demarrage_des_mises_a_jour_a_dire_par_eSpeak = "Maintenant, des mises à jour vont être effectués"

				#
                        	if self.langue_uttilisee == 0:

                         		#
                                	texte_a_dire_par_eSpeak = "Now, the current language is English."

                        	#
                        	else:

                                	#
                                	texte_a_dire_par_eSpeak = "Maintenant, la langue courante est le français"

                        	#
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#Sinon...
                	else:

				#
				self.langue_selectionnee.set(self.langue_uttilisee)

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: A window is open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Une fenetre est ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#Cette fonction permet de vérifier si le single à jouer est bien à jour depuis la derniére modification des paramétres du reveil, et dans le cas contraire il le met à jour
	def mise_a_jour_du_single_a_faire_jouer_pour_le_reveil(self):

		#Définition d'une variable chemin_d_accee_du_single_a_faire_jouer permettant d'éffectuer les opérations qui vont suivre...
		chemin_d_accee_du_single_a_faire_jouer = horloge_monde.renvoi_du_single_utilise_pour_le_reveil()

		#
		if not(self.single_utilise_pour_le_reveil == chemin_d_accee_du_single_a_faire_jouer):

			#Le chemin d'accee du single à faire jouer est affecté à la variable self.single_utilise_pour_le_reveil pour etre joué dès que le reveil sonne
			self.single_utilise_pour_le_reveil = chemin_d_accee_du_single_a_faire_jouer

	#
	def changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube(self):

		#
		if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

			#
			if self.frame_courant_de_lecteur_courant_de_fichiers_audio_telecharges_depuis_YouTube.est_stoppe == False:

				#
				self.frame_courant_de_lecteur_courant_de_fichiers_audio_telecharges_depuis_YouTube.lecture_ou_pause_de_la_musique()

	#
	def changement_de_l_etat_du_reveil_a_l_aide_de_la_commande_vocale(self, mot_cle_de_la_commande_vocale):

		#
		etat_actuel_du_reveil = horloge_monde.renvoi_de_l_etat_du_reveil()

		#
		if etat_actuel_du_reveil == 1 and (mot_cle_de_la_commande_vocale == "ACTIVATE" or mot_cle_de_la_commande_vocale == "ACTIVER"):

			#
                        if self.langue_uttilisee == 0:

                        	#
                                texte_a_dire_par_eSpeak = "Error: The alarm is already activated"

                        #
                        else:

                        	#
                                texte_a_dire_par_eSpeak = "Erreur: Le reveil est déjà activé"

                        #
                        horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

		#
		elif etat_actuel_du_reveil == 0 and (mot_cle_de_la_commande_vocale == "DISABLE" or mot_cle_de_la_commande_vocale == "DESACTIVER"):

			#
                        if self.langue_uttilisee == 0:

                                #
                                texte_a_dire_par_eSpeak = "Error: The alarm is already disable"

                        #
                        else:

                                #
                                texte_a_dire_par_eSpeak = "Erreur: Le reveil est déjà désactivé"

                        #
                        horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

		#
		else:

			#
			if mot_cle_de_la_commande_vocale == "DESACTIVER" or mot_cle_de_la_commande_vocale == "DISABLE":

				#
				horloge_monde.changement_d_etat_du_reveil(0, self.langue_uttilisee, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#
			else:

				#
                                horloge_monde.changement_d_etat_du_reveil(1, self.langue_uttilisee, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#
                        self.etat_du_reveil = horloge_monde.renvoi_de_l_etat_du_reveil()

                        #
                        self.est_active_reveil.set(self.etat_du_reveil)

	#Cette fonction permet l'activation ou la désactivation de la fonctionnalité révéil grâce à la checkbox du menu menu_du_reveil
	def changement_de_l_etat_du_reveil_a_l_aide_de_la_case_a_cocher(self):

		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

                        #
                        self.est_en_train_de_sonner_reveil = False

                        #
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

		#
		else:

			#Si la variable self.est_ouverte_boite_d_insertion_des_villes est à False (donc, si la fenetre d'insertion de nouvelles villes n'est pas ouverte) alors...
			if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#
				if self.est_active_reveil.get() == True:

					#
					horloge_monde.changement_d_etat_du_reveil(1, self.langue_uttilisee, self.identifiant_en_lettres_de_la_langue_uttilisee)

				#Sinon...
				else:

					#
					horloge_monde.changement_d_etat_du_reveil(0, self.langue_uttilisee, self.identifiant_en_lettres_de_la_langue_uttilisee)

				#
				self.etat_du_reveil = horloge_monde.renvoi_de_l_etat_du_reveil()

				#
				self.est_active_reveil.set(self.etat_du_reveil)

			#Sinon...
			else:

				#
				self.est_active_reveil.set(self.etat_du_reveil)

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: A window is open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Une fenetre est ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#Définition de la fonction tick() qui met à jour l'heure pour un fuseau horaire donné
	def tick(self):

		 #
		 self.mise_a_jour_du_single_a_faire_jouer_pour_le_reveil()

		 #
		 time2 = horloge_monde.retour_de_la_date_et_de_l_heure_passee_en_parametre_sous_forme_de_timestamp(self.incrementeur + 1)

    		 # if time string has changed, update it
    		 if time2 != self.time1:

			#La valeur contenue dans la variable time2
        	 	self.time1 = time2

			#
			time2_str = horloge_monde.retour_de_la_date_et_de_l_heure_sous_forme_de_string(self.incrementeur + 1, self.langue_uttilisee, self.format_de_date_uttilisee)

			#Et le label afficheur affiche l'heure au format demandé
        	 	self.afficheur.config(text=time2_str)

		 #Dans le cas ou la fonction reveil du module horloge_monde renvoie True (donc, que c'est le moment de déclencher le reveil)
		 if horloge_monde.reveil() == True:

			#
                        self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

			#
			self.sonnerie = pygame.mixer.Sound(self.single_utilise_pour_le_reveil)

			#Le son défini dans le constructeur  de la classe Horloge est joué
			self.sonnerie.play()

			#
			self.est_en_train_de_sonner_reveil = True

			#Le programme se met en pause durant 1 seconde
			time.sleep(1)

		 #
		 if horloge_monde.mise_a_jour() == True:

			#
			horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#
			horloge_monde.mise_a_jour_des_modules_python_necessaires_pour_le_reveil()

    		 #La fonction s'appelle elle-meme toute les 200 milisecondes pour se mettre à jour
		 self.afficheur.after(200, self.tick)

	#
	def expression_des_donnees_concernant_le_single_enregistre_pour_le_reveil(self):

		#
		tableau_des_donnees_concernant_le_single_enregistre_pour_le_reveil = horloge_monde.renvoi_des_donnees_concernant_le_single_enregistre_pour_le_reveil(self.langue_uttilisee)

		#
		if self.langue_uttilisee == 0:

			#
			texte_a_dire_par_eSpeak = "The musical single defined for the alarm clock is {} by {} and originally from {}".format(tableau_des_donnees_concernant_le_single_enregistre_pour_le_reveil[0], tableau_des_donnees_concernant_le_single_enregistre_pour_le_reveil[1], tableau_des_donnees_concernant_le_single_enregistre_pour_le_reveil[2])

		#
		else:

			#
			texte_a_dire_par_eSpeak = "Le single musical défini pour le réveil est {} par {} et originaire de {}".format(tableau_des_donnees_concernant_le_single_enregistre_pour_le_reveil[0], tableau_des_donnees_concernant_le_single_enregistre_pour_le_reveil[1], tableau_des_donnees_concernant_le_single_enregistre_pour_le_reveil[2])

		#
		horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def expression_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil(self):

		#
		tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil = horloge_monde.renvoi_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil(self.langue_uttilisee)

		#
		if self.langue_uttilisee == 0:

			#
			texte_a_dire_par_eSpeak = "The alarm is set to ring {} hours {} minutes and {} seconds {} time in the country named {} {}".format(tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil[0], tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil[1], tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil[2], tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil[3], tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil[5], tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil[4])

		#
		else:

			#
			texte_a_dire_par_eSpeak = "Le reveil est paramétré pour sonner à {} heures {} minutes et {} secondes heure de {} dans le pays nommé {} {}".format(tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil[0], tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil[1], tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil[2], tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil[3], tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil[5], tableau_des_donnees_concernant_l_heure_la_frequence_et_la_ville_parametrees_pour_faire_sonner_le_reveil[4])

		#
		horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def expression_de_l_heure_et_de_la_date_par_commande_vocale(self, tableau_des_elements_demandes):

		#
		texte_a_dire_par_eSpeak = ""

		#
		tz_correspondant_a_la_ville_courante = horloge_monde.renvoi_du_timezone_correspondant_a_l_id_de_la_ville_passe_en_parametre(self.incrementeur + 1)

		#
		nom_de_la_ville_courante_dans_la_langue_courante = horloge_monde.renvoi_du_nom_de_la_ville_courante_dans_le_language_passe_en_parametre(self.incrementeur + 1, self.langue_uttilisee)

		#
		nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante = horloge_monde.renvoi_du_nom_du_pays_correspondant_a_l_id_de_la_ville_passe_en_parametre(self.incrementeur + 1, self.langue_uttilisee)

		#
                horaire_courant_dans_la_ville_courante = horloge_monde.renvoi_de_la_date_et_de_l_heure(tz_correspondant_a_la_ville_courante)

		#Définition des deux tableaux pour les jours de la semaine, tant en français qu'en anglais
        	jour_de_la_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        	days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        	#Définition des deux tableaux pour les mois de l'année, tant en français qu'en anglais
        	mois_de_l_annee = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
        	months_in_the_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

		#
		if self.langue_uttilisee == 0:

			#
			if len(tableau_des_elements_demandes) == 1:

				#
				if tableau_des_elements_demandes[0] == "TIME":

					#
					heure_a_faire_dire_a_eSpeak = str(horaire_courant_dans_la_ville_courante.hour % 12)

					#
					minute_a_faire_dire_a_eSpeak = str(horaire_courant_dans_la_ville_courante.minute)

					#
					seconde_a_faire_dire_a_eSpeak = str(horaire_courant_dans_la_ville_courante.second)

					#
					if horaire_courant_dans_la_ville_courante.hour < 13:

						#
						identificateur_du_moment_de_la_journee = "AM"

					#
					else:

						#
						identificateur_du_moment_de_la_journee = "PM"

					#
					texte_a_dire_par_eSpeak = "It is " + heure_a_faire_dire_a_eSpeak + " hours " + minute_a_faire_dire_a_eSpeak + " minutes and " + seconde_a_faire_dire_a_eSpeak + " seconds " + identificateur_du_moment_de_la_journee + " in " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

				#
				else:

					#
                			jour_courant_dans_la_semaine = days_of_the_week[horaire_courant_dans_la_ville_courante.weekday()]

                			#
                			mois_courant_dans_l_annee = months_in_the_year[horaire_courant_dans_la_ville_courante.month - 1]

					#
					jour = str(horaire_courant_dans_la_ville_courante.day)

					#
        				if self.format_de_date_uttilisee == 0:

                				#
                				texte_a_dire_par_eSpeak = "It is " + jour_courant_dans_la_semaine + " " + mois_courant_dans_l_annee + " " + jour + " " + str(horaire_courant_dans_la_ville_courante.year) + " in " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

        				#
        				elif self.format_de_date_uttilisee == 1:

                				#
                				texte_a_dire_par_eSpeak = "It is " + jour_courant_dans_la_semaine + " " + jour + " " + mois_courant_dans_l_annee + " " + str(horaire_courant_dans_la_ville_courante.year) + " in " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

        				#
        				elif self.format_de_date_uttilisee == 2:

                				#
                				texte_a_dire_par_eSpeak = "It is " + jour_courant_dans_la_semaine + " " + str(horaire_courant_dans_la_ville_courante.year) + " " + mois_courant_dans_l_annee + " " + jour + " in " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

        				#
        				else:

                				#
                				texte_a_dire_par_eSpeak = "It is " + jour_courant_dans_la_semaine + " " + str(horaire_courant_dans_la_ville_courante.year) + " " + jour + " " + mois_courant_dans_l_annee + " in " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

			#
			else:

				#
                		jour_courant_dans_la_semaine = days_of_the_week[horaire_courant_dans_la_ville_courante.weekday()]

                		#
                		mois_courant_dans_l_annee = months_in_the_year[horaire_courant_dans_la_ville_courante.month - 1]

				#
				jour = str(horaire_courant_dans_la_ville_courante.day)

				#
				heure_a_faire_dire_a_eSpeak = str(horaire_courant_dans_la_ville_courante.hour % 12)

				#
				minute_a_faire_dire_a_eSpeak = str(horaire_courant_dans_la_ville_courante.minute)

				#
				seconde_a_faire_dire_a_eSpeak = str(horaire_courant_dans_la_ville_courante.second)

				#
				if horaire_courant_dans_la_ville_courante.hour < 13:

					#
					identificateur_du_moment_de_la_journee = "AM"

				#
				else:

					#
					identificateur_du_moment_de_la_journee = "PM"

				#
        			if self.format_de_date_uttilisee == 0:

                			#
                			texte_a_dire_par_eSpeak = "It is " + heure_a_faire_dire_a_eSpeak + " hours " + minute_a_faire_dire_a_eSpeak + " minutes and " + seconde_a_faire_dire_a_eSpeak + " seconds " + identificateur_du_moment_de_la_journee + " on " + jour_courant_dans_la_semaine + " " + mois_courant_dans_l_annee + " " + jour + " " + str(horaire_courant_dans_la_ville_courante.year) + " in " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

        			#
        			elif self.format_de_date_uttilisee == 1:

                			#
                			texte_a_dire_par_eSpeak = "It is " + heure_a_faire_dire_a_eSpeak + " hours " + minute_a_faire_dire_a_eSpeak + " minutes and " + seconde_a_faire_dire_a_eSpeak + " seconds " + identificateur_du_moment_de_la_journee + " on " + jour_courant_dans_la_semaine + " " + jour + " " + mois_courant_dans_l_annee + " " + str(horaire_courant_dans_la_ville_courante.year) + " in " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

        			#
        			elif self.format_de_date_uttilisee == 2:

                			#
                			texte_a_dire_par_eSpeak = "It is " + heure_a_faire_dire_a_eSpeak + " hours " + minute_a_faire_dire_a_eSpeak + " minutes and " + seconde_a_faire_dire_a_eSpeak + " seconds " + identificateur_du_moment_de_la_journee + " on " + jour_courant_dans_la_semaine + " " + str(horaire_courant_dans_la_ville_courante.year) + " " + mois_courant_dans_l_annee + " " + jour + " in " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

        			#
        			else:

                			#
                			texte_a_dire_par_eSpeak = "It is " + heure_a_faire_dire_a_eSpeak + " hours " + minute_a_faire_dire_a_eSpeak + " minutes and " + seconde_a_faire_dire_a_eSpeak + " seconds " + identificateur_du_moment_de_la_journee + " on " + jour_courant_dans_la_semaine + " " + str(horaire_courant_dans_la_ville_courante.year) + " " + jour + " " + mois_courant_dans_l_annee + " in " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

		#
		else:

			#
			if len(tableau_des_elements_demandes) == 1:

				#
				if tableau_des_elements_demandes[0] == "HEURE":

					#
					heure_a_faire_dire_a_eSpeak = str(horaire_courant_dans_la_ville_courante.hour)

					#
					minute_a_faire_dire_a_eSpeak = str(horaire_courant_dans_la_ville_courante.minute)

					#
					seconde_a_faire_dire_a_eSpeak = str(horaire_courant_dans_la_ville_courante.second)

					#
					if horaire_courant_dans_la_ville_courante.hour < 13:

						#
						identificateur_du_moment_de_la_journee = "AM"

					#
					else:

						#
						identificateur_du_moment_de_la_journee = "PM"

					#
					texte_a_dire_par_eSpeak = "Il est " + heure_a_faire_dire_a_eSpeak + " heures " + minute_a_faire_dire_a_eSpeak + " minutes et " + seconde_a_faire_dire_a_eSpeak + " secondes " + identificateur_du_moment_de_la_journee + " à " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

				#
				else:

					#
                			jour_courant_dans_la_semaine = jour_de_la_semaine[horaire_courant_dans_la_ville_courante.weekday()]

                			#
                			mois_courant_dans_l_annee = mois_de_l_annee[horaire_courant_dans_la_ville_courante.month - 1]

					#
					jour = str(horaire_courant_dans_la_ville_courante.day)

					#
        				if self.format_de_date_uttilisee == 0:

                				#
                				texte_a_dire_par_eSpeak = "On est " + jour_courant_dans_la_semaine + " " + mois_courant_dans_l_annee + " " + jour + " " + str(horaire_courant_dans_la_ville_courante.year) + " à " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

        				#
        				elif self.format_de_date_uttilisee == 1:

                				#
                				texte_a_dire_par_eSpeak = "On est " + jour_courant_dans_la_semaine + " " + jour + " " + mois_courant_dans_l_annee + " " + str(horaire_courant_dans_la_ville_courante.year) + " à " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

        				#
        				elif self.format_de_date_uttilisee == 2:

                				#
                				texte_a_dire_par_eSpeak = "On est " + jour_courant_dans_la_semaine + " " + str(horaire_courant_dans_la_ville_courante.year) + " " + mois_courant_dans_l_annee + " " + jour + " à " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

        				#
        				else:

                				#
                				texte_a_dire_par_eSpeak = "On est " + jour_courant_dans_la_semaine + " " + str(horaire_courant_dans_la_ville_courante.year) + " " + jour + " " + mois_courant_dans_l_annee + " à " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

			#
			else:

				#
                		jour_courant_dans_la_semaine = jour_de_la_semaine[horaire_courant_dans_la_ville_courante.weekday()]

                		#
                		mois_courant_dans_l_annee = mois_de_l_annee[horaire_courant_dans_la_ville_courante.month - 1]

				#
				jour = str(horaire_courant_dans_la_ville_courante.day)

				#
				heure_a_faire_dire_a_eSpeak = str(horaire_courant_dans_la_ville_courante.hour)

				#
				minute_a_faire_dire_a_eSpeak = str(horaire_courant_dans_la_ville_courante.minute)

				#
				seconde_a_faire_dire_a_eSpeak = str(horaire_courant_dans_la_ville_courante.second)

				#
        			if self.format_de_date_uttilisee == 0:

                			#
                			texte_a_dire_par_eSpeak = "On est " + heure_a_faire_dire_a_eSpeak + " heures " + minute_a_faire_dire_a_eSpeak + " minutes et " + seconde_a_faire_dire_a_eSpeak + " secondes " + " le " + jour_courant_dans_la_semaine + " " + mois_courant_dans_l_annee + " " + jour + " " + str(horaire_courant_dans_la_ville_courante.year) + " à " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

        			#
        			elif self.format_de_date_uttilisee == 1:

                			#
                			texte_a_dire_par_eSpeak = "On est " + heure_a_faire_dire_a_eSpeak + " heures " + minute_a_faire_dire_a_eSpeak + " minutes et " + seconde_a_faire_dire_a_eSpeak + " secondes " + " le " + jour_courant_dans_la_semaine + " " + jour + " " + mois_courant_dans_l_annee + " " + str(horaire_courant_dans_la_ville_courante.year) + " à " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

        			#
        			elif self.format_de_date_uttilisee == 2:

                			#
                			texte_a_dire_par_eSpeak = "On est " + heure_a_faire_dire_a_eSpeak + " heures " + minute_a_faire_dire_a_eSpeak + " minutes et " + seconde_a_faire_dire_a_eSpeak + " secondes " + " le " + jour_courant_dans_la_semaine + " " + str(horaire_courant_dans_la_ville_courante.year) + " " + mois_courant_dans_l_annee + " " + jour + " à " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

        			#
        			else:

                			#
                			texte_a_dire_par_eSpeak = "On est " + heure_a_faire_dire_a_eSpeak + " heures " + minute_a_faire_dire_a_eSpeak + " minutes et " + seconde_a_faire_dire_a_eSpeak + " secondes " + " le " + jour_courant_dans_la_semaine + " " + str(horaire_courant_dans_la_ville_courante.year) + " " + jour + " " + mois_courant_dans_l_annee + " à " + nom_de_la_ville_courante_dans_la_langue_courante + "(" + nom_du_pays_dans_lequel_se_situe_la_ville_courante_dans_la_langue_courante + ")"

		#
		horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

	#
	def appel_de_la_commande_vocale(self, tableau_de_la_commande_vocale_de_l_uttilisateur):

		#
                if self.langue_uttilisee == 0:

			#
			if horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CONFIGURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("FRENCH",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.langue_selectionnee.set(1)

				#
				self.langue_uttilisee = 1

				#
                                self.identifiant_en_lettres_de_la_langue_uttilisee = 'fr'

                                #
                                self.bouton_avant.config(text = "Ville suivante")

                                #
                                self.bouton_arriere.config(text = "Ville précédente")

                                #
                                self.bouton_de_declenchement_de_la_commande_vocale.config(text = "Appuyez ici, puis parlez")

                                #
                                self.menu_des_villes.entryconfig(0, label = "Inclusion d'une nouvelle ville")

                                #
                               	self.menu_des_villes.entryconfig(1, label = "Suppression d'une ville")

                                #
                                self.menu_du_reveil.entryconfig(0, label = "Configuration du réveil")

                                #
                                self.menu_de_la_meteo.entryconfig(0, label = "Affichage des données météo")

				#
                                self.menu_de_configuration_des_mises_a_jour.entryconfig(0, label = "Configuration du moment pour effectuer les mises à jour")

				#
                                self.menu_du_reveil.entryconfig(1, label = "Est activé")

                                #
                                self.menu_de_YouTube.entryconfig(0, label = "Lecture de singles téléchargés depuis YouTube")

                                #
                                self.menu_de_YouTube.entryconfig(1, label = "Extraction et téléchargement de singles depuis YouTube")

                                #
                                self.menu_de_YouTube.entryconfig(2, label = "Suppression d'un single télécharger depuis YouTube")

				#
				self.menu_d_aide.entryconfig(0, label = "Commandes vocales...")

				#
                                self.menu_d_aide.entryconfig(1, label = "Affichage du contenu du fichier log de la commande vocale...")

				#
				self.menu_d_aide.entryconfig(2, label = "Affichage du contenu du fichier des mises à jour...")

				#
                                self.menu_d_aide.entryconfig(3, label = "A propos...")

				#
                                texte_a_dire_par_eSpeak = "Maintenant, la langue courante est le français"

                        	#
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CONFIGURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CELSIUS",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.unite_de_mesure_selectionnee_pour_la_temperature.set(0)

				#
				self.unite_de_mesure_de_la_temperature = 0

                                #
                                texte_a_dire_par_eSpeak = "Now, temperature in celsius."

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CONFIGURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("FAHRENHEIT",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.unite_de_mesure_selectionnee_pour_la_temperature.set(1)

                                #
                                self.unite_de_mesure_de_la_temperature = 1

                                #
                                texte_a_dire_par_eSpeak = "Now, temperature in fahrenheit."

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("SHOW",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("WEATHER",tableau_de_la_commande_vocale_de_l_uttilisateur):

                        	#
                                self.affichage_des_donnees_meteo_de_la_ville_courante()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("TEMPERATURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("MAXIMUM",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CITY",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				horloge_monde.expression_de_donnees_meteo_par_la_commande_vocale(["TEMPERATURE","MAXIMUM"], self.incrementeur + 1, self.cle_de_l_API_pour_uttilisation_des_fonctionnalites_d_OpenWeather, self.unite_de_mesure_de_la_temperature, self.langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("TEMPERATURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("MINIMUM",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CITY",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				horloge_monde.expression_de_donnees_meteo_par_la_commande_vocale(["TEMPERATURE","MINIMUM"], self.incrementeur + 1, self.cle_de_l_API_pour_uttilisation_des_fonctionnalites_d_OpenWeather, self.unite_de_mesure_de_la_temperature, self.langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("TEMPERATURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CITY",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				horloge_monde.expression_de_donnees_meteo_par_la_commande_vocale(["TEMPERATURE"], self.incrementeur + 1, self.cle_de_l_API_pour_uttilisation_des_fonctionnalites_d_OpenWeather, self.unite_de_mesure_de_la_temperature, self.langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("SUNRISE",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				horloge_monde.expression_de_donnees_meteo_par_la_commande_vocale(["SUNRISE"], self.incrementeur + 1, self.cle_de_l_API_pour_uttilisation_des_fonctionnalites_d_OpenWeather, self.unite_de_mesure_de_la_temperature, self.langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("SUNSET",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				horloge_monde.expression_de_donnees_meteo_par_la_commande_vocale(["SUNSET"], self.incrementeur + 1, self.cle_de_l_API_pour_uttilisation_des_fonctionnalites_d_OpenWeather, self.unite_de_mesure_de_la_temperature, self.langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("SETTINGS",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("ALARM",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.expression_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("SINGLE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("ALARM",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.expression_des_donnees_concernant_le_single_enregistre_pour_le_reveil()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CONFIGURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("ALARM",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.configuration_du_reveil()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("INCLUDE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CITY",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.insertion_d_une_nouvelle_ville()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CONSULT",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("LOG",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("VOICE",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.affichage_du_contenu_du_fichier_de_log_de_la_commande_vocale_dans_une_fenetre()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CONSULT",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("LOG",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("UPDATES",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.affichage_du_contenu_du_fichier_de_log_des_mises_a_jour_dans_une_fenetre()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("REMOVE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CITY",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.suppression_d_une_ville()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("READER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("YOUTUBE",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.lecture_de_fichiers_audio_telecharges_depuis_YouTube()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("INCLUDE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("YOUTUBE",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.telechargement_et_extraction_d_un_single_depuis_YouTube()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("NEXT",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CITY",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.suivant()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("PREVIOUS",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CITY",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.precedent()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("SHOW",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.verification_d_une_correspondance_avec_le_nom_d_une_ville_inscrite_dans_la_base(tableau_de_la_commande_vocale_de_l_uttilisateur[1], self.langue_uttilisee) == True:

				#
				self.incrementeur = horloge_monde.renvoi_de_l_id_d_une_ville_a_partir_de_son_nom(tableau_de_la_commande_vocale_de_l_uttilisateur[1], self.langue_uttilisee) - 1

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("SHOW",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("ABOUT",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.affichage_des_informations_sur_le_reveil_intelligent_et_connecte()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("ACTIVATE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("ALARM",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.changement_de_l_etat_du_reveil_a_l_aide_de_la_commande_vocale("ACTIVATE")

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("DISABLE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("ALARM",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.changement_de_l_etat_du_reveil_a_l_aide_de_la_commande_vocale("DISABLE")

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("WHAT",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("IS",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("DATE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("TIME",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.expression_de_l_heure_et_de_la_date_par_commande_vocale(["TIME", "DATE"])

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("WHAT",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("TIME",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("IS",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.expression_de_l_heure_et_de_la_date_par_commande_vocale(["TIME"])

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("WHAT",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("DATE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("IS",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.expression_de_l_heure_et_de_la_date_par_commande_vocale(["DATE"])

                #
                else:

			#
			if horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CONFIGURER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("ANGLAIS",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.langue_selectionnee.set(0)

				#
                                self.langue_uttilisee = 0

				#
                                self.identifiant_en_lettres_de_la_langue_uttilisee = 'en'

                                #
                                self.bouton_avant.config(text = "Next city")

                                #
                                self.bouton_arriere.config(text = "Previous city")

                                #
                                self.bouton_de_declenchement_de_la_commande_vocale.config(text = "Tap here, then talk")

                                #
                                self.menu_des_villes.entryconfig(0, label = "Inclusion of a new city")

                                #
                                self.menu_des_villes.entryconfig(1, label = "Deleting a city")

				#
                                self.menu_du_reveil.entryconfig(1, label = "Is activated")

                                #
                                self.menu_du_reveil.entryconfig(0, label = "Alarm clock configuration")

				#
                                self.menu_de_configuration_des_mises_a_jour.entryconfig(0, label = "Configuring the moment to update")

                                #
                                self.menu_de_la_meteo.entryconfig(0, label = "Weather data display")

                                #
                                self.menu_de_YouTube.entryconfig(0, label = "Playing singles downloaded from YouTube")

                                #
                                self.menu_de_YouTube.entryconfig(1, label = "Extraction and download of singles from YouTube")

				#
				self.menu_de_YouTube.entryconfig(2, label = "Deleting a single download from YouTube")

				#
				self.menu_d_aide.entryconfig(0, label = "Voice commands...")

				#
                                self.menu_d_aide.entryconfig(1, label = "Showing the contents of the voice command log file...")

				#
				self.menu_d_aide.entryconfig(2, label = "Showing the contents of the updates log file...")

				#
				self.menu_d_aide.entryconfig(3, label = "About...")

				#
				texte_a_dire_par_eSpeak = "Now, the current language is English."

				#
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CONFIGURER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CELSIUS",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.unite_de_mesure_selectionnee_pour_la_temperature.set(0)

                                #
                                self.unite_de_mesure_de_la_temperature = 0

				#
                                texte_a_dire_par_eSpeak = "Maintenant, température en celsius"

                        	#
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CONFIGURER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("FAHRENHEIT",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.unite_de_mesure_selectionnee_pour_la_temperature.set(1)

                                #
                                self.unite_de_mesure_de_la_temperature = 1

				#
                                texte_a_dire_par_eSpeak = "Maintenant, température en fahrenheit."

                        	#
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("AFFICHER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("METEO",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.affichage_des_donnees_meteo_de_la_ville_courante()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("SINGLE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("REVEIL",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.expression_des_donnees_concernant_le_single_enregistre_pour_le_reveil()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("TEMPERATURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("MAXIMALE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("VILLE",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				horloge_monde.expression_de_donnees_meteo_par_la_commande_vocale(["TEMPERATURE","MAXIMALE"], self.incrementeur + 1, self.cle_de_l_API_pour_uttilisation_des_fonctionnalites_d_OpenWeather, self.unite_de_mesure_de_la_temperature, self.langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("TEMPERATURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("MINIMALE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("VILLE",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				horloge_monde.expression_de_donnees_meteo_par_la_commande_vocale(["TEMPERATURE","MINIMALE"], self.incrementeur + 1, self.cle_de_l_API_pour_uttilisation_des_fonctionnalites_d_OpenWeather, self.unite_de_mesure_de_la_temperature, self.langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("TEMPERATURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("VILLE",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				horloge_monde.expression_de_donnees_meteo_par_la_commande_vocale(["TEMPERATURE"], self.incrementeur + 1, self.cle_de_l_API_pour_uttilisation_des_fonctionnalites_d_OpenWeather, self.unite_de_mesure_de_la_temperature, self.langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("COUCHER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("SOLEIL",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				horloge_monde.expression_de_donnees_meteo_par_la_commande_vocale(["COUCHER"], self.incrementeur + 1, self.cle_de_l_API_pour_uttilisation_des_fonctionnalites_d_OpenWeather, self.unite_de_mesure_de_la_temperature, self.langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("LEVER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("SOLEIL",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				horloge_monde.expression_de_donnees_meteo_par_la_commande_vocale(["LEVER"], self.incrementeur + 1, self.cle_de_l_API_pour_uttilisation_des_fonctionnalites_d_OpenWeather, self.unite_de_mesure_de_la_temperature, self.langue_uttilisee)

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CONFIGURER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("REVEIL",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.configuration_du_reveil()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("INCLURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("VILLE",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.insertion_d_une_nouvelle_ville()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("SUPPRIMER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("VILLE",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.suppression_d_une_ville()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CONSULTER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("LOG",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("VOIX",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.affichage_du_contenu_du_fichier_de_log_de_la_commande_vocale_dans_une_fenetre()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("CONSULTER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("LOG",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("MAJ",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.affichage_du_contenu_du_fichier_de_log_des_mises_a_jour_dans_une_fenetre()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("REVEIL",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("PARAMETRES",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.expression_de_l_heure_de_la_frequence_et_de_la_ville_parametrees_pour_faire_sonner_le_reveil()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("LECTEUR",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("YOUTUBE",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
				self.lecture_de_fichiers_audio_telecharges_depuis_YouTube()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("INCLURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("YOUTUBE",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
				self.telechargement_et_extraction_d_un_single_depuis_YouTube()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("VILLE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("SUIVANT",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.suivant()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("VILLE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("PRECEDENT",tableau_de_la_commande_vocale_de_l_uttilisateur):

                                #
                                self.precedent()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("AFFICHER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.verification_d_une_correspondance_avec_le_nom_d_une_ville_inscrite_dans_la_base(tableau_de_la_commande_vocale_de_l_uttilisateur[1], self.langue_uttilisee) == True:

				#
				self.incrementeur = horloge_monde.renvoi_de_l_id_d_une_ville_a_partir_de_son_nom(tableau_de_la_commande_vocale_de_l_uttilisateur[1], self.langue_uttilisee) - 1

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("AFFICHER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("PROPOS",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.affichage_des_informations_sur_le_reveil_intelligent_et_connecte()

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("ACTIVER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("REVEIL",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.changement_de_l_etat_du_reveil_a_l_aide_de_la_commande_vocale("ACTIVER")

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("DESACTIVER",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("REVEIL",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.changement_de_l_etat_du_reveil_a_l_aide_de_la_commande_vocale("DESACTIVER")

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("QUELLE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("EST",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("DATE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("HEURE",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.expression_de_l_heure_et_de_la_date_par_commande_vocale(["HEURE", "DATE"])

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("QUELLE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("HEURE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("EST",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.expression_de_l_heure_et_de_la_date_par_commande_vocale(["HEURE"])

			#
			elif horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("QUELLE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("DATE",tableau_de_la_commande_vocale_de_l_uttilisateur) and horloge_monde.contient_l_element_passe_en_parametre_dans_le_tableau_passe_en_parametre("EST",tableau_de_la_commande_vocale_de_l_uttilisateur):

				#
				self.expression_de_l_heure_et_de_la_date_par_commande_vocale(["DATE"])

	#
	def commande_vocale_du_reveil(self):

		#Dans le cas ou la musique du reveil joue, alors...
                if self.est_en_train_de_sonner_reveil == True:

                        #On arrete de la jouer
                        self.sonnerie.stop()

                        #
                        self.est_en_train_de_sonner_reveil = False

                        #
                        if self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == True:

                                #
                                self.changement_d_etat_du_lecteur_de_fichiers_audio_telecharges_depuis_YouTube()

                #
                else:

			#Si la variable self.est_ouverte_boite_d_insertion_des_villes est à False (donc, si la fenetre d'insertion de nouvelles villes n'est pas ouverte) alors...
			if self.est_ouverte_boite_d_insertion_des_villes == False and self.est_ouverte_boite_de_configuration_du_reveil == False and self.est_ouverte_boite_de_suppression_des_villes == False and self.est_ouverte_boite_d_affichage_des_donnees_meteo == False and self.est_ouverte_boite_de_lecture_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_d_extraction_et_de_telechargement_depuis_YouTube == False and self.est_ouverte_boite_de_suppression_de_fichiers_audio_telecharges_depuis_YouTube == False and self.est_ouverte_boite_de_configuration_des_mises_a_jour == False and self.est_ouverte_boite_d_affichage_des_informations_sur_le_reveil == False and self.est_ouverte_boite_d_affichage_des_commandes_vocales == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False and self.est_ouverte_boite_de_consultation_des_logs_de_la_commande_vocale == False and self.est_ouverte_boite_de_consultation_des_logs_des_mises_a_jour == False:

				#
				enregistreur_de_la_commande_vocale_de_l_uttilisateur = speech_recognition.Recognizer()

				#
				with speech_recognition.Microphone() as source:

					#
					enregistrement_audio_de_la_commande_vocale_de_l_uttilisateur = enregistreur_de_la_commande_vocale_de_l_uttilisateur.listen(source)

					#
					try:

						#
						if self.langue_uttilisee == 0:

							#
							variable_du_resultat_de_la_conversion_d_audio_a_texte = enregistreur_de_la_commande_vocale_de_l_uttilisateur.recognize_google(enregistrement_audio_de_la_commande_vocale_de_l_uttilisateur, language = "en-US")

						#
						else:

							#
							variable_du_resultat_de_la_conversion_d_audio_a_texte = enregistreur_de_la_commande_vocale_de_l_uttilisateur.recognize_google(enregistrement_audio_de_la_commande_vocale_de_l_uttilisateur, language = "fr-FR")

						#
						tableau_de_la_commande_vocale_de_l_uttilisateur = horloge_monde.filtre_de_la_commande_vocale_de_l_uttilisateur(variable_du_resultat_de_la_conversion_d_audio_a_texte, self.langue_uttilisee)

						#
						heure_et_date_du_systeme = time.strftime("%a %d %b %Y - %H:%M:%S")

						#
						descripteur_du_fichier_de_logs_pour_la_commande_vocale = os.open("logs/logs_commande_vocale", os.O_WRONLY | os.O_CREAT | os.O_APPEND)

						#
						os.write(descripteur_du_fichier_de_logs_pour_la_commande_vocale, "{heure_et_date} - {commande_passee}".format(heure_et_date = heure_et_date_du_systeme, commande_passee = variable_du_resultat_de_la_conversion_d_audio_a_texte))

						#
						os.write(descripteur_du_fichier_de_logs_pour_la_commande_vocale, "\n")

						#
						os.close(descripteur_du_fichier_de_logs_pour_la_commande_vocale)

						#
						self.appel_de_la_commande_vocale(tableau_de_la_commande_vocale_de_l_uttilisateur)

					#
					except speech_recognition.UnknownValueError:

						#
						if self.langue_uttilisee == 0:

							#
							texte_a_dire_par_eSpeak_en_cas_d_erreur = "Sorry, impossible to understand you"

						#
						else:

							#
							texte_a_dire_par_eSpeak_en_cas_d_erreur = "Désolé, impossible de vous comprendre"

						#
						horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

					#
					except speech_recognition.RequestError as e:

						#
						if self.langue_uttilisee == 0:

                                			#
                                			texte_a_dire_par_eSpeak_en_cas_d_erreur = "Sorry, could not request results from Google Speech Recognition Service"

                        			#
                        			else:

                                			#
                                			texte_a_dire_par_eSpeak_en_cas_d_erreur = "Désolé, impossible de demander les résultats du service de reconnaissance vocale de Google"

                        			#
						horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak_en_cas_d_erreur, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#Sinon...
                	else:

				#
                                if self.langue_uttilisee == 0:

                                        #
                                        texte_a_dire_par_eSpeak = "Error: Window already open"

                                #
                                else:

                                        #
                                        texte_a_dire_par_eSpeak = "Erreur: Fenetre déjà ouverte"

                                #
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(texte_a_dire_par_eSpeak, self.identifiant_en_lettres_de_la_langue_uttilisee)

#Cette fonction (qui sera appellée pour faire tourner l'horloge
def initialisation_et_affichage_de_l_horloge():

	#
        fenetre = Tk()

        #
        fenetre.title("Horloge - Monde")

	#
	fenetre.resizable(False, False)

        #
        horloge = Horloge(fenetre, "Hologe - Monde", fenetre.winfo_screenwidth(), fenetre.winfo_screenheight())

        #
        horloge.tick()

        #
        horloge.mainloop()

#Bloc de test du module
if __name__ == '__main__':

	#
	initialisation_et_affichage_de_l_horloge()
