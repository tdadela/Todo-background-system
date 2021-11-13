from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    name = StringField('Add new task', validators=[DataRequired()])
    submit = SubmitField('Add')
