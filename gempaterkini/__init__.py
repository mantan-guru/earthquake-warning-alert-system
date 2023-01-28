"""
MODUL GEMPA TERKINI
"""

#import modul
import requests
from bs4 import BeautifulSoup
def ekstraksi_data():
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
        content = requests.get('https://bmkg.go.id/')
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

        return hasil
    else:
        return None




def show_data(result):
    if result is None :
        print('data tidak ditemukan')
        return
    #
    # print(result)
    print('Gempa terakhir berdasarkan BMKG')
    print(f"tanggal =  {result['tanggal']}")
    print(f"waktu  = {result['waktu']}")
    print(f"Magnitudo = {result['magnitudo']}")
    print(f"Koordinat LS = {result['koordinat']['ls']} , BT =  {result['koordinat']['bt']}")
    print(f"lokasi  = {result['lokasi']}")
    # print(f"pusat {result['pusat']}")
    print(f"dirasakan = {result['dirasakan']}")


