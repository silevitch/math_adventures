import datetime 
from datetime import timedelta
import re

one_day = datetime.timedelta(1)

day = datetime.date(1,1,1)

while day.year < 3000:
	day_string = re.sub('-', '', day.isoformat())

	reverse_day_string = ''.join(reversed(day_string))

	if day_string == reverse_day_string:
		print day.isoformat()

	day += one_day

