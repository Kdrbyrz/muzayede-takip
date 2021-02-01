import requests
from bs4 import BeautifulSoup


class CarsiMezat:
    base_url = "https://www.carsimezat.com/"

    def __init__(self, kw_list):
        self.kw_list = kw_list

    def check_product_exist(self):
        for kw in self.kw_list:
            resp = requests.get(self.base_url + "peyver?qtxt=" + kw)
            if "Aradığınız kriterlere uygun ürün bulunamadı!" not in resp.text:
                soup = BeautifulSoup(resp.text, 'html.parser')
                products = soup.find_all(class_='strip_all_tour_list')
                for product in products:
                    product_detail_wrapper = product.find(class_="tour_list_desc")
                    product_detail = product_detail_wrapper.find(class_="UrunFrame")
                    print(self.base_url + product_detail["href"], end=" --- ")
                    print(product_detail.get_text())
            else:
                print(kw + "YOK")
