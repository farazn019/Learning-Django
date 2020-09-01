from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return "Hello World!"


@app.route('/')
def main_page():
    return '<h2 style="text-align: center">This is THE main page</h2>'


if __name__ == '__main__':
    app.run(debug=True)