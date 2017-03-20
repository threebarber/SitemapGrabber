# -*- coding: utf-8 -*-
from pws import Google
from pws import Bing
from config import *
from google import search
import os

#don't touch any of this just edit the config file 

sitemapfile = open(filename,'w+')

try:
    for url in search('inurl:\"/sitemap_products_1.xml\" intext:'+keyword,lang='es', stop=numresults):
        print("[+]Retrieved Sitemap Containing Keyword \"" +keyword+"\": "+url)
        if "?" in url:
            url = url.split("?")[0]
        else:
            pass
        sitemapfile.write(url+"\n")
except Exception, e:
    print str(e)+"[-]Google is probably blocking you so wait and try later or something"

os.remove('.google-cookie')
    #yes this is literally like 10 lines of code 
