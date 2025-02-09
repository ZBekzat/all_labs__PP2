from datetime import timedelta, datetime, time

now = datetime.now()
today = datetime(now.year, now.month, now.day,
                 now.hour, now.minute, now.second, now.microsecond)
today.replace(microsecond=0)
print(today)

# secondDate = datetime(f"0000-00-00 {time()}:{now.microsecond}",
#                       "%Y-%m-%d %H:%M:%S:%f")
# print(
#     now - secondDate
# )