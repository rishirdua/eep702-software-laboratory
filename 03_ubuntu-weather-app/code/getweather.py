import MySQLdb
import urllib2, urllib, re, sys
import xml
from datetime import datetime

##fetches and inserts into database
def parseweather(woeid):
	try:

		##define required elements		
		import xml.etree.ElementTree as ET
		namespaces = {'yweather': 'http://xml.weather.yahoo.com/ns/rss/1.0'} # add more as needed

		##get records
		proxy = urllib2.ProxyHandler({'https': '10.10.78.62:3128','http': '10.10.78.62:3128'})
		opener = urllib2.build_opener(proxy)
		urllib2.install_opener(opener)
		query_args = { 'w':woeid }
		encoded_args = urllib.urlencode(query_args)
		url = 'http://weather.yahooapis.com/forecastrss?' + encoded_args
		f = urllib2.urlopen(url)
		xmldata = f.read()
		root = ET.fromstring(xmldata)

		#root = ET.parse('data_weather.xml').getroot() 
		forecasts = root.find('channel').find('item').findall('yweather:forecast', namespaces=namespaces)
		
		## connect to database
		db = MySQLdb.connect(host="localhost", user="root", passwd="4c9hq5ea", db="cmaxopaw_weather")
		cursor = db.cursor()
		##parse and insert if not already in database
		for thisday in forecasts:
			cursor.execute("SELECT * FROM  `records` WHERE  `woeid` = " + woeid + " AND `date` = \'" + yahootosql(thisday.get('date')) + "\'")
			numrows = int(cursor.rowcount)
			if numrows == 0:
				cursor.execute ("INSERT INTO records (timestamp, userid, woeid, day, date, low, high, text, code) values (CURRENT_TIMESTAMP, 1234, " + str(woeid) + ", \"" + thisday.get('day') + "\", \'" + yahootosql(thisday.get('date')) + "\', " + thisday.get('low') + ", " + thisday.get('high') + ", \"" + thisday.get('text') + "\", " + thisday.get('code') + ")")
		#commit your changes
		db.commit()
	except Exception as e:
		print '<>',e

##custom function to convert date time format
def yahootosql(yahoodate):
	sqldate = datetime.strptime(yahoodate, '%d %b %Y').strftime('%Y-%m-%d')
	return sqldate
	
##main file, run as parseweather(woeid)
if __name__ == '__main__':
	parseweather(sys.argv[1])	

