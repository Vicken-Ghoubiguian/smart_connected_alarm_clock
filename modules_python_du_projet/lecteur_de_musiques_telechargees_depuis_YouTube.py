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

import pygame
import pygame.mixer
import horloge_monde
import math
import subprocess

#Cette classe permet de définir une interface pour lire des fichiers audios téléchargés depuis YouTube
class Lecteur_de_musiques_telechargees_depuis_YouTube(Frame):

	#Définition du constructeur de la classe Lecteur_de_musiques_telechargees_depuis_YouTube
        def __init__(self, fenetre, langue_utilisee, width_fenetre_de_conf, height_fenetre_de_conf):

                #Appel au constructeur de la classe parente
                Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)

		#
                pygame.mixer.init(44100, -16, 2, 2048)

		#
                pygame.mixer.music.set_volume(0.5)

		#
		self.langue = langue_utilisee

		#
		if langue_utilisee == 0:

			#
			self.identifiant_en_lettres_de_la_langue_uttilisee = "en"

			#
			texte_du_label_d_indication_de_selection_du_fichier_audio_a_ecouter = "Selection of music to listen to: "

			#
			texte_du_label_de_definition_du_choix_du_nombre_de_repetitions = "Setting the number of repetitions: "

			#
			texte_du_label_d_affichage_du_titre_du_fichier_audio_a_ecouter = "Title of the single you want to listen to: "

			#
			texte_du_bouton_de_validation_du_choix_du_fichier_audio_a_ecouter = "Confirm the selected music"

			#
			texte_du_label_d_affichage_de_l_auteur_du_fichier_audio_a_ecouter = "Author of the single you want to listen to: "

			#
			texte_du_label_d_affichage_du_pays_d_origine_du_fichier_audio_a_ecouter = "Country of origin of the single you want to listen to: "

			#
			texte_du_boutton_de_demarrage_ou_de_reset_du_fichier_audio_ecoute = "Start / Restart"

			#
			texte_du_label_d_indication_de_la_position_de_la_lecture_du_fichier_audio_selectionne = "Indication of the playback position of the selected audio file: "

			#
			self.texte_d_indication_de_l_unite_temporelle_de_base = " (in seconds)"

			#
			self.texte_d_indication_du_label_d_indication_du_volume = "Volume is at "

			#
			self.texte_d_indication_de_l_arret_de_la_musique_avec_succes = "Music stopped successfully"

			#
			self.texte_d_indication_d_une_erreur_liee_a_la_musique_qui_est_arrete = "Error: Music already stopped"

			#
			self.texte_d_indication_d_une_erreur_liee_a_la_musique_qui_ne_joue_pas = "Error: The music does not play"

			#
                        self.texte_d_indication_d_une_erreur_liee_a_la_musique_qui_n_est_pas_chargee = "Error: Music is not loaded"

		#
		else:

			#
			self.identifiant_en_lettres_de_la_langue_uttilisee = "fr"

			#
			texte_du_label_d_indication_de_selection_du_fichier_audio_a_ecouter = "Séléction de la musique à écouter: "

			#
			texte_du_label_de_definition_du_choix_du_nombre_de_repetitions = "Définition du nombre de répétition: "

			#
			texte_du_label_d_affichage_du_titre_du_fichier_audio_a_ecouter = "Titre du single que vous voulez écouter: "

			#
			texte_du_bouton_de_validation_du_choix_du_fichier_audio_a_ecouter = "Validez la musique séléctionée"

			#
			texte_du_label_d_affichage_de_l_auteur_du_fichier_audio_a_ecouter = "Auteur du single que vous voulez écouter: "

			#
			texte_du_label_d_affichage_du_pays_d_origine_du_fichier_audio_a_ecouter = "Pays d'origine du single que vous voulez écouter: "

			#
			texte_du_boutton_de_demarrage_ou_de_reset_du_fichier_audio_ecoute = "Demarage / Redemarage"

			#
			texte_du_label_d_indication_de_la_position_de_la_lecture_du_fichier_audio_selectionne = "Indication de la position de lecture du fichier audio séléctionné: "

			#
			self.texte_d_indication_de_l_unite_temporelle_de_base = " (en secondes)"

			#
			self.texte_d_indication_du_label_d_indication_du_volume = "Le volume est à "

			#
			self.texte_d_indication_de_l_arret_de_la_musique_avec_succes = "Musique arretée avec succès"

			#
                        self.texte_d_indication_d_une_erreur_liee_a_la_musique_qui_est_arrete = "Erreur: Musique déjà arretée"

			#
			self.texte_d_indication_d_une_erreur_liee_a_la_musique_qui_ne_joue_pas = "Erreur: La musique ne joue pas"

			#
			self.texte_d_indication_d_une_erreur_liee_a_la_musique_qui_n_est_pas_chargee = "Erreur: La musique n'est pas chargée"

		#
		self.label_de_selection_du_fichier_audio_a_ecouter = Label(fenetre, text = texte_du_label_d_indication_de_selection_du_fichier_audio_a_ecouter)

		#
		self.label_de_selection_du_fichier_audio_a_ecouter.pack()

		#
                self.liste_des_singles_a_choisir_pour_ecouter = horloge_monde.retour_des_singles_enregistres_dans_la_base(fenetre, 0)

		#
		self.liste_des_singles_a_choisir_pour_ecouter.current(0)

                #
                self.liste_des_singles_a_choisir_pour_ecouter.pack()

		#
		self.label_de_definition_du_choix_du_nombre_de_repetitions = Label(fenetre, text = texte_du_label_de_definition_du_choix_du_nombre_de_repetitions)

		#
		self.label_de_definition_du_choix_du_nombre_de_repetitions.pack()

		#
		self.choix_du_nombre_de_repetitions_du_fichier_audio_selectionne = Spinbox(fenetre, state = "readonly", from_ = 0, to = 100)

		#
		self.choix_du_nombre_de_repetitions_du_fichier_audio_selectionne.pack()

		#
		self.bouton_de_validation_du_choix_du_fichier_audio_a_ecouter = Button(fenetre, text = texte_du_bouton_de_validation_du_choix_du_fichier_audio_a_ecouter, command = self.validation_de_la_musique)

		#
		self.bouton_de_validation_du_choix_du_fichier_audio_a_ecouter.pack()

		#
		self.label_d_affichage_du_titre_du_fichier_audio_a_ecouter = Label(fenetre, text = texte_du_label_d_affichage_du_titre_du_fichier_audio_a_ecouter)

		#
		self.label_d_affichage_du_titre_du_fichier_audio_a_ecouter.pack()

		#
		self.label_d_affichage_de_l_auteur_du_fichier_audio_a_ecouter = Label(fenetre, text = texte_du_label_d_affichage_de_l_auteur_du_fichier_audio_a_ecouter)

		#
                self.label_d_affichage_de_l_auteur_du_fichier_audio_a_ecouter.pack()

		#
                self.label_d_affichage_du_pays_d_origine_du_fichier_audio_a_ecouter = Label(fenetre, text = texte_du_label_d_affichage_du_pays_d_origine_du_fichier_audio_a_ecouter)

                #
                self.label_d_affichage_du_pays_d_origine_du_fichier_audio_a_ecouter.pack()

		#
		self.boutton_de_demarrage_ou_de_reset_du_fichier_audio_ecoute = Button(fenetre, text = texte_du_boutton_de_demarrage_ou_de_reset_du_fichier_audio_ecoute, command = self.demarage_ou_redemarage_de_la_musique)

		#
		self.boutton_de_demarrage_ou_de_reset_du_fichier_audio_ecoute.pack()

		#
		self.bouton_de_lecture_ou_de_pause_du_fichier_audio_ecoute = Button(fenetre, text = "Play / Pause", command = self.lecture_ou_pause_de_la_musique)

		#
		self.bouton_de_lecture_ou_de_pause_du_fichier_audio_ecoute.pack()

		#
		self.bouton_d_arret_du_fichier_audio_ecoute = Button(fenetre, text = "Stop", command = self.arret_du_fichier_audio)

		#
		self.bouton_d_arret_du_fichier_audio_ecoute.pack()

		#
		self.label_d_indication_de_la_position_de_la_lecture_du_fichier_audio_selectionne = Label(fenetre, text = texte_du_label_d_indication_de_la_position_de_la_lecture_du_fichier_audio_selectionne)

		#
		self.label_d_indication_de_la_position_de_la_lecture_du_fichier_audio_selectionne.pack()

		#
		self.longueur_du_fichier_audio_selectionne = 0

		#
		self.label_d_indication_de_la_position_de_la_lecture = Label(fenetre, text = "0 / " + str(self.longueur_du_fichier_audio_selectionne) + self.texte_d_indication_de_l_unite_temporelle_de_base)

		#
		self.label_d_indication_de_la_position_de_la_lecture.pack()

		#
		self.barre_de_defilement_pour_le_reglage_du_volume_sonore = Scale(fenetre, from_ = 0, to = 100, fg = 'Yellow', bg = 'blue', command = self.reglage_du_volume_sonore, orient = HORIZONTAL)

		#
		self.barre_de_defilement_pour_le_reglage_du_volume_sonore.set(50)

		#
		self.barre_de_defilement_pour_le_reglage_du_volume_sonore.pack()

		#
		self.label_d_indication_du_volume = Label(fenetre, text = self.texte_d_indication_du_label_d_indication_du_volume + str(pygame.mixer.music.get_volume() * 100) + "%")

		#
		self.label_d_indication_du_volume.pack()

		#
		self.chemin_du_fichier_audio_a_jouer = ''

		#
		self.nombre_de_cliques_sur_le_bouton_de_validation = 0

		#
		self.nombre_de_repetitions_du_fichier_audio_selectionne = None

		#
		self.est_en_pause = False

		#
		self.est_stoppe = True

		#
		self.position_de_lecture = 0

		#
		self.fenetre = fenetre

	#
	def validation_de_la_musique(self):

		#Si le fichier audio selectionne est en cours de lecture alors...
		if pygame.mixer.music.get_busy() == True:

			#Une boite de dialogue de type affichage d'erreur (showerror) s'ouvre et indique qu'il est impossible d'effectuer une quelconque validation quand une musique joue.
                        showerror("Erreur dans le chargement de musique", "Erreur: Il est impossible de faire jouer une musique quand une autre le fait déjà !!!!")

		#Sinon...
		else:

			#
			id_du_single_choisi_pour_etre_ecoute = self.liste_des_singles_a_choisir_pour_ecouter.current() + 1

			#
			nom_du_single = horloge_monde.renvoi_du_titre_du_single_a_ecouter(id_du_single_choisi_pour_etre_ecoute)

			#
			nom_de_l_auteur = horloge_monde.renvoi_de_l_auteur_du_single_a_ecouter(id_du_single_choisi_pour_etre_ecoute)

			#
			nom_du_pays_d_origine = horloge_monde.renvoi_du_nom_du_pays_d_origine_du_single_a_ecouter(id_du_single_choisi_pour_etre_ecoute, self.langue)

			#
			self.est_en_pause = False

			#
			self.label_d_affichage_du_titre_du_fichier_audio_a_ecouter.config(text = nom_du_single)

			#
			self.label_d_affichage_de_l_auteur_du_fichier_audio_a_ecouter.config(text = nom_de_l_auteur)

			#
			self.label_d_affichage_du_pays_d_origine_du_fichier_audio_a_ecouter.config(text = nom_du_pays_d_origine)

			#
			self.chemin_du_fichier_audio_a_jouer = horloge_monde.renvoi_du_fichier_audio_selectionne_pour_etre_joue(id_du_single_choisi_pour_etre_ecoute)

			#
			collecte_des_informations_concernant_le_fichier_audio_selectionne = pygame.mixer.Sound(self.chemin_du_fichier_audio_a_jouer)

			#
			self.longueur_du_fichier_audio_selectionne = (collecte_des_informations_concernant_le_fichier_audio_selectionne.get_length())

			#
			self.longueur_du_fichier_audio_selectionne = int(math.ceil(self.longueur_du_fichier_audio_selectionne))

			#
			self.label_d_indication_de_la_position_de_la_lecture.config(text = "0 / " + str(self.longueur_du_fichier_audio_selectionne) + self.texte_d_indication_de_l_unite_temporelle_de_base)

			#
			self.nombre_de_repetitions_du_fichier_audio_selectionne = int(self.choix_du_nombre_de_repetitions_du_fichier_audio_selectionne.get())

			#
			self.nombre_de_cliques_sur_le_bouton_de_validation = self.nombre_de_cliques_sur_le_bouton_de_validation + 1

			#
			pygame.mixer.music.load(self.chemin_du_fichier_audio_a_jouer)

			#
			if self.langue == 0:

				#
				texte_a_dire_par_eSpeak_concernant_la_prise_en_compte_du_changement_de_musique = "Music taken into account"

			#
			else:

				#
				texte_a_dire_par_eSpeak_concernant_la_prise_en_compte_du_changement_de_musique = "Musique prise en compte"

			#
                        subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", texte_a_dire_par_eSpeak_concernant_la_prise_en_compte_du_changement_de_musique])

	#
	def demarage_ou_redemarage_de_la_musique(self):

		#
		if self.nombre_de_cliques_sur_le_bouton_de_validation > 0:

			#
			if pygame.mixer.music.get_busy() == True:

				#
				pygame.mixer.music.rewind()

				#
				pygame.mixer.music.play(loops = self.nombre_de_repetitions_du_fichier_audio_selectionne)

			#
			else:

				#
				pygame.mixer.music.play(loops = self.nombre_de_repetitions_du_fichier_audio_selectionne)

				#
				self.est_stoppe = False

		#
		else:

			#
			subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", self.texte_d_indication_d_une_erreur_liee_a_la_musique_qui_n_est_pas_chargee])

	#
	def lecture_ou_pause_de_la_musique(self):

		#Si le fichier audio selectionne est en pause alors...
                if self.est_en_pause == True:

			#
			pygame.mixer.music.unpause()

			#
			self.est_en_pause = False

		#
		elif self.nombre_de_cliques_sur_le_bouton_de_validation == 0:

			#
			subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", self.texte_d_indication_d_une_erreur_liee_a_la_musique_qui_ne_joue_pas])

		#
		elif self.est_stoppe == True:

			#
			subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", self.texte_d_indication_d_une_erreur_liee_a_la_musique_qui_est_arrete])

		#Sinon...
		else:

			#On met la musique en pause
			pygame.mixer.music.pause()

			#
			self.est_en_pause = True

	#
	def arret_du_fichier_audio(self):

		#Si le fichier audio selectionne joue alors...
		if pygame.mixer.music.get_busy() == True:

			#On arrete de la jouer
			pygame.mixer.music.stop()

			#
			self.est_stoppe = True

			#
                        subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", self.texte_d_indication_de_l_arret_de_la_musique_avec_succes])

			#
			self.label_d_indication_de_la_position_de_la_lecture.config(text = "0 / " + str(self.longueur_du_fichier_audio_selectionne) + self.texte_d_indication_de_l_unite_temporelle_de_base)

		#Sinon...
		else:

			#
			if self.nombre_de_cliques_sur_le_bouton_de_validation == 0:

				#
				subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", self.texte_d_indication_d_une_erreur_liee_a_la_musique_qui_ne_joue_pas])

			#
			else:

				#
				subprocess.call(["espeak", "-v" + self.identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", self.texte_d_indication_d_une_erreur_liee_a_la_musique_qui_est_arrete])

	#
	def reglage_du_volume_sonore(self, valeur_du_volume):

		#
		volume_a_parametrer = float(self.barre_de_defilement_pour_le_reglage_du_volume_sonore.get()) / 100

		#
		pygame.mixer.music.set_volume(volume_a_parametrer)

		#
		volume_a_afficher = pygame.mixer.music.get_volume() * 100

		#
		volume_a_afficher = math.ceil(volume_a_afficher)

		#
		self.label_d_indication_du_volume.config(text = self.texte_d_indication_du_label_d_indication_du_volume + str(volume_a_afficher) + "%")

	#
	def mise_a_jour_de_la_position_de_lecture(self):

		#
		if pygame.mixer.music.get_busy() == True:

			#
			if self.position_de_lecture != (pygame.mixer.music.get_pos() / 1000):

				#
				self.position_de_lecture = pygame.mixer.music.get_pos() / 1000

				#
                        	self.label_d_indication_de_la_position_de_la_lecture.config(text = str(self.position_de_lecture) + " / " + str(self.longueur_du_fichier_audio_selectionne) + self.texte_d_indication_de_l_unite_temporelle_de_base)

		#
		self.label_d_indication_de_la_position_de_la_lecture.after(200, self.mise_a_jour_de_la_position_de_lecture)
