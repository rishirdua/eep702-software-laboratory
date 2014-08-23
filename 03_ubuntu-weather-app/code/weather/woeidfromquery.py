import MySQLdb
import urllib2, urllib, re, sys
import xml
from datetime import datetime

## gets woeid from query -helper function
def getwoeid(searchstring):
	try:
		import xml.etree.ElementTree as ET
		namespaces = {'yweather': 'http://www.yahooapis.com/v1/base.rng'} # add more as needed
		#get records
		proxy = urllib2.ProxyHandler({'https': '10.10.78.61:3128','http': '10.10.78.61:3128'})
		opener = urllib2.build_opener(proxy)
		urllib2.install_opener(opener)
		url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20geo.placefinder%20where%20text=%22"+ urllib.quote_plus(searchstring) + ",%22%20&format=xml"
		f = urllib2.urlopen(url)
		xmldata = f.read()
		root = ET.fromstring(xmldata)
		
		#root = ET.parse('test.xml').getroot()
		cities = root.find('results').findall('Result')
		fcities = open('cities.txt', 'w')
		fwoeid = open('woeids.txt', 'w')
		for thiscity in cities:
			if thiscity.find('state').text is not None:
				fcities.write(thiscity.find('city').text + ", " + thiscity.find('state').text + ", " + thiscity.find('country').text + "\n")
				fwoeid.write(thiscity.find('woeid').text + "\n")
			else:
				fcities.write(thiscity.find('city').text + ", " + ", " + thiscity.find('country').text + "\n")
				fwoeid.write(thiscity.find('woeid').text + "\n")
		fcities.close()
		fwoeid.close()
		
	except Exception as e:
		print '<>',e
	
## gets woeid from query -main program
#takes searchstring as arg
if __name__ == '__main__':
	getwoeid(sys.argv[1])	

