from datetime import timedelta, datetime

today = datetime.today()
yesterday = today - timedelta(1)
tomorrow = today + timedelta(1)
print(f"Yesterday: {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")