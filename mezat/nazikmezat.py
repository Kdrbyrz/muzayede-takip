import requests

from bs4 import BeautifulSoup

from mezat.bitmezat import BitMezat


class NazikMezat(BitMezat):
    base_url = "https://www.nazikmezat.com/"
