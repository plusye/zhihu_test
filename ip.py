from urllib import request
import json

ips_json = request.urlopen("http://127.0.0.1:8000/?protocol=0").read().decode('utf-8')
ips = json.loads(ips_json)