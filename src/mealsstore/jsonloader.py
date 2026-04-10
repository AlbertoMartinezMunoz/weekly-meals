from typing import List, Tuple
from mealsstore.mealsloader import MealsLoader

import json

class JsonFileLoader(MealsLoader):
    default_json_file_path = "meals.json"

    def __init__(self, path: str) -> None:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            with open(self.default_json_file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
    
    def starters(self) -> List[Tuple[str, str]]:
        return self._meals("starters")
    
    def main_courses(self) -> List[Tuple[str, str]]:
        return self._meals("main_courses")

    def dinners(self) -> List[Tuple[str, str]]:
        return self._meals("dinners")

    def _meals(self, mealtype: str) -> List[Tuple[str, str]]:
        meals = []
        for meal in self.data.get(mealtype):
            meals.append(tuple(meal))
        return meals