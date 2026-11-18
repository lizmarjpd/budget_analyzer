# Importation de SQLAlchemy pour effectuer les opérations sur la base de données.
from base_de_donnees.db import db

# Importation du modèle représentant les dépenses.
from modeles.depense_modele import Depense


# Classe contenant la logique de gestion des dépenses.
# Elle permet de consulter, ajouter, modifier, supprimer et calculer les dépenses.
class DepenseService:

    # ==========================================================
    # 1. CONSULTER TOUTES LES DÉPENSES
    # ==========================================================

    # Méthode permettant de récupérer toutes les dépenses enregistrées.
    @staticmethod
    def lister_depenses(mois=None):

        # Chercher les dépenses enregistrées.
        requete = Depense.query

        # Garder seulement les dépenses du mois choisi.
        if mois:
            requete = requete.filter(Depense.date.startswith(mois + "-"))

        return requete.all()
    # ==========================================================
    # 2. AJOUTER UNE NOUVELLE DÉPENSE
    # ==========================================================

    # Méthode permettant de créer et d'enregistrer une nouvelle dépense.
    @staticmethod
    def ajouter_depense(data):

        # Création d'un objet Depense avec les données reçues.
        depense = Depense(**data)

        # Ajout de la nouvelle dépense à la session SQLAlchemy.
        db.session.add(depense)

        # Validation et enregistrement des changements dans la base de données.
        db.session.commit()

        # Retourne la dépense créée au contrôleur.
        return depense

    # ==========================================================
    # 3. MODIFIER UNE DÉPENSE EXISTANTE
    # ==========================================================

    # Méthode permettant de modifier une dépense à partir de son identifiant.
    @staticmethod
    def modifier_depense(id_depense, donnees):

        # Recherche de la dépense dans la base de données.
        depense = db.session.get(Depense, id_depense)

        # Si la dépense n'existe pas, retourne None.
        if depense is None:
            return None

        # Modification du montant si cette information est fournie.
        if "montant" in donnees:
            depense.montant = donnees["montant"]

        # Modification de la date si cette information est fournie.
        if "date" in donnees:
            depense.date = donnees["date"]

        # Modifier la note de la dépense.
        if "note" in donnees:
            depense.note = donnees["note"]

        # Modifier la nature de la dépense.
        if "nature" in donnees:
            depense.nature = donnees["nature"]

        # Modifier le type de dépense.
        if "type_depense_id" in donnees:
            depense.type_depense_id = donnees["type_depense_id"]

        # Modification de la catégorie si cette information est fournie.
        if "categorie_id" in donnees:
            depense.categorie_id = donnees["categorie_id"]

        # Modification de la description si cette information est fournie.
        if "description" in donnees:
            depense.description = donnees["description"]

        # Enregistrement des modifications dans la base de données.
        db.session.commit()

        # Retourne la dépense mise à jour.
        return depense

    # ==========================================================
    # 4. SUPPRIMER UNE DÉPENSE
    # ==========================================================

    # Méthode permettant de supprimer une dépense selon son identifiant.
    @staticmethod
    def supprimer_depense(id_depense):

        # Recherche de la dépense à supprimer.
        depense = db.session.get(Depense, id_depense)

        # Si la dépense n'existe pas, retourne False.
        if depense is None:
            return False

        # Suppression de la dépense dans la session SQLAlchemy.
        db.session.delete(depense)

        # Confirmation de la suppression dans la base de données.
        db.session.commit()

        # Retourne True pour confirmer la suppression.
        return True

    # ==========================================================
    # 5. CALCULER LE MONTANT TOTAL DES DÉPENSES
    # ==========================================================

    # Méthode permettant de calculer la somme de toutes les dépenses.
    @staticmethod
    def calculer_total_depenses(mois=None):

        # Chercher les dépenses du mois choisi.
        depenses = DepenseService.lister_depenses(mois)

        # Additionner les montants.
        total = sum(depense.montant for depense in depenses)

        return round(total, 2)
    # ==========================================================
    # 6. CALCULER LES DÉPENSES PAR CATÉGORIE
    # ==========================================================

    # Méthode permettant de regrouper les dépenses selon leur catégorie.
    @staticmethod
    def calculer_depenses_par_categorie(mois=None):

        # Chercher les dépenses du mois choisi.
        depenses = DepenseService.lister_depenses(mois)

        # Création d'un dictionnaire pour conserver les totaux par catégorie.
        totaux = {}

        # Parcours de toutes les dépenses.
        for depense in depenses:

            # Récupération de l'identifiant de la catégorie.
            categorie_id = depense.categorie_id

            # Si la catégorie n'existe pas encore dans le dictionnaire,
            # on initialise son total à zéro.
            if categorie_id not in totaux:
                totaux[categorie_id] = 0

            # Ajout du montant de la dépense au total de sa catégorie.
            totaux[categorie_id] += depense.montant

        # Retourne le dictionnaire contenant les totaux par catégorie.
        return totaux