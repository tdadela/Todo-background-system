import sys
# from app import app
from flask import render_template, request, redirect, url_for
from app.main.forms import AddTaskForm
from app.main import bp
import app.main.settings as st

sys.path.append(st.LIBRARY_PATH)
from db_operation import select_all_tasks, add_to_task, remove_using_id, add_to_done


@bp.post('/')
@bp.get('/')
@bp.get('/finish/<string:id_fin>')
@bp.get('/delete/<string:id_del>')
def index(id_fin=None, id_del=None):
    if id_fin:
        task_name = remove_using_id(st.DATABASE_PATH, "TASK", id_fin)
        add_to_done(st.DATABASE_PATH, task_name)
        return redirect(url_for('main.index'))
    elif id_del:
        remove_using_id(st.DATABASE_PATH, "TASK", id_del)
        return redirect(url_for('main.index'))

    add_task = AddTaskForm()
    if add_task.submit.data and add_task.validate_on_submit():
        add_to_task(st.DATABASE_PATH, add_task.name.data)
        add_task.name.data = ''

    '''
    add_task = AddTaskForm()
    task_done = TaskDone()
    task_delete = TaskDelete()

    if add_task.submit.data and add_task.validate_on_submit():
        add_to_task(st.DATABASE_PATH, add_task.name.data)
        add_task.name.data = ''
    
    elif task_delete.submit.data and task_delete.validate():
        task_id = request.form.get("task_id", "")
        remove_using_id(st.DATABASE_PATH, "TASK", task_id)
    
    elif task_done.submit.data and task_done.validate():
        task_id = request.form.get("task_id", "")
        task_name = remove_using_id(st.DATABASE_PATH, "TASK", task_id)
        add_to_done(st.DATABASE_PATH, task_name)
    '''
    tasks = select_all_tasks(st.DATABASE_PATH, 'TASK')
    return render_template('index.html', form=add_task,
                           tasks=tasks, index=True)


@bp.get('/finished')
@bp.post('/finished')
def finished():
    tasks = select_all_tasks(st.DATABASE_PATH, 'DONE')
    return render_template('index.html', tasks=tasks, index=False)
