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
		texte_du_bouton_de_validation = ""

		#
		self.contenu_textuel_d_indication_du_succee = ""

		#
		self.contenu_textuel_d_indication_pour_une_erreur_classique = ""

		#
		self.contenu_textuel_d_indication_pour_une_erreur_de_type_valueerror = ""

		#
		self.langue_utilisee = langue_utilisee

		#
		tableau_contenant_l_heure_la_minute_et_la_seconde_pour_enclencher_les_mises_a_jour = horloge_monde.renvoie_de_l_heure_de_la_minute_de_la_seconde_et_de_la_timezone_pour_les_mises_a_jour()

		#
		indice_de_la_ville_courante_pour_les_mises_a_jour = horloge_monde.renvoie_de_l_id_de_la_ville_pour_les_mises_a_jour()

		#
		indice_de_la_ville_courante_pour_les_mises_a_jour = indice_de_la_ville_courante_pour_les_mises_a_jour - 1

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
                	texte_du_bouton_de_validation = "Validate to regularly update"

			#
			texte_du_label_d_indication_de_la_combobox_pour_renseignement_de_la_ville_pour_lequel_appliquer_le_reveil = "Choice of the city for which to apply the time of updates"

			#
                	self.contenu_textuel_d_indication_du_succee = "time and city of updates registered succesfully"

			#
                	self.contenu_textuel_d_indication_pour_une_erreur_classique = "Error: Time not valid"

			#
			self.contenu_textuel_d_indication_pour_une_erreur_de_type_valueerror = "Hour, minute and second obligatorily integers !!!!"

			#
			self.contenu_textuel_d_indication_de_la_similitude_avec_heure_et_minute_du_reveil = "Error: The hour, minute and timezone for updates must be strictly different from those of the alarm clock"

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
                        texte_du_bouton_de_validation = "Valider pour mettre à jour régulièrement"

			#
			texte_du_label_d_indication_de_la_combobox_pour_renseignement_de_la_ville_pour_lequel_appliquer_le_reveil = "Choix de la ville pour lequel appliquer l'heure des mises à jour"

			#
                        self.contenu_textuel_d_indication_du_succee = "heure et ville des mises à jour enregistrées avec succès"

			#
                	self.contenu_textuel_d_indication_pour_une_erreur_classique = "Erreur: Heure pas valide"

			#
			self.contenu_textuel_d_indication_pour_une_erreur_de_type_valueerror = "Heure, minute et seconde obligatoirement entiers !!!!"

			#
			self.contenu_textuel_d_indication_de_la_similitude_avec_heure_et_minute_du_reveil = "Erreur: L'heure, la minute et la timezone pour les mises à jour doivent être strictement différents de ceux du réveil"

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
		self.fenetre = fenetre

		#
                self.bouton_de_validation = Button(fenetre, text = texte_du_bouton_de_validation, command = self.validation_de_l_heure_la_minute_la_seconde_et_de_la_ville_pour_proceder_aux_mises_a_jour_regulieres)

                #
                self.bouton_de_validation.pack()

	#
	def modification_des_parametres_des_mises_a_jour(self, heure, minute, seconde, id_de_la_ville):

		#
		horloge_monde.mise_a_jour_de_la_table_Mise_a_jour(heure, minute, seconde, id_de_la_ville)

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
	def validation_de_l_heure_la_minute_la_seconde_et_de_la_ville_pour_proceder_aux_mises_a_jour_regulieres(self):

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
					tableau_contenant_l_heure_la_minute_la_seconde_et_la_timezone_pour_faire_sonner_le_reveil = horloge_monde.renvoie_de_l_heure_de_la_minute_de_la_seconde_et_de_la_timezone_pour_faire_sonner_le_reveil()

					#
					heure_a_prendre = str(self.choix_heure.get())

					#
					minute_a_prendre = str(self.choix_minute.get())

					#
					seconde_a_prendre = str(self.choix_seconde.get())

					#
                        		timezone_a_prendre = horloge_monde.renvoie_de_l_id_du_timezone_correspondant_a_l_id_de_la_ville_courante(self.liste_des_villes.current() + 1)

					#
					id_de_la_ville_selectionnee = str(self.liste_des_villes.current() + 1)

					#
					if int(heure_a_prendre) == int(tableau_contenant_l_heure_la_minute_la_seconde_et_la_timezone_pour_faire_sonner_le_reveil[0]) and int(minute_a_prendre) == int(tableau_contenant_l_heure_la_minute_la_seconde_et_la_timezone_pour_faire_sonner_le_reveil[1]) and int(timezone_a_prendre) == int(tableau_contenant_l_heure_la_minute_la_seconde_et_la_timezone_pour_faire_sonner_le_reveil[3]):

						#
						horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(self.contenu_textuel_d_indication_de_la_similitude_avec_heure_et_minute_du_reveil, self.identifiant_en_lettres_de_la_langue_uttilisee)

					#
					else:

						#
						self.modification_des_parametres_des_mises_a_jour(heure_a_prendre, minute_a_prendre, seconde_a_prendre, id_de_la_ville_selectionnee)

						#
						horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(self.contenu_textuel_d_indication_du_succee, self.identifiant_en_lettres_de_la_langue_uttilisee)

				#
				except Exception:

					#
					horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(self.contenu_textuel_d_indication_pour_une_erreur_classique, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#
			else:

				#
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(self.contenu_textuel_d_indication_pour_une_erreur_classique, self.identifiant_en_lettres_de_la_langue_uttilisee)

		#
		except ValueError:

			#
			horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(self.contenu_textuel_d_indication_pour_une_erreur_de_type_valueerror, self.identifiant_en_lettres_de_la_langue_uttilisee)

		#
		finally:

			#
			self.fenetre.destroy()
