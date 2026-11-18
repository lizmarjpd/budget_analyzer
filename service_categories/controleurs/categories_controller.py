# Importation des outils Flask nécessaires pour créer les routes,
# recevoir les données des requêtes et retourner des réponses JSON.
from flask import Blueprint, request, jsonify

# Importation du service qui contient la logique de gestion des catégories.
from services.categorie_service import CategorieService


# Création du Blueprint pour regrouper les routes liées aux catégories.
categories_bp = Blueprint("categories", __name__)


# Route GET : permet de consulter toutes les catégories enregistrées.
@categories_bp.route("/", methods=["GET"])
def lister_categories():
    """
    Liste toutes les catégories
    ---
    tags:
      - Catégories
    responses:
      200:
        description: Liste des catégories
    """

    # Appel du service pour récupérer les catégories dans la base de données.
    categories = CategorieService.lister_categories()

    # Conversion des catégories en dictionnaires et retour au format JSON.
    return jsonify([c.to_dict() for c in categories])


# Route POST : permet d'ajouter une nouvelle catégorie.
@categories_bp.route("/", methods=["POST"])
def ajouter_categorie():
    """
    Ajouter une catégorie
    ---
    tags:
      - Catégories
    parameters:
      - in: body
        name: body
        required: true
        schema:
          properties:
            nom:
              type: string
            icone:
              type: string
            couleur:
              type: string
    responses:
      201:
        description: Catégorie créée avec succès
    """

    # Récupération des données JSON envoyées par le client.
    data = request.json

    # Appel du service pour créer et enregistrer la nouvelle catégorie.
    categorie = CategorieService.ajouter_categorie(data)

    # Retour de la catégorie créée au format JSON avec le statut HTTP 201.
    return jsonify(categorie.to_dict()), 201