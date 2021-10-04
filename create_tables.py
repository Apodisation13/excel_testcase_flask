from sqlalchemy import MetaData
from sqlalchemy.testing.schema import Table

from db import *


metadata_obj = MetaData()

TestExcel = Table(
    'test_excel', metadata_obj,
    sq.Column('id', sq.Integer, primary_key=True),
    sq.Column('mnn', sq.String(150), nullable=False),
    sq.Column('trade_name', sq.String(150), nullable=False),
    sq.Column('form', sq.String(500), nullable=False),
    sq.Column('quantity', sq.Integer, nullable=False),
    sq.Column('price', sq.DECIMAL, nullable=False),
    sq.Column('result', sq.DECIMAL(15, 2), nullable=False)
)

AggrExcel = Table(
    'aggr_excel', metadata_obj,
    sq.Column('id', sq.Integer, primary_key=True),
    sq.Column('mnn', sq.String(150), nullable=False),
    sq.Column('trade_name', sq.String(150), nullable=False),
    sq.Column('form', sq.String(500), nullable=False),
    sq.Column('quantity', sq.Integer, nullable=False),
    sq.Column('price', sq.DECIMAL, nullable=False),
    sq.Column('result', sq.DECIMAL(15,2), nullable=False)
)

metadata_obj.create_all(engine)
