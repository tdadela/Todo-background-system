from app import app
from flask import render_template
# from app.main.forms import
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')
