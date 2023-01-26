"""
Aplikasi Deteksi Gempa Terkini
MODULARISASI DENGAN FUNCTION
"""


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
    hasil = dict()
    hasil['tanggal'] = '6 Januari 2023'
    hasil['waktu'] = '19:20:12 WIB'
    hasil['magnitudo'] = '4.3'
    hasil['kedalaman'] = '24 km'
    hasil['lokasi'] = {'lu': '2.19', 'bt': '97.86'}
    hasil['pusat'] = 'Pusat gempa berada di laut 17 km Tenggara Kabupaten Aceh Singkil'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II - III Singkil'

    return hasil



def show_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"lokasi LU = {result['lokasi']['lu']} , BT =  {result['lokasi']['bt']}")
    print(f"pusat {result['pusat']}")
    print(f"dirasakan {result['dirasakan']}")



if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    show_data(result)
