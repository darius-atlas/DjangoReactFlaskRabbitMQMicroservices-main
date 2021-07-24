form main import app, db
form flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
