import requests
from dotenv  import load_dotenv
import os
load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API')
url = 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey={NEWS_API_KEY}'

# for wall street:- https://newsapi.org/v2/everything?domains=wsj.com&apiKey=25b5a6c1f34e4c23977411808e679c4a
# top headlines from techcrunch:- https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=25b5a6c1f34e4c23977411808e679c4a
# top buisness headlines in US :- https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=25b5a6c1f34e4c23977411808e679c4a
# articles about tesla:- https://newsapi.org/v2/everything?q=tesla&from=2024-05-03&sortBy=publishedAt&apiKey=25b5a6c1f34e4c23977411808e679c4a
# apple articles:- https://newsapi.org/v2/everything?q=apple&from=2024-06-02&to=2024-06-02&sortBy=popularity&apiKey=25b5a6c1f34e4c23977411808e679c4a


response = requests.get(url).json()

# print(response)

def getnewstitle():
    titles=[]
    for i in range(5):
        titles.append(response["articles"][i]["title"]+ ".")
    return titles
    

def getnewsdescription():
    description=[]
    for i in range(5):
        description.append(response["articles"][i]["description"]+ ".")
    return description

