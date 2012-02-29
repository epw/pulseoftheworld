#! /usr/bin/env python

import urllib2
from xml.dom import minidom as xml

def get_content (headnode):
    nodes = headnode.getElementsByTagName ("content")
    for node in nodes:
        if node.getAttribute ("type") == u"html":
            return node.firstChild.data

gtrends = urllib2.urlopen ("http://www.google.com/trends/hottrends/atom/hourly")
firstline = gtrends.readline()
doc = firstline + '\n'.join(gtrends.readlines())
contentxmlstr = get_content (xml.parseString (doc))

contentxml = xml.parseString (firstline + "\n" + contentxmlstr)

# Need to sanitize input by turning & into &amp;
