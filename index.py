#!/usr/bin/env python
#encoding: utf-8

from user_relation import yejia
from save_relation import redis
import threading
redis.set_pipeline()
length = redis.get_length("unEnum")
start_url = redis.pop(length)
yejia.init_url(start_url, 0)
yejia.enum_by_item()

redis.remove_pipeline()
# print(redis.get_length("unEnum"), redis.get_length("Enumed"))