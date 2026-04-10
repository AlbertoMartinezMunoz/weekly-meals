from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from mealsstore.jsonloader import JsonLoader


class WeeklyPlannerForm(FlaskForm):
    loader = JsonLoader("meals.json")
    starters = loader.starters()
    main_courses = loader.main_courses()
    dinners = loader.dinners()

    saturday_lunch_starter = SelectField('Saturday Lunch Starter', choices=starters)
    saturday_lunch_main = SelectField('Saturday Lunch Starter', choices=main_courses)
    saturday_dinner = SelectField('Saturday Lunch Starter', choices=dinners)
    sunday_lunch_starter = SelectField('Sunday Lunch Starter', choices=starters)
    sunday_lunch_main = SelectField('Sunday Lunch Starter', choices=main_courses)
    sunday_dinner = SelectField('Sunday Lunch Starter', choices=dinners)
    monday_lunch_starter = SelectField('Monday Lunch Starter', choices=starters)
    monday_lunch_main = SelectField('Monday Lunch Starter', choices=main_courses)
    monday_dinner = SelectField('Monday Lunch Starter', choices=dinners)
    tuesday_lunch_starter = SelectField('Tuesday Lunch Starter', choices=starters)
    tuesday_lunch_main = SelectField('Tuesday Lunch Starter', choices=main_courses)
    tuesday_dinner = SelectField('Tuesday Lunch Starter', choices=dinners)
    wednesday_lunch_starter = SelectField('Wednesday Lunch Starter', choices=starters)
    wednesday_lunch_main = SelectField('Wednesday Lunch Starter', choices=main_courses)
    wednesday_dinner = SelectField('Wednesday Lunch Starter', choices=dinners)
    thursday_lunch_starter = SelectField('Thursday Lunch Starter', choices=starters)
    thursday_lunch_main = SelectField('Thursday Lunch Starter', choices=main_courses)
    thursday_dinner = SelectField('Thursday Lunch Starter', choices=dinners)
    friday_lunch_starter = SelectField('Friday Lunch Starter', choices=starters)
    friday_lunch_main = SelectField('Friday Lunch Starter', choices=main_courses)
    friday_dinner = SelectField('Friday Lunch Starter', choices=dinners)
    submit = SubmitField('Generar Plan')
