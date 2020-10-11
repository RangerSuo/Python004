# -*- coding: utf-8 -*-
import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
'User-Agent' : ua.random,
'Referer' : 'https://processon.com/login?f=index'
}

s = requests.Session()

login_url = 'https://processon.com/login'
form_data = {
'login_email':'1072681412',
'login_password':'qqqqqqqqq',
}

r = s.post(login_url, data=form_data, headers=headers)
t= r.text
return_text = r.json
status_code=r.status_code
print(status_code)
print(return_text)
print(t)