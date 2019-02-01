# smart_connected_alarm_clock
Ceci est un projet de reveil intélligent et connecté.

Ce reveil permet:

* d'afficher l'heure et la date pour tous les fuseaux horaires du monde,
* d'afficher la météo dans la ville courante (la ville qui est affichée),
* d'insérer une nouvelle ville dans la base de données,
* de configurer le reveil pour qu'il sonne à l'heure, la minute, et la seconde renseignée dans la ville courante,
* de télécharger et de lire des fichiers audio depuis YouTube.

Pour fonctionner correctement, ce reveil necessite la base registre_des_timezones_des_villes_et_des_pays instalée en tant que base sqlite grâce au script sql script_de_creation_et_mise_en_place_des_tables.sql.
Il necessite aussi le langage Python installé et configué correctement, ainsi que les modules suivants: pygame, pyowm, pytube, pytz, datetime, pyaudio, et SpeechRecognition.
