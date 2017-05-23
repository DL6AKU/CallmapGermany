#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

dbconn = sqlite3.connect('calls.db')
dbcursor = dbconn.cursor()

t = dbcursor.execute("SELECT Count(*) FROM Callsigns").fetchone()[0]
a = dbcursor.execute("SELECT Count(*) FROM Callsigns WHERE Class IS \"A\"").fetchone()[0]
e = dbcursor.execute("SELECT Count(*) FROM Callsigns WHERE Class IS \"E\"").fetchone()[0]
print "Records:\t\t\t " + str(t) + "/"+str(a)+"/"+str(e) 

t = dbcursor.execute("SELECT Count(Distinct(Callsign)) FROM Callsigns").fetchone()[0]
a = dbcursor.execute("SELECT Count(Distinct(Callsign)) FROM Callsigns WHERE Class IS \"A\"").fetchone()[0]
e = dbcursor.execute("SELECT Count(Distinct(Callsign)) FROM Callsigns WHERE Class IS \"E\"").fetchone()[0]
print "Distinct call signs:\t\t " + str(t) + "/"+str(a)+"/"+str(e) 

t = dbcursor.execute("SELECT Count(Callsign) FROM Callsigns WHERE Zip IS NOT NULL").fetchone()[0]
a = dbcursor.execute("SELECT Count(Callsign) FROM Callsigns WHERE Class IS \"A\" AND Zip IS NOT NULL").fetchone()[0]
e = dbcursor.execute("SELECT Count(Callsign) FROM Callsigns WHERE Class IS \"E\" AND Zip IS NOT NULL").fetchone()[0]
print "Records w/ address:\t\t " + str(t) + "/"+str(a)+"/"+str(e) 

t = dbcursor.execute("SELECT Count(Distinct(Callsign)) FROM Callsigns WHERE Zip IS NOT NULL").fetchone()[0]
a = dbcursor.execute("SELECT Count(Distinct(Callsign)) FROM Callsigns WHERE Class IS \"A\" AND Zip IS NOT NULL").fetchone()[0]
e = dbcursor.execute("SELECT Count(Distinct(Callsign)) FROM Callsigns WHERE Class IS \"E\" AND Zip IS NOT NULL").fetchone()[0]
print "Distinct call signs w/ address:\t " + str(t) + "/"+str(a)+"/"+str(e) 
 
t = dbcursor.execute("SELECT Count(*) FROM Callsigns WHERE Geocode = 1").fetchone()[0]
a = dbcursor.execute("SELECT Count(*) FROM Callsigns WHERE Geocode = 1 AND Class IS \"A\" AND Zip IS NOT NULL").fetchone()[0]
e = dbcursor.execute("SELECT Count(*) FROM Callsigns WHERE Geocode = 1 AND Class IS \"E\" AND Zip IS NOT NULL").fetchone()[0]
print "Records w/ geocode:\t\t " + str(t) + "/"+str(a)+"/"+str(e) 

t = dbcursor.execute("SELECT Count(Distinct(Callsign)) FROM Callsigns WHERE Geocode = 1").fetchone()[0]
a = dbcursor.execute("SELECT Count(Distinct(Callsign)) FROM Callsigns WHERE Geocode = 1 AND Class IS \"A\" AND Zip IS NOT NULL").fetchone()[0]
e = dbcursor.execute("SELECT Count(Distinct(Callsign)) FROM Callsigns WHERE Geocode = 1 AND Class IS \"E\" AND Zip IS NOT NULL").fetchone()[0]
print "Distinct call signs w/ geocode:\t " + str(t) + "/"+str(a)+"/"+str(e) 



dbconn.close()
