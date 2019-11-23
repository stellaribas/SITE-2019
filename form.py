from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email

class CadastroForm (FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])


class LoginForm(FlaskForm):
    usuario = StringField("Usuario", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
  
class DenunciasForm(FlaskForm):
    latitude = StringField('Latitude', validators=[DataRequired()])
    longitude = StringField('Longitude', validators=[DataRequired()])
    mensagem = TextAreaField('Mensagem', validators=[DataRequired()])
