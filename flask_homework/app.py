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


# <HW32> Task 3: Endpoint returns HTML
@app.route('/')
def root_page():
    app.logger.info('Request to endpoint "/"')   # <HW32> Task 4: Logging in function
    return '''
    <div><a href='http://127.0.0.1:5000/hello'>Hello page</a></div>
    <div>-</div>
    <div><a href='http://127.0.0.1:5000/json'>Return json</a></div>
    <div>-</div>
    <div><a href='http://127.0.0.1:5000/html'>Return html</a></div>
    '''


# <HW32> Task 2: Endpoint '/hello' returns 'Hello world'
@app.route('/hello', methods=['GET'])
def hello_world():
    app.logger.info('Request to endpoint "/hello"')   # <HW32> Task 4: Logging in function
    return 'Hello World!'


# <HW32> Task 3: Endpoint returns JSON
@app.route('/json')
def return_json():
    app.logger.info('Request to endpoint "/json"')    # <HW32> Task 4: Logging in function
    return [
        {'item 1': {'parameter 1': 'value 1', 'parameter 2': 'value 2'}},
        {'item 2': {'nested item': {'parameter 1': 'value 1', 'parameter 2': 'value 2'}}}
    ]


# <HW32> Task 3: Endpoint returns HTML
@app.route('/html')
def return_html():
    app.logger.info('Request to endpoint "/html"')    # <HW32> Task 4: Logging in function
    return '''
    <h1>This is HTML return</h1>
    '''


if __name__ == '__main__':
    app.run(debug=True)
