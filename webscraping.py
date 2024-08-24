# load in libraries
import regex as re

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

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

print("------------------webscrape a Table on a web page--------------------")

table = webpage.select("table.hockey-stats")[0]
print(table)

columns = table.find("thead").find_all("th")
print(columns)

column_names = [c.string for c in columns]
print(column_names)
table_rows = table.find("tbody").find_all("tr")
l = []
for tr in table_rows:
    td = tr.find_all("td")
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)

print(l)

df = pd.DataFrame(l, columns=column_names)
print(df.head())

df.loc[df['Team'] != "Did not play"]
print("grab all fun facts that have the word --id--")

import re

facts = webpage.select("ul.fun-facts li")
print(facts)
facts_with_is = [fact.find(string=re.compile("is")) for fact in facts]
print(facts_with_is)
print("Getting rid of the NONEs--> list comprehension")
facts_with_is = [fact for fact in facts_with_is if fact]
print(facts_with_is)

print("with elements")
facts_with_is = [fact.find_parent() for fact in facts_with_is if fact]
print(facts_with_is)
print("get the whole sentence")
facts_with_is = [fact.find_parent().get_text() for fact in facts_with_is if fact]
print(facts_with_is)

print("download images on the webpage")
# pip install requests
url = "https://keithgalli.github.io/web-scraping/"
r = requests.get(url + "webpage.html")
webpage = bs(r.content, features="html.parser")
images = webpage.select("div.row div.column img")
image_url = images[0]['src']
print(image_url)
full_url = url + image_url

image_data = requests.get(full_url).content
with open('kale_como.jpg', 'wb') as handler:
    handler.write(image_data)

print("web scrape files")
files = webpage.select("div.block a")
print(files)

relative_file = [f['href'] for f in files]
print(relative_file)
url = "https://keithgalli.github.io/web-scraping/"
for f in relative_file:
    full_file_url = url+f
    # load the page
    page = requests.get(full_file_url)
    bs_page = bs(page.content)
    print(bs_page.body.prettify())
    break
