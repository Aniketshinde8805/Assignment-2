# 5.	Write a python program to calculate number of days between two dates as given below
# 	(hint - convert input to string, string to time tuple)
# 	Input
# 	Date1 - 2015/07/02
#     Date2 - 2015/07/11
#     Expected output: 9 days


import datetime

def difference(d1,d2):
	d1=datetime.datetime.strptime(d1,"%Y-%m-%d")
	d2=datetime.datetime.strptime(d2,"%Y-%m-%d")

	print(d2-d1)

difference("2015-07-02","2015-7-11")