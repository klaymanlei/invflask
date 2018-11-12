# coding:utf-8

from sqlalchemy import Column, String, create_engine, Numeric, Date, Integer, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://leidayu:leidayu@10.88.15.50:23306/invdb')
Base = declarative_base()

class Transaction(Base):
    __tablename__ = 't_transaction'

    id = Column(Integer, primary_key = True)
    dt = Column(Date)
    code = Column(String(50))
    operation = Column(String(50))
    portfolio = Column(String(50))
    sec_type = Column(String(50))
    quantity = Column(Numeric(20, 4))
    price = Column(Numeric(20, 4))
    tax = Column(Numeric(20, 4))
    other_charges = Column(Numeric(20, 4))
    amount = Column(Numeric(20, 4))

    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'), # 联合唯一索引
        Index('ix_id_name', 'name', 'email'), #给name和email创建普通索引，索引名为ix_id_name
    )

    def __repr__(self):
        return '%s(%d, %s, %s)' % (self.__class__.__name__, self.id, self.dt, self.code)

#class User(Base):
#
#    __tablename__ = 't_users'
#
#    id = Column(Integer, primary_key=True)
#    username = Column(String(64), nullable=False, index=True)
#    password = Column(String(64), nullable=False)
#    email = Column(String(64), nullable=False, index=True)
#
#
#    def __repr__(self):
#        return '%s(%r)' % (self.__class__.__name__, self.username)

def get_trans(date, code = None):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    res = []
    if (code == None):
        res = session.query(Transaction).filter(Transaction.dt == date).all()
    else:
        res = session.query(Transaction).filter(Transaction.dt == date, Transaction.code == code).all()
    session.close()
    return res

print get_trans('2016-03-07')

# create tables
# if __name__ == '__main__':
#      Base.metadata.create_all(engine)

# execute sql
# result = engine.execute("select * from t_transaction limit 20")
# res = result.fetchall()
# print res
