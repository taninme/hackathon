import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.getenv('LEAGUE_DEV_KEY', 'ARE YOU KIDDING ME?')
DB_USER = os.getenv('DB_USER', 'ARE YOU KIDDING ME?')
DB_PWD = os.getenv('DB_PWD', 'ARE YOU KIDDING ME?')
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PWD + '@localhost/development'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')