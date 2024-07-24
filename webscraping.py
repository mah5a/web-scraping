# load in libraries
import regex as re

import requests
from bs4 import BeautifulSoup as bs

# load the web page content
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# convert to a beautifulsoup object
soup = bs(r.content, features="html.parser")
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
# you can nest calls
print("--------------")
body = soup.find("body")
print(body)
print("--------------")
# look for div in body
div = body.find("div")
print(div)
print("--------------")
# find header in div
header = div.find("h1")
print(header)
print("--------------")
# search for EXACT specific string ex: some
paragraphs = soup.find_all("p", string="Some bold text")
print(paragraphs)

print("--------------")
# look for a string


paragraph = soup.find_all("p", string=re.compile("Some"))
print(paragraph)

print("--------------")
# find string with different capitalization
headers = soup.find_all("h2", string=re.compile("(H|h)eader"))
print(headers)

print("********************--------------SELECT as in CSS-------------*******************")

select = soup.select("p")
print(select)
print("--------------")
content = soup.select("div p")
print(content)
print("--------------")
paragraphs = soup.select("h2 ~ p")
print(paragraphs)
print("--------------")
bold_text = soup.select("p#paragraph-id b")
print(bold_text)
print("--------------")
print("direct dicendent of a paragraph")
paragraphs = soup.select("body > p")
print(paragraphs)
print("--------------")

for par in paragraphs:
    print(par.select("i"))
