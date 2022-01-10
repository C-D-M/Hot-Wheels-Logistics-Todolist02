from flask import redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user, login_required
from flask_wtf import form

from todolist import db, app
from todolist.forms import LoginForm, TaskForm
from todolist.models import Task, User

# questo file contiene le function view

# homepage
@app.route("/")
def homepage():
    # query che restituisce tutti i tasks
    tasks = Task.query.all()
    return render_template("homepage.html", tasks=tasks)

# crea task, sono l'admin può creare un task
@app.route("/create-task", methods=["GET", "POST"])
@login_required
def task_create():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, description=form.description.data,
            author=current_user)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template("task_editor.html", form=form)

# elimina task, sono l'admin può eliminare un task
# devo passare task_id alla function task_delete, così da
# eliminare un instanza specifica del task
@app.route("/delete-task")
@login_required
def task_delete():
    # task_instance = Task.query.get(task_id)
    task_instance = Task.query.first()
    db.session.delete(task_instance)
    db.session.commit()
    return redirect(url_for('homepage'))

# login
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('homepage'))
    return render_template("login.html", form=form)

# logout
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage'))