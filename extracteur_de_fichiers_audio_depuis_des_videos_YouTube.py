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

#Cette classe permet de définir une interface graphique pour extraire les fichiers audio depuis YouTube à partir de l'id de la video passée en paramétre
class Extracteur_de_fichiers_audio_depuis_YouTube(Frame):

	#Définition du constructeur de la classe Extracteur_de_fichiers_audio_depuis_YouTube
	def __init__(self, fenetre, langue_utilisee, width_fenetre_de_conf, height_fenetre_de_conf):

		#Appel au constructeur de la classe parente
                Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)

		#
		self.label_d_indication_de_renseignement_de_l_identifiant_de_la_video_YouTube_pour_extraction = Label(fenetre, text = "Entrer ici l'identifiant de la video YouTube pour extraction de son fichier audio: ")

		#
		self.label_d_indication_de_renseignement_de_l_identifiant_de_la_video_YouTube_pour_extraction.pack()

		#
		self.label_pour_indication_et_exemple_de_renseignement_de_l_identifiant_de_la_video_YouTube_pour_extraction = Label(fenetre, text = "P.ex: Dans l'URL https://www.youtube.com/watch?v=8kke47am23iop, entrer 8kke47am23iop")

		#
		self.label_pour_indication_et_exemple_de_renseignement_de_l_identifiant_de_la_video_YouTube_pour_extraction.pack()

		#
		self.variable_de_renseignement_de_l_identifiant_de_la_video_YouTube_choisie = StringVar()

		#
		self.entree_texte_d_indication_de_renseignement_de_l_identifiant_de_la_video_YouTube_pour_extraction = Entry(fenetre, textvariable = self.variable_de_renseignement_de_l_identifiant_de_la_video_YouTube_choisie)

		#
		self.entree_texte_d_indication_de_renseignement_de_l_identifiant_de_la_video_YouTube_pour_extraction.pack()

		#
		self.bouton_de_validation_de_l_identifiant_concernant_la_video_YouTube_pour_extraction = Button(fenetre, text = "Valider le choix effectué", command = self.validation_du_choix_effectue)

		#
		self.bouton_de_validation_de_l_identifiant_concernant_la_video_YouTube_pour_extraction.pack()

		#
		self.label_d_indication_du_titre_de_la_video_YouTube_pour_extraction = Label(fenetre, text = "Titre de la video YouTube pour extraction")

		#
		self.label_d_indication_du_titre_de_la_video_YouTube_pour_extraction.pack()

		#
		self.label_d_indication_de_la_duree_de_la_video_YouTube_pour_extraction = Label(fenetre, text = "Durée de la video YouTube pour extraction")

		#
		self.label_d_indication_de_la_duree_de_la_video_YouTube_pour_extraction.pack()

		#
		self.label_d_indication_de_l_url_de_l_image_de_presentation_de_la_video_YouTube_pour_extraction = Label(fenetre, text = "Image de la video YouTube pour extraction")

		#
		self.label_d_indication_de_l_url_de_l_image_de_presentation_de_la_video_YouTube_pour_extraction.pack()

		#
		self.label_d_indication_de_renseignement_du_nom_du_single_a_inserer_dans_la_base = Label(fenetre, text = "Entrer le nom souhaité pour le single à enregistrer: ")

		#
		self.label_d_indication_de_renseignement_du_nom_du_single_a_inserer_dans_la_base.pack()

		#
		self.variable_de_renseignement_du_nom_du_single_a_inserer_dans_la_base = StringVar()

		#
		self.entree_texte_d_indication_de_renseignement_du_nom_du_single_a_inserer_dans_la_base = Entry(fenetre, textvariable = self.variable_de_renseignement_du_nom_du_single_a_inserer_dans_la_base, state = "disabled")

		#
		self.entree_texte_d_indication_de_renseignement_du_nom_du_single_a_inserer_dans_la_base.pack()

		#
                self.label_d_indication_de_renseignement_du_nom_de_l_auteur_du_single_a_inserer_dans_la_base = Label(fenetre, text = "Entrer le nom de l'auteur du single à enregistrer: ")

                #
                self.label_d_indication_de_renseignement_du_nom_de_l_auteur_du_single_a_inserer_dans_la_base.pack()

                #
                self.variable_de_renseignement_du_nom_de_l_auteur_du_single_a_inserer_dans_la_base = StringVar()

                #
                self.entree_texte_d_indication_de_renseignement_du_nom_de_l_auteur_du_single_a_inserer_dans_la_base = Entry(fenetre, textvariable = self.variable_de_renseignement_du_nom_de_l_auteur_du_single_a_inserer_dans_la_base, state = "disabled")

                #
                self.entree_texte_d_indication_de_renseignement_du_nom_de_l_auteur_du_single_a_inserer_dans_la_base.pack()

		#
		self.label_d_indication_du_pays_d_origine_du_single_a_inserer_dans_la_base = Label(fenetre, text = "Sélectionner le pays d'origine du single à enregistrer: ") 

		#
		self.label_d_indication_du_pays_d_origine_du_single_a_inserer_dans_la_base.pack()

		#
		self.liste_des_pays_pour_renseigner_le_pays_d_origine_du_single_a_inserer_dans_la_base = horloge_monde.retour_des_pays_enregistres_dans_la_base(fenetre, langue_utilisee, "disabled")

		#
		self.liste_des_pays_pour_renseigner_le_pays_d_origine_du_single_a_inserer_dans_la_base.pack()

		#
		self.canvas_d_affichage_de_l_image_de_presentation_de_la_video_YouTube_pour_extraction = Canvas(fenetre)

		#
		self.canvas_d_affichage_de_l_image_de_presentation_de_la_video_YouTube_pour_extraction.pack()

		#
		self.label_d_indication_de_l_etat_du_processus_d_extraction_du_fichier_audio_depuis_la_video_YouTube = Label(fenetre, text = "Choix pas encore effectué !!!!")

		#
		self.label_d_indication_de_l_etat_du_processus_d_extraction_du_fichier_audio_depuis_la_video_YouTube.pack()

		#
		self.bouton_de_demarrage_du_telechargement_de_la_video_YouTube_pour_extraction = Button(fenetre, text = "Télécharger le fichier audio", command = self.telechargement_du_fichier_audio_depuis_YouTube)

		#
		self.bouton_de_demarrage_du_telechargement_de_la_video_YouTube_pour_extraction.pack()

		#
		self.fenetre = fenetre

		#
		self.video_YouTube_a_partir_duquel_extraire_le_fichier_audio = None

		#
		self.choix_valide = False

	#
	def validation_du_choix_effectue(self):

		#
		try:

			#
			self.identifiant_de_la_video_YouTube_renseignee_dans_le_widget_Entry = self.variable_de_renseignement_de_l_identifiant_de_la_video_YouTube_choisie.get()

			#
			self.video_YouTube_a_partir_duquel_extraire_le_fichier_audio = pytube.YouTube("https://www.youtube.com/watch?v=" + self.identifiant_de_la_video_YouTube_renseignee_dans_le_widget_Entry)

			#
			self.label_d_indication_du_titre_de_la_video_YouTube_pour_extraction.config(text = self.video_YouTube_a_partir_duquel_extraire_le_fichier_audio.title)

			#
			self.label_d_indication_de_la_duree_de_la_video_YouTube_pour_extraction.config(text = self.video_YouTube_a_partir_duquel_extraire_le_fichier_audio.length + " secondes")

			#
			self.label_d_indication_de_l_url_de_l_image_de_presentation_de_la_video_YouTube_pour_extraction.config(text = self.video_YouTube_a_partir_duquel_extraire_le_fichier_audio.thumbnail_url)

			#
			reponse_de_la_requete_de_recuperation_de_l_image = requests.get(self.video_YouTube_a_partir_duquel_extraire_le_fichier_audio.thumbnail_url)

			#
			donnees_relatives_a_l_image = reponse_de_la_requete_de_recuperation_de_l_image.content

			#
			image_prete_a_l_affichage = ImageTk.PhotoImage(Image.open(BytesIO(donnees_relatives_a_l_image)))

			#
			self.canvas_d_affichage_de_l_image_de_presentation_de_la_video_YouTube_pour_extraction.create_image(50, 10, image = image_prete_a_l_affichage, anchor = NW)

			#
			self.choix_valide = True

			#
			self.label_d_indication_de_l_etat_du_processus_d_extraction_du_fichier_audio_depuis_la_video_YouTube.config(text = "Prêt pour commencer la processus de téléchargement et d'extraction !!!!")

			#
			self.entree_texte_d_indication_de_renseignement_du_nom_du_single_a_inserer_dans_la_base.config(state = "normal")

			#
			self.entree_texte_d_indication_de_renseignement_du_nom_de_l_auteur_du_single_a_inserer_dans_la_base.config(state = "normal")

			#
			self.liste_des_pays_pour_renseigner_le_pays_d_origine_du_single_a_inserer_dans_la_base.config(state = "readonly")

			#
			showinfo("Validation effectuée correctement"," Le choix de la video YouTube à partir duquel extraire le fichier audio a été enregistré avec succès !!!!")

		#
		except pytube.exceptions.LiveStreamError:

			#
			showerror("Erreur dans le choix effectué", "Erreur: La vidéo YouTube choisie à partir duquel extraire le fichier audio est un direct !!!!")

		#
		except pytube.exceptions.RegexMatchError:

			#
			showerror("Erreur dans l'identifiant renseigneé", "Erreur: L'identifiant que vous avez renseigné n'est pas valide !!!!")

		#
		except pytube.exceptions.VideoUnavailable:

			#
			showerror("Erreur dans le choix effectué", "Erreur: La vidéo YouTube choisie à partir duquel extraire le fichier audio est indisponible !!!!")

	#
	def telechargement_du_fichier_audio_depuis_YouTube(self):

		#
		try:

			#
                        self.label_d_indication_de_l_etat_du_processus_d_extraction_du_fichier_audio_depuis_la_video_YouTube.config(text = "Procéssus de téléchargement et d'extraction en cours...")

			#
			reponse_donnee_par_l_utilisateur = askyesno("Question importante concernant le procéssus de téléchargement et d'extraction","Le procéssus de téléchargement et d'extraction du fichier audio depuis la vidéo YouTube choisie risque d'être un peu long. Il est impossible d'intérrompre le procéssus dès son démarrage. En conséquence: Etes-vous sûr de votre choix ET aurez-vous la patiente d'attendre la fin du procéssus ?")

			#Dans le cas ou la variable reponse_donnee_par_l_utilisateur contient la valeur booléenne True (L'utilisateur a donné son accord à l'extraction du fichier audio depuis la video YouTube renseignée depuis son identifiant), alors...
			if reponse_donnee_par_l_utilisateur == True:

				#
				if horloge_monde.verification_de_l_existance_d_un_titre_de_single_similaire_dans_la_base(self.identifiant_de_la_video_YouTube_renseignee_dans_le_widget_Entry) == True:

					#
					showerror("Erreur pour cause de possibilité d'un doublon","Erreur: Un single extrait depuis la vidéo YouTube renseignée existe déjà. Téléchargement et extraction refusés")

				#
				else:

					#
					if int(self.video_YouTube_a_partir_duquel_extraire_le_fichier_audio.length) <= 300:

						#
						if horloge_monde.verification_de_la_validite_d_une_chaine_de_caracteres_passee_en_parametre(self.variable_de_renseignement_du_nom_du_single_a_inserer_dans_la_base.get()) == True and horloge_monde.verification_de_la_validite_d_une_chaine_de_caracteres_passee_en_parametre(self.variable_de_renseignement_du_nom_de_l_auteur_du_single_a_inserer_dans_la_base.get()) == True:

							#
							nom_du_fichier_audio_extrait_depuis_YouTube = horloge_monde.remplacement_des_espaces_par_des_underscores(self.variable_de_renseignement_du_nom_du_single_a_inserer_dans_la_base.get())

							#
							nom_du_fichier_audio_extrait_depuis_YouTube = horloge_monde.remplacement_des_espaces_par_des_underscores(nom_du_fichier_audio_extrait_depuis_YouTube)

							#
							self.video_YouTube_a_partir_duquel_extraire_le_fichier_audio.streams.filter(only_audio = True).first().download(output_path = "./media", filename = nom_du_fichier_audio_extrait_depuis_YouTube)

							#
							subprocess.call(["ffmpeg", "-loglevel", "quiet", "./media/" + nom_du_fichier_audio_extrait_depuis_YouTube + ".wav", "-i", "./media/" + nom_du_fichier_audio_extrait_depuis_YouTube + ".mp4"], shell = False)

							#
							os.remove("./media/" + nom_du_fichier_audio_extrait_depuis_YouTube  + ".mp4")

							#
							indice_du_pays_selectionne = int(self.liste_des_pays_pour_renseigner_le_pays_d_origine_du_single_a_inserer_dans_la_base.current())

							#
							indice_du_pays_selectionne = indice_du_pays_selectionne + 2

							#
							horloge_monde.enregistrement_du_fichier_audio_extrait_depuis_la_video_YouTube_renseignee_dans_la_base(self.variable_de_renseignement_du_nom_du_single_a_inserer_dans_la_base.get(), self.variable_de_renseignement_du_nom_de_l_auteur_du_single_a_inserer_dans_la_base.get(), str(indice_du_pays_selectionne), nom_du_fichier_audio_extrait_depuis_YouTube + ".wav", self.identifiant_de_la_video_YouTube_renseignee_dans_le_widget_Entry)

							#
							showinfo("Téléchargement et extraction effectués correctement","Le fichier audio a été extrait avec succès de la vidéo YouTube !!!!")

							#
							self.fenetre.destroy()

						#Sinon...
						else:

							#
							showerror("Erreur liée au titre du single et/ou au nom de l'auteur du single renseignés", "Erreur: Le titre du single et le nom de l'auteur du single renseignés doivent obligatoirement être des caractères alphanumériques (tous les chiffres et les lettres sans accents ni cédilles), des espaces, des tirets (-) ou des underscores (_)")

							#
							self.label_d_indication_de_l_etat_du_processus_d_extraction_du_fichier_audio_depuis_la_video_YouTube.config(text = "Prêt pour commencer le procéssus de téléchargement et d'extraction !!!!")

					#Sinon...
					else:

						#
						showerror("Erreur liée à la durée de la video YouTube", "Erreur: la durée de la video YouTube à partir duquel extraire le fichier audio est supérieur aux 300 secondes (5 minutes) maximales autorisées !!!!")

						#
						self.label_d_indication_de_l_etat_du_processus_d_extraction_du_fichier_audio_depuis_la_video_YouTube.config(text = "Prêt pour commencer le procéssus de téléchargement et d'extraction !!!!")

			#Sinon...
			else:

				#
				self.label_d_indication_de_l_etat_du_processus_d_extraction_du_fichier_audio_depuis_la_video_YouTube.config(text = "Prêt pour commencer le procéssus de téléchargement et d'extraction !!!!")

				#
				return

		#
                except:

                        #
                        showerror("Erreur dans l'extraction et/ou le téléchargement", "Erreur: Une erreur est survenue. Veuillez réessayer ultérieurement !!!!")

                        #
                        self.fenetre.destroy()

#
def initialisation_et_affichage_de_l_Extracteur_de_fichiers_audio_depuis_YouTube():

	#
        fenetre = Tk()

        #
        fenetre.title("Test de l'extracteur de fichiers audio depuis YouTube")

	#
	fenetre.resizable(False, False)

	#
	test_du_lecteur_de_l_extracteur_de_fichiers_audio_telecharges_depuis_YouTube = Extracteur_de_fichiers_audio_depuis_YouTube(fenetre, fenetre.winfo_screenwidth(), fenetre.winfo_screenheight())

	#
	test_du_lecteur_de_l_extracteur_de_fichiers_audio_telecharges_depuis_YouTube.mainloop()

#Bloc de test du module
if __name__ == '__main__':

	#
	initialisation_et_affichage_de_l_Extracteur_de_fichiers_audio_depuis_YouTube()
