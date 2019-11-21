from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email

class CadastroForm (FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired])
    email = StringField('Email', validators=[DataRequired(), Email()])


class LoginForm(FlaskForm):
    usuario = StringField("usuario", validators=[DataRequired()])
    senha = PasswordField("senha", validators=[DataRequired])
    lembrar_Senha = BooleanField("lembrar_senha")

