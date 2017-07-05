from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), ])

class WorkspaceForm(FlaskForm):
    workspace = TextAreaField('workspace')

class JoinForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
