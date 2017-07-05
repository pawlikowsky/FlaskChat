from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), ])

class WorkspaceForm(FlaskForm):
    workspace = StringField('workspace')

class JoinForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
