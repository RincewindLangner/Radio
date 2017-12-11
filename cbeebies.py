#!/usr/bin/python2.7
import feedparser, os
# Opens feed.
d = feedparser.parse('https://podcasts.files.bbci.co.uk/p02pnn9d.rss')
NumEntries =  len(d['entries'])
for x in range(0, NumEntries):
	print d.entries[x]['title']
	print d.entries[x].media_content[0]['url']
	print

#print d.entries[0]['enclosure']['url']
