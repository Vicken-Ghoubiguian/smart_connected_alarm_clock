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

#Cette classe permet de définir une interface graphique pour choisir un fichier audio téléchargé depuis YouTube pour suppréssion
class Suppression_de_musiques_telechargees_depuis_YouTube(Frame):

        #Définition du constructeur de la classe Extracteur_de_fichiers_audio_depuis_YouTube
        def __init__(self, fenetre, langue_utilisee, width_fenetre_de_conf, height_fenetre_de_conf):

                #Appel au constructeur de la classe parente
                Frame.__init__(self, fenetre, width = width_fenetre_de_conf, height = height_fenetre_de_conf)

