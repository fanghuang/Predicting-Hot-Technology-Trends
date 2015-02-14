from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

def stringToDate(str):
	date_parts = [int(x) for x in str.split('-')]
	return date(year=date_parts[0], month=date_parts[1], day=date_parts[2])