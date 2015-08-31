#!/usr/bin/env python

from lxml import html
import requests
from feedgen.feed import FeedGenerator
import datetime
import pytz

mainpage = requests.get('http://wurstball.de')
tree = html.fromstring(mainpage.text)
wids = tree.xpath('//div[@id="content"]//a/@href')

fg = FeedGenerator()
fg.title('Wurstball')
fg.link(href='http://wurstball.de', rel='alternate')
fg.description('Foo')

for wid in wids:
    subpage = requests.get(('http://wurstball.de%s' % wid))
    tree = html.fromstring(subpage.text)
    url = tree.xpath('//div[@id="content-related"]/li/text()')[0][6:]
    date = tree.xpath('//div[@id="content-related"]/li/text()')[1][7:26]
    date2 = pytz.utc.localize(datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S'))

    fe = fg.add_entry()
    fe.id(wid)
    fe.title('Foo')
    fe.description('<img src="%s">' % url)
    fg.link(href=url, rel='alternate')
    fe.pubdate(date2)

rssfeed  = fg.rss_str(pretty=True)
fg.rss_file('rss.xml')
