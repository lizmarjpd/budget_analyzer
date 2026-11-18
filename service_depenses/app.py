from flask import Flask
from base_de_donnees.db import db
from controleurs.depenses_controller import depenses_bp
from flasgger import Swagger


app = Flask(__name__)

# Initialisation de la documentation Swagger
Swagger(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///depenses.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(depenses_bp, url_prefix="/depenses")

if __name__ == "__main__":
    app.run(port=5002, debug=True)
