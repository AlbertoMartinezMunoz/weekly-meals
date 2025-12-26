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

    def test_given_when_then_(self):
        self.assertEqual(expected, build_whatsapp_meal_plan(json_plan))


if __name__ == '__main__':
    unittest.main()        