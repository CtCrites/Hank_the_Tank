#############################################################################
# Program Title: Time-find
# Creation Date: 1/23/24
# Description: This program will gather and format the date and time for Hank
#
##### Imports
from datetime import datetime
from geopy.geocoders import Nominatim
from pyowm.owm import OWM
import aladhan
##### Functions

### Time and Date ###
def currenttime():
	date_and_time = str(datetime.now())
	time_now = formattime(date_and_time)
	return time_now

def currentdate():
	date_and_time = str(datetime.now())
	date_now = formatdate(date_and_time)
	return date_now

def formatdate(date_and_time):
	date_and_time = date_and_time.split()
	date = date_and_time[0].split("-")
	year = date[0]
	month = int(date[1])
	day = date[2]
	match month:
		case 1:
			month = "January "
		case 2:
			month = "February "
		case 3:
			month = "March "
		case 4:
			month = "April "
		case 5:
			month = "May "
		case 6:
			month = "June "
		case 7:
			month = "July "
		case 8:
			month = "August "
		case 9:
			month = "September "
		case 10:
			month = "October "
		case 11:
			month = "November "
		case 12:
			month = "December "
	formatted_date = month + day + ", " + year
	return formatted_date
	
def formattime(date_and_time):
	date_and_time = date_and_time.split()
	time = date_and_time[1].split(":")
	hour = time[0]
	minute = time[1]
	indicator = " AM"
	if int(hour) > 12:
		hour = str(int(hour) - 12)
		indicator = " PM"
	formatted_time = hour + ":" + minute + indicator
	return formatted_time
	
def timestamp():
	date_and_time = str(datetime.now())
	time = date_and_time.split()[1]
	time = time[:5]
	date = date_and_time.split()[0]
	date = date.split("-")
	date = date[1] + ":" + date[2] + ":" + date[0][2:4]
	timestamp = date + "  " + time
	return timestamp
	
### Location ###
def getcoordinates(place):
	geo_locator = Nominatim(user_agent="Hank")
	full_location = geo_locator.geocode(place)
	raw_location = full_location.raw
	longitude = raw_location['lon']
	latitude = raw_location['lat']
	return float(longitude), float(latitude)
	
def coordweather(longitude, latitude):
	owm = OWM('de2268604699c2bd7aa882d139664df1')
	mgr = owm.weather_manager()
	weather = mgr.weather_at_coords(latitude, longitude).weather
	temp_info = weather.temperature('fahrenheit')
	condition = weather.status
	return temp_info, condition
	
def weather(place):
	place = place + ", USA"
	longitude, latitude = getcoordinates(place)
	temp_info, condition = coordweather(longitude, latitude)
	currenttemp = float(temp_info['temp'])
	formatted_weather = "It is currently {} degrees in {}, with some {}".format(currenttemp, place, condition)
	return formatted_weather
	
def prayer_times(place):
	longitude, latitude = getcoordinates(place)
	location = aladhan.Coordinates(latitude, longitude)
	client = aladhan.Client(location)
	adhan = client.get_today_times()
	times = []
	for time in adhan:
		times.append("{} is {}".format(time.get_en_name(), time.readable_timing(show_date=False)))
	return times
#####
prayer_times("Kutztown, Pennsylvania, USA")
#Last Updated: 


