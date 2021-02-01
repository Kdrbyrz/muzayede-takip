import requests

from bs4 import BeautifulSoup


class BitMezat:
    base_url = "https://www.bitmezat.com/"

    def __init__(self, kw_list):
        self.kw_list = kw_list

    def check_product_exist(self):
        for kw in self.kw_list:
            resp = requests.get(self.base_url + "ara?search=" + kw)
            if "Aradığınız kriterlerde bir lot bulunamadı." not in resp.text:
                soup = BeautifulSoup(resp.text, 'html.parser')
                products = soup.find_all(class_='item')
                for product in products:
                    product_detail_wrapper = product.find(class_="lot-content")
                    product_detail = product_detail_wrapper.find("a")
                    print(self.base_url + product_detail["href"], end=" --- ")
                    print(product_detail.get_text())
            else:
                print(kw + " YOK")
