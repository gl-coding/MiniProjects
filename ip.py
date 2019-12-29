#encoding=utf8
#感谢taobao.com提供的api！
import requests
import json
request = requests.get("http://ip.taobao.com/service/getIpInfo.php?ip=14.130.66.149")
print request.text
