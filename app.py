from flask import Flask, render_template, request
from search import search4letters as s4l


app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello Vikaaaaa! <3 <3 <3'


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(s4l(phrase, letters))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


if __name__ == "__main__":
    app.run(debug=True)
