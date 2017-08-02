#!/usr/bin/env python
#encoding: utf-8
import random
from urllib import request
from urllib import error
import json
import ip
from imp import reload
reload(ip)
length = len(ip.ips) - 1
def download(url):
	index = random.randint(0,length)
	proxy = "http://" + ip.ips[index][0] + ":" + str(ip.ips[index][1])
	try:
		proxy_support = request.ProxyHandler({'http':proxy})
		opener = request.build_opener(proxy_support)
		request.install_opener(opener)
		webReq = request.Request(url, headers = {\
		"accept": "application/json, text/plain, */*",
		"authorization":"oauth c3cef7c66a1843f8b3a9e6a1e3160e20"
			})
		webReq.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
		# webReq.add_header('Cookie', '_zap=79529f88-b0e0-434d-99e5-64aa54e6dfc4; q_c1=6806b5234aa7454885e44e583ba31a8d|1501485042000|1501485042000; aliyungf_tc=AQAAAMBGLmJMcg0ACzP3PC2EU73Wfcnx; r_cap_id="NzQzNDg5YjMzZWM4NDUyMzk4OTBiYzgxZGE1MmM0YmU=|1501553117|798b1ba2e1bf0e5a47da3e1d3e25abe6ae8efc43"; cap_id="YjJhYTM2ZTI5MjU0NGUzNDgxOWNmYjM0ZGEzZWE5NjY=|1501553117|2c7de1fd82feb91153223c08114131063d5c7d34"; d_c0="ADACID_2JgyPTpovSK-JkhnB0RHPFAjDAd8=|1501553119"; __utma=51854390.549307643.1501553120.1501553120.1501553120.1; __utmb=51854390.0.10.1501553120; __utmc=51854390; __utmz=51854390.1501553120.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20170731=1; l_n_c=1; z_c0=Mi4wQUpDQ01DTXFWd3NBTUFJZ1BfWW1EQmNBQUFCaEFsVk5DbS1uV1FBV3k0R2hxR1gzRkNhMTRacmlTcjdpZWVWbUN3|1501553162|58d4ff08ce7c6c9c49348fc8389aa17c069c246b; _xsrf=7c6759aa-978b-4255-95eb-e35f85e58078')
		html = request.urlopen(webReq).read().decode('utf-8')
		return html
	except error.HTTPError as e:
		print(e.code, e.reason)