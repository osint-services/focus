import httpx
import urllib
v = 'https://www.deviantart.com/muse1908'
url = urllib.parse.quote(v, safe='')
response = httpx.get(f'http://localhost:8000/profile?url={url}')