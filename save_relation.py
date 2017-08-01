#!/usr/bin/env python
#encoding: utf-8
import redis
class Redis(object):
	def __init__(self, host, port):
		self.pool = redis.ConnectionPool(host=host, port=port)
		self.r = redis.Redis(connection_pool=self.pool)
	def set_pipeline(self):
		self.pipe = self.r.pipeline(transaction=True)
	def remove_pipeline(self):
		self.pipe.execute()
	def insert(self, url_token):
		self.r.sadd("unEnum", url_token)
	def insert_aready_pop(self, pop_item):
		self.r.sadd("Enumed", pop_item)
	def get_length(self, name):
		return self.r.scard(name)
	def pop(self, length):
		if length == 0:
			return None
		else:
			return self.r.spop("unEnum").decode('utf-8')
	def is_pop(self,url_token):
		return self.r.sismember("Enumed", url_token)

redis = Redis('45.78.25.218', 6379)