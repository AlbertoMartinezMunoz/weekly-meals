from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Tuple

class MealsLoader(ABC):
    @abstractmethod
    def starters(self) -> List[Tuple[str, str]]:
        pass

    @abstractmethod
    def main_courses(self) -> List[Tuple[str, str]]:
        pass

    @abstractmethod
    def dinners(self) -> List[Tuple[str, str]]:
        pass