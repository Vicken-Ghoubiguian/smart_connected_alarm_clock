# -*- coding: utf-8 -*

#
try:

	#
	from Tkinter import *

	#
	from tkMessageBox import *

	#
	import ttk

#
except ImportError:

	#
	from tkinter import *

	#
	from tkinter.messagebox import *

	#
	import tkinter.ttk

import horloge_monde

#
class Configuration_du_Reveil(Frame):

	#Définition du constructeur de la classe Configuration_du_Reveil
	def __init__(self, fenetre, langue_uttilisee, width_fenetre_de_conf, height_fenetre_de_conf):

		#Appel au constructeur de la classe parente
		Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)

		#
		self.langue_uttilisee = langue_uttilisee

		#
		tableau_contenant_l_heure_la_minute_et_la_seconde_pour_faire_sonner_le_reveil = horloge_monde.renvoie_de_l_heure_de_la_minute_de_la_seconde_et_de_la_timezone_pour_faire_sonner_le_reveil()

		#
		indice_du_single_courant_a_jouer_en_cas_de_sonnerie_du_reveil = horloge_monde.renvoie_de_l_id_du_single_enregistre_pour_faire_sonner_le_reveil()

		#
		indice_de_la_ville_courante_pour_faire_sonner_le_reveil = horloge_monde.renvoie_de_l_id_de_la_ville_pour_faire_sonner_le_reveil()

		#
		indice_de_la_ville_courante_pour_faire_sonner_le_reveil = indice_de_la_ville_courante_pour_faire_sonner_le_reveil - 1

		#
		frequence_de_la_sonnerie_du_reveil = horloge_monde.renvoie_de_la_frequence_de_la_sonnerie_du_reveil()

		#
		texte_du_label_d_indication_du_spinbox_de_l_heure_a_renseigner = " "

		#
		texte_du_label_d_indication_du_spinbox_de_la_minute_a_renseigner = " "

		#
		texte_du_label_d_indication_du_spinbox_de_la_seconde_a_renseigner = " "

		#
		texte_du_label_d_indication_de_la_combobox_pour_renseignement_du_single_a_jouer = " "

		#
                texte_du_bouton_de_validation = " "

		#
		texte_de_la_spinbox_d_indication_de_la_frequence_d_activation_du_reveil = " "

		#
		texte_du_label_d_indication_de_la_combobox_pour_renseignement_du_jour_de_la_semaine_en_fonction_duquel_appliquer_le_reveil = " "

		#
		texte_du_label_d_indication_de_la_combobox_pour_renseignement_de_la_ville_pour_lequel_appliquer_le_reveil = " "

		#
		self.titre_de_la_fenetre_modale_d_indication_d_une_erreur = " "

		#
		self.titre_de_la_fenetre_modale_d_indication_du_succee = " "

		#
		self.texte_de_la_fenetre_modale_d_indication_du_succee = " "

		#
		self.texte_de_la_fenetre_d_indication_pour_une_erreur_classique = " "

		#
		self.texte_de_la_fenetre_d_indication_pour_une_erreur_de_type_valueerror = " "

		#
		liste_des_jours_de_la_semaine = []

		#
		if langue_uttilisee == 0:

			#
			self.identifiant_en_lettres_de_la_langue_uttilisee = "en"

			#
			texte_du_label_d_indication_du_spinbox_de_l_heure_a_renseigner = "Hour: "

			#
			texte_du_label_d_indication_du_spinbox_de_la_minute_a_renseigner = "Minute: "

			#
			texte_du_label_d_indication_du_spinbox_de_la_seconde_a_renseigner = "Second: "

			#
			texte_du_label_d_indication_de_la_combobox_pour_renseignement_du_single_a_jouer = "Choice of the single for the alarm clock: "

			#
			texte_du_bouton_de_validation = "Confirm the alarm time"

			#
			texte_de_la_spinbox_d_indication_de_la_frequence_d_activation_du_reveil = "Frequency: "

			#
			liste_des_jours_de_la_semaine = ["Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday", "Everyday"]

			#
			texte_du_label_d_indication_de_la_combobox_pour_renseignement_du_jour_de_la_semaine_en_fonction_duquel_appliquer_le_reveil = "Choice of the day of the week: "

			#
			texte_du_label_d_indication_de_la_combobox_pour_renseignement_de_la_ville_pour_lequel_appliquer_le_reveil = "Choice of the city for which to apply the alarm clock: "

			#
                	self.contenu_textuel_d_indication_du_succee = "Time, frequency and city registered !!!!"

			#
			self.contenu_textuel_d_indication_pour_une_erreur_classique = "Error: Time you not valid"

			#
			self.contenu_textuel_d_indication_pour_une_erreur_de_type_valueerror = "Hour, minute and second obligatorily integers !!!!"

			#
			self.contenu_textuel_d_indication_de_la_similitude_avec_heure_et_minute_des_mises_a_jour = "Error: The hour, the minute and the timezone to sound the alarm must be strictly different from those of the updates"

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
                        texte_du_label_d_indication_de_la_combobox_pour_renseignement_du_single_a_jouer = "Choix du single pour le réveil: "

                        #
                        texte_du_bouton_de_validation = "Valider l'heure de réveil"

                        #
                        texte_de_la_spinbox_d_indication_de_la_frequence_d_activation_du_reveil = "Frequence: "

                        #
                        liste_des_jours_de_la_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche", "Tous les jours"]

			#
			texte_du_label_d_indication_de_la_combobox_pour_renseignement_du_jour_de_la_semaine_en_fonction_duquel_appliquer_le_reveil = "Choix du jour de la semaine: "

			#
			texte_du_label_d_indication_de_la_combobox_pour_renseignement_de_la_ville_pour_lequel_appliquer_le_reveil = "Choix de la ville pour lequel appliquer le réveil: "

			#
                	self.contenu_textuel_d_indication_du_succee = "Heure, fréquence et ville enregistrés avec succès !!!!"

			#
			self.contenu_textuel_d_indication_pour_une_erreur_classique = "Erreur: Heure pas valide !!!!"

			#
			self.contenu_textuel_d_indication_pour_une_erreur_de_type_valueerror = "Heure, minute et seconde obligatoirement entiers !!!!"

			#
			self.contenu_textuel_d_indication_de_la_similitude_avec_heure_et_minute_des_mises_a_jour = "Erreur: L'heure, la minute et la timezone pour faire sonner le réveil doivent être strictement différents de ceux des mises à jour"

		#
		self.label_choix_heure = Label(fenetre, text = texte_du_label_d_indication_du_spinbox_de_l_heure_a_renseigner)

		#
		self.label_choix_heure.pack()

		#
                heure_par_defaut = StringVar()

                #
                heure_par_defaut.set(tableau_contenant_l_heure_la_minute_et_la_seconde_pour_faire_sonner_le_reveil[0])

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
		minute_par_defaut.set(tableau_contenant_l_heure_la_minute_et_la_seconde_pour_faire_sonner_le_reveil[1])

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
		seconde_par_defaut.set(tableau_contenant_l_heure_la_minute_et_la_seconde_pour_faire_sonner_le_reveil[2])

		#
		self.choix_seconde = Spinbox(fenetre, from_ = 0, to = 59, textvariable = seconde_par_defaut)

		#
		self.choix_seconde.pack()

		#
		self.label_du_choix_du_single_pour_le_reveil = Label(fenetre, text = texte_du_label_d_indication_de_la_combobox_pour_renseignement_du_single_a_jouer)

		#
		self.label_du_choix_du_single_pour_le_reveil.pack()

		#
		self.liste_des_singles_pour_choisir_celui_du_reveil = horloge_monde.retour_des_singles_enregistres_dans_la_base(fenetre, indice_du_single_courant_a_jouer_en_cas_de_sonnerie_du_reveil - 1, -1)

		#
		self.liste_des_singles_pour_choisir_celui_du_reveil.pack()

		#
                self.label_du_choix_de_la_frequence = Label(fenetre, text = texte_du_label_d_indication_de_la_combobox_pour_renseignement_du_single_a_jouer)

                #
                self.label_du_choix_de_la_frequence.pack()

		#
		self.label_choix_de_la_frequence = Label(fenetre, text = texte_du_label_d_indication_de_la_combobox_pour_renseignement_du_jour_de_la_semaine_en_fonction_duquel_appliquer_le_reveil)

		#Insertion de tous les jours de la semaine, en plus de la demande de déclanchement du reveil pour tous les jours, dans la liste (de type Listbox)
		self.liste_des_jours_de_la_semaine = ttk.Combobox(fenetre, state = "readonly", values = liste_des_jours_de_la_semaine)

		#Initialisation de la valeur par défaut à la valeur numérique (int) correspondant au jour de la semaine pour lequel le reveil est configuré pour sonner
		self.liste_des_jours_de_la_semaine.current(frequence_de_la_sonnerie_du_reveil)

		#
		self.liste_des_jours_de_la_semaine.pack()

		#
		self.label_du_choix_de_la_ville = Label(fenetre, text = texte_du_label_d_indication_de_la_combobox_pour_renseignement_de_la_ville_pour_lequel_appliquer_le_reveil)

                #
                self.label_du_choix_de_la_ville.pack()

		#
		self.liste_des_villes = horloge_monde.retour_des_villes_enregistrees_dans_la_base(fenetre, -1, indice_de_la_ville_courante_pour_faire_sonner_le_reveil, self.langue_uttilisee)

		#
		self.liste_des_villes.pack()

		#
                self.boutton_de_validation = Button(fenetre, text = texte_du_bouton_de_validation, command = self.validation_des_donnees)

                #
                self.boutton_de_validation.pack()

		#
		self.fenetre = fenetre

	#
	def modification_des_parametres_du_reveil(self, heure, minute, seconde, frequence, ville, indice_du_single_a_jouer):

		#
		horloge_monde.mise_a_jour_de_la_table_reveil(heure, minute, seconde, frequence, ville, indice_du_single_a_jouer)

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

	#Cette fonction permet de valider () les données entrées dans les champs de la fenetre de configuration du reveil
	def validation_des_donnees(self):

		#
		try:

			#Les valeurs renseignées précédements concernant l'heure, la minute, et la seconde sont converties en entiers et affectées dans des variables respectives
			heure_a_analyser = int(self.choix_heure.get())

			#
			minute_a_analyser = int(self.choix_minute.get())

			#
			seconde_a_analyser = int(self.choix_seconde.get())

			#
			indice_du_single_a_faire_jouer = self.liste_des_singles_pour_choisir_celui_du_reveil.current() + 1

			#Dans le cas ou l'heure entrée, puis vérifiée par la fonction verification_des_donnees est valide (la valeur de retour est True), alors....
			if self.verification_des_donnees(heure_a_analyser, minute_a_analyser, seconde_a_analyser) == True:

				#
				try:

					#
					tableau_contenant_l_heure_la_minute_la_seconde_et_la_timezone_pour_les_mises_a_jour = horloge_monde.renvoie_de_l_heure_de_la_minute_de_la_seconde_et_de_la_timezone_pour_les_mises_a_jour()

					#
					heure_a_prendre = str(self.choix_heure.get())

					#
                			minute_a_prendre = str(self.choix_minute.get())

					#
                			seconde_a_prendre = str(self.choix_seconde.get())

					#
                        		timezone_a_prendre = horloge_monde.renvoie_de_l_id_du_timezone_correspondant_a_l_id_de_la_ville_courante(self.liste_des_villes.current() + 1)

					#
                			frequence_selectionnee = str(self.liste_des_jours_de_la_semaine.current())

					#
                			id_de_la_ville_selectionnee = self.liste_des_villes.current() + 1

					#
					if int(heure_a_prendre) == int(tableau_contenant_l_heure_la_minute_la_seconde_et_la_timezone_pour_les_mises_a_jour[0]) and int(minute_a_prendre) == int(tableau_contenant_l_heure_la_minute_la_seconde_et_la_timezone_pour_les_mises_a_jour[1]) and timezone_a_prendre == int(tableau_contenant_l_heure_la_minute_la_seconde_et_la_timezone_pour_les_mises_a_jour[3]):

						#
						horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(self.contenu_textuel_d_indication_de_la_similitude_avec_heure_et_minute_des_mises_a_jour, self.identifiant_en_lettres_de_la_langue_uttilisee)

					#
					else:

						#
						self.modification_des_parametres_du_reveil(heure_a_prendre, minute_a_prendre, seconde_a_prendre, frequence_selectionnee, id_de_la_ville_selectionnee, str(indice_du_single_a_faire_jouer))

						#
						horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(self.contenu_textuel_d_indication_du_succee, self.identifiant_en_lettres_de_la_langue_uttilisee)

				#
				except Exception:

					#
					horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(self.contenu_textuel_d_indication_pour_une_erreur_classique, self.identifiant_en_lettres_de_la_langue_uttilisee)

			#Sinon...
			else:
				#
				horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(self.contenu_textuel_d_indication_pour_une_erreur_classique, self.identifiant_en_lettres_de_la_langue_uttilisee)

		#Dans le cas où les données entrées dans les champs de l'heure, de la minute et de la seconde ne sont pas des entiers (une erreur de type ValueError est générée), alors...
		except ValueError:

			#
			horloge_monde.uttilisation_de_la_conversion_du_texte_a_la_voix_grace_a_eSpeak(self.contenu_textuel_d_indication_pour_une_erreur_de_type_valueerror, self.identifiant_en_lettres_de_la_langue_uttilisee)

		#
		finally:

			#
			self.fenetre.destroy()

