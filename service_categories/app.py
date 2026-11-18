from flask import Flask
from flasgger import Swagger
from base_de_donnees.db import db
from controleurs.categories_controller import categories_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///categories.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Swagger(app)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(categories_bp, url_prefix="/categories")

if __name__ == "__main__":
    app.run(port=5003, debug=True)
