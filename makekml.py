#!/usr/bin/env python
# -*- coding: utf-8 -*-
#By Ulrich Thiel, VK2UTL/DK1UT
import sys  
import sqlite3

reload(sys)  
sys.setdefaultencoding('utf8')
import simplekml

dbconn = sqlite3.connect('calls.db')
dbcursor = dbconn.cursor()

dbcursor.execute("SELECT * FROM Callsigns WHERE Lng IS NOT NULL AND Lat IS NOT  NULL AND Class IS \"A\"")
res = dbcursor.fetchall()

print str(len(res))+ " class A call signs with geocode"

kml=simplekml.Kml()
for row in res:
	address = row[4] + ", " + row[5] + " " + row[6] + ", Germany"
	pnt = kml.newpoint()
	pnt.name = row[1]+" ("+row[3]+")"
	pnt.coords=[(row[7],row[8])]
	pnt.address=address
	pnt.description = address
	
	if row[2] == "A":
		pnt.style.iconstyle.color = simplekml.Color.green 
	else:
		pnt.style.iconstyle.color = simplekml.Color.green 

kml.save('calls-A.kml')

#
dbcursor.execute("SELECT * FROM Callsigns WHERE Lng IS NOT NULL AND Lat IS NOT  NULL AND Class IS \"E\"")
res = dbcursor.fetchall()

print str(len(res))+ " class E call signs with geocode"

kml=simplekml.Kml()
for row in res:
	address = row[4] + ", " + row[5] + " " + row[6] + ", Germany"
	pnt = kml.newpoint()
	pnt.name = row[1]+" ("+row[3]+")"
	pnt.coords=[(row[7],row[8])]
	pnt.address=address
	pnt.description = address
	
	if row[2] == "A":
		pnt.style.iconstyle.color = simplekml.Color.red 
	else:
		pnt.style.iconstyle.color = simplekml.Color.green 

kml.save('calls-E.kml')


dbconn.close()