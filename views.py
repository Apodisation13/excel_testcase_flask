from flask import render_template
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from app import app
from models import TestExcel, AggrExcel


with open('password.txt') as f:
    password = f.readline()

user = 'postgres'
db = 'test_case_excel'
postgres_uri = f'postgresql://{user}:{password}@127.0.0.1:5432/{db}'


engine = sq.create_engine(postgres_uri)

Session = sessionmaker(bind=engine)
session = Session()


@app.route('/')
def home():  # put application's code here
    return render_template('base.html')


@app.route('/page1/')
def page_1():  # put application's code here
    data = session.query(TestExcel)
    query_q = session.query(sq.func.SUM(TestExcel.quantity)).all()
    query_p = session.query(sq.func.SUM(TestExcel.price)).all()
    query_r = session.query(sq.func.SUM(TestExcel.result)).all()
    return render_template('page_1.html', context=data,
                           query_q=query_q[0][0], query_p=query_p[0][0], query_r=query_r[0][0])


@app.route('/page2/')
def page_2():  # put application's code here
    data = session.query(AggrExcel)
    query_q = session.query(sq.func.SUM(AggrExcel.quantity)).all()
    query_p = session.query(sq.func.SUM(AggrExcel.price)).all()
    query_r = session.query(sq.func.SUM(AggrExcel.result)).all()
    return render_template('page_1.html', context=data,
                           query_q=query_q[0][0], query_p=query_p[0][0], query_r=query_r[0][0])


@app.route('/page3/')
def page_3():  # put application's code here
    return render_template('page_3.html')
