# passos para publicar no servidor do heroku
# pip install Flask
# pip install gunicorn
# pip freeze > requirements.txt

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome>")
def usuarios(nome):
    return render_template("usuarios.html", nome = nome)

if __name__ == "__main__":
    app.run(debug=True)

