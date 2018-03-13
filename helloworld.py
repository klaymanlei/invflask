from flask import Flask, render_template
import config_flask
import json
import ast_query
import query_3ls 

app = Flask(__name__)
app.config.from_object(config_flask)

@app.route('/')
def hello_world():
    return render_template('summary.html')
    # return 'hello world'

@app.route('/ast_line')
def ast_line():
    rs = ast_query.ast_line()
    #print rs
    return json.dumps(obj = rs)

@app.route('/candles_3ls')
def candles_3ls():
    rs = query_3ls.candles('510050', 'day')
    #print rs
    return json.dumps(obj = rs)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
