
import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text,"html.parser")

# print(soup.select(".toctext"))
# print(len(soup.select("p")))
# print(soup.select("text"))
gh_img=soup.select(".infobox-image a img")
print(gh_img[0])


print(f'''The sourcse of the image be :{gh_img[0].get("src")}''')
image_url="https:"+ gh_img[0].get("src")
print(image_url)

res=requests.get(image_url)
print(f'''The context of thta image be:{res.content}''')

with open("deepblue.jpg",mode="wb") as f:
    f.write(res.content)
