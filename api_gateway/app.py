from flask import Flask, render_template
from routes import gateway_bp

app = Flask(__name__)

app.register_blueprint(gateway_bp)


# Vérifier le fonctionnement de l'API Gateway
@app.route("/test")
def tester_gateway():
    return "Mon API Gateway fonctionne !"


# Afficher le tableau de bord
@app.route("/")
def afficher_tableau_de_bord():
    return render_template("tableau_de_bord.html")


if __name__ == "__main__":
    app.run(port=5010, debug=True)