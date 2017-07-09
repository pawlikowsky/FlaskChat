from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), ])
    language = SelectField('language',
    choices=[('python','Python'), ('javascript','Javascript'), ('sql','SQL'), ('html','HTML'), ('java','Java'), ('csharp','C#')]
    )

class WorkspaceForm(FlaskForm):
    workspace = TextAreaField('workspace')
    

class JoinForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
