import requests
from time import sleep

print('Testing~\n')

url = 'http://10.0.0.185:8080'
# url = 'http://localhost:8080'

r = requests.get(url)

print("Get request: %s\n" % r.text)

sleep(1)

r = requests.post(url, data={"url": "SEND_POST_TEST"})

print("Post request: %s\n" % r.text)
print(r)
