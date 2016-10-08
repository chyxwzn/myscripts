#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request as request
from bs4 import BeautifulSoup

baseurl = "http://www.ted.com/talks/quick-list"
with request.urlopen(baseurl) as html:
    soup = BeautifulSoup(html.read().decode("utf-8"), 'html.parser')
    totalPages = int(soup.find_all("a", class_='pagination__link')[-2].string)
    with open("ted list_1.txt", "w") as f:
        for i in range(50, totalPages + 1):
            url = baseurl + "?page=" + str(i)
            with request.urlopen(url) as html:
                soup = BeautifulSoup(html.read().decode("utf-8"), 'html.parser')
                # soup.find_all("div", attrs={"class": "quick-list__row"})
                quicklist = soup.find_all("div", class_='quick-list__row')
                for item in quicklist:
                    a = item.find("div", class_='title').span.a
                    title = a.string
                    href = "http://www.ted.com" + a['href']
                    f.write(title+"\n")
                    f.write(href+"\n")
