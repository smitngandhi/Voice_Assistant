import requests

url = 'https://newsapi.org/v2/everything?q=apple&from=2024-05-18&to=2024-05-18&sortBy=popularity&apiKey=25b5a6c1f34e4c23977411808e679c4a'

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