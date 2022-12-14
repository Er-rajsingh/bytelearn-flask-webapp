from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"


@app.route('/time')
def time():
    date = datetime.now()
    return str(date)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
