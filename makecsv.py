#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Ulrich Thiel, VK2UTL/DK1UT
import sys  
import sqlite3
import csv

reload(sys)  
sys.setdefaultencoding('utf8')
import simplekml

dbconn = sqlite3.connect('calls.db')
dbcursor = dbconn.cursor()

dbcursor.execute("SELECT * FROM Callsigns WHERE Lng IS NOT NULL AND Lat IS NOT  NULL")
res = dbcursor.fetchall()

print str(len(res))+ " class call signs with geocode"

with open('calls.csv', 'w') as csvfile:
    fieldnames = ['Id', 'Callsign', 'Class', 'Name', 'Street', 'Zip' , 'City', 'Lng', 'Lat', 'Address', 'NameCall', 'Marker']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    for row in res:
    	address = str(row[4]) + ", " + str(row[5]) + " " + str(row[6])
    	namecall = str(row[1]) + " (" + str(row[3]) + ")"
    	if row[2] == "A":
    		marker = "small_red"
    	else:
    		marker = "small_purple"
    	writer.writerow({'Id': row[0], 'Callsign' : row[1], 'Class' : row[2], 'Name': row[3], 'Street':row[4], 'Zip':row[5], 'City':row[6], 'Lng':row[7],'Lat':row[8],'Address':address, 'NameCall':namecall, 'Marker':marker})

dbconn.close()