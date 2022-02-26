#print yesterday, today, tomorrow

import datetime

x = datetime.date.today()
y = datetime.timedelta(1)

print(x - y)
print(x)
print(x + y)