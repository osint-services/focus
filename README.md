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

v = 'https://www.deviantart.com/muse1908'
url = urllib.parse.quote(v, safe='')
response = httpx.get(f'http://localhost:8000/profile?url={url}') # assuming the server is running locally
```