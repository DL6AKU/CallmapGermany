#!/usr/bin/env python
# -*- coding: utf-8 -*-
import geocoder

address = raw_input("Address: ")

g = geocoder.google(address)

print g.lng, g.lat
