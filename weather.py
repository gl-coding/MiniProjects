#encoding=utf8
import requests
rb = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=乌兰察布')
print rb.text
