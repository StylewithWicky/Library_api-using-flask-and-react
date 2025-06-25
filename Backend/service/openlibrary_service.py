import requests
from config import Config

def fetch_books(query):
    url=f'https://developer.nytimes.com/my-apps/ef66fd53-09ef-4320-99f0-4bcd86262aaa/search.json?q={query}'
    response=requests.get(url)

    if response.status_code !=200:
        return{ 'error':"Failed to fetch data"}
    
    data=response.json()
    results=[]

    for item in data.get('docs',[]):
        results.append({
            "title":item.get('title'),
            "author":item.get('author_name')
        })
    return results
