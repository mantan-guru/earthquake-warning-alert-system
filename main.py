"""
Aplikasi Deteksi Gempa Terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE

"""
# from gempaterkini import ekstraksi_data, show_data
from src import  gempaterkini


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.show_data(result)
