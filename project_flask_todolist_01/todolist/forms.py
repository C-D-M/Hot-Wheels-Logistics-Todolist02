# Sistema di Autenticazione Utenti: Login e Logout
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# forms

# form login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# form crea task
class TaskForm(FlaskForm):
    title = StringField('Titolo', validators=[DataRequired()])
    description = TextAreaField('Descrizione', validators=[DataRequired()])
    submit = SubmitField('Pubblica Task')