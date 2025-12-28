from flask import Flask

app = Flask(__name__)


@app.route('/weekly-meals-planner')
def index():
    return '<h2>WEEKLY MEALS PLANNER<h2>'
