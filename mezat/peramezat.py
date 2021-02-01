import requests
from bs4 import BeautifulSoup


class PeraMezat:
    base_url = "https://www.peramezat.com/"

    def __init__(self, kw_list):
        self.kw_list = kw_list

    def check_product_exist(self):
        for kw in self.kw_list:
            resp = requests.get(self.base_url + "ara?ara=" + kw)
            if "Aradığınız kriterlerde sonuç bulunamadı!" not in resp.text:
                soup = BeautifulSoup(resp.text, 'html.parser')
                products = soup.find_all(class_='pey-detail')
                for product in products:
                    product_detail = product.find("a")
                    print(self.base_url + product_detail["href"], end=" --- ")
                    print(product_detail.get_text())
            else:
                print(kw + "YOK")
