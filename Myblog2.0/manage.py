# coding:utf-8
from app import create_app,db
from app.models import User,Role,Post,Board
from flask.ext.script import Manager,Shell
from flask.ext.migrate import Migrate,MigrateCommand
import os


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role,Post=Post)
manager.add_command("shell",Shell(make_shell_context()))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()