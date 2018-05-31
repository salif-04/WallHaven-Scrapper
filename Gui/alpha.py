import requests
from bs4 import BeautifulSoup
import random

class alpha:

    def __init__(self):
        self.img_list = list()

    def get_all_img(self, tag):
        url = "https://alpha.wallhaven.cc/search?q=" + tag + "&search_image="
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html5lib")
        for ii in soup.body.find_all("figure"):
            self.img_list.append(ii["data-wallpaper-id"])

    def randomize_pic(self):
        if len(self.img_list) >0:
            while(1):
                target = random.randint(0, len(self.img_list)-1)
                if self.img_list[target] is not 'None':
                    break
            return self.img_list[target]
        else:
            return -1

    def get_img(self, target_img, tag):
        new_url = "https://alpha.wallhaven.cc/wallpaper/" + target_img
        new_r = requests.get(new_url)
        new_soup = BeautifulSoup(new_r.content, "html5lib")
        wall_src = new_soup.body.find("img", attrs={"id":"wallpaper"})["src"].replace("//", "https://")
        img_data = requests.get(wall_src)
        with open(tag+".jpg", "wb") as handler:
            handler.write(img_data.content)