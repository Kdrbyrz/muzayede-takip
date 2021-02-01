import requests
from bs4 import BeautifulSoup

from mezat.carsimezat import CarsiMezat


class MezatDukkani(CarsiMezat):
    base_url = "https://www.mezatdukkani.com//"
