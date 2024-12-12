from fastapi import FastAPI
from .main import search_profile

app = FastAPI()

@app.get('/profile')
def find_profile(url: str):
    profile_info = search_profile(url)
    return profile_info