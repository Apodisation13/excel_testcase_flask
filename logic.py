import sqlite3

from db import *


def query(model):
    data = session.query(model)
    query_q = session.query(sq.func.SUM(model.quantity)).all()
    query_p = session.query(sq.func.SUM(model.price)).all()
    query_r = session.query(sq.func.SUM(model.result)).all()
    return data, query_q, query_p, query_r


def aggregate_logic():

    def aggregate(queryset: list):
        i = 1
        db_set = [{queryset[0][1]: queryset[0][2], 'id': i}, ]

        for row in queryset[1:]:

            if row[1] not in db_set[i - 1]:
                db_set.append({row[1]: row[2], 'id': i + 1})
                i += 1
            else:
                db_set[i - 1][row[1]] += '<br>' + row[2]
        return db_set

    conn = sqlite3.connect('data.sqlite')
    cur = conn.cursor()

    query_V = 'select spTN.id, spMNN.MNN, spTN.TN, spMNN.VEN from spTN left outer join spMNN on spMNN.id = spTN.MNN ' \
            'WHERE spMNN.VEN = "True" ORDER BY spMNN.MNN'
    query_N = 'select spTN.id, spMNN.MNN, spTN.TN, spMNN.VEN from spTN left outer join spMNN on spMNN.id = spTN.MNN ' \
            'WHERE spMNN.VEN = "False" ORDER BY spMNN.MNN'
    cur.execute(query_V)
    rows_V = cur.fetchall()

    cur.execute(query_N)
    rows_N = cur.fetchall()

    db_V = aggregate(rows_V)
    db_N = aggregate(rows_N)

    # for el in db_V[:10]:
    #     print(el)
    # print()
    # for el in db_N[:10]:
    #     print(el)

    return db_V, db_N
