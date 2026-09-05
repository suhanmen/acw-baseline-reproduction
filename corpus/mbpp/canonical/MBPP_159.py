def month_season(month,days):
 if month in ('January', 'February', 'March'):
	 season = 'winter'
 elif month in ('April', 'May', 'June'):
	 season = 'spring'
 elif month in ('July', 'August', 'September'):
	 season = 'summer'
 else:
	 season = 'autumn'
 if (month == 'March') and (days > 19):
	 season = 'spring'
 elif (month == 'June') and (days > 20):
	 season = 'summer'
 elif (month == 'September') and (days > 21):
	 season = 'autumn'
 elif (month == 'October') and (days > 21):
	 season = 'autumn'
 elif (month == 'November') and (days > 21):
	 season = 'autumn'
 elif (month == 'December') and (days > 20):
	 season = 'winter'
 return season