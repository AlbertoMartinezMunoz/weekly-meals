from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

STARTERS = [('---', '---'), 
            ('Lentejas con Rape', 'Lentejas con Rape'), 
            ('Garbanzos con Bakalao', 'Garbanzos con Bakalao'), 
            ('Alubias con Calamar', 'Alubias con Calamar'), 
            ('Judias Verdes', 'Judias Verdes'),
            ('Cream de Calabacín', 'Cream de Calabacín') ,
            ('Ensaladilla', 'Ensaladilla'),
            ('Pisto con Huevo', 'Pisto con Huevo'),
            ('Paella','Paella')]

MAIN_COURSES = [('---', '---'), 
                ('Filetes de Maza', 'Filetes de Maza'),
                ('Filetes de Cabecero', 'Filetes de Cabecero'),
                ('Muslos de Pollo Plancha', 'Muslos de Pollo Plancha'),
                ('Muslos Pollo Asados', 'Muslos Pollo Asados'),
                ('Hamburguesa', 'Hamburguesa'),
                ('Chuleta Cerdo', 'Chuleta Cerdo'),
                ('Solomillo Cerdo', 'Solomillo Cerdo'),
                ('Bakalao Vizcaina', 'Bakalao Vizcaina')]

DINNER = [('---', '---'), 
          ('Sopa', 'Sopa'), 
          ('Tortilla Francesa', 'Tortilla Francesa'), 
          ('Tortilla Patata', 'Tortilla Patata'), 
          ('Bakalao Vizcaina', 'Bakalao Vizcaina'), 
          ('Pescado Rebozado', 'Pescado Rebozado'), 
          ('Filetes Lomo', 'Filetes Lomo'), 
          ('Pechuga Empanada', 'Pechuga Empanada')]

class WeeklyPlannerForm(FlaskForm):
    saturday_lunch_starter = SelectField('Saturday Lunch Starter', choices=STARTERS)
    saturday_lunch_main = SelectField('Saturday Lunch Starter', choices=MAIN_COURSES)
    saturday_dinner = SelectField('Saturday Lunch Starter', choices=DINNER)
    sunday_lunch_starter = SelectField('Sunday Lunch Starter', choices=STARTERS)
    sunday_lunch_main = SelectField('Sunday Lunch Starter', choices=MAIN_COURSES)
    sunday_dinner = SelectField('Sunday Lunch Starter', choices=DINNER)
    monday_lunch_starter = SelectField('Monday Lunch Starter', choices=STARTERS)
    monday_lunch_main = SelectField('Monday Lunch Starter', choices=MAIN_COURSES)
    monday_dinner = SelectField('Monday Lunch Starter', choices=DINNER)
    tuesday_lunch_starter = SelectField('Tuesday Lunch Starter', choices=STARTERS)
    tuesday_lunch_main = SelectField('Tuesday Lunch Starter', choices=MAIN_COURSES)
    tuesday_dinner = SelectField('Tuesday Lunch Starter', choices=DINNER)
    wednesday_lunch_starter = SelectField('Wednesday Lunch Starter', choices=STARTERS)
    wednesday_lunch_main = SelectField('Wednesday Lunch Starter', choices=MAIN_COURSES)
    wednesday_dinner = SelectField('Wednesday Lunch Starter', choices=DINNER)
    thursday_lunch_starter = SelectField('Thursday Lunch Starter', choices=STARTERS)
    thursday_lunch_main = SelectField('Thursday Lunch Starter', choices=MAIN_COURSES)
    thursday_dinner = SelectField('Thursday Lunch Starter', choices=DINNER)
    friday_lunch_starter = SelectField('Friday Lunch Starter', choices=STARTERS)
    friday_lunch_main = SelectField('Friday Lunch Starter', choices=MAIN_COURSES)
    friday_dinner = SelectField('Friday Lunch Starter', choices=DINNER)
    submit = SubmitField('Generar Plan')