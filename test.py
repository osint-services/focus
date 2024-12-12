import httpx
import urllib

#v = 'https://www.deviantart.com/muse1908'
#v = 'https://twitter.com/MynameisAkeem'
#v = 'http://web.archive.org/web/20230326054832/https://twitter.com/MynameisAkeem'

v = 'https://www.deviantart.com/muse1908'
url = urllib.parse.quote(v, safe='')
response = httpx.get(f'http://localhost:8000/profile?url={url}')
print(response.json())