from flask import Flask
# from flask_migrate import Migrate

# from models import db


app = Flask(__name__)

# db.init_app(app)
# migrate = Migrate(app, db)


# with open('password.txt') as f:
#     password = f.readline()
#
# postgres_uri = f'postgresql://postgres:{password}@127.0.0.1:5432/flask_hw_db'
# app.config.from_mapping(SQLALCHEMY_DATABASE_URI=postgres_uri)

user = 'james'
password = '1234567890'
db = 'test_case_excel'
host = 'postgresdb'
postgres_uri = f'postgresql://{user}:{password}@{host}:5432/{db}'
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=postgres_uri)
