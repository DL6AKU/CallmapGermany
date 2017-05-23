#!/usr/bin/env python
# -*- coding: utf-8 -*-
#By Ulrich Thiel, VK2UTL/DK1UT
import sqlite3
import geocoder
import requests
import progressbar
import sys
import time

dbconn = sqlite3.connect('calls.db')
dbcursor = dbconn.cursor()

#dbcursor.execute("SELECT * FROM Callsigns WHERE Geocode IS NULL AND Street IS NOT NULL")
dbcursor.execute("SELECT * FROM Callsigns WHERE Geocode = 0")
res = dbcursor.fetchall()
bar = progressbar.ProgressBar(max_value=len(res))
count = 0
with requests.Session() as session:
	bar.start()
	for row in res:
		address = row[4] + ", " + row[5] + " " + row[6] + ", Germany"
		g = geocoder.google(address, session=session)
		#print g.status
		if g.status == 'OVER_QUERY_LIMIT':
			print "Query limit reached"
			sys.exit(0)
		if g.status == 'ZERO_RESULTS' or g.status == 'ERROR - No results found' or g.lng == None:
			dbcursor.execute("UPDATE Callsigns SET Geocode = 0 WHERE Id = " + str(row[0]))
		else:
			dbcursor.execute("UPDATE Callsigns SET Lng = " + str(g.lng) + ", Lat = " + str(g.lat) + ", Geocode = 1 WHERE Id = " + str(row[0]))
		dbconn.commit()
		count = count + 1
		bar.update(count)

dbconn.close()
