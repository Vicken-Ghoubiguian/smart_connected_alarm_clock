# -*- coding: utf-8 -*

#
try:

	#
	from Tkinter import *

	#
	from tkMessageBox import *

#
except ImportError:

	#
	from tkinter import *

	#
	from tkinter.messagebox import *

import horloge_monde
import subprocess

#Cette classe permet de définir une interface graphique pour insérer une ville dans la base de données
class Insertion_des_Villes(Frame):

	#Définition du constructeur de la classe Insertion_des_villes
	def __init__(self, fenetre, language, width_fenetre_de_conf, height_fenetre_de_conf):

		#Appel au constructeur de la classe parente
		Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)

		#
		self.language_utilise_dans_la_fenetre = language

		#
		if self.language_utilise_dans_la_fenetre == 0:

			#
                        self.texte_du_label_d_entree_de_la_ville_en_francais = "City to insert (in french): "

                        #
                        self.texte_du_label_d_entree_de_la_ville_en_anglais = "City to insert (in english): "

                        #
                        self.texte_du_label_choix_du_pays_correspondant_a_la_ville =  "Country: "

                        #
                        self.texte_du_label_choix_du_timezone_correspondant_a_la_ville = "Time zone: "

			#
			self.texte_du_boutton_de_validation = "Validate the insertion of this city"

		#Sinon...
		else:

			#
			self.texte_du_label_d_entree_de_la_ville_en_francais = "Ville à insérer (en français): "

			#
			self.texte_du_label_d_entree_de_la_ville_en_anglais = "Ville à insérer (en anglais): "

			#
			self.texte_du_label_choix_du_pays_correspondant_a_la_ville =  "Pays: "

			#
			self.texte_du_label_choix_du_timezone_correspondant_a_la_ville = "Fuseau horaire: "

			#
			self.texte_du_boutton_de_validation = "Valider l'insertion de cette ville"

		#
		self.label_entree_de_la_ville_en_francais = Label(fenetre, text = self.texte_du_label_d_entree_de_la_ville_en_francais)

		#
		self.label_entree_de_la_ville_en_francais.pack()

		#
		self.saisie_de_la_ville_a_inserer_en_francais = Entry(fenetre)

		#
		self.saisie_de_la_ville_a_inserer_en_francais.pack()

		#
		self.entree_de_la_ville_en_anglais = Label(fenetre, text = self.texte_du_label_d_entree_de_la_ville_en_anglais)

		#
		self.entree_de_la_ville_en_anglais.pack()

		#
		self.saisie_de_la_ville_a_inserer_en_anglais = Entry(fenetre)

		#
		self.saisie_de_la_ville_a_inserer_en_anglais.pack()

		#
		self.label_choix_du_pays_correspondant_a_la_ville = Label(fenetre, text = self.texte_du_label_choix_du_pays_correspondant_a_la_ville)

		#
		self.label_choix_du_pays_correspondant_a_la_ville.pack()

		#
		self.liste_des_pays = horloge_monde.retour_des_pays_enregistres_dans_la_base(fenetre, language, "readonly")

		#
		self.liste_des_pays.pack()

		#
                self.label_choix_du_timezone_correspondant_a_la_ville = Label(fenetre, text = self.texte_du_label_choix_du_timezone_correspondant_a_la_ville)

                #
                self.label_choix_du_timezone_correspondant_a_la_ville.pack()

		#
		self.liste_des_timezones = horloge_monde.retour_des_timezones_enregistrees_dans_la_base(fenetre, -1)

                #
                self.liste_des_timezones.pack()

		#
                self.boutton_de_validation = Button(fenetre, text = self.texte_du_boutton_de_validation, command = self.validation_de_l_insertion_de_la_ville_dans_la_base)

                #
                self.boutton_de_validation.pack()

		#
		self.fenetre = fenetre

	#
	def validation_de_l_insertion_de_la_ville_dans_la_base(self):

		#
		indice_du_pays_selectionne = int(self.liste_des_pays.current())

		#
		contenu_textuel_de_la_fenetre_d_indication_du_succe_de_l_insertion_de_la_ville_dans_la_base_de_donnees = ""

		#
		indice_du_pays_selectionne = indice_du_pays_selectionne + 2

		#
		indice_du_timezone_selectionne = int(self.liste_des_timezones.current())

		#
		indice_du_timezone_selectionne = indice_du_timezone_selectionne + 1

		#
		if horloge_monde.verification_de_la_validite_de_la_ville(self.saisie_de_la_ville_a_inserer_en_francais.get(), self.saisie_de_la_ville_a_inserer_en_anglais.get(), indice_du_pays_selectionne) and horloge_monde.verification_de_la_pertinance_de_la_correspondance_entre_le_pays_et_le_timezone_selectionnes(indice_du_pays_selectionne, indice_du_timezone_selectionne):

			#
			try:

				#Dans le cas ou le nom de la ville entré possède une équivalence avec un nom de timezone
				if horloge_monde.verification_de_l_existence_d_une_equivalence_avec_un_nom_de_timezone(self.saisie_de_la_ville_a_inserer_en_anglais.get(), indice_du_pays_selectionne) == True:

					#
					horloge_monde.insertion_d_une_ville_dans_la_base_concernant_les_pays_a_plusieurs_timezones_dans_le_cas_d_equivalence_entre_nom_de_la_ville_et_nom_du_timezone(self.saisie_de_la_ville_a_inserer_en_francais.get(), self.saisie_de_la_ville_a_inserer_en_anglais.get(), str(indice_du_pays_selectionne))

					#
					if self.language_utilise_dans_la_fenetre == 0:

						#
						contenu_textuel_du_texte_a_dire_par_eSpeak_en_tant_qu_indication_du_succes_de_l_insertion_de_la_ville_dans_la_base_de_donnees = "The city " + self.saisie_de_la_ville_a_inserer_en_anglais.get() + " located in the country named " + self.liste_des_pays.get() + " has been inserted successfully"

						#
						identifiant_en_lettres_de_la_langue_uttilisee = "en"

					#
					else:

						#
						contenu_textuel_du_texte_a_dire_par_eSpeak_en_tant_qu_indication_du_succes_de_l_insertion_de_la_ville_dans_la_base_de_donnees = "La ville " + self.saisie_de_la_ville_a_inserer_en_francais.get() + " située dans le pays nommé " + self.liste_des_pays.get() + " a été insérée avec succès"

						#
						identifiant_en_lettres_de_la_langue_uttilisee = "fr"

				#Sinon...
				else:

					#
					horloge_monde.insertion_d_une_ville_dans_la_base(self.saisie_de_la_ville_a_inserer_en_francais.get(), self.saisie_de_la_ville_a_inserer_en_anglais.get(), indice_du_timezone_selectionne, indice_du_pays_selectionne)

					#
					if self.language_utilise_dans_la_fenetre == 0:


						#
						contenu_textuel_du_texte_a_dire_par_eSpeak_en_tant_qu_indication_du_succes_de_l_insertion_de_la_ville_dans_la_base_de_donnees = "The city " + self.saisie_de_la_ville_a_inserer_en_anglais.get() + " located in the country named " + self.liste_des_pays.get() + " has been inserted successfully"

						#
						identifiant_en_lettres_de_la_langue_uttilisee = "en"

					#
					else:

						#
						contenu_textuel_du_texte_a_dire_par_eSpeak_en_tant_qu_indication_du_succes_de_l_insertion_de_la_ville_dans_la_base_de_donnees = "La ville " + self.saisie_de_la_ville_a_inserer_en_francais.get() + " située dans le pays nommé " + self.liste_des_pays.get() + " a été insérée avec succès"

						#
						identifiant_en_lettres_de_la_langue_uttilisee = "fr"

				#
				subprocess.call(["espeak", "-v" + identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", contenu_textuel_du_texte_a_dire_par_eSpeak_en_tant_qu_indication_du_succes_de_l_insertion_de_la_ville_dans_la_base_de_donnees])

			#
			except:

				#
				if self.language_utilise_dans_la_fenetre == 0:

					#
                                        contenu_textuel_du_texte_a_dire_par_eSpeak_en_tant_qu_indication__d_une_ville_dans_la_base_de_donnees_pour_une_erreur_non_traitee = "Error: Insertion could not be done properly"

                                        #
                                        identifiant_en_lettres_de_la_langue_uttilisee = "en"

				#
				else:

					#
					contenu_textuel_du_texte_a_dire_par_eSpeak_en_tant_qu_indication__d_une_ville_dans_la_base_de_donnees_pour_une_erreur_non_traitee = "Erreur: L'insertion n'a pas pu se faire corretement"

					#
                                        identifiant_en_lettres_de_la_langue_uttilisee = "fr"

				#
				subprocess.call(["espeak", "-v" + identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", contenu_textuel_du_texte_a_dire_par_eSpeak_en_tant_qu_indication__d_une_ville_dans_la_base_de_donnees_pour_une_erreur_non_traitee])

		#Sinon, dans le cas contraire...
		else:

			#
			if self.language_utilise_dans_la_fenetre == 0:

				#
				contenu_textuel_du_texte_a_dire_par_eSpeak_en_tant_qu_indication__d_une_ville_dans_la_base_de_donnees_pour_une_erreur_non_traitee = "Error: Either the city is already filled, or it is not valid, the time zone indicated does not correspond to the indicated country"

				#
				identifiant_en_lettres_de_la_langue_uttilisee = "en"

			#
			else:

				#
				contenu_textuel_du_texte_a_dire_par_eSpeak_en_tant_qu_indication__d_une_ville_dans_la_base_de_donnees_pour_une_erreur_non_traitee = "Erreur: Soit la ville est déjà renseignée, soit celle-ci n'est pas valide, soit le fuseau horaire indiqué ne correspond pas au pays indiqué"

				#
				identifiant_en_lettres_de_la_langue_uttilisee = "fr"

			#
                        subprocess.call(["espeak", "-v" + identifiant_en_lettres_de_la_langue_uttilisee, "-s", "20", contenu_textuel_du_texte_a_dire_par_eSpeak_en_tant_qu_indication__d_une_ville_dans_la_base_de_donnees_pour_une_erreur_non_traitee])

                #
                self.fenetre.destroy()
