#!/usr/bin/env python
# -*- coding: utf-8 -*-
#By Ulrich Thiel, VK2UTL/DK1UT
#Reads calls.txt and creates call.csv

import re
import sqlite3
import sys


def fix(str):
	str = re.sub("u\"", "ü", str)
	str = re.sub("o\"", "ö", str)
	str = re.sub("a\"", "ä", str)
	str = re.sub("A\"", "Ä", str)
	str = re.sub("U\"", "Ü", str)
	str = re.sub("O\"", "Ö", str)
	str = re.sub("\"", "", str)
	str = re.sub("\n", "", str)
	str = re.sub("\f", "", str)
	str = re.sub("Seite [0-9]{1,3}", "", str)
	str = re.sub("[1-6][\s]*Liste der.*Klubstation", "", str)
	return str
	
def fixCity(str):
	#insert dash
	pos = re.search("[a-z][A-Z]",str)
	if pos == None:
		return str
	else:
		pos = pos.start()
		return str[0:pos+1]+"-"+str[pos+1:]

calls = [] #will be the array of calls
call = ""	#for reading lines
incall = False
with open('calls.txt') as f:
	for line in f:						
		#match call sign
		if re.match("D[A-R]+[0-9]+[A-Z]+", line): #match call sign
			if call != "":
				calls.append(fix(call))
				call = ""
			call = line
		else:
			if call != "":
				call = call + line	

calls.append(fix(call)) #flush


#now process data
dbconn = sqlite3.connect('calls.db')
dbcursor = dbconn.cursor()	
for call in calls:
	fields = call.split(";")
	callsign = fields[0].split(",")[0]
	callclass = fields[0].split(",")[1]
	name = fields[0].split(",")[2]
	name = re.sub("^[\s]*", "", name)
	name = re.sub("[\s]*$", "", name)
	callclass = re.sub("^[\s]*", "", callclass)
	if len(fields) == 1:	#no address given
		dbcursor.execute("INSERT OR IGNORE INTO Callsigns (Callsign, Class, Name) VALUES (\"" + callsign + "\",\"" + callclass + "\",\"" + name + "\")")
		None
	else:
		if len(fields) == 3:	#one address given
			street = fields[1]
			street = re.sub("^[\s]*", "", street)
			street = re.sub("[\s]*$", "", street)
			city = fields[2].split(",")[0]	#just in case, there are some errors in the PDF eg DB0ATV
			city = re.sub("^[\s]*", "", city)
			city = re.sub("[\s]*$", "", city)
			zip = city[0:5]
			city = city[6:]
			city = fixCity(city)
			dbcursor.execute("INSERT OR IGNORE INTO Callsigns (Callsign, Class, Name, Street, Zip, City) VALUES (\"" + callsign + "\",\"" + callclass + "\",\"" + name + "\",\"" + street + "\",\"" + zip + "\",\"" + city + "\")")
		elif len(fields) == 4:	#two addresses given
			street1 = fields[1]
			street1 = re.sub("^[\s]*", "", street1)
			street1 = re.sub("[\s]*$", "", street1)
			city1 = fields[2].split(",")[0]
			street2 = fields[2].split(",")[1]
			city2 = fields[3]
			street1 = re.sub("^[\s]*", "", street1)
			street1 = re.sub("[\s]*$", "", street1)
			city1 = re.sub("^[\s]*", "", city1)
			city1 = re.sub("[\s]*$", "", city1)
			zip1 = city1[0:5]
			city1 = city1[6:]
			street2 = re.sub("^[\s]*", "", street2)
			street2 = re.sub("[\s]*$", "", street2)
			city2 = re.sub("^[\s]*", "", city2)
			city2 = re.sub("[\s]*$", "", city2)
			zip2 = city2[0:5]
			city2 = city2[6:]
			city1 = fixCity(city1)
			city2 = fixCity(city2)
			dbcursor.execute("INSERT OR IGNORE INTO Callsigns (Callsign, Class, Name, Street, Zip, City) VALUES (\"" + callsign + "\",\"" + callclass + "\",\"" + name + "\",\"" + street1 + "\",\"" + zip1 + "\",\"" + city1 + "\")")
			dbcursor.execute("INSERT OR IGNORE INTO Callsigns (Callsign, Class, Name, Street, Zip, City) VALUES (\"" + callsign + "\",\"" + callclass + "\",\"" + name + "\",\"" + street2 + "\",\"" + zip2 + "\",\"" + city2 + "\")")
			
dbconn.commit()
dbconn.close()