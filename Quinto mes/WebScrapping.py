from bs4 import BeautifulSoup

import requests
# link = 'https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/'
link  = "https://dataquestio.github.io/web-scraping-pages/simple.html"
page = requests.get(link)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title)
