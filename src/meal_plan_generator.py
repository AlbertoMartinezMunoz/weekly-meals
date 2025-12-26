#!/usr/bin/env python3

import json
import sys
from pathlib import Path
from message_templates.whatsapp import build_whatsapp_meal_plan


def load_meal_plan(json_path: str) -> dict:
    """
    Load a meal plan JSON file and return it as a Python dictionary.
    """
    path = Path(json_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".json":
        raise ValueError("Input file must be a .json file")

    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError("Meal plan JSON must contain a JSON object at root level")

    return data


def main():
    if len(sys.argv) != 2:
        print("Usage: python load_meal_plan.py <meal_plan.json>")
        sys.exit(1)

    json_path = sys.argv[1]

    try:
        meal_plan = load_meal_plan(json_path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Output: the dictionary (for piping or debugging)
    print(meal_plan)

    message = build_whatsapp_meal_plan(meal_plan)

    print(message)


if __name__ == "__main__":
    main()
