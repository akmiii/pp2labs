#calculate two date difference in seconds.

import datetime

d1 = datetime.datetime.strptime(input(), '%Y-%m-%d')
d2 = datetime.datetime.strptime(input(), '%Y-%m-%d')
differ = d1 - d2
print(differ.total_seconds())