import requests

from bs4 import BeautifulSoup


class BayrakMezat:
    base_url = "https://www.bayrakmuzayede.com/"

    def __init__(self, kw_list):
        self.kw_list = kw_list

    def check_product_exist(self):
        for kw in self.kw_list:
            payload = {"search_words": kw}
            resp = requests.post(self.base_url + "tumurunler.html", payload)
            if '<h2 class="label label-danger">Sonuç Bulunmadı !</h2>' not in resp.text:
                soup = BeautifulSoup(resp.text, 'html.parser')
                products = soup.find_all(class_='p_img_container')
                for product in products:
                    product_detail = product.find("a")
                    print(product_detail["href"], end=" --- ")
                    print(product_detail.find("img")["alt"])
            else:
                print(kw + " YOK")
