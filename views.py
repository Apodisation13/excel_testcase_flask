from flask import render_template

from app import app
from models import TestExcel, AggrExcel
from logic import *


@app.route('/')
def home():  # put application's code here
    return render_template('base.html')


@app.route('/page1/')
def page_1():  # put application's code here
    data, query_q, query_p, query_r = query(TestExcel)
    return render_template('page_1.html', context=data,
                           query_q=query_q, query_p=query_p, query_r=query_r)


@app.route('/page2/')
def page_2():  # put application's code here
    data, query_q, query_p, query_r = query(AggrExcel)
    return render_template('page_1.html', context=data,
                           query_q=query_q, query_p=query_p, query_r=query_r)


@app.route('/page3/')
def page_3():  # put application's code here
    db_v, db_n = aggregate_logic()
    return render_template('page_3.html', db_v=db_v[:120], db_n=db_n[:120])
