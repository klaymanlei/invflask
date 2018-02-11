from flask import Flask, render_template
import config_flask

app = Flask(__name__)
app.config.from_object(config_flask)

@app.route('/')
def hello_world():
    return render_template('summary.html')
    # return 'hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
