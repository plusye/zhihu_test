#!/usr/bin/env python
#encoding: utf-8
import random
from urllib import request
from ips1 import ips1

def download(url):
	# ip_list = ["http://118.117.139.117:9000", "http://121.232.146.205:9000", \
	# "http://121.232.147.112:9000", "http://202.141.161.30:8118", \
	# "http://117.90.0.205:9000", "http://121.232.144.156:9000", \
	# "http://122.96.59.105:82", "http://122.96.59.106:80", \
	# "http://222.208.66.14:9000", "http://111.12.96.188:80", \
	# "http://115.213.1.83:8998", "http://60.178.137.158:8081", \
	# "http://117.90.3.185:9000", "http://110.73.48.146:8123", \
	# "http://111.13.7.42:83", "http://117.90.1.204:9000", \
	# "http://118.178.227.171:80", "http://111.74.56.249:9000",\
	# "http://182.42.46.43:808", "http://122.96.59.105:82",\
	# "http://112.95.241.76:80", "http://124.172.117.189:80",\
 #    "http://219.133.31.120:8888", "http://183.237.194.145:8080", \
	# "http://183.62.172.50:9999","http://163.125.157.243:8888",\
	# "http://183.57.42.79:81", "http://202.103.150.70:8088",\
	# "http://182.254.129.124:80", "http://58.251.132.181:8888",\
	# "http://125.67.239.175:8080","http://125.67.239.175:8080",\
 #    "http://61.156.141.205:8118", "http://117.21.234.107:8080", \
	# "http://103.231.64.53:80", "http://123.130.22.172:81", \
	# "http://175.25.184.214:3128", "http://60.207.106.140:3128", \
	# "http://111.62.251.46:8088", "http://118.114.149.200:3128", \
	# "http://119.114.109.171:8080", "http://221.218.38.45:8888", \
	# "http://124.206.89.242:3128", "http://202.201.64.112:80", \
	# "http://111.62.251.107:8080", "http://221.7.36.78:9999", \
	# "http://220.174.236.211:80", "http://222.125.34.11:8080", \
	# "http://39.90.183.174:9999", "http://218.75.149.207:3128", \
	# "http://202.201.64.112:8080", "http://125.77.25.116:80", \
	# "http://182.16.69.184:80", "http://183.169.128.30:80", \
	# "http://120.76.55.49:8088", "http://200.189.117.51:808"]
	index = random.randint(0,79)
	proxy = ips1[index]
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