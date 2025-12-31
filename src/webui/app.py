from flask import Flask, render_template, flash
from webui.forms import WeeklyPlannerForm

import os
SECRET_KEY = os.urandom(32)


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/weekly-meals-planner', methods=['GET', 'POST'])
def index():
    form = WeeklyPlannerForm()
    if form.validate_on_submit():
        weekly_plan = {'sabado': {'lunch': {'first': form.saturday_lunch_starter.data, 'second': form.saturday_lunch_main.data}, 'dinner': form.saturday_dinner.data},
                       'domingo': {'lunch': {'first': form.sunday_lunch_starter.data, 'second': form.sunday_lunch_main.data}, 'dinner': form.sunday_dinner.data},
                       'lunes': {'lunch': {'first': form.monday_lunch_starter.data, 'second': form.monday_lunch_main.data}, 'dinner': form.monday_dinner.data},
                       'martes': {'lunch': {'first': form.tuesday_lunch_starter.data, 'second': form.tuesday_lunch_main.data}, 'dinner': form.tuesday_dinner.data},
                       'miercoles': {'lunch': {'first': form.wednesday_lunch_starter.data, 'second': form.wednesday_lunch_main.data}, 'dinner': form.wednesday_dinner.data},
                       'jueves': {'lunch': {'first': form.thursday_lunch_starter.data, 'second': form.thursday_lunch_main.data}, 'dinner': form.thursday_dinner.data},
                       'viernes': {'lunch': {'first': form.friday_lunch_starter.data, 'second': form.friday_lunch_main.data}, 'dinner': form.friday_dinner.data}}
        flash(weekly_plan)
    return render_template('planner.html', form=form)
