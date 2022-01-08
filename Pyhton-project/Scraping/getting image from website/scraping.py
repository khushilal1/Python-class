# from types import resolve_bases
from bs4.element import ProcessingInstruction
from requests import *
import requests
# from requests.models import Response
url="https://www.example.com"
response=requests.get(url)
# result=requests.get(url)
# print(response)
# print(result)
# print(dir(result))
# print(type(result))
# print(dir(requests))  #gives all the class of request module
# print(response.text)


import bs4
# from bs4 import BeautifulSoup
# # print(dir(bs4))
soup=bs4.BeautifulSoup(response.text,"html.parser")
# # print(soup)
# print("...................................................")
# html_part=BeautifulSoup(response.text,"html.parser")
# # print(html_part)
# # print(type(html_part))

# print("the html value in the proeper indentataion")
# print(html_part.prettify())
# print("The head of selected url")
# print(soup.select("head"))

# print("..................................")
# print("The whole part inside the html")
# print(soup.select("html"))

# print("..................................")
# print("The whole part inside the head")
# print(soup.select("head"))


# print("....................................")
# print("The whole part inside the head")
# print(soup.select("tag"))
# print(type(soup.select("tag")))


# print(soup.select("tag"))
# # print(type(soup.select("tag")))


# print("GETTING THE HAED AND PAARGRAPH")
# print(soup.select("h1"))
# print(soup.select("h1")[0]) #getting the elemnt from the list using indexing
# print(soup.select("p"))

# import time
# print(len(soup.select("p")))
# for ele in range(len(soup.select("p"))):
#     print(f'''The element in "p" be" :{soup.select("p")[ele]}''')
#     print(f'''The text in "p" be" :{soup.select("p")[ele].getText()}''')
#     time.sleep(4)

# print(''' all the value from the  "p" printed  successfully''')










