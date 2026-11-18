# Importation de l'objet SQLAlchemy pour définir le modèle de données.
from base_de_donnees.db import db


# Modèle représentant une catégorie de dépenses dans la base de données.
class Categorie(db.Model):

    # Nom de la table dans la base de données.
    __tablename__ = "categories"

    # Identifiant unique de chaque catégorie (clé primaire).
    id = db.Column(db.Integer, primary_key=True)

    # Nom de la catégorie. Ce champ est obligatoire.
    nom = db.Column(db.String, nullable=False)

    # Icône associée à la catégorie.
    icone = db.Column(db.String)

    # Couleur utilisée pour représenter la catégorie.
    couleur = db.Column(db.String)

    # Conversion des informations de la catégorie en dictionnaire Python.
    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "icone": self.icone,
            "couleur": self.couleur
        }