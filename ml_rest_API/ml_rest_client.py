import json
from urllib import response
import requests

url = 'http://xxxx.xx.xx.x:8005/model'

request_data = json.dumps({'age': 40, 'salary':20000})
response = requests.post(url,request_data)

print(response.text)