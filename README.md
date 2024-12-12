# focus

focus is an OSINT microservice that seaches the profile of a given URL and returns metadata found at that site using https://github.com/soxoj/socid-extractor to gather the data.

## Requirements
- Python 3.9 or higher

### Tech Stack
- The REST API framework being used is [FastAPI](https://fastapi.tiangolo.com/)
- The tool being used to query social media URLs [socid-extractor](https://github.com/soxoj/socid-extractor)


### Setup
1. Create Python virtual environment. `python -m venv venv`
2. Activate virtual environment. `source venv/bin/activate`
3. Install dependencies. `pip install -r requirements.txt`
4. Start server. `fastapi dev main.py` 


### Example
```python
import httpx
import urllib
import time

# processing, try again later or get the current status

status_code = 102
while status_code == 102:
    response = httpx.get(f'http://localhost:8000/scan/j-doe') # assuming the server is running locally
    status_code = response.status_code

    if status_code == 102:
        time.sleep(5) # give server time to process
        continue

    if response.status_code == 200:
        profiles_found = response.json()
        for profile in profiles_found:
            unsafe_url = profile["uri_check"]
            url = urllib.parse.quote(unsafe_url, safe='')
            response = httpx.get(f'http://localhost:8000/focus?url={url}') # assuming the server is running locally
            details = response.json() # contains profile details
            print(details)
        
```