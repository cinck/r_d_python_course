from flask import Flask

app = Flask(__name__)


@app.route('/')
def root_page():
    return '''
    <div><a href='http://127.0.0.1:5000/hello'>Hello page</a></div>
    <div>-</div>
    <div><a href='http://127.0.0.1:5000/json'>Return json</a></div>
    <div>-</div>
    <div><a href='http://127.0.0.1:5000/html'>Return html</a></div>
    '''


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/json')
def return_json():
    return [
        {'item 1': {'parameter 1': 'value 1', 'parameter 2': 'value 2'}},
        {'item 2': {'nested item': {'parameter 1': 'value 1', 'parameter 2': 'value 2'}}}
    ]


@app.route('/html')
def return_html():
    return '''
    <h1>Return HTML</h1>
    '''


if __name__ == '__main__':
    app.run(debug=True)
