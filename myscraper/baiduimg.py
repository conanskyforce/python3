# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os

headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
url="http://www.meitu.com/all"
start_html = requests.get(url,headers=headers)
Soup=BeautifulSoup(start_html.text,'lxml')
all_a = Soup.find('div',class_='all').find_all('a')

for a in all_a:
	title = a.get_text()
	href =a['href']
	html = requests.get(href,headers=headers)
	html_Soup = BeautifulSoup(html.text,'lxml')
	max_span = html_Soup.find_all('span')[10].get_text()

	for page in range(1,int(max_span)+1):
		page_url =href+'/'+str(page)
		print(page_url)






