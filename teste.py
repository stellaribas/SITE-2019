from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from form import LoginForm, CadastroForm

site=Flask(__name__)
site.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto2019.db'
site.config['SECRET_KEY'] = '46ED57RF8GT9YH80UJ-OLÇP='
db = SQLAlchemy(site)

class Usuario (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return '<Usuario %r>' % self.login

@site.route("/")
def home():
    return render_template("index.html")

@site.route("/cadastro")
def cadastro():
    form = CadastroForm ()
    return render_template("cadastro.html",
                                form=form)

@site.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm ()
    if form.validate_on_submit():
        print(form.usuario.date)
        print(form.senha.date)


    return render_template("login.html", 
                                form=form)

@site.route("/mapa")
def mapa():
    return render_template("mapa.html")

@site.route("/denuncias")
def denuncias():
    return render_template("denuncias.html")

if __name__== "__main__":
    site.run(debug=True)



