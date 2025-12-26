# whatsapp_meal_plan.py

DAYS_ORDER = [
    "sabado",
    "domingo",
    "lunes",
    "martes",
    "miercoles",
    "jueves",
    "viernes",
]

DAY_NAMES = {
    "sabado": "SÁBADO",
    "domingo": "DOMINGO",
    "lunes": "LUNES",
    "martes": "MARTES",
    "miercoles": "MIÉRCOLES",
    "jueves": "JUEVES",
    "viernes": "VIERNES",
}

HEADER = "🍽️*PLAN SEMANAL DE COMIDAS Y CENAS*🍽️"


def _format_lunch(lunch):
    """
    Lunch can be:
    - dict with 'first' / 'second'
    - string
    - missing
    """
    if isinstance(lunch, dict):
        first = lunch.get("first")
        second = lunch.get("second")

        if first and second:
            return f"{first} + {second}"
        return first or "---"

    if isinstance(lunch, str):
        return lunch

    return "---"


def _format_dinner(dinner):
    if isinstance(dinner, str):
        return dinner
    return "---"


def build_whatsapp_meal_plan(meal_plan: dict) -> str:
    """
    Build a WhatsApp-formatted weekly meal plan message.
    """
    lines = [HEADER, ""]

    for day_key in DAYS_ORDER:
        day_data = meal_plan.get(day_key, {})
        day_name = DAY_NAMES[day_key]

        lunch = _format_lunch(day_data.get("lunch"))
        dinner = _format_dinner(day_data.get("dinner"))

        lines.extend([
            f"📅*{day_name}*",
            f"🍴 {lunch}",
            f"🌙 {dinner}",
            "",
        ])

    return "\n".join(lines).rstrip()
