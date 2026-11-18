# Importation de SQLAlchemy pour gérer les interactions avec la base de données.
from flask_sqlalchemy import SQLAlchemy

# Création de l'instance SQLAlchemy qui sera initialisée dans l'application Flask.
# Cet objet sera utilisé par les modèles et les services pour accéder à la base de données.
db = SQLAlchemy()