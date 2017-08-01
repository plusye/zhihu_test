#!/usr/bin/env python
#encoding: utf-8
import json
import time
import download
from save_relation import redis
import threading
redis.set_pipeline()

class User_info(object):
	def init_url(self, start_people, start_item):
		self.url_token = start_people
		self.item = start_item
		self.url = 'https://www.zhihu.com/api/v4/members/'+ \
		self.url_token + \
		'/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset='+ str(self.item) +'&limit=20'

	def get_page(self):
		self.page_obj = download.download(self.url)
		self.data = json.loads(self.page_obj)
		self.is_end = self.data['paging']['is_end']
		return self.data


class Controller(User_info):
	def __init__(self):
		self.sets = set()
	def change_url_item(self):
		self.item += 20
		self.init_url(self.url_token, self.item)

	def change_url_token(self, new_url_token):
		self.url_token = new_url_token
		self.init_url(self.url_token, self.item)

	def save_url_token(self):
		self.data_lists = self.get_page()['data']
		for data in self.data_lists:
			set_item = data['url_token']
			redis.insert(set_item)
			print(set_item)

	def enum_by_item(self):
		self.get_page()
		self.save_url_token()	
		while self.is_end is False:
			time.sleep(2)
			t2 = threading.Thread(target = self.change_url_item, name = "loop2")
			t3 = threading.Thread(target = self.get_page, name = "loop3")
			t4 = threading.Thread(target = self.save_url_token, name = "loop4")
			t2.start()
			t3.start()
			t4.start()
			t2.join(3)
			t3.join(3)
			t4.join(3)
			#self.change_url_item()
			#self.get_page()
			#self.save_url_token()
		self.item = 0
		#redis中set的长度
		self.sets_length = redis.get_length("unEnum")
		#set长度不为0时，从redis中取出一个urllib_token
		pop_url =  redis.pop(self.sets_length)
		#改变URL
		self.change_url_token(pop_url)
		if self.sets_length != 0:
			t5 = threading.Thread(target = self.get_page, name = "loop3")
			time.sleep(5)
			t5.start()
			t5.join(2)
			#self.get_page()
			t6 = threading.Thread(target = self.enum_by_item)
			t6.start()
			t6.join(15)
			# self.enum_by_item()

yejia = Controller()

