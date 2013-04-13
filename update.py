#!/usr/bin/python

'''
    Copyright 2013, Jeff Sharkey

    Licensed under the Apache License, Version 2.0 (the "License"); 
    you may not use this file except in compliance with the License. 
    You may obtain a copy of the License at 

        http://www.apache.org/licenses/LICENSE-2.0 

    Unless required by applicable law or agreed to in writing, software 
    distributed under the License is distributed on an "AS IS" BASIS, 
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
    See the License for the specific language governing permissions and 
    limitations under the License.
'''

import urllib2
import datetime

PLACES = [
    (38.668323,-120.065353,"Kirkwood"),
    (38.916815,-119.903541,"Heavenly"),
    (39.250584,-120.132558,"Northstar"),
    (39.189059,-120.265789,"Squaw")
]

API = "http://graphical.weather.gov/xml/sample_products/browser_interface/ndfdBrowserClientByDay.php?lat=%s&lon=%s&format=24+hourly&numDays=1"
POINT = ""

snowing = []
for place in PLACES:
    lat, lon, name = place
    response = urllib2.urlopen(API % (lat, lon))
    if "snow" in response.read().lower():
        snowing.append(place)

print """
<!DOCTYPE HTML>
<html>
<head>
<title>Is it snowing in Tahoe?</title>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta http-equiv="refresh" content="3600">
<link href='http://fonts.googleapis.com/css?family=Alegreya:900|Open+Sans' rel='stylesheet' 
type='text/css'>
<style>

html, body, table {
width: 100%;
height: 100%;
margin: 0;
}

body {
background: #F2FEFF url("back.png");
font-family: 'Open Sans', sans-serif;
}

* {
color: #606060;
}


h1 {
color: #afb3b3;
font-family: 'Alegreya', serif;
font-weight: 900; 
font-size: 120pt;
text-shadow: 0px 0px 10px #ffffff;
margin-top: -20pt;
margin-bottom: -20pt;
}

h1.yes {
color: #6CDFEA;
}

</style>
</head>

<body>
<table><tr><td style="vertical-align:middle; text-align:center;">
"""

if len(snowing) > 0:
    snowing = [('<a target="_blank" href="http://forecast.weather.gov/MapClick.php?textField1=%s&textField2=%s">%s</a>' % (lat, lon, place)) for lat, lon, place in snowing]
    snowing = " and ".join(snowing)
    print """<h1 class="yes">YES!</h1><p>It's snowing at %s.</p>""" % (snowing)
else:
    print """<h1>NO.</h1>"""

today = datetime.datetime.today()
date = today.strftime('%B %d at %I:%M')
ampm = today.strftime('%p').lower()

print """<p>I checked %s<span style="font-variant:small-caps;">%s</span>.</p>""" % (date, ampm)

print """
</td></tr></table>
</body>
</html>
"""
