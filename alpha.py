import requests
from bs4 import BeautifulSoup
import random
url = "https://alpha.wallhaven.cc/search?q="
tag = input("Enter the tag to search > ").replace(" ", "+").lower()
url = url + tag + "&search_image="
r = requests.get(url)
soup = BeautifulSoup(r.content, "html5lib")
img_list = list()
for ii in soup.body.find_all("figure"):
    img_list.append(ii["data-wallpaper-id"])
while(1):
    target = random.randint(0, len(img_list))
    if img_list[target] is not 'None':
        break
new_url = "https://alpha.wallhaven.cc/wallpaper/" + img_list[target]
new_r = requests.get(new_url)
new_soup = BeautifulSoup(new_r.content, "html5lib")
wall_src = new_soup.body.find("img", attrs={"id":"wallpaper"})["src"].replace("//", "https://")
img_data = requests.get(wall_src)
with open(tag+".jpg", "wb") as handler:
    handler.write(img_data.content)