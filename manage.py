from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
import os

from codechat import app
from database import db_session

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/codechat.db'

db=SQLAlchemy(app)
migrate = Migrate(app, db_session)
manager = Manager(app)


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()