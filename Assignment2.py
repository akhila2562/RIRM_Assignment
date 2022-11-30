import requests
from bs4 import BeautifulSoup
r = requests.get('https://ful.io')
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser') #Parsing HTML
for link in soup.find_all('a'):
    print(link.get('href'))