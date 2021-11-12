import sys
# from app import app
from flask import render_template
from app.main.forms import AddTaskForm
from app.main import bp
import app.main.settings as st

sys.path.append(st.LIBRARY_PATH)
from db_operation import select_all_tasks, add_to_task


@bp.get('/')
@bp.post('/')
@bp.get('/index')
@bp.post('/index')
def index():
    form = AddTaskForm()
    if form.validate_on_submit():
        add_to_task(st.DATABASE_PATH, form.name.data)
        form.name.data = ''
    tasks = select_all_tasks(st.DATABASE_PATH, 'TASK')
    return render_template('index.html', form=form, tasks=tasks)


@bp.get('/finished')
@bp.post('/finished')
def finished():
    tasks = select_all_tasks(st.DATABASE_PATH, 'DONE')
    return render_template('index.html', tasks=tasks)
