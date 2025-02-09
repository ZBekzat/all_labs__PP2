from datetime import datetime, date
from datetime import timedelta, datetime

today = datetime.today()
fiveDays = timedelta(days=5)
print(today - fiveDays)