#!/usr/local/bin/python

import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from bs4 import BeautifulSoup as bs
from lxml import html
import requests
from urllib2 import urlopen
import numpy as np
import string
import re


stat2 = "PTS"
url = None
id = None

soup = bs(urlopen("http://www.basketball-reference.com/players/j/jordami01.html"),"html.parser")
players = soup.find("table",attrs={"id":"per_game"})
headings = [th.get_text() for th in players.find("tr").find_all("th")]
#i = 0
#while i < (headings.len):
#        temp = headings[i]
#        if temp == "Lg":
#            headings.remove("Lg")
headings.remove("eFG%")
pdata = []
pdata.append(headings)
l = 0
for row in players.find_all("tr")[1:]:
    pdata_row = (td for td in row.find_all("td"))
    #print pdata_row
    pdata.append(pdata_row)
index = np.arange(len(pdata)-1)
print len(pdata)
#print index[5]
#playerdf_raw = pd.DataFrame(data=pdata[1:][0:],index=index,columns=pdata[0][0:])
playerdf_raw = pd.DataFrame(data=pdata[1:][0:],index=index,columns=pdata[0][0:])
playerdf_raw.head()

stat4 = "Age"
array_accessor = 1
pdata_better = []
pdata_better.append(["Name", stat2, "BLK", stat4])
base = "www.basketball-reference.com"
#for i in index:
#ppage = base+str(playerdf_raw['Player'][i]).split("\"")[1]
pname = "MJ"
pname = pname.replace('*', '')
statnum = str(playerdf_raw[stat2][array_accessor])
block = str(playerdf_raw["BLK"][array_accessor])
non_decimal = re.compile(r'[^\d.]+')
statnum = non_decimal.sub("", statnum)
block = non_decimal.sub("", block)
stat4num = str(playerdf_raw[stat4][array_accessor])
#stat4num = non_decimal.sub("", stat4num)
print statnum
row = (pname, statnum, block, stat4num)
pdata_better.append(row)
index = np.arange(len(pdata_better)-1)
playerdf = pd.DataFrame(data=pdata_better[1:][0:],index=index,columns=pdata_better[0][0:])
playerdf.head()
print playerdf[stat4][0]
