from flask import Flask, render_template
from flask_ngrok import run_with_ngrok
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# from forms import RegisterForm
# efjnioerniofnreiognre

from jarditou import config

app = Flask(__name__)
app.config.from_object(config)
run_with_ngrok(app)


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[])
    submit = SubmitField("Je m'inscrit !")


@app.route("/", methods=["post", "get"])
def index():
    return render_template("views/index.html")


@app.route("/catalogue")
def catalogue():
    return render_template("views/catalogue.html")


@app.route("/produit")  # /blog du mec
def produit():
    posts = [{'name': 'pioche', 'description': 'Casse les cailloux', 'prix': 52},
             {'name': 'mandrin', 'description': 'Fais des trous et des gros', 'prix': 25},
             {'name': 'marteau', 'description': 'Martelle des clous par exemple', 'prix': 2552},
             ]  # liste de chaine de caractère
    return render_template("views/produit.html", posts=posts)  # envoie la variable dans le template


@app.route("/produit/posts/1")
def details():
    posts = [{'name': 'pioche', 'description': 'Casse les cailloux', 'prix': 52},
             {'name': 'mandrin', 'description': 'Fais des trous et des gros', 'prix': 25},
             {'name': 'marteau', 'description': 'Martelle des clous par exemple', 'prix': 2552},
             ]  # liste de chaine de caractère
    return render_template("views/details.html")  # envoie la variable dans le template


@app.route("/register")
def register():
    form = RegisterForm()
    return render_template("views/register.html", form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('views/404.jarditou.html'), 404


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run()
