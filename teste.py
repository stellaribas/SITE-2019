from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from form import LoginForm, CadastroForm, DenunciasForm

site=Flask(__name__)
site.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto2019.db'
site.config['SECRET_KEY'] = '46ED57RF8GT9YH80UJ-OLÇP='
db = SQLAlchemy(site)

class Usuario (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(15), nullable=False)
    denuncias = db.relationship('Denuncia', backref='usuario', lazy=True)

    def __repr__(self):
        return '<Usuario %r>' % self.usuario

class Denuncia (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.String(20), unique=False, nullable=False)
    longitude = db.Column(db.String(20), unique=False, nullable=False)
    mensagem = db.Column(db.Text(), unique=False, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __repr__(self):
        return '<Denuncia %r>' % self.mensagem

@site.route("/")
def home():
    return render_template("index.html")

@site.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    form = CadastroForm ()
    if form.validate_on_submit():
        u = Usuario()
        u.usuario=form.usuario.data
        u.email=form.email.data
        u.senha=form.senha.data
        db.session.add(u)
        db.session.commit()

    return render_template("cadastro.html",
                                form=form)

@site.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm ()
    if form.validate_on_submit():
        print(form.usuario.data)
        print(form.senha.data)

    return render_template("login.html", 
                            form=form)


@site.route("/mapa")
def mapa():
    return render_template("mapa.html")


@site.route("/denuncias", methods=["GET", "POST"])
def denuncias():
    form = DenunciasForm ()
    if form.validate_on_submit():
        d = Denuncia()
        d.latitude=form.latitude.data
        d.longitude=form.longitude.data
        d.mensagem=form.mensagem.data
        d.usuario_id=1
        db.session.add(d)
        db.session.commit()

    return render_template("denuncias.html",
                                form=form)

if __name__== "__main__":
    site.run(debug=True)



