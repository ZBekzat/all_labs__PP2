from datetime import timedelta, datetime, time

date1 = datetime.now()
date2 = datetime.strptime("2025/02/03 21:00:03.123456",
                          "%Y/%m/%d %H:%M:%S.%f")
result = date1 - date2
total = result.total_seconds()
total = result.days * 86400 + result.microseconds + result.seconds
print(total)