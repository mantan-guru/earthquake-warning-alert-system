"""
MODUL GEMPA TERKINI
"""

#import modul
import time
import requests
from bs4 import BeautifulSoup
from itertools import chain

class GempaTerkini():

    def __init__(self, url):
        self.description = f'to get the last Earthquake in indonesia from {url}'
        self.result = None
        self.url = url

    def ekstraksi_data(self):
        """
        tanggal : 6 Januari 2023,
        waktu   : 19:20:12 WIB
        magnitudo : 4.3
        kedalaman   : 24 km
        lokasi  : LU = 2.19  - 97.86 BT
        pusat gempa : Pusat gempa berada di laut 17 km Tenggara Kabupaten Aceh Singkil
        dirasakan : Dirasakan (Skala MMI): II - III Singkil
        :return:
        """
        try:
            content = requests.get(self.url)
            print(content.status_code)
        except Exception:
            return None

        # print(soup.prettify())
        if content.status_code == 200:
            soup = BeautifulSoup(content.text, 'html.parser')
            date_time = soup.find("span", {"waktu"}).text.split(',')
            tanggal = date_time[0]
            waktu = date_time[1]
            i: int = 0
            magnitudo = None
            kedalaman = None
            ls  =  None
            bt = None
            lokasi = None
            pusat = None
            dirasakan = None
            result = soup.find("div", {"class" : "col-md-6 col-xs-6 gempabumi-detail no-padding"})
            results = result.findChildren("li")
            for result in results:

                if i == 1:
                    magnitudo = result.text
                elif i == 2:
                    kedalaman = result.text
                elif i == 3:
                    ls = result.text.split('-')[0]
                    bt = result.text.split('-')[1]
                elif i == 4:
                    lokasi = result.text
                elif i == 5:
                    dirasakan = result.text

                i = i + 1

            hasil = dict()
            hasil['tanggal'] = tanggal  #
            hasil['waktu'] = waktu #
            hasil['magnitudo'] = magnitudo
            hasil['kedalaman'] = kedalaman
            hasil['koordinat'] = {'ls' :  ls, 'bt' : bt }
            hasil['pusat'] = pusat
            hasil['lokasi'] = lokasi
            hasil['dirasakan'] = dirasakan

            hasil_comprehension = [result.text.split('\n') for result in results]
            convert_dimension = list(chain.from_iterable(hasil_comprehension))


            hasil_scraper = {'hasil' : hasil, 'hasil_comprehension' : convert_dimension }
            self.result = hasil_scraper

        else:
            return None




    def show_data(self):
        if self.result is None :
            print('data tidak ditemukan')
            return
        #
        print('Gempa terakhir berdasarkan BMKG tanpa List comprehension')
        print(f"tanggal =  {self.result['hasil']['tanggal']}")
        print(f"waktu  = {self.result['hasil']['waktu']}")
        print(f"Magnitudo = {self.result['hasil']['magnitudo']}")
        print(f"Koordinat LS = {self.result['hasil']['koordinat']['ls']} , BT =  {self.result['hasil']['koordinat']['bt']}")
        print(f"lokasi  = {self.result['hasil']['lokasi']}")
        print(f"dirasakan = {self.result['hasil']['dirasakan']}")
        print(time.time())

    def show_data_comprehension(self):
        print('\nGempa terakhir berdasarkan BMKG dengan List comprehension')
        dict_gempa = {'tanggal': 0, 'Magnitudo': 1, 'kedalaman': 2, 'Koordinate': 3, 'Lokasi': 4, 'dirasakan': 5}
        results = self.result['hasil_comprehension']
        i = 0
        for key, value in dict_gempa.items():
            print(f"{key} =  {results[value]}")

    def run(self):
        self.ekstraksi_data()
        self.show_data()
        self.show_data_comprehension()
