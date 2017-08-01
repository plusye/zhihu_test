#!/usr/bin/env python
#coding:utf-8
from urllib import request
from bs4 import BeautifulSoup
import time
import re

ips1 = []
def ip():
	webReq = request.Request("http://www.xicidaili.com", headers = {\
		"accept": "application/json, text/plain, */*",
		"Referer": "https://www.google.com/",
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
		})
	html = request.urlopen(webReq).read().decode('utf-8')
	bs_obj = BeautifulSoup(html, 'lxml')
	ips = bs_obj.find_all(text = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'))
	procol = bs_obj.find_all(text = re.compile('HTTP$|HTTPS$'))
	ports = bs_obj.find_all(text = re.compile('^\d{2,5}$'))
	for i in [x for x in range(80)]:
		ip = procol[i].lower() + "://" + ips[i] + ":" + ports[i]
		ips1.append(ip)
ip()