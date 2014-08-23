import MySQLdb
import urllib2, urllib, re, sys
import xml
from datetime import datetime

##reads from database and gives it to tcl

def showweather(woeid, n):
	try:
		# connect
		db = MySQLdb.connect(host="localhost", user="root", passwd="4c9hq5ea", db="cmaxopaw_weather")
		cursor = db.cursor()
		
		# execute SQL select statement
		cursor.execute("SELECT * FROM  `records` WHERE  `woeid` = " + woeid +" AND date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL " + n + " DAY)")
		# get the number of rows in the resultset
		numrows = int(cursor.rowcount)
		print "Weather will be as follows:"
		# get and display one row at a time.
		for x in range(0,numrows):
		    row = cursor.fetchone()
		    print "Weather for " + str(row[4]) + ", " + str(row[5]) + " will be between " + str(row[6]) + " and " + str(row[7]) + " Celcius (" + str(row[8]) + ")"
		#commit your changes)
		db.commit()
	except Exception as e:
		print '<>',e

##custom function for datetime conversion
def yahootosql(yahoodate):
	sqldate = datetime.strptime(yahoodate, '%d %b %Y').strftime('%Y-%m-%d')
	return sqldate

##main code to write and display on tcl interface	
if __name__ == '__main__':
	showweather(sys.argv[1], sys.argv[2])

