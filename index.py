#!/usr/bin/env python
#encoding: utf-8

from user_relation import yejia
from save_relation import redis
import threading
redis.set_pipeline()
length = redis.get_length("unEnum")
while length != 0:
	length = redis.get_length("unEnum")
	start_url = redis.pop(length)
	try:
		t = threading.Thread(target = yejia.init_url, args = (start_url, 0) )
		t1 = threading.Thread(target = yejia.enum_by_item)
		t.start()
		t1.start()
		t.join(20)
		t1.join(20)
	except TypeError as e:
		print(e)
	#yejia.enum_by_item()

redis.remove_pipeline()
# print(redis.get_length("unEnum"), redis.get_length("Enumed"))