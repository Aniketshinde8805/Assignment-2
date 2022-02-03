# 8	Write a python program to print the week day, day number of a current date 
# 	And print the dates and days of past and current week (use datetime module)

# 	Ex- current date - 2017-10-11
# 		week day - Wed
# 		day number - 2

# 	current week
# 		2017-10-09 Mon
# 		2017-10-10 Tue
# 		2017-10-11 Wed
# 		2017-10-12 Thu
# 		2017-10-13 Fri
# 		2017-10-14 Sat
# 		2017-10-15 Sun

# 	Past week
# 		2017-10-02 Mon
# 		2017-10-03 Tue
# 		2017-10-04 Wed
# 		2017-10-05 Thu
# 		2017-10-06 Fri
# 		2017-10-07 Sat
# 		2017-10-08 Sun


import datetime
from datetime import timedelta





# def week():
# 	print("Current week")
	
# 	for i in range(7):
# 		t1=datetime.date.today()+timedelta(days=i)
# 		print(t1.isocalendar()[1])
# 		print(datetime.datetime.strftime(t1,"%Y-%m-%d %a" ))

# 	print("Past Week")
# 	for i in reversed(range(7)):
# 		t2=datetime.date.today()-timedelta(days=i)
# 		print(datetime.datetime.strftime(t2,"%Y-%m-%d %a" ))

# week()


import datetime
from datetime import timedelta
def calculate_week():
	print("Current week")
	t1=datetime.date.today()   #calculating today's date
	week=t1.weekday()             #calculating weekday
	t0=datetime.date.today()-timedelta(days=week)  #calculating date of first day of current week
	
	for i in range(7):     #for loop for iterating through the dates of current week
		dd=t0+timedelta(days=i)   
		
		print(datetime.datetime.strftime(dd,"%Y-%m-%d %a" ))

	print("Past Week")
	t2=t0-timedelta(days=7)   # calculating past week's first day
	for i in range(7):   #for loop for iterating through the dates of past week
		dd2=t2+timedelta(days=i)
		print(datetime.datetime.strftime(dd2,"%Y-%m-%d %a" ))

calculate_week()