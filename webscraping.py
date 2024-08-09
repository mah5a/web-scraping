# load in libraries
import regex as re

import requests
from bs4 import BeautifulSoup as bs

# # load the web page content
# r = requests.get("https://keithgalli.github.io/web-scraping/example.html")
#
# # convert to a beautifulsoup object
# soup = bs(r.content, features="html.parser")
# # print out our HTML
# print(soup.prettify())
#
# # Start using BeautfulSoup to scrape
# # find() and find_all()
# first_header = soup.find("h2")
# print(first_header)
# headers = soup.find_all("h2")
# print(headers)
#
# # pass in a list of elements to look for the first element of the list
# print("--------------")
# find_header = soup.find(["h1", "h2"])
# print(find_header)
# print("--------------")
# # pass in a list of elements to look for all
# headers = soup.find_all(["h1", "h2"])
# print(headers)
# print("--------------")
# # pass in attributes to find/find_all
# paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
# print(paragraph)
# # you can nest calls
# print("--------------")
# body = soup.find("body")
# print(body)
# print("--------------")
# # look for div in body
# div = body.find("div")
# print(div)
# print("--------------")
# # find header in div
# header = div.find("h1")
# print(header)
# print("--------------")
# # search for EXACT specific string ex: some
# paragraphs = soup.find_all("p", string="Some bold text")
# print(paragraphs)
#
# print("--------------")
# # look for a string
#
#
# paragraph = soup.find_all("p", string=re.compile("Some"))
# print(paragraph)
#
# print("--------------")
# # find string with different capitalization
# headers = soup.find_all("h2", string=re.compile("(H|h)eader"))
# print(headers)
#
# print("********************--------------SELECT as in CSS-------------*******************")
#
# select = soup.select("p")
# print(select)
# print("--------------")
# content = soup.select("div p")
# print(content)
# print("--------------")
# paragraphs = soup.select("h2 ~ p")
# print(paragraphs)
# print("--------------")
# bold_text = soup.select("p#paragraph-id b")
# print(bold_text)
# print("--------------")
# print("direct decedent of a paragraph")
# paragraphs = soup.select("body > p")
# print(paragraphs)
# print("--------------")
#
# for par in paragraphs:
#     print(par.select("i"))
#
# print("------Align=middle--------")
# # Grab with specific property
# m = soup.select("[align = middle]")
# print(m)
# print("----Use .string ----------")
# header = soup.find("h2")
# print(header)
# print(header.string)
#
# print("---If multiple child elements use getText()-----------")
# div = soup.find("div")
# print(div.prettify())
# print(div.string)
# print(div.getText())
#
# print("------Get a specific property from an element--------")
# link = soup.find("a")
# print(link)
# print(link["href"])
# print("--------------")
# paragraphs = soup.select("p#paragraph-id")
# print(paragraphs[0]['id'])
# print("-------Path Syntax-------")
# link = soup.find("a")
# print(link)
# print(link['href'])
# print("--------")
# print(soup.body.find("div"))
# print("------------parent, sibling, child----------")
# print(soup.body.find("div").find_next_siblings())

print("+++++++++++++++++++++Let's Test Our Knowledge++++++++++++++++")
# load the web page content
r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
# r = requests.get("https://github.com/mah5a?tab=overview&from=2024-08-01&to=2024-08-05")

# convert to a beautifulsoup object
webpage = bs(r.content, features="html.parser")
# print out our HTML
print(webpage.prettify())

print("-----FIND SOCIAL LINKS:Method 1: SELECT->UL-----")
links = webpage.select('ul.socials a')
actual_links = [link['href'] for link in links]
print(actual_links)
print("-----FIND SOCIAL LINKS:Method 2: FIND-----")
ulist = webpage.find("ul", attrs={"class": "socials"})
links = ulist.find_all('a')
print(links)
actual_links = [link['href'] for link in links]
print(actual_links)

print("-----FIND SOCIAL LINKS:Method 1: SELECT->li-----")
links = webpage.select("li.social a")
print(links)

print("-----webscrape a Table on a web page-----")
table = webpage.select("table.hockey-stats")[0]
print(table)
