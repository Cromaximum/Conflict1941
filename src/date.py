MONTHS = ['January','February','March','April', 'May',
	'June','July','August','September','October',
	'November', 'December']

month_cnt = 6

class date:
    hour = 0
    day = 22
    month = MONTHS[month_cnt]
    year = 1941

def print_date_c(date):
    print("")
    print(str(date.hour) + ":00 " + date.month + " " + str(date.day) + " " + str(date.year))
    print("")
    print("-----------")

def next_month(date):
	global month_cnt
	month_cnt += 1
	date.month = MONTHS[month_cnt]
	date.day = 1

def iterate_by_hour(date):
	global month_cnt
	if(date.hour == 24):
		date.hour = 1
		if(date.day == 28 and date.month == 'February'):
			next_month(date)
		if(date.day == 30 and date.month == 'April' or date.month == 'June' 
			or date.month == 'September' or date.month == 'November'):
			next_month(date)
		if(date.day == 31 and date.month == 'December'):
			month_cnt = -1
			next_month(date)
		elif(date.day == 31):
			next_month(date)
		else:
			date.day += 1
	else:
		date.hour += 1
			
