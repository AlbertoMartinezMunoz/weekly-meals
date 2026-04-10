from flask import Flask, render_template, flash
from webui.forms import WeeklyPlannerForm
from message_templates.whatsapp import build_whatsapp_meal_plan
from mealsstore.jsonloader import JsonFileLoader

import os
SECRET_KEY = os.urandom(32)


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/weekly-meals-planner', methods=['GET', 'POST'])
def index():
    loader = JsonFileLoader("/var/www/weekly-meals/meals.json")
    starters = loader.starters()
    main_courses = loader.main_courses()
    dinners = loader.dinners()

    form = WeeklyPlannerForm()
    
    if form.validate_on_submit():
        weekly_plan = {}
        if form.saturday_lunch_starter.data and form.saturday_lunch_starter.data != starters[0][0]:
            weekly_plan.setdefault("sabado", {}).setdefault('lunch', {})['first'] =  form.saturday_lunch_starter.data
        if form.saturday_lunch_main.data and form.saturday_lunch_main.data != main_courses[0][0]:
            weekly_plan.setdefault("sabado", {}).setdefault('lunch', {})['second'] = form.saturday_lunch_main.data
        if form.saturday_dinner.data and form.saturday_dinner.data != dinners[0][0]:
            weekly_plan.setdefault("sabado", {})['dinner'] = form.saturday_dinner.data
        if form.sunday_lunch_starter.data and form.sunday_lunch_starter.data != starters[0][0]:
            weekly_plan.setdefault("domingo", {}).setdefault('lunch', {})['first'] =  form.sunday_lunch_starter.data
        if form.sunday_lunch_main.data and form.sunday_lunch_main.data != main_courses[0][0]:
            weekly_plan.setdefault("domingo", {}).setdefault('lunch', {})['second'] = form.sunday_lunch_main.data
        if form.sunday_dinner.data and form.sunday_dinner.data != dinners[0][0]:
            weekly_plan.setdefault("domingo", {})['dinner'] = form.sunday_dinner.data
        if form.monday_lunch_starter.data and form.monday_lunch_starter.data != starters[0][0]:
            weekly_plan.setdefault("lunes", {}).setdefault('lunch', {})['first'] =  form.monday_lunch_starter.data
        if form.monday_lunch_main.data and form.monday_lunch_main.data != main_courses[0][0]:
            weekly_plan.setdefault("lunes", {}).setdefault('lunch', {})['second'] = form.monday_lunch_main.data
        if form.monday_dinner.data and form.monday_dinner.data != dinners[0][0]:
            weekly_plan.setdefault("lunes", {})['dinner'] = form.monday_dinner.data
        if form.tuesday_lunch_starter.data and form.tuesday_lunch_starter.data != starters[0][0]:
            weekly_plan.setdefault("martes", {}).setdefault('lunch', {})['first'] =  form.tuesday_lunch_starter.data
        if form.tuesday_lunch_main.data and form.tuesday_lunch_main.data != main_courses[0][0]:
            weekly_plan.setdefault("martes", {}).setdefault('lunch', {})['second'] = form.tuesday_lunch_main.data
        if form.tuesday_dinner.data and form.tuesday_dinner.data != dinners[0][0]:
            weekly_plan.setdefault("martes", {})['dinner'] = form.tuesday_dinner.data
        if form.wednesday_lunch_starter.data and form.wednesday_lunch_starter.data != starters[0][0]:
            weekly_plan.setdefault("miercoles", {}).setdefault('lunch', {})['first'] =  form.wednesday_lunch_starter.data
        if form.wednesday_lunch_main.data and form.wednesday_lunch_main.data != main_courses[0][0]:
            weekly_plan.setdefault("miercoles", {}).setdefault('lunch', {})['second'] = form.wednesday_lunch_main.data
        if form.wednesday_dinner.data and form.wednesday_dinner.data != dinners[0][0]:
            weekly_plan.setdefault("miercoles", {})['dinner'] = form.wednesday_dinner.data
        if form.thursday_lunch_starter.data and form.thursday_lunch_starter.data != starters[0][0]:
            weekly_plan.setdefault("jueves", {}).setdefault('lunch', {})['first'] =  form.thursday_lunch_starter.data
        if form.thursday_lunch_main.data and form.thursday_lunch_main.data != main_courses[0][0]:
            weekly_plan.setdefault("jueves", {}).setdefault('lunch', {})['second'] = form.thursday_lunch_main.data
        if form.thursday_dinner.data and form.thursday_dinner.data != dinners[0][0]:
            weekly_plan.setdefault("jueves", {})['dinner'] = form.thursday_dinner.data
        if form.friday_lunch_starter.data and form.friday_lunch_starter.data != starters[0][0]:
            weekly_plan.setdefault("viernes", {}).setdefault('lunch', {})['first'] =  form.friday_lunch_starter.data
        if form.friday_lunch_main.data and form.friday_lunch_main.data != main_courses[0][0]:
            weekly_plan.setdefault("viernes", {}).setdefault('lunch', {})['second'] = form.friday_lunch_main.data
        if form.friday_dinner.data and form.friday_dinner.data != dinners[0][0]:
            weekly_plan.setdefault("viernes", {})['dinner'] = form.friday_dinner.data

        flash(build_whatsapp_meal_plan(weekly_plan))
    return render_template('planner.html', form=form)
