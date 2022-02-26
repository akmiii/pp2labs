#subtract five days from current date

import datetime

x = datetime.date.today()
y = datetime.timedelta(5)

print(x - y)
