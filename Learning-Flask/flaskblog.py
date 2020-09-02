from flask import Flask, render_template


app = Flask(__name__)


posts = [
    {
        'author': 'Faraz Naseem',
        'title': 'Blog Post 1',
        'content': 'The content for the first post',
        'date_posted': 'August 31, 2020'
    },
    {
        'author': 'Zaraf Maseen',
        'title': 'Blog Post 2',
        'content': 'The content for the second post',
        'date_posted': 'September 1, 2020'
    }
]


@app.route('/hello')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/')
@app.route('/main')
def main_page():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)