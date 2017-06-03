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
import time
from datetime import datetime
import re


ppgurll = "http://www.basketball-reference.com/leaders/pts_per_g_season.html"
ptsgameurll = "http://www.basketball-reference.com/leaders/pts_game.html"

ppgid = "stats_NBA"
ptsgameid = "stats_game_pts"
def getstatleadername ( stat, number ):
    stat2 = None
    url = None
    id = None
    if stat ==  "ppgs":
        url = ppgurll
        id = ppgid
        stat2 = "PPG"
    elif stat == "ptsgame":
        url = ptsgameurll
        id = ptsgameid
        stat2 = "PTS"
    soup = bs(urlopen(url),"html.parser")
    players = soup.find("table",attrs={"id":id})
    headings = [th.get_text() for th in players.find("tr").find_all("th")]
    pdata = []
    pdata.append(headings)
    for row in players.find_all("tr")[1:]:
        pdata_row = (td for td in row.find_all("td"))
        pdata.append(pdata_row)
    index = np.arange(len(pdata)-1)
    playerdf_raw = pd.DataFrame(data=pdata[1:][0:],index=index,columns=pdata[0][0:])
    playerdf_raw.head()
    #print playerdf_raw[stat][0]

    pdata_better = []
    pdata_better.append(["Name","Page", stat2])
    base = "www.basketball-reference.com"
    for i in index:
        pname = playerdf_raw['Player'][i].get_text()
        pname = pname.replace('*', '')
        ppage = base+str(playerdf_raw['Player'][i]).split("\"")[1]
        statnum = str(playerdf_raw[stat2][i])
        statnum = statnum.replace('<td', '')
        statnum = statnum.replace('align="right">', '')
        statnum = statnum.replace('</td>', '')
        statnum = statnum.replace(' ', '')
        row = (pname,ppage,statnum)
        pdata_better.append(row)
    index = np.arange(len(pdata_better)-1)
    playerdf = pd.DataFrame(data=pdata_better[1:][0:],index=index,columns=pdata_better[0][0:])
    playerdf.head()
    return playerdf['Name'][number-1]
    #for num in range(0,(topx)):
    #    print playerdf['Name'][num]
def getstatleaderstat ( stat, number ):
    stat2 = None
    url = None
    id = None
    if stat ==  "ppgs":
        url = ppgurll
        id = ppgid
        stat2 = "PPG"
    elif stat == "ptsgame":
        url = ptsgameurll
        stat2 = "PTS"
        id = ptsgameid
    soup = bs(urlopen(url),"html.parser")
    players = soup.find("table",attrs={"id":id})
    headings = [th.get_text() for th in players.find("tr").find_all("th")]
    pdata = []
    pdata.append(headings)
    for row in players.find_all("tr")[1:]:
        pdata_row = (td for td in row.find_all("td"))
        pdata.append(pdata_row)
    index = np.arange(len(pdata)-1)
    playerdf_raw = pd.DataFrame(data=pdata[1:][0:],index=index,columns=pdata[0][0:])
    playerdf_raw.head()
    #print playerdf_raw[stat][0]

    pdata_better = []
    pdata_better.append(["Name","Page", stat2])
    base = "www.basketball-reference.com"
    for i in index:
        pname = playerdf_raw['Player'][i].get_text()
        pname = pname.replace('*', '')
        ppage = base+str(playerdf_raw['Player'][i]).split("\"")[1]
        statnum = str(playerdf_raw[stat2][i])
        statnum = statnum.replace('<td', '')
        statnum = statnum.replace('align="right">', '')
        statnum = statnum.replace('</td>', '')
        statnum = statnum.replace(' ', '')
        statnum = statnum.replace('>', '')
        row = (pname,ppage,statnum)
        pdata_better.append(row)
    index = np.arange(len(pdata_better)-1)
    playerdf = pd.DataFrame(data=pdata_better[1:][0:],index=index,columns=pdata_better[0][0:])
    playerdf.head()
    return playerdf[stat2][number-1]
def writetopxtotxt (stat, url, topx):
    datestime = datetime.now()
    yr = str(datestime.strftime('%Y'))
    #print rdatetime
    filename = str(yr + "_" + stat + "_" + "top" + str(topx) + ".txt")
    file = open(filename,"w")
    i = 1
    topx = topx+1
    while i < topx:
        string = getstatleadername(stat, url, i)
        string2 = getstatleaderstat(stat, url, i)
        stringi = str(i)
        file.write(stringi + ". " + string + " " + string2 + "\n")
        i+=1
    file.close()
#getstatleadername("PPG", "http://www.basketball-reference.com/leaders/pts_per_g_season.html", 1)
#writetopxtotxt ("PPG", "http://www.basketball-reference.com/leaders/pts_per_g_season.html", 5)

lul = True
while lul is True:
    print ">",
    input = raw_input()
    commands = ["help", "statleader"]
    if lul == True:
        cmdlen = len(input.split())
        #print cmdlen
        cmdreal = input.split(' ', 1)[0]
        #print cmdreal
        i = 0
        while i < cmdlen:
            #print input.split(' ', 1)[i]
            i = i + 1
        if cmdreal == "help":
            print "nba_proj by tejasprak"
            print "commands: "
            print "help: list commands"
            print "liststats: list stats"
            print "statleader [STAT] [TOPX]"
        elif cmdreal == "liststats":
            print "ppgs: pts per game season average"
            print "ptsgame: pts per single gae"
        elif cmdreal == "statleader":
            #print "statleader"
            inputstat = input.split(' ', 2)[1]
            #print inputstat
            inputtopx = input.split(' ', 2)[2]
        #    print inputtopx
            vv = 1
            while vv < (int(inputtopx) + 1):
                #print "what"
                print str((vv)) + ". ",
                print getstatleadername (inputstat, vv),
                print getstatleaderstat(inputstat, vv)
                vv = vv + 1
