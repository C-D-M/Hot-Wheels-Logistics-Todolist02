from todolist import app, db
from todolist.models import User, Task

# flask shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Task': Task}