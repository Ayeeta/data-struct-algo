import datetime

def dayOfTheWeek(self, day, month, year):
    days = ['Monday', 'Tuesday','Wednesday','Thursday','Friday',
               'Saturday', 'Sunday']
    day_number = datetime.date(year,month,day).weekday()
    return days[day_number]