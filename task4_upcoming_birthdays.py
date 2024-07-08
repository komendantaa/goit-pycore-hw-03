from datetime import datetime, timedelta

WEEK = 7
WORKING_DAYS = 5


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today = datetime.today().date()
    event_from = today
    event_to = today + timedelta(days=WEEK)

    result = []

    for user in users:
        date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        date = date.replace(year=today.year)
        if date < event_from or date > event_to:
            continue

        if date.isoweekday() > WORKING_DAYS:
            correct_to_monday = 1 if date.isoweekday() - WORKING_DAYS == 2 else 2
            date = date + timedelta(days=correct_to_monday)

        result.append({"name": user["name"], "congratulation_date": date})

    return result


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
