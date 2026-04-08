from typing import List, Tuple
from mealsstore.mealsloader import MealsLoader

import json

class JsonLoader(MealsLoader):

    def __init__(self, path: str) -> None:
        with open(path, 'r') as file:
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