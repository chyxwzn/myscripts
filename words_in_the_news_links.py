#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request as request
import io

topPages1 = ['''http://www.bbc.co.uk/worldservice/learningenglish/language/wordsinthenews/''',
            '''http://www.bbc.co.uk/worldservice/learningenglish/language/wordsinthenews/2013/01/130125_witn_archive_2012.shtml''',
            '''http://www.bbc.co.uk/worldservice/learningenglish/language/wordsinthenews/2012/02/120208_witn_archive_2011.shtml''',
            '''http://www.bbc.co.uk/worldservice/learningenglish/language/wordsinthenews/2011/01/110112_witn_archive_2010.shtml''',
            '''http://www.bbc.co.uk/worldservice/learningenglish/language/wordsinthenews/2010/01/100121_witn_archive_2009.shtml''',
            ]

f = io.open("articles.txt", "w", encoding='utf-8')

def parse_all_articles(url):
    print(url)
    html = request.urlopen(url)
    soup = BeautifulSoup(html.read().decode("utf-8"), "html.parser")
    main = soup.find(class_='g-w6')
    links = main.find_all('div', class_='teaser')
    for link in links:
        if link.h3.span == None:
            title = link.h3.a.contents[0]
        else:
            title = link.h3.span.contents[0]
        date = link.find(class_='body').contents[0]
        href = "http://www.bbc.co.uk" + link.h3.a['href']
        print(title, file=f)
        print(date, file=f)
        print(href, file=f)

for page in topPages1:
    parse_all_articles(page)

f.close()
