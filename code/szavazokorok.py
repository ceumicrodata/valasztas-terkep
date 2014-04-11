from urllib2 import urlopen
import sys
import re
import json

regex = re.compile("\"kod\":\"(\d{3})_(\d{3})\"")

for county in ["%02d" % (item) for item in range(1,21)]:
	for district in ["%02d" % (item) for item in range(100)]:
		try:
			lines = open("../raw/oevk-%s-%s.js" % (county, district),"r").readlines()
		except:
			continue
		for precint in regex.findall(lines[3]):
			print "http://valasztas.hu/dyn/pv14/map/oevk/M%s/%s/T%s/%s.js" % (county, district, precint[0], precint[1])
