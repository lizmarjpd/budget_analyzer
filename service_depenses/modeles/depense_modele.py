from base_de_donnees.db import db


# Cette classe représente une dépense.
class Depense(db.Model):

    __tablename__ = "depenses"

    # Numéro de la dépense.
    id = db.Column(db.Integer, primary_key=True)

    # Montant payé.
    montant = db.Column(db.Float, nullable=False)

    # Date de la dépense.
    date = db.Column(db.String, nullable=False)

    # Catégorie choisie.
    categorie_id = db.Column(db.Integer, nullable=True)

    # Nom ou description de la dépense.
    description = db.Column(db.String, nullable=True)

    # Dépense habituelle ou occasionnelle.
    nature = db.Column(db.String, nullable=True)

    # Type choisi pour une dépense habituelle.
    type_depense_id = db.Column(db.Integer, nullable=True)

    # Note facultative.
    note = db.Column(db.String, nullable=True)

    # Mode de paiement facultatif.
    mode_paiement = db.Column(db.String, nullable=True)

    # Préparer les données pour le format JSON.
    def to_dict(self):
        return {
            "id": self.id,
            "montant": self.montant,
            "date": self.date,
            "categorie_id": self.categorie_id,
            "description": self.description,
            "nature": self.nature,
            "type_depense_id": self.type_depense_id,
            "note": self.note,
            "mode_paiement": self.mode_paiement
        }