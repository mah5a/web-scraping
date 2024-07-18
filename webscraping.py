# load in libraries
import requests
from bs4 import BeautifulSoup as bs

# load the web page content
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# convert to a beautifulsoup object
soup = bs(r.content)
# print out our HTML
print(soup.prettify())

# Start using BeautfulSoup to scrape
# find() and find_all()
first_header = soup.find("h2")
print(first_header)
headers = soup.find_all("h2")
print(headers)

# pass in a list of elements to look for the first element of the list
print("--------------")
find_header = soup.find(["h1", "h2"])
print(find_header)
print("--------------")
# pass in a list of elements to look for all
headers = soup.find_all(["h1", "h2"])
print(headers)
print("--------------")
# pass in attributes to find/find_all
paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
print(paragraph)

