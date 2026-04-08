import unittest

from message_templates.whatsapp import build_whatsapp_meal_plan

json_plan = {'domingo': {'lunch': {'first': 'Paella'}},
         'lunes': {'lunch': 'Judías Verdes', 'dinner': 'Tortilla Francesa'},
         'martes': {'lunch': {'first': 'Lentejas con Rape', 'second': 'Chuleta Cerdo'}, 'dinner': 'Pechugas Empanadas'},
         'miercoles': {'lunch': {'first': 'Ensaladilla', 'second': 'Bakalao Vizcaina'}},         
         'viernes': {'lunch': {'first': 'Crema Calabacín', 'second': 'Escalopines'}, 'dinner': 'Tortilla Francesa'}}

expected = """🍽️*PLAN SEMANAL DE COMIDAS Y CENAS*🍽️

📅*SÁBADO*
🍴 ---
🌙 ---

📅*DOMINGO*
🍴 Paella
🌙 ---

📅*LUNES*
🍴 Judías Verdes
🌙 Tortilla Francesa

📅*MARTES*
🍴 Lentejas con Rape + Chuleta Cerdo
🌙 Pechugas Empanadas

📅*MIÉRCOLES*
🍴 Ensaladilla + Bakalao Vizcaina
🌙 ---

📅*JUEVES*
🍴 ---
🌙 ---

📅*VIERNES*
🍴 Crema Calabacín + Escalopines
🌙 Tortilla Francesa"""

class TestBuilder(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

    def test_given_meals_plan_dict_when_only_lunch_main_course_then_meal_plan_should_be_generated(self):
        expected2 = """🍽️*PLAN SEMANAL DE COMIDAS Y CENAS*🍽️

📅*SÁBADO*
🍴 ---
🌙 ---

📅*DOMINGO*
🍴 Filetes de Maza
🌙 ---

📅*LUNES*
🍴 ---
🌙 ---

📅*MARTES*
🍴 ---
🌙 ---

📅*MIÉRCOLES*
🍴 ---
🌙 ---

📅*JUEVES*
🍴 ---
🌙 ---

📅*VIERNES*
🍴 ---
🌙 ---"""
        plan = {'domingo': {'lunch': {'second': 'Filetes de Maza'}}}
        self.assertEqual(expected2, build_whatsapp_meal_plan(plan))


if __name__ == '__main__':
    unittest.main()        
