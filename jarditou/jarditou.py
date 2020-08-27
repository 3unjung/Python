from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/", methods=["post", "get"])
def index():
    return render_template("views/index.html")


@app.route("/catalogue")
def catalogue():
    return render_template("views/catalogue.html")


@app.route("/produit")  # /blog du mec
def produits():
    posts = [{'name': 'pioche', 'description': 'Casse les cailloux', 'prix': 52},
             {'name': 'mandrin', 'description': 'Fais des trous et des gros', 'prix': 25},
             {'name': 'marteau', 'description': 'Martelle des clous par exemple', 'prix': 2552},
             ]  # liste de chaine de caractère
    return render_template("views/produits.html", posts=posts)  # envoie la variable dans le template


@app.route("/produit/posts/1")
def details():
    posts = [{'name': 'pioche', 'description': 'Casse les cailloux', 'prix': 52},
             {'name': 'mandrin', 'description': 'Fais des trous et des gros', 'prix': 25},
             {'name': 'marteau', 'description': 'Martelle des clous par exemple', 'prix': 2552},
             ]  # liste de chaine de caractère
    return render_template("views/details.html")  # envoie la variable dans le template


@app.errorhandler(404)
def page_not_found(error):
    return render_template('views/404.jarditou.html'), 404


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run()
