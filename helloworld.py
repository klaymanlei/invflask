from flask import Flask, request, render_template
import config_flask
import json
import ast_query
import query_3ls
from scripts.db.mysql.mysql_utils import *

app = Flask(__name__)
app.config.from_object(config_flask)

@app.route('/')
def hello_world():
    return render_template('summary.html')
    # return 'hello world'

@app.route('/new_trans')
def input_trans():
    return render_template('input_transaction_tmp.html')

@app.route('/insert_trans', methods=['post','get'])
def insert_trans():
    dt = request.args.get('date')
    code = request.args.get('code')
    oper = request.args.get('oper')
    portf = request.args.get('portf')
    sectype = request.args.get('sectype')
    quantity = request.args.get('quantity')
    price = request.args.get('price')
    tax = request.args.get('tax')
    othercharge = request.args.get('othercharge')
    amount = request.args.get('amount')
    print (dt,code,oper,portf, sectype, quantity, price, tax, othercharge, amount)
    save_transaction(dt, code, oper, portf, sectype, quantity, price, tax, othercharge, amount)
    return render_template('ast_summary.html')

@app.route('/ast_summary')
def ast_summary():
    return render_template('ast_summary.html')

@app.route('/ast_line')
def ast_line():
    rs = ast_query.ast_line()
    #print rs
    return json.dumps(obj = rs)

@app.route('/candles_3ls/<code>')
def candles_3ls(code):
    period = request.args.get('type')
    rs = query_3ls.candles(code, period)
    #print rs
    return json.dumps(obj = rs)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
