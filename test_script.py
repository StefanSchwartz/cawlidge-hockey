import datetime

date_string = '3/2/1998'
datetime_object = datetime.datetime.strptime(date_string, '%m/%d/%Y')
year = datetime_object.year
month = datetime_object.month
day = datetime_object.day
print(datetime.date(year, month, day))
