Budget Analyzer

1. Présentation du projet

Budget Analyzer est une application web de gestion des dépenses personnelles, développée dans le cadre de notre formation.

L'objectif principal est d'aider les utilisateurs à enregistrer, organiser et analyser leurs dépenses afin d'avoir une meilleure vision de leurs habitudes financières.

L'application repose sur une architecture composée de plusieurs services qui communiquent entre eux.

Réalisé par

Lizmar Perdomo

Christelle Niecho

2. Technologies utilisées

Technologie

Utilisation

Python

Langage principal du projet

Flask

Développement des API REST

SQLite

Stockage des données

SQLAlchemy

Gestion des modèles et des bases de données

Flasgger / Swagger

Documentation et tests des API

HTML, CSS et JavaScript

Interface utilisateur

Requests

Communication entre les services

3. Architecture du projet

Budget Analyzer est composé de trois services principaux.

Service des catégories — Port 5003

Ce service permet de gérer les catégories utilisées pour classer les dépenses.

Il propose notamment les opérations suivantes :

Consulter les catégories enregistrées.

Ajouter une nouvelle catégorie.

Service des dépenses — Port 5002

Ce service permet de gérer les dépenses personnelles.

Ses principales fonctionnalités sont :

Ajouter une dépense.

Consulter les dépenses enregistrées.

Modifier une dépense.

Supprimer une dépense.

API Gateway — Port 5010

L'API Gateway constitue le point d'entrée principal de l'application.

Elle permet de communiquer avec les services des catégories et des dépenses.

Elle fournit également les informations nécessaires à l'affichage du tableau de bord.

4. Fonctionnalités principales

Budget Analyzer permet notamment de :

Enregistrer les dépenses personnelles.

Classer les dépenses par catégorie.

Distinguer les dépenses habituelles et occasionnelles.

Ajouter une description facultative.

Indiquer un mode de paiement.

Modifier ou supprimer des transactions.

Consulter le total des dépenses.

Consulter le nombre de transactions.

Filtrer les dépenses par mois.

Visualiser la répartition des dépenses par catégorie.

Le tableau de bord permet de consulter les informations financières de manière simple et organisée.

5. Structure du projet

budget_analyzer/
│
├── api_gateway/
│   ├── templates/
│   ├── app.py
│   └── routes.py
│
├── service_categories/
│   ├── base_de_donnees/
│   ├── controleurs/
│   ├── modeles/
│   ├── services/
│   └── app.py
│
├── service_depenses/
│   ├── base_de_donnees/
│   ├── controleurs/
│   ├── modeles/
│   ├── services/
│   └── app.py
│
├── .gitignore
└── README.md

Chaque service possède son propre rôle dans l'application.

6. Installation du projet

Prérequis

Avant de commencer, il faut disposer de :

Python installé sur l'ordinateur.

Un terminal PowerShell ou un environnement comme PyCharm.

Une connexion Internet pour installer les dépendances.

Étape 1 — Télécharger le projet

Télécharger le dépôt depuis GitHub.

Décompresser le fichier ZIP si nécessaire, puis ouvrir le dossier budget_analyzer.

Étape 2 — Créer un environnement virtuel

Dans un terminal ouvert à la racine du projet, exécuter :

python -m venv .venv

Activer l'environnement virtuel sous Windows PowerShell :

.\.venv\Scripts\Activate.ps1

Si l'environnement virtuel est déjà configuré dans PyCharm, cette étape peut être adaptée à la configuration existante.

Étape 3 — Installer les dépendances

Exécuter :

python -m pip install flask flask-sqlalchemy flask-cors requests flasgger

Ces bibliothèques sont nécessaires au fonctionnement des services de l'application.

7. Démarrer les services

Pour démarrer l'application, ouvrir trois terminaux distincts.

Chaque terminal doit initialement être ouvert dans le dossier principal budget_analyzer, avec l'environnement Python configuré.

Terminal 1 — Service des catégories (port 5003)

cd service_categories
python app.py

Le service doit afficher une adresse semblable à :

http://127.0.0.1:5003

Terminal 2 — Service des dépenses (port 5002)

Dans un nouveau terminal ouvert à la racine du projet :

cd service_depenses
python app.py

Le service doit afficher :

http://127.0.0.1:5002

Terminal 3 — API Gateway (port 5010)

Dans un troisième terminal ouvert à la racine du projet :

cd api_gateway
python app.py

Le service doit afficher :

http://127.0.0.1:5010

Important : les trois services doivent rester actifs pendant l'utilisation de Budget Analyzer.

8. Accéder à l'application

Une fois les trois services démarrés, ouvrir un navigateur web.

Accéder à l'adresse suivante :

http://127.0.0.1:5010/

Le tableau de bord de Budget Analyzer sera affiché.

L'utilisateur pourra consulter les dépenses et utiliser les fonctionnalités disponibles dans l'interface.

9. Initialisation des bases de données

Les services utilisent SQLite pour stocker les informations.

Les bases de données sont configurées dans les fichiers app.py des services concernés.

Lors du démarrage, SQLAlchemy exécute :

with app.app_context():
    db.create_all()

Cette instruction permet de créer les tables qui n'existent pas encore.

Les fichiers de bases de données locales ne sont pas inclus dans le dépôt GitHub.

Création des premières catégories

Lors d'une nouvelle installation, la base de données des catégories peut être vide.

Il est possible d'ajouter des catégories à l'aide de l'API REST.

Pour cela :

Démarrer le service des catégories sur le port 5003.

Ouvrir Swagger.

Sélectionner l'opération POST /categories/.

Cliquer sur Try it out.

Entrer les informations de la catégorie.

Cliquer sur Execute.

Exemple de données :

{
  "nom": "Alimentation",
  "icone": "🍽️",
  "couleur": "#4CAF50"
}

Une réponse HTTP 201 indique que la catégorie a été créée.

La méthode GET /categories/ permet ensuite de consulter les catégories enregistrées.

10. Documentation des API avec Swagger

Swagger permet de consulter la documentation des API REST et de tester les opérations disponibles.

Service des catégories

http://127.0.0.1:5003/apidocs/

Service des dépenses

http://127.0.0.1:5002/apidocs/

Pour utiliser Swagger :

Démarrer le service correspondant.

Ouvrir l'adresse de documentation dans le navigateur.

Sélectionner une opération.

Cliquer sur Try it out.

Fournir les données demandées, si nécessaire.

Cliquer sur Execute pour effectuer le test.

11. Exemples d'opérations API

Consulter les catégories

Méthode : GET

Endpoint : /categories/

Service : Port 5003

Cette opération retourne les catégories enregistrées dans la base de données.

Ajouter une catégorie

Méthode : POST

Endpoint : /categories/

Service : Port 5003

Exemple :

{
  "nom": "Transport",
  "icone": "🚗",
  "couleur": "#2196F3"
}

Gestion des dépenses

Le service des dépenses permet d'effectuer les principales opérations CRUD :

CREATE : créer une dépense.

READ : consulter les dépenses.

UPDATE : modifier une dépense.

DELETE : supprimer une dépense.

Les opérations disponibles peuvent être consultées dans Swagger.

12. Difficultés rencontrées

Pendant le développement, nous avons rencontré plusieurs difficultés techniques.

Gestion des bases de données

Nous avons dû comprendre le fonctionnement de SQLAlchemy et la relation entre les modèles Python et les tables SQLite.

Communication entre les services

Nous avons appris à faire communiquer plusieurs services Flask en utilisant une API Gateway.

Gestion du mode de paiement

Nous avons rencontré une difficulté liée au champ mode_paiement, qui nécessitait une adaptation du modèle et de la base de données.

Démarrage des services

Nous avons également constaté que certains problèmes d'affichage pouvaient être liés à un service qui n'était pas démarré.

Ces difficultés nous ont permis de mieux comprendre le fonctionnement des API REST, des bases de données et d'une architecture composée de plusieurs services.

13. Améliorations futures

Dans une prochaine version, nous aimerions ajouter :

L'enregistrement des revenus mensuels.

La définition d'un budget mensuel.

Le calcul du pourcentage des revenus consacré aux dépenses.

Une comparaison entre les revenus et les dépenses.

Des fonctionnalités supplémentaires pour améliorer le suivi financier.

Ces fonctionnalités représentent des pistes d'évolution et ne font pas partie de la version actuelle.

14. Conclusion

Le projet Budget Analyzer nous a permis de mettre en pratique plusieurs notions étudiées pendant notre formation, notamment :

La programmation en Python.

Le développement d'API REST avec Flask.

La gestion des bases de données SQLite.

L'utilisation de SQLAlchemy.

La documentation des API avec Swagger.

La communication entre plusieurs services.

Ce projet répond à un besoin concret : permettre aux utilisateurs de mieux organiser leurs dépenses et de comprendre leurs habitudes financières.

Budget Analyzer — Projet réalisé par Lizmar Perdomo et Christelle Niecho.