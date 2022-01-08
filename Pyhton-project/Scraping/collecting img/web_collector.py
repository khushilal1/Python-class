import requests
import bs4

res=requests.get(f'''http://books.toscrape.com/catalogue/page-{"1"}.html''')
# print(response)
soup=bs4.BeautifulSoup(res.text,"html.parser")

img=soup.select(".image_container a img")
img_url=img[0].get("src")
print(img_url)
# res=requests.get(img_url)
# print(f'''The context of thta image be:{res.content}''')


# res=img_url.get()
# with open("collected_image.jpg",mode="wb") as f:
#     f.write(res.content)