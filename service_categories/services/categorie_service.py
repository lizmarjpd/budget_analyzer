# Importation de l'objet SQLAlchemy pour effectuer les opérations sur la base de données.
from base_de_donnees.db import db

# Importation du modèle Categorie qui représente la table des catégories.
from modeles.categorie_modele import Categorie


# Service responsable de la gestion des catégories dans la base de données.
class CategorieService:

    # Méthode permettant de récupérer toutes les catégories enregistrées.
    @staticmethod
    def lister_categories():

        # Recherche et retourne toutes les catégories de la base de données.
        return Categorie.query.all()

    # Méthode permettant d'ajouter une nouvelle catégorie.
    @staticmethod
    def ajouter_categorie(data):

        # Création d'un objet Categorie avec les données reçues.
        categorie = Categorie(**data)

        # Ajout de la nouvelle catégorie à la session SQLAlchemy.
        db.session.add(categorie)

        # Validation et enregistrement des changements dans la base de données.
        db.session.commit()

        # Retourne la catégorie créée au contrôleur.
        return categorie