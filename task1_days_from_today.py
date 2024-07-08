from datetime import datetime

today = datetime.today()


def get_days_from_today(date: str, format="%Y-%m-%d") -> int:
    try:
        date = datetime.strptime(date, format)
        return (today - date).days
    except Exception as e:
        print(e)
        return None


res = get_days_from_today("2023-10-0AA9")
print(res)
