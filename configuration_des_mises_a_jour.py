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

#Cette classe permet de définir une interface graphique pour configurer les mises à jour
class Configuration_des_mises_a_jour(Frame):

        #Définition du constructeur de la classe Configuration_des_mises_a_jour
        def __init__(self, fenetre, langue_utilisee, width_fenetre_de_conf, height_fenetre_de_conf):

                #Appel au constructeur de la classe parente
                Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)

		#
		self.identifiant_en_lettres_de_la_langue_uttilisee = ""

		#
		texte_du_label_d_indication_du_spinbox_de_l_heure_a_renseigner = ""

		#
		texte_du_label_d_indication_du_spinbox_de_la_minute_a_renseigner = ""

		#
		texte_du_label_d_indication_du_spinbox_de_la_seconde_a_renseigner = ""

		#
		texte_du_label_d_indication_de_la_frequence_d_activation_des_mises_a_jour = ""

		#
		texte_du_bouton_de_validation = ""

		#
		self.contenu_textuel_d_indication_du_succee = ""

		#
		self.contenu_textuel_d_indication_pour_une_erreur_classique = ""

		#
		self.contenu_textuel_d_indication_pour_une_erreur_de_type_valueerror = ""

		#
		tableau_contenant_les_differentes_frequences_pour_les_mises_a_jour = []

		#
		self.langue_utilisee = langue_utilisee

		#
		tableau_contenant_l_heure_la_minute_et_la_seconde_pour_enclencher_les_mises_a_jour = horloge_monde.renvoie_de_l_heure_de_la_minute_et_de_la_seconde_pour_les_mises_a_jour()

		#
		indice_de_la_ville_courante_pour_les_mises_a_jour = horloge_monde.renvoie_de_l_id_de_la_ville_pour_les_mises_a_jour()

		#
		indice_de_la_ville_courante_pour_les_mises_a_jour = indice_de_la_ville_courante_pour_les_mises_a_jour - 1

		#
		frequence_des_mises_a_jour = horloge_monde.renvoie_de_la_frequence_pour_les_mises_a_jour()

		#
		if self.langue_utilisee == 0:

			#
                	self.identifiant_en_lettres_de_la_langue_uttilisee = "en"

                	#
                	texte_du_label_d_indication_du_spinbox_de_l_heure_a_renseigner = "Hour: "

                	#
                	texte_du_label_d_indication_du_spinbox_de_la_minute_a_renseigner = "Minute: "

                	#
                	texte_du_label_d_indication_du_spinbox_de_la_seconde_a_renseigner = "Second: "

                	#
               	 	texte_du_label_d_indication_de_la_frequence_d_activation_des_mises_a_jour = "Choice of frequency of updates: "

                	#
                	texte_du_bouton_de_validation = "Validate to regularly update"

			#
			texte_du_label_d_indication_de_la_combobox_pour_renseignement_de_la_ville_pour_lequel_appliquer_le_reveil = "Choix de la ville pour lequel appliquer l'heure et la fréquence des mises à jour"

			#
                	tableau_contenant_les_differentes_frequences_pour_les_mises_a_jour = ["every day from today", "every week starting today", "every month starting today"]

			#
                	self.contenu_textuel_d_indication_du_succee = "time, city, and frequency of updates registered succesfully"

			#
                	self.contenu_textuel_d_indication_pour_une_erreur_classique = "Error: Time not valid"

			#
			self.contenu_textuel_d_indication_pour_une_erreur_de_type_valueerror = "Hour, minute and second obligatorily integers !!!!"

			#
			self.contenu_textuel_d_indication_de_la_similitude_avec_heure_et_minute_du_reveil = "Error: The hour and the minute for the updates must be strictly different from those of the alarm clock"

		#
		else:

			#
                        self.identifiant_en_lettres_de_la_langue_uttilisee = "fr"

                        #
                        texte_du_label_d_indication_du_spinbox_de_l_heure_a_renseigner = "Heure: "

                        #
                        texte_du_label_d_indication_du_spinbox_de_la_minute_a_renseigner = "Minute: "

                        #
                        texte_du_label_d_indication_du_spinbox_de_la_seconde_a_renseigner = "Seconde: "

                        #
                        texte_du_label_d_indication_de_la_frequence_d_activation_des_mises_a_jour = "Choix de la fréquence des mises à jour: "

                        #
                        texte_du_bouton_de_validation = "Valider pour mettre à jour régulièrement"

			#
                        texte_du_label_d_indication_de_la_combobox_pour_renseignement_de_la_ville_pour_lequel_appliquer_le_reveil = "Choice of the city for which to apply the time and frequency of updates"

			#
			tableau_contenant_les_differentes_frequences_pour_les_mises_a_jour = ["Chaque jour à partir d'aujourd'hui", "Chaque semaine à partir d'aujourd'hui", "Chaque mois à partir d'aujourd'hui"]

			#
                        self.contenu_textuel_d_indication_du_succee = "heure, ville et fréquence des mises à jour enregistrées avec succès"

			#
                	self.contenu_textuel_d_indication_pour_une_erreur_classique = "Erreur: Heure pas valide"

			#
			self.contenu_textuel_d_indication_pour_une_erreur_de_type_valueerror = "Heure, minute et seconde obligatoirement entiers !!!!"

			#
			self.contenu_textuel_d_indication_de_la_similitude_avec_heure_et_minute_du_reveil = "Erreur: L'heure et la minute pour les mises à jour doivent être strictement différents de ceux du reveil"

		#
                self.label_choix_heure = Label(fenetre, text = texte_du_label_d_indication_du_spinbox_de_l_heure_a_renseigner)

                #
                self.label_choix_heure.pack()

		#
                heure_par_defaut = StringVar()

                #
                heure_par_defaut.set(tableau_contenant_l_heure_la_minute_et_la_seconde_pour_enclencher_les_mises_a_jour[0])

                #
                self.choix_heure = Spinbox(fenetre, from_ = 0, to = 23, textvariable = heure_par_defaut)

                #
                self.choix_heure.pack()

		#
                self.label_choix_minute = Label(fenetre, text = texte_du_label_d_indication_du_spinbox_de_la_minute_a_renseigner)

                #
                self.label_choix_minute.pack()

                #
                minute_par_defaut = StringVar()

                #
                minute_par_defaut.set(tableau_contenant_l_heure_la_minute_et_la_seconde_pour_enclencher_les_mises_a_jour[1])

		#
                self.choix_minute = Spinbox(fenetre, from_ = 0, to = 59, textvariable = minute_par_defaut)

                #
                self.choix_minute.pack()

                #
                self.label_choix_seconde = Label(fenetre, text = texte_du_label_d_indication_du_spinbox_de_la_seconde_a_renseigner)

                #
                self.label_choix_seconde.pack()

                #
                seconde_par_defaut = StringVar()

                #
                seconde_par_defaut.set(tableau_contenant_l_heure_la_minute_et_la_seconde_pour_enclencher_les_mises_a_jour[2])

                #
                self.choix_seconde = Spinbox(fenetre, from_ = 0, to = 59, textvariable = seconde_par_defaut)

		#
                self.choix_seconde.pack()

		#
                self.label_du_choix_de_la_ville = Label(fenetre, text = texte_du_label_d_indication_de_la_combobox_pour_renseignement_de_la_ville_pour_lequel_appliquer_le_reveil)

                #
                self.label_du_choix_de_la_ville.pack()

                #
                self.liste_des_villes = horloge_monde.retour_des_villes_enregistrees_dans_la_base(fenetre, -1, -1, indice_de_la_ville_courante_pour_les_mises_a_jour, self.langue_utilisee)

                #
                self.liste_des_villes.pack()

		#
                self.label_du_choix_de_la_frequence = Label(fenetre, text = texte_du_label_d_indication_de_la_frequence_d_activation_des_mises_a_jour)

                #
                self.label_du_choix_de_la_frequence.pack()

		#
		self.combobox_du_choix_de_la_frequence = ttk.Combobox(fenetre, state = "readonly", values = tableau_contenant_les_differentes_frequences_pour_les_mises_a_jour, width = 50)

        	#
        	self.combobox_du_choix_de_la_frequence.current(frequence_des_mises_a_jour)

		#
		self.combobox_du_choix_de_la_frequence.pack()

		#
		self.fenetre = fenetre

		#
                self.bouton_de_validation = Button(fenetre, text = texte_du_bouton_de_validation, command = self.validation_de_l_heure_la_minute_la_seconde_la_ville_et_la_frequence_pour_proceder_aux_mises_a_jour_regulieres)

                #
                self.bouton_de_validation.pack()

	#
	def modification_des_parametres_des_mises_a_jour(self, heure, minute, seconde, frequence, id_de_la_ville):

		#
		horloge_monde.mise_a_jour_de_la_table_Mise_a_jour(heure, minute, seconde, frequence, id_de_la_ville)

	#La fonction verification_des_donnees permet de vérifier si les données entrées dans les differents champs de la fenetre de configuration du reveil sont valides
	def verification_des_donnees(self, heure, minute, seconde):

		#
                variable_de_retour = True

                #
                if not(heure < 24 and heure >= 0):

                        #
                        variable_de_retour = False

                #
                if not(minute < 60 and minute >= 0):

                        #
                        variable_de_retour = False

                #
                if not(seconde < 60 and seconde >= 0):

                        #
                        variable_de_retour = False

                #La variable de retour de la fonction variable_de_retour est retournée
                return variable_de_retour

	#
	def validation_de_l_heure_la_minute_la_seconde_la_ville_et_la_frequence_pour_proceder_aux_mises_a_jour_regulieres(self):

		#
		try:

			#
			heure_a_analyser = int(self.choix_heure.get())

			#
			minute_a_analyser = int(self.choix_minute.get())

			#
			seconde_a_analyser = int(self.choix_seconde.get())

			#
			if self.verification_des_donnees(heure_a_analyser, minute_a_analyser, seconde_a_analyser) == True:

				#
				try:

					#
					tableau_contenant_l_heure_la_minute_et_la_seconde_pour_faire_sonner_le_reveil = horloge_monde.renvoie_de_l_heure_de_la_minute_et_de_la_seconde_pour_faire_sonner_le_reveil()

					#
					heure_a_prendre = str(self.choix_heure.get())

					#
					minute_a_prendre = str(self.choix_minute.get())

					#
					seconde_a_prendre = str(self.choix_seconde.get())

					#
					frequence_selectionnee = str(self.combobox_du_choix_de_la_frequence.current())

					#
					id_de_la_ville_selectionnee = str(self.liste_des_villes.current() + 1)

					#
					if int(heure_a_prendre) == int(tableau_contenant_l_heure_la_minute_et_la_seconde_pour_faire_sonner_le_reveil[0]) and int(minute_a_prendre) == int(tableau_contenant_l_heure_la_minute_et_la_seconde_pour_faire_sonner_le_reveil[1]):

						#
						subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", self.contenu_textuel_d_indication_de_la_similitude_avec_heure_et_minute_du_reveil])

					#
					else:

						#
						self.modification_des_parametres_des_mises_a_jour(heure_a_prendre, minute_a_prendre, seconde_a_prendre, frequence_selectionnee, id_de_la_ville_selectionnee)

						#
						subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", self.contenu_textuel_d_indication_du_succee])

				#
				except Exception:

					#
					subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", self.contenu_textuel_d_indication_pour_une_erreur_classique])

			#
			else:

				#
				subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", self.contenu_textuel_d_indication_pour_une_erreur_classique])

		#
		except ValueError:

			#
			subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", self.contenu_textuel_d_indication_pour_une_erreur_de_type_valueerror])

		#
		finally:

			#
			self.fenetre.destroy()
