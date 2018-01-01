#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request as request
import io
from pathlib import Path
import time

f = io.open("articles.txt", "r")

articles = []
nr = 0
title = ""
date = ""
link = ""
for line in f.readlines():
    if nr == 0:
        title = line.strip()
    elif nr == 1:
        date = line.strip()
    elif nr == 2:
        link = line.strip()
    if nr == 2:
        articles.append({"title":title, "date":date, "link":link})
    nr = (nr + 1) % 3

topDir = "Words in the news"

def download_article(article):
    date = time.strptime(article["date"], "%d %B %Y")
    articleDir = topDir+"/"+str(date.tm_year)+'_'+str(date.tm_mon)+'_'+str(date.tm_mday)
    p = Path(articleDir)
    p.mkdir(parents=True, exist_ok=True)
    with request.urlopen(article["link"]) as html:
        soup = BeautifulSoup(html.read().decode("utf-8"), "html.parser")
        dlli = soup.find(id='relateddownloads0').find_all('li')
        for li in dlli:
            href = li.a['href']
            filetype = li.span.contents[0].split(' (')[0]
            extention = href.split('.')[-1]
            filePath = articleDir+"/"+article["title"]+"_"+filetype+'.'+extention
            request.urlretrieve(href, filePath)

for article in articles:
    print(article["date"])
    download_article(article)

f.close()
