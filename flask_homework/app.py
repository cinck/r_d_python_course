from flask import Flask
from logging.config import dictConfig


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)


@app.route('/')
def root_page():
    app.logger.info('Request to endpoint "/"')
    return '''
    <div><a href='http://127.0.0.1:5000/hello'>Hello page</a></div>
    <div>-</div>
    <div><a href='http://127.0.0.1:5000/json'>Return json</a></div>
    <div>-</div>
    <div><a href='http://127.0.0.1:5000/html'>Return html</a></div>
    '''


@app.route('/hello')
def hello_world():
    app.logger.info('Request to endpoint "/hello"')
    return '<h1>Hello World!</h1>'


@app.route('/json')
def return_json():
    app.logger.info('Request to endpoint "/json"')
    return [
        {'item 1': {'parameter 1': 'value 1', 'parameter 2': 'value 2'}},
        {'item 2': {'nested item': {'parameter 1': 'value 1', 'parameter 2': 'value 2'}}}
    ]


@app.route('/html')
def return_html():
    app.logger.info('Request to endpoint "/html"')
    return '''
    <h1>This is HTML return</h1>
    '''


if __name__ == '__main__':
    app.run(debug=True)
