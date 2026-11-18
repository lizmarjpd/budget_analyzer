from flask import Blueprint, jsonify, request
import requests

gateway_bp = Blueprint("gateway", __name__)

URL_CATEGORIES = "http://127.0.0.1:5003"
URL_DEPENSES = "http://127.0.0.1:5002"


# Consulter les catégories disponibles.
@gateway_bp.route("/categories", methods=["GET"])
def lister_categories():
    try:
        reponse = requests.get(
            f"{URL_CATEGORIES}/categories/",
            timeout=5
        )

        reponse.raise_for_status()
        return jsonify(reponse.json()), reponse.status_code

    except requests.RequestException:
        return jsonify({
            "erreur": "Le service des catégories est indisponible."
        }), 503


# Consulter les dépenses, avec un filtre mensuel si nécessaire.
@gateway_bp.route("/depenses", methods=["GET"])
def lister_depenses():
    try:
        reponse = requests.get(
            f"{URL_DEPENSES}/depenses/",
            params=request.args,
            timeout=5
        )

        reponse.raise_for_status()
        return jsonify(reponse.json()), reponse.status_code

    except requests.RequestException:
        return jsonify({
            "erreur": "Le service des dépenses est indisponible."
        }), 503


# Ajouter une nouvelle dépense.
@gateway_bp.route("/depenses", methods=["POST"])
def ajouter_depense():
    try:
        donnees = request.get_json(silent=True)

        if not isinstance(donnees, dict):
            return jsonify({
                "erreur": "Les données JSON sont invalides."
            }), 400

        reponse = requests.post(
            f"{URL_DEPENSES}/depenses/",
            json=donnees,
            timeout=5
        )

        return jsonify(reponse.json()), reponse.status_code

    except requests.RequestException:
        return jsonify({
            "erreur": "Le service des dépenses est indisponible."
        }), 503


# Ajouter une nouvelle catégorie.
@gateway_bp.route("/categories", methods=["POST"])
def ajouter_categorie():
    try:
        donnees = request.get_json(silent=True)

        if not isinstance(donnees, dict):
            return jsonify({
                "erreur": "Les données JSON sont invalides."
            }), 400

        reponse = requests.post(
            f"{URL_CATEGORIES}/categories/",
            json=donnees,
            timeout=5
        )

        return jsonify(reponse.json()), reponse.status_code

    except requests.RequestException:
        return jsonify({
            "erreur": "Le service des catégories est indisponible."
        }), 503


# Modifier une dépense existante.
@gateway_bp.route("/depenses/<int:id_depense>", methods=["PUT"])
def modifier_depense(id_depense):
    try:
        donnees = request.get_json(silent=True)

        if not isinstance(donnees, dict):
            return jsonify({
                "erreur": "Les données JSON sont invalides."
            }), 400

        reponse = requests.put(
            f"{URL_DEPENSES}/depenses/{id_depense}",
            json=donnees,
            timeout=5
        )

        return jsonify(reponse.json()), reponse.status_code

    except requests.RequestException:
        return jsonify({
            "erreur": "Le service des dépenses est indisponible."
        }), 503


# Supprimer une dépense.
@gateway_bp.route("/depenses/<int:id_depense>", methods=["DELETE"])
def supprimer_depense(id_depense):
    try:
        reponse = requests.delete(
            f"{URL_DEPENSES}/depenses/{id_depense}",
            timeout=5
        )

        return jsonify(reponse.json()), reponse.status_code

    except requests.RequestException:
        return jsonify({
            "erreur": "Le service des dépenses est indisponible."
        }), 503


# Calculer le total des dépenses du mois choisi.
@gateway_bp.route("/depenses/total", methods=["GET"])
def obtenir_total_depenses():
    try:
        reponse = requests.get(
            f"{URL_DEPENSES}/depenses/total",
            params=request.args,
            timeout=5
        )

        reponse.raise_for_status()
        return jsonify(reponse.json()), reponse.status_code

    except requests.RequestException:
        return jsonify({
            "erreur": "Le service des dépenses est indisponible."
        }), 503


# Consulter les dépenses par catégorie pour le mois choisi.
@gateway_bp.route("/depenses/par-categorie", methods=["GET"])
def obtenir_depenses_par_categorie():
    try:
        reponse = requests.get(
            f"{URL_DEPENSES}/depenses/par-categorie",
            params=request.args,
            timeout=5
        )

        reponse.raise_for_status()
        return jsonify(reponse.json()), reponse.status_code

    except requests.RequestException:
        return jsonify({
            "erreur": "Le service des dépenses est indisponible."
        }), 503