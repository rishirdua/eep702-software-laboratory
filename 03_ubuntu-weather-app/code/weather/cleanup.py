import MySQLdb
import urllib2, urllib, re, sys
import xml
from datetime import datetime

##removes all records older than 30 days.. run as cron job
def cleandb(woeid):
	try:
		# connect to database
		db = MySQLdb.connect(host="localhost", user="root", passwd="4c9hq5ea", db="cmaxopaw_weather")
		cursor = db.cursor()
		cursor.execute("SELECT * FROM  `records` WHERE  `date` < DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
		db.commit()
	except Exception as e:
		print '<>',e
	
#main file, run as parseweather(woeid)
if __name__ == '__main__':
	cleandb()	

