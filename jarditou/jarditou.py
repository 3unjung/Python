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


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run()
