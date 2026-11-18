# Importation des outils Flask.
from flask import Blueprint, request, jsonify

# Importation du service de gestion des dépenses.
from services.depense_service import DepenseService


# Création du Blueprint du microservice Dépenses.
depenses_bp = Blueprint("depenses", __name__)


# ==========================================================
# 1. CONSULTER TOUTES LES DÉPENSES
# ==========================================================

@depenses_bp.route("/", methods=["GET"])
def lister_depenses():
    """
    Consulter la liste des dépenses.
    ---
    tags:
      - Dépenses
    parameters:
      - name: mois
        in: query
        type: string
        required: false
        description: Mois à consulter au format AAAA-MM.
    responses:
      200:
        description: Liste des dépenses au format JSON.
    """

    # Lire le mois choisi.
    mois = request.args.get("mois")

    # Chercher les dépenses du mois.
    depenses = DepenseService.lister_depenses(mois)

    # Retourner les dépenses au format JSON.
    return jsonify([d.to_dict() for d in depenses])


# ==========================================================
# 2. AJOUTER UNE NOUVELLE DÉPENSE
# ==========================================================

@depenses_bp.route("/", methods=["POST"])
def ajouter_depense():
    """
    Ajouter une nouvelle dépense.
    ---
    tags:
      - Dépenses
    consumes:
      - application/json
    parameters:
      - name: depense
        in: body
        required: true
        description: Informations de la nouvelle dépense.
        schema:
          type: object
          required:
            - montant
            - date
            - categorie_id
          properties:
            montant:
              type: number
              example: 25.50
            date:
              type: string
              example: "2026-11-18"
            categorie_id:
              type: integer
              example: 1
            description:
              type: string
              example: "Épicerie"
            nature:
              type: string
              example: "occasionnelle"
            mode_paiement:
              type: string
              example: "Carte de débit"
            note:
              type: string
              example: "Achat de démonstration"
    responses:
      201:
        description: Dépense créée avec succès.
    """

    # Récupérer les données JSON.
    data = request.json

    # Enregistrer la nouvelle dépense.
    depense = DepenseService.ajouter_depense(data)

    # Retourner la dépense créée.
    return jsonify(depense.to_dict()), 201


# ==========================================================
# 3. MODIFIER UNE DÉPENSE EXISTANTE
# ==========================================================

@depenses_bp.route("/<int:id_depense>", methods=["PUT"])
def modifier_depense(id_depense):
    """
    Modifier une dépense existante.
    ---
    tags:
      - Dépenses
    consumes:
      - application/json
    parameters:
      - name: id_depense
        in: path
        type: integer
        required: true
        description: Identifiant de la dépense à modifier.
      - name: donnees
        in: body
        required: true
        description: Nouvelles informations de la dépense.
        schema:
          type: object
          properties:
            montant:
              type: number
              example: 30.00
            date:
              type: string
              example: "2026-11-18"
            categorie_id:
              type: integer
              example: 1
            description:
              type: string
              example: "Épicerie modifiée"
            nature:
              type: string
              example: "occasionnelle"
            mode_paiement:
              type: string
              example: "Carte de débit"
            note:
              type: string
              example: "Modification de démonstration"
    responses:
      200:
        description: Dépense modifiée avec succès.
      400:
        description: Données JSON invalides.
      404:
        description: Dépense introuvable.
    """

    # Récupération des données JSON.
    donnees = request.get_json(silent=True)

    # Vérifier que les données sont valides.
    if not isinstance(donnees, dict):
        return jsonify({
            "erreur": "Les données JSON sont invalides."
        }), 400

    # Modifier la dépense.
    depense = DepenseService.modifier_depense(id_depense, donnees)

    # Vérifier si la dépense existe.
    if depense is None:
        return jsonify({
            "erreur": "La dépense n'existe pas."
        }), 404

    # Retourner la dépense modifiée.
    return jsonify(depense.to_dict()), 200


# ==========================================================
# 4. SUPPRIMER UNE DÉPENSE
# ==========================================================

@depenses_bp.route("/<int:id_depense>", methods=["DELETE"])
def supprimer_depense(id_depense):
    """
    Supprimer une dépense existante.
    ---
    tags:
      - Dépenses
    parameters:
      - name: id_depense
        in: path
        type: integer
        required: true
        description: Identifiant de la dépense à supprimer.
    responses:
      200:
        description: Dépense supprimée avec succès.
      404:
        description: Dépense introuvable.
    """

    # Supprimer la dépense demandée.
    resultat = DepenseService.supprimer_depense(id_depense)

    # Vérifier si la dépense existe.
    if not resultat:
        return jsonify({
            "erreur": "La dépense n'existe pas."
        }), 404

    # Confirmer la suppression.
    return jsonify({
        "message": "La dépense a été supprimée avec succès."
    }), 200


# ==========================================================
# 5. CALCULER LE TOTAL DES DÉPENSES
# ==========================================================

@depenses_bp.route("/total", methods=["GET"])
def obtenir_total_depenses():
    """
    Consulter le montant total des dépenses.
    ---
    tags:
      - Statistiques
    parameters:
      - name: mois
        in: query
        type: string
        required: false
        description: Mois à consulter au format AAAA-MM.
    responses:
      200:
        description: Montant total des dépenses.
    """

    # Lire le mois choisi.
    mois = request.args.get("mois")

    # Calculer le total.
    total = DepenseService.calculer_total_depenses(mois)

    # Retourner le résultat au format JSON.
    return jsonify({
        "total_depenses": total
    }), 200


# ==========================================================
# 6. CONSULTER LES DÉPENSES PAR CATÉGORIE
# ==========================================================

@depenses_bp.route("/par-categorie", methods=["GET"])
def obtenir_depenses_par_categorie():
    """
    Consulter les dépenses regroupées par catégorie.
    ---
    tags:
      - Statistiques
    parameters:
      - name: mois
        in: query
        type: string
        required: false
        description: Mois à consulter au format AAAA-MM.
    responses:
      200:
        description: Montants des dépenses par catégorie.
    """

    # Lire le mois choisi.
    mois = request.args.get("mois")

    # Calculer les montants par catégorie.
    totaux = DepenseService.calculer_depenses_par_categorie(mois)

    # Retourner les statistiques.
    return jsonify({
        "depenses_par_categorie": totaux
    }), 200