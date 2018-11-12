#coding: utf-8

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

DATABASE = 'mysql'
CONNECTOR = 'mysqldb'
USERNAME = 'leidayu'
PASSWORD = 'leidayu'
HOST = '10.88.15.50'
PORT = '23306'
DB = 'invdb'

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://leidayu:leidayu@10.88.15.50:23306/invdb'
app.config['SQLALCHEMY_DATABASE_URI'] = '%s+%s://%s:%s@%s:%s/%s' % (DATABASE, CONNECTOR, USERNAME, PASSWORD, HOST, PORT, DB)
db = SQLAlchemy(app)
#也可以db = SQLAlchemy()        db.init_app(app)