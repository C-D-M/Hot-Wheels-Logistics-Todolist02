# sistema di autenticazione
from flask_login import UserMixin
from todolist import db, login_manager

# database, classi modelli
# Tabelle: User, Task
# Il capo reparto può creare n istanze di task, una istanza di task è creata da un capo reparto.

# login
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# Classe User, Tabella User
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # chiave primaria
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    tasks = db.relationship('Task', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return self.password == password

# Classe Task, Tabella Task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) # chiave primaria
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # chiave esterna
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(400), nullable=False)