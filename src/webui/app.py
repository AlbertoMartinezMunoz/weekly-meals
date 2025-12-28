from flask import Flask, render_template


app = Flask(__name__)


@app.route('/weekly-meals-planner')
def index():
    return render_template('planner.html')
