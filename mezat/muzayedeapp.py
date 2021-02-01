import requests
from bs4 import BeautifulSoup


class MuzayedeApp:
    base_url = "http://api.muzayedeapp.com/"

    def __init__(self, kw_list):
        self.kw_list = kw_list

    def check_product_exist(self):
        for kw in self.kw_list:
            headers = {"User-Agent": "Dart/2.10",
                       "Content-Type": "application/json", "x-version": "3"}
            payload = {
                "PageNumber": 1,
                "Count": 50,
                "Search": kw,
                "LotNo": 0,
                "TagId": 0,
                "SortType": 1,
                "LastId": 0,
                "AuctionCategoryId": 0
            }
            resp = requests.post(self.base_url + "api/Product/Search",
                                 json=payload,
                                 headers=headers)
            resp_data = resp.json()
            is_resp = True
            while True:
                if len(resp_data["Obj"]):
                    for product in resp_data["Obj"]:
                        print(product["Shop"]["Url"] + product["Url"][1:],
                              end=" --- ")
                        print(product["Name"])
                    payload["PageNumber"] += 1
                    is_resp = False
                    resp = requests.post(self.base_url + "api/Product/Search",
                                         json=payload, headers=headers)
                    resp_data = resp.json()
                else:
                    if is_resp:
                        print(kw + " YOK")
                    break
