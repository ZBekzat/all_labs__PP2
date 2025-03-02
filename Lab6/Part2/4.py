import time
number = int(input())
ms = int(input())
time.sleep(ms / 1000)
print(f"Square root of {number} after {ms} miliseconds is {number ** 0.5}")