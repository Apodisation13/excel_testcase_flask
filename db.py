import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker


with open('password.txt') as f:
    password = f.readline()

user = 'postgres'
db = 'test_case_excel'
postgres_uri = f'postgresql://{user}:{password}@127.0.0.1:5432/{db}'


engine = sq.create_engine(postgres_uri)

Session = sessionmaker(bind=engine)
session = Session()
