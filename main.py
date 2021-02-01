from mezat.bayrakmezat import BayrakMezat
from mezat.carsimezat import CarsiMezat
from mezat.mezatdukkani import MezatDukkani
from mezat.muzayedeapp import MuzayedeApp
from mezat.peramezat import PeraMezat

kw_list = []

class_list = [PeraMezat, CarsiMezat, MezatDukkani, BayrakMezat,
              MuzayedeApp]
for klass in class_list:
    klass(kw_list).check_product_exist()
