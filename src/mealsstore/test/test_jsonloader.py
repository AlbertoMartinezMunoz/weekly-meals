import unittest

from mealsstore.jsonloader import JsonFileLoader

class TestJsonLoader(unittest.TestCase):

    def setUp(self) -> None:
        self.loader = JsonFileLoader("src/mealsstore/test/test.json")
        super().setUp()

    def test_given_json_file_when_retrieving_starters_then_return_list(self):
        expected_starters = [('StarterKey0', 'StarterValue0'),
                             ('StarterKey1', 'StarterValue1'),
                             ]
        self.assertEqual(expected_starters,self.loader.starters())

    def test_given_json_file_when_retrieving_main_courses_then_return_list(self):
        expected_main_courses = [('MainKey0', 'MainValue0'),]
        self.assertEqual(expected_main_courses,self.loader.main_courses())

    def test_given_json_file_when_retrieving_dinners_then_return_list(self):
        expected_dinners = [('DinnerKey0', 'DinnerValue0'),
                             ('DinnerKey1', 'DinnerValue1'),
                             ]
        self.assertEqual(expected_dinners,self.loader.dinners())


if __name__ == '__main__':
    unittest.main()        