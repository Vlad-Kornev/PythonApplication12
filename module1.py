import requests
st = 'https://stepic.org/media/attachments/course67/3.6.3/'
n = '699991.txt'
r = requests.get(st+n)
print(r.text.split())
