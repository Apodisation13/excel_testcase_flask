import sqlalchemy as sq
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class TestExcel(Base):
    __tablename__ = 'test_excel'

    id = sq.Column(sq.Integer, primary_key=True)
    mnn = sq.Column(sq.String(150), nullable=False)
    trade_name = sq.Column(sq.String(150), nullable=False)
    form = sq.Column(sq.String(500), nullable=False)
    quantity = sq.Column(sq.Integer, nullable=False)
    price = sq.Column(sq.DECIMAL, nullable=False)
    result = sq.Column(sq.DECIMAL, nullable=False)

    def __str__(self):
        return f'{self.id} {self.mnn} {self.trade_name} {self.form} {self.quantity} {self.price}'


class AggrExcel(Base):
    __tablename__ = 'aggr_excel'

    id = sq.Column(sq.Integer, primary_key=True)
    mnn = sq.Column(sq.String(150), nullable=False)
    trade_name = sq.Column(sq.String(150), nullable=False)
    form = sq.Column(sq.String(500), nullable=False)
    quantity = sq.Column(sq.Integer, nullable=False)
    price = sq.Column(sq.DECIMAL, nullable=False)
    result = sq.Column(sq.DECIMAL, nullable=False)

    def __str__(self):
        return f'{self.mnn} {self.trade_name} {self.form} {self.quantity} {self.price}'
