import requests

url = 'http://140.113.216.103:8000/'
files = {'file': open('new_test.mp4', 'rb')}
r = requests.post(url, files=files)
r.text