# 1. 	Write a Python program to get next day of a given date 
# 	take input from user as as string date
# 	use datetime module

import datetime
from datetime import timedelta

def get_next_day(tt):
	datetime_obj = datetime.datetime.strptime(tt, '%Y-%m-%d')
	print(datetime_obj+timedelta(days=1))         #adding 1 day to the user given date

	print(datetime.date.today())

get_next_day("2022-2-1")