--CREATION DE TOUTES LES TABLES NECESSAIRES DANS LE MODELE--
CREATE TABLE IF NOT EXISTS timezone(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	timezone VARCHAR(100) NOT NULL,
	pays INTEGER NOT NULL,
	code_du_pays_ou_de_la_region VARCHAR(100) NOT NULL,
	FOREIGN KEY (pays) REFERENCES pays(id)
);

CREATE TABLE IF NOT EXISTS pays(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	pays_en_fr VARCHAR(100) NOT NULL,
	pays_en_en VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS ville(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	ville_en_fr VARCHAR(100) NOT NULL,
	ville_en_en VARCHAR(100) NOT NULL,
	pays INTEGER NOT NULL,
	timezone INTEGER NOT NULL,
	FOREIGN KEY (pays) REFERENCES pays(id),
	FOREIGN KEY (timezone) REFERENCES timezone(id)
);

CREATE TABLE IF NOT EXISTS Single(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nom_du_single VARCHAR(100) NOT NULL,
        nom_de_l_auteur VARCHAR(100) NOT NULL,
        chemin_d_accee VARCHAR(100) NOT NULL,
        pays INTEGER NOT NULL,
	identifiant_YouTube_de_la_video_d_origine VARCHAR(100) NOT NULL,
        FOREIGN KEY (pays) REFERENCES pays(id)
);

CREATE TABLE IF NOT EXISTS Reveil(
	ville INTEGER NOT NULL,
	timezone INTEGER NOT NULL,
	heure INTEGER NOT NULL,
	minute INTEGER NOT NULL,
	seconde INTEGER NOT NULL,
	frequence INTEGER NOT NULL,
	single_choisi INTEGER NOT NULL,
	est_active INTEGER NOT NULL,
	FOREIGN KEY (ville) REFERENCES ville(id),
	FOREIGN KEY (timezone) REFERENCES timezone(id),
	FOREIGN KEY (single_choisi) REFERENCES Single(id)
);

CREATE TABLE IF NOT EXISTS Mise_a_jour(
	ville INTEGER NOT NULL,
	timezone INTEGER NOT NULL,
	heure INTEGER NOT NULL,
	minute INTEGER NOT NULL,
	seconde INTEGER NOT NULL,
	FOREIGN KEY (ville) REFERENCES ville(id),
	FOREIGN KEY (timezone) REFERENCES timezone(id)
);

--INSERTION DES DONNEES RELATIFS AUX PAYS RECONNUS PAR L'ONU (PAR ORDRE ALPHABETIQUE) DANS LA TABLE PAYS--
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("None", "None");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Afrique du Sud", "Republic of South Africa");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République islamique d'Afghanistan", "Islamic Republic of Afhanistan");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Albanie", "Republic of Albania");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République algeriénne démocratique et populaire", "People's Democratic Republic of Algeria");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République fédérale d'Allemagne", "Federal Republic of Germany");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Principauté d'Andorre", "Principality of Andorra");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Angola", "Republic of Angola");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Antigua-et-Barbuda", "Antigua and Barbuda");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume d'Arabie saoudite", "Kingdom of Saudi Arabia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République argentine", "Argentine Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Armenie", "Republic of Armenia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Commonwealth d'Australie", "Commonwealth of Australia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Autriche", "Republic of Austria");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Azerbaidjan", "Republic of Azerbaijan");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Commonwealth des Bahamas", "Commonwealth of The Bahamas");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume de Bahrein", "Kingdom of Bahrain");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République populaire du Bangladesh", "People's Republic of Bangladesh");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Barbade", "Barbados");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume de Belgique", "Kingdom of Belgium");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Belize", "Belize");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Benin", "Republic of Benin");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume du Bhoutan", "Kingdom of Bhutan");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Biélorussie", "Republic of Byelorussia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de l'Union du Myanmar", "Republic of the Union of Myanmar");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etat plurinational de Bolivie", "Plurinational State of Bolivia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Bosnie-Herzegovine", "Bosnia-Herzegovina");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Botswana", "Republic of Botswana");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République fédérative du Brésil", "Federative Republic of Brazil");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Negara Brunei Darussalam", "Nation of Brunei, the Abode of Peace");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Bulgarie", "Republic of Bulgaria");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Burkina Faso", "Burkina Faso");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Burundi", "Republic of Burundi");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume du Cambodge", "Kingdom of Cambodia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Cameroun", "Republic of Cameroon");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Dominion du Canada", "Dominion of Canada");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Cap-Vert", "Republic of Cabo Verde");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Chili", "Republic of Chile");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République populaire de Chine", "People's Republic of China");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Chypre", "Republic of Cyprus");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Colombie", "Republic of Colombia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Union des Comores", "Union of the Comoros");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République populaire et démocratique de Corée", "Democratic People's Republic of Korea");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Corée", "Republic of Korea");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Costa Rica", "Republic of Costa Rica");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Côte d'Ivoire", "Republic of Cote d'Ivoire");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Croatie", "Republic of Croatia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Cuba", "Republic of Cuba");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume de Danemark", "Kingdom of Denmark");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Djibouti", "Republic of Djibouti");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Commonwealth de la Dominique", "Commonwealth of Dominica");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République arabe d Egypte", "Arab Republic of Egypt");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Emirats arabes unis", "United Arab Emirates");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Equateur", "Republic of Ecuador");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etat d'Erythrée", "State of Eritrea");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume d'Espagne", "Kingdom of Spain");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Estonie", "Republic of Estonia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etats-Unis d Amerique", "United States of America");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République démocratique fédérale d'Ethiopie", "Federal Democratic Republic of Ethiopia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République des Fidji", "Republic of Fidji");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Finlande", "Republic of Finland");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République française", "French Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République gabonaise", "Gabonese Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Gambie", "Republic of the Gambia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Géorgie", "Georgia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Ghana", "Republic of Ghana");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Republique hellénique", "Hellenic Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Grenade", "Grenada");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Guatemala", "Republic of Guatemala");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Guinée", "Republic of Guinea");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Guinée équatoriale", "Republic of Equatorial Guinea");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Guinée-Bissau", "Republic of Guinea-Bissau");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République coopérative du Guyana", "Co-operative Republic of Guyana");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Haiti", "Republic of Haiti");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Honduras", "Republic of Honduras");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Hongrie", "Hungary");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République des Iles Marshall", "Republic of the Marshall Islands");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de l'Inde", "Republic of India");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Indonesie", "Republic of Indonesia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Irak", "Republic of Iraq");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République islamique d'Iran", "Islamic Republic of Iran");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Irlande", "Republic of Ireland");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Islande", "Republic of Iceland");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etat d'Israël", "State of Israel");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République italienne", "Italian Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Jamaïque", "Jamaica");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Empire du Japon", "Empire of Japan");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume hachémite de Jordanie", "Hashemite Kingdom of Jordan");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Kazakhstan", "Republic of Kazakhstan");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Kenya", "Republic of Kenya");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République kirghize", "Kyrgyz Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République des kiribati", "Republic of Kiribati");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etat du Koweit", "State of Kuwait");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République démocratique populaire lao", "Lao People s Democratic Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume du Lesotho", "Kingdom of Lesotho");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Lettonie", "Republic of Latvia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République libanaise", "Lebanese Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Liberia", "Republic of Liberia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etat de Libye", "State of Libya");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Principauté de Liechtenstein", "Principality of Liechtenstein");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Lituanie", "Republic of Lithuania");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Grand-Duché de Luxembourg", "Grand Duchy of Luxembourg");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Macédoine", "Republic of Macedonia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Madagascar", "Republic of Madagascar");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Fédération de Malaisie", "Republic of Malaysia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Malawi", "Republic of Malawi");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République des Maldives", "Republic of Maldives");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Mali", "Republic of Mali");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Malte", "Republic of Malta");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume du Maroc", "Kingdom of Morocco");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Maurice", "Republic of Mauritius");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République islamique de Mauritanie", "Islamic Republic of Mauritania");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etats-Unis mexicains", "United Mexican States");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etats fédérés de Micronésie", "Federated States of Micronesia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Moldavie", "Republic of Moldavia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Principauté de Monaco", "Principality of Monaco");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Mongolie", "Mongolia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Monténégro", "Montenegro");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Mozambique", "Republic of Mozambique");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Namibie", "Republic of Namibia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Nauru", "Republic of Nauru");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République démocratique fédérale du Népal", "Democratic Republic of Nepal");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Nicaragua", "Republic of Nicaragua");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Niger", "Republic of Niger");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République fédérale du Nigeria", "Federal Republic of Nigeria");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES('Antarctique', 'Antarctica');
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume de Norvège", "Kingdom of Norway");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Nouvelle-Zélande", "New Zeland");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Sultanat d'Oman", "Sultanate of Oman");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Ouganda", "Republic of Uganda");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République d'Ouzbekistan", "Republic of Uzbekistan");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République islamique du Pakistan", "Islamic Republic of Pakistan");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République des Palaos", "Republic of Palau");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etat de Palestine", "State of Palestine");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Panama", "Republic of Panama");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etat indépendant de Papouasie-Nouvelle-Guinée", "Independent State of Papua New Guinea");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Paraguay", "Republic of Paraguay");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume des Pays-Bas", "Kingdom of Netherlands");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Pérou", "Republic of Peru");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République des Philippines", "Republic of the Philippines");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Pologne", "Republic of Poland");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République portugaise", "Portuguese Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etat du Qatar", "State of Qatar");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République centrafricaine", "Central African Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République démocratique du Congo", "Democratic Republic of the Congo");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République dominicaine", "Dominican Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Congo", "Republic of the Congo");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République tchèque", "Czech Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Roumanie", "Roumania");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume-Uni de Grande-Bretagne et d'Irlande du Nord", "United Kingdom of Great Britain and Northem Ireland");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Fédération de Russie", "Russian Federation");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Rwanda", "Republic of Rwanda");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Fédération de Saint-Christophe-et-Niévès", "Federation of Saint Christopher and Nevis");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Saint-Vincent-et-les-Grenadines", "Saint Vincent and the Grenadines");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Sainte-Lucie", "Saint Lucia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Saint-Marin", "Republic of San Marino");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Iles Salomon", "Solomon Islands");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Salvador", "Republic of El Salvador");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etat independant des Samoa", "Independant State of Samoa");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République démocratique de Sao Tomé-et-Principe", "Democratic Republic of Sao Tome and Principe");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Sénégal", "Republic of Senegal");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Serbie", "Republic of Serbia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République des Seychelles", "Republic of Seychelles");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Sierra Leone", "Republic of Sierra Leone");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Singapour", "Republic of Singapore");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République slovaque", "Slovak Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Slovénie", "Republic of Slovenia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République fédérale de Somalie", "Federal Republic of Somalia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Soudan", "Republic of Sudan");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Soudan du sud", "Republic of South Sudan");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République démocratique socialiste du Sri Lanka", "Democratic Socialist Republic of Sri Lanka");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume de Suède", "Kingdom of Sweden");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Confédération suisse", "Swiss Confederation");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Suriname", "Republic of Suriname");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume du Swaziland", "Kingdom of Eswatini");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République arabe syrienne", "Syrian Arab Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Tadjikistan", "Republic of Tadjikistan");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République unie de Tanzanie", "United Republic of Tanzania");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Chine (Taiwan)", "Republic of China (Taiwan)");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Tchad", "Republic of Chad");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume de Thaïlande", 'Kingdom of Thailand');
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République démocratique du Timor oriental", "Democratic Republic of Timor-Leste");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République togolaise", "Togolese Republic");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Royaume des Tonga", "Kingdom of Tonga");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Trinité-et-Tobago", "Republic of Trinidad and Tobago");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République tunisienne", "Republic of Tunisia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Turkmenistan", "Republic of Turkmenistan");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Turquie", "Republic of Turkey");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etat des Tuvalu", "State of Tuvalu");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Ukraine", "Ukraine");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République orientale de l'Uruguay", "Oriental Republic of Uruguay");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Vanuatu", "Republic of Vanuatu");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("Etat de la Cité du Vatican", "Vatican City State");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République bolivarienne du Venezuela", "Bolivarian Republic of Venezuela");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République socialiste du Viêt Nam", "Socialist Republic of Vietnam");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Yemen", "Republic of Yemen");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République de Zambie", "Republic of Zambia");
INSERT INTO pays(pays_en_fr, pays_en_en) VALUES("République du Zimbabwe", "Republic of Zimbabwe");

--INSERTION DES DONNEES REALTIFS AUX TIMEZONES (CANONIQUES ET ALIAS) DANS LA TABLE TIMEZONE--
--POUR L'AFRIQUE--
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Abidjan', 46, 'CI');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Accra', 66, 'GH');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Addis_Ababa', 59, 'ET');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Algiers', 5, 'DZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Asmara', 55, 'ER');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Bamako', 108, 'ML');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Bangui', 144, 'CF');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Banjul', 64, 'GM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Bissau', 72, 'GW');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Blantyre', 106, 'MW');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Brazzaville', 147, 'CG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Bujumbura', 33, 'BI');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Cairo', 52, 'EG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Casablanca', 110, 'MA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Ceuta', 56, 'ES');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Conakry', 70, 'GN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Dakar', 161, 'SN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Dar_es_Salaam', 178, 'TZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Djibouti', 50, 'DJ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Douala', 35, 'CM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/El_Aaiun', 110, 'EH');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Freetown', 164, 'SL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Gaborone', 28, 'BW');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Harare', 198, 'ZW');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Johannesburg', 2, 'ZA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Juba', 170, 'SS');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Kampala', 130, 'UG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Khartoum', 169, 'SD');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Kigali', 152, 'RW');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Kinshasa', 145, 'CD');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Lagos', 125, 'NG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Libreville', 63, 'GA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Lome', 183, 'TG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Luanda', 8, 'AO');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Lubumbashi', 145, 'CD');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Lusaka', 197, 'ZM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Malabo', 71, 'GQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Maputo', 119, 'MZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Maseru', 95, 'LS');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Mbabane', 175, 'SZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Mogadishu', 168, 'SO');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Monrovia', 98, 'LR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Nairobi', 90, 'KE');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Ndjamena', 180, 'TD');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Niamey', 124, 'NE');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Nouakchott', 112, 'MR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Ouagadougou', 32, 'BF');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Porto-Novo', 22, 'BJ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Sao_Tome', 160, 'ST');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Tripoli', 99, 'LY');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Tunis', 186, 'TN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Africa/Windhoek', 120, 'NA');

--POUR L'AMERIQUE--
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Adak', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Anchorage', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Anguilla', 150, 'AI');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Antigua', 9, 'AG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Araguaina', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Argentina/Buenos_Aires', 11, 'AR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Argentina/Catamarca', 11, 'AR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Argentina/Cordoba', 11, 'AR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Argentina/Jujuy', 11, 'AR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Argentina/La_Rioja', 11, 'AR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Argentina/Mendoza', 11, 'AR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Argentina/Rio_Gallegos', 11, 'AR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Argentina/Salta', 11, 'AR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Argentina/San_Juan', 11, 'AR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Argentina/San_Luis', 11, 'AR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Argentina/Tucuman', 11, 'AR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Argentina/Ushuaia', 11, 'AR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Aruba', 138, 'AW');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Asuncion', 137, 'PY');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Atikokan', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Bahia', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Bahia_Banderas', 113, 'MX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Barbados', 19, 'BB');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Belem', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Belize', 21, 'BZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Blanc-Sablon', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Boa_Vista', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Bogota', 41, 'CO');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Boise', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Cambridge_Bay', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Campo_Grande', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Cancun', 113, 'MX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Caracas', 194, 'VE');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Cayenne', 62, 'GF');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Cayman', 150, 'KY');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Chicago', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Chihuahua', 113, 'MX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Costa_Rica', 45, 'CR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Creston', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Cuiaba', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Curacao', 138, 'CW');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Danmarkshavn', 49, 'GL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Dawson', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Dawson_Creek', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Denver', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Detroit', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Dominica', 51, 'DM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Edmonton', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Eirunepe', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/El_Salvador', 158, 'SV');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Fort_Nelson', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Fortaleza', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Glace_Bay', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Godthab', 49, 'GL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Goose_Bay', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Grand_Turk', 150, 'TC');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Grenada', 68, 'GD');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Guadeloupe', 62, 'GP');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Guatemala', 69, 'GT');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Guayaquil', 54, 'EC');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Guyana', 73, 'GY');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Halifax', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Havana', 48, 'CU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Hermosillo', 113, 'MX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Indiana/Indianapolis', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Indiana/Knox', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Indiana/Marengo', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Indiana/Petersburg', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Indiana/Tell_City', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Indiana/Vevay', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Indiana/Vincennes', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Indiana/Winamac', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Inuvik', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Iqaluit', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Jamaica', 86, 'JM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Juneau', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Kentucky/Louisville', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Kentucky/Monticello', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Kralendijk', 138, 'BQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/La_Paz', 26, 'BO');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Lima', 139, 'PE');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Los_Angeles', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Lower_Princes', 138, 'SX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Maceio', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Managua', 123, 'NI');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Manaus', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Marigot', 62, 'MF');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Martinique', 62, 'MQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Matamoros', 113, 'MX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Mazatlan', 113, 'MX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Menominee', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Merida', 113, 'MX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Metlakatla', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Mexico_City', 113, 'MX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Miquelon', 62, 'PM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Moncton', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Monterrey', 113, 'MX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Montevideo', 191, 'UY');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Montserrat', 150, 'MS');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Nassau', 16, 'BS');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/New_York', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Nipigon', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Nome', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Noronha', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/North_Dakota/Beulah', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/North_Dakota/Center', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/North_Dakota/New_Salem', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Ojinaga', 113, 'MX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Panama', 135, 'PA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Pangnirtung', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Paramaribo', 174, 'SR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Phoenix', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Port_of_Spain', 185, 'TT');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Port-au-Prince', 74, 'HT');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Porto_Velho', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Puerto_Rico', 58, 'PR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Punta_Arenas', 38, 'CL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Rainy_River', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Rankin_Inlet', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Recife', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Regina', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Resolute', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Rio_Branco', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Santarem', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Santiago', 38, 'CL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Santo_Domingo', 146, 'DO');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Sao_Paulo', 29, 'BR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Scoresbysund', 49, 'GL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Sitka', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/St_Barthelemy', 62, 'BL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/St_Johns', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/St_Kitts', 153, 'KN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/St_Lucia', 155, 'LC');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/St_Thomas', 58, 'VI');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/St_Vincent', 154, 'VC');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Swift_Current', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Tegucigalpa', 75, 'HN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Thule', 49, 'GL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Thunder_Bay', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Tijuana', 113, 'MX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Toronto', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Tortola', 150, 'VG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Vancouver', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Whitehorse', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Winnipeg', 36, 'CA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Yakutat', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('America/Yellowknife', 36, 'CA');

--POUR L'ANTARTIQUE--
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Antarctica/Casey', 126, 'AQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Antarctica/Davis', 126, 'AQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Antarctica/DumontDUrville', 126, 'AQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Antarctica/Macquarie', 126, 'AQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Antarctica/Mawson', 126, 'AQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Antarctica/McMurdo', 126, 'AQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Antarctica/Palmer', 126, 'AQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Antarctica/Rothera', 126, 'AQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Antarctica/Syowa', 126, 'AQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Antarctica/Troll', 126, 'AQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Antarctica/Vostok', 126, 'AQ');

--POUR L'OCEAN ARCTIQUE--
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Arctic/Longyearbyen', 127, 'SJ');

--POUR L'ASIE--
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Aden', 196, 'YE');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Almaty', 89, 'KZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Amman', 88, 'JO');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Anadyr', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Aqtau', 89, 'KZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Aqtobe', 89, 'KZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Ashgabat', 187, 'TM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Atyrau', 89, 'KZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Baghdad', 80, 'IQ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Bahrain', 17, 'BH');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Baku', 15, 'AZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Bangkok', 181, 'TH');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Barnaul', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Beirut', 97, 'LB');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Bishkek', 91, 'KG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Brunei', 30, 'BN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Chita', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Choibalsan', 117, 'MN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Colombo', 171, 'LK');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Damascus', 176, 'SY');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Dhaka', 18, 'BD');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Dili', 182, 'TL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Dubai', 53, 'AE');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Dushanbe', 177, 'TJ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Famagusta', 40, 'CY');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Gaza', 134, 'PS');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Hebron', 134, 'PS');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Ho_Chi_Minh', 195, 'VN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Hong_Kong', 39, 'HK');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Hovd', 117, 'MN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Irkutsk', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Jakarta', 79, 'ID');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Jayapura', 79, 'ID');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Jerusalem', 84, 'IL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Kabul', 3, 'AF');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Kamchatka', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Karachi', 132, 'PK');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Kathmandu', 122, 'NP');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Khandyga', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Kolkata', 78, 'IN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Krasnoyarsk', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Kuala_Lumpur', 105, 'MY');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Kuching', 105, 'MY');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Kuwait', 93, 'KW');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Macau', 39, 'MO');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Magadan', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Makassar', 79, 'ID');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Manila', 140, 'PH');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Muscat', 129, 'OM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Novokuznetsk', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Novosibirsk', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Omsk', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Oral', 89, 'KZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Phnom_Penh', 34, 'KH');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Pontianak', 79, 'ID');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Pyongyang', 43, 'KP');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Qatar', 143, 'QA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Qyzylorda', 89, 'KZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Riyadh', 10, 'SA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Sakhalin', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Samarkand', 131, 'UZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Seoul', 44, 'KR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Shanghai', 39, 'CN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Singapore', 165, 'SG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Srednekolymsk', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Taipei', 179, 'TW');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Tashkent', 131, 'UZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Tbilisi', 65, 'GE');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Tehran', 81, 'IR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Thimphu', 23, 'BT');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Tokyo', 87, 'JP');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Tomsk', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Ulaanbaatar', 117, 'MN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Urumqi', 39, 'CN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Ust-Nera', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Vientiane', 94, 'LA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Vladivostok', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Yakutsk', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Yangon', 25, 'MM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Yekaterinburg', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Asia/Yerevan', 12, 'AM');

--POUR L'OCEAN ATLANTIQUE--
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Atlantic/Azores', 142, 'PT');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Atlantic/Bermuda', 150, 'BM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Atlantic/Canary', 56, 'ES');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Atlantic/Cape_Verde', 37, 'CV');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Atlantic/Faroe', 49, 'FO');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Atlantic/Madeira', 142, 'PT');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Atlantic/Reykjavik', 83, 'IS');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Atlantic/South_Georgia', 150, 'GS');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Atlantic/St_Helena', 150, 'SH');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Atlantic/Stanley', 150, 'FK');

--POUR L'AUSTRALIE--
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Australia/Adelaide', 13, 'AU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Australia/Brisbane', 13, 'AU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Australia/Broken_Hill', 13, 'AU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Australia/Currie', 13, 'AU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Australia/Darwin', 13, 'AU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Australia/Eucla', 13, 'AU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Australia/Hobart', 13, 'AU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Australia/Lindeman', 13, 'AU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Australia/Lord_Howe', 13, 'AU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Australia/Melbourne', 13, 'AU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Australia/Perth', 13, 'AU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Australia/Sydney', 13, 'AU');

--POUR L'UTC ET LE GMT--
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('UTC', 1, '0');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('GMT', 1, '0');

--POUR L'EUROPE--
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Amsterdam', 138, 'NL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Andorra', 7, 'AD');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Astrakhan', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Athens', 67, 'GR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Belgrade', 162, 'RS');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Berlin', 6, 'DE');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Bratislava', 166, 'SK');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Brussels', 20, 'BE');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Bucharest', 149, 'RO');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Budapest', 76, 'HU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Chisinau', 115, 'MD');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Copenhagen', 49, 'DK');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Dublin', 82, 'IE');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Gibraltar', 150, 'GI');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Helsinki', 61, 'FI');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Isle_of_Man', 150, 'IM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Istanbul', 188, 'TR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Kaliningrad', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Kiev', 190, 'UA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Kirov', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Lisbon', 142, 'PT');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Ljubljana', 167, 'SI');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/London', 150, 'GB');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Luxembourg', 102, 'LU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Madrid', 56, 'ES');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Malta', 109, 'MT');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Minsk', 24, 'BY');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Monaco', 116, 'MC');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Moscow', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Nicosia', 40, 'CY');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Oslo', 127, 'NO');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Paris', 62, 'FR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Podgorica', 118, 'ME');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Prague', 148, 'CZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Riga', 96, 'LV');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Rome', 85, 'IT');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Samara', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/San_Marino', 156, 'SM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Sarajevo', 27, 'BA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Saratov', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Simferopol', 190, 'UA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Skopje', 103, 'MK');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Sofia', 31, 'BG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Stockholm', 172, 'SE');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Tallinn', 57, 'EE');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Tirane', 4, 'AL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Ulyanovsk', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Uzhgorod', 190, 'UA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Vaduz', 100, 'LI');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Vatican', 193, 'VA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Vienna', 14, 'AT');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Vilnius', 101, 'LT');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Volgograd', 151, 'RU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Warsaw', 141, 'PL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Zagreb', 47, 'HR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Zaporozhye', 190, 'UA');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Europe/Zurich', 173, 'CH');

--POUR L'OCEAN INDIEN--
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Indian/Antananarivo', 104, 'MG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Indian/Chagos', 150, 'IO');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Indian/Christmas', 13, 'CX');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Indian/Cocos', 13, 'CC');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Indian/Comoro', 42, 'KM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Indian/Kerguelen', 62, 'TF');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Indian/Mahe', 163, 'SC');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Indian/Maldives', 107, 'MV');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Indian/Mauritius', 111, 'MU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Indian/Mayotte', 62, 'YT');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Indian/Reunion', 62, 'RE');

--POUR L'OCEAN PACIFIQUE--
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Apia', 159, 'WS');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Auckland', 128, 'NZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Bougainville', 136, 'PG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Chatham', 128, 'NZ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Chuuk', 114, 'FM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Easter', 38, 'CL');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Efate', 192, 'VU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Enderbury', 92, 'KI');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Fakaofo', 128, 'TK');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Fiji', 60, 'FJ');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Funafuti', 189, 'TV');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Galapagos', 54, 'EC');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Gambier', 62, 'PF');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Guadalcanal', 157, 'SB');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Guam', 58, 'GU');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Honolulu', 58, 'US');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Kiritimati', 92, 'KI');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Kosrae', 114, 'FM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Kwajalein', 77, 'MH');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Majuro', 77, 'MH');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Marquesas', 62, 'PF');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Midway', 58, 'UM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Nauru', 121, 'NR');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Norfolk', 13, 'NF');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Noumea', 62, 'NC');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Pago_Pago', 58, 'AS');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Palau', 133, 'PW');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Pitcairn', 150, 'PN');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Pohnpei', 114, 'FM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Port_Moresby', 136, 'PG');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Rarotonga', 128, 'CK');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Saipan', 58, 'MP');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Tahiti', 62, 'PF');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Tarawa', 92, 'KI');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Tongatapu', 184, 'TO');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Wake', 58, 'UM');
INSERT INTO timezone(timezone, pays, code_du_pays_ou_de_la_region) VALUES('Pacific/Wallis', 62, 'WF');

--INSERTION DES DONNEES REALTIFS AUX VILLES DANS LA TABLE VILLE--
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Perpignan', 'Perpignan', 62, 348);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Los Angeles', 'Los Angeles', 58, 134);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Ottawa', 'Ottawa', 36, 193);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('New York', 'New York', 58, 153);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Phoenix', 'Phoenix', 58, 164);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Moscou', 'Moscow', 151, 345);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Vladivostok', 'Vladivostok', 151, 288);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Séoul', 'Seoul', 44, 273);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Tokyo', 'Tokyo', 87, 282);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Pékin', 'Beijing', 39, 274);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Londres', 'London', 150, 339);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Canberra', 'Canberra', 13, 314);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Wellington', 'Wellington', 128, 386);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Santiago', 'Santiago', 38, 177);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Johannesburg', 'Johannesburg', 2, 25);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Windhoek', 'Windhoek', 120, 52);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Antananarivo', 'Antananarivo', 104, 374);
INSERT INTO ville(ville_en_fr, ville_en_en, pays, timezone) VALUES('Lima', 'Lima', 139, 133);

--INSERTION DANS LA TABLE REVEIL--
INSERT INTO Reveil(ville, timezone, heure, minute, seconde, frequence, single_choisi, est_active) VALUES(1, 348, 0, 0, 0, 7, 1, 1);

--INSERTION DANS LA TABLE MISE_A_JOUR--
INSERT INTO Mise_a_jour(ville, timezone, heure, minute, seconde) VALUES(1, 348, 1, 1, 1);

--INSERTION DANS LA TABLE SINGLE--
INSERT INTO Single(nom_du_single, nom_de_l_auteur, pays, chemin_d_accee, identifiant_YouTube_de_la_video_d_origine) VALUES('We are all made of stars', 'Moby', 58, "./media/Moby_We_Are_All_Made_of_Stars_Official_video.wav", "x1rFAaAKpVc");
INSERT INTO Single(nom_du_single, nom_de_l_auteur, pays, chemin_d_accee, identifiant_YouTube_de_la_video_d_origine) VALUES('Wizards in Winter', 'Trans-Siberian-Orchestra', 58, "./media/Wizards_in_Winter-Trans-Siberian_Orchestra.wav", "XFLOh44P5z0");
